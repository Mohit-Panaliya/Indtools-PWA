<template>
  <div :style="darkMode ? 'background:#111827;color:#e5e7eb' : 'background:#f5f5f5'" class="min-h-screen">
    <div class="max-w-lg mx-auto px-4 py-6">
      <!-- User Card -->
      <div class="rounded-xl shadow-sm p-6 mb-4 text-center transition-colors" :class="darkMode ? 'bg-gray-800' : 'bg-white'">
        <div class="inline-flex items-center justify-center w-20 h-20 rounded-full bg-[#2a7f3e] text-white text-3xl font-bold mb-3">
          {{ initials }}
        </div>
        <h2 class="text-lg font-bold" :class="darkMode ? 'text-white' : 'text-gray-900'">{{ fullName || 'User' }}</h2>
        <p class="text-sm mt-1" :class="darkMode ? 'text-gray-400' : 'text-gray-500'">{{ email || '' }}</p>
      </div>

      <!-- Menu Items -->
      <div class="rounded-xl shadow-sm overflow-hidden transition-colors" :class="darkMode ? 'bg-gray-800' : 'bg-white'">
        <router-link
          v-for="(item, idx) in menuItems"
          :key="idx"
          :to="item.to"
          class="flex items-center gap-3 px-4 py-3.5 border-b transition-colors"
          :class="darkMode ? 'border-gray-700 last:border-b-0' : 'border-gray-100 last:border-b-0'"
        >
          <div class="w-9 h-9 rounded-lg flex items-center justify-center" :class="item.iconBg">
            <span v-html="item.icon" class="w-5 h-5"></span>
          </div>
          <span class="flex-1 text-sm font-medium" :class="darkMode ? 'text-gray-200' : 'text-gray-900'">{{ item.label }}</span>
          <svg class="w-5 h-5" :class="darkMode ? 'text-gray-600' : 'text-gray-400'" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
          </svg>
        </router-link>

        <!-- Logout -->
        <button
          @click="handleLogout"
          class="w-full flex items-center gap-3 px-4 py-3.5 transition-colors"
          :class="darkMode ? 'hover:bg-gray-750' : 'hover:bg-gray-50'"
        >
          <div class="w-9 h-9 rounded-lg flex items-center justify-center bg-red-50">
            <svg class="w-5 h-5 text-red-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1" />
            </svg>
          </div>
          <span class="flex-1 text-left text-sm font-medium text-red-500">Logout</span>
          <svg class="w-5 h-5" :class="darkMode ? 'text-gray-600' : 'text-gray-400'" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
          </svg>
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed, inject, ref } from 'vue'
import { useRouter } from 'vue-router'
import { useSession } from '@/data/session'

const router = useRouter()
const { user, logout, userFullName, userEmail } = useSession()
const darkMode = inject('darkMode', ref(false))

const fullName = computed(() => userFullName.value || user.value?.full_name || '')
const email = computed(() => userEmail.value || user.value?.email || '')
const initials = computed(() => {
  const name = fullName.value || 'U'
  return name.split(' ').map(w => w[0]).join('').toUpperCase().slice(0, 2)
})

const menuItems = [
  {
    label: 'My Orders',
    to: '/indtools/orders',
    iconBg: 'bg-blue-50',
    icon: '<svg class="w-5 h-5 text-blue-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2" /></svg>',
  },
  {
    label: 'Wishlist',
    to: '/indtools/wishlist',
    iconBg: 'bg-pink-50',
    icon: '<svg class="w-5 h-5 text-pink-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z" /></svg>',
  },
  {
    label: 'Notifications',
    to: '/indtools/notifications',
    iconBg: 'bg-amber-50',
    icon: '<svg class="w-5 h-5 text-amber-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 17h5l-1.405-1.405A2.032 2.032 0 0118 14.158V11a6.002 6.002 0 00-4-5.659V5a2 2 0 10-4 0v.341C7.67 6.165 6 8.388 6 11v3.159c0 .538-.214 1.055-.595 1.436L4 17h5m6 0v1a3 3 0 11-6 0v-1m6 0H9" /></svg>',
  },
  {
    label: 'Change Password',
    to: '/indtools/change-password',
    iconBg: 'bg-purple-50',
    icon: '<svg class="w-5 h-5 text-purple-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z" /></svg>',
  },
]

function handleLogout() {
  logout()
  router.push('/indtools/login')
}
</script>
