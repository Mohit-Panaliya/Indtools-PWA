<template>
  <div :class="darkMode ? 'bg-[#0f1710]' : 'bg-[#f5f5f5]'" class="min-h-screen" v-if="product">
    <!-- Breadcrumb -->
    <div :class="darkMode ? 'bg-[#1a2e1f]' : 'bg-gradient-to-r from-[#1a4d2a] to-[#2a7f3e]'" class="py-8 md:py-10">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <nav class="flex items-center flex-wrap gap-1 text-xs md:text-sm">
          <router-link :class="darkMode ? 'text-green-400' : 'text-green-200'" to="/indtools/home" class="hover:underline">Home</router-link>
          <span :class="darkMode ? 'text-green-500' : 'text-green-300'">/</span>
          <router-link :class="darkMode ? 'text-green-400' : 'text-green-200'" to="/indtools/products" class="hover:underline">Products</router-link>
          <span :class="darkMode ? 'text-green-500' : 'text-green-300'">/</span>
          <span :class="darkMode ? 'text-green-200' : 'text-white'" class="opacity-80 truncate max-w-[180px]">{{ product.name }}</span>
        </nav>
      </div>
    </div>

    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6 md:py-10">
      <div class="grid grid-cols-1 md:grid-cols-2 gap-6 md:gap-10 lg:gap-14">
        <!-- Left: Image Gallery -->
        <div class="space-y-3 md:sticky md:top-24 md:self-start">
          <!-- Main Image -->
          <div :class="darkMode ? 'bg-[#1a2e1f] border-[#2a7f3e]/30' : 'bg-white border-gray-100'" class="rounded-2xl border-2 p-4 md:p-8 relative group cursor-zoom-in overflow-hidden transition-all duration-300 hover:border-[#2a7f3e]/50" @click="openLightbox(galleryImages[selectedImage] || product.image)">
            <div class="aspect-square flex items-center justify-center">
              <img :src="galleryImages[selectedImage] || product.image" :alt="product.name" class="max-w-full max-h-full object-contain transition-transform duration-500 group-hover:scale-110" loading="eager" @error="handleImageError" />
            </div>
            <div class="absolute top-4 left-4">
              <span :class="darkMode ? 'bg-[#4caf50] text-black' : 'bg-[#2a7f3e] text-white'" class="text-[10px] font-bold px-3 py-1.5 rounded-full uppercase tracking-wider shadow-lg">{{ product.category }}</span>
            </div>
            <div class="absolute top-4 right-4 opacity-0 group-hover:opacity-100 transition-all duration-300 translate-y-1 group-hover:translate-y-0">
              <div :class="darkMode ? 'bg-black/70' : 'bg-black/50'" class="p-2.5 rounded-full backdrop-blur-sm">
                <svg class="w-5 h-5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0zM10 7v3m0 0v3m0-3h3m-3 0H7"/></svg>
              </div>
            </div>
          </div>
          <!-- Thumbnails (product photos only) -->
          <div v-if="galleryImages.length > 1" class="flex gap-2 overflow-x-auto pb-1 scrollbar-hide">
            <button v-for="(img, i) in galleryImages" :key="i" @click="selectedImage = i"
              :class="selectedImage === i ? (darkMode ? 'border-[#4caf50] bg-[#1a2e1f] shadow-lg shadow-[#4caf50]/20' : 'border-[#2a7f3e] bg-white shadow-lg shadow-[#2a7f3e]/20') : (darkMode ? 'border-[#2a7f3e]/20 bg-[#1a2e1f] hover:border-[#2a7f3e]/50' : 'border-gray-200 bg-white hover:border-gray-300')"
              class="flex-shrink-0 w-16 h-16 md:w-20 md:h-20 rounded-xl border-2 p-1.5 transition-all duration-200">
              <img :src="img" :alt="product.name" class="w-full h-full object-contain" @error="handleImageError" />
            </button>
          </div>
        </div>

        <!-- Right: Product Info -->
        <div class="space-y-5">
          <!-- Title + Brand -->
          <div>
            <p :class="darkMode ? 'text-[#4caf50]' : 'text-[#3d9970]'" class="text-[10px] font-bold uppercase tracking-[0.2em] mb-2">{{ product.category }}</p>
            <h1 :class="darkMode ? 'text-white' : 'text-[#1a4d2a]'" class="text-2xl md:text-3xl font-extrabold leading-tight tracking-tight">{{ product.name }}</h1>
            <div class="flex items-center gap-3 mt-2.5">
              <div class="flex items-center gap-0.5">
                <svg v-for="i in 5" :key="i" class="w-3.5 h-3.5" :class="i <= 4 ? 'text-amber-400' : (darkMode ? 'text-gray-700' : 'text-gray-300')" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/></svg>
              </div>
              <span :class="darkMode ? 'text-gray-500' : 'text-gray-400'" class="text-xs">4.0</span>
              <span class="w-1 h-1 rounded-full" :class="darkMode ? 'bg-gray-700' : 'bg-gray-300'"></span>
              <span class="inline-flex items-center gap-1 text-xs font-semibold text-[#4caf50]">
                <span class="w-1.5 h-1.5 rounded-full bg-[#4caf50] animate-pulse"></span>In Stock
              </span>
            </div>
          </div>

          <hr :class="darkMode ? 'border-[#2a7f3e]/20' : 'border-gray-100'" />

          <!-- Price / Request Quote -->
          <div :class="darkMode ? 'bg-[#1a2e1f]' : 'bg-gradient-to-r from-[#f0faf3] to-[#e8f5e9]'" class="rounded-2xl p-5 border" :style="{ borderColor: darkMode ? 'rgba(42,127,62,0.2)' : 'rgba(42,127,62,0.15)' }">
            <p :class="darkMode ? 'text-gray-500' : 'text-gray-400'" class="text-[10px] font-bold uppercase tracking-widest mb-1">Price on Request</p>
            <p :class="darkMode ? 'text-white' : 'text-[#1a4d2a]'" class="text-xl font-extrabold">Bulk & Custom Orders</p>
            <p :class="darkMode ? 'text-gray-500' : 'text-gray-400'" class="text-xs mt-1">Competitive pricing for all quantities. Get a quote now.</p>
          </div>

          <!-- Selectors -->
          <div class="space-y-3">
            <p :class="darkMode ? 'text-white' : 'text-[#1a4d2a]'" class="text-sm font-bold">Select Options</p>

            <!-- Size Dropdown -->
            <div>
              <label :class="darkMode ? 'text-gray-400' : 'text-gray-500'" class="text-[10px] font-bold uppercase tracking-widest mb-1.5 block">Size</label>
              <div class="relative">
                <select v-model="selectedSize"
                  :class="darkMode ? 'bg-[#0f1710] border-[#2a7f3e]/30 text-white' : 'bg-white border-gray-200 text-[#1a4d2a]'"
                  class="w-full px-4 py-3 text-sm font-semibold border-2 rounded-xl appearance-none focus:outline-none focus:border-[#4caf50] transition-colors cursor-pointer">
                  <option value="">Select Size</option>
                  <option v-for="s in product.sizeOptions" :key="s" :value="s">{{ s }}</option>
                </select>
                <svg class="absolute right-3 top-1/2 -translate-y-1/2 w-4 h-4 pointer-events-none" :class="darkMode ? 'text-gray-500' : 'text-gray-400'" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/></svg>
              </div>
            </div>

            <!-- Grade Dropdown -->
            <div>
              <label :class="darkMode ? 'text-gray-400' : 'text-gray-500'" class="text-[10px] font-bold uppercase tracking-widest mb-1.5 block">Grade</label>
              <div class="relative">
                <select v-model="selectedGrade"
                  :class="darkMode ? 'bg-[#0f1710] border-[#2a7f3e]/30 text-white' : 'bg-white border-gray-200 text-[#1a4d2a]'"
                  class="w-full px-4 py-3 text-sm font-semibold border-2 rounded-xl appearance-none focus:outline-none focus:border-[#4caf50] transition-colors cursor-pointer">
                  <option value="">Select Grade</option>
                  <option v-for="g in product.gradeOptions" :key="g" :value="g">{{ g }}</option>
                </select>
                <svg class="absolute right-3 top-1/2 -translate-y-1/2 w-4 h-4 pointer-events-none" :class="darkMode ? 'text-gray-500' : 'text-gray-400'" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/></svg>
              </div>
            </div>

            <!-- Finish Dropdown -->
            <div>
              <label :class="darkMode ? 'text-gray-400' : 'text-gray-500'" class="text-[10px] font-bold uppercase tracking-widest mb-1.5 block">Surface Finish</label>
              <div class="relative">
                <select v-model="selectedFinish"
                  :class="darkMode ? 'bg-[#0f1710] border-[#2a7f3e]/30 text-white' : 'bg-white border-gray-200 text-[#1a4d2a]'"
                  class="w-full px-4 py-3 text-sm font-semibold border-2 rounded-xl appearance-none focus:outline-none focus:border-[#4caf50] transition-colors cursor-pointer">
                  <option value="">Select Finish</option>
                  <option v-for="f in product.finishOptions" :key="f" :value="f">{{ f }}</option>
                </select>
                <svg class="absolute right-3 top-1/2 -translate-y-1/2 w-4 h-4 pointer-events-none" :class="darkMode ? 'text-gray-500' : 'text-gray-400'" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/></svg>
              </div>
            </div>
          </div>

          <!-- Quantity + Add to Cart -->
          <div class="flex flex-col sm:flex-row gap-3 pt-1">
            <div :class="darkMode ? 'bg-[#0f1710] border-[#2a7f3e]/30' : 'bg-white border-gray-200'" class="flex items-center border-2 rounded-xl overflow-hidden">
              <button @click="qty = Math.max(1, qty - 1)" :class="darkMode ? 'text-gray-400 hover:text-white hover:bg-[#1a2e1f]' : 'text-gray-500 hover:text-[#1a4d2a] hover:bg-gray-50'" class="px-4 py-3 text-lg font-bold transition-all">-</button>
              <input v-model.number="qty" type="number" min="1" :class="darkMode ? 'bg-transparent text-white' : 'bg-transparent text-[#1a4d2a]'" class="w-14 text-center text-sm font-bold border-x-2 outline-none" :style="{ borderColor: darkMode ? 'rgba(42,127,62,0.3)' : '#e5e7eb' }" />
              <button @click="qty++" :class="darkMode ? 'text-gray-400 hover:text-white hover:bg-[#1a2e1f]' : 'text-gray-500 hover:text-[#1a4d2a] hover:bg-gray-50'" class="px-4 py-3 text-lg font-bold transition-all">+</button>
            </div>
            <button @click="addToCart" :disabled="addingToCart" class="flex-1 inline-flex items-center justify-center gap-2.5 bg-gradient-to-r from-[#2a7f3e] to-[#3d9970] hover:from-[#1a4d2a] hover:to-[#2a7f3e] disabled:opacity-50 text-white px-6 py-3.5 rounded-xl font-bold transition-all duration-300 text-sm shadow-xl shadow-[#2a7f3e]/25 hover:shadow-[#2a7f3e]/40 hover:-translate-y-0.5 active:translate-y-0">
              <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 3h2l.4 2M7 13h10l4-8H5.4M7 13L5.4 5M7 13l-2.293 2.293c-.63.63-.184 1.707.707 1.707H17m0 0a2 2 0 100 4 2 2 0 000-4zm-8 2a2 2 0 100 4 2 2 0 000-4z"/></svg>
              {{ addingToCart ? 'Adding...' : 'Add to Cart' }}
            </button>
          </div>

          <!-- Secondary Actions -->
          <div class="flex gap-3">
            <router-link to="/indtools/enquiry" :class="darkMode ? 'bg-[#0f1710] border-[#2a7f3e]/30 text-gray-300 hover:bg-[#1a2e1f]' : 'bg-white border-gray-200 text-gray-700 hover:bg-gray-50'" class="flex-1 inline-flex items-center justify-center gap-2 px-4 py-3 border-2 rounded-xl text-sm font-semibold transition-all duration-200 hover:-translate-y-0.5">
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z"/></svg>
              Enquire
            </router-link>
            <a :href="whatsappLink" target="_blank" class="inline-flex items-center justify-center gap-2 px-4 py-3 bg-[#25d366] hover:bg-[#1da851] text-white rounded-xl text-sm font-semibold transition-all duration-200 hover:-translate-y-0.5 hover:shadow-lg hover:shadow-[#25d366]/30">
              <svg class="w-4 h-4" viewBox="0 0 24 24" fill="currentColor"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>
              WhatsApp
            </a>
          </div>

          <!-- Trust Badges -->
          <div class="grid grid-cols-3 gap-2 pt-1">
            <div v-for="badge in trustBadges" :key="badge.label" :class="darkMode ? 'bg-[#0f1710] border-[#2a7f3e]/15' : 'bg-white border-gray-100'" class="rounded-xl border p-3 text-center">
              <div class="w-8 h-8 mx-auto mb-1.5 rounded-lg bg-[#e8f5e9] flex items-center justify-center">
                <span class="text-sm">{{ badge.icon }}</span>
              </div>
              <p :class="darkMode ? 'text-white' : 'text-[#1a4d2a]'" class="text-[10px] font-bold leading-tight">{{ badge.label }}</p>
              <p :class="darkMode ? 'text-gray-500' : 'text-gray-400'" class="text-[9px] mt-0.5">{{ badge.sub }}</p>
            </div>
          </div>
        </div>
      </div>

      <!-- Tabs: Specs / Description -->
      <div class="mt-8 md:mt-12">
        <div class="flex gap-1 p-1 rounded-xl w-fit" :class="darkMode ? 'bg-[#1a2e1f]' : 'bg-gray-100'">
          <button v-for="tab in ['Specifications', 'Description']" :key="tab" @click="activeTab = tab"
            :class="activeTab === tab ? (darkMode ? 'bg-[#4caf50] text-black shadow-lg' : 'bg-white text-[#1a4d2a] shadow-md') : (darkMode ? 'text-gray-400 hover:text-white' : 'text-gray-500 hover:text-[#1a4d2a]')"
            class="px-5 py-2.5 rounded-lg text-sm font-semibold transition-all duration-200">
            {{ tab }}
          </button>
        </div>

        <!-- Specs Tab -->
        <div v-show="activeTab === 'Specifications'" :class="darkMode ? 'bg-[#1a2e1f] border-[#2a7f3e]/30' : 'bg-white border-gray-100'" class="rounded-2xl border mt-4 overflow-hidden">
          <div class="p-5 md:p-8">
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-0">
              <div v-for="(spec, i) in allSpecs" :key="i" class="flex items-center gap-3 px-4 py-3.5 border-b" :class="[darkMode ? 'border-[#2a7f3e]/10' : 'border-gray-50', i % 2 === 0 ? '' : '']">
                <span :class="darkMode ? 'text-gray-500' : 'text-gray-400'" class="text-xs w-28 flex-shrink-0">{{ spec.label }}</span>
                <span :class="darkMode ? 'text-white' : 'text-[#1a4d2a]'" class="text-sm font-semibold">{{ spec.value }}</span>
              </div>
            </div>
            <!-- Dimension Chart(s): full-width, natural aspect -->
            <div v-if="product.charts && product.charts.length" class="mt-6 space-y-4">
              <p :class="darkMode ? 'text-white' : 'text-[#1a4d2a]'" class="text-sm font-bold">Dimension Chart</p>
              <div v-for="(chart, i) in product.charts" :key="i" :class="darkMode ? 'bg-[#0f1710] border-[#2a7f3e]/20' : 'bg-[#f9fafb] border-gray-100'" class="rounded-xl border overflow-hidden cursor-zoom-in" @click="openLightbox(chart)">
                <img :src="chart" :alt="product.name + ' dimensions'" class="w-full h-auto object-contain" loading="lazy" @error="handleImageError" />
              </div>
            </div>
          </div>
        </div>

        <!-- Description Tab -->
        <div v-show="activeTab === 'Description'" :class="darkMode ? 'bg-[#1a2e1f] border-[#2a7f3e]/30' : 'bg-white border-gray-100'" class="rounded-2xl border mt-4 overflow-hidden">
          <div class="p-5 md:p-8">
            <p :class="darkMode ? 'text-gray-400' : 'text-gray-600'" class="leading-relaxed text-sm">{{ product.longDescription || product.description || 'High-quality industrial fastener manufactured to the highest standards for durability and reliability.' }}</p>
            <div class="mt-6 grid grid-cols-2 sm:grid-cols-4 gap-3">
              <div v-for="feat in features" :key="feat" :class="darkMode ? 'bg-[#0f1710]' : 'bg-[#f9fafb]'" class="rounded-xl p-3 text-center">
                <p :class="darkMode ? 'text-white' : 'text-[#1a4d2a]'" class="text-xs font-bold">{{ feat }}</p>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Related Products -->
      <div v-if="relatedProducts.length" class="mt-10 md:mt-14">
        <div class="flex items-center justify-between mb-6">
          <h2 :class="darkMode ? 'text-white' : 'text-[#1a4d2a]'" class="text-lg md:text-xl font-extrabold">You May Also Like</h2>
          <router-link to="/indtools/products" :class="darkMode ? 'text-[#4caf50]' : 'text-[#2a7f3e]'" class="text-xs font-bold hover:underline flex items-center gap-1">
            View All <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
          </router-link>
        </div>
        <div class="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-4 gap-3 md:gap-5">
          <router-link v-for="rp in relatedProducts" :key="rp.name" :to="'/indtools/product/' + rp.route"
            :class="darkMode ? 'bg-[#1a2e1f] hover:bg-[#223a28] border-[#2a7f3e]/30' : 'bg-white hover:shadow-xl border-gray-100'"
            class="group rounded-2xl border overflow-hidden transition-all duration-300 hover:-translate-y-1.5 hover:shadow-xl">
            <div :class="darkMode ? 'bg-[#0f1710]' : 'bg-[#f8f9fa]'" class="aspect-square flex items-center justify-center p-3 relative overflow-hidden">
              <img :src="rp.image" :alt="rp.name" class="max-w-full max-h-full object-contain group-hover:scale-110 transition-transform duration-500" loading="lazy" @error="handleImageError" />
              <div class="absolute inset-0 bg-gradient-to-t from-black/5 to-transparent opacity-0 group-hover:opacity-100 transition-opacity"></div>
            </div>
            <div class="p-3">
              <p :class="darkMode ? 'text-gray-500' : 'text-gray-400'" class="text-[9px] font-bold uppercase tracking-wider mb-0.5">{{ rp.category }}</p>
              <h3 :class="darkMode ? 'text-white' : 'text-[#1a4d2a]'" class="font-bold text-xs leading-tight line-clamp-2">{{ rp.name }}</h3>
            </div>
          </router-link>
        </div>
      </div>
    </div>

    <!-- Lightbox -->
    <teleport to="body">
      <transition name="fade">
        <div v-if="lightboxOpen" class="fixed inset-0 z-[100] bg-black/95 flex items-center justify-center p-4 backdrop-blur-sm" @click.self="lightboxOpen = false">
          <button @click="lightboxOpen = false" class="absolute top-4 right-4 text-white/70 hover:text-white p-2 rounded-full hover:bg-white/10 transition-all">
            <svg class="w-7 h-7" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg>
          </button>
          <img :src="lightboxSrc" :alt="product.name" class="max-w-full max-h-full object-contain rounded-lg animate-fade-in" @error="handleImageError" />
        </div>
      </transition>
    </teleport>

    <!-- Toast -->
    <teleport to="body">
      <transition name="slide-up">
        <div v-if="showToast" class="fixed bottom-24 md:bottom-8 left-1/2 -translate-x-1/2 md:left-auto md:translate-x-0 md:right-6 bg-gradient-to-r from-[#2a7f3e] to-[#3d9970] text-white px-6 py-3.5 rounded-2xl shadow-2xl shadow-[#2a7f3e]/40 z-[90] flex items-center gap-2.5">
          <div class="w-6 h-6 rounded-full bg-white/20 flex items-center justify-center flex-shrink-0">
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M5 13l4 4L19 7"/></svg>
          </div>
          <span class="text-sm font-bold whitespace-nowrap">Added to cart!</span>
        </div>
      </transition>
    </teleport>
  </div>

  <!-- Not Found -->
  <div v-else-if="!loading" :class="darkMode ? 'bg-[#0f1710]' : 'bg-[#f5f5f5]'" class="min-h-screen flex items-center justify-center">
    <div class="text-center p-8">
      <div class="text-5xl mb-4">🔍</div>
      <h2 :class="darkMode ? 'text-white' : 'text-[#1a4d2a]'" class="text-xl font-bold mb-2">Product Not Found</h2>
      <p :class="darkMode ? 'text-gray-400' : 'text-gray-500'" class="text-sm mb-6">The product you're looking for doesn't exist.</p>
      <router-link to="/indtools/products" class="bg-[#2a7f3e] hover:bg-[#1a4d2a] text-white px-6 py-2.5 rounded-lg font-semibold text-sm transition-colors">Browse Products</router-link>
    </div>
  </div>

  <!-- Loading -->
  <div v-else :class="darkMode ? 'bg-[#0f1710]' : 'bg-[#f5f5f5]'" class="min-h-screen flex items-center justify-center">
    <div class="text-center">
      <div class="animate-spin w-8 h-8 border-4 border-[#2a7f3e] border-t-transparent rounded-full mx-auto mb-3"></div>
      <p :class="darkMode ? 'text-gray-400' : 'text-gray-500'" class="text-sm">Loading...</p>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, inject, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import { allProducts, categories, WHATSAPP_NUMBER } from '../../data/categories.js'
