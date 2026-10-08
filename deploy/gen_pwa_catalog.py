"""Generate frontend/src/data/categories.js from kaloti_catalog.json + legacy leftovers.

Single source of truth for the PWA catalog; Frappe Items carry the same
names/codes/images (see indtools_pwa/setup_kaloti_products.py).
"""
import json
import os

APP_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CATALOG = json.load(open(os.path.join(APP_ROOT, "indtools_pwa", "kaloti_catalog.json")))
OUT = os.path.join(APP_ROOT, "frontend", "src", "data", "categories.js")
PRODUCT_BASE = "/assets/indtools_pwa/frontend/products"

# legacy leftovers: (item_code, name, dir, file) — kept as-is from old catalog
LEGACY = {
    "Bolts / Screws": [
        ("BOL-BUCKET-BOLT", "Bucket Bolt", "BOLTS", "BUCKET_BOLT.png"),
        ("BOL-EYE-BOLT", "Eye Bolt", "BOLTS", "EYE_BOLT.png"),
        ("BOL-FOUNDATION-BOLT", "Foundation Bolt", "BOLTS", "FOUNDATION_BOLT.png"),
        ("BOL-J-BOLT", "J Bolt", "BOLTS", "J_BOLT.png"),
        ("BOL-T-BOLT", "T Bolt", "BOLTS", "T_BOLT.png"),
        ("BOL-U-BOLT", "U Bolt", "BOLTS", "U_BOLT.png"),
    ],
    "Nuts": [
        ("NUT-CASTLE-NUT", "Castle Nut", "NUTS", "CASTLE_NUT.png"),
        ("NUT-KM-NUT", "KM Nut", "NUTS", "KM_Nut.png"),
        ("NUT-LH-NUT", "LH Nut", "NUTS", "LH_NUT.png"),
        ("NUT-LONG-NUT", "Long Nut", "NUTS", "LONG_NUT.png"),
        ("NUT-SLOTTED-NUT", "Slotted Nut", "NUTS", "SLOTTED_NUT.png"),
        ("NUT-SQUARE-NUT", "Square Nut", "NUTS", "SQUARE-NUT-removebg-preview.png"),
    ],
    "Washers": [
        ("WAS-FIBER-WASHER", "Fiber Washer", "WASHERS", "FIBER_WASHER.png"),
        ("WAS-HYLAM-WASHER", "Hylam Washer", "WASHERS", "HYLAM_WASHER.png"),
        ("WAS-POLISH-WASHER", "Polish Washer", "WASHERS", "POLISH_WASHER.png"),
        ("WAS-PUNCH-WASHER", "Punch Washer", "WASHERS", "PUNCH_WASHER.png"),
        ("WAS-RUBBER-WASHER", "Rubber Washer", "WASHERS", "RUBBER_WASHER.png"),
    ],
    "Screws": [
        ("SCR-CLIPBOARD-SCREW", "Clipboard Screw", "SCREWS", "CLIPBOARD_SCREW.png"),
        ("SCR-MACHINE-SCREW", "Machine Screw", "SCREWS", "MACHINE_SCREW.png"),
        ("SCR-PHILLIP-HEAD-SCREW", "Phillip Head Screw", "SCREWS", "PHILLIP_HEAD_SCREW.png"),
        ("SCR-SELF-TAPPING-SCREW", "Self Tapping Screw", "SCREWS", "SELF_TAPPING_SCREW.png"),
        ("SCR-WOOD-SCREW", "Wood Screw", "SCREWS", "self_tapping-removebg-preview.png"),
    ],
    "Rivets": [
        ("RIV-HAMMER-DRIVE", "Hammer Drive", "RIVETS", "HAMMER_DRIVE.png"),
        ("RIV-MS-RIVETS", "MS Rivets", "RIVETS", "MS_RIVETS.png"),
    ],
    "Socket Screws": [
        ("SOC-ALLEN-HEAD", "Allen Head", "SOCKET_PRODUCTS", "ALLEN_HEAD.png"),
    ],
    "Circlip & Dowell Pins": [
        ("PIN-SOLID-DOWEL-PIN", "Solid Dowel Pin", "PINS", "SOLID_DOWEL_PIN.png"),
    ],
    "Other Products": [
        ("OTH-CONVEYOR-BELT", "Conveyor Belt", "OTHER_PRODUCTS", "CONVEYER_BOLT.png"),
        ("OTH-GASKETS", "Gaskets", "OTHER_PRODUCTS", "GASKETS.png"),
        ("OTH-RUBBER-SHEET", "Rubber Sheet", "OTHER_PRODUCTS", "RUBBER_SHEET.png"),
        ("OTH-STEEL-BELT", "Steel Belt", "OTHER_PRODUCTS", "STEEL_BELT.png"),
        ("OTH-V-BELT", "V Belt", "OTHER_PRODUCTS", "V_BELT.png"),
    ],
}
LEGACY_META = {
    "Rivets": {"icon": "🔗", "description": "Blind / pop rivets for permanent sheet fastening",
               "long": "Aluminium blind (pop) rivets plus MS rivets and hammer-drive rivets for fast, permanent fastening of sheet metal and industrial assemblies.",
               "grade": "ALUMINIUM", "grades": ["Aluminium", "Steel", "Stainless Steel"],
               "finishing": "PLAIN", "finishes": ["Plain", "Zinc Plated"]},
    "Other Products": {"icon": "📦", "description": "Belts, gaskets and rubber products",
               "long": "Industrial consumables — conveyor belts, V belts, steel belts, gaskets and rubber sheets — for plant maintenance and OEM needs.",
               "grade": "INDUSTRIAL", "grades": ["Standard", "Heavy Duty", "Premium"],
               "finishing": "STANDARD", "finishes": ["Standard"]},
}

