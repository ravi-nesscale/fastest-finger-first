<template>
  <div class="min-h-screen py-10 px-4 bg-gradient-to-br from-[#1f2937] via-[#0f172a] to-[#111827]">
    <div class="p-6 max-w-4xl mx-auto backdrop-blur-xl bg-white/10 rounded-2xl shadow-2xl border border-white/20">
      <h1 class="text-4xl font-bold mb-8 text-center text-white drop-shadow">🎛️ Manage Quiz Questions</h1>

      <!-- Add New Question -->
      <div class="mb-10 bg-white/10 p-6 rounded-xl shadow-lg border border-white/20 backdrop-blur-lg">
        <h2 class="text-2xl font-semibold mb-5 text-white">➕ Add New Question</h2>
        <input v-model="newQuestion.question" placeholder="Enter question" class="input mb-4 w-full" />
        <div class="grid grid-cols-2 md:grid-cols-4 gap-3 mb-4">
          <input v-model="newQuestion.option_1" placeholder="Option 1" class="input" />
          <input v-model="newQuestion.option_2" placeholder="Option 2" class="input" />
          <input v-model="newQuestion.option_3" placeholder="Option 3" class="input" />
          <input v-model="newQuestion.option_4" placeholder="Option 4" class="input" />
        </div>
        <input v-model="newQuestion.correct_option" placeholder="Correct Option (Option 1)" class="input mb-5 w-full" />
        <button @click="addQuestion" class="button-success w-full">➕ Add Question</button>
      </div>

      <!-- Question List -->
      <div>
        <h2 class="text-2xl font-semibold mb-5 text-white">📜 All Questions</h2>
        <div v-if="questions.length === 0" class="text-white text-lg">No questions available yet.</div>

        <div v-for="q in questions" :key="q.name" class="question-card">
          <div>
            <p class="font-semibold text-lg text-white mb-1">{{ q.question_text }}</p>
            <p class="text-sm text-gray-300">Correct Option: {{ q.correct_answer }}</p>
          </div>
          <button @click="deleteQuestion(q.name)" class="button-danger">🗑️ Delete</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { call } from 'frappe-ui'

const questions = ref([])
const newQuestion = ref({
  question: '',
  option_1: '',
  option_2: '',
  option_3: '',
  option_4: '',
  correct_option: '',
})

const fetchQuestions = async () => {
  const res = await call('kbc.api.question.get_questions')
  questions.value = res.message
}

const addQuestion = async () => {
  await call('kbc.api.question.add_question', {
    question_text: newQuestion.value.question,
    option_1: newQuestion.value.option_1,
    option_2: newQuestion.value.option_2,
    option_3: newQuestion.value.option_3,
    option_4: newQuestion.value.option_4,
    correct_answer: newQuestion.value.correct_option,
  })
  await fetchQuestions()
  newQuestion.value = {
    question: '',
    option_1: '',
    option_2: '',
    option_3: '',
    option_4: '',
    correct_option: '',
  }
}

const deleteQuestion = async (questionName) => {
  await call('kbc.api.question.delete_question', { question_name: questionName })
  await fetchQuestions()
}

onMounted(fetchQuestions)
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');

* {
  font-family: 'Poppins', sans-serif;
}

.input {
  @apply border border-white/30 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500 bg-white/10 text-white placeholder-white placeholder-opacity-80 backdrop-blur-lg;
}

button {
  @apply transition duration-200 ease-in-out;
}

.question-card {
  @apply border border-white/20 rounded-xl p-5 mb-4 flex items-center justify-between bg-white/10 backdrop-blur-lg shadow-lg;
}

.button-primary {
  @apply bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700 shadow-lg;
}

.button-danger {
  @apply bg-red-600 text-white px-4 py-2 rounded-lg hover:bg-red-700 shadow-lg;
}

.button-success {
  @apply bg-green-600 text-white px-5 py-3 rounded-lg hover:bg-green-700 shadow-xl text-lg;
}
</style>
