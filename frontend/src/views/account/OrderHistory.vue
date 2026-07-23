<template>
  <ion-page>
    <ion-header>
      <ion-toolbar class="bg-[#2a7f3e]">
        <ion-buttons slot="start">
          <button @click="$router.back()" class="px-2 py-1">
            <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7" />
            </svg>
          </button>
        </ion-buttons>
        <ion-title class="text-white font-semibold">My Orders</ion-title>
      </ion-toolbar>
    </ion-header>

    <ion-content class="ion-padding bg-[#f5f5f5]">
      <div class="max-w-lg mx-auto">
        <!-- Loading -->
        <div v-if="orders.loading" class="flex flex-col items-center justify-center py-20">
          <svg class="animate-spin h-8 w-8 text-[#2a7f3e] mb-3" fill="none" viewBox="0 0 24 24">
            <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4" />
            <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4z" />
          </svg>
          <span class="text-sm text-gray-500">Loading orders...</span>
        </div>

        <!-- Error -->
        <div v-else-if="orders.error" class="text-center py-20">
          <div class="inline-flex items-center justify-center w-16 h-16 rounded-full bg-red-100 mb-4">
            <svg class="w-8 h-8 text-red-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-2.5L13.732 4c-.77-.833-1.964-.833-2.732 0L4.082 16.5c-.77.833.192 2.5 1.732 2.5z" />
            </svg>
          </div>
          <p class="text-sm text-gray-500">Failed to load orders</p>
          <button @click="orders.reload()" class="mt-2 text-sm text-[#2a7f3e] font-semibold hover:underline">
            Retry
          </button>
        </div>

        <!-- Empty -->
        <div v-else-if="orders.data && orders.data.length === 0" class="text-center py-20">
          <div class="inline-flex items-center justify-center w-16 h-16 rounded-full bg-gray-100 mb-4">
            <svg class="w-8 h-8 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2" />
            </svg>
          </div>
          <p class="text-gray-900 font-semibold">No orders yet</p>
          <p class="text-sm text-gray-500 mt-1">Your order history will appear here</p>
          <router-link
            to="/indtools"
            class="inline-block mt-4 px-6 py-2.5 bg-[#2a7f3e] text-white text-sm font-semibold rounded-xl hover:bg-[#1a4d2a]"
          >
            Browse Products
          </router-link>
        </div>

        <!-- Orders List -->
        <div v-else class="space-y-3">
          <router-link
            v-for="order in orders.data"
            :key="order.name"
            :to="`/indtools/orders/${order.name}`"
            class="block bg-white rounded-xl shadow-sm p-4 active:bg-gray-50 transition-colors"
          >
            <div class="flex items-start justify-between">
              <div class="flex-1 min-w-0">
                <p class="text-sm font-bold text-gray-900 truncate">{{ order.name }}</p>
                <p class="text-xs text-gray-500 mt-1">{{ formatDate(order.creation) }}</p>
              </div>
              <div class="text-right ml-3">
                <p class="text-sm font-bold text-[#2a7f3e]">₹{{ formatAmount(order.grand_total) }}</p>
                <span
                  class="inline-block mt-1 px-2 py-0.5 text-xs font-semibold rounded-full"
                  :class="statusClass(order.status)"
                >
                  {{ order.status }}
                </span>
              </div>
            </div>
          </router-link>
        </div>
      </div>
    </ion-content>
  </ion-page>
</template>

<script setup>
import { onMounted } from 'vue'
import { IonPage, IonContent, IonHeader, IonToolbar, IonTitle, IonButtons } from '@ionic/vue'
import { createListResource } from 'frappe-ui'
import { sessionUser } from '@/data/session'

const orders = createListResource({
  doctype: 'Sales Order',
  fields: ['name', 'grand_total', 'status', 'creation'],
  filters: { owner: sessionUser() },
  orderBy: 'creation desc',
  limit: 20,
})

onMounted(() => {
  orders.fetch()
})

function formatDate(dateStr) {
  if (!dateStr) return ''
  const d = new Date(dateStr)
  return d.toLocaleDateString('en-IN', { day: 'numeric', month: 'short', year: 'numeric' })
}

function formatAmount(val) {
  return Number(val || 0).toLocaleString('en-IN', { minimumFractionDigits: 0, maximumFractionDigits: 0 })
}

function statusClass(status) {
  const s = (status || '').toLowerCase()
  if (s === 'completed' || s === 'delivered') return 'bg-green-100 text-green-700'
  if (s === 'cancelled') return 'bg-red-100 text-red-700'
  if (s === 'pending' || s === 'draft') return 'bg-yellow-100 text-yellow-700'
  if (s === 'processing' || s === 'in progress') return 'bg-blue-100 text-blue-700'
  return 'bg-gray-100 text-gray-700'
}
</script>