EXTRA_GROUPS = ["Other Products"]

def js(s):
    return json.dumps(s, ensure_ascii=False)

lines = []
lines.append("export const PRODUCT_BASE = '/assets/indtools_pwa/frontend/products'")
lines.append("")
lines.append("export const WHATSAPP_NUMBER = '+919898855350'")
lines.append("")
lines.append("function makeRoute(name) {")
lines.append("  return name.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '')")
lines.append("}")
lines.append("")
lines.append("export const categories = [")

def cat_id(name):
    return {"Bolts / Screws": "bolts-screws"}.get(name,
        name.lower().replace(" & ", "-").replace(" / ", "-").replace(" ", "-"))

for g in CATALOG["groups"] + [{"name": n, **LEGACY_META[n], "products": [], "size_options": [],
                                "image_product": None} for n in EXTRA_GROUPS]:
    name = g["name"]
    cid = cat_id(name)
    prods = list(g["products"])
    # append legacy leftovers into their groups
    for code, lname, d, f in LEGACY.get(name, []):
        prods.append({"__legacy__": True, "item_code": code, "title": lname,
                      "img": f"{PRODUCT_BASE}/{d}/{f}", "short": g.get("long", g.get("description", "")),
                      "standards": [], "dimensions": [], "sizes": []})
    # category image: first Kaloti product, else first legacy
    first_img = None
    for p in prods:
        if not p.get("__legacy__"):
            first_img = f"{PRODUCT_BASE}/KALOTI/{p['main_file']}"
            break
    if not first_img and prods:
        first_img = prods[0]["img"]
    sizes = g.get("size_options", []) or []
    if all(s.startswith("M") for s in sizes) and len(sizes) > 1 and "Inch" not in str(sizes):
        size_range = f"{sizes[0]} – {sizes[-1]}"
    else:
        size_range = ", ".join(sizes) if sizes else "Various"
    grades = g.get("grades", ["Industrial"])
    finishes = g.get("finishes", ["Standard"])
    lines.append("  {")
    lines.append(f"    id: {js(cid)},")
    lines.append(f"    slug: {js(cid)},")
    lines.append(f"    name: {js(name)},")
    lines.append(f"    icon: {js(g.get('icon', '🔩'))},")
    lines.append(f"    description: {js(g.get('description', ''))},")
    lines.append(f"    longDescription: {js(g.get('long', g.get('description', '')))},")
    lines.append(f"    image: {js(first_img)},")
    lines.append(f"    sizeRange: {js(size_range)},")
    lines.append(f"    sizeOptions: {js(sizes or ['Standard'])},")
    lines.append(f"    grade: {js(g.get('grade', 'Industrial'))},")
    lines.append(f"    gradeOptions: {js(grades)},")
    lines.append(f"    finishing: {js(g.get('finishing', 'Standard'))},")
    lines.append(f"    finishOptions: {js(finishes)},")
    lines.append(f"    details: {js(g.get('long', g.get('description', '')))},")
    lines.append("    subProducts: [")
    for p in prods:
        if p.get("__legacy__"):
            lines.append("      {")
            lines.append(f"        name: {js(p['title'])},")
            lines.append(f"        image: {js(p['img'])},")
            lines.append(f"        route: makeRoute({js(p['title'])}),")
            lines.append(f"        itemCode: {js(p['item_code'])},")
            lines.append(f"        longDescription: {js(p['short'])},")
            lines.append("        standards: [],")
            lines.append("        dimensions: [],")
            lines.append("        images: [],")
            lines.append("        charts: [],")
            lines.append("      },")
        else:
            imgs = [f"{PRODUCT_BASE}/KALOTI/{p['main_file']}"]
            charts = [f"{PRODUCT_BASE}/KALOTI/{c}" for c in p["chart_files"]]
            std = p["standards"]; dims = p["dimensions"]
            longd = p["short"]
            if std:
                longd += " Standards: " + " ".join(std)
            if dims:
                longd += " Dimensions: " + " ".join(dims)
            lines.append("      {")
            lines.append(f"        name: {js(p['title'])},")
            lines.append(f"        image: {js(imgs[0])},")
            lines.append(f"        route: {js(p['slug'])},")
            lines.append(f"        itemCode: {js(p['item_code'])},")
            lines.append(f"        longDescription: {js(longd)},")
            lines.append(f"        standards: {js(std)},")
            lines.append(f"        dimensions: {js(dims)},")
            lines.append(f"        images: {js(imgs)},")
            lines.append(f"        charts: {js(charts)},")
            lines.append("      },")
    lines.append("    ],")
    lines.append("  },")

