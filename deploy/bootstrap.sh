# Bench command sequence that boots the PWA "from scratch" once a bench
# (Frappe 16 + ERPNext 16 + Python) and a site exist.
#
# Prereqs (done once per machine):
#   pip install --upgrade frappe-bench    (or use your bench env)
#   bench init --python /path/to/python --frappe-branch version-16 new-bench
#   bench new-site <your-site>      # with MySQL root creds of your server
#
# Then run, replacing <your-site>:

# 1) Get the required Frappe apps
bench get-app --branch version-16 https://github.com/frappe/webshop
bench get-app --branch version-16 https://github.com/frappe/payments
bench get-app --branch version-16 https://github.com/frappe/erpnext
bench get-app https://github.com/Mohit-Panaliya/Indtools-PWA

# 2) Install apps on the site (order matters: erpnext first for webshop deps)
bench --site <your-site> install-app erpnext payments webshop indtools_pwa

# 3) Create the Company, Fiscal Year, chart, etc.
bench --site <your-site> console < deploy/setup_company.py

# 4) Create Item Groups, 64 products + 8 category items + Website Items
bench --site <your-site> execute indtools_pwa.setup_products.setup_all
#   (or: bench --site <your-site> console < deploy/products_start.py )

# 5) Configure Webshop Settings + create Item Prices (25..220 INR, deterministic)
cd /path/to/bench/sites && /path/to/bench/env/bin/python /path/to/Indtools-PWA/deploy/setup_webshop.py

# 6) Fix product images (copies them under the site public files + File records)
cd /path/to/bench/sites && /path/to/bench/env/bin/python /path/to/Indtools-PWA/deploy/apply_images.py

# 7) Start
bench --site <your-site> enable-scheduler
#   Go live: bench setup production --user <www-user> --yes, supervisorctl start
#   SocketIO: see deploy/supervisor/ (set FRAPPE_SOCKETIO_PORT per bench)
#   Web: nginx site block in deploy/nginx/, external router in deploy/traefik/