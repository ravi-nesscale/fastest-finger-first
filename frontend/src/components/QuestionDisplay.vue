<template>
  <div>
    <div v-if="question" class="question-card">
      <h2>{{ question.question_text }}</h2>
    </div>

    <div class="options-container" v-if="options.length">
      <div
        v-for="(option, index) in options"
        :key="index"
        class="option-item"
        :class="{ selected: selectedOption === index }"
        @click="$emit('select-option', index)"
      >
        <span class="option-number">{{ index + 1 }}.</span>
        <span class="option-text">{{ option }}</span>
      </div>
    </div>
  </div>
</template>

<script setup>
defineProps({
  question: Object,
  options: Array,
  selectedOption: Number,
});

defineEmits(["select-option"]);
</script>
<style scoped>
.question-card {
  background: rgba(0, 0, 0, 0.3);
  color: gold;
  padding: 24px;
  border-radius: 12px;
  font-size: 1.5rem;
  font-weight: bold;
  margin-bottom: 25px;
  text-shadow: 1px 1px 4px rgba(0,0,0,0.6);
  border: 2px solid gold;
}

.options-container {
  display: flex;
  flex-direction: column;
  gap: 15px;
  align-items: center;
}

.option-item {
  background: #1a1a1a;
  color: white;
  padding: 14px 20px;
  border-radius: 25px;
  font-size: 1.2rem;
  font-weight: 500;
  width: 90%;
  max-width: 500px;
  box-shadow: inset 0 0 0 2px gold;
  transition: all 0.3s ease;
  cursor: pointer;
}

.option-item:hover {
  background: #292929;
}

.selected {
  background: #fbc02d;
  color: #000;
  transform: scale(1.03);
  box-shadow: 0 0 15px gold;
}

.option-number {
  font-weight: bold;
  font-size: 1.3rem;
  color: #03a9f4;
  margin-right: 10px;
}
</style>
