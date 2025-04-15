<template>
  <div class="welcome-screen" :class="{ 'fade-out': redirecting }">
    <div class="content" v-if="!countdownStarted">
      <img
        src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi7fbeKHIBbJhyphenhyphen6hs1Dr-QkK5p2qfta2u6dFjVpQR-cdOmxyje8Ye8Vbko8H3aIg5Jkwf67WLuffkS7rAwfxKI5q4rBQ59J0NDBmZ4y8hXTmYaTaa3ObnC9Uq0iU-wEwfMCRoMqQvkm9rU/s320/mfVLlTy5REeHIswugf0KFp6iuS3i3nrA7flUvXhkCBT.png"
        alt="KBC Logo"
        class="logo"
      />
      <h2 class="player-name">Welcome, {{ userName }}!</h2>
      <h1 class="title">🎉 Get Ready for the KBC Quiz 🎉</h1>
      <button @click="startCountdown" class="start-button">Start Game</button>
    </div>

    <div v-else class="countdown-wrapper">
      <div class="countdown-circle">
        <svg viewBox="0 0 100 100">
          <circle cx="50" cy="50" r="45" class="bg" />
          <circle
            cx="50"
            cy="50"
            r="45"
            class="progress"
            :stroke-dashoffset="dashOffset"
          />
          <text x="50" y="65" text-anchor="middle" class="countdown-text">
            {{ Math.ceil(timeLeft) }}
          </text>
        </svg>
        <p class="getting-ready">Get Ready...</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const userName = ref('Player')
const countdownStarted = ref(false)
const timeLeft = ref(3)
const dashOffset = ref(0)
const redirecting = ref(false)

onMounted(() => {
  const name = localStorage.getItem('user_name')
  userName.value = name || 'Player'
})

const startCountdown = () => {
  const beepSound = new Audio('/media/kbc_beep.mp3')
  beepSound.play()

  countdownStarted.value = true
  const duration = 3000 // 👈 Countdown duration: 3 seconds
  const startTime = performance.now()

  const update = (now) => {
    const elapsed = now - startTime
    const progress = Math.min(elapsed / duration, 1)
    timeLeft.value = 3 - progress * 3
    dashOffset.value = 2 * Math.PI * 45 * progress

    if (progress < 1) {
      requestAnimationFrame(update)
    } else {
      redirecting.value = true
      setTimeout(() => {
        router.push('/Gamesession')
      }, 800)
    }
  }

  requestAnimationFrame(update)
}
</script>

<style scoped>
.welcome-screen {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  height: 100vh;
  background: radial-gradient(circle at center, #0b0f30, #000000);
  color: white;
  font-family: 'Segoe UI', sans-serif;
  text-align: center;
  transition: opacity 0.8s ease-in-out;
  padding: 1rem;
}

.fade-out {
  opacity: 0;
}

.content {
  display: flex;
  flex-direction: column;
  align-items: center;
  animation: fadeIn 1s ease-in-out;
}

.logo {
  width: 260px;
  margin-bottom: 2rem;
  animation: glowPulse 2s infinite ease-in-out;
}

.player-name {
  font-size: 2.2rem;
  margin-bottom: 1rem;
  color: #ffd700;
  font-weight: bold;
}

.title {
  font-size: 2.4rem;
  margin-bottom: 2rem;
  color: #ffffff;
  text-shadow: 2px 2px 12px #00f7ff;
}

.start-button {
  padding: 1rem 2.5rem;
  font-size: 1.5rem;
  background: #ffd700;
  color: black;
  border: none;
  border-radius: 15px;
  cursor: pointer;
  transition: all 0.3s ease-in-out;
  box-shadow: 0 0 15px rgba(255, 215, 0, 0.6);
}
.start-button:hover {
  background: #ffa500;
  transform: scale(1.08);
}

.countdown-wrapper {
  display: flex;
  flex-direction: column;
  align-items: center;
  animation: fadeIn 0.5s ease-in-out;
}

.countdown-circle {
  width: 220px;
  height: 220px;
  position: relative;
}

svg {
  width: 100%;
  height: 100%;
  transform: rotate(-90deg);
}

circle {
  fill: none;
  stroke-width: 10;
  stroke-linecap: round;
}

.bg {
  stroke: #222;
}

.progress {
  stroke: #00f7ff;
  stroke-dasharray: 282.6;
  stroke-dashoffset: 0;
  transition: stroke-dashoffset 0.1s linear;
}

.countdown-text {
  fill: #ffd700;
  font-size: 2.5rem;
  font-weight: bold;
  transform: rotate(90deg);
  transform-origin: center;
}

.getting-ready {
  margin-top: 1rem;
  font-size: 1.5rem;
  color: #ffffff;
}

/* Animations */
@keyframes fadeIn {
  from {
    opacity: 0;
    transform: scale(0.95);
  }
  to {
    opacity: 1;
    transform: scale(1);
  }
}

@keyframes glowPulse {
  0% {
    filter: drop-shadow(0 0 5px #00f7ff);
  }
  50% {
    filter: drop-shadow(0 0 15px #00f7ff);
  }
  100% {
    filter: drop-shadow(0 0 5px #00f7ff);
  }
}
/* Mobile Responsive Adjustments */
@media (max-width: 768px) {
  .logo {
    width: 180px;
    margin-bottom: 1.5rem;
  }

  .player-name {
    font-size: 1.8rem;
    margin-bottom: 0.8rem;
  }

  .title {
    font-size: 2rem;
    margin-bottom: 1.5rem;
  }

  .start-button {
    padding: 0.8rem 2rem;
    font-size: 1.3rem;
    border-radius: 12px;
  }

  .countdown-circle {
    width: 160px;
    height: 160px;
  }

  .countdown-text {
    font-size: 2rem;
  }

  .getting-ready {
    font-size: 1.2rem;
  }
}

@media (max-width: 480px) {
  .logo {
    width: 140px;
  }

  .player-name {
    font-size: 1.5rem;
  }

  .title {
    font-size: 1.6rem;
  }

  .start-button {
    padding: 0.7rem 1.8rem;
    font-size: 1.1rem;
  }

  .countdown-circle {
    width: 140px;
    height: 140px;
  }

  .countdown-text {
    font-size: 1.8rem;
  }

  .getting-ready {
    font-size: 1rem;
  }
}

</style>
