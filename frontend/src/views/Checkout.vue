<template>
  <div :class="darkMode ? 'bg-[#0f1710]' : 'bg-[#f5f5f5]'" class="min-h-screen">
    <!-- Hero Banner -->
    <div :class="darkMode ? 'bg-[#1a2e1f]' : 'bg-gradient-to-r from-[#1a4d2a] to-[#2a7f3e]'" class="py-10 md:py-14">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <h1 :class="darkMode ? 'text-green-300' : 'text-white'" class="text-3xl md:text-4xl font-extrabold mb-2 tracking-tight">Checkout</h1>
        <nav class="flex items-center space-x-2 text-sm">
          <router-link :class="darkMode ? 'text-green-400' : 'text-green-200'" to="/indtools/home" class="hover:underline">Home</router-link>
          <span :class="darkMode ? 'text-green-500' : 'text-green-300'">/</span>
          <router-link :class="darkMode ? 'text-green-400' : 'text-green-200'" to="/indtools/cart" class="hover:underline">Cart</router-link>
          <span :class="darkMode ? 'text-green-500' : 'text-green-300'">/</span>
          <span :class="darkMode ? 'text-green-200' : 'text-white'" class="opacity-80">Checkout</span>
        </nav>
      </div>
    </div>

    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6 md:py-10">
      <!-- Success Message -->
      <div v-if="orderPlaced" class="text-center py-20">
        <div class="w-20 h-20 mx-auto rounded-full flex items-center justify-center mb-6" :class="darkMode ? 'bg-[#1a2e1f]' : 'bg-[#e8f5e9]'">
          <svg class="w-10 h-10 text-[#4caf50]" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M5 13l4 4L19 7" />
          </svg>
        </div>
        <h2 :class="darkMode ? 'text-white' : 'text-[#1a4d2a]'" class="text-2xl font-extrabold mb-2">Order Placed Successfully!</h2>
        <p :class="darkMode ? 'text-gray-400' : 'text-gray-500'" class="text-sm mb-6">Your order has been placed. We'll contact you shortly.</p>
        <router-link to="/indtools/products" class="inline-block bg-[#2a7f3e] hover:bg-[#1a4d2a] text-white px-6 py-3 rounded-xl font-bold text-sm transition-all shadow-lg shadow-[#2a7f3e]/20">
          Continue Shopping
        </router-link>
      </div>

      <!-- Checkout Form -->
      <div v-else class="flex flex-col lg:flex-row gap-6">
        <!-- Left: Order Summary -->
        <div class="flex-1">
          <div :class="darkMode ? 'bg-[#1a2e1f] border-[#2a7f3e]/20' : 'bg-white border-gray-100'" class="rounded-2xl p-5 border">
            <h2 :class="darkMode ? 'text-white' : 'text-gray-900'" class="text-lg font-extrabold mb-4">Order Summary</h2>
            <div v-if="cartItems.length" class="space-y-3">
              <div v-for="item in cartItems" :key="item.item_code" class="flex gap-3 py-3" :class="darkMode ? 'border-[#2a7f3e]/10' : 'border-gray-50'" style="border-bottom-style: solid; border-bottom-width: 1px;">
                <div :class="darkMode ? 'bg-[#0f1710]' : 'bg-gray-50'" class="w-14 h-14 rounded-xl overflow-hidden flex items-center justify-center flex-shrink-0">
                  <img :src="item.image || '/assets/indtools_pwa/frontend/products/BOLTS/HEX_BOLT.png'" :alt="item.name" class="w-full h-full object-contain p-0.5" @error="handleImageError" />
                </div>
                <div class="flex-1 min-w-0">
                  <p :class="darkMode ? 'text-white' : 'text-gray-800'" class="text-sm font-bold truncate">{{ item.name }}</p>
                  <p :class="darkMode ? 'text-gray-500' : 'text-gray-400'" class="text-xs mt-0.5">Qty: {{ item.qty }}</p>
                </div>
                <p :class="darkMode ? 'text-white' : 'text-gray-800'" class="text-sm font-bold flex-shrink-0">₹{{ formatPrice(item.amount) }}</p>
              </div>
            </div>
            <div v-else :class="darkMode ? 'text-gray-500' : 'text-gray-400'" class="text-sm py-4 text-center">Your cart is empty.</div>

            <div class="flex justify-between mt-4 pt-4" :class="darkMode ? 'border-[#2a7f3e]/15' : 'border-gray-100'" style="border-top-style: solid; border-top-width: 1px;">
              <span :class="darkMode ? 'text-white' : 'text-gray-900'" class="font-extrabold">Total</span>
              <span class="font-extrabold text-lg text-[#4caf50]">₹{{ formatPrice(subtotal) }}</span>
            </div>
          </div>
        </div>

        <!-- Right: Shipping Form -->
        <div class="w-full lg:w-[480px] flex-shrink-0">
          <div :class="darkMode ? 'bg-[#1a2e1f] border-[#2a7f3e]/20' : 'bg-white border-gray-100'" class="rounded-2xl p-5 border">
            <h2 :class="darkMode ? 'text-white' : 'text-gray-900'" class="text-lg font-extrabold mb-4">Shipping Details</h2>
            <form @submit.prevent="placeOrder" class="space-y-4">
              <div>
                <label :class="darkMode ? 'text-gray-400' : 'text-gray-600'" class="block text-xs font-bold mb-1">Full Name *</label>
                <input v-model="form.name" type="text" required placeholder="Enter your full name"
                  :class="darkMode ? 'bg-[#0f1710] border-[#2a7f3e]/30 text-white placeholder-gray-600 focus:border-[#4caf50]' : 'bg-white border-gray-200 text-gray-900 placeholder-gray-400 focus:border-[#2a7f3e]'"
                  class="w-full px-4 py-3 text-sm border-2 rounded-xl focus:outline-none transition-colors" />
              </div>

              <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                <div>
                  <label :class="darkMode ? 'text-gray-400' : 'text-gray-600'" class="block text-xs font-bold mb-1">Email *</label>
                  <input v-model="form.email" type="email" required placeholder="you@example.com"
                    :class="darkMode ? 'bg-[#0f1710] border-[#2a7f3e]/30 text-white placeholder-gray-600 focus:border-[#4caf50]' : 'bg-white border-gray-200 text-gray-900 placeholder-gray-400 focus:border-[#2a7f3e]'"
                    class="w-full px-4 py-3 text-sm border-2 rounded-xl focus:outline-none transition-colors" />
                </div>
                <div>
                  <label :class="darkMode ? 'text-gray-400' : 'text-gray-600'" class="block text-xs font-bold mb-1">Phone *</label>
                  <input v-model="form.phone" type="tel" required placeholder="+91 XXXXX XXXXX"
                    :class="darkMode ? 'bg-[#0f1710] border-[#2a7f3e]/30 text-white placeholder-gray-600 focus:border-[#4caf50]' : 'bg-white border-gray-200 text-gray-900 placeholder-gray-400 focus:border-[#2a7f3e]'"
                    class="w-full px-4 py-3 text-sm border-2 rounded-xl focus:outline-none transition-colors" />
                </div>
              </div>

              <div>
                <label :class="darkMode ? 'text-gray-400' : 'text-gray-600'" class="block text-xs font-bold mb-1">Address Line 1 *</label>
                <input v-model="form.address1" type="text" required placeholder="Street address, P.O. box"
                  :class="darkMode ? 'bg-[#0f1710] border-[#2a7f3e]/30 text-white placeholder-gray-600 focus:border-[#4caf50]' : 'bg-white border-gray-200 text-gray-900 placeholder-gray-400 focus:border-[#2a7f3e]'"
                  class="w-full px-4 py-3 text-sm border-2 rounded-xl focus:outline-none transition-colors" />
              </div>

              <div>
                <label :class="darkMode ? 'text-gray-400' : 'text-gray-600'" class="block text-xs font-bold mb-1">Address Line 2</label>
                <input v-model="form.address2" type="text" placeholder="Apartment, suite, unit, etc."
                  :class="darkMode ? 'bg-[#0f1710] border-[#2a7f3e]/30 text-white placeholder-gray-600 focus:border-[#4caf50]' : 'bg-white border-gray-200 text-gray-900 placeholder-gray-400 focus:border-[#2a7f3e]'"
                  class="w-full px-4 py-3 text-sm border-2 rounded-xl focus:outline-none transition-colors" />
              </div>

              <div class="grid grid-cols-2 sm:grid-cols-3 gap-4">
                <div class="col-span-2 sm:col-span-1">
                  <label :class="darkMode ? 'text-gray-400' : 'text-gray-600'" class="block text-xs font-bold mb-1">City *</label>
                  <input v-model="form.city" type="text" required placeholder="City"
                    :class="darkMode ? 'bg-[#0f1710] border-[#2a7f3e]/30 text-white placeholder-gray-600 focus:border-[#4caf50]' : 'bg-white border-gray-200 text-gray-900 placeholder-gray-400 focus:border-[#2a7f3e]'"
                    class="w-full px-4 py-3 text-sm border-2 rounded-xl focus:outline-none transition-colors" />
                </div>
                <div>
                  <label :class="darkMode ? 'text-gray-400' : 'text-gray-600'" class="block text-xs font-bold mb-1">State *</label>
                  <input v-model="form.state" type="text" required placeholder="State"
                    :class="darkMode ? 'bg-[#0f1710] border-[#2a7f3e]/30 text-white placeholder-gray-600 focus:border-[#4caf50]' : 'bg-white border-gray-200 text-gray-900 placeholder-gray-400 focus:border-[#2a7f3e]'"
                    class="w-full px-4 py-3 text-sm border-2 rounded-xl focus:outline-none transition-colors" />
                </div>
                <div>
                  <label :class="darkMode ? 'text-gray-400' : 'text-gray-600'" class="block text-xs font-bold mb-1">Pincode *</label>
                  <input v-model="form.pincode" type="text" required placeholder="Pincode"
                    :class="darkMode ? 'bg-[#0f1710] border-[#2a7f3e]/30 text-white placeholder-gray-600 focus:border-[#4caf50]' : 'bg-white border-gray-200 text-gray-900 placeholder-gray-400 focus:border-[#2a7f3e]'"
                    class="w-full px-4 py-3 text-sm border-2 rounded-xl focus:outline-none transition-colors" />
                </div>
              </div>

              <button type="submit" :disabled="placing || !cartItems.length"
                class="w-full py-3.5 rounded-xl text-white font-bold transition-all duration-200 shadow-lg shadow-[#2a7f3e]/25 hover:shadow-[#2a7f3e]/40 hover:-translate-y-0.5 disabled:opacity-50 disabled:cursor-not-allowed disabled:hover:translate-y-0 bg-gradient-to-r from-[#2a7f3e] to-[#3d9970] hover:from-[#1a4d2a] hover:to-[#2a7f3e] mt-2">
                <span v-if="placing" class="flex items-center justify-center gap-2">
                  <svg class="animate-spin w-4 h-4" fill="none" viewBox="0 0 24 24"><circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4" /><path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4z" /></svg>
                  Placing Order...
                </span>
                <span v-else>Place Order</span>
              </button>

              <router-link to="/indtools/cart" :class="darkMode ? 'bg-[#0f1710] border-[#2a7f3e]/30 text-gray-400 hover:bg-[#1a2e1f]' : 'bg-white border-gray-200 text-gray-600 hover:bg-gray-50'" class="block text-center py-3 text-sm font-semibold rounded-xl border-2 transition-all">
                Back to Cart
              </router-link>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, reactive, computed, inject } from 'vue'
