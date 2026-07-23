<template>
  <div :class="darkMode ? 'bg-[#0f1710]' : 'bg-[#f5f5f5]'" class="min-h-screen">
    <!-- Hero Banner -->
    <div :class="darkMode ? 'bg-[#1a2e1f]' : 'bg-gradient-to-r from-[#1a4d2a] to-[#2a7f3e]'" class="py-10 md:py-14">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <h1 :class="darkMode ? 'text-green-300' : 'text-white'" class="text-3xl md:text-4xl font-bold mb-2">About INDTOOLS</h1>
        <nav class="flex items-center space-x-2 text-sm">
          <router-link :class="darkMode ? 'text-green-400' : 'text-green-200'" to="/" class="hover:underline">Home</router-link>
          <span :class="darkMode ? 'text-green-500' : 'text-green-300'">/</span>
          <span :class="darkMode ? 'text-green-200' : 'text-white'" class="opacity-80">About Us</span>
        </nav>
      </div>
    </div>

    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 md:py-12">
      <!-- Company Overview -->
      <div class="grid md:grid-cols-2 gap-10 items-center mb-12 md:mb-16">
        <div>
          <span :class="darkMode ? 'text-[#4caf50]' : 'text-[#2a7f3e]'" class="text-sm font-bold uppercase tracking-widest">Our Story</span>
          <h2 :class="darkMode ? 'text-white' : 'text-[#1a4d2a]'" class="text-2xl md:text-3xl font-bold mt-2 mb-6">Three Decades of Excellence in Fastener Manufacturing</h2>
          <p :class="darkMode ? 'text-gray-400' : 'text-gray-600'" class="mb-4 leading-relaxed">
            Established in 1992, INDTOOLS has grown from a small manufacturing unit to one of Gujarat's leading producers of industrial fasteners. Our journey began with a simple vision: to provide quality fasteners that industries can depend on.
          </p>
          <p :class="darkMode ? 'text-gray-400' : 'text-gray-600'" class="mb-4 leading-relaxed">
            Located in the industrial hub of GIDC Anand, Gujarat, our state-of-the-art facility spans over 15,000 sq. ft. and is equipped with modern CNC machines, hydraulic presses, and quality testing laboratories.
          </p>
          <p :class="darkMode ? 'text-gray-400' : 'text-gray-600'" class="leading-relaxed">
            Over the years, we have served industries ranging from automotive, construction, oil & gas, railways, and heavy engineering across India and abroad.
          </p>
        </div>
        <div :class="darkMode ? 'bg-[#1a2e1f]' : 'bg-[#e8f5e9]'" class="rounded-3xl p-8 relative overflow-hidden">
          <div class="absolute top-0 right-0 w-40 h-40 bg-[#4caf50]/10 rounded-full -translate-y-1/2 translate-x-1/2"></div>
          <div class="relative space-y-5">
            <div v-for="item in milestones" :key="item.year" class="flex items-start gap-4">
              <div class="w-14 h-14 rounded-xl bg-[#2a7f3e] flex items-center justify-center flex-shrink-0">
                <span class="text-white font-bold text-sm">{{ item.year }}</span>
              </div>
              <div>
                <h4 :class="darkMode ? 'text-white' : 'text-[#1a4d2a]'" class="font-bold">{{ item.title }}</h4>
                <p :class="darkMode ? 'text-gray-400' : 'text-gray-500'" class="text-sm">{{ item.desc }}</p>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Mission & Vision -->
      <div class="grid sm:grid-cols-2 gap-6 mb-12 md:mb-16">
        <div :class="darkMode ? 'bg-[#1a2e1f] border-[#2a7f3e]/30' : 'bg-white border-gray-100'" class="rounded-2xl border p-8">
          <div class="w-14 h-14 rounded-xl bg-[#e8f5e9] flex items-center justify-center mb-4">
            <span class="text-2xl">🎯</span>
          </div>
          <h3 :class="darkMode ? 'text-white' : 'text-[#1a4d2a]'" class="text-xl font-bold mb-3">Our Mission</h3>
          <p :class="darkMode ? 'text-gray-400' : 'text-gray-600'" class="leading-relaxed">
            To manufacture and supply premium quality industrial fasteners that meet the highest standards of strength, durability, and precision, while maintaining competitive pricing and exceptional customer service.
          </p>
        </div>
        <div :class="darkMode ? 'bg-[#1a2e1f] border-[#2a7f3e]/30' : 'bg-white border-gray-100'" class="rounded-2xl border p-8">
          <div class="w-14 h-14 rounded-xl bg-[#e8f5e9] flex items-center justify-center mb-4">
            <span class="text-2xl">👁️</span>
          </div>
          <h3 :class="darkMode ? 'text-white' : 'text-[#1a4d2a]'" class="text-xl font-bold mb-3">Our Vision</h3>
          <p :class="darkMode ? 'text-gray-400' : 'text-gray-600'" class="leading-relaxed">
            To be recognized as India's most trusted fastener brand, known for innovation, quality, and reliability. We aspire to set new benchmarks in the fastener industry through continuous improvement and technological advancement.
          </p>
        </div>
      </div>

      <!-- Values -->
      <div class="text-center mb-10">
        <span :class="darkMode ? 'text-[#4caf50]' : 'text-[#2a7f3e]'" class="text-sm font-bold uppercase tracking-widest">Core Values</span>
        <h2 :class="darkMode ? 'text-white' : 'text-[#1a4d2a]'" class="text-2xl md:text-3xl font-bold mt-2 mb-4">What Drives Us</h2>
        <div class="w-20 h-1 bg-[#4caf50] mx-auto rounded-full"></div>
      </div>
      <div class="grid sm:grid-cols-2 lg:grid-cols-4 gap-6">
        <div v-for="val in values" :key="val.title" :class="darkMode ? 'bg-[#1a2e1f] border-[#2a7f3e]/20' : 'bg-white border-gray-100'" class="rounded-2xl border p-6 text-center">
          <div class="w-14 h-14 mx-auto mb-4 rounded-2xl bg-[#e8f5e9] flex items-center justify-center">
            <span class="text-2xl">{{ val.icon }}</span>
          </div>
          <h3 :class="darkMode ? 'text-white' : 'text-[#1a4d2a]'" class="font-bold mb-2">{{ val.title }}</h3>
          <p :class="darkMode ? 'text-gray-400' : 'text-gray-500'" class="text-sm leading-relaxed">{{ val.desc }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, inject } from 'vue'

const darkMode = inject('darkMode', ref(false))

const milestones = [
  { year: '1992', title: 'Founded', desc: 'Started operations in Anand, Gujarat' },
  { year: '2005', title: 'GIDC Facility', desc: 'Expanded to GIDC industrial estate' },
  { year: '2015', title: 'ISO Certified', desc: 'Achieved ISO 9001:2015 certification' },
  { year: '2020', title: 'Digital Presence', desc: 'Launched online ordering platform' }
]

const values = [
  { icon: '🏆', title: 'Quality', desc: 'Every product passes through rigorous quality checks before dispatch.' },
  { icon: '🤝', title: 'Integrity', desc: 'Transparent business practices and honest dealings with all stakeholders.' },
  { icon: '💡', title: 'Innovation', desc: 'Continuous improvement in manufacturing processes and product design.' },
  { icon: '🌱', title: 'Sustainability', desc: 'Eco-friendly manufacturing practices and responsible resource usage.' }
]
</script>
