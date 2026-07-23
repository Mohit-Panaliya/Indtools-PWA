import frappe
from frappe import _
from frappe.utils import escape_html


@frappe.whitelist(allow_guest=True)
def login(usr, pwd):
    """Login user via API"""
    from frappe.auth import LoginManager
    lm = LoginManager()
    lm.authenticate(user=usr, pwd=pwd)
    lm.login()
    return {"message": "Logged in successfully"}


@frappe.whitelist(allow_guest=True)
def register(full_name, email, password):
    """Register a new user account"""
    if frappe.db.get("User", {"email": email}):
        frappe.throw(_("Email already registered"))

    user = frappe.get_doc({
        "doctype": "User",
        "email": email,
        "first_name": escape_html(full_name),
        "enabled": 1,
        "new_password": password,
        "user_type": "Website User",
    })
    user.flags.ignore_permissions = True
    user.flags.ignore_password_policy = True
    user.insert()

    default_role = frappe.get_single_value("Portal Settings", "default_role")
    if default_role:
        user.add_roles(default_role)
        user.save()

    frappe.db.commit()
    return {"message": "Account created successfully"}


@frappe.whitelist()
def get_cart():
    """Get current user's cart"""
    try:
        from webshop.webshop.shopping_cart.cart import get_cart_quotation
        return get_cart_quotation()
    except Exception:
        return {"doc": {"items": [], "total": 0}, "shipping_addresses": [], "billing_addresses": []}


@frappe.whitelist()
def add_to_cart(item_code, qty=1, size=None, grade=None, finish=None):
    """Add item to cart or update quantity"""
    try:
        from webshop.webshop.shopping_cart.cart import update_cart
        notes = ""
        if size:
            notes += f"Size: {size}"
        if grade:
            notes += f" Grade: {grade}"
        if finish:
            notes += f" Finish: {finish}"
        return update_cart(item_code=item_code, qty=qty, additional_notes=notes.strip())
    except Exception as e:
        frappe.throw(str(e))


@frappe.whitelist()
def remove_from_cart(item_code):
    """Remove item from cart (set qty to 0)"""
    try:
        from webshop.webshop.shopping_cart.cart import update_cart
        return update_cart(item_code=item_code, qty=0)
    except Exception as e:
        frappe.throw(str(e))


@frappe.whitelist()
def place_order_api(billing_address=None, shipping_address=None):
    """Place order from cart"""
    try:
        from webshop.webshop.shopping_cart.cart import place_order
        kwargs = {}
        if billing_address:
            kwargs["billing_address"] = billing_address
        if shipping_address:
            kwargs["shipping_address"] = shipping_address
        return place_order(**kwargs)
    except Exception as e:
        frappe.throw(str(e))


@frappe.whitelist(allow_guest=True)
def create_enquiry(name, email, phone, company=None, subject=None, message=None, product=None):
    """Create an enquiry lead"""
    try:
        lead = frappe.get_doc({
            "doctype": "Lead",
            "lead_name": name,
            "email_id": email,
            "phone": phone,
            "company": company or "INDTOOLS",
            "lead_source": "Website",
            "notes": f"Subject: {subject or 'Product Enquiry'}\n{message or ''}\n\nProduct: {product or 'General'}",
        })
        lead.flags.ignore_permissions = True
        lead.insert()
        frappe.db.commit()
        return {"message": "Enquiry submitted successfully"}
    except Exception as e:
        frappe.throw(str(e))


@frappe.whitelist()
def get_product_info(item_code):
    """Get product pricing and stock info"""
    try:
        from webshop.webshop.shopping_cart.product_info import get_product_info_for_website
        return get_product_info_for_website(item_code)
    except Exception:
        return {"price": {"price_list_rate": 0}, "stock_status": {"in_stock": True}}
