<template>
  <div class="container">
    <h1 class="title">Fastest Finger First</h1>

    <Navbar
      :questions="questions"
      :activeIndex="activeIndex"
      :disabledQuestions="disabledQuestions"
      @select-question="selectQuestion"
    />

    <Timer ref="timerRef" />

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

    <!-- <Audioplayer /> -->

    <div v-if="submittedTime" class="mt-4 text-lg font-semibold text-green-400">
      Time Spent: {{ submittedTime }}
    </div>

    <div v-if="showTransition" class="transition-screen">
      <h2 class="transition-text">Get Ready for Next Question!</h2>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { useRouter } from "vue-router";
import Navbar from "../components/Navbar.vue";
import QuestionCard from "../components/QuestionDisplay.vue";
import Timer from "../components/Timer.vue";
import Audioplayer from "../components/Audioplayer.vue";
import { createListResource } from "frappe-ui";

const timerRef = ref(null);
const router = useRouter();

const questions = ref([]);
const activeIndex = ref(0);
const selectedOption = ref(null);
const currentQuestion = ref({});
const currentOptions = ref([]);
const submittedTime = ref("");
const disabledQuestions = ref([]);
const showTransition = ref(false);

const user_id = localStorage.getItem("user_id");
const user_name = localStorage.getItem("user_name");

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

const selectOption = (index) => {
  selectedOption.value = index;
};

const goToNextQuestion = () => {
  showTransition.value = true;
  setTimeout(() => {
    selectQuestion(activeIndex.value + 1);
    showTransition.value = false;
  }, 2000);
};

const submitAnswer = async () => {
  const time = timerRef.value?.getFormattedTime() || "00:00:00";
  submittedTime.value = time;
  const question = currentQuestion.value;
  const optionLabel = currentOptions.value[selectedOption.value];
  const answerData = {
    user_id,
    user_name,
    question_name: question.name,
    select_option: optionLabel,
    time_spent: time,
  };

  try {
    const response = await fetch(
      "/api/method/kbc.api.game_session.save_single_answer",
      {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ data: JSON.stringify(answerData) }),
      }
    );

    const result = await response.json();
    console.log("✅ API Response:", result);

    if (result.message === "success" || result.message?.message === "success") {
      alert("✅ Answer submitted successfully");
      disabledQuestions.value.push(activeIndex.value);

      if (activeIndex.value < questions.value.length - 1) {
        goToNextQuestion();
      } else {
        setTimeout(() => {
          router.push("/Leaderboard");
        }, 2000);
      }
    } else {
      const msg =
        typeof result.message === "object"
          ? JSON.stringify(result.message)
          : result.message;
      alert("⚠️ Failed: " + msg);
    }
  } catch (error) {
    console.error("❌ Network/API error:", error);
    alert("❌ Network error: " + error.message);
  }
};
</script>

<style scoped>
.container {
  max-width: 100%;
  height: 800px;
  margin: auto;
  text-align: center;
  padding: 10px;
  background: linear-gradient(to bottom right, #000428, #004e92);
  border-radius: 15px;
  color: #fff;
  font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
  box-shadow: 0 0 30px rgba(255, 255, 255, 0.1);
  overflow-x: hidden;
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

.transition-screen {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: #000;
  z-index: 9999;
  display: flex;
  align-items: center;
  justify-content: center;
}

.transition-text {
  font-size: 2.5rem;
  color: #ffc107;
  font-weight: bold;
  text-shadow: 2px 2px 5px rgba(255, 255, 255, 0.3);
}

/* Mobile Responsive */
@media screen and (max-width: 480px) {
  .container {
    padding: 20px;
    margin: 10px;
    max-width: 100%;
    border-radius: 10px;
    box-shadow: none;
    overflow-x: hidden;
  }

  .title {
    font-size: 1.8rem;
    margin-bottom: 20px;
  }

  h1, h2, h3, .transition-text {
    font-size: 1.5rem;
  }

  .submit-button {
    position: fixed;
    bottom: 15px;
    left: 50%;
    transform: translateX(-50%);
    width: 90%;
    z-index: 1000;
  }

  .submit-button button {
    width: 100%;
    padding: 12px;
    font-size: 1.1rem;
    border-radius: 25px;
  }

  .transition-screen {
    padding: 20px;
  }

  .transition-text {
    font-size: 1.8rem;
  }

  .text-center {
    font-size: 1.2rem;
  }

  .mt-4 {
    margin-top: 16px;
  }

  body, html {
    overflow-x: hidden;
  }
}
@media screen and (max-width: 360px) {
.container {
  padding: 16px;
  margin: 8px;
  max-width: 100%;
  border-radius: 8px;
  box-shadow: none;
  overflow-x: hidden;
}

.title {
  font-size: 1.4rem;
  margin-bottom: 18px;
}

h1, h2, h3, .transition-text {
  font-size: 1.3rem;
}

.submit-button {
  position: fixed;
  bottom: 12px;
  left: 50%;
  transform: translateX(-50%);
  width: 92%;
  z-index: 1000;
}

.submit-button button {
  width: 100%;
  padding: 10px;
  font-size: 1rem;
  border-radius: 22px;
}

.transition-screen {
  padding: 16px;
}

.transition-text {
  font-size: 1.5rem;
}

.text-center {
  font-size: 1.1rem;
}

.mt-4 {
  margin-top: 14px;
}

body, html {
  overflow-x: hidden;
}
}


</style>
