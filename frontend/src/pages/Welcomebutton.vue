<template>
  <div class="welcome-screen">
    <div class="content" v-if="!showCountdown">
      <img
        src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi7fbeKHIBbJhyphenhyphen6hs1Dr-QkK5p2qfta2u6dFjVpQR-cdOmxyje8Ye8Vbko8H3aIg5Jkwf67WLuffkS7rAwfxKI5q4rBQ59J0NDBmZ4y8hXTmYaTaa3ObnC9Uq0iU-wEwfMCRoMqQvkm9rU/s320/mfVLlTy5REeHIswugf0KFp6iuS3i3nrA7flUvXhkCBT.png"
        alt="KBC Logo"
        class="logo"
      />
      <h2 class="player-name">Welcome, {{ userName }}!</h2>
      <h1 class="title">🎉 Get Ready for the KBC Quiz 🎉</h1>
      <button @click="startCountdown" class="start-button">Start Game</button>
    </div>

    <div v-else class="countdown">
      <h1 class="count">{{ countdown }}</h1>
      <p class="getting-ready">Get Ready...</p>
    </div>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'
import { ref, onMounted } from 'vue'

const router = useRouter()
const userName = ref('Player')
const countdown = ref(5)
const showCountdown = ref(false)

onMounted(() => {
  const name = localStorage.getItem('user_name')
  userName.value = name || 'Player'
})

const playBeep = () => {
  const beep = new Audio('https://www.soundjay.com/button/beep-07.wav') // any short beep sound
  beep.play()
}

const startCountdown = () => {
  showCountdown.value = true
  const interval = setInterval(() => {
    playBeep()
    countdown.value--
    if (countdown.value <= 0) {
      clearInterval(interval)
      router.push('/Gamesession')
    }
  }, 1000)
}
</script>

<style scoped>
.welcome-screen {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background: linear-gradient(135deg, #1e3c72, #2a5298);
  color: white;
  font-family: 'Segoe UI', sans-serif;
  text-align: center;
}

.content {
  display: flex;
  flex-direction: column;
  align-items: center;
  animation: fadeIn 1s ease-in-out;
}

.logo {
  width: 300px;
  height: auto;
  margin-bottom: 1.5rem;
  animation: scaleIn 0.8s ease-in-out;
}

.player-name {
  font-size: 2rem;
  margin-bottom: 1rem;
  color: #ffdd57;
  font-weight: bold;
}

.title {
  font-size: 2.5rem;
  margin-bottom: 2rem;
  color: gold;
  text-shadow: 2px 2px 8px rgba(0, 0, 0, 0.3);
}

.start-button {
  padding: 1rem 2.5rem;
  font-size: 1.5rem;
  background: gold;
  color: black;
  border: none;
  border-radius: 12px;
  cursor: pointer;
  transition: 0.3s;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
}

.start-button:hover {
  background: orange;
  transform: scale(1.05);
}

.countdown {
  display: flex;
  flex-direction: column;
  align-items: center;
  animation: fadeIn 0.5s ease-in-out;
}

.count {
  font-size: 6rem;
  color: #ffdd57;
  font-weight: bold;
}

.getting-ready {
  font-size: 2rem;
  margin-top: 1rem;
  color: white;
}

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(-20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes scaleIn {
  from {
    transform: scale(0.8);
    opacity: 0;
  }
  to {
    transform: scale(1);
    opacity: 1;
  }
}
</style>
