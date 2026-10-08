"""Import the Kaloti precision catalog into Frappe (Items + Website Items).

Replaces the generic placeholder data for the 33 matched items, creates the
37 new Kaloti items, moves 8 legacy items into the right groups, wires real
product photos and deterministic Standard Selling prices.

Idempotent: safe to re-run. Run with:
    bench --site order.indtools.in console < indtools_pwa/setup_kaloti_products.py

Requires the frontend to be built first so images exist in either:
    indtools_pwa/public/frontend/products/KALOTI/   (vite build output), or
    frontend/public/products/KALOTI/                (source)
"""
import hashlib
import json
import os
import shutil

import frappe
from frappe.utils import escape_html

APP_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CATALOG_PATH = os.path.join(APP_ROOT, "indtools_pwa", "kaloti_catalog.json")
IMG_CANDIDATES = [
    os.path.join(APP_ROOT, "indtools_pwa", "public", "frontend", "products", "KALOTI"),
    os.path.join(APP_ROOT, "frontend", "public", "products", "KALOTI"),
]

PRICE_LIST = "Standard Selling"
FILES_SUBDIR = "kaloti"


def load_catalog():
    with open(CATALOG_PATH) as f:
        return json.load(f)


def find_img_dir():
    for d in IMG_CANDIDATES:
        if os.path.isdir(d) and os.listdir(d):
            return d
    frappe.throw(f"Kaloti images not found. Run the frontend build first. Checked: {IMG_CANDIDATES}")


def long_html(p):
    parts = [f"<p>{escape_html(p['short'])}</p>"]
    if p["standards"]:
        parts.append("<h4>Standards</h4><ul>")
        parts += [f"<li>{escape_html(s)}</li>" for s in p["standards"]]
        parts.append("</ul>")
    if p["dimensions"]:
        parts.append("<h4>Dimensions &amp; Weights</h4><ul>")
        parts += [f"<li>{escape_html(s)}</li>" for s in p["dimensions"]]
        parts.append("</ul>")
    for cf in p["chart_files"]:
        parts.append(
            f'<p><img src="/files/{FILES_SUBDIR}/{cf}" '
            f'alt="{escape_html(p["title"])} dimensions chart" style="max-width:100%"/></p>'
        )
    parts.append(f'<p><small>Source: <a href="{p["url"]}" target="_blank">Kaloti India</a></small></p>')
    return "".join(parts)


def spec_rows(group_meta, p):
    std = " | ".join(p["standards"])[:500] or group_meta.get("grade", "")
    size = " | ".join(p["dimensions"])[:500] or ", ".join(p.get("sizes", [])) or group_meta.get("size_range", "")
    return [
        ("Size Range", size or "Standard"),
        ("Grade", group_meta.get("grade", "")),
        ("Finishing", group_meta.get("finishing", "")),
        ("Standard", std or "As per DIN / ISO"),
    ]


def set_website_item(doc, group_meta, p, img_url):
    doc.web_item_name = p["title"]
    doc.item_group = p["group"]
    doc.description = p["short"]
    doc.short_description = p["short"][:1000]
    doc.web_long_description = long_html(p)
    doc.published = 1
    doc.set("website_specifications", [])
    for label, desc in spec_rows(group_meta, p):
        doc.append("website_specifications", {"label": label, "description": desc})
    doc.save(ignore_permissions=True)
    # set via db to bypass Webshop image validation (File record created first)
    frappe.db.set_value("Website Item", doc.name, "website_image", img_url)


