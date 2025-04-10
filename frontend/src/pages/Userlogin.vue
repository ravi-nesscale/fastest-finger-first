<template>
  <div class="form-container">
    <h2>Register Player</h2>

    <input v-model="player_name" placeholder="Full Name" required />
    <input v-model="email" placeholder="Email" type="email" required />
    <input v-model="password" placeholder="Password" type="password" required autocomplete="new-password" />

    <button @click="submitPlayer">Submit</button>

    <p>{{ message }}</p>
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
      message.value = 'Failed to create player'
    }
  } catch (err) {
    console.error(err)
    message.value = 'Something went wrong!'
  }
}
</script>

<style scoped>
.form-container {
  max-width: 400px;
  margin: auto;
  padding: 2rem;
  background: #f0f0f0;
  border-radius: 10px;
}
input {
  display: block;
  margin: 1rem 0;
  padding: 0.5rem;
  width: 100%;
}
button {
  padding: 0.7rem;
  width: 100%;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 8px;
}
</style>
