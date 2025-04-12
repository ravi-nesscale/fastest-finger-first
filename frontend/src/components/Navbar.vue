<template>
  <nav class="navbar">
    <button
      v-for="(question, index) in questions"
      :key="question.name"
      class="nav-button"
      :class="{ active: activeIndex === index }"
      :disabled="disabledQuestions.includes(index)"
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
  disabledQuestions: Array,
});

defineEmits(["select-question"]);
</script>

<style scoped>
.navbar {
  display: flex;
  justify-content: center;
  gap: 10px;
  background: linear-gradient(to right, #001f3f, #004e92);
  padding: 12px;
  border-radius: 12px;
  margin-bottom: 25px;
  overflow-x: auto;
  white-space: nowrap;
  box-shadow: 0 3px 10px rgba(0, 0, 0, 0.2);
}

.navbar::-webkit-scrollbar {
  height: 6px;
}
.navbar::-webkit-scrollbar-thumb {
  background: #666;
  border-radius: 4px;
}

.nav-button {
  background: #fff;
  border: 2px solid #ccc;
  padding: 10px 16px;
  font-size: 1rem;
  font-weight: bold;
  cursor: pointer;
  border-radius: 8px;
  transition: all 0.3s ease;
  color: #222;
  min-width: 42px;
}

.nav-button:hover:not(:disabled) {
  background-color: #f8c93c;
  color: #000;
  border-color: #f1b800;
}

.nav-button:disabled {
  background: #999;
  color: #eee;
  border-color: #888;
  cursor: not-allowed;
  box-shadow: none;
  opacity: 0.6;
}

.active {
  background: #f8c93c;
  color: #000;
  border-color: #e0a800;
  box-shadow: 0 0 10px rgba(255, 215, 0, 0.6);
}
</style>
