#!/usr/bin/env python3
"""
One-time ERPNext company setup for the INDTOOLS PWA.

Run inside the bench environment against your site:

    bench --site <your-site> console < deploy/setup_company.py

Runs the standard ERPNext setup wizard programmatically:
  - Company (default: INDTOOLS / ABBR / INR / India / Manufacturing domain)
  - Fiscal Year (default FY 2026-04-01 .. 2027-03-31)
  - Standard Chart of Accounts ("India - Chart of Accounts")
  - English language

After it runs, `setup_complete` is 1, so the site boots straight into the app.

NOTE: `erpnext.setup.setup_wizard.setup_wizard.setup_complete` is required
before product setup; it also provisions the default Item Groups, Price
Lists, Territory/Country, and the default "Standard Selling" price list.
"""
import frappe


def main(company_name="INDTOOLS", company_abbr="IND", currency="INR",
         country="India", fy_start="2026-04-01", fy_end="2027-03-31"):
    frappe.db.set_single_value("System Settings", "language", "en")
    frappe.db.set_single_value("System Settings", "country", country)
    frappe.db.set_default("language", "en")

    from erpnext.setup.setup_wizard.setup_wizard import setup_complete

    args = frappe._dict({
        "language": "en",
        "company_name": company_name,
        "company_abbr": company_abbr,
        "currency": currency,
        "country": country,
        "chart_of_accounts": f"{country} - Chart of Accounts",
        "domain": "Manufacturing",
        "fy_start_date": fy_start,
        "fy_end_date": fy_end,
    })
    setup_complete(args)
    frappe.db.commit()
    print("Company setup done")

    comp = frappe.db.get_value("Company", {"company_name": company_name}, "name")
    print("Company:", comp)
    print("All Item Groups:", frappe.db.exists("Item Group", "All Item Groups"))
    print("Standard Selling:", frappe.db.exists("Price List", "Standard Selling"))
    print("setup_complete:", frappe.db.get_single_value("System Settings", "setup_complete", fieldname="setup_complete") if False else frappe.db.get_value("System Settings", None, "setup_complete"))


if __name__ == "__main__":
    main()