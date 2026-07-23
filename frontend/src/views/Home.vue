<template>
  <div :class="darkMode ? 'bg-[#0f1710]' : 'bg-[#f5f5f5]'" class="min-h-screen pb-20 md:pb-0">
    <!-- Hero Slider -->
    <div class="relative w-full h-[50vh] sm:h-[60vh] md:h-[70vh] overflow-hidden">
      <div
        class="absolute inset-0 transition-opacity duration-700 ease-in-out"
        v-for="(slide, index) in heroSlides"
        :key="index"
        :class="{ 'opacity-100 z-10': index === currentSlide, 'opacity-0 z-0': index !== currentSlide }"
      >
        <img :src="slide.image" :alt="slide.title" class="w-full h-full object-cover" />
        <div class="absolute inset-0 bg-gradient-to-r from-[#1a4d2a]/80 to-transparent"></div>
        <div class="absolute inset-0 flex items-center">
          <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 w-full">
            <div class="max-w-xl">
              <span class="inline-block bg-[#4caf50] text-white text-xs font-bold px-3 py-1 rounded-full mb-4 uppercase tracking-wide">{{ slide.badge }}</span>
              <h1 class="text-3xl sm:text-4xl md:text-5xl lg:text-6xl font-bold text-white mb-4 leading-tight drop-shadow-lg">{{ slide.title }}</h1>
              <p class="text-sm sm:text-base md:text-lg text-white/90 mb-6 drop-shadow">{{ slide.subtitle }}</p>
              <div class="flex flex-wrap gap-3">
                <router-link to="/indtools/products" class="inline-flex items-center gap-2 bg-[#4caf50] hover:bg-[#3d9970] text-white px-6 py-3 rounded-lg font-semibold transition-colors shadow-lg text-sm sm:text-base">
                  <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 11V7a4 4 0 00-8 0v4M5 9h14l1 12H4L5 9z"/></svg>
                  Browse Products
                </router-link>
                <router-link to="/enquiry" class="inline-flex items-center gap-2 bg-white/20 hover:bg-white/30 text-white px-6 py-3 rounded-lg font-semibold backdrop-blur-sm transition-colors border border-white/30 text-sm sm:text-base">
                  Get Quote
                </router-link>
              </div>
            </div>
          </div>
        </div>
      </div>
      <!-- Nav Arrows -->
      <button @click="prevSlide" class="absolute left-4 top-1/2 -translate-y-1/2 z-20 bg-white/20 hover:bg-white/40 backdrop-blur-sm text-white w-10 h-10 md:w-12 md:h-12 rounded-full flex items-center justify-center transition-all">
        <svg class="w-5 h-5 md:w-6 md:h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"/></svg>
      </button>
      <button @click="nextSlide" class="absolute right-4 top-1/2 -translate-y-1/2 z-20 bg-white/20 hover:bg-white/40 backdrop-blur-sm text-white w-10 h-10 md:w-12 md:h-12 rounded-full flex items-center justify-center transition-all">
        <svg class="w-5 h-5 md:w-6 md:h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
      </button>
      <!-- Dots -->
      <div class="absolute bottom-4 left-1/2 -translate-x-1/2 z-20 flex space-x-2">
        <button v-for="(_, i) in heroSlides" :key="i" @click="currentSlide = i" :class="i === currentSlide ? 'w-8 bg-[#4caf50]' : 'w-3 bg-white/50'" class="h-3 rounded-full transition-all duration-300"></button>
      </div>
    </div>

    <!-- Stats Bar -->
    <div :class="darkMode ? 'bg-[#1a2e1f] border-[#2a7f3e]/20' : 'bg-white border-[#2a7f3e]/10'" class="border-y shadow-sm">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="grid grid-cols-2 md:grid-cols-4 divide-x divide-y md:divide-y-0" :class="darkMode ? 'divide-[#2a7f3e]/20' : 'divide-gray-100'">
          <div v-for="stat in stats" :key="stat.label" class="flex items-center gap-3 p-4 md:p-6">
            <div class="w-10 h-10 md:w-12 md:h-12 rounded-xl flex items-center justify-center" :class="darkMode ? 'bg-[#2a7f3e]/20' : 'bg-[#e8f5e9]'">
              <component :is="stat.icon" class="w-5 h-5 md:w-6 md:h-6 text-[#2a7f3e]" />
            </div>
            <div>
              <div :class="darkMode ? 'text-green-300' : 'text-[#1a4d2a]'" class="text-lg md:text-2xl font-bold">{{ stat.value }}</div>
              <div :class="darkMode ? 'text-gray-400' : 'text-gray-500'" class="text-xs md:text-sm">{{ stat.label }}</div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Categories -->
    <section class="py-12 md:py-20">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-10 md:mb-14">
          <span :class="darkMode ? 'text-[#4caf50]' : 'text-[#2a7f3e]'" class="text-sm font-bold uppercase tracking-widest">Our Range</span>
          <h2 :class="darkMode ? 'text-white' : 'text-[#1a4d2a]'" class="text-2xl md:text-4xl font-bold mt-2 mb-4">Product Categories</h2>
          <div class="w-20 h-1 bg-[#4caf50] mx-auto rounded-full"></div>
        </div>
        <div class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 gap-4 md:gap-6">
          <router-link
            v-for="cat in categories"
            :key="cat.slug"
            :to="'/indtools/products?category=' + cat.slug"
            :class="darkMode ? 'bg-[#1a2e1f] hover:bg-[#223a28] border-[#2a7f3e]/30' : 'bg-white hover:shadow-xl border-gray-100'"
            class="group rounded-2xl border p-4 md:p-6 text-center transition-all duration-300 cursor-pointer hover:-translate-y-1"
          >
            <div class="w-14 h-14 md:w-16 md:h-16 mx-auto mb-3 md:mb-4 rounded-2xl flex items-center justify-center text-2xl md:text-3xl transition-transform duration-300 group-hover:scale-110" :class="darkMode ? 'bg-[#2a7f3e]/20' : 'bg-[#e8f5e9]'">
              {{ cat.icon }}
            </div>
            <h3 :class="darkMode ? 'text-white' : 'text-[#1a4d2a]'" class="font-bold text-sm md:text-base mb-1">{{ cat.name }}</h3>
            <p :class="darkMode ? 'text-[#4caf50]' : 'text-[#3d9970]'" class="text-xs font-medium">{{ cat.count }} Products</p>
          </router-link>
        </div>
      </div>
    </section>

    <!-- Why Choose Us -->
    <section :class="darkMode ? 'bg-[#1a2e1f]' : 'bg-white'" class="py-12 md:py-20">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-10 md:mb-14">
          <span :class="darkMode ? 'text-[#4caf50]' : 'text-[#2a7f3e]'" class="text-sm font-bold uppercase tracking-widest">Why Us</span>
          <h2 :class="darkMode ? 'text-white' : 'text-[#1a4d2a]'" class="text-2xl md:text-4xl font-bold mt-2 mb-4">Why Choose INDTOOLS?</h2>
          <div class="w-20 h-1 bg-[#4caf50] mx-auto rounded-full"></div>
        </div>
        <div class="grid sm:grid-cols-2 lg:grid-cols-4 gap-6">
          <div v-for="item in whyUs" :key="item.title" :class="darkMode ? 'bg-[#0f1710] border-[#2a7f3e]/20' : 'bg-[#f9fafb] border-gray-100'" class="rounded-2xl border p-6 text-center hover:-translate-y-1 transition-transform">
            <div class="w-14 h-14 mx-auto mb-4 rounded-2xl bg-[#e8f5e9] dark:bg-[#2a7f3e]/20 flex items-center justify-center">
              <span class="text-2xl">{{ item.icon }}</span>
            </div>
            <h3 :class="darkMode ? 'text-white' : 'text-[#1a4d2a]'" class="font-bold mb-2">{{ item.title }}</h3>
            <p :class="darkMode ? 'text-gray-400' : 'text-gray-500'" class="text-sm leading-relaxed">{{ item.desc }}</p>
          </div>
        </div>
      </div>
    </section>

    <!-- About INDTOOLS -->
    <section class="py-12 md:py-20">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="grid md:grid-cols-2 gap-10 items-center">
          <div>
            <span :class="darkMode ? 'text-[#4caf50]' : 'text-[#2a7f3e]'" class="text-sm font-bold uppercase tracking-widest">About Us</span>
            <h2 :class="darkMode ? 'text-white' : 'text-[#1a4d2a]'" class="text-2xl md:text-4xl font-bold mt-2 mb-6">Leading Manufacturer of Industrial Fasteners</h2>
            <p :class="darkMode ? 'text-gray-400' : 'text-gray-600'" class="mb-4 leading-relaxed">
              INDTOOLS has been a trusted name in industrial fasteners since 1992. Based in the heart of Gujarat's industrial hub, we specialize in manufacturing and supplying high-quality bolts, nuts, washers, screws, and specialized fasteners.
            </p>
            <p :class="darkMode ? 'text-gray-400' : 'text-gray-600'" class="mb-6 leading-relaxed">
              Our state-of-the-art facility at GIDC Anand is equipped with modern machinery and quality testing equipment to ensure every product meets international standards.
            </p>
            <div class="flex flex-wrap gap-4">
              <router-link to="/about" class="inline-flex items-center gap-2 bg-[#2a7f3e] hover:bg-[#1a4d2a] text-white px-6 py-3 rounded-lg font-semibold transition-colors text-sm">
                Learn More
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"/></svg>
              </router-link>
              <a :href="'tel:+919825783701'" class="inline-flex items-center gap-2 border-2 border-[#2a7f3e] text-[#2a7f3e] hover:bg-[#2a7f3e] hover:text-white px-6 py-3 rounded-lg font-semibold transition-colors text-sm">
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/></svg>
                Call Now
              </a>
            </div>
          </div>
          <div :class="darkMode ? 'bg-[#1a2e1f]' : 'bg-[#e8f5e9]'" class="rounded-3xl p-8 md:p-12 relative overflow-hidden">
            <div class="absolute top-0 right-0 w-40 h-40 bg-[#4caf50]/10 rounded-full -translate-y-1/2 translate-x-1/2"></div>
            <div class="absolute bottom-0 left-0 w-32 h-32 bg-[#4caf50]/10 rounded-full translate-y-1/2 -translate-x-1/2"></div>
            <div class="relative space-y-6">
              <div v-for="feat in aboutFeatures" :key="feat.label" class="flex items-center gap-4">
                <div class="w-12 h-12 rounded-xl bg-[#2a7f3e] flex items-center justify-center flex-shrink-0">
                  <span class="text-xl text-white">{{ feat.icon }}</span>
                </div>
                <div>
                  <h4 :class="darkMode ? 'text-white' : 'text-[#1a4d2a]'" class="font-bold">{{ feat.label }}</h4>
                  <p :class="darkMode ? 'text-gray-400' : 'text-gray-500'" class="text-sm">{{ feat.desc }}</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Contact CTA -->
    <section class="py-12 md:py-20">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div :class="darkMode ? 'bg-[#1a2e1f] border-[#2a7f3e]/30' : 'bg-gradient-to-r from-[#1a4d2a] to-[#2a7f3e]'" class="rounded-3xl p-8 md:p-12 text-center relative overflow-hidden">
          <div class="absolute inset-0 opacity-10">
            <div class="absolute top-10 left-10 w-32 h-32 border border-white rounded-full"></div>
            <div class="absolute bottom-10 right-10 w-48 h-48 border border-white rounded-full"></div>
          </div>
          <div class="relative">
            <h2 class="text-2xl md:text-3xl font-bold text-white mb-4">Ready to Place an Order?</h2>
            <p class="text-white/80 mb-8 max-w-xl mx-auto">Contact us for bulk orders, custom specifications, or any inquiries. Our team is ready to help.</p>
            <div class="flex flex-wrap justify-center gap-4">
              <router-link to="/enquiry" class="inline-flex items-center gap-2 bg-white text-[#1a4d2a] hover:bg-gray-100 px-8 py-3 rounded-lg font-bold transition-colors shadow-lg text-sm">
                Send Enquiry
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"/></svg>
              </router-link>
              <a :href="'https://wa.me/919825783701'" target="_blank" class="inline-flex items-center gap-2 bg-[#25d366] hover:bg-[#1da851] text-white px-8 py-3 rounded-lg font-bold transition-colors shadow-lg text-sm">
                WhatsApp Us
              </a>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted, h, inject } from 'vue'