def setup_all():
    frappe.flags.in_test = False
    catalog = load_catalog()
    groups = {g["name"]: g for g in catalog["groups"]}
    products = [p for g in catalog["groups"] for p in g["products"]]
    assert len(products) == 70, f"catalog must hold 70 products, has {len(products)}"

    stats = {"groups": 0, "updated": 0, "created": 0, "moved": 0, "prices": 0, "files": 0}
    errors = []

    print("=" * 60)
    print("INDTOOLS Kaloti catalog import (70 products)")
    print("=" * 60)

    # 1. Item Groups
    for name in groups:
        try:
            if frappe.db.exists("Item Group", name):
                continue
            ig = frappe.new_doc("Item Group")
            ig.item_group_name = name
            ig.parent_item_group = "All Item Groups"
            ig.insert(ignore_permissions=True)
            stats["groups"] += 1
            print(f"  [OK] Item Group '{name}'")
        except Exception as e:
            errors.append(f"group {name}: {e}")
    frappe.db.commit()

    # 2. Images -> site files + File records (attached: mains to Item,
    # charts to Website Item — unattached File rows get garbage-collected)
    img_dir = find_img_dir()
    public_files = os.path.join(frappe.get_site_path("public"), "files", FILES_SUBDIR)
    os.makedirs(public_files, exist_ok=True)
    needed = {}
    for p in products:
        wid = frappe.db.get_value("Website Item", {"item_code": p["item_code"]}, "name")
        needed[p["main_file"]] = ("Item", p["item_code"])
        for cf in p["chart_files"]:
            needed[cf] = ("Website Item", wid)
    for fname, (att_dt, att_dn) in needed.items():
        src = os.path.join(img_dir, fname)
        if not os.path.exists(src):
            errors.append(f"missing image file: {fname}")
            continue
        dst = os.path.join(public_files, fname)
        if not os.path.exists(dst) or os.path.getsize(dst) != os.path.getsize(src):
            shutil.copy2(src, dst)
        url = f"/files/{FILES_SUBDIR}/{fname}"
        if not frappe.db.exists("File", {"file_url": url}):
            frappe.get_doc({
                "doctype": "File", "file_url": url, "is_private": 0,
                "file_name": fname, "attached_to_doctype": att_dt,
                "attached_to_name": att_dn,
            }).insert(ignore_permissions=True, ignore_mandatory=True)
            stats["files"] += 1
        else:
            # ensure attachment (unattached rows do not survive)
            row = frappe.db.get_value("File", {"file_url": url}, ["name", "attached_to_name"], as_dict=True)
            if row and not row.attached_to_name and att_dn:
                frappe.db.set_value("File", row.name, {
                    "attached_to_doctype": att_dt, "attached_to_name": att_dn})
    frappe.db.commit()
    print(f"  images/files ready ({len(needed)} files, {stats['files']} new File records)")

    # 3. Items + Website Items
    for p in products:
        meta = groups[p["group"]]
        img_url = f"/files/{FILES_SUBDIR}/{p['main_file']}"
        try:
            if frappe.db.exists("Item", p["item_code"]):
                frappe.db.set_value("Item", p["item_code"], {
                    "item_name": p["title"],
                    "item_group": p["group"],
                    "description": p["short"] + (
                        "\n\nStandards: " + " | ".join(p["standards"]) if p["standards"] else ""
                    ),
                    "image": img_url,
                })
                stats["updated"] += 1
                action = "UPD"
            else:
                item = frappe.new_doc("Item")
                item.item_code = p["item_code"]
                item.item_name = p["title"]
                item.item_group = p["group"]
                item.description = p["short"] + (
                    "\n\nStandards: " + " | ".join(p["standards"]) if p["standards"] else ""
                )
                item.image = img_url
                item.insert(ignore_permissions=True)
                stats["created"] += 1
                action = "NEW"

            wid = frappe.db.get_value("Website Item", {"item_code": p["item_code"]}, "name")
            if wid:
                set_website_item(frappe.get_doc("Website Item", wid), meta, p, img_url)
            else:
                wi = frappe.new_doc("Website Item")
                wi.item_code = p["item_code"]
                wi.item_group = p["group"]
                set_website_item(wi, meta, p, img_url)
            frappe.db.commit()
            print(f"  [{action}] {p['item_code']} :: {p['title'][:60]}")
        except Exception as e:
            frappe.db.rollback()
            errors.append(f"{p['item_code']}: {e}")
            print(f"  [ERR] {p['item_code']}: {e}")

    # 4. Legacy moves (keep name/data, fix group)
    for m in catalog["moves"]:
        try:
            if frappe.db.exists("Item", m["item_code"]):
                frappe.db.set_value("Item", m["item_code"], "item_group", m["group"])
                wid = frappe.db.get_value("Website Item", {"item_code": m["item_code"]}, "name")
                if wid:
                    frappe.db.set_value("Website Item", wid, "item_group", m["group"])
                stats["moved"] += 1
                print(f"  [MOV] {m['item_code']} -> {m['group']}")
        except Exception as e:
            errors.append(f"move {m['item_code']}: {e}")
    frappe.db.commit()

    # 5. Prices for items missing Standard Selling
    for p in products:
        try:
            if frappe.db.exists("Item Price", {"item_code": p["item_code"], "price_list": PRICE_LIST}):
                continue
            h = int(hashlib.md5(p["item_code"].encode()).hexdigest(), 16)
            frappe.get_doc({
                "doctype": "Item Price", "item_code": p["item_code"],
                "price_list": PRICE_LIST, "price_list_rate": 25 + (h % 40) * 5,
                "currency": "INR", "selling": 1,
            }).insert(ignore_permissions=True)
            stats["prices"] += 1
        except Exception as e:
            errors.append(f"price {p['item_code']}: {e}")
    frappe.db.commit()

    # 6. Unpublish category placeholders of groups left empty
    for code in ("BOLTS", "PINS", "SOCKETPRODUCTS"):
        try:
            grp = frappe.db.get_value("Item", code, "item_group")
            n = frappe.db.count("Item", {"item_group": grp}) if grp else 0
            if n <= 1:
                wid = frappe.db.get_value("Website Item", {"item_code": code}, "name")
                if wid:
                    frappe.db.set_value("Website Item", wid, "published", 0)
                    print(f"  [UNPUB] placeholder {code} (group '{grp}' now empty)")
        except Exception as e:
            errors.append(f"unpublish {code}: {e}")
    frappe.db.commit()

    print("=" * 60)
    print(f"  groups created: {stats['groups']} | items updated: {stats['updated']} | "
          f"created: {stats['created']} | moved: {stats['moved']}")
    print(f"  prices: {stats['prices']} | file records: {stats['files']} | errors: {len(errors)}")
    for e in errors:
        print(f"  - {e}")
    print("Done.")


