# INDTOOLS PWA

**INDTOOLS - Industrial Tools & Fasteners** Progressive Web App for Frappe/ERPNext.

A custom Frappe app providing an Ionic Vue 3 PWA frontend with offline support, product catalog, cart management, checkout, and account management.

## Features

- Product catalog with categories (Bolts, Nuts, Washers, Screws, Rivets, Pins, Socket Products, Other Products)
- Shopping cart and checkout
- User account (login, register, profile, order history, wishlist)
- Product enquiry and contact forms
- Offline-capable PWA with service worker (Workbox injectManifest)
- Frappe REST API backend

## Tech Stack

- **Backend:** Frappe / ERPNext
- **Frontend:** Ionic Vue 3, Tailwind CSS, Vite
- **PWA:** vite-plugin-pwa, Workbox

## Installation

```bash
# In your Frappe bench
bench get-app https://github.com/Mohit-Panaliya/Indtools-PWA
bench --site your-site install-app indtools_pwa
```

The app is ready to use immediately — the frontend is pre-built.

## Development

```bash
cd apps/indtools_pwa/frontend
npm install
npm run dev
```

Dev server runs on port `8081` with API proxy to the Frappe backend.

## Build

```bash
cd apps/indtools_pwa/frontend
npm run build
```

Output goes to `indtools_pwa/public/frontend/`.
