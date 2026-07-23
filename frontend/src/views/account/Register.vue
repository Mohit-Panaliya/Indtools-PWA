<template>
  <div class="flex items-center justify-center px-4 py-8 min-h-[calc(100vh-10rem)]" :style="darkMode ? 'background:#111827' : 'background:#f5f5f5'">
    <div class="w-full max-w-sm">
      <div class="text-center mb-6">
        <div class="inline-flex items-center justify-center w-16 h-16 rounded-2xl bg-[#2a7f3e] mb-4">
          <svg class="w-8 h-8 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M18 9v3m0 0v3m0-3h3m-3 0h-3m-2-5a4 4 0 11-8 0 4 4 0 018 0zM3 20a6 6 0 0112 0v1H3v-1z" />
          </svg>
        </div>
        <h1 class="text-2xl font-bold" :class="darkMode ? 'text-white' : 'text-gray-900'">Create Account</h1>
        <p class="text-sm mt-1" :class="darkMode ? 'text-gray-400' : 'text-gray-500'">Join us today</p>
      </div>

      <div class="rounded-xl shadow-sm p-6 transition-colors" :class="darkMode ? 'bg-gray-800' : 'bg-white'">
        <div v-if="error" class="mb-4 p-3 bg-red-50 border border-red-200 rounded-lg text-red-700 text-sm">
          {{ error }}
        </div>
        <div v-if="success" class="mb-4 p-3 bg-green-50 border border-green-200 rounded-lg text-green-700 text-sm">
          {{ success }}
        </div>

        <div class="space-y-4">
          <div>
            <label class="block text-sm font-medium mb-1" :class="darkMode ? 'text-gray-300' : 'text-gray-700'">Full Name</label>
            <input v-model="fullName" type="text" placeholder="Enter your full name" :disabled="loading"
              class="w-full px-4 py-2.5 rounded-xl outline-none text-sm transition-all border"
              :class="darkMode ? 'bg-gray-700 border-gray-600 text-white placeholder-gray-400 focus:border-[#4caf50]' : 'bg-gray-50 border-gray-200 text-gray-900 placeholder-gray-400 focus:border-[#2a7f3e] focus:shadow-[0_0_0_2px_rgba(42,127,62,0.15)]'"
            />
          </div>
          <div>
            <label class="block text-sm font-medium mb-1" :class="darkMode ? 'text-gray-300' : 'text-gray-700'">Email</label>
            <input v-model="email" type="email" placeholder="Enter your email" :disabled="loading"
              class="w-full px-4 py-2.5 rounded-xl outline-none text-sm transition-all border"
              :class="darkMode ? 'bg-gray-700 border-gray-600 text-white placeholder-gray-400 focus:border-[#4caf50]' : 'bg-gray-50 border-gray-200 text-gray-900 placeholder-gray-400 focus:border-[#2a7f3e] focus:shadow-[0_0_0_2px_rgba(42,127,62,0.15)]'"
            />
          </div>
          <div>
            <label class="block text-sm font-medium mb-1" :class="darkMode ? 'text-gray-300' : 'text-gray-700'">Password</label>
            <input v-model="password" type="password" placeholder="Create a password" :disabled="loading"
              class="w-full px-4 py-2.5 rounded-xl outline-none text-sm transition-all border"
              :class="darkMode ? 'bg-gray-700 border-gray-600 text-white placeholder-gray-400 focus:border-[#4caf50]' : 'bg-gray-50 border-gray-200 text-gray-900 placeholder-gray-400 focus:border-[#2a7f3e] focus:shadow-[0_0_0_2px_rgba(42,127,62,0.15)]'"
            />
          </div>
          <div>
            <label class="block text-sm font-medium mb-1" :class="darkMode ? 'text-gray-300' : 'text-gray-700'">Confirm Password</label>
            <input v-model="confirmPassword" type="password" placeholder="Confirm your password" :disabled="loading"
              class="w-full px-4 py-2.5 rounded-xl outline-none text-sm transition-all border"
              :class="darkMode ? 'bg-gray-700 border-gray-600 text-white placeholder-gray-400 focus:border-[#4caf50]' : 'bg-gray-50 border-gray-200 text-gray-900 placeholder-gray-400 focus:border-[#2a7f3e] focus:shadow-[0_0_0_2px_rgba(42,127,62,0.15)]'"
            />
          </div>
        </div>

        <button @click="handleRegister" :disabled="loading || !fullName || !email || !password || !confirmPassword"
          class="mt-6 w-full py-3 rounded-xl font-semibold text-white text-sm transition-colors disabled:opacity-50 disabled:cursor-not-allowed bg-[#2a7f3e] hover:bg-[#1a4d2a]"
        >
          <span v-if="loading" class="inline-flex items-center gap-2">
            <svg class="animate-spin h-4 w-4" fill="none" viewBox="0 0 24 24"><circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"/><path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4z"/></svg>
            Creating account...
          </span>
          <span v-else>Register</span>
        </button>
      </div>

      <p class="mt-6 text-center text-sm" :class="darkMode ? 'text-gray-400' : 'text-gray-500'">
        Already have an account?
        <router-link to="/indtools/login" class="font-semibold hover:underline" :class="darkMode ? 'text-[#4caf50]' : 'text-[#2a7f3e]'">
          Login
        </router-link>
      </p>
    </div>
  </div>
</template>

<script setup>
import { ref, inject } from 'vue'
import { useRouter } from 'vue-router'
import { call } from 'frappe-ui'

const router = useRouter()
const darkMode = inject('darkMode', ref(false))

const fullName = ref('')
const email = ref('')
const password = ref('')
const confirmPassword = ref('')
const error = ref('')
const success = ref('')
const loading = ref(false)

async function handleRegister() {
  error.value = ''
  success.value = ''
  if (password.value !== confirmPassword.value) { error.value = 'Passwords do not match.'; return }
  if (password.value.length < 6) { error.value = 'Password must be at least 6 characters.'; return }

  loading.value = true
  try {
    await call('indtools_pwa.api.register', {
      full_name: fullName.value,
      email: email.value,
      password: password.value,
    })
    success.value = 'Account created successfully! Redirecting to login...'
    setTimeout(() => router.push('/indtools/login'), 2000)
  } catch (e) {
    error.value = e.message || 'Registration failed. Please try again.'
  } finally {
    loading.value = false
  }
}
</script>
