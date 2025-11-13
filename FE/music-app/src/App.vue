<script setup lang="ts">
import { ref, onMounted } from 'vue'

const message = ref('')

onMounted(async () => {
  const res = await fetch('http://localhost:5000/')
  message.value = await res.text()
})
</script>

<template>
  <div>
    {{ message }}
  </div>
</template>

<style scoped>
header {
  line-height: 1.5;
}
</style>
