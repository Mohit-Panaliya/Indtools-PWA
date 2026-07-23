<template>
  <div class="flex items-center justify-center px-4 py-8 min-h-[calc(100vh-10rem)]" :style="darkMode ? 'background:#111827' : 'background:#f5f5f5'">
    <div class="w-full max-w-sm">
      <div class="text-center mb-6">
        <div class="inline-flex items-center justify-center w-16 h-16 rounded-2xl bg-[#2a7f3e] mb-4">
          <svg class="w-8 h-8 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 7a2 2 0 012 2m4 0a6 6 0 01-7.743 5.743L11 17H9v2H7v2H4a1 1 0 01-1-1v-2.586a1 1 0 01.293-.707l5.964-5.964A6 6 0 1121 9z" />
          </svg>
        </div>
        <h1 class="text-2xl font-bold" :class="darkMode ? 'text-white' : 'text-gray-900'">Reset Password</h1>
        <p class="text-sm mt-1" :class="darkMode ? 'text-gray-400' : 'text-gray-500'">Enter your email to receive a reset link</p>
      </div>

      <div class="rounded-xl shadow-sm p-6 transition-colors" :class="darkMode ? 'bg-gray-800' : 'bg-white'">
        <div v-if="error" class="mb-4 p-3 bg-red-50 border border-red-200 rounded-lg text-red-700 text-sm">{{ error }}</div>
        <div v-if="sent" class="mb-4 p-3 bg-green-50 border border-green-200 rounded-lg text-green-700 text-sm">If an account exists with this email, a reset link has been sent.</div>

        <div v-if="!sent">
          <div>
            <label class="block text-sm font-medium mb-1" :class="darkMode ? 'text-gray-300' : 'text-gray-700'">Email</label>
            <input v-model="email" type="email" placeholder="Enter your email address" :disabled="loading"
              class="w-full px-4 py-2.5 rounded-xl outline-none text-sm transition-all border"
              :class="darkMode ? 'bg-gray-700 border-gray-600 text-white placeholder-gray-400 focus:border-[#4caf50]' : 'bg-gray-50 border-gray-200 text-gray-900 placeholder-gray-400 focus:border-[#2a7f3e] focus:shadow-[0_0_0_2px_rgba(42,127,62,0.15)]'"
            />
          </div>
          <button @click="handleSend" :disabled="loading || !email"
            class="mt-6 w-full py-3 rounded-xl font-semibold text-white text-sm transition-colors disabled:opacity-50 bg-[#2a7f3e] hover:bg-[#1a4d2a]"
          >
            <span v-if="loading" class="inline-flex items-center gap-2">
              <svg class="animate-spin h-4 w-4" fill="none" viewBox="0 0 24 24"><circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"/><path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4z"/></svg>
              Sending...
            </span>
            <span v-else>Send Reset Link</span>
          </button>
        </div>
      </div>

      <p class="mt-6 text-center text-sm" :class="darkMode ? 'text-gray-400' : 'text-gray-500'">
        <router-link to="/indtools/login" class="font-semibold hover:underline inline-flex items-center gap-1" :class="darkMode ? 'text-[#4caf50]' : 'text-[#2a7f3e]'">
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"/></svg>
          Back to Login
        </router-link>
      </p>
    </div>
  </div>
</template>

<script setup>
import { ref, inject } from 'vue'
import { call } from 'frappe-ui'

const darkMode = inject('darkMode', ref(false))
const email = ref('')
const error = ref('')
const sent = ref(false)
const loading = ref(false)

async function handleSend() {
  error.value = ''
  loading.value = true
  try {
    await call('frappe.core.doctype.user.user.reset_password', { user: email.value })
    sent.value = true
  } catch (e) {
    sent.value = true
  } finally {
    loading.value = false
  }
}
</script>
