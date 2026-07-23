import frappe

ITEM_GROUPS = [
    "Bolts", "Nuts", "Washers", "Screws", "Rivets", "Pins",
    "Socket Products", "Other Products"
]

CATEGORIES = {
    "bolts": {
        "item_group_name": "Bolts",
        "item_name": "Bolts",
        "description": "Durable bolts for all industrial applications",
        "size_range": "M3-M100",
        "grade": "4.6/8.8/10.9",
        "finishing": "ZINC PLATED",
        "web_description": "Our bolts are designed for strength and reliability in demanding industrial environments.",
        "image": "/assets/indtools_pwa/frontend/products/BOLTS/HEX_BOLT.png",
        "sub_products": [
            {"name": "Anchor Bolt", "image": "ANCHOR_BOLT.png"},
            {"name": "Bucket Bolt", "image": "BUCKET_BOLT.png"},
            {"name": "Carriage Bolt", "image": "CARRIAGE_BOLT.png"},
            {"name": "Eye Bolt", "image": "EYE_BOLT.png"},
            {"name": "Flange Bolt", "image": "FLANGE_BOLT.png"},
            {"name": "Foundation Bolt", "image": "FOUNDATION_BOLT.png"},
            {"name": "Hex Bolt", "image": "HEX_BOLT.png"},
            {"name": "High Tensile Bolts", "image": "HIGH_TENSILE_BOLTS.png"},
            {"name": "J Bolt", "image": "J_BOLT.png"},
            {"name": "T Bolt", "image": "T_BOLT.png"},
            {"name": "U Bolt", "image": "U_BOLT.png"},
        ],
    },
    "nuts": {
        "item_group_name": "Nuts",
        "item_name": "Nuts",
        "description": "High-quality nuts in various sizes and grades",
        "size_range": "M3-M100",
        "grade": "4.6/8.8/10.9",
        "finishing": "ZINC PLATED",
        "web_description": "Our nuts are manufactured to the highest standards and are available in various materials including carbon steel, stainless steel, and alloy steel.",
        "image": "/assets/indtools_pwa/frontend/products/NUTS/HEX_NUT.png",
        "sub_products": [
            {"name": "Cage Nut", "image": "CAGE_NUT.png"},
            {"name": "Castle Nut", "image": "CASTLE_NUT.png"},
            {"name": "Clinge Nut", "image": "CLINGE_NUT.png"},
            {"name": "Dome Nut", "image": "DOME_NUT.png"},
            {"name": "Flange Nut", "image": "FLANGE_NUT.png"},
            {"name": "Hex Nut", "image": "HEX_NUT.png"},
            {"name": "KM Nut", "image": "KM_Nut.png"},
            {"name": "LH Nut", "image": "LH_NUT.png"},
            {"name": "Lock Nut", "image": "LOCK_NUT.png"},
            {"name": "Long Nut", "image": "LONG_NUT.png"},
            {"name": "Nylock Nut", "image": "NYLOCK_NUT.png"},
            {"name": "Slotted Nut", "image": "SLOTTED_NUT.png"},
            {"name": "Square Nut", "image": "SQUARE-NUT-removebg-preview.png"},
            {"name": "Tee Nut", "image": "TEE_NUT.png"},
            {"name": "Weld Nut", "image": "WELD_NUT.png"},
            {"name": "Wing Nut", "image": "WING_NUT.png"},
            {"name": "Flange Nut (Special)", "image": "Untitled-design-1.png"},
        ],
    },
    "washers": {
        "item_group_name": "Washers",
        "item_name": "Washers",
        "description": "Precision washers for secure fastening",
        "size_range": "M3-M100",
        "grade": "4.6/8.8/10.9",
        "finishing": "ZINC PLATED",
        "web_description": "Precision engineered washers that provide optimal load distribution and prevent loosening.",
        "image": "/assets/indtools_pwa/frontend/products/WASHERS/PLAIN_WASHER.png",
        "sub_products": [
            {"name": "Fiber Washer", "image": "FIBER_WASHER.png"},
            {"name": "Hylam Washer", "image": "HYLAM_WASHER.png"},
            {"name": "Lock Washer", "image": "LOCK_WASHER.png"},
            {"name": "Plain Washer", "image": "PLAIN_WASHER.png"},
            {"name": "Polish Washer", "image": "POLISH_WASHER.png"},
            {"name": "Punch Washer", "image": "PUNCH_WASHER.png"},
            {"name": "Rubber Washer", "image": "RUBBER_WASHER.png"},
            {"name": "Spring Washer", "image": "SPRING_WASHER.png"},
            {"name": "Star Washer", "image": "STAR_WASHER.png"},
            {"name": "Taper Washer", "image": "TAPER_WASHER.png"},
            {"name": "Flat Washer", "image": "LOCK-WASHERS-removebg-preview.png"},
        ],
    },
    "screws": {
        "item_group_name": "Screws",
        "item_name": "Screws",
        "description": "High-quality screws for various applications",
        "size_range": "M3-M100",
        "grade": "4.6/8.8/10.9",
        "finishing": "ZINC PLATED",
        "web_description": "Wide variety of screws including machine screws, self-tapping screws, and wood screws.",
        "image": "/assets/indtools_pwa/frontend/products/SCREWS/MACHINE_SCREW.png",
        "sub_products": [
            {"name": "Clipboard Screw", "image": "CLIPBOARD_SCREW.png"},
            {"name": "Drywall Screw", "image": "DRYWALL_SCREW.png"},
            {"name": "Frame Fixing Screw", "image": "FRAME_FIXING_SCREW.png"},
            {"name": "Machine Screw", "image": "MACHINE_SCREW.png"},
            {"name": "Pan Head Screw", "image": "PAN_HEAD_SCREW.png"},
            {"name": "Phillip Head Screw", "image": "PHILLIP_HEAD_SCREW.png"},
            {"name": "Self Drilling Screw", "image": "SELF_DRILLING_SCREW.png"},
            {"name": "Self Tapping Screw", "image": "SELF_TAPPING_SCREW.png"},
            {"name": "Socket Head Screw", "image": "sCREW.png"},
            {"name": "Wood Screw", "image": "self_tapping-removebg-preview.png"},
        ],
    },
    "rivets": {
        "item_group_name": "Rivets",
        "item_name": "Rivets",
        "description": "Industrial rivets for permanent fastening",
        "size_range": "M3-M100",
        "grade": "Industrial Grade",
        "finishing": "ZINC PLATED",
        "web_description": "Solid and blind rivets for permanent fastening applications in various industries.",
        "image": "/assets/indtools_pwa/frontend/products/RIVETS/BLIND_RIVETS.png",
        "sub_products": [
            {"name": "Blind Rivets", "image": "BLIND_RIVETS.png"},
            {"name": "Hammer Drive", "image": "HAMMER_DRIVE.png"},
            {"name": "MS Rivets", "image": "MS_RIVETS.png"},
        ],
    },
    "pins": {
        "item_group_name": "Pins",
        "item_name": "Pins",
        "description": "Various types of pins for industrial use",
        "size_range": "M3-M100",
        "grade": "4.6/8.8/10.9",
        "finishing": "ZINC PLATED",
        "web_description": "Industrial pins including cotter pins, dowel pins, and taper pins for various applications.",
        "image": "/assets/indtools_pwa/frontend/products/PINS/COTTER_PIN.png",
        "sub_products": [
            {"name": "Cotter Pin", "image": "COTTER_PIN.png"},
            {"name": "Solid Dowel Pin", "image": "SOLID_DOWEL_PIN.png"},
            {"name": "Spring Dowel Pin", "image": "SPRING_DOWEL_PIN.png"},
        ],
    },
    "socket-products": {
        "item_group_name": "Socket Products",
        "item_name": "Socket Products",
        "description": "Allen Head CSK Allen Button Head Grub Screw",
        "size_range": "M3-M100",
        "grade": "4.6/8.8/10.9",
        "finishing": "ZINC PLATED",
        "web_description": "Complete range of socket head products including Allen bolts, button head screws, and grub screws.",
        "image": "/assets/indtools_pwa/frontend/products/SOCKET_PRODUCTS/ALLEN_HEAD.png",
        "sub_products": [
            {"name": "Allen Head", "image": "ALLEN_HEAD.png"},
            {"name": "Button Head Allen Screw", "image": "BUTTON_HEAD_ALLEN_SCREW.png"},
            {"name": "Countersunk Allen", "image": "COUNTERSUNK_ALLEN.png"},
            {"name": "Grub Screw", "image": "GRUB_SCREW.png"},
        ],
    },
    "other-products": {
        "item_group_name": "Other Products",
        "item_name": "Other Products",
        "description": "Additional industrial fasteners and tools",
        "size_range": "Various",
        "grade": "Industrial Grade",
        "finishing": "Standard",
        "web_description": "Additional fasteners and tools including clips, clamps, and specialty items.",
        "image": "/assets/indtools_pwa/frontend/products/OTHER_PRODUCTS/GASKETS.png",
        "sub_products": [
            {"name": "Conveyor Belt", "image": "CONVEYER_BELT.png"},
            {"name": "Gaskets", "image": "GASKETS.png"},
            {"name": "Rubber Sheet", "image": "RUBBER_SHEET.png"},
            {"name": "Steel Belt", "image": "STEEL_BELT.png"},
            {"name": "V Belt", "image": "V_BELT.png"},
        ],
    },
}


