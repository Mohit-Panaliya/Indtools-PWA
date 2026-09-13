# Deploying the INDTOOLS PWA from scratch

This guide walks through hosting the Indtools PWA end-to-end, in the exact way it
is run in production (`https://indtools.in`). It assumes Ubuntu 24.04, the public
domain's DNS first pointed at your server, and root/sudo access. Everything is
reusable: swap `<SITE>`, ports and hosts for your own box.

The architecture:

```
Internet
   │  :443 / :80  (Let's Encrypt TLS)
   ▼
Traefik  (edge router, dynamic config in deploy/traefik/)
   │  http://<HOST>:8002        │  http://<HOST>:9001  (/socket.io only)
   ▼                            ▼
nginx (bench "production" front)  node socketio.js (Frappe realtime)
   │  static /assets /files, else proxy pass
   ▼
gunicorn  (Frappe, :8001)  ──►  MariaDB
```

---

## 1. DNS

Add an **A record** for the domain (and `www` as A → same IP, or CNAME):

```
indtools.in   A    <your-public-ip>
www.indtools.in  CNAME  indtools.in.
```

Verify with an unbiased resolver before continuing:

```bash
dig @8.8.8.8 indtools.in +short     # expect your public IP
```

## 2. Bench with Frappe 16 + ERPNext 16

