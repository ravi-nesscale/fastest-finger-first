<template>
  <div class="leaderboard-bg">
    <div class="leaderboard-container">
      <h2 class="title">🏆 Leaderboard</h2>
      <table class="leaderboard-table">
        <thead>
          <tr>
            <th>#</th>
            <th>User Name</th>
            <th>Email</th>
            <th>Total Score</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(user, index) in leaderboardData" :key="user.user_id">
            <td>{{ index + 1 }}</td>
            <td>{{ user.user_name }}</td>
            <td>{{ user.user_id }}</td>
            <td>₹ {{ user.total_score.toLocaleString() }}</td>
          </tr>
        </tbody>
      </table>
      <h1 class="text-center text-3xl font-bold mt-3 text-yellow-400 hover:text-yellow-300 transition duration-300">
    <router-link to="/Gamesession">HOME </router-link>
  </h1>
    </div>
  </div>
  
</template>

<script setup>
import { ref } from 'vue';

const leaderboardData = ref([
  {
    user_id: 'ravisoni788@gmail.com',
    user_name: 'Ravi Kumar',
    total_score: 120000,
  },
  {
    user_id: 'neha.sharma@example.com',
    user_name: 'Neha Sharma',
    total_score: 100000,
  },
  {
    user_id: 'arjun.mehra@example.com',
    user_name: 'Arjun Mehra',
    total_score: 80000,
  },
  {
    user_id: 'priya.raj@example.com',
    user_name: 'Priya Raj',
    total_score: 64000,
  },
  {
    user_id: 'aman.verma@example.com',
    user_name: 'Aman Verma',
    total_score: 32000,
  },
]);
</script>

<style scoped>
.leaderboard-bg {
  background: radial-gradient(circle at top, #000066, #000022);
  min-height: 100vh;
  padding: 2rem;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  display: flex;
  justify-content: center;
  align-items: flex-start;
}

.leaderboard-container {
  background: #111244;
  padding: 2rem;
  border-radius: 16px;
  border: 4px solid gold;
  width: 100%;
  max-width: 900px;
  box-shadow: 0 0 40px gold;
  color: white;
  text-align: center;
}

.title {
  margin-bottom: 1.5rem;
  font-size: 2rem;
  color: gold;
  text-shadow: 0 0 10px gold;
}

.leaderboard-table {
  width: 100%;
  border-collapse: collapse;
  color: white;
}

.leaderboard-table th,
.leaderboard-table td {
  border: 1px solid gold;
  padding: 12px 8px;
}

.leaderboard-table thead {
  background-color: #1a1a3f;
}

.leaderboard-table tbody tr:nth-child(even) {
  background-color: #2c2c5a;
}

.leaderboard-table tbody tr:hover {
  background-color: #4444aa;
}
</style>