if __name__ == "__main__":
    setup_all()


def verify_kaloti():
    """Print a JSON health snapshot (use with `bench --site X execute`)."""
    nulls = frappe.db.sql(
        "select count(*) from `tabWebsite Item` "
        "where published=1 and (website_image is null or website_image='')"
    )[0][0]
    print(json.dumps({
        "items": frappe.db.count("Item"),
        "published_website_items": frappe.db.count("Website Item", {"published": 1}),
        "kaloti_file_records": frappe.db.count("File", {"file_url": ["like", "/files/kaloti/%"]}),
        "published_without_image": nulls,
    }))


def repair_images():
    """Dedupe /files/kaloti File records, backfill missing ones, re-pin images
    + thumbnails via set_value (immune to Webshop validate/make_thumbnail).

    Use with `bench --site X execute indtools_pwa.setup_kaloti_products.repair_images`.
    """
    catalog = load_catalog()
    products = [p for g in catalog["groups"] for p in g["products"]]
    urls = {f"/files/{FILES_SUBDIR}/{p['main_file']}" for p in products}
    urls |= {f"/files/{FILES_SUBDIR}/{cf}" for p in products for cf in p["chart_files"]}

    # dedupe File records (keep oldest per URL)
    for url in urls:
        rows = frappe.db.get_all("File", filters={"file_url": url}, pluck="name", order_by="creation asc")
        for extra in rows[1:]:
            frappe.delete_doc("File", extra, ignore_permissions=True)
    # backfill missing (attached — unattached rows do not survive)
    made = 0
    for p in products:
        wid = frappe.db.get_value("Website Item", {"item_code": p["item_code"]}, "name")
        pairs = [(p["main_file"], "Item", p["item_code"])] + \
                [(cf, "Website Item", wid) for cf in p["chart_files"]]
        for fname, att_dt, att_dn in pairs:
            url = f"/files/{FILES_SUBDIR}/{fname}"
            if not frappe.db.exists("File", {"file_url": url}):
                frappe.get_doc({
                    "doctype": "File", "file_url": url, "is_private": 0,
                    "file_name": fname, "attached_to_doctype": att_dt,
                    "attached_to_name": att_dn,
                }).insert(ignore_permissions=True, ignore_mandatory=True)
                made += 1
            else:
                row = frappe.db.get_value("File", {"file_url": url},
                                          ["name", "attached_to_name"], as_dict=True)
                if row and not row.attached_to_name and att_dn:
                    frappe.db.set_value("File", row.name, {
                        "attached_to_doctype": att_dt, "attached_to_name": att_dn})
    # re-pin image + thumbnail on all 70 website items
    pinned = 0
    for p in products:
        img = f"/files/{FILES_SUBDIR}/{p['main_file']}"
        wid = frappe.db.get_value("Website Item", {"item_code": p["item_code"]}, "name")
        if wid:
            frappe.db.set_value("Website Item", wid, {"website_image": img, "thumbnail": img})
            pinned += 1
    frappe.db.commit()
    print(json.dumps({"file_records_created": made, "website_items_pinned": pinned}))
