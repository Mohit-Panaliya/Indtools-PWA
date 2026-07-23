<template>
  <div :class="darkMode ? 'bg-[#0f1710]' : 'bg-[#f5f5f5]'" class="min-h-screen">
    <!-- Hero Banner -->
    <div :class="darkMode ? 'bg-[#1a2e1f]' : 'bg-gradient-to-r from-[#1a4d2a] to-[#2a7f3e]'" class="py-10 md:py-14">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <h1 :class="darkMode ? 'text-green-300' : 'text-white'" class="text-3xl md:text-4xl font-bold mb-2">Quick Enquiry</h1>
        <nav class="flex items-center space-x-2 text-sm">
          <router-link :class="darkMode ? 'text-green-400' : 'text-green-200'" to="/" class="hover:underline">Home</router-link>
          <span :class="darkMode ? 'text-green-500' : 'text-green-300'">/</span>
          <span :class="darkMode ? 'text-green-200' : 'text-white'" class="opacity-80">Enquiry</span>
        </nav>
      </div>
    </div>

    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 md:py-12">
      <!-- Success State -->
      <div v-if="submitted" class="flex flex-col items-center justify-center py-16 md:py-24 text-center">
        <div :class="darkMode ? 'bg-[#2a7f3e]/20' : 'bg-[#e8f5e9]'" class="w-20 h-20 mb-6 rounded-full flex items-center justify-center">
          <svg class="w-10 h-10 text-[#2a7f3e]" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M5 13l4 4L19 7" />
          </svg>
        </div>
        <h2 :class="darkMode ? 'text-white' : 'text-[#1a4d2a]'" class="text-xl font-bold mb-2">Enquiry Submitted!</h2>
        <p :class="darkMode ? 'text-gray-400' : 'text-gray-500'" class="text-sm mb-6 max-w-sm">
          Thank you for your enquiry. Our team will review it and get back to you within 24 hours.
        </p>
        <button @click="resetForm" class="bg-[#2a7f3e] hover:bg-[#1a4d2a] text-white px-6 py-3 rounded-lg font-semibold transition-colors text-sm">
          Submit Another Enquiry
        </button>
      </div>

      <!-- Form + WhatsApp -->
      <div v-else class="flex flex-col lg:flex-row gap-6 md:gap-8">
        <!-- Form Card -->
        <div class="flex-1">
          <div :class="darkMode ? 'bg-[#1a2e1f] border-[#2a7f3e]/30' : 'bg-white border-gray-100'" class="rounded-2xl border p-5 md:p-8">
            <div v-if="errorMsg" class="mb-4 p-3 bg-red-50 border border-red-200 rounded-lg text-red-700 text-sm">{{ errorMsg }}</div>
            <form @submit.prevent="handleSubmit" class="space-y-4 md:space-y-5">
              <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                <div>
                  <label :class="darkMode ? 'text-gray-400' : 'text-gray-600'" class="block text-xs font-medium mb-1.5">Name *</label>
                  <input v-model="form.name" type="text" required placeholder="Your full name"
                    :class="darkMode ? 'bg-[#0f1710] border-[#2a7f3e]/30 text-white placeholder-gray-500' : 'bg-[#f9fafb] border-gray-200 text-[#1a4d2a] placeholder-gray-400'"
                    class="w-full px-3 py-2.5 text-sm border rounded-lg focus:outline-none focus:ring-2 focus:ring-[#4caf50] transition-colors" />
                </div>
                <div>
                  <label :class="darkMode ? 'text-gray-400' : 'text-gray-600'" class="block text-xs font-medium mb-1.5">Company</label>
                  <input v-model="form.company" type="text" placeholder="Company name"
                    :class="darkMode ? 'bg-[#0f1710] border-[#2a7f3e]/30 text-white placeholder-gray-500' : 'bg-[#f9fafb] border-gray-200 text-[#1a4d2a] placeholder-gray-400'"
                    class="w-full px-3 py-2.5 text-sm border rounded-lg focus:outline-none focus:ring-2 focus:ring-[#4caf50] transition-colors" />
                </div>
              </div>

              <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                <div>
                  <label :class="darkMode ? 'text-gray-400' : 'text-gray-600'" class="block text-xs font-medium mb-1.5">Email *</label>
                  <input v-model="form.email" type="email" required placeholder="you@example.com"
                    :class="darkMode ? 'bg-[#0f1710] border-[#2a7f3e]/30 text-white placeholder-gray-500' : 'bg-[#f9fafb] border-gray-200 text-[#1a4d2a] placeholder-gray-400'"
                    class="w-full px-3 py-2.5 text-sm border rounded-lg focus:outline-none focus:ring-2 focus:ring-[#4caf50] transition-colors" />
                </div>
                <div>
                  <label :class="darkMode ? 'text-gray-400' : 'text-gray-600'" class="block text-xs font-medium mb-1.5">Phone *</label>
                  <input v-model="form.phone" type="tel" required placeholder="+91 XXXXX XXXXX"
                    :class="darkMode ? 'bg-[#0f1710] border-[#2a7f3e]/30 text-white placeholder-gray-500' : 'bg-[#f9fafb] border-gray-200 text-[#1a4d2a] placeholder-gray-400'"
                    class="w-full px-3 py-2.5 text-sm border rounded-lg focus:outline-none focus:ring-2 focus:ring-[#4caf50] transition-colors" />
                </div>
              </div>

              <div>
                <label :class="darkMode ? 'text-gray-400' : 'text-gray-600'" class="block text-xs font-medium mb-1.5">Product Interested In</label>
                <select v-model="form.product"
                  :class="darkMode ? 'bg-[#0f1710] border-[#2a7f3e]/30 text-white' : 'bg-[#f9fafb] border-gray-200 text-[#1a4d2a]'"
                  class="w-full px-3 py-2.5 text-sm border rounded-lg focus:outline-none focus:ring-2 focus:ring-[#4caf50] transition-colors appearance-none"
                  style="background-image: url('data:image/svg+xml;charset=UTF-8,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20width%3D%2216%22%20height%3D%2216%22%20viewBox%3D%220%200%2024%2024%22%20fill%3D%22none%22%20stroke%3D%22%236b7280%22%20stroke-width%3D%222%22%20stroke-linecap%3D%22round%22%20stroke-linejoin%3D%22round%22%3E%3Cpolyline%20points%3D%226%209%2012%2015%2018%209%22%3E%3C%2Fpolyline%3E%3C%2Fsvg%3E'); background-repeat: no-repeat; background-position: right 0.75rem center; padding-right: 2.5rem;">
                  <option value="">Select a product category</option>
                  <option v-for="cat in categories" :key="cat.id" :value="cat.name">{{ cat.name }}</option>
                </select>
              </div>

              <div>
                <label :class="darkMode ? 'text-gray-400' : 'text-gray-600'" class="block text-xs font-medium mb-1.5">Quantity</label>
                <input v-model="form.quantity" type="text" placeholder="e.g., 1000 pcs, 5 boxes"
                  :class="darkMode ? 'bg-[#0f1710] border-[#2a7f3e]/30 text-white placeholder-gray-500' : 'bg-[#f9fafb] border-gray-200 text-[#1a4d2a] placeholder-gray-400'"
                  class="w-full px-3 py-2.5 text-sm border rounded-lg focus:outline-none focus:ring-2 focus:ring-[#4caf50] transition-colors" />
              </div>

              <div>
                <label :class="darkMode ? 'text-gray-400' : 'text-gray-600'" class="block text-xs font-medium mb-1.5">Message *</label>
                <textarea v-model="form.message" required rows="4" placeholder="Describe your requirements..."
                  :class="darkMode ? 'bg-[#0f1710] border-[#2a7f3e]/30 text-white placeholder-gray-500' : 'bg-[#f9fafb] border-gray-200 text-[#1a4d2a] placeholder-gray-400'"
                  class="w-full px-3 py-2.5 text-sm border rounded-lg resize-none focus:outline-none focus:ring-2 focus:ring-[#4caf50] transition-colors"></textarea>
              </div>

              <button type="submit" :disabled="submitting"
                class="w-full py-3 text-sm font-semibold text-white rounded-lg transition-colors disabled:opacity-50 disabled:cursor-not-allowed bg-[#2a7f3e] hover:bg-[#1a4d2a]">
                <span v-if="submitting" class="flex items-center justify-center gap-2">
                  <svg class="animate-spin w-4 h-4" fill="none" viewBox="0 0 24 24">
                    <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4" />
                    <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4z" />
                  </svg>
                  Submitting...
                </span>
                <span v-else>Submit Enquiry</span>
              </button>
            </form>
          </div>
        </div>

        <!-- WhatsApp + Contact Sidebar -->
        <div class="w-full lg:w-[320px] flex-shrink-0 space-y-4">
          <!-- WhatsApp Card -->
          <div :class="darkMode ? 'bg-[#1a2e1f] border-[#2a7f3e]/30' : 'bg-white border-gray-100'" class="rounded-2xl border p-5 md:p-6 text-center">
            <div :class="darkMode ? 'bg-[#25d366]/20' : 'bg-[#dcf8c6]'" class="w-14 h-14 mx-auto mb-4 rounded-full flex items-center justify-center">
              <svg class="w-7 h-7" viewBox="0 0 24 24" fill="#25d366">
                <path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z" />
              </svg>
            </div>
            <h3 :class="darkMode ? 'text-white' : 'text-[#1a4d2a]'" class="font-bold mb-1">WhatsApp Us</h3>
            <p :class="darkMode ? 'text-gray-400' : 'text-gray-500'" class="text-xs mb-4">Get instant responses to your queries</p>
            <a :href="whatsappLink" target="_blank" rel="noopener noreferrer"
              class="inline-flex items-center justify-center gap-2 w-full py-3 text-sm font-semibold text-white rounded-lg bg-[#25d366] hover:bg-[#1da851] transition-colors">
              <svg class="w-5 h-5" viewBox="0 0 24 24" fill="currentColor">
                <path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z" />
              </svg>
              Chat on WhatsApp
            </a>
            <p :class="darkMode ? 'text-gray-500' : 'text-gray-400'" class="text-[11px] mt-3">{{ WHATSAPP_NUMBER }}</p>
          </div>

          <!-- Contact Info Card -->
          <div :class="darkMode ? 'bg-[#1a2e1f] border-[#2a7f3e]/30' : 'bg-white border-gray-100'" class="rounded-2xl border p-5 md:p-6">
            <h3 :class="darkMode ? 'text-white' : 'text-[#1a4d2a]'" class="font-bold text-sm mb-3">Other Ways to Reach Us</h3>
            <div class="space-y-3">
              <div class="flex items-center gap-3">
                <div class="w-9 h-9 rounded-lg bg-[#e8f5e9] flex items-center justify-center flex-shrink-0">
                  <svg class="w-4 h-4 text-[#2a7f3e]" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
                  </svg>
                </div>
                <span :class="darkMode ? 'text-gray-400' : 'text-gray-600'" class="text-xs">indtools1992@gmail.com</span>
              </div>
              <div class="flex items-center gap-3">
                <div class="w-9 h-9 rounded-lg bg-[#e8f5e9] flex items-center justify-center flex-shrink-0">
                  <svg class="w-4 h-4 text-[#2a7f3e]" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z" />
                  </svg>
                </div>
                <span :class="darkMode ? 'text-gray-400' : 'text-gray-600'" class="text-xs">+91 9825783701 / +91 9898855350</span>
              </div>
              <div class="flex items-start gap-3">
                <div class="w-9 h-9 rounded-lg bg-[#e8f5e9] flex items-center justify-center flex-shrink-0">
                  <svg class="w-4 h-4 text-[#2a7f3e]" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z" />
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z" />
                  </svg>
                </div>
                <span :class="darkMode ? 'text-gray-400' : 'text-gray-600'" class="text-xs">Shop no.21, Plot 129-A, Ambica Estate, GIDC, Anand, Gujarat 388120</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { reactive, ref, inject } from 'vue'
