<template>
  <div :class="darkMode ? 'bg-[#0f1710]' : 'bg-[#f5f5f5]'" class="min-h-screen">
    <!-- Hero Banner -->
    <div :class="darkMode ? 'bg-[#1a2e1f]' : 'bg-gradient-to-r from-[#1a4d2a] to-[#2a7f3e]'" class="py-10 md:py-14">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <h1 :class="darkMode ? 'text-green-300' : 'text-white'" class="text-3xl md:text-4xl font-extrabold mb-2 tracking-tight">Shopping Cart</h1>
        <nav class="flex items-center space-x-2 text-sm">
          <router-link :class="darkMode ? 'text-green-400' : 'text-green-200'" to="/indtools/home" class="hover:underline">Home</router-link>
          <span :class="darkMode ? 'text-green-500' : 'text-green-300'">/</span>
          <span :class="darkMode ? 'text-green-200' : 'text-white'" class="opacity-80">Cart ({{ cartCount }})</span>
        </nav>
      </div>
    </div>

    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6 md:py-10">
      <!-- Empty Cart -->
      <div v-if="!cartItems.length" class="text-center py-20">
        <div class="w-20 h-20 mx-auto rounded-full flex items-center justify-center mb-4" :class="darkMode ? 'bg-[#1a2e1f]' : 'bg-[#e8f5e9]'">
          <svg class="w-10 h-10" :class="darkMode ? 'text-[#4caf50]' : 'text-[#2a7f3e]'" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M3 3h2l.4 2M7 13h10l4-8H5.4M7 13L5.4 5M7 13l-2.293 2.293c-.63.63-.184 1.707.707 1.707H17m0 0a2 2 0 100 4 2 2 0 000-4zm-8 2a2 2 0 100 4 2 2 0 000-4z"/>
          </svg>
        </div>
        <h3 :class="darkMode ? 'text-white' : 'text-[#1a4d2a]'" class="text-xl font-bold mb-2">Your cart is empty</h3>
        <p :class="darkMode ? 'text-gray-400' : 'text-gray-500'" class="text-sm mb-6">Browse our products and add items to your cart</p>
        <router-link to="/indtools/products" class="inline-block bg-[#2a7f3e] hover:bg-[#1a4d2a] text-white px-6 py-3 rounded-xl font-bold text-sm transition-all shadow-lg shadow-[#2a7f3e]/20 hover:-translate-y-0.5">
          Browse Products
        </router-link>
      </div>

      <!-- Cart Items -->
      <div v-else class="grid grid-cols-1 lg:grid-cols-3 gap-6">
        <div class="lg:col-span-2 space-y-3">
          <div v-for="item in cartItems" :key="item.item_code"
            :class="darkMode ? 'bg-[#1a2e1f] border-[#2a7f3e]/20 hover:border-[#2a7f3e]/40' : 'bg-white border-gray-100 hover:shadow-lg'"
            class="rounded-2xl p-4 border transition-all duration-200">
            <div class="flex gap-4 items-start">
              <div :class="darkMode ? 'bg-[#0f1710]' : 'bg-gray-50'" class="w-20 h-20 flex-shrink-0 rounded-xl overflow-hidden flex items-center justify-center">
                <img :src="item.image || '/assets/indtools_pwa/frontend/products/BOLTS/HEX_BOLT.png'" :alt="item.name" class="w-full h-full object-contain p-1" @error="handleImageError" />
              </div>
              <div class="flex-1 min-w-0">
                <h3 :class="darkMode ? 'text-white' : 'text-gray-900'" class="text-sm font-bold truncate">{{ item.name }}</h3>
                <p :class="darkMode ? 'text-gray-500' : 'text-gray-400'" class="text-xs mt-0.5">{{ item.item_code }}</p>
                <div v-if="item.size || item.grade || item.finish" class="flex flex-wrap gap-1.5 mt-1.5">
                  <span v-if="item.size" class="text-[10px] px-2 py-0.5 rounded-md font-semibold" :class="darkMode ? 'bg-[#0f1710] text-[#4caf50]' : 'bg-[#e8f5e9] text-[#2a7f3e]'">{{ item.size }}</span>
                  <span v-if="item.grade" class="text-[10px] px-2 py-0.5 rounded-md font-semibold" :class="darkMode ? 'bg-[#0f1710] text-[#4caf50]' : 'bg-[#e8f5e9] text-[#2a7f3e]'">{{ item.grade }}</span>
                  <span v-if="item.finish" class="text-[10px] px-2 py-0.5 rounded-md font-semibold" :class="darkMode ? 'bg-[#0f1710] text-[#4caf50]' : 'bg-[#e8f5e9] text-[#2a7f3e]'">{{ item.finish }}</span>
                </div>
                <div class="flex items-center justify-between mt-3">
                  <div class="flex items-center gap-2">
                    <button @click="updateQty(item.item_code, item.qty - 1)" :disabled="item.qty <= 1"
                      :class="darkMode ? 'border-[#2a7f3e]/30 text-gray-400 hover:text-white hover:bg-[#223a28]' : 'border-gray-200 text-gray-500 hover:text-[#1a4d2a] hover:bg-gray-50'"
                      class="w-7 h-7 rounded-lg border flex items-center justify-center transition-all disabled:opacity-30">
                      <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20 12H4"/></svg>
                    </button>
                    <span :class="darkMode ? 'text-white' : 'text-gray-900'" class="text-sm font-bold w-8 text-center">{{ item.qty }}</span>
                    <button @click="updateQty(item.item_code, item.qty + 1)"
                      :class="darkMode ? 'border-[#2a7f3e]/30 text-gray-400 hover:text-white hover:bg-[#223a28]' : 'border-gray-200 text-gray-500 hover:text-[#1a4d2a] hover:bg-gray-50'"
                      class="w-7 h-7 rounded-lg border flex items-center justify-center transition-all">
                      <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4"/></svg>
                    </button>
                  </div>
                  <button @click="removeItem(item.item_code)" class="p-1.5 rounded-lg transition-all" :class="darkMode ? 'text-gray-500 hover:text-red-400 hover:bg-red-400/10' : 'text-gray-400 hover:text-red-500 hover:bg-red-50'">
                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"/></svg>
                  </button>
                </div>
              </div>
            </div>
          </div>

          <!-- Clear Cart -->
          <div class="text-right pt-2">
            <button @click="clearCart" class="text-xs font-semibold transition-colors" :class="darkMode ? 'text-gray-500 hover:text-red-400' : 'text-gray-400 hover:text-red-500'">Clear Cart</button>
          </div>
        </div>

        <!-- Order Summary -->
        <div class="w-full lg:w-auto">
          <div :class="darkMode ? 'bg-[#1a2e1f] border-[#2a7f3e]/20 md:sticky md:top-24' : 'bg-white border-gray-100 md:sticky md:top-24'" class="rounded-2xl p-5 border shadow-sm">
            <h2 :class="darkMode ? 'text-white' : 'text-gray-900'" class="text-lg font-extrabold mb-4">Order Summary</h2>
            <div class="space-y-3 pb-4" :class="darkMode ? 'border-[#2a7f3e]/15' : 'border-gray-100'" style="border-bottom-style: solid; border-bottom-width: 1px;">
              <div class="flex justify-between text-sm">
                <span :class="darkMode ? 'text-gray-400' : 'text-gray-500'">Items ({{ cartCount }})</span>
                <span :class="darkMode ? 'text-white' : 'text-gray-900'" class="font-semibold">₹{{ formatPrice(subtotal) }}</span>
              </div>
              <div class="flex justify-between text-sm">
                <span :class="darkMode ? 'text-gray-400' : 'text-gray-500'">Shipping</span>
                <span class="font-semibold text-[#4caf50]">Free</span>
              </div>
            </div>
            <div class="flex justify-between py-4">
              <span :class="darkMode ? 'text-white' : 'text-gray-900'" class="font-extrabold">Total</span>
              <span class="font-extrabold text-lg text-[#4caf50]">₹{{ formatPrice(subtotal) }}</span>
            </div>
            <button @click="router.push('/indtools/checkout')"
              :disabled="!cartItems.length"
              class="w-full py-3 rounded-xl text-white font-bold transition-all duration-200 shadow-lg shadow-[#2a7f3e]/25 hover:shadow-[#2a7f3e]/40 hover:-translate-y-0.5 disabled:opacity-50 disabled:cursor-not-allowed disabled:hover:translate-y-0 bg-gradient-to-r from-[#2a7f3e] to-[#3d9970] hover:from-[#1a4d2a] hover:to-[#2a7f3e]">
              Proceed to Checkout
            </button>
            <router-link to="/indtools/products" class="block text-center text-xs font-semibold mt-3 py-2 transition-colors" :class="darkMode ? 'text-gray-500 hover:text-[#4caf50]' : 'text-gray-400 hover:text-[#2a7f3e]'">
              Continue Shopping
            </router-link>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { inject, ref } from 'vue'
import { useRouter } from 'vue-router'
import { useCart } from '@/data/cart'

const darkMode = inject('darkMode', ref(false))
const router = useRouter()
const { cartItems, cartCount, subtotal, updateQty, removeItem, clearCart } = useCart()

function formatPrice(val) {
  if (!val) return '0.00'
  return Number(val).toLocaleString('en-IN', { minimumFractionDigits: 2, maximumFractionDigits: 2 })
}

function handleImageError(e) {
  e.target.src = '/assets/indtools_pwa/frontend/indtools_logo_new.png'
}
</script>