lines.append("]")
lines.append("")
lines.append("export const getCategoryById = (id) => categories.find(c => c.id === id || c.slug === id)")
lines.append("export const getSubProduct = (categoryId, subProductName) => {")
lines.append("  const cat = getCategoryById(categoryId)")
lines.append("  return cat?.subProducts.find(s => s.name === subProductName)")
lines.append("}")
lines.append("")
lines.append("export const allProducts = categories.flatMap(cat =>")
lines.append("  (cat.subProducts || []).map(sp => ({")
lines.append("    name: sp.name,")
lines.append("    image: sp.image,")
lines.append("    images: sp.images && sp.images.length ? sp.images : [sp.image],")
lines.append("    charts: sp.charts || [],")
lines.append("    route: sp.route || makeRoute(sp.name),")
lines.append("    itemCode: sp.itemCode || sp.name,")
lines.append("    category: cat.name,")
lines.append("    categoryId: cat.id,")
lines.append("    description: cat.description,")
lines.append("    longDescription: sp.longDescription || cat.longDescription,")
lines.append("    standards: sp.standards || [],")
lines.append("    dimensions: sp.dimensions || [],")
lines.append("    sizeOptions: cat.sizeOptions || [],")
lines.append("    gradeOptions: cat.gradeOptions || [],")
lines.append("    finishOptions: cat.finishOptions || [],")
lines.append("    specs: [")
lines.append("      { label: 'Category', value: cat.name },")
lines.append("      { label: 'Size Range', value: cat.sizeRange || 'Various' },")
lines.append("      { label: 'Grade', value: cat.grade || 'Industrial Grade' },")
lines.append("      { label: 'Finish', value: cat.finishing || 'Standard' },")
lines.append("    ],")
lines.append("  }))")
lines.append(")")
lines.append("")

open(OUT, "w").write("\n".join(lines))
print(f"wrote {OUT}")
# quick validation with node
import subprocess
r = subprocess.run(["node", "-e",
    f"import('{OUT}').then(m=>{{console.log('categories:',m.categories.length);console.log('products:',m.allProducts.length)}})"],
    capture_output=True, text=True)
print(r.stdout[-500:])
print(r.stderr[-500:] if r.returncode else "")
