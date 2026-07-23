<template>
  <div :class="[darkMode ? 'dark' : '', 'min-h-screen']" :style="darkMode ? 'background:#111827;color:#e5e7eb' : 'background:#f5f5f5;color:#333'">
    <!-- Desktop Header -->
    <header class="mobile-hide fixed top-0 left-0 right-0 z-50">
      <!-- Green accent bar -->
      <div class="h-1 bg-gradient-to-r from-[#1a4d2a] via-[#2a7f3e] to-[#4caf50]"></div>
      <div class="transition-colors duration-300" :class="darkMode ? 'bg-gray-900/95 backdrop-blur-xl shadow-lg shadow-black/30' : 'bg-white/95 backdrop-blur-xl shadow-md'">
        <div class="container">
          <div class="flex items-center justify-between h-16 lg:h-[4.5rem]">
            <!-- Logo -->
            <router-link to="/indtools/home" class="flex items-center gap-3 flex-shrink-0 group">
              <img :src="darkMode ? '/assets/indtools_pwa/frontend/INDTOOLS_WHITE_LOGO.png' : '/assets/indtools_pwa/frontend/INDTOOLS_BLACK_LOGO.png'" alt="INDTOOLS" class="h-9 lg:h-11 w-auto transition-transform duration-300 group-hover:scale-105" />
              <div class="hidden lg:flex flex-col leading-none">
                <span class="text-[10px] font-medium tracking-[0.2em] uppercase" :class="darkMode ? 'text-gray-500' : 'text-gray-400'">Industrial Tools</span>
              </div>
            </router-link>

            <!-- Nav -->
            <nav class="flex items-center gap-1 lg:gap-1.5 flex-1 justify-center">
              <router-link to="/indtools/home" class="nav-link text-sm font-medium" :class="darkMode ? 'text-gray-400' : 'text-gray-600'" active-class="active">Home</router-link>
              <router-link to="/indtools/about" class="nav-link text-sm font-medium" :class="darkMode ? 'text-gray-400' : 'text-gray-600'" active-class="active">About</router-link>

              <!-- Products Mega Dropdown -->
              <div class="relative" @mouseenter="productsOpen = true" @mouseleave="productsOpen = false">
                <button class="nav-link text-sm font-medium flex items-center gap-1.5" :class="darkMode ? 'text-gray-400' : 'text-gray-600'">
                  Products
                  <svg class="w-3.5 h-3.5 transition-transform duration-200" :class="productsOpen ? 'rotate-180' : ''" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/></svg>
                </button>
                <transition name="mega">
                  <div v-if="productsOpen" class="absolute top-full left-1/2 -translate-x-1/2 mt-3 w-[520px] rounded-2xl shadow-2xl border py-4 z-50" :class="darkMode ? 'bg-gray-800 border-gray-700' : 'bg-white border-gray-100'">
                    <div class="grid grid-cols-2 gap-1 px-3">
                      <router-link v-for="cat in categories" :key="cat.id" :to="`/indtools/products/${cat.id}`" class="flex items-center gap-3 px-3 py-2.5 rounded-xl text-sm transition-all duration-200" :class="darkMode ? 'text-gray-300 hover:bg-gray-700 hover:text-[#4caf50]' : 'text-gray-700 hover:bg-[#f0faf3] hover:text-[#2a7f3e]'" @click="productsOpen = false">
                        <div class="w-8 h-8 rounded-lg flex items-center justify-center flex-shrink-0" :class="darkMode ? 'bg-gray-700' : 'bg-[#f0faf3]'">
                          <img :src="cat.image" :alt="cat.name" class="w-5 h-5 object-contain" />
                        </div>
                        <span class="font-medium">{{ cat.name }}</span>
                      </router-link>
                    </div>
                    <div class="mt-3 pt-3 px-3 border-t" :class="darkMode ? 'border-gray-700' : 'border-gray-100'">
                      <router-link to="/indtools/products" class="flex items-center justify-center gap-2 py-2.5 rounded-xl text-sm font-semibold transition-all" :class="darkMode ? 'bg-gray-700 text-[#4caf50] hover:bg-gray-600' : 'bg-[#f0faf3] text-[#2a7f3e] hover:bg-[#e0f5e8]'" @click="productsOpen = false">
                        View All Products
                        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"/></svg>
                      </router-link>
                    </div>
                  </div>
                </transition>
              </div>

              <router-link to="/indtools/contact" class="nav-link text-sm font-medium" :class="darkMode ? 'text-gray-400' : 'text-gray-600'" active-class="active">Contact</router-link>
              <router-link to="/indtools/enquiry" class="nav-link text-sm font-medium" :class="darkMode ? 'text-gray-400' : 'text-gray-600'" active-class="active">Enquiry</router-link>
            </nav>

            <!-- Right actions -->
            <div class="flex items-center gap-1.5">
              <button @click="toggleDark" class="p-2.5 rounded-xl transition-all duration-200" :class="darkMode ? 'text-yellow-400 hover:bg-gray-800' : 'text-gray-400 hover:bg-gray-100 hover:text-gray-600'" :title="darkMode ? 'Light mode' : 'Dark mode'">
                <svg v-if="darkMode" class="w-[18px] h-[18px]" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z"/></svg>
                <svg v-else class="w-[18px] h-[18px]" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z"/></svg>
              </button>

              <a href="/assets/indtools_pwa/frontend/Catalog.pdf" target="_blank" rel="noopener" class="hidden lg:inline-flex items-center gap-2 px-4 py-2.5 rounded-xl text-sm font-semibold transition-all duration-200" :class="darkMode ? 'bg-[#4caf50]/10 text-[#4caf50] hover:bg-[#4caf50]/20' : 'bg-[#2a7f3e]/5 text-[#2a7f3e] hover:bg-[#2a7f3e]/10'">
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 10v6m0 0l-3-3m3 3l3-3m2 8H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/></svg>
                Catalog
              </a>

              <!-- Cart -->
              <router-link to="/indtools/cart" class="relative p-2.5 rounded-xl transition-all duration-200" :class="darkMode ? 'text-gray-400 hover:bg-gray-800 hover:text-[#4caf50]' : 'text-gray-400 hover:bg-gray-100 hover:text-[#2a7f3e]'">
                <svg class="w-[18px] h-[18px]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 3h2l.4 2M7 13h10l4-8H5.4M7 13L5.4 5M7 13l-2.293 2.293c-.63.63-.184 1.707.707 1.707H17m0 0a2 2 0 100 4 2 2 0 000-4zm-8 2a2 2 0 100 4 2 2 0 000-4z"/></svg>
                <span v-if="cartCount > 0" class="absolute -top-0.5 -right-0.5 min-w-[18px] h-[18px] text-[10px] font-bold text-white bg-[#e53935] rounded-full flex items-center justify-center px-1 ring-2" :class="darkMode ? 'ring-gray-900' : 'ring-white'">{{ cartCount > 99 ? '99+' : cartCount }}</span>
              </router-link>

              <!-- User -->
              <router-link :to="isLoggedIn ? '/indtools/profile' : '/indtools/login'" class="p-2.5 rounded-xl transition-all duration-200" :class="darkMode ? 'text-gray-400 hover:bg-gray-800 hover:text-[#4caf50]' : 'text-gray-400 hover:bg-gray-100 hover:text-[#2a7f3e]'">
                <svg class="w-[18px] h-[18px]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"/></svg>
              </router-link>
            </div>
          </div>
        </div>
      </div>
    </header>

    <!-- Mobile Header -->
    <header class="desktop-hide fixed top-0 left-0 right-0 z-50">
      <div class="h-[3px] bg-gradient-to-r from-[#1a4d2a] via-[#2a7f3e] to-[#4caf50]"></div>
      <div class="flex items-center justify-between h-14 px-4 transition-colors" :class="darkMode ? 'bg-gray-900/95 backdrop-blur-xl shadow-lg shadow-black/30' : 'bg-white/95 backdrop-blur-xl shadow-sm'">
        <router-link to="/indtools/home" class="flex items-center">
          <img :src="darkMode ? '/assets/indtools_pwa/frontend/INDTOOLS_WHITE_LOGO.png' : '/assets/indtools_pwa/frontend/INDTOOLS_BLACK_LOGO.png'" alt="INDTOOLS" class="h-8 w-auto" />
        </router-link>
        <div class="flex items-center gap-1">
          <button @click="toggleDark" class="p-2.5 rounded-xl transition-all" :class="darkMode ? 'text-yellow-400' : 'text-gray-400'">
            <svg v-if="darkMode" class="w-5 h-5" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z"/></svg>
            <svg v-else class="w-5 h-5" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z"/></svg>
          </button>
          <router-link to="/indtools/cart" class="relative p-2.5 rounded-xl transition-all" :class="darkMode ? 'text-gray-400' : 'text-gray-400'">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 3h2l.4 2M7 13h10l4-8H5.4M7 13L5.4 5M7 13l-2.293 2.293c-.63.63-.184 1.707.707 1.707H17m0 0a2 2 0 100 4 2 2 0 000-4zm-8 2a2 2 0 100 4 2 2 0 000-4z"/></svg>
            <span v-if="cartCount > 0" class="absolute -top-0.5 -right-0.5 min-w-[16px] h-[16px] text-[9px] font-bold text-white bg-[#e53935] rounded-full flex items-center justify-center px-0.5 ring-2" :class="darkMode ? 'ring-gray-900' : 'ring-white'">{{ cartCount > 99 ? '99+' : cartCount }}</span>
          </router-link>
        </div>
      </div>
    </header>

    <!-- Main Content -->
    <main class="pt-[3.25rem] md:pt-[4rem] pb-20 md:pb-0">
      <router-view :darkMode="darkMode" />
    </main>

    <!-- Footer -->
    <footer class="py-12 transition-colors" :class="darkMode ? 'bg-gray-900 border-t border-gray-800' : 'bg-[#2a7f3e]'">
      <div class="container">
        <div class="grid grid-cols-1 md:grid-cols-4 gap-8">
          <div>
            <img :src="'/assets/indtools_pwa/frontend/INDTOOLS_WHITE_LOGO.png'" alt="INDTOOLS" class="h-10 w-auto mb-4" />
            <p class="mb-4" :class="darkMode ? 'text-gray-400' : 'text-white/80'">Your trusted partner for high-quality industrial tools and fasteners.</p>
            <a href="/assets/indtools_pwa/frontend/Catalog.pdf" download class="inline-block border px-4 py-2 rounded-lg text-sm font-medium transition-all" :class="darkMode ? 'border-gray-600 text-gray-300 hover:bg-gray-800' : 'border-white/30 text-white hover:bg-white hover:text-[#2a7f3e]'">Download Catalog</a>
          </div>
          <div>
            <h4 class="text-sm font-semibold mb-4 uppercase tracking-wider" :class="darkMode ? 'text-gray-300' : 'text-white'">Products</h4>
            <ul class="space-y-2.5">
              <li v-for="cat in categories" :key="cat.id"><router-link :to="`/indtools/products/${cat.id}`" class="text-sm transition-colors" :class="darkMode ? 'text-gray-500 hover:text-white' : 'text-white/60 hover:text-white'">{{ cat.name }}</router-link></li>
            </ul>
          </div>
          <div>
            <h4 class="text-sm font-semibold mb-4 uppercase tracking-wider" :class="darkMode ? 'text-gray-300' : 'text-white'">Quick Links</h4>
            <ul class="space-y-2.5">
              <li><router-link to="/indtools/home" class="text-sm transition-colors" :class="darkMode ? 'text-gray-500 hover:text-white' : 'text-white/60 hover:text-white'">Home</router-link></li>
              <li><router-link to="/indtools/about" class="text-sm transition-colors" :class="darkMode ? 'text-gray-500 hover:text-white' : 'text-white/60 hover:text-white'">About Us</router-link></li>
              <li><router-link to="/indtools/products" class="text-sm transition-colors" :class="darkMode ? 'text-gray-500 hover:text-white' : 'text-white/60 hover:text-white'">All Products</router-link></li>
              <li><router-link to="/indtools/contact" class="text-sm transition-colors" :class="darkMode ? 'text-gray-500 hover:text-white' : 'text-white/60 hover:text-white'">Contact Us</router-link></li>
              <li><router-link to="/indtools/enquiry" class="text-sm transition-colors" :class="darkMode ? 'text-gray-500 hover:text-white' : 'text-white/60 hover:text-white'">Quick Enquiry</router-link></li>
            </ul>
          </div>
          <div>
            <h4 class="text-sm font-semibold mb-4 uppercase tracking-wider" :class="darkMode ? 'text-gray-300' : 'text-white'">Contact Info</h4>
            <ul class="space-y-3 text-sm" :class="darkMode ? 'text-gray-500' : 'text-white/60'">
              <li class="flex items-start gap-2.5">
                <svg class="w-4 h-4 mt-0.5 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"/></svg>
                <span>Shop no.21, Plot 129-A, Ambica Estate, Vithal Udyognagar, GIDC, Anand, Gujarat 388120</span>
              </li>
              <li class="flex items-center gap-2.5">
                <svg class="w-4 h-4 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/></svg>
                <span>+91 9825783701 / +91 9898855350</span>
              </li>
              <li class="flex items-center gap-2.5">
                <svg class="w-4 h-4 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"/></svg>
                <span>indtools1992@gmail.com</span>
              </li>
            </ul>
          </div>
        </div>
        <div class="mt-10 pt-6 text-center text-xs transition-colors" :class="darkMode ? 'border-t border-gray-800 text-gray-600' : 'border-t border-white/10 text-white/40'">
          <p>&copy; {{ new Date().getFullYear() }} INDTOOLS. All Rights Reserved.</p>
        </div>
      </div>
    </footer>

    <!-- Mobile Bottom Nav -->
    <nav class="desktop-hide fixed bottom-0 left-0 right-0 z-50 safe-area-bottom transition-colors" :class="darkMode ? 'bg-gray-900/95 backdrop-blur-xl border-t border-gray-800' : 'bg-white/95 backdrop-blur-xl border-t border-gray-100'">
      <div class="flex items-center justify-around h-[4.25rem] px-2">
        <router-link to="/indtools/home" class="mobile-tab" active-class="active">
          <div class="mobile-tab-icon">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.8" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"/></svg>
          </div>
          <span class="mobile-tab-label">Home</span>
        </router-link>
        <router-link to="/indtools/products" class="mobile-tab" active-class="active">
          <div class="mobile-tab-icon">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.8" d="M20 7l-8-4-8 4m16 0l-8 4m8-4v10l-8 4m0-10L4 7m8 4v10M4 7v10l8 4"/></svg>
          </div>
          <span class="mobile-tab-label">Products</span>
        </router-link>
        <router-link to="/indtools/cart" class="mobile-tab relative" active-class="active">
          <div class="mobile-tab-icon">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.8" d="M3 3h2l.4 2M7 13h10l4-8H5.4M7 13L5.4 5M7 13l-2.293 2.293c-.63.63-.184 1.707.707 1.707H17m0 0a2 2 0 100 4 2 2 0 000-4zm-8 2a2 2 0 100 4 2 2 0 000-4z"/></svg>
            <span v-if="cartCount > 0" class="absolute -top-1 -right-1 min-w-[16px] h-[16px] text-[9px] font-bold text-white bg-[#e53935] rounded-full flex items-center justify-center px-0.5">{{ cartCount > 99 ? '99+' : cartCount }}</span>
          </div>
          <span class="mobile-tab-label">Cart</span>
        </router-link>
        <router-link to="/indtools/enquiry" class="mobile-tab" active-class="active">
          <div class="mobile-tab-icon">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.8" d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z"/></svg>
          </div>
          <span class="mobile-tab-label">Enquiry</span>
        </router-link>
        <router-link :to="isLoggedIn ? '/indtools/profile' : '/indtools/login'" class="mobile-tab" active-class="active">
          <div class="mobile-tab-icon">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.8" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"/></svg>
          </div>
          <span class="mobile-tab-label">Account</span>
        </router-link>
      </div>
    </nav>

    <!-- WhatsApp FAB -->
    <a :href="whatsappLink" target="_blank" rel="noopener" class="fab-whatsapp desktop-hide">
      <svg class="w-7 h-7" viewBox="0 0 24 24" fill="white"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>
    </a>

    <!-- Scroll to Top -->
    <button v-if="showScrollTop" @click="scrollToTop" class="scroll-to-top">
      <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 15l7-7 7 7"/></svg>
    </button>

    <!-- PWA Install Banner -->
    <transition name="slide-up">
      <div v-if="showInstall" class="fixed bottom-24 md:bottom-6 left-4 right-4 md:left-auto md:right-6 md:w-80 z-[80] rounded-2xl shadow-2xl border overflow-hidden" :class="darkMode ? 'bg-gray-800 border-gray-700' : 'bg-white border-gray-200'">
        <div class="p-4 flex items-start gap-3">
          <div class="w-10 h-10 rounded-xl flex-shrink-0 flex items-center justify-center" style="background: #e8f5e9">
            <img :src="'/assets/indtools_pwa/frontend/manifest/icon-192.png'" alt="INDTOOLS" class="w-6 h-6 rounded" />
          </div>
          <div class="flex-1 min-w-0">
            <p class="text-sm font-bold" :class="darkMode ? 'text-white' : 'text-gray-900'">Install INDTOOLS</p>
            <p class="text-xs mt-0.5" :class="darkMode ? 'text-gray-400' : 'text-gray-500'">Add to Home Screen for quick access</p>
            <div class="flex gap-2 mt-3">
              <button @click="handleInstall" class="px-4 py-1.5 rounded-lg text-xs font-bold text-white bg-[#2a7f3e] hover:bg-[#1a4d2a] transition-colors">Install</button>
              <button @click="dismissInstall" class="px-3 py-1.5 rounded-lg text-xs font-semibold transition-colors" :class="darkMode ? 'text-gray-400 hover:bg-gray-700' : 'text-gray-500 hover:bg-gray-100'">Later</button>
            </div>
          </div>
          <button @click="dismissInstall" class="p-1 flex-shrink-0" :class="darkMode ? 'text-gray-500 hover:text-white' : 'text-gray-400 hover:text-gray-600'">
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg>
          </button>
        </div>
      </div>
    </transition>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted, watch, provide } from 'vue'
