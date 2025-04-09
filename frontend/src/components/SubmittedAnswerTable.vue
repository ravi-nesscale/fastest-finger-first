<template>
    <div class="mt-10 container mx-auto p-4">
      <h2 class="text-3xl font-bold mb-6 text-center text-indigo-700">📊 Your Answer Submissions</h2>
  
      <div class="overflow-x-auto bg-white shadow-md rounded-lg">
        <table class="min-w-full table-auto">
          <thead>
            <tr class="bg-indigo-600 text-white">
              <th class="px-6 py-3 text-left text-sm font-medium">#</th>
              <th class="px-6 py-3 text-left text-sm font-medium">Question</th>
              <th class="px-6 py-3 text-left text-sm font-medium">Selected Option</th>
              <th class="px-6 py-3 text-left text-sm font-medium">Correct Answer</th>
              <th class="px-6 py-3 text-left text-sm font-medium">Time Spent</th>
            </tr>
          </thead>
  
          <tbody>
            <tr
              v-for="(answer, index) in submittedAnswers"
              :key="index"
              class="border-b border-gray-300"
            >
              <td class="px-6 py-4 text-sm">{{ index + 1 }}</td>
              <td class="px-6 py-4 text-sm font-medium text-indigo-800">{{ answer.question_name }}</td>
              <td class="px-6 py-4 text-sm">{{ answer.selected_option }}</td>
              <td class="px-6 py-4 text-sm">{{ answer.correct_answer }}</td>
              <td class="px-6 py-4 text-sm">{{ answer.time_spent }}</td>
            </tr>
          </tbody>
        </table>
      </div>
  
      <p v-if="!submittedAnswers.length" class="mt-4 text-center text-gray-500">No answers submitted yet.</p>
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from "vue";
  
  const submittedAnswers = ref([]);
  
  onMounted(() => {
    const data = localStorage.getItem("submitted_answers");
    if (data) {
      submittedAnswers.value = JSON.parse(data);
    }
  });
  </script>
  
  <style scoped>
  .container {
    max-width: 800px;
  }
  
  table {
    width: 100%;
    border-collapse: collapse;
  }
  
  th, td {
    padding: 12px 16px;
    text-align: left;
  }
  
  th {
    background-color: #4f46e5;
    color: white;
  }
  
  tr:nth-child(even) {
    background-color: #f9fafb;
  }
  
  tr:hover {
    background-color: #f3f4f6;
  }
  
  p {
    font-size: 1rem;
    color: #6b7280;
  }
  </style>
  