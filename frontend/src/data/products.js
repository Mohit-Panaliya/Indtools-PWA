import { createResource, createListResource } from "frappe-ui"

export const productList = createResource({
  url: "webshop.webshop.api.get_product_filter_data",
  transform(data) {
    return data
  },
  onError(error) {
    console.error("Failed to fetch products:", error)
  },
})

export const productInfo = createResource({
  url: "webshop.webshop.shopping_cart.product_info.get_product_info_for_website",
  transform(data) {
    return data
  },
  onError(error) {
    console.error("Failed to fetch product info:", error)
  },
})

export const searchProducts = createResource({
  url: "webshop.webshop.api.get_product_filter_data",
  onError(error) {
    console.error("Search failed:", error)
  },
})

export const cartResource = createResource({
  url: "webshop.webshop.shopping_cart.cart.get_cart_quotation",
  onSuccess(data) {
    return data
  },
  onError(error) {
    console.error("Failed to load cart:", error)
  },
})

export const updateCartResource = createResource({
  url: "webshop.webshop.shopping_cart.cart.update_cart",
  onSuccess(data) {
    return data
  },
  onError(error) {
    console.error("Failed to update cart:", error)
  },
})

export const placeOrderResource = createResource({
  url: "webshop.webshop.shopping_cart.cart.place_order",
  onError(error) {
    console.error("Failed to place order:", error)
  },
})

export const addToWishlist = createResource({
  url: "webshop.webshop.shopping_cart.cart.add_to_wishlist",
  onError(error) {
    console.error("Failed to add to wishlist:", error)
  },
})

export const removeFromWishlist = createResource({
  url: "webshop.webshop.shopping_cart.cart.remove_from_wishlist",
  onError(error) {
    console.error("Failed to remove from wishlist:", error)
  },
})

export const submitEnquiry = createResource({
  url: "webshop.webshop.shopping_cart.cart.create_lead_for_item_inquiry",
  onError(error) {
    console.error("Failed to submit enquiry:", error)
  },
})

export const websiteItems = createListResource({
  doctype: "Website Item",
  fields: [
    "name",
    "web_item_name",
    "item_code",
    "item_group",
    "route",
    "website_image",
    "short_description",
    "published",
  ],
  filters: { published: 1 },
  orderBy: "ranking desc",
  limit: 20,
})
