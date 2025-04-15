<template>
  <div class="min-h-screen flex flex-col md:flex-row bg-gradient-to-br from-[#0f172a] via-[#111827] to-[#0f172a] p-6 text-white gap-6">

    <!-- Control Panel -->
    <div class="backdrop-blur-3xl bg-white/10 border border-white/20 rounded-3xl p-10 shadow-2xl w-full md:max-w-lg text-center flex flex-col gap-8">
      <h1 class="text-5xl font-extrabold drop-shadow tracking-tight">🎛️ Admin Control</h1>

      <div class="text-xl space-y-4">
        <p v-if="questions.length">
          📜 <span class="font-semibold">Current Question:</span>
          <br />
          <span class="block mt-4 text-3xl font-bold text-green-400 animate-fade-in">
            {{ currentQuestionText }}
          </span>
        </p>
        <p v-else class="text-gray-300 animate-pulse">Loading questions...</p>
      </div>

      <div class="flex flex-col gap-4">
        <button @click="nextQuestion" :disabled="!questions.length" class="btn-primary">
          🚀 Next Question
        </button>
      </div>

      <transition>
        <p v-if="statusMessage" class="text-green-400 text-lg animate-fade-in-fast">
          {{ statusMessage }}
        </p>
      </transition>
    </div>

    <!-- Question List -->
    <div class="backdrop-blur-3xl bg-white/10 border border-white/20 rounded-3xl p-8 shadow-2xl w-full md:max-w-sm flex flex-col gap-6">
      <h2 class="text-3xl font-bold mb-2">📋 All Questions</h2>

      <ul class="space-y-3 overflow-y-auto max-h-[75vh] pr-2">
        <li v-for="(q, index) in questions" :key="q.name"
            :class="currentIndex === index ? 'text-green-400 font-bold' : 'text-gray-200'"
            class="text-lg transition duration-300">
          {{ index + 1 }}️⃣ {{ q.question_text }}
        </li>
      </ul>
    </div>

  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'

const questions = ref([])
const currentIndex = ref(0)
const statusMessage = ref('')

const fetchQuestions = async () => {
  const res = await fetch('/api/method/kbc.api.question.get_questions')
  const data = await res.json()
  questions.value = data.message
}

const nextQuestion = async () => {
  const res = await fetch('/api/method/kbc.api.admin_control.next_question', {
    method: 'POST'
  })
  const result = await res.json()

  if (currentIndex.value < questions.value.length - 1) {
    currentIndex.value++
    statusMessage.value = `✅ "${questions.value[currentIndex.value].question_text}" is now live!`
  } else {
    statusMessage.value = '🎉 All questions sent!'
  }

  setTimeout(() => (statusMessage.value = ''), 3000)
}

const currentQuestionText = computed(() => {
  if (!questions.value.length) return 'No questions loaded'
  if (currentIndex.value >= questions.value.length) return '🎉 All questions sent!'
  return questions.value[currentIndex.value].question_text
})

onMounted(fetchQuestions)
</script>

<style scoped>
.btn-primary {
  @apply bg-green-500 text-white px-6 py-3 rounded-xl hover:bg-green-600 shadow-lg text-lg transition duration-300 ease-in-out disabled:opacity-50 disabled:cursor-not-allowed;
}

.animate-fade-in {
  animation: fadeIn 0.6s ease forwards;
}
.animate-fade-in-fast {
  animation: fadeIn 0.3s ease forwards;
}

@keyframes fadeIn {
  0% { opacity: 0; transform: translateY(10px); }
  100% { opacity: 1; transform: translateY(0); }
}
</style>
