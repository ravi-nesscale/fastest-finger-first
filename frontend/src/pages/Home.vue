<template>
  <div>
    <!-- Splash Screen -->
    <div v-if="showSplash" class="splash-wrapper">
      <img :src="splashImage" alt="Splash Image" class="splash-image" />
    </div>

    <!-- Register Page -->
    <div v-else class="register-wrapper">
      <div class="form-card">
        <h2 class="form-title">🚀 Join the Game Arena</h2>

        <input v-model.trim="player_name" placeholder="👤 Full Name" />

        <input v-model.trim="email" type="email" placeholder="📧 Email Address" />

        <div class="password-field">
  <input
    :type="showPassword ? 'text' : 'password'"
    v-model="password"
    placeholder="🔒 Password"
    autocomplete="new-password"
    required
  />
  <span class="toggle-btn" @click="showPassword = !showPassword">
    {{ showPassword ? '🙈' : '👁️' }}
  </span>
</div>

        <button :disabled="loading" @click="submitPlayer">
          {{ loading ? '⏳ Registering...' : '✨ Register & Start' }}
        </button>

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
const loading = ref(false)
const showPassword = ref(false)
const showSplash = ref(true)
const splashImage = ref('')
const router = useRouter()

// Splash loader with Promise-based delay
const delay = (ms) => new Promise((resolve) => setTimeout(resolve, ms))

onMounted(async () => {
  const isMobile = window.innerWidth <= 768
  splashImage.value = isMobile
    ? 'https://images.justwatch.com/poster/248781841/s718/kaun-banega-crorepati.%7Bformat%7D'
    : 'https://images.odishatv.in/uploadimage/library/16_9/16_9_0/IMAGE_1638171703.jpg'

  await delay(3500)
  showSplash.value = false
})

const togglePassword = () => {
  showPassword.value = !showPassword.value
}

const submitPlayer = async () => {
  message.value = ''

  if (!player_name.value || !email.value || !password.value) {
    message.value = '⚠️ Please fill all fields!'
    return
  }

  const emailPattern = /\S+@\S+\.\S+/
  if (!emailPattern.test(email.value)) {
    message.value = '⚠️ Enter a valid email address!'
    return
  }

  loading.value = true

  try {
    const res = await axios.post('/api/method/kbc.api.player.create_simple_player', null, {
      params: {
        player_name: player_name.value,
        email: email.value,
        password: password.value,
      },
    })

    if (res.data.message) {
      message.value = res.data.message
      localStorage.setItem('user_id', email.value)
      localStorage.setItem('user_name', player_name.value)
      router.push('/Welcomebutton')
    } else {
      message.value = '❌ Registration failed.'
    }
  } catch (err) {
    console.error(err)
    message.value = err.response?.data?.message || '❌ Something went wrong!'
  } finally {
    loading.value = false
  }
}
</script>

<style scoped>
/* Splash */
.splash-wrapper {
  min-height: 100vh;
  width: 100vw;
  background: #000;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
  position: fixed;
  top: 0;
  left: 0;
  z-index: 9999;
}

.splash-image {
  width: 100vw;
  height: 100vh;
  object-fit: cover;
  animation: zoomIn 3s ease-in-out;
}
.splash-wrapper::after {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0,0,0,0.4);
}

@keyframes zoomIn {
  0% {
    transform: scale(0.8);
    opacity: 0;
  }
  100% {
    transform: scale(1);
    opacity: 1;
  }
}

/* Main Layout */
.register-wrapper {
  min-height: 100vh;
  background: linear-gradient(135deg, #2c3e50, #4ca1af);
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 1.5rem;
}

/* Card */
.form-card {
  background: #f7f9fc;
  padding: 2.5rem;
  border-radius: 20px;
  box-shadow: 0 12px 40px rgba(0, 0, 0, 0.2);
  max-width: 420px;
  width: 100%;
  text-align: center;
  animation: fadeIn 0.8s ease;
}
.form-title {
  font-size: 1.8rem;
  color: #2c3e50;
  margin-bottom: 1.6rem;
  font-weight: bold;
}

/* Inputs */
input {
  width: 100%;
  padding: 14px;
  margin-bottom: 1rem;
  border: 2px solid #dcdfe6;
  border-radius: 16px;
  font-size: 1rem;
  background: #fff;
  transition: 0.3s;
}
input:focus {
  border-color: #4ca1af;
  outline: none;
  box-shadow: 0 0 8px rgba(76, 161, 175, 0.4);
}

/* Password Toggle */
.password-field {
  position: relative;
}

.password-field input {
  width: 100%;
  padding: 14px 44px 14px 14px; /* extra right padding for toggle icon space */
  margin-bottom: 1rem;
  border: 2px solid #dcdfe6;
  border-radius: 16px;
  font-size: 1rem;
  transition: all 0.25s ease;
  background-color: #fff;
}

.password-field input:focus {
  border-color: #4ca1af;
  outline: none;
  box-shadow: 0 0 8px rgba(76, 161, 175, 0.4);
}

.toggle-btn {
  position: absolute;
  right: 14px;
  top: 50%;
  transform: translateY(-50%);
  cursor: pointer;
  font-size: 1.3rem;
  user-select: none;
  color: #4ca1af;
}


/* Button */
button {
  width: 100%;
  padding: 14px;
  background: linear-gradient(135deg, #4ca1af, #2c3e50);
  color: #fff;
  font-weight: bold;
  border: none;
  border-radius: 16px;
  font-size: 1rem;
  cursor: pointer;
  transition: 0.3s;
}
button:hover:enabled {
  transform: scale(1.03);
  box-shadow: 0 8px 20px rgba(76, 161, 175, 0.3);
}
button:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

/* Message */
.message {
  margin-top: 1rem;
  color: #ff5252;
  animation: fadeIn 0.5s ease;
}

/* Fade Transition */
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
.fade-enter-active, .fade-leave-active {
  transition: opacity 0.4s;
}
.fade-enter-from, .fade-leave-to {
  opacity: 0;
}

/* Responsive */
@media (max-width: 480px) {
  .form-card {
    padding: 2rem 1.4rem;
  }
  .form-title {
    font-size: 1.6rem;
  }
  input, button {
    padding: 12px;
    font-size: 0.95rem;
  }
}
</style>
