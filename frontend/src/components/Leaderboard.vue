<template>
  <div class="container">
    <!-- Game Header -->
    <h1 class="title">Fastest Finger First</h1>

    <!-- Navigation for Questions -->
    <nav class="navbar">
      <button
        v-for="(q, index) in questions"
        :key="q.name"
        class="nav-button"
        :class="{ active: activeIndex === index }"
        @click="selectQuestion(index)"
      >
        {{ index + 1 }}
      </button>
    </nav>

    <!-- Question Card -->
    <div v-if="currentQuestion" class="question-card">
      <h2>{{ currentQuestion.question_text }}</h2>
    </div>

    <!-- Answer Options -->
    <div class="options-container" v-if="options.length">
      <div
        v-for="(option, index) in options"
        :key="index"
        class="option-item"
        :class="{ selected: selectedOption === index }"
        @click="selectOption(index)"
      >
        <span class="option-number">{{ index + 1 }}.</span> 
        <span class="option-text">{{ option }}</span>
      </div>
    </div>

    <!-- Submit Button -->
    <div class="submit-button">
      <button :disabled="selectedOption === null" @click="submitAnswer">Submit</button>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from "vue";
import { createListResource } from "frappe-ui";

// Reactive variables
const questions = ref([]);
const activeIndex = ref(0);
const selectedOption = ref(null);

// Fetch all questions
const questionListResource = createListResource({
  doctype: "Question",
  fields: ["name", "question_text", "option_1", "option_2", "option_3", "option_4", "correct_answer"],
  auto: true,
  onSuccess(data) {
    questions.value = data;
  },
});

// Compute current question dynamically
const currentQuestion = computed(() => questions.value[activeIndex.value] || null);

// Compute options dynamically
const options = computed(() => currentQuestion.value
  ? [currentQuestion.value.option_1, currentQuestion.value.option_2, currentQuestion.value.option_3, currentQuestion.value.option_4]
  : []);

// Select a question and reset selection
const selectQuestion = (index) => {
  activeIndex.value = index;
  selectedOption.value = null; // Reset selection when switching
};

// Select an option
const selectOption = (index) => {
  selectedOption.value = index;
};

// Submit answer
const submitAnswer = () => {
  alert(`You selected: ${options.value[selectedOption.value]}`);
};
</script>

<style scoped>
/* General Container */
.container {
  max-width: 700px;
  margin: auto;
  text-align: center;
  padding: 30px;
  background: #f4f4f9;
  border-radius: 15px;
  box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.2);
}

/* Game Title */
.title {
  font-size: 2.2rem;
  font-weight: bold;
  color: #333;
  margin-bottom: 25px;
}

/* Navigation Bar */
.navbar {
  display: flex;
  justify-content: center;
  gap: 10px;
  background: #007bff;
  padding: 10px;
  border-radius: 8px;
  margin-bottom: 20px;
}

.nav-button {
  background: white;
  border: none;
  padding: 10px 15px;
  font-size: 1.1rem;
  font-weight: bold;
  cursor: pointer;
  border-radius: 5px;
  transition: 0.3s;
}

.nav-button:hover {
  background: #ddd;
}

.active {
  background: #354e68;
  color: white;
}

/* Question Card */
.question-card {
  background: #007bff;
  color: white;
  padding: 20px;
  border-radius: 10px;
  font-size: 1.5rem;
  margin-bottom: 20px;
  box-shadow: 0px 3px 8px rgba(0, 0, 0, 0.2);
}

/* Answer Options */
.options-container {
  display: flex;
  flex-direction: column;
  gap: 12px;
  align-items: flex-start;
  padding-left: 20px;
}

/* Option Item */
.option-item {
  background: #ffffff;
  padding: 12px 15px;
  border-radius: 8px;
  display: flex;
  align-items: center;
  font-size: 1.2rem;
  font-weight: 500;
  width: 100%;
  box-shadow: 0px 3px 6px rgba(0, 0, 0, 0.15);
  transition: 0.3s;
  cursor: pointer;
}

/* Selected Option */
.selected {
  background: #007bff;
  color: white;
  transform: scale(1.05);
}

/* Number Style */
.option-number {
  font-weight: bold;
  font-size: 1.3rem;
  color: #007bff;
  margin-right: 10px;
}

/* Submit Button */
.submit-button {
  margin-top: 20px;
}

.submit-button button {
  padding: 12px 20px;
  font-size: 1.2rem;
  font-weight: bold;
  color: white;
  background: #28a745;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: 0.3s;
}

.submit-button button:disabled {
  background: #cccccc;
  cursor: not-allowed;
}

.submit-button button:hover:not(:disabled) {
  background: #218838;
}
</style>
