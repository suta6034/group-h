<script setup lang="ts">
import { ref, onMounted } from 'vue'

import VDataTableDemo from './components/VDataTableDemo.vue'

const data = ref<number[]>([])
const error = ref('')

onMounted(async () => {
  try {
    const res = await fetch('http://localhost:5000/get-data')
    if (!res.ok) throw new Error('Failed to fetch')
    data.value = await res.json()
  } catch (e) {
    error.value = 'Error fetching data'
  }
})
</script>

<template>
  <div>
    <h1>Fetched Data from /get-data</h1>
    <div v-if="error">{{ error }}</div>
    <ul v-else>
      <li v-for="item in data" :key="item">{{ item }}</li>
    </ul>
    <VDataTableDemo />
  </div>
</template>

<style scoped>
header {
  line-height: 1.5;
}
</style>
