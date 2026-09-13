#!/usr/bin/env python3
"""
Configure Webshop Settings + create Item Prices for all INDTOOLS items.

Run from the bench `sites` directory (auto-connects against the site in
`SITE`, default `order.indtools.in`):

    cd /path/to/bench/sites && /path/to/bench/env/bin/python /path/to/Indtools-PWA/deploy/setup_webshop.py

or inside the bench environment (site already connected — the auto-init below
is skipped):

    bench --site <your-site> console < deploy/setup_webshop.py

This creates/corrects:
  - Webshop Settings (enabled, checkout enabled, company, "Standard Selling"
    price list, "Individual" default customer group, SAL-QTN- quotation series)
  - An Item Price on "Standard Selling" for every non-"All Item Groups" item.
    Prices are deterministic (25..220 INR in steps of 5, seeded from the item
    code) so every deployment has identical prices.
"""
import hashlib
import os

import frappe

SITE = os.environ.get("SITE", "order.indtools.in")

PRICE_LIST = "Standard Selling"
CURRENCY = "INR"
QUOTATION_SERIES = "SAL-QTN-"
DEFAULT_CUSTOMER_GROUP = "Individual"


def main():
    ws = frappe.get_single("Webshop Settings")
    ws.enabled = 1
    ws.enable_checkout = 1
    ws.show_price = 1
    ws.show_stock_availability = 1
    ws.allow_items_not_in_stock = 1
    ws.show_apply_coupon_code_in_website = 0
    ws.company = (
        frappe.db.get_single_value("Global Defaults", "default_company")
        or frappe.db.get_value("Company", {}, "name")
    )
    ws.price_list = PRICE_LIST

    if not frappe.db.exists("Customer Group", DEFAULT_CUSTOMER_GROUP):
        frappe.get_doc(
            {"doctype": "Customer Group", "customer_group_name": DEFAULT_CUSTOMER_GROUP}
        ).insert(ignore_permissions=True)
    ws.default_customer_group = DEFAULT_CUSTOMER_GROUP
    ws.quotation_series = QUOTATION_SERIES
    ws.save(ignore_permissions=True)
    frappe.db.commit()
    print("Webshop Settings configured:", ws.company, ws.price_list)

    items = frappe.get_all("Item", filters={"item_group": ["!=", "All Item Groups"]}, pluck="name")
    made = skipped = 0
    for code in items:
        if frappe.db.exists("Item Price", {"item_code": code, "price_list": PRICE_LIST}):
            skipped += 1
            continue
        h = int(hashlib.md5(code.encode()).hexdigest(), 16)
        price = 25 + (h % 40) * 5  # 25..220 INR in 5s
        frappe.get_doc(
            {
                "doctype": "Item Price",
                "item_code": code,
                "price_list": PRICE_LIST,
                "price_list_rate": price,
                "currency": CURRENCY,
                "selling": 1,
            }
        ).insert(ignore_permissions=True)
        made += 1
    frappe.db.commit()
    print("Item Prices created:", made, "| skipped (already exist):", skipped)
    print("Published website items:", frappe.db.count("Website Item", {"published": 1}))


if __name__ == "__main__":
    if not getattr(frappe.local, "conf", None):
        frappe.init(site=SITE, sites_path=os.getcwd())
        frappe.connect()
    main()