import { call } from 'frappe-ui'
import { categories, WHATSAPP_NUMBER } from '@/data/categories'

const darkMode = inject('darkMode', ref(false))
const submitted = ref(false)
const submitting = ref(false)
const errorMsg = ref('')

const form = reactive({
  name: '',
  company: '',
  email: '',
  phone: '',
  product: '',
  quantity: '',
  message: '',
})

const whatsappLink = `https://wa.me/${WHATSAPP_NUMBER.replace('+', '')}?text=${encodeURIComponent('Hi, I am interested in your products. Can you share more details?')}`

async function handleSubmit() {
  submitting.value = true
  errorMsg.value = ''
  try {
    await call('indtools_pwa.api.create_enquiry', {
      name: form.name,
      email: form.email,
      phone: form.phone,
      company: form.company || undefined,
      subject: form.product ? `${form.product} - Qty: ${form.quantity || 'N/A'}` : 'Product Enquiry',
      message: form.message,
      product: form.product || undefined,
    })
    submitted.value = true
  } catch (e) {
    errorMsg.value = e.message || 'Failed to submit enquiry. Please try again.'
  } finally {
    submitting.value = false
  }
}

function resetForm() {
  Object.assign(form, { name: '', company: '', email: '', phone: '', product: '', quantity: '', message: '' })
  submitted.value = false
}
</script>
