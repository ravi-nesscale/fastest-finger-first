<template>
    <div class="mt-8 p-4 bg-white rounded shadow-md">
      <h2 class="text-xl font-semibold mb-4 text-center">📋 Submitted Answers</h2>
  
      <!-- Clear Button -->
      <div class="text-right mb-2">
        <button @click="clearAnswers" class="bg-red-500 hover:bg-red-600 text-white px-3 py-1 rounded">
          Clear All Answers
        </button>
      </div>
  
      <table class="min-w-full text-sm text-left border border-gray-300">
        <thead class="bg-gray-100">
          <tr>
            <th class="py-2 px-4 border">#</th>
            <th class="py-2 px-4 border">Question</th>
            <th class="py-2 px-4 border">Selected Option</th>
            <th class="py-2 px-4 border">Time Spent</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(answer, index) in answers" :key="index" class="hover:bg-gray-50">
            <td class="py-2 px-4 border">{{ index + 1 }}</td>
            <td class="py-2 px-4 border">{{ answer.question_name }}</td>
            <td class="py-2 px-4 border">{{ answer.selected_option }}</td>
            <td class="py-2 px-4 border">{{ answer.time_spent }}</td>
          </tr>
          <tr v-if="answers.length === 0">
            <td colspan="4" class="text-center py-3 text-gray-500">No answers submitted yet.</td>
          </tr>
        </tbody>
      </table>
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue';
  
  const answers = ref([]);
  
  const loadAnswers = () => {
    const storedAnswers = localStorage.getItem("submitted_answers");
    answers.value = storedAnswers ? JSON.parse(storedAnswers) : [];
  };
  
  const clearAnswers = () => {
    localStorage.removeItem("submitted_answers");
    answers.value = [];
    alert("All answers cleared from localStorage!");
  };
  
  onMounted(() => {
    loadAnswers();
  });
  </script>
  
  <style scoped>
  table {
    border-collapse: collapse;
    width: 100%;
  }
  th,
  td {
    text-align: left;
  }
  </style>
  
  <style scoped>
  table {
    border-collapse: collapse;
    width: 100%;
  }
  th,
  td {
    text-align: left;
  }
  </style>
  