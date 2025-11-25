<script setup lang="ts">
import { onMounted, ref } from 'vue'

import VDataTableDemo from './components/VDataTableDemo.vue'

const data = ref<any>([])
const error = ref('')
const searchResult = ref<any>(null)

onMounted(async () => {
  try {
    const res = await fetch('http://localhost:5000/getDefault')
    if (!res.ok) throw new Error('Failed to fetch')
    data.value = await res.json()
  } catch (e) {
    error.value = 'Error fetching data'
  }
})

async function fetchSearch() {
  try {
    const res = await fetch('http://localhost:5000/getSongs', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ type: 'genre', key: 'love', algorithm: 'knn' }),
    })
    if (!res.ok) throw new Error('Failed to fetch')
    searchResult.value = await res.json()
  } catch (e) {
    error.value = 'Error fetching search result'
  }
}
</script>

<template>
  <div>
    <h1>Fetched Data from /get-data</h1>
    <div v-if="error" class="error-message text-red-500">{{ error }}</div>
    <ul v-else>
      <li v-for="(item, index) in data.data ?? data" :key="index">{{ item }}</li>
    </ul>
    <button @click="fetchSearch">Test /search POST</button>
    <div v-if="searchResult">
      <h2>/search Response</h2>
      <pre>{{ searchResult }}</pre>
    </div>
    <VDataTableDemo />
  </div>
</template>

<style scoped></style>
