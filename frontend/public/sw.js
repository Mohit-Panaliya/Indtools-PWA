import { cleanupOutdatedCaches, precacheAndRoute } from "workbox-precaching"
import { clientsClaim } from "workbox-core"

precacheAndRoute(self.__WB_MANIFEST)

cleanupOutdatedCaches()

self.addEventListener("message", (event) => {
  if (event.data && event.data.type === "SKIP_WAITING") {
    self.skipWaiting()
  }
})

self.skipWaiting()
clientsClaim()
