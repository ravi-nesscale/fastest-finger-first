<template>
  <div>
    <div v-if="question" class="question-card">
      <h2>{{ question.question_text }}</h2>
    </div>

    <div class="options-grid">
      <div
        v-for="(option, index) in options"
        :key="index"
        class="option-item"
        :class="{ selected: selectedOption === index }"
        @click="$emit('select-option', index)"
      >
        <span class="option-number">{{ index + 1 }}</span>
        <span class="option-text">{{ option }}</span>
      </div>

      <!-- Timer slot in center if odd number or at position 2 for 4 options -->
      <div v-if="options.length === 4" class="timer-slot">
        <slot name="timer"></slot>
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
  background: linear-gradient(135deg, #222, #000);
  color: #ffeb3b;
  padding: 10px;
  border-radius: 15px;
  font-size: 1.5rem;
  font-weight: 300;
  margin-bottom: 35px;
  text-align: center;
  border: 3px solid #ffeb3b;
  box-shadow: 0 0 20px rgba(255, 235, 59, 0.5);
  text-shadow: 2px 2px 8px rgba(0, 0, 0, 0.7);
}

.options-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  grid-gap: 20px;
  justify-items: center;
  align-items: center;
}

.option-item {
  display: flex;
  align-items: center;
  background: linear-gradient(145deg, #1c1c1c, #111);
  color: #eee;
  padding: 8px 10px;
  border-radius: 30px;
  font-size: 1.1rem;
  font-weight: 300;
  width: 80%;
  max-width: 100%;
  box-shadow: inset 0 0 0 2px #ffeb3b;
  transition: all 0.25s ease;
  cursor: pointer;
}

.option-item:hover {
  background: #292929;
  box-shadow: 0 0 12px #ffeb3b;
}

.selected {
  background: #ffeb3b;
  color: #000;
  transform: scale(1.05);
  box-shadow: 0 0 20px #ffeb3b;
}

.option-number {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  background: #1877a3;
  color: #fff;
  font-weight: bold;
  font-size: 1.3rem;
  width: 40px;
  height: 40px;
  border-radius: 50%;
  margin-right: 15px;
  box-shadow: 0 0 10px rgba(3, 169, 244, 0.5);
}

.option-text {
  flex: 1;
}

.timer-slot {
  grid-column: span 2;
  display: flex;
  justify-content: center;
  align-items: center;
  margin-top: 10px;
}

/* 📱 Mobile responsiveness */
@media (max-width: 480px) {
  .question-card {
    font-size: 1.2rem;
    padding: 8px;
    margin-bottom: 25px;
  }

  .options-grid {
    grid-template-columns: 1fr;
    grid-gap: 15px;
  }

  .option-item {
    width: 90%;
    padding: 10px;
    font-size: 1rem;
  }

  .option-number {
    font-size: 1.1rem;
    width: 35px;
    height: 35px;
    margin-right: 10px;
  }

  .timer-slot {
    grid-column: span 1;
    margin-top: 8px;
  }
}

/* Even tighter for ultra-small 320px screens */
@media (max-width: 360px) {
  .question-card {
    font-size: 1rem;
    padding: 6px;
  }

  .option-item {
    font-size: 0.95rem;
    padding: 8px;
  }

  .option-number {
    font-size: 1rem;
    width: 30px;
    height: 30px;
    margin-right: 8px;
  }
}
</style>

