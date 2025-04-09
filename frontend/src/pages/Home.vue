<template>
  <div class="container">
    <h1 class="title">Fastest Finger First</h1>

    <Navbar
      :questions="questions"
      :activeIndex="activeIndex"
      @select-question="selectQuestion"
    />

    <QuestionCard
      :question="currentQuestion"
      :options="currentOptions"
      :selectedOption="selectedOption"
      @select-option="selectOption"
    />

    <div class="submit-button">
      <button :disabled="selectedOption === null" @click="submitAnswer">
        Submit
      </button>
    </div>

    <Timer ref="timerRef" />

    <div v-if="submittedTime" class="mt-4 text-lg font-semibold text-green-700">
      Time Spent: {{ submittedTime }}
    </div>

  </div>
</template>

<script setup>
import { ref } from "vue";
import Navbar from "../components/Navbar.vue";
import QuestionCard from "../components/QuestionDisplay.vue";
import Timer from "../components/Timer.vue";
import { createListResource } from "frappe-ui";

const timerRef = ref(null);

const questions = ref([]);
const activeIndex = ref(0);
const selectedOption = ref(null);
const currentQuestion = ref({});
const currentOptions = ref([]);
const submittedTime = ref("");

// Load questions from Question doctype
const questionResource = createListResource({
  doctype: "Question",
  fields: [
    "name",
    "question_text",
    "option_1",
    "option_2",
    "option_3",
    "option_4",
    "correct_answer",
  ],
  auto: true,
  onSuccess(data) {
    questions.value = data;
    if (data.length > 0) selectQuestion(0);
  },
});

// Change active question
const selectQuestion = (index) => {
  activeIndex.value = index;
  selectedOption.value = null;

  const question = questions.value[index];
  currentQuestion.value = question;

  currentOptions.value = [
    question.option_1,
    question.option_2,
    question.option_3,
    question.option_4,
  ].filter(Boolean);

  timerRef.value?.resetTimer();
  timerRef.value?.startTimer();
};

// Option selected
const selectOption = (index) => {
  selectedOption.value = index;
};

// Submit single question
const submitAnswer = async () => {
  timerRef.value?.pauseTimer();
  const exactTime = timerRef.value?.getFormattedTime();
  submittedTime.value = exactTime;

  const answerData = {
    question_name: currentQuestion.value.name,
    selected_option: currentOptions.value[selectedOption.value],
    time_spent: exactTime,
  };

  try {
    const response = await fetch("/api/method/kbc.api.game_session.save_single_answer", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        data: JSON.stringify({
          answer: answerData
        })
      })
    });

    const result = await response.json();
    console.log("API Response:", result);
    if (result.message?.status === "success") {
      alert("✅ Answer submitted!");
      if (activeIndex.value < questions.value.length - 1) {
        selectQuestion(activeIndex.value + 1);
      }
    } else {
      alert("❌ Failed to submit answer: " + (result.message || "Unknown error"));
    }
  } catch (err) {
    console.error("❌ Error submitting answer:", err);
    alert("❌ Failed to submit answer.");
  }
};
</script>



<style scoped>
.container {
  max-width: 700px;
  margin: auto;
  text-align: center;
  padding: 30px;
  background: #f4f4f9;
  border-radius: 15px;
  box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.2);
}

.title {
  font-size: 2.2rem;
  font-weight: bold;
  color: #333;
  margin-bottom: 25px;
}

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
