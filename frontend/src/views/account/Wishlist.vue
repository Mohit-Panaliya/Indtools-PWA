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
        <ion-title class="text-white font-semibold">My Wishlist</ion-title>
      </ion-toolbar>
    </ion-header>

    <ion-content class="ion-padding bg-[#f5f5f5]">
      <div class="max-w-lg mx-auto">
        <!-- Loading -->
        <div v-if="wishlist.loading" class="flex flex-col items-center justify-center py-20">
          <svg class="animate-spin h-8 w-8 text-[#2a7f3e] mb-3" fill="none" viewBox="0 0 24 24">
            <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4" />
            <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4z" />
          </svg>
          <span class="text-sm text-gray-500">Loading wishlist...</span>
        </div>

        <!-- Error -->
        <div v-else-if="wishlist.error" class="text-center py-20">
          <div class="inline-flex items-center justify-center w-16 h-16 rounded-full bg-red-100 mb-4">
            <svg class="w-8 h-8 text-red-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-2.5L13.732 4c-.77-.833-1.964-.833-2.732 0L4.082 16.5c-.77.833.192 2.5 1.732 2.5z" />
            </svg>
          </div>
          <p class="text-sm text-gray-500">Failed to load wishlist</p>
          <button @click="wishlist.reload()" class="mt-2 text-sm text-[#2a7f3e] font-semibold hover:underline">
            Retry
          </button>
        </div>

        <!-- Empty -->
        <div v-else-if="localItems.length === 0" class="text-center py-20">
          <div class="inline-flex items-center justify-center w-16 h-16 rounded-full bg-pink-100 mb-4">
            <svg class="w-8 h-8 text-pink-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z" />
            </svg>
          </div>
          <p class="text-gray-900 font-semibold">Wishlist is empty</p>
          <p class="text-sm text-gray-500 mt-1">Save items you love for later</p>
          <router-link
            to="/indtools"
            class="inline-block mt-4 px-6 py-2.5 bg-[#2a7f3e] text-white text-sm font-semibold rounded-xl hover:bg-[#1a4d2a]"
          >
            Browse Products
          </router-link>
        </div>

        <!-- Items Grid -->
        <div v-else class="grid grid-cols-2 gap-3">
          <div
            v-for="item in localItems"
            :key="item.item_code"
            class="bg-white rounded-xl shadow-sm overflow-hidden"
          >
            <div class="aspect-square bg-gray-100 flex items-center justify-center overflow-hidden">
              <img
                v-if="item.website_image"
                :src="item.website_image"
                :alt="item.item_name"
                class="w-full h-full object-cover"
              />
              <svg v-else class="w-10 h-10 text-gray-300" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"
                  d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z" />
              </svg>
            </div>
            <div class="p-3">
              <p class="text-xs font-medium text-gray-900 line-clamp-2 min-h-[2.5rem]">{{ item.item_name }}</p>
              <p class="text-sm font-bold text-[#2a7f3e] mt-1">₹{{ formatAmount(item.price) }}</p>
              <button
                @click="removeItem(item)"
                :disabled="removing === item.item_code"
                class="mt-2 w-full py-1.5 text-xs font-semibold text-red-500 bg-red-50 rounded-lg hover:bg-red-100 transition-colors disabled:opacity-50"
              >
                <span v-if="removing === item.item_code">Removing...</span>
                <span v-else>Remove</span>
              </button>
            </div>
          </div>
        </div>
      </div>
    </ion-content>
  </ion-page>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import { IonPage, IonContent, IonHeader, IonToolbar, IonTitle, IonButtons } from '@ionic/vue'
import { createListResource } from 'frappe-ui'
import { sessionUser } from '@/data/session'
import { removeFromWishlist } from '@/data/products'

const removing = ref(null)

const wishlist = createListResource({
  doctype: 'Wishlist',
  fields: ['item_code', 'item_name', 'website_image', 'price'],
  filters: { owner: sessionUser() },
  orderBy: 'creation desc',
  limit: 50,
})

const localItems = computed(() => wishlist.data || [])

onMounted(() => {
  wishlist.fetch()
})

function formatAmount(val) {
  return Number(val || 0).toLocaleString('en-IN', { minimumFractionDigits: 0, maximumFractionDigits: 0 })
}

async function removeItem(item) {
  removing.value = item.item_code
  try {
    await removeFromWishlist.submit({ item_code: item.item_code })
    localItems.value = localItems.value.filter(i => i.item_code !== item.item_code)
  } catch (e) {
    // silently fail
  } finally {
    removing.value = null
  }
}
</script>
