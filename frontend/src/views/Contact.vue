<template>
  <div :class="darkMode ? 'bg-[#0f1710]' : 'bg-[#f5f5f5]'" class="min-h-screen">
    <!-- Hero Banner -->
    <div :class="darkMode ? 'bg-[#1a2e1f]' : 'bg-gradient-to-r from-[#1a4d2a] to-[#2a7f3e]'" class="py-10 md:py-14">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <h1 :class="darkMode ? 'text-green-300' : 'text-white'" class="text-3xl md:text-4xl font-bold mb-2">Contact Us</h1>
        <nav class="flex items-center space-x-2 text-sm">
          <router-link :class="darkMode ? 'text-green-400' : 'text-green-200'" to="/" class="hover:underline">Home</router-link>
          <span :class="darkMode ? 'text-green-500' : 'text-green-300'">/</span>
          <span :class="darkMode ? 'text-green-200' : 'text-white'" class="opacity-80">Contact Us</span>
        </nav>
      </div>
    </div>

    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 md:py-12">
      <div class="grid md:grid-cols-2 gap-8 md:gap-12">
        <!-- Contact Info -->
        <div>
          <h2 :class="darkMode ? 'text-white' : 'text-[#1a4d2a]'" class="text-2xl font-bold mb-6">Get in Touch</h2>
          <p :class="darkMode ? 'text-gray-400' : 'text-gray-600'" class="mb-8 leading-relaxed">
            Have questions about our products or need a custom solution? We'd love to hear from you. Reach out through any of the channels below.
          </p>

          <div class="space-y-5">
            <div v-for="info in contactInfo" :key="info.label" :class="darkMode ? 'bg-[#1a2e1f] border-[#2a7f3e]/20' : 'bg-white border-gray-100'" class="flex items-start gap-4 p-4 rounded-xl border">
              <div class="w-12 h-12 rounded-xl bg-[#e8f5e9] flex items-center justify-center flex-shrink-0">
                <span class="text-xl">{{ info.icon }}</span>
              </div>
              <div>
                <h4 :class="darkMode ? 'text-white' : 'text-[#1a4d2a]'" class="font-bold text-sm">{{ info.label }}</h4>
                <p :class="darkMode ? 'text-gray-400' : 'text-gray-600'" class="text-sm mt-1" v-html="info.value"></p>
              </div>
            </div>
          </div>

          <!-- Social Links -->
          <div class="mt-8">
            <h3 :class="darkMode ? 'text-white' : 'text-[#1a4d2a]'" class="font-bold mb-4">Follow Us</h3>
            <div class="flex gap-3">
              <a v-for="social in socials" :key="social.name" :href="social.url" target="_blank" :class="darkMode ? 'bg-[#1a2e1f] hover:bg-[#223a28] border-[#2a7f3e]/20' : 'bg-white hover:bg-gray-50 border-gray-100'" class="w-11 h-11 rounded-xl border flex items-center justify-center transition-colors" :title="social.name">
                <img :src="social.icon" :alt="social.name" class="w-5 h-5" @error="(e) => e.target.style.display='none'" />
              </a>
            </div>
          </div>
        </div>

        <!-- Map & Enquiry Form -->
        <div>
          <!-- Map -->
          <div :class="darkMode ? 'bg-[#1a2e1f] border-[#2a7f3e]/20' : 'bg-white border-gray-100'" class="rounded-2xl border overflow-hidden mb-6">
            <div class="aspect-video bg-gray-200 relative">
              <img :src="'/assets/indtools_pwa/frontend/MAP.png'" alt="INDTOOLS Location Map" class="w-full h-full object-cover" @error="(e) => e.target.style.display='none'" />
              <div class="absolute inset-0 flex items-center justify-center" style="display:none" id="map-fallback">
                <div class="text-center">
                  <span class="text-4xl mb-2 block">📍</span>
                  <p :class="darkMode ? 'text-gray-400' : 'text-gray-500'" class="text-sm">GIDC Anand, Gujarat</p>
                </div>
              </div>
            </div>
          </div>

          <!-- Quick Enquiry Form -->
          <div :class="darkMode ? 'bg-[#1a2e1f] border-[#2a7f3e]/20' : 'bg-white border-gray-100'" class="rounded-2xl border p-6">
            <h3 :class="darkMode ? 'text-white' : 'text-[#1a4d2a]'" class="font-bold text-lg mb-4">Quick Enquiry</h3>
            <form @submit.prevent="submitEnquiry" class="space-y-3">
              <input v-model="form.name" type="text" placeholder="Your Name" required :class="darkMode ? 'bg-[#0f1710] border-[#2a7f3e]/30 text-white placeholder-gray-500' : 'bg-[#f9fafb] border-gray-200 text-[#1a4d2a] placeholder-gray-400'" class="w-full px-4 py-2.5 rounded-lg border text-sm focus:ring-2 focus:ring-[#4caf50] outline-none" />
              <input v-model="form.phone" type="tel" placeholder="Phone Number" required :class="darkMode ? 'bg-[#0f1710] border-[#2a7f3e]/30 text-white placeholder-gray-500' : 'bg-[#f9fafb] border-gray-200 text-[#1a4d2a] placeholder-gray-400'" class="w-full px-4 py-2.5 rounded-lg border text-sm focus:ring-2 focus:ring-[#4caf50] outline-none" />
              <textarea v-model="form.message" rows="3" placeholder="Your Message" required :class="darkMode ? 'bg-[#0f1710] border-[#2a7f3e]/30 text-white placeholder-gray-500' : 'bg-[#f9fafb] border-gray-200 text-[#1a4d2a] placeholder-gray-400'" class="w-full px-4 py-2.5 rounded-lg border text-sm focus:ring-2 focus:ring-[#4caf50] outline-none resize-none"></textarea>
              <button type="submit" :disabled="submitting" class="w-full bg-[#2a7f3e] hover:bg-[#1a4d2a] disabled:opacity-50 text-white py-2.5 rounded-lg font-semibold transition-colors text-sm">
                {{ submitting ? 'Sending...' : 'Send Message' }}
              </button>
            </form>
            <p v-if="submitted" class="text-[#4caf50] text-sm mt-3 text-center font-medium">Message sent! We'll get back to you soon.</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, inject } from 'vue'

