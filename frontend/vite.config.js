import { defineConfig } from "vite"
import vue from "@vitejs/plugin-vue"
import { VitePWA } from "vite-plugin-pwa"
import frappeui from "frappe-ui/vite"
import path from "path"
import fs from "fs"

export default defineConfig({
  base: "/assets/indtools_pwa/frontend/",
  server: {
    port: 8081,
    proxy: getProxyOptions(),
    allowedHosts: true,
  },
  plugins: [
    vue(),
    frappeui(),
    VitePWA({
      registerType: "autoUpdate",
      strategies: "injectManifest",
      injectRegister: null,
      devOptions: { enabled: true },
      manifest: {
        display: "standalone",
        name: "INDTOOLS - Industrial Tools & Fasteners",
        short_name: "INDTOOLS",
        start_url: "/indtools",
        scope: "/",
        description: "Your trusted partner for high-quality industrial tools and fasteners",
        theme_color: "#2a7f3e",
        background_color: "#f5f5f5",
        icons: [
          { src: "/assets/indtools_pwa/frontend/manifest/icon-192.png", sizes: "192x192", type: "image/png", purpose: "any" },
          { src: "/assets/indtools_pwa/frontend/manifest/icon-192.png", sizes: "192x192", type: "image/png", purpose: "maskable" },
          { src: "/assets/indtools_pwa/frontend/manifest/icon-512.png", sizes: "512x512", type: "image/png", purpose: "any" },
          { src: "/assets/indtools_pwa/frontend/manifest/icon-512.png", sizes: "512x512", type: "image/png", purpose: "maskable" },
        ],
      },
    }),
  ],
  resolve: {
    alias: { "@": path.resolve(__dirname, "src") },
  },
  build: {
    outDir: "../indtools_pwa/public/frontend",
    emptyOutDir: true,
    target: "es2015",
    sourcemap: true,
    rollupOptions: {
      output: {
        manualChunks: { "frappe-ui": ["frappe-ui"] },
      },
    },
  },
  optimizeDeps: {
    include: ["frappe-ui > feather-icons", "showdown", "tailwind.config.js", "engine.io-client"],
  },
})

function getProxyOptions() {
  const config = getCommonSiteConfig()
  const webserver_port = config ? config.webserver_port : 8000
  if (!config) {
    console.log("No common_site_config.json found, using default port 8000")
  }
  return {
    "^/(app|login|api|assets|files|private)": {
      target: `http://127.0.0.1:${webserver_port}`,
      ws: true,
      router: function (req) {
        const site_name = req.headers.host.split(":")[0]
        return `http://${site_name}:${webserver_port}`
      },
    },
  }
}

function getCommonSiteConfig() {
  let currentDir = path.resolve(".")
  while (currentDir !== "/") {
    if (
      fs.existsSync(path.join(currentDir, "sites")) &&
      fs.existsSync(path.join(currentDir, "apps"))
    ) {
      let configPath = path.join(currentDir, "sites", "common_site_config.json")
      if (fs.existsSync(configPath)) {
        return JSON.parse(fs.readFileSync(configPath))
      }
      return null
    }
    currentDir = path.resolve(currentDir, "..")
  }
  return null
}
