# INDTOOLS PWA

**INDTOOLS — Industrial Tools & Fasteners** Progressive Web App for Frappe / ERPNext 16.

A custom Frappe app (`indtools_pwa`) that ships a pre-built **Ionic Vue 3** PWA frontend with offline support, product catalog, cart, checkout and account management, backed by the Frappe `webshop` + `erpnext` REST APIs.

> **Live store:** https://indtools.in  (the PWA is served at the root URL)
> **ERP back-office:** https://indtools.in/desk

---

## Features

- 8 product categories / 72 products: Bolts, Nuts, Washers, Screws, Rivets, Pins, Socket Products, Other Products
- Home, About, Enquiry, Contact, Cart, Checkout, Product List & Detail screens
- Account: login, register, profile, wishlist, order history, notifications, change/forgot password
- Product enquiry + contact forms
- Offline-capable PWA with service worker (Workbox injectManifest)
- Frappe REST + realtime (Socket.IO) backend

Full product catalog: **[ITEMS.md](ITEMS.md)**.

## Tech Stack

| Layer | Tech |
|---|---|
| Backend | Frappe 16 · ERPNext 16 · Webshop · Payments |
| Storefront APIs | `frappe` `webshop` (product filter, cart, pricing, orders, wishlist) |
| PWA frontend | Ionic Vue 3, Tailwind CSS, Vite, frappe-ui |
| Realtime | Frappe Socket.IO node |
| Routing / TLS | nginx (bench front) · Traefik (edge, Let's Encrypt) |

## Repository layout

```
.
├── indtools_pwa/            # the Frappe app
│   ├── api.py               # indtools REST helpers (login, register, cart, enquiry, product info)
│   ├── setup_products.py    # creates 8 Item Groups + 72 Items/Website Items (source of catalog)
│   ├── fix_images.py        # asset copier used on first deploy
│   ├── www/indtools.py      # website route -> renders the PWA (REST-render template)
│   ├── www/indtools.html    # PWA shell (icons, manifest, initial loader)
│   └── public/frontend/     # PRE-BUILT PWA assets (served at /assets/indtools_pwa/frontend/)
├── frontend/                # Ionic Vue 3 SOURCE (dev/build only)
├── deploy/                  # everything needed to host from scratch
│   ├── bootstrap.sh         # full bench command sequence
│   ├── setup_company.py     # ERPNext wizard (Company, FY, chart, language)
│   ├── setup_webshop.py     # Webshop Settings + deterministic Item Prices
│   ├── apply_images.py      # sets Item.image + Website Item image + File records
│   ├── nginx/indtools-pwa.conf
│   ├── supervisor/indtools-socketio.conf
│   └── traefik/indtools-routes.yml
├── ITEMS.md                 # product catalog (groups, codes, specs, images)
└── DEPLOYMENT.md            # step-by-step hosting guide from scratch
```

## Quick start (deploying from scratch)

See **[DEPLOYMENT.md](DEPLOYMENT.md)** for the full guide (bench → apps → site → company → products → webshop → images → nginx → socketio → Traefik → DNS/TLS → verification).

The short version once a **Frappe 16 bench with ERPNext 16** and a site exist:

```bash
bench get-app --branch version-16 https://github.com/frappe/webshop
bench get-app --branch version-16 https://github.com/frappe/payments
bench get-app https://github.com/Mohit-Panaliya/Indtools-PWA

bench --site <your-site> install-app erpnext payments webshop indtools_pwa

bench --site <your-site> console < deploy/setup_company.py      # Company + FY + chart
bench --site <your-site> execute indtools_pwa.setup_products.setup_all   # 72 items
bench --site <your-site> console < deploy/setup_webshop.py       # Webshop + prices
# then apply_images.py + nginx/supervisor/traefik templates (see DEPLOYMENT.md)
```

The app is **ready to use immediately** — the PWA frontend is included pre-built; no `bench build` / node build required on the server.

## API surface (used by the PWA)

- `indtools_pwa.api.login` · `register` · `get_cart` · `add_to_cart` · `remove_from_cart` · `place_order_api` · `create_enquiry` · `get_product_info`
- `webshop.webshop.api.get_product_filter_data`
- `webshop.webshop.shopping_cart.cart.get_cart_quotation` · `update_cart` · `place_order` · `add_to_wishlist` · `remove_from_wishlist` · `create_lead_for_item_inquiry`
- `webshop.webshop.shopping_cart.product_info.get_product_info_for_website`
- Frappe REST: `Website Item` list, `frappe.client.get_value`, `frappe.client.get_list`
- Socket.IO namespace = site name (`/order.indtools.in`), port via `FRAPPE_SOCKETIO_PORT`

## Development

```bash
# PWA frontend (source in frontend/)
cd frontend
npm install
npm run dev          # Vite dev server on :8081, proxies API to the bench
npm run build        # outputs pre-built assets to indtools_pwa/public/frontend/
```

Making PWA changes? Commit the rebuilt `indtools_pwa/public/frontend/` so servers keep serving the pre-built bundle.

## License

Proprietary; © INDTOOLS. Contact [indtools1992@gmail.com](mailto:indtools1992@gmail.com).