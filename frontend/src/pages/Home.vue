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

    <button
      @click="viewStoredAnswers"
      class="mt-4 mr-1 px-4 py-2 bg-blue-500 text-white rounded"
    >
      View Stored Answers
    </button>

    <!-- 🔥 Removed Submit All Answers button here -->
    
    <!-- Custom Components -->
    <ClearDataInLocal />
    <AllDataSubmit/>
</div>
</template>


<script setup>
import { ref } from "vue";
import Navbar from "../components/Navbar.vue";
import QuestionCard from "../components/QuestionDisplay.vue";
import Timer from "../components/Timer.vue";
import { createListResource, createResource } from "frappe-ui";
import ClearDataInLocal from "../components/ClearDataInLocal.vue";
import AllDataSubmit from "../components/AllDataSubmit.vue";

const timerRef = ref(null);

const questions = ref([]);
const activeIndex = ref(0);
const selectedOption = ref(null);
const currentQuestion = ref({});
const currentOptions = ref([]);
const submittedTime = ref("");
// const showSubmitAllButton = ref(false); // 🔥 Track visibility

const userName = "ravi kumar"; // Optional: make dynamic with login or input

// Load Questions
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

const selectQuestion = (index) => {
  activeIndex.value = index;
  selectedOption.value = null;
  const question = questions.value[index] || {};
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

const selectOption = (index) => {
  selectedOption.value = index;
};

const submitAnswer = () => {
  timerRef.value?.pauseTimer();
  const exactTime = timerRef.value?.getFormattedTime();
  submittedTime.value = exactTime;

  const question = currentQuestion.value;
  const answerData = {
    question_name: question.name,
    selected_option: currentOptions.value[selectedOption.value],
    correct_answer: question.correct_answer,
    time_spent: exactTime,
    user_name: userName,
  };

  let existingData = JSON.parse(localStorage.getItem("submitted_answers") || "[]");

  const index = existingData.findIndex((ans) => ans.question_name === question.name);
  if (index >= 0) {
    existingData[index] = answerData;
  } else {
    existingData.push(answerData);
  }

  localStorage.setItem("submitted_answers", JSON.stringify(existingData));

  alert(`You selected: ${answerData.selected_option}\nTime: ${exactTime}`);

  // Go to next question
  if (activeIndex.value < questions.value.length - 1) {
    selectQuestion(activeIndex.value + 1);
  }

  // ✅ Show final submit button only after all questions answered
  // if (existingData.length === questions.value.length) {
  //   showSubmitAllButton.value = true;
  // }
};

const viewStoredAnswers = () => {
  const data = JSON.parse(localStorage.getItem("submitted_answers") || "[]");
  console.log("Stored Answers:", data);
  alert(JSON.stringify(data, null, 2));
};

const submitAllAnswersToGameSession = async () => {
  const answers = JSON.parse(localStorage.getItem("submitted_answers") || "[]");

  if (answers.length === 0) {
    alert("No answers to submit.");
    return;
  }

  const payload = {
    user_name: userName,
    questions: answers.map((ans) => ({
      question_name: ans.question_name,
      selected_option: ans.selected_option,
      correct_answer: ans.correct_answer,
      time_spent: ans.time_spent,
    })),
  };

  try {
    const response = await createResource({
      doctype: "Game Session",
      values: payload,
    }).submit();

    alert("Answers submitted to Game Session!");
    localStorage.removeItem("submitted_answers");
    showSubmitAllButton.value = false;
  } catch (err) {
    console.error("Submission error:", err);
    alert("Failed to submit answers.");
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