import { useRoute } from 'vue-router'
import { categories, WHATSAPP_NUMBER } from '@/data/categories'
import { sessionUser, useSession } from '@/data/session'
import { useCart } from '@/data/cart'

const route = useRoute()
const { isLoggedIn, fetchUserInfo } = useSession()
const { cartCount } = useCart()

const productsOpen = ref(false)
const showScrollTop = ref(false)

const darkMode = ref(localStorage.getItem('indtools_dark') === 'true')
provide('darkMode', darkMode)

function toggleDark() {
  darkMode.value = !darkMode.value
  localStorage.setItem('indtools_dark', darkMode.value)
}

const whatsappLink = computed(() => {
  const msg = encodeURIComponent("Hi, I'm interested in your industrial products. Please provide more details.")
  return `https://wa.me/${WHATSAPP_NUMBER}?text=${msg}`
})

const showInstall = ref(false)
let deferredPrompt = null

function handleInstall() {
  if (deferredPrompt) {
    deferredPrompt.prompt()
    deferredPrompt.userChoice.then(() => { showInstall.value = false; deferredPrompt = null })
  }
}
function dismissInstall() { showInstall.value = false }

function handleScroll() { showScrollTop.value = window.scrollY > 400 }
function scrollToTop() { window.scrollTo({ top: 0, behavior: 'smooth' }) }

onMounted(() => {
  window.addEventListener('scroll', handleScroll)
  if (sessionUser()) fetchUserInfo()
  window.addEventListener('beforeinstallprompt', (e) => {
    e.preventDefault()
    deferredPrompt = e
    showInstall.value = true
  })
})
onUnmounted(() => {
  window.removeEventListener('scroll', handleScroll)
})

watch(() => route.path, () => { productsOpen.value = false })
</script>

<style>
/* All styles moved to main.css for global scope */
</style>
