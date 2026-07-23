<template>
  <div :style="darkMode ? 'background:#111827;color:#e5e7eb' : 'background:#f5f5f5'" class="min-h-screen">
    <div class="max-w-lg mx-auto px-4 py-6">
      <div class="flex items-center gap-3 mb-6">
        <button @click="$router.back()" class="p-2 rounded-lg transition-colors" :class="darkMode ? 'hover:bg-gray-800 text-gray-400' : 'hover:bg-gray-100 text-gray-600'">
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"/></svg>
        </button>
        <h1 class="text-xl font-bold" :class="darkMode ? 'text-white' : 'text-gray-900'">Change Password</h1>
      </div>

      <div class="rounded-xl shadow-sm p-6 transition-colors" :class="darkMode ? 'bg-gray-800' : 'bg-white'">
        <div class="text-center mb-6">
          <div class="inline-flex items-center justify-center w-14 h-14 rounded-full bg-purple-100 mb-3">
            <svg class="w-7 h-7 text-purple-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z" />
            </svg>
          </div>
          <h2 class="text-lg font-bold" :class="darkMode ? 'text-white' : 'text-gray-900'">Update Your Password</h2>
          <p class="text-xs mt-1" :class="darkMode ? 'text-gray-400' : 'text-gray-500'">Make sure your new password is strong</p>
        </div>

        <div v-if="error" class="mb-4 p-3 bg-red-50 border border-red-200 rounded-lg text-red-700 text-sm">{{ error }}</div>
        <div v-if="success" class="mb-4 p-3 bg-green-50 border border-green-200 rounded-lg text-green-700 text-sm">{{ success }}</div>

        <div class="space-y-4">
          <div>
            <label class="block text-sm font-medium mb-1" :class="darkMode ? 'text-gray-300' : 'text-gray-700'">Old Password</label>
            <input v-model="oldPassword" type="password" placeholder="Enter current password" :disabled="loading"
              class="w-full px-4 py-2.5 rounded-xl outline-none text-sm transition-all border"
              :class="darkMode ? 'bg-gray-700 border-gray-600 text-white placeholder-gray-400 focus:border-[#4caf50]' : 'bg-gray-50 border-gray-200 text-gray-900 placeholder-gray-400 focus:border-[#2a7f3e] focus:shadow-[0_0_0_2px_rgba(42,127,62,0.15)]'"
            />
          </div>
          <div>
            <label class="block text-sm font-medium mb-1" :class="darkMode ? 'text-gray-300' : 'text-gray-700'">New Password</label>
            <input v-model="newPassword" type="password" placeholder="Enter new password" :disabled="loading"
              class="w-full px-4 py-2.5 rounded-xl outline-none text-sm transition-all border"
              :class="darkMode ? 'bg-gray-700 border-gray-600 text-white placeholder-gray-400 focus:border-[#4caf50]' : 'bg-gray-50 border-gray-200 text-gray-900 placeholder-gray-400 focus:border-[#2a7f3e] focus:shadow-[0_0_0_2px_rgba(42,127,62,0.15)]'"
            />
          </div>
          <div>
            <label class="block text-sm font-medium mb-1" :class="darkMode ? 'text-gray-300' : 'text-gray-700'">Confirm New Password</label>
            <input v-model="confirmPassword" type="password" placeholder="Confirm new password" :disabled="loading"
              class="w-full px-4 py-2.5 rounded-xl outline-none text-sm transition-all border"
              :class="darkMode ? 'bg-gray-700 border-gray-600 text-white placeholder-gray-400 focus:border-[#4caf50]' : 'bg-gray-50 border-gray-200 text-gray-900 placeholder-gray-400 focus:border-[#2a7f3e] focus:shadow-[0_0_0_2px_rgba(42,127,62,0.15)]'"
            />
          </div>
        </div>

        <button @click="handleChange" :disabled="loading || !oldPassword || !newPassword || !confirmPassword"
          class="mt-6 w-full py-3 rounded-xl font-semibold text-white text-sm transition-colors disabled:opacity-50 bg-[#2a7f3e] hover:bg-[#1a4d2a]"
        >
          <span v-if="loading" class="inline-flex items-center gap-2">
            <svg class="animate-spin h-4 w-4" fill="none" viewBox="0 0 24 24"><circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"/><path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4z"/></svg>
            Updating...
          </span>
          <span v-else>Update Password</span>
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, inject } from 'vue'
import { useRouter } from 'vue-router'
import { call } from 'frappe-ui'

const router = useRouter()
const darkMode = inject('darkMode', ref(false))

const oldPassword = ref('')
const newPassword = ref('')
const confirmPassword = ref('')
const error = ref('')
const success = ref('')
const loading = ref(false)

async function handleChange() {
  error.value = ''
  success.value = ''
  if (newPassword.value !== confirmPassword.value) { error.value = 'New passwords do not match.'; return }
  if (newPassword.value.length < 6) { error.value = 'New password must be at least 6 characters.'; return }

  loading.value = true
  try {
    await call('frappe.core.doctype.user.user.update_password', { old_password: oldPassword.value, new_password: newPassword.value })
    success.value = 'Password updated successfully! Redirecting...'
    oldPassword.value = ''; newPassword.value = ''; confirmPassword.value = ''
    setTimeout(() => router.push('/indtools/profile'), 2000)
  } catch (e) {
    error.value = e.message || 'Failed to update password.'
  } finally {
    loading.value = false
  }
}
</script>