Perform the host OS prep (MariaDB, etc.) per the [Frappe docs](https://frappeframework.com/docs/v16/user/en/installation).
Create the bench:

```bash
pip install --upgrade frappe-bench
bench init --python /usr/bin/python3 --frappe-branch version-16 new-bench
cd new-bench

bench get-app --branch version-16 https://github.com/frappe/erpnext
bench get-app --branch version-16 https://github.com/frappe/payments    # dependency of webshop
bench get-app --branch version-16 https://github.com/frappe/webshop
bench get-app https://github.com/Mohit-Panaliya/Indtools-PWA

# Create the site. Use a MySQL admin user, NOT root, where possible.
bench new-site <SITE> \
  --db-root-username frappe_admin --db-root-password '<strong-pass>' \
  --admin-password <admin-password>
```

Register the site-tenant domains in `sites/<SITE>/site_config.json`:

```json
{
  "db_name": "...",
  "db_password": "...",
  "db_type": "mariadb",
  "db_user": "...",
  "domains": ["indtools.in", "www.indtools.in", "<SITE>", "localhost"],
  "host_name": "<SITE>"
}
```

> **Bench tip:** `webshop` imports `erpnext` and `payments`, so install
> `erpnext` first. `bench build` (JS asset bundling) is NOT required — the PWA
> ships pre-built static assets.

## 3. Install the apps on the site

```bash
bench --site <SITE> install-app erpnext payments webshop indtools_pwa
```

Expected `sites/apps.txt`: `frappe, erpnext, payments, webshop, indtools_pwa`.

## 4. Company + fiscal year (ERPNext setup wizard)

```bash
bench --site <SITE> console < deploy/setup_company.py
```

Creates the Company (`INDTOOLS` / `IND` / INR / India / Manufacturing domain),
a fiscal year, the "India - Chart of Accounts", and marks `setup_complete`, so
the site boots straight into the app. Run **before** product setup (it creates
the default Item Groups, Price Lists and "Standard Selling").

## 5. Products + catalog

```bash
bench --site <SITE> execute indtools_pwa.setup_products.setup_all
```

Creates 8 Item Groups, 8 category Items, 64 product Items, 72 published
Website Items, each with website specifications (Size Range, Grade, Finishing).
The catalog (codes, groups, images) is documented in **[ITEMS.md](ITEMS.md)**.

## 6. Webshop Settings + Item Prices

```bash
cd new-bench/sites && /path/to/new-bench/env/bin/python /path/to/Indtools-PWA/deploy/setup_webshop.py
```

- Enables Webshop + checkout, sets company → `Standard Selling` price list,
  `Individual` default customer group, `SAL-QTN-` quotation series.
- Creates an Item Price on `Standard Selling` for every item — deterministic
  25..220 INR (step 5, seeded from item code MD5) so deployments match.

## 7. Product images

The PWA images must be served publicly for webshop's `validate_website_image`
and for the storefront. Run:

```bash
cd new-bench/sites && /path/to/new-bench/env/bin/python /path/to/Indtools-PWA/deploy/apply_images.py
```

It copies `indtools_pwa/public/frontend/products/` into
`sites/<SITE>/public/files/`, creates public `File` records
(`/files/<CATEGORY>/<file>.png`) and sets `Item.image` + `Website
Item.website_image`. Do this from the bench `sites` dir so the site path
resolves; keep `SITE=...` env in sync.

> **Gotcha encountered:** ERPNext 16 renamed `Item.website_image` → `Item.image`,
> and Webshop's Website Item validation silently nulls `website_image` unless a
> matching File record exists. This script is the workaround.

## 8. Run in production (gunicorn + socketio)

```bash
bench --site <SITE> enable-scheduler
bench setup production --user www-data --yes         # writes supervisor + nginx
supervisorctl reread && supervisorctl update && supervisorctl start all
```

Dedicated **Socket.IO** node (separate port to avoid clashing with default 9000):

```bash
sudo cp deploy/supervisor/indtools-socketio.conf /etc/supervisor/conf.d/
# edit <path> + user; FRAPPE_SOCKETIO_PORT=9001 (must match nginx/socketio route)
sudo supervisorctl reread && sudo supervisorctl update
```

Verify: `ss -ltnp | grep 9001` shows `node socketio.js`.

## 9. nginx front

Use `deploy/nginx/indtools-pwa.conf`:

```bash
sudo cp deploy/nginx/indtools-pwa.conf /etc/nginx/sites-enabled/<SITE>.conf
sudo nginx -t && sudo systemctl reload nginx
```

What it does:

- listens on `:8002` (private; only Traefik reaches it)
- serves `/assets` and `/files` directly from the bench sites dir
- proxies everything else to gunicorn `:8001` (`X-Frappe-Site-Name <SITE>`)
- proxies `/socket.io` to the SocketIO node `:9001`
- on the storefront domains, `location = /` rewires `/` → `/indtools` **internally**
  (browser URL stays `/`), so the PWA is the homepage while `/desk` still opens
  ERP. Remove/replace that `location = /` block if you prefer the PWA under a path.

Smoke test locally:

```bash
curl -s -o /dev/null -w "%{http_code}\n" http://127.0.0.1:8002/indtools   # 200
curl -s http://127.0.0.1:8002/indtools | grep -o "<title>[^<]*"           # INDTOOLS title
# API sanity
curl "http://127.0.0.1:8002/api/method/webshop.webshop.api.get_product_filter_data" \
  -H "X-Frappe-Site-Name: <SITE>"   # items with website_image set
# SocketIO handshake
curl "http://127.0.0.1:8002/socket.io/?EIO=4&transport=polling"           # {"sid":...}
```

## 10. Edge router (Traefik + TLS)

If you use Traefik (e.g. Dokploy) at the edge:

```bash
sudo cp deploy/traefik/indtools-routes.yml /etc/dokploy/traefik/dynamic/
```

Traefik hot-reloads it, issues **Let's Encrypt** certs automatically for the
Host rules, and redirects http→https. The config routes the PWA to
`http://<HOST>:8002` and `/socket.io` to `http://<HOST>:9001` with
`passHostHeader: true`. Adjust the IP/ports for your box.

If you expose nginx directly instead, remove Step 10's Traefik config and point
you DNS A record at the server running nginx 80/443 (add `listen 80;`+`listen
443 ssl;` to the nginx block, or use certbot).

## 11. Verification (should all be green)

```bash
curl -s -o /dev/null -w "%{http_code}\n" https://indtools.in/            # 200 (PWA root)
curl -s https://indtools.in/           | grep -o "<title>[^<]*"          # INDTOOLS...
curl -s -o /dev/null -w "%{http_code}\n" https://indtools.in/files/BOLTS/HEX_BOLT.png  # 200
curl -s -o /dev/null -w "%{http_code}\n" https://indtools.in/desk        # 301 -> /login
echo | openssl s_client -connect indtools.in:443 -servername indtools.in 2>/dev/null \
  | openssl x509 -noout -issuer -dates                                       # Let's Encrypt
# guest API (no auth) must work:
curl "https://indtools.in/api/method/webshop.webshop.api.get_product_filter_data" # items+j/images
```

Point the PWA at your site by ensuring your Socket.IO port/namespace match
`frontend/src/socket.js` (`site name` namespace), and that Webshop/guest
product APIs are enabled (configured in Step 6).

## Troubleshooting quick-notes

| Symptom | Cause / fix |
|---|---|
| `website_image` empty everywhere | Webshop validation cleared them → re-run `deploy/apply_images.py` |
| `InstancesOf this item is unresolvable` style errors during setup | Run setup scripts via `bench ... console < file` or `bench ... execute` |
| PWA assets 404 | `sites/assets` symlinks missing → `bench setup add-to-hosts`/`bench build` not needed; check symlink `sites/assets/indtools_pwa` → app `public/` |
| `/socket.io` fails | confirm node program running on 9001 + nginx proxies with `X-Frappe-Site-Name` |
| `UnboundLocalError` in `frappe.locale` with some languages | upstream bug in older Frappe; check the frappe version / patch |
| `/order`/`/me` style hosts must be disabled | remove them from the Traefik Host rules + nginx `server_name` (see `deploy/`) |