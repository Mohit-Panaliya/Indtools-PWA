import { ref, computed } from "vue"
import { call } from "frappe-ui"

export function sessionUser() {
  let cookies = new URLSearchParams(document.cookie.split("; ").join("&"))
  let _sessionUser = cookies.get("user_id")
  if (_sessionUser === "Guest") {
    _sessionUser = null
  }
  return _sessionUser
}

const user = ref(sessionUser())
const isLoggedIn = computed(() => !!user.value)
export const userFullName = ref("")
export const userEmail = ref("")

export async function fetchUserInfo() {
  if (!user.value) return
  try {
    const info = await call("frappe.client.get_value", {
      doctype: "User",
      filters: { name: user.value },
      fieldname: ["full_name", "email"],
    })
    if (info) {
      userFullName.value = info.full_name || ""
      userEmail.value = info.email || ""
    }
  } catch (e) {
    console.error("Failed to fetch user info:", e)
  }
}

export function useSession() {
  async function login(email, password) {
    const response = await call("indtools_pwa.api.login", { usr: email, pwd: password })
    user.value = sessionUser()
    await fetchUserInfo()
    return response
  }

  async function logout() {
    await call("logout")
    user.value = null
    userFullName.value = ""
    userEmail.value = ""
    window.location.href = "/indtools/login"
  }

  function getUser() {
    user.value = sessionUser()
    return user.value
  }

  return {
    user,
    isLoggedIn,
    userFullName,
    userEmail,
    login,
    logout,
    getUser,
    fetchUserInfo,
  }
}