def make_item_code(category_key, sub_name):
    """Generate a unique item code from category and sub-product name."""
    prefix = category_key.upper().replace("-", "")[:3]
    clean = sub_name.upper().replace(" ", "-").replace("(", "").replace(")", "")
    return f"{prefix}-{clean}"


def setup_all():
    """Main entry point: create all item groups, category items, sub-products, and website items."""
    frappe.flags.in_test = False
    created_groups = 0
    created_items = 0
    created_website_items = 0
    skipped = 0
    errors = []

    print("=" * 60)
    print("INDTOOLS Product Setup")
    print("=" * 60)

    # 1. Create Item Groups
    print("\n--- Creating Item Groups ---")
    for group_name in ITEM_GROUPS:
        try:
            if frappe.db.exists("Item Group", group_name):
                print(f"  [SKIP] Item Group '{group_name}' already exists")
                skipped += 1
                continue
            ig = frappe.new_doc("Item Group")
            ig.item_group_name = group_name
            ig.parent_item_group = "All Item Groups"
            ig.insert(ignore_permissions=True)
            frappe.db.commit()
            print(f"  [OK]   Item Group '{group_name}' created")
            created_groups += 1
        except Exception as e:
            err = f"Error creating Item Group '{group_name}': {e}"
            print(f"  [ERR]  {err}")
            errors.append(err)

    # 2. Create category-level items and website items, then sub-products
    print("\n--- Creating Products ---")
    for cat_key, cat in CATEGORIES.items():
        group = cat["item_group_name"]

        # Category-level item
        cat_code = cat_key.upper().replace("-", "")
        try:
            if not frappe.db.exists("Item", cat_code):
                item = frappe.new_doc("Item")
                item.item_code = cat_code
                item.item_name = cat["item_name"]
                item.item_group = group
                item.description = cat["description"]
                item.website_image = cat["image"]
                item.insert(ignore_permissions=True)
                frappe.db.commit()
                print(f"  [OK]   Category Item '{cat['item_name']}' created")
                created_items += 1
            else:
                print(f"  [SKIP] Category Item '{cat['item_name']}' already exists")
                skipped += 1

            # Category-level Website Item
            cat_web_name = cat["item_name"]
            if not frappe.db.exists("Website Item", {"item_code": cat_code}):
                wi = frappe.new_doc("Website Item")
                wi.web_item_name = cat_web_name
                wi.item_code = cat_code
                wi.item_group = group
                wi.description = cat["web_description"]
                wi.web_long_description = cat["web_description"]
                wi.website_image = cat["image"]
                wi.published = 1
                wi.set_meta_tags = 0
                wi.append("website_specifications", {
                    "label": "Size Range",
                    "description": cat["size_range"],
                })
                wi.append("website_specifications", {
                    "label": "Grade",
                    "description": cat["grade"],
                })
                wi.append("website_specifications", {
                    "label": "Finishing",
                    "description": cat["finishing"],
                })
                wi.insert(ignore_permissions=True)
                frappe.db.commit()
                print(f"  [OK]   Website Item '{cat_web_name}' created")
                created_website_items += 1
            else:
                print(f"  [SKIP] Website Item '{cat_web_name}' already exists")
                skipped += 1
        except Exception as e:
            err = f"Error in category '{cat_key}': {e}"
            print(f"  [ERR]  {err}")
            errors.append(err)

        # Sub-products
        for sub in cat["sub_products"]:
            sub_name = sub["name"]
            sub_image = f"/assets/indtools_pwa/frontend/products/{cat_key.upper().replace('-', '_')}/{sub['image']}"
            item_code = make_item_code(cat_key, sub_name)

            try:
                # Item
                if not frappe.db.exists("Item", item_code):
                    item = frappe.new_doc("Item")
                    item.item_code = item_code
                    item.item_name = sub_name
                    item.item_group = group
                    item.description = cat["description"]
                    item.website_image = sub_image
                    item.insert(ignore_permissions=True)
                    frappe.db.commit()
                    created_items += 1
                else:
                    skipped += 1

                # Website Item
                if not frappe.db.exists("Website Item", {"item_code": item_code}):
                    wi = frappe.new_doc("Website Item")
                    wi.web_item_name = sub_name
                    wi.item_code = item_code
                    wi.item_group = group
                    wi.description = cat["web_description"]
                    wi.web_long_description = cat["web_description"]
                    wi.website_image = sub_image
                    wi.published = 1
                    wi.set_meta_tags = 0
                    wi.append("website_specifications", {
                        "label": "Size Range",
                        "description": cat["size_range"],
                    })
                    wi.append("website_specifications", {
                        "label": "Grade",
                        "description": cat["grade"],
                    })
                    wi.append("website_specifications", {
                        "label": "Finishing",
                        "description": cat["finishing"],
                    })
                    wi.insert(ignore_permissions=True)
                    frappe.db.commit()
                    created_website_items += 1
                    print(f"  [OK]   {sub_name} ({item_code})")
                else:
                    skipped += 1
                    print(f"  [SKIP] {sub_name} ({item_code})")
            except Exception as e:
                err = f"Error creating '{sub_name}': {e}"
                print(f"  [ERR]  {err}")
                errors.append(err)

    # Summary
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"  Item Groups created:    {created_groups}")
    print(f"  Items created:          {created_items}")
    print(f"  Website Items created:  {created_website_items}")
    print(f"  Skipped (existing):     {skipped}")
    print(f"  Errors:                 {len(errors)}")
    if errors:
        print("\nError details:")
        for e in errors:
            print(f"  - {e}")
    print("=" * 60)
    print("Done.")
