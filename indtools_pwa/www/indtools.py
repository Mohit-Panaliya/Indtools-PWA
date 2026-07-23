import frappe
from frappe.boot import load_translations

no_cache = 1


def get_context(context):
	csrf_token = frappe.sessions.get_csrf_token()
	frappe.db.commit()
	context = frappe._dict()
	context.csrf_token = csrf_token
	context.boot = get_boot()
	context.site_name = frappe.local.site
	return context


def get_boot():
	bootinfo = frappe._dict(
		{
			"site_name": frappe.local.site,
		}
	)
	bootinfo.lang = frappe.local.lang
	return bootinfo
