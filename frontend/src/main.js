import { createApp } from "vue"
import { IonicVue } from "@ionic/vue"
import App from "./App.vue"
import router from "./router"
import {
  setConfig,
  frappeRequest,
  resourcesPlugin,
  Button,
  Input,
  FormControl,
  ErrorMessage,
  Toasts,
  toast,
} from "frappe-ui"
import "@ionic/vue/css/core.css"
import "@ionic/vue/css/normalize.css"
import "@ionic/vue/css/typography.css"
import "./main.css"
import { initSocket } from "./socket"

let app = null

function setupApp() {
  setConfig("resourceFetcher", frappeRequest)
  app = createApp(App)
  const socket = initSocket()

  app.use(IonicVue, { mode: "ios" })
  app.use(router)
  app.use(resourcesPlugin)

  app.component("Button", Button)
  app.component("Input", Input)
  app.component("FormControl", FormControl)
  app.component("ErrorMessage", ErrorMessage)
  app.component("Toasts", Toasts)

  app.provide("$socket", socket)
  app.provide("$toast", toast)

  app.mount("#app")
}

if (window.frappe && window.frappe.boot) {
  setupApp()
} else {
  setupApp()
}
