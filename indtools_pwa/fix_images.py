"""
fix_images.py
Copy product images from /mnt/data/indtools/public/ to the Frappe site's
public/files/ directory so they are accessible via /files/ URLs if the
asset paths aren't being served correctly.

Usage:
    bench --site order.indtools.in execute indtools_pwa.fix_images.fix_images
"""

import frappe
import os
import shutil

SOURCE_ROOT = "/mnt/data/indtools/public"
SITE_PUBLIC = os.path.join(
    frappe.get_site_path("public"), "files"
)

CATEGORY_DIRS = [
    "BOLTS", "NUTS", "WASHERS", "SCREWS", "RIVETS", "PINS",
    "SOCKET_PRODUCTS", "OTHER_PRODUCTS"
]


def fix_images():
    """Copy all product images into the site's public/files directory."""
    frappe.flags.in_test = False
    copied = 0
    skipped = 0
    errors = []

    print("=" * 60)
    print("Fix Images – Copying product images to site public/files")
    print("=" * 60)

    if not os.path.isdir(SOURCE_ROOT):
        print(f"[ERR] Source root not found: {SOURCE_ROOT}")
        return

    for category in CATEGORY_DIRS:
        src_dir = os.path.join(SOURCE_ROOT, category)
        if not os.path.isdir(src_dir):
            print(f"  [WARN] Source directory not found: {src_dir}")
            continue

        dest_dir = os.path.join(SITE_PUBLIC, category)
        os.makedirs(dest_dir, exist_ok=True)

        for fname in os.listdir(src_dir):
            src_file = os.path.join(src_dir, fname)
            dest_file = os.path.join(dest_dir, fname)

            if not os.path.isfile(src_file):
                continue

            if os.path.exists(dest_file):
                skipped += 1
                continue

            try:
                shutil.copy2(src_file, dest_file)
                copied += 1
                print(f"  [COPY] {category}/{fname}")
            except Exception as e:
                err = f"Error copying {category}/{fname}: {e}"
                print(f"  [ERR]  {err}")
                errors.append(err)

    # Also copy BANNERS and LOGO if they exist
    for extra_dir in ["BANNERS", "LOGO"]:
        src_dir = os.path.join(SOURCE_ROOT, extra_dir)
        if not os.path.isdir(src_dir):
            continue
        dest_dir = os.path.join(SITE_PUBLIC, extra_dir)
        os.makedirs(dest_dir, exist_ok=True)
        for fname in os.listdir(src_dir):
            src_file = os.path.join(src_dir, fname)
            dest_file = os.path.join(dest_dir, fname)
            if not os.path.isfile(src_file):
                continue
            if os.path.exists(dest_file):
                skipped += 1
                continue
            try:
                shutil.copy2(src_file, dest_file)
                copied += 1
                print(f"  [COPY] {extra_dir}/{fname}")
            except Exception as e:
                err = f"Error copying {extra_dir}/{fname}: {e}"
                print(f"  [ERR]  {err}")
                errors.append(err)

    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"  Copied:   {copied}")
    print(f"  Skipped:  {skipped}")
    print(f"  Errors:   {len(errors)}")
    if errors:
        print("\nError details:")
        for e in errors:
            print(f"  - {e}")
    print("=" * 60)

    # Rebuild assets so bench serve picks them up
    print("\nRunning 'bench build' to rebuild assets...")
    os.system("bench build")
    print("Done.")