import { categories as categoryList } from '../data/categories.js'

const darkMode = inject('darkMode', ref(false))

const currentSlide = ref(0)
let slideInterval = null

const heroSlides = [
  { image: '/assets/indtools_pwa/frontend/banners/1.png', badge: 'Since 1992', title: 'Premium Industrial Fasteners', subtitle: 'Manufactured in Gujarat, trusted worldwide for quality and precision.' },
  { image: '/assets/indtools_pwa/frontend/banners/2.png', badge: 'ISO Certified', title: 'Complete Fastener Solutions', subtitle: 'Bolts, nuts, washers, screws, rivets, pins, and socket products.' },
  { image: '/assets/indtools_pwa/frontend/banners/3.png', badge: 'Made in India', title: 'Trusted by Industries', subtitle: 'Serving automotive, construction, oil & gas, and heavy engineering sectors.' },
  { image: '/assets/indtools_pwa/frontend/banners/4.png', badge: 'Quality First', title: 'Custom & Standard Fasteners', subtitle: 'From standard grades to specialized alloys, we deliver precision.' }
]

const nextSlide = () => { currentSlide.value = (currentSlide.value + 1) % heroSlides.length }
const prevSlide = () => { currentSlide.value = (currentSlide.value - 1 + heroSlides.length) % heroSlides.length }

