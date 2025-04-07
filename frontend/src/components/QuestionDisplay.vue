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
  background: #f8f9fa;
  color: #495057;
  padding: 20px;
  border-radius: 10px;
  font-size: 1.25rem;
  margin-bottom: 20px;
  box-shadow: 0px 3px 8px rgba(0, 0, 0, 0.1);
}

.options-container {
  display: flex;
  flex-direction: column;
  gap: 12px;
  align-items: flex-start;
  padding-left: 20px;
}

.option-item {
  background: #ffffff;
  padding: 12px 15px;
  border-radius: 8px;
  display: flex;
  align-items: center;
  font-size: 1.2rem;
  font-weight: 400;
  width: 100%;
  box-shadow: 0px 3px 6px rgba(0, 0, 0, 0.1);
  transition: 0.3s;
  cursor: pointer;
  border: 1px solid #dcdcdc;
}

.option-item:hover {
  background: #f1f1f1;
}

.selected {
  background: #e9ecef;
  color: #3e4953;
  transform: scale(1.05);
}

.option-number {
  font-weight: bold;
  font-size: 1.2rem;
  color: #007bff;
  margin-right: 10px;
}
</style>
