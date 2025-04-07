<template>
  <nav class="navbar">
    <button
      v-for="(question, index) in questions"
      :key="question.name"
      class="nav-button"
      :class="{ active: activeIndex === index }"
      @click="$emit('select-question', index)"
    >
      {{ index + 1 }}
    </button>
  </nav>
</template>

<script setup>
defineProps({
  questions: Array,
  activeIndex: Number,
});

defineEmits(["select-question"]);
</script>

<style scoped>
.navbar {
  display: flex;
  justify-content: center;
  gap: 10px;
  background: #92a9c1;
  padding: 10px;
  border-radius: 8px;
  margin-bottom: 20px;
  overflow-x: auto;
  white-space: nowrap;
  padding-bottom: 5px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.05);
}

.navbar::-webkit-scrollbar {
  height: 6px;
}
.navbar::-webkit-scrollbar-thumb {
  background: #ccc;
  border-radius: 3px;
}

.nav-button {
  background: #ffffff;
  border: 1px solid #dee2e6;
  padding: 8px 14px;
  font-size: 1rem;
  font-weight: 500;
  cursor: pointer;
  border-radius: 6px;
  transition: background 0.2s, color 0.2s;
  color: #333;
}

.nav-button:hover {
  background: #92a9c1;
}

.active {
  background: #495057;
  color: #ffffff;
  border-color: #495057;
}
</style>

