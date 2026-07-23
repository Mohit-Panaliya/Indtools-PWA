import { io } from "socket.io-client"

let socket = null

export function initSocket() {
  const host = window.location.hostname
  const port = window.location.port || (window.location.protocol === "https:" ? "443" : "80")
  const protocol = window.location.protocol === "https:" ? "wss:" : "ws:"
  const siteName = window.site_name || host

  socket = io(`${protocol}//${host}:${port}/${siteName}`, {
    withCredentials: true,
    reconnectionAttempts: 5,
  })

  socket.on("connect", () => {
    console.log("Socket connected")
  })

  socket.on("disconnect", () => {
    console.log("Socket disconnected")
  })

  return socket
}

export function getSocket() {
  return socket
}