const darkMode = inject('darkMode', ref(false))
const submitting = ref(false)
const submitted = ref(false)
const form = ref({ name: '', phone: '', message: '' })

const contactInfo = [
  { icon: '📍', label: 'Address', value: 'Shop no.21, Plot 129-A,<br/>Ambica Estate, Vithal Udyognagar,<br/>GIDC, Anand, Gujarat 388120' },
  { icon: '📞', label: 'Phone', value: '<a href="tel:+919825783701" class="hover:text-[#4caf50]">+91 9825 783 701</a><br/><a href="tel:+919898855350" class="hover:text-[#4caf50]">+91 9898 855 350</a>' },
  { icon: '✉️', label: 'Email', value: '<a href="mailto:indtools1992@gmail.com" class="hover:text-[#4caf50]">indtools1992@gmail.com</a>' },
  { icon: '🕐', label: 'Business Hours', value: 'Mon - Sat: 9:00 AM - 6:00 PM<br/>Sunday: Closed' }
]

const socials = [
  { name: 'Facebook', url: 'https://facebook.com', icon: '/assets/indtools_pwa/frontend/social/facebook.png' },
  { name: 'Instagram', url: 'https://instagram.com', icon: '/assets/indtools_pwa/frontend/social/instagram.png' },
  { name: 'LinkedIn', url: 'https://linkedin.com', icon: '/assets/indtools_pwa/frontend/social/linkedin.png' },
  { name: 'Twitter', url: 'https://twitter.com', icon: '/assets/indtools_pwa/frontend/social/twitter.png' }
]

const submitEnquiry = async () => {
  submitting.value = true
  try {
    await new Promise(r => setTimeout(r, 1000))
    submitted.value = true
    form.value = { name: '', phone: '', message: '' }
    setTimeout(() => { submitted.value = false }, 5000)
  } finally {
    submitting.value = false
  }
}
</script>
