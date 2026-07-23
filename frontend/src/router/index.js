import { createRouter, createWebHistory } from "@ionic/vue-router"
import { sessionUser } from "@/data/session"

const routes = [
  { path: "/indtools/", redirect: "/indtools/home" },
  { path: "/indtools/home", name: "Home", component: () => import("@/views/Home.vue"), meta: { guest: true } },
  { path: "/indtools/products", name: "Products", component: () => import("@/views/products/ProductList.vue"), meta: { guest: true } },
  { path: "/indtools/products/:group", name: "ProductsByGroup", component: () => import("@/views/products/ProductList.vue"), meta: { guest: true } },
  { path: "/indtools/product/:code", name: "ProductDetail", component: () => import("@/views/products/ProductDetail.vue"), meta: { guest: true } },
  { path: "/indtools/cart", name: "Cart", component: () => import("@/views/Cart.vue"), meta: { guest: true } },
  { path: "/indtools/checkout", name: "Checkout", component: () => import("@/views/Checkout.vue") },
  { path: "/indtools/enquiry", name: "Enquiry", component: () => import("@/views/Enquiry.vue"), meta: { guest: true } },
  { path: "/indtools/contact", name: "Contact", component: () => import("@/views/Contact.vue"), meta: { guest: true } },
  { path: "/indtools/about", name: "About", component: () => import("@/views/About.vue"), meta: { guest: true } },
  { path: "/indtools/login", name: "Login", component: () => import("@/views/account/Login.vue"), meta: { guest: true } },
  { path: "/indtools/register", name: "Register", component: () => import("@/views/account/Register.vue"), meta: { guest: true } },
  { path: "/indtools/forgot-password", name: "ForgotPassword", component: () => import("@/views/account/ForgotPassword.vue"), meta: { guest: true } },
  { path: "/indtools/profile", name: "Profile", component: () => import("@/views/account/Profile.vue") },
  { path: "/indtools/orders", name: "Orders", component: () => import("@/views/account/OrderHistory.vue") },
  { path: "/indtools/orders/:id", name: "OrderDetail", component: () => import("@/views/account/OrderDetail.vue") },
  { path: "/indtools/wishlist", name: "Wishlist", component: () => import("@/views/account/Wishlist.vue") },
  { path: "/indtools/notifications", name: "Notifications", component: () => import("@/views/account/Notifications.vue") },
  { path: "/indtools/change-password", name: "ChangePassword", component: () => import("@/views/account/ChangePassword.vue") },
  { path: "/:pathMatch(.*)*", redirect: "/indtools/home" },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
  scrollBehavior() { return { top: 0 } },
})

router.beforeEach((to, from, next) => {
  const user = sessionUser()
  const isGuestRoute = to.meta.guest
  if (!user && !isGuestRoute) {
    next({ name: "Login", query: { redirect: to.fullPath } })
  } else if (user && (to.name === "Login" || to.name === "Register")) {
    next({ name: "Home" })
  } else {
    next()
  }
})

export default router
