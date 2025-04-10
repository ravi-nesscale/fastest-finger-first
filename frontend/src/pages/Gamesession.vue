<template>
    <div class="container">
      <h1 class="title">Fastest Finger First</h1>
  
  
  
      <Navbar :questions="questions" :activeIndex="activeIndex" @select-question="selectQuestion" />
  
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
      <h1 class="text-center text-3xl mt-3 font-bold text-yellow-400 hover:text-yellow-300 transition duration-300">
      <router-link to="/leaderboard">LEADER BOARD</router-link>
    </h1>
      <div v-if="submittedTime" class="mt-4 text-lg font-semibold text-green-700">
        Time Spent: {{ submittedTime }}
      </div>
      <Audioplayer/>
    </div>
    
  </template>
  
  <script setup>
  import { ref } from "vue";
  import Navbar from "../components/Navbar.vue";
  import QuestionCard from "../components/QuestionDisplay.vue";
  import Timer from "../components/Timer.vue";
  import { createListResource } from "frappe-ui";
  import Audioplayer from "../components/Audioplayer.vue";
  
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
      select_option: currentOptions.value[selectedOption.value],
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
    max-width: 800px;
    margin: auto;
    text-align: center;
    padding: 40px;
    background: linear-gradient(to bottom right, #000428, #004e92);
    border-radius: 15px;
    color: #fff;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    box-shadow: 0 0 30px rgba(255, 255, 255, 0.1);
    position: relative;
  }
  
  .title {
    font-size: 2.8rem;
    font-weight: bold;
    color: gold;
    margin-bottom: 30px;
    text-shadow: 2px 2px 5px rgba(0, 0, 0, 0.6);
  }
  
  .submit-button {
    margin-top: 25px;
  }
  
  .submit-button button {
    padding: 14px 24px;
    font-size: 1.3rem;
    font-weight: bold;
    color: #fff;
    background: linear-gradient(145deg, #ffc107, #ff9800);
    border: none;
    border-radius: 30px;
    cursor: pointer;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
    transition: 0.3s;
  }
  
  .submit-button button:disabled {
    background: #777;
    cursor: not-allowed;
  }
  
  .submit-button button:hover:not(:disabled) {
    background: #ffa000;
  }
  
  
  </style>
  