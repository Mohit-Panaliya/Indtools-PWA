<template>
  <div class="flex items-center justify-center px-4 py-8 min-h-[calc(100vh-10rem)]" :style="darkMode ? 'background:#111827' : 'background:#f5f5f5'">
    <div class="w-full max-w-sm">
      <div class="text-center mb-8">
        <div class="inline-flex items-center justify-center w-16 h-16 rounded-2xl bg-[#2a7f3e] mb-4">
          <svg class="w-8 h-8 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 3h2l.4 2M7 13h10l4-8H5.4M7 13L5.4 5M7 13l-2.293 2.293c-.63.63-.184 1.707.707 1.707H17m0 0a2 2 0 100 4 2 2 0 000-4zm-8 2a2 2 0 100 4 2 2 0 000-4z" />
          </svg>
        </div>
        <h1 class="text-2xl font-bold" :class="darkMode ? 'text-white' : 'text-gray-900'">Welcome Back</h1>
        <p class="text-sm mt-1" :class="darkMode ? 'text-gray-400' : 'text-gray-500'">Sign in to your account</p>
      </div>

      <div class="rounded-xl shadow-sm p-6 transition-colors" :class="darkMode ? 'bg-gray-800' : 'bg-white'">
        <div v-if="error" class="mb-4 p-3 bg-red-50 border border-red-200 rounded-lg text-red-700 text-sm">
          {{ error }}
        </div>

        <div class="space-y-4">
          <div>
            <label class="block text-sm font-medium mb-1" :class="darkMode ? 'text-gray-300' : 'text-gray-700'">Email</label>
            <input v-model="email" type="email" placeholder="Enter your email" :disabled="loading"
              class="w-full px-4 py-2.5 rounded-xl outline-none text-sm transition-all border"
              :class="darkMode ? 'bg-gray-700 border-gray-600 text-white placeholder-gray-400 focus:border-[#4caf50]' : 'bg-gray-50 border-gray-200 text-gray-900 placeholder-gray-400 focus:border-[#2a7f3e] focus:shadow-[0_0_0_2px_rgba(42,127,62,0.15)]'"
            />
          </div>

          <div>
            <label class="block text-sm font-medium mb-1" :class="darkMode ? 'text-gray-300' : 'text-gray-700'">Password</label>
            <input v-model="password" type="password" placeholder="Enter your password" :disabled="loading"
              class="w-full px-4 py-2.5 rounded-xl outline-none text-sm transition-all border"
              :class="darkMode ? 'bg-gray-700 border-gray-600 text-white placeholder-gray-400 focus:border-[#4caf50]' : 'bg-gray-50 border-gray-200 text-gray-900 placeholder-gray-400 focus:border-[#2a7f3e] focus:shadow-[0_0_0_2px_rgba(42,127,62,0.15)]'"
            />
          </div>
        </div>

        <button @click="handleLogin" :disabled="loading || !email || !password"
          class="mt-6 w-full py-3 rounded-xl font-semibold text-white text-sm transition-colors disabled:opacity-50 disabled:cursor-not-allowed bg-[#2a7f3e] hover:bg-[#1a4d2a]"
        >
          <span v-if="loading" class="inline-flex items-center gap-2">
            <svg class="animate-spin h-4 w-4" fill="none" viewBox="0 0 24 24"><circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"/><path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4z"/></svg>
            Logging in...
          </span>
          <span v-else>Login</span>
        </button>

        <div class="mt-4 text-center">
          <router-link to="/indtools/forgot-password" class="text-sm hover:underline" :class="darkMode ? 'text-[#4caf50]' : 'text-[#2a7f3e]'">
            Forgot Password?
          </router-link>
        </div>
      </div>

      <p class="mt-6 text-center text-sm" :class="darkMode ? 'text-gray-400' : 'text-gray-500'">
        Don't have an account?
        <router-link to="/indtools/register" class="font-semibold hover:underline" :class="darkMode ? 'text-[#4caf50]' : 'text-[#2a7f3e]'">
          Register
        </router-link>
      </p>
    </div>
  </div>
</template>

<script setup>
import { ref, inject } from 'vue'
import { useRouter } from 'vue-router'
import { useSession } from '@/data/session'

const router = useRouter()
const { login } = useSession()
const darkMode = inject('darkMode', ref(false))

const email = ref('')
const password = ref('')
const error = ref('')
const loading = ref(false)

async function handleLogin() {
  error.value = ''
  loading.value = true
  try {
    await login(email.value, password.value)
    router.push('/indtools')
  } catch (e) {
    error.value = e.message || 'Login failed. Please check your credentials.'
  } finally {
    loading.value = false
  }
}
</script>
