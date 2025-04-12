<template>
  <div>
    <!-- Splash Screen -->
    <div v-if="showSplash" class="splash-wrapper">
      <img
        src="https://www.editionscomplexe.com/wp-content/uploads/2022/10/Untitled.png"
        alt="Splash Image"
        class="splash-image"
      />
    </div>

    <!-- Register Page -->
    <div v-else class="register-wrapper">
      <div class="form-card">
        <h2 class="form-title">🚀 Join the Game Arena</h2>

        <input v-model="player_name" placeholder="👤 Full Name" required />
        <input v-model="email" type="email" placeholder="📧 Email Address" required />
        <input v-model="password" type="password" placeholder="🔒 Password" autocomplete="new-password" required />

        <button @click="submitPlayer">✨ Register & Start</button>

        <transition name="fade">
          <p v-if="message" class="message">{{ message }}</p>
        </transition>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import axios from 'axios'

const player_name = ref('')
const email = ref('')
const password = ref('')
const message = ref('')
const router = useRouter()

// Splash screen state
const showSplash = ref(true)

// Automatically hide splash screen after 4-5 seconds
onMounted(() => {
  setTimeout(() => {
    showSplash.value = false
  }, 4000) // 4000 ms = 4 seconds
})

const submitPlayer = async () => {
  try {
    const res = await axios.post('/api/method/kbc.api.player.create_simple_player', null, {
      params: {
        player_name: player_name.value,
        email: email.value,
        password: password.value,
      }
    })

    if (res.data.message) {
      message.value = res.data.message
      localStorage.setItem('user_id', email.value)
      localStorage.setItem('user_name', player_name.value)
      router.push('/Welcomebutton')
    } else {
      message.value = '❌ Failed to create player'
    }
  } catch (err) {
    console.error(err)
    message.value = '❌ Something went wrong!'
  }
}
</script>

<style scoped>
/* Splash Screen Style */
.splash-wrapper {
  min-height: 100vh;
  background: #000;
  display: flex;
  align-items: center;
  justify-content: center;
}

.splash-image {
  width: 100%;
  height: auto;
  animation: fadeIn 4s ease-in-out;
}

/* Register Page Style */
.register-wrapper {
  min-height: 100vh;
  background: linear-gradient(135deg, #2c3e50, #4ca1af);
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 2rem;
}

.form-card {
  background: #f7f9fc;
  padding: 2.5rem;
  border-radius: 20px;
  box-shadow: 0 12px 40px rgba(0, 0, 0, 0.2);
  width: 100%;
  max-width: 420px;
  text-align: center;
  animation: fadeIn 1s ease-in;
}

.form-title {
  margin-bottom: 1.8rem;
  font-size: 1.8rem;
  color: #2c3e50;
  font-weight: bold;
}

input {
  width: 100%;
  padding: 14px;
  margin-bottom: 1rem;
  border: 2px solid #dcdfe6;
  border-radius: 16px;
  font-size: 1rem;
  transition: all 0.25s ease;
  background-color: #fff;
}

input:focus {
  border-color: #4ca1af;
  outline: none;
  box-shadow: 0 0 8px rgba(76, 161, 175, 0.4);
}

button {
  width: 100%;
  padding: 14px;
  background: linear-gradient(135deg, #4ca1af, #2c3e50);
  color: white;
  font-weight: bold;
  border: none;
  border-radius: 16px;
  font-size: 1rem;
  cursor: pointer;
  transition: all 0.3s ease;
}

button:hover {
  transform: scale(1.03);
  box-shadow: 0 8px 20px rgba(76, 161, 175, 0.3);
}

.message {
  margin-top: 1rem;
  font-weight: 500;
  color: #ff5252;
  animation: fadeIn 0.5s ease;
}

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(15px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.4s;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>