import { useCart } from '../../data/cart.js'

const darkMode = inject('darkMode', ref(false))
const route = useRoute()
const qty = ref(1)
const addingToCart = ref(false)
const showToast = ref(false)
const lightboxOpen = ref(false)
const lightboxSrc = ref('')
function openLightbox(src) {
  lightboxSrc.value = src || ''
  lightboxOpen.value = true
}
const selectedImage = ref(0)
const selectedSize = ref('')
const selectedGrade = ref('')
const selectedFinish = ref('')
const activeTab = ref('Specifications')
const loading = ref(true)

const product = computed(() => allProducts.find(p => p.route === route.params.code))
const productCategory = computed(() => categories.find(c => c.id === product.value?.categoryId))

const trustBadges = [
  { icon: '🚚', label: 'Fast Delivery', sub: 'Pan India' },
  { icon: '🛡️', label: 'Quality Assured', sub: 'ISO Certified' },
  { icon: '💬', label: 'Expert Support', sub: '24/7 Available' },
]

const features = ['ISO 9001:2015', 'Made in India', 'Bulk Available', 'Custom Sizes']

const allSpecs = computed(() => {
  if (!product.value) return []
  const specs = [
    { label: 'Product Name', value: product.value.name },
    { label: 'Category', value: product.value.category },
    { label: 'Brand', value: 'INDTOOLS' },
    { label: 'SKU', value: product.value.itemCode || makeSku(product.value.name) },
    { label: 'Selected Size', value: selectedSize.value || productCategory.value?.sizeRange || 'Various' },
    { label: 'Selected Grade', value: selectedGrade.value || productCategory.value?.grade || 'Industrial Grade' },
    { label: 'Surface Finish', value: selectedFinish.value || productCategory.value?.finishing || 'Standard' },
    { label: 'Material', value: 'Carbon Steel / Alloy Steel / Stainless Steel' },
    { label: 'Application', value: 'Industrial / Construction / Automotive' },
    { label: 'Origin', value: 'Gujarat, India' },
  ]
  if (product.value.standards && product.value.standards.length) {
    specs.push({ label: 'Standards', value: product.value.standards.join(' | ') })
  }
  if (product.value.dimensions && product.value.dimensions.length) {
    specs.push({ label: 'Dimensions', value: product.value.dimensions.join(' | ') })
  }
  return specs
})