import { useRouter } from 'vue-router'
import { useCart } from '@/data/cart'
import { sessionUser } from '@/data/session'
import { call } from 'frappe-ui'

const darkMode = inject('darkMode', ref(false))
const router = useRouter()
const { cartItems, subtotal, clearCart } = useCart()

const orderPlaced = ref(false)
const placing = ref(false)

const form = reactive({
  name: '', email: '', phone: '',
  address1: '', address2: '',
  city: '', state: '', pincode: '',
})

function formatPrice(val) {
  return Number(val || 0).toLocaleString('en-IN', { minimumFractionDigits: 2, maximumFractionDigits: 2 })
}

function handleImageError(e) {
  e.target.src = '/assets/indtools_pwa/frontend/indtools_logo_new.png'
}

function buildAddress() {
  return [form.address1, form.address2, form.city, form.state, form.pincode].filter(Boolean).join(', ')
}

async function placeOrder() {
  if (!cartItems.value.length) return
  placing.value = true
  try {
    const address = buildAddress()
    if (sessionUser()) {
      await call('webshop.webshop.shopping_cart.cart.place_order', {
        billing_address: address,
        shipping_address: address,
      })
    }
    clearCart()
    orderPlaced.value = true
  } catch (e) {
    console.error('Failed to place order:', e)
    alert('Failed to place order. Please try again or contact us.')
  } finally {
    placing.value = false
  }
}
</script>
