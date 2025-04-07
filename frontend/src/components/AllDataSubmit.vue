<template>
  <div class="submit-all-container">
    <button
      @click="submitAllAnswers"
      class="px-4 py-2 bg-purple-600 text-white font-semibold rounded hover:bg-purple-700"
    >
      Submit All Answers
    </button>
  </div>
</template>

<script setup>
import { createResource } from "frappe-ui";

const userName = "Ravi"; // Optional: Use dynamic session later

const submitAllAnswers = async () => {
  const stored = localStorage.getItem("submitted_answers");
  if (!stored) {
    alert("No answers found in localStorage.");
    return;
  }

  const answers = JSON.parse(stored);

  if (answers.length === 0) {
    alert("Answer list is empty.");
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
    await createResource({
      doctype: "Game Session",
      values: payload,
    }).submit();

    alert("All answers submitted to Game Session successfully!");
    localStorage.removeItem("submitted_answers");
  } catch (error) {
    console.error("Error submitting answers:", error);
    alert("Submission failed. Check console for details.");
  }
};
</script>

<style scoped>
.submit-all-container {
  margin-top: 20px;
}
</style>
