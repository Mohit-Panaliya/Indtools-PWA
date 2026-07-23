<template>
  <div :class="darkMode ? 'bg-[#0f1710]' : 'bg-[#f5f5f5]'" class="min-h-screen">
    <!-- Hero Banner -->
    <div :class="darkMode ? 'bg-[#1a2e1f]' : 'bg-gradient-to-r from-[#1a4d2a] to-[#2a7f3e]'" class="py-10 md:py-14">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <h1 :class="darkMode ? 'text-green-300' : 'text-white'" class="text-3xl md:text-4xl font-extrabold mb-2 tracking-tight">Our Products</h1>
        <div class="flex items-center justify-between flex-wrap gap-3">
          <nav class="flex items-center space-x-2 text-sm">
            <router-link :class="darkMode ? 'text-green-400' : 'text-green-200'" to="/indtools/home" class="hover:underline">Home</router-link>
            <span :class="darkMode ? 'text-green-500' : 'text-green-300'">/</span>
            <span :class="darkMode ? 'text-green-200' : 'text-white'" class="opacity-80">Products</span>
          </nav>
          <p :class="darkMode ? 'text-green-400/70' : 'text-white/70'" class="text-xs font-medium">{{ displayedProducts.length }} products</p>
        </div>
      </div>
    </div>

    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6 md:py-10">
      <!-- Category Filter Pills -->
      <div class="flex flex-wrap gap-2 mb-8">
        <button @click="selectedCategory = ''"
          :class="selectedCategory === '' ? (darkMode ? 'bg-[#4caf50] text-black shadow-lg shadow-[#4caf50]/20' : 'bg-[#2a7f3e] text-white shadow-lg shadow-[#2a7f3e]/20') : (darkMode ? 'bg-[#1a2e1f] text-gray-300 hover:bg-[#223a28] border-[#2a7f3e]/20' : 'bg-white text-gray-600 hover:bg-gray-50 border-gray-200 hover:border-gray-300')"
          class="px-4 py-2.5 rounded-xl text-xs font-bold transition-all duration-200 border hover:-translate-y-0.5 active:translate-y-0">
          All Products
        </button>
        <button v-for="cat in categories" :key="cat.id" @click="selectedCategory = cat.id"
          :class="selectedCategory === cat.id ? (darkMode ? 'bg-[#4caf50] text-black shadow-lg shadow-[#4caf50]/20' : 'bg-[#2a7f3e] text-white shadow-lg shadow-[#2a7f3e]/20') : (darkMode ? 'bg-[#1a2e1f] text-gray-300 hover:bg-[#223a28] border-[#2a7f3e]/20' : 'bg-white text-gray-600 hover:bg-gray-50 border-gray-200 hover:border-gray-300')"
          class="px-4 py-2.5 rounded-xl text-xs font-bold transition-all duration-200 border hover:-translate-y-0.5 active:translate-y-0 flex items-center gap-1.5">
          <span>{{ cat.icon }}</span>
          {{ cat.name }}
          <span :class="selectedCategory === cat.id ? (darkMode ? 'bg-black/20' : 'bg-white/20') : (darkMode ? 'bg-[#2a7f3e]/20 text-[#4caf50]' : 'bg-[#e8f5e9] text-[#2a7f3e]')" class="text-[10px] px-1.5 py-0.5 rounded-md font-bold ml-0.5">
            {{ cat.subProducts?.length || 0 }}
          </span>
        </button>
      </div>

      <!-- Product Grid -->
      <div class="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-4 gap-3 md:gap-5">
        <router-link v-for="(product, idx) in displayedProducts" :key="product.name" :to="'/indtools/product/' + product.route"
          :class="darkMode ? 'bg-[#1a2e1f] hover:bg-[#223a28] border-[#2a7f3e]/20 hover:border-[#2a7f3e]/50' : 'bg-white hover:shadow-2xl border-gray-100 hover:border-gray-200'"
          class="group rounded-2xl border overflow-hidden transition-all duration-300 hover:-translate-y-1.5 flex flex-col"
          :style="{ animationDelay: idx * 30 + 'ms' }">
          <!-- Image -->
          <div :class="darkMode ? 'bg-[#0f1710]' : 'bg-gradient-to-b from-[#f8f9fa] to-[#f0f0f0]'" class="aspect-square relative overflow-hidden flex items-center justify-center p-5">
            <img :src="product.image" :alt="product.name" class="max-w-full max-h-full object-contain group-hover:scale-110 transition-transform duration-500 ease-out" loading="lazy" @error="handleImageError" />
            <div class="absolute inset-0 bg-gradient-to-t from-black/5 via-transparent to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300"></div>
          </div>
          <!-- Info -->
          <div class="p-3 md:p-4 flex-1 flex flex-col">
            <p :class="darkMode ? 'text-[#4caf50]' : 'text-[#3d9970]'" class="text-[9px] font-bold uppercase tracking-widest mb-1">{{ product.category }}</p>
            <h3 :class="darkMode ? 'text-white' : 'text-[#1a4d2a]'" class="font-bold text-sm md:text-[15px] leading-snug mb-2.5 line-clamp-2 flex-1">{{ product.name }}</h3>
            <div class="flex items-center justify-between mt-auto">
              <span :class="darkMode ? 'text-[#4caf50]' : 'text-[#2a7f3e]'" class="text-[11px] font-bold flex items-center gap-1 group-hover:gap-2 transition-all duration-300">
                View Details
                <svg class="w-3.5 h-3.5 transition-transform duration-300 group-hover:translate-x-0.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M9 5l7 7-7 7"/></svg>
              </span>
            </div>
          </div>
        </router-link>
      </div>

      <!-- Empty State -->
      <div v-if="displayedProducts.length === 0" :class="darkMode ? 'bg-[#1a2e1f] border-[#2a7f3e]/20' : 'bg-white border-gray-100'" class="rounded-2xl p-12 md:p-16 text-center border">
        <div class="text-5xl mb-4">🔍</div>
        <h3 :class="darkMode ? 'text-white' : 'text-[#1a4d2a]'" class="text-xl font-bold mb-2">No Products Found</h3>
        <p :class="darkMode ? 'text-gray-400' : 'text-gray-500'" class="text-sm mb-6">No products match the selected category.</p>
        <button @click="selectedCategory = ''" class="bg-[#2a7f3e] hover:bg-[#1a4d2a] text-white px-6 py-3 rounded-xl font-bold transition-all duration-200 text-sm shadow-lg shadow-[#2a7f3e]/20 hover:-translate-y-0.5">View All Products</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, inject, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import { categories as categoryList, allProducts } from '../../data/categories.js'

const darkMode = inject('darkMode', ref(false))
const route = useRoute()
const selectedCategory = ref('')

onMounted(() => {
  if (route.query.category) selectedCategory.value = route.query.category
})

const categories = categoryList
const displayedProducts = computed(() => {
  if (!selectedCategory.value) return allProducts
  return allProducts.filter(p => p.categoryId === selectedCategory.value)
})

const handleImageError = (e) => {
  e.target.src = '/assets/indtools_pwa/frontend/indtools_logo_new.png'
}
</script>