const galleryImages = computed(() => {
  if (!product.value) return []
  // photo gallery only — dimension charts render separately, full-width
  if (product.value.images && product.value.images.length) return product.value.images
  const imgs = [product.value.image]
  const cat = productCategory.value
  if (cat) {
    cat.subProducts.filter(sp => sp.image !== product.value.image).slice(0, 4).forEach(sp => imgs.push(sp.image))
  }
  return imgs
})

const relatedProducts = computed(() => {
  if (!product.value) return []
  return allProducts.filter(p => p.categoryId === product.value.categoryId && p.route !== product.value.route).slice(0, 6)
})

const whatsappLink = computed(() => {
  const msg = encodeURIComponent(`Hi, I'm interested in ${product.value?.name || 'your product'}${selectedSize.value ? ` (Size: ${selectedSize.value})` : ''}${selectedGrade.value ? ` (Grade: ${selectedGrade.value})` : ''}. Please share details.`)
  return `https://wa.me/${WHATSAPP_NUMBER.replace('+', '')}?text=${msg}`
})

function makeSku(name) {
  return 'IND-' + name.replace(/[^a-zA-Z0-9]/g, '').substring(0, 12).toUpperCase()
}

function handleImageError(e) {
  e.target.src = '/assets/indtools_pwa/frontend/indtools_logo_new.png'
}

