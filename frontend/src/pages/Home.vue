<template>
  <div class="register-wrapper">
    <div class="form-card">
      <h2 class="form-title">🎮 Register to Play</h2>

      <input v-model="player_name" placeholder="Full Name" required />
      <input v-model="email" type="email" placeholder="Email" required />
      <input v-model="password" type="password" placeholder="Password" autocomplete="new-password" required />

      <button @click="submitPlayer">Register</button>

      <p class="message">{{ message }}</p>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'

const player_name = ref('')
const email = ref('')
const password = ref('')
const message = ref('')

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
      player_name.value = ''
      email.value = ''
      password.value = ''
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
.register-wrapper {
  min-height: 100vh;
  background: linear-gradient(135deg, #1f1c2c, #928dab);
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 2rem;
}

.form-card {
  background: #ffffff;
  padding: 2rem;
  border-radius: 16px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.15);
  max-width: 400px;
  width: 100%;
  text-align: center;
}

.form-title {
  margin-bottom: 1.5rem;
  color: #333;
}

input {
  width: 100%;
  padding: 12px;
  margin-bottom: 1rem;
  border: 1px solid #ccc;
  border-radius: 12px;
  font-size: 1rem;
  transition: all 0.2s ease-in-out;
}

input:focus {
  border-color: #007bff;
  outline: none;
  box-shadow: 0 0 5px #007bff50;
}

button {
  width: 100%;
  padding: 12px;
  background-color: #007bff;
  color: white;
  font-weight: bold;
  border: none;
  border-radius: 12px;
  cursor: pointer;
  transition: background 0.3s ease;
}

button:hover {
  background-color: #0056b3;
}

.message {
  margin-top: 1rem;
  color: #333;
  font-weight: 500;
}
</style>
