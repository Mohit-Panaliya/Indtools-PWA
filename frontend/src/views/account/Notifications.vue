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
        <ion-title class="text-white font-semibold">Notifications</ion-title>
      </ion-toolbar>
    </ion-header>

    <ion-content class="ion-padding bg-[#f5f5f5]">
      <div class="max-w-lg mx-auto">
        <!-- Loading -->
        <div v-if="notifications.loading" class="flex flex-col items-center justify-center py-20">
          <svg class="animate-spin h-8 w-8 text-[#2a7f3e] mb-3" fill="none" viewBox="0 0 24 24">
            <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4" />
            <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4z" />
          </svg>
          <span class="text-sm text-gray-500">Loading notifications...</span>
        </div>

        <!-- Error -->
        <div v-else-if="notifications.error" class="text-center py-20">
          <div class="inline-flex items-center justify-center w-16 h-16 rounded-full bg-red-100 mb-4">
            <svg class="w-8 h-8 text-red-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-2.5L13.732 4c-.77-.833-1.964-.833-2.732 0L4.082 16.5c-.77.833.192 2.5 1.732 2.5z" />
            </svg>
          </div>
          <p class="text-sm text-gray-500">Failed to load notifications</p>
          <button @click="notifications.reload()" class="mt-2 text-sm text-[#2a7f3e] font-semibold hover:underline">
            Retry
          </button>
        </div>

        <!-- Empty -->
        <div v-else-if="notifications.data && notifications.data.length === 0" class="text-center py-20">
          <div class="inline-flex items-center justify-center w-16 h-16 rounded-full bg-gray-100 mb-4">
            <svg class="w-8 h-8 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                d="M15 17h5l-1.405-1.405A2.032 2.032 0 0118 14.158V11a6.002 6.002 0 00-4-5.659V5a2 2 0 10-4 0v.341C7.67 6.165 6 8.388 6 11v3.159c0 .538-.214 1.055-.595 1.436L4 17h5m6 0v1a3 3 0 11-6 0v-1m6 0H9" />
            </svg>
          </div>
          <p class="text-gray-900 font-semibold">No notifications</p>
          <p class="text-sm text-gray-500 mt-1">You're all caught up!</p>
        </div>

        <!-- Notifications List -->
        <div v-else class="space-y-2">
          <div
            v-for="notif in notifications.data"
            :key="notif.name"
            class="bg-white rounded-xl shadow-sm p-4 transition-colors"
            :class="notif.read ? 'opacity-75' : 'border-l-4 border-[#2a7f3e]'"
          >
            <div class="flex items-start justify-between mb-1">
              <p class="text-sm font-semibold text-gray-900" :class="{ 'font-bold': !notif.read }">
                {{ notif.subject }}
              </p>
              <span v-if="!notif.read" class="w-2 h-2 rounded-full bg-[#2a7f3e] ml-2 mt-1.5 flex-shrink-0" />
            </div>
            <p class="text-xs text-gray-500 mb-1">{{ formatDate(notif.creation) }}</p>
            <p
              v-if="notif.email_content"
              class="text-xs text-gray-600 line-clamp-2"
              v-html="stripHtml(notif.email_content)"
            />
          </div>
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

const notifications = createListResource({
  doctype: 'Notification Log',
  fields: ['subject', 'email_content', 'creation', 'read'],
  filters: { for_user: sessionUser() },
  orderBy: 'creation desc',
  limit: 30,
})

onMounted(() => {
  notifications.fetch()
})

function formatDate(dateStr) {
  if (!dateStr) return ''
  const d = new Date(dateStr)
  return d.toLocaleDateString('en-IN', { day: 'numeric', month: 'short', year: 'numeric', hour: '2-digit', minute: '2-digit' })
}

function stripHtml(html) {
  if (!html) return ''
  return html.replace(/<[^>]+>/g, '').trim()
}
</script>
