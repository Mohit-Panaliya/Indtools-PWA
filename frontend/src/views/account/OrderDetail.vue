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
        <ion-title class="text-white font-semibold">Order Details</ion-title>
      </ion-toolbar>
    </ion-header>

    <ion-content class="ion-padding bg-[#f5f5f5]">
      <div class="max-w-lg mx-auto">
        <!-- Loading -->
        <div v-if="doc.loading" class="flex flex-col items-center justify-center py-20">
          <svg class="animate-spin h-8 w-8 text-[#2a7f3e] mb-3" fill="none" viewBox="0 0 24 24">
            <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4" />
            <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4z" />
          </svg>
          <span class="text-sm text-gray-500">Loading order details...</span>
        </div>

        <!-- Error -->
        <div v-else-if="doc.error" class="text-center py-20">
          <div class="inline-flex items-center justify-center w-16 h-16 rounded-full bg-red-100 mb-4">
            <svg class="w-8 h-8 text-red-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-2.5L13.732 4c-.77-.833-1.964-.833-2.732 0L4.082 16.5c-.77.833.192 2.5 1.732 2.5z" />
            </svg>
          </div>
          <p class="text-sm text-gray-500">Failed to load order</p>
          <button @click="doc.reload()" class="mt-2 text-sm text-[#2a7f3e] font-semibold hover:underline">
            Retry
          </button>
        </div>

        <template v-else-if="doc.data">
          <!-- Order Header -->
          <div class="bg-white rounded-xl shadow-sm p-5 mb-4">
            <div class="flex items-start justify-between mb-3">
              <div>
                <p class="text-xs text-gray-500">Order ID</p>
                <p class="text-base font-bold text-gray-900">{{ doc.data.name }}</p>
              </div>
              <span
                class="px-2.5 py-1 text-xs font-semibold rounded-full"
                :class="statusClass(doc.data.status)"
              >
                {{ doc.data.status }}
              </span>
            </div>
            <div class="grid grid-cols-2 gap-3 pt-3 border-t border-gray-100">
              <div>
                <p class="text-xs text-gray-500">Date</p>
                <p class="text-sm font-medium text-gray-900">{{ formatDate(doc.data.creation) }}</p>
              </div>
              <div>
                <p class="text-xs text-gray-500">Total</p>
                <p class="text-sm font-bold text-[#2a7f3e]">₹{{ formatAmount(doc.data.grand_total) }}</p>
              </div>
            </div>
          </div>

          <!-- Items -->
          <div class="bg-white rounded-xl shadow-sm overflow-hidden">
            <div class="px-5 py-3 border-b border-gray-100">
              <h3 class="text-sm font-bold text-gray-900">Items</h3>
            </div>

            <div v-if="doc.data.items && doc.data.items.length > 0">
              <div
                v-for="(item, idx) in doc.data.items"
                :key="idx"
                class="px-5 py-3 border-b border-gray-50 last:border-b-0"
              >
                <div class="flex items-start justify-between">
                  <div class="flex-1 min-w-0">
                    <p class="text-sm font-medium text-gray-900 truncate">{{ item.item_name || item.item_code }}</p>
                    <p class="text-xs text-gray-500 mt-0.5">
                      {{ item.qty }} × ₹{{ formatAmount(item.rate) }}
                    </p>
                  </div>
                  <p class="text-sm font-semibold text-gray-900 ml-3">
                    ₹{{ formatAmount(item.amount) }}
                  </p>
                </div>
              </div>
            </div>

            <div v-else class="px-5 py-6 text-center">
              <p class="text-sm text-gray-500">No items found</p>
            </div>

            <!-- Total -->
            <div class="px-5 py-3 bg-gray-50 flex items-center justify-between">
              <span class="text-sm font-bold text-gray-900">Grand Total</span>
              <span class="text-base font-bold text-[#2a7f3e]">₹{{ formatAmount(doc.data.grand_total) }}</span>
            </div>
          </div>
        </template>
      </div>
    </ion-content>
  </ion-page>
</template>

<script setup>
import { onMounted } from 'vue'
import { useRoute } from 'vue-router'
import { IonPage, IonContent, IonHeader, IonToolbar, IonTitle, IonButtons } from '@ionic/vue'
import { createDocumentResource } from 'frappe-ui'

const route = useRoute()

const doc = createDocumentResource({
  doctype: 'Sales Order',
  name: route.params.id,
})

onMounted(() => {
  doc.fetch()
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
