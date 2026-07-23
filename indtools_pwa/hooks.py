app_name = "indtools_pwa"
app_title = "INDTOOLS PWA"
app_publisher = "INDTOOLS"
app_description = "INDTOOLS - Industrial Tools & Fasteners Ionic PWA"
app_email = "indtools1992@gmail.com"
app_license = "MIT"

# Includes
app_include_css = "/assets/indtools_pwa/css/indtools_pwa.css"

# Website route rules
website_route_rules = [
    {
        "from_route": "/indtools/<path:app_path>",
        "to_route": "indtools",
    },
]

# Jinja context
def get_context(context):
    context.app_name = "indtools_pwa"
