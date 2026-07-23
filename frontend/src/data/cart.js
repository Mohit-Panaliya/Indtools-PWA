import { ref, computed } from 'vue'
import { call } from 'frappe-ui'

const CART_KEY = 'indtools_cart'

const cartItems = ref(loadCart())

function loadCart() {
  try {
    return JSON.parse(localStorage.getItem(CART_KEY) || '[]')
  } catch { return [] }
}

function saveCart(items) {
  cartItems.value = items
  localStorage.setItem(CART_KEY, JSON.stringify(items))
  window.dispatchEvent(new Event('cart-updated'))
}

export function useCart() {
  const cartCount = computed(() => cartItems.value.reduce((s, i) => s + i.qty, 0))
  const subtotal = computed(() => cartItems.value.reduce((s, i) => s + (i.amount || i.qty * (i.rate || 0)), 0))

  function addToCart(item) {
    const existing = cartItems.value.find(c => c.item_code === item.item_code)
    if (existing) {
      existing.qty += (item.qty || 1)
      existing.amount = existing.qty * (existing.rate || 0)
    } else {
      cartItems.value.push({
        item_code: item.item_code,
        name: item.name || item.item_name || item.item_code,
        image: item.image || item.thumbnail || '',
        category: item.category || '',
        rate: item.rate || 0,
        qty: item.qty || 1,
        amount: (item.rate || 0) * (item.qty || 1),
        size: item.size || '',
        grade: item.grade || '',
        finish: item.finish || '',
      })
    }
    saveCart([...cartItems.value])

    syncToBackend(item)
  }

  async function syncToBackend(item) {
    try {
      await call('indtools_pwa.api.add_to_cart', {
        item_code: item.item_code,
        qty: item.qty || 1,
        size: item.size || null,
        grade: item.grade || null,
        finish: item.finish || null,
      })
    } catch (e) {
      console.warn('Cart sync to backend failed (user may not be logged in):', e.message || e)
    }
  }

  function updateQty(itemCode, qty) {
    const item = cartItems.value.find(c => c.item_code === itemCode)
    if (!item) return
    if (qty <= 0) {
      cartItems.value = cartItems.value.filter(c => c.item_code !== itemCode)
    } else {
      item.qty = qty
      item.amount = qty * (item.rate || 0)
    }
    saveCart([...cartItems.value])
  }

  function removeItem(itemCode) {
    cartItems.value = cartItems.value.filter(c => c.item_code !== itemCode)
    saveCart([...cartItems.value])
  }

  function clearCart() {
    saveCart([])
  }

  async function placeOrder() {
    try {
      const result = await call('indtools_pwa.api.place_order_api')
      clearCart()
      return result
    } catch (e) {
      console.error('Failed to place order:', e)
      throw e
    }
  }

  return {
    cartItems,
    cartCount,
    subtotal,
    addToCart,
    updateQty,
    removeItem,
    clearCart,
    placeOrder,
  }
}