onMounted(() => { slideInterval = setInterval(nextSlide, 5000) })
onUnmounted(() => { clearInterval(slideInterval) })

// Dynamic icon components
const IconFactory = (paths) => ({
  render() {
    return h('svg', { class: 'w-6 h-6', fill: 'none', stroke: 'currentColor', viewBox: '0 0 24 24' },
      paths.map(d => h('path', { 'stroke-linecap': 'round', 'stroke-linejoin': 'round', 'stroke-width': '2', d }))
    )
  }
})
const IconCheck = IconFactory(['M5 13l4 4L19 7'])
const IconBox = IconFactory(['M20 7l-8-4-8 4m16 0l-8 4m8-4v10l-8 4m0-10L4 7m8 4v10M4 7v10l8 4'])
const IconClock = IconFactory(['M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z'])
const IconGlobe = IconFactory(['M3.055 11H5a2 2 0 012 2v1a2 2 0 002 2 2 2 0 012 2v2.945M8 3.935V5.5A2.5 2.5 0 0010.5 8h.5a2 2 0 012 2 2 2 0 104 0 2 2 0 012-2h1.064M15 20.488V18a2 2 0 012-2h3.064M21 12a9 9 0 11-18 0 9 9 0 0118 0z'])

const stats = [
  { value: '30+', label: 'Years Experience', icon: IconCheck },
  { value: '72+', label: 'Product Varieties', icon: IconBox },
  { value: '24/7', label: 'Support Available', icon: IconClock },
  { value: 'PAN', label: 'India Coverage', icon: IconGlobe }
]

const whyUs = [
  { icon: '🏭', title: 'In-House Manufacturing', desc: 'State-of-the-art facility at GIDC Anand, Gujarat with modern CNC machinery.' },
  { icon: '✅', title: 'Quality Assured', desc: 'ISO certified with strict quality control at every production stage.' },
  { icon: '🚚', title: 'Pan-India Delivery', desc: 'Fast and reliable logistics network covering all major industrial hubs.' },
  { icon: '💰', title: 'Competitive Pricing', desc: 'Direct manufacturer pricing with no middlemen for best value.' }
]

const aboutFeatures = [
  { icon: '⚙️', label: 'ISO 9001:2015 Certified', desc: 'Quality management system certified' },
  { icon: '🏭', label: 'In-House R&D', desc: 'Continuous product development & improvement' },
  { icon: '📦', label: 'Large Stock', desc: 'Ready inventory for fast dispatch' },
  { icon: '🤝', label: 'OEM Partnerships', desc: 'Trusted by leading OEMs across India' }
]

const categories = categoryList.map(cat => ({
  ...cat,
  count: cat.subProducts ? cat.subProducts.length : 0
}))
</script>