const { addToCart: cartAdd } = useCart()

async function addToCart() {
  addingToCart.value = true
  try {
    cartAdd({
      item_code: product.value.itemCode || product.value.name,
      name: product.value.name,
      image: product.value.image,
      category: product.value.category,
      qty: qty.value,
      size: selectedSize.value,
      grade: selectedGrade.value,
      finish: selectedFinish.value,
    })
    showToast.value = true
    setTimeout(() => { showToast.value = false }, 3000)
  } catch (e) {
    console.error(e)
  } finally {
    addingToCart.value = false
  }
}

onMounted(() => { setTimeout(() => { loading.value = false }, 400) })
</script>

<style scoped>
.scrollbar-hide::-webkit-scrollbar { display: none; }
.scrollbar-hide { -ms-overflow-style: none; scrollbar-width: none; }
.fade-enter-active, .fade-leave-active { transition: opacity 0.3s ease; }
.fade-enter-from, .fade-leave-to { opacity: 0; }
.slide-up-enter-active { transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1); }
.slide-up-leave-active { transition: all 0.3s ease-in; }
.slide-up-enter-from { opacity: 0; transform: translate(-50%, 20px); }
.slide-up-leave-to { opacity: 0; transform: translate(-50%, 10px); }
@keyframes fade-in { from { opacity: 0; transform: scale(0.95); } to { opacity: 1; transform: scale(1); } }
.animate-fade-in { animation: fade-in 0.3s ease-out; }
</style>
