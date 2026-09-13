#!/usr/bin/env python3
"""
Fix product images for INDTOOLS items.

ERPNext 16 renamed Item.website_image -> Item.image, and the Webshop
Website Item validate() clears website_image unless a matching Frappe "File"
record exists for the image URL. This script makes product images work
end-to-end for a fresh deployment:

  1. Copies the pre-built product images from the app's
     `indtools_pwa/public/frontend/products/` into the site's public files dir
     (so they are served at `/files/<CATEGORY>/<file>.png`).
  2. Creates a public "File" record for every image (so Website Item
     validation passes and thumbnails can be generated).
  3. Sets `Item.image` and `Website Item.website_image` to the `/files/...`
     URLs (using set_value so Webshop validation can't clear them).

Run from the bench sites directory:

    cd /path/to/bench/sites && /path/to/bench/env/bin/python /path/to/repo/deploy/apply_images.py

CWD must be the bench `sites` folder so the site path resolves correctly.
Works without numpy/PIL (pure stdlib copy + SQL updates).
"""
import os
import shutil

import frappe

SITE = os.environ.get("SITE", "order.indtools.in")
APP_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
PRODUCTS_SRC = os.path.join(APP_ROOT, "indtools_pwa", "public", "frontend", "products")

# Make Item codes unique & mirror setup_products.py (keep in sync)
import sys

sys.path.insert(0, os.path.join(APP_ROOT, "indtools_pwa"))
from setup_products import CATEGORIES, make_item_code  # noqa: E402

item_image = {}


def main():
    PUBLIC_FILES = os.path.join(frappe.get_site_path("public"), "files")
    os.makedirs(PUBLIC_FILES, exist_ok=True)

    # 1. Copy product images into site public/files/<CATEGORY>/
    for cat_key, cat in CATEGORIES.items():
        cat_dir = cat_key.upper().replace("-", "_")
        src_dir = os.path.join(PRODUCTS_SRC, cat_dir)
        dst_dir = os.path.join(PUBLIC_FILES, cat_dir)
        os.makedirs(dst_dir, exist_ok=True)
        for f in os.listdir(src_dir):
            shutil.copy2(os.path.join(src_dir, f), os.path.join(dst_dir, f))

    # Build item_code -> /files/ URL mapping
    for cat_key, cat in CATEGORIES.items():
        cat_dir = cat_key.upper().replace("-", "_")
        cat_url = f"/files/{cat_dir}/{os.path.basename(cat['image'])}"
        cat_code = cat_key.upper().replace("-", "")
        item_image.setdefault(cat_code, cat_url)
        for sub in cat["sub_products"]:
            code = make_item_code(cat_key, sub["name"])
            item_image[code] = f"/files/{cat_dir}/{os.path.basename(sub['image'])}"

    # 2. Create public File records (valid for /files/ URLs)
    created = 0
    for url in sorted(set(item_image.values())):
        if not frappe.db.exists("File", {"file_url": url}):
            frappe.get_doc(
                {
                    "doctype": "File",
                    "file_url": url,
                    "is_private": 0,
                    "file_name": os.path.basename(url),
                }
            ).insert(ignore_permissions=True, ignore_mandatory=True)
            created += 1
    frappe.db.commit()
    print("file records created ->", created)

    # 3. Set Item.image + Website Item.website_image (bypasses validation)
    upd_i = upd_w = 0
    for code, url in item_image.items():
        if frappe.db.exists("Item", code):
            frappe.db.set_value("Item", code, "image", url)
            upd_i += 1
        wid = frappe.db.get_value("Website Item", {"item_code": code}, "name")
        if wid:
            frappe.db.set_value("Website Item", wid, "website_image", url)
            upd_w += 1
    frappe.db.commit()
    print("items updated ->", upd_i, "website items updated ->", upd_w)
    nulls = frappe.db.sql(
        "select count(*) from `tabWebsite Item` where published=1 and (website_image is null or website_image='')"
    )
    print("website items still null ->", nulls)
    frappe.destroy()


if __name__ == "__main__":
    if not getattr(frappe.local, "conf", None):
        frappe.init(site=SITE, sites_path=os.getcwd())
        frappe.connect()
    main()