<!-- <template>
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
    </div>
  </div>
</template>

<script setup>
import { onMounted, ref } from 'vue';
import { call } from 'frappe-ui';

const leaderboardData = ref([]);

onMounted(async () => {
  const res = await call('kbc.kbc.api.game_session.get_leaderboard');
  leaderboardData.value = res.message || [];
});
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
</style> -->



<!-- 
<template>
  <div class="leaderboard-container">
    <h1 class="leaderboard-title">🏆 KBC Leaderboard</h1>

    <div class="leaderboard-table">
      <div class="leaderboard-header">
        <div>Rank</div>
        <div>Player</div>
        <div>Score</div>
      </div>

      <div
        v-for="(entry, index) in leaderboard"
        :key="index"
        class="leaderboard-row"
      >
        <div>#{{ index + 1 }}</div>
        <div>{{ entry.user_name }}</div>
        <div>{{ entry.score }}</div>
      </div>
    </div>


  </div>
</template>

<script setup>
import { onMounted, ref } from "vue";
import axios from "axios";

const leaderboard = ref([]);

onMounted(async () => {
  try {
    const res = await axios.get("/api/method/kbc.api.leaderboard.get_leaderboard");
    leaderboard.value = res.data.message || [];
  } catch (err) {
    console.error("Failed to load leaderboard", err);
  }
});
</script>

<style scoped>
.leaderboard-container {
  padding: 2rem;
  background: linear-gradient(135deg, #1e3c72, #2a5298);
  min-height: 100vh;
  color: white;
  font-family: 'Segoe UI', sans-serif;
  text-align: center;
}

.leaderboard-title {
  font-size: 2.5rem;
  font-weight: bold;
  margin-bottom: 2rem;
  color: gold;
  text-shadow: 1px 1px 4px black;
}

.leaderboard-table {
  max-width: 600px;
  margin: auto;
  border-radius: 16px;
  background: #ffffff15;
  padding: 1rem;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
}

.leaderboard-header,
.leaderboard-row {
  display: flex;
  justify-content: space-between;
  padding: 0.75rem 1rem;
  font-size: 1.2rem;
}

.leaderboard-header {
  font-weight: bold;
  border-bottom: 2px solid #fff;
}

.leaderboard-row {
  border-bottom: 1px solid #ffffff30;
}

.back-home {
  margin-top: 2rem;
  display: inline-block;
  padding: 10px 20px;
  background: gold;
  color: black;
  border-radius: 10px;
  font-weight: bold;
  text-decoration: none;
  transition: background 0.3s ease;
}

.back-home:hover {
  background: orange;
}
</style>
 -->
 <template>
  <div class="leaderboard-container">
    <h1 class="leaderboard-title">🏆 KBC Champions</h1>

    <div v-if="leaderboard.length === 0" class="text-xl animate-pulse">
      Loading leaderboard...
    </div>

    <div class="leaderboard-table">
      <div class="leaderboard-header">
        <div>Rank</div>
        <div>Player Name</div>
        <div>Points</div>
      </div>

      <transition-group name="fade" tag="div">
        <div
          v-for="(player, index) in leaderboard"
          :key="player.player_id"
          class="leaderboard-row animate-slide-in"
          :class="getRankClass(index)"
        >
          <div>
            <span v-if="index === 0">🥇</span>
            <span v-else-if="index === 1">🥈</span>
            <span v-else-if="index === 2">🥉</span>
            <span v-else>#{{ index + 1 }}</span>
          </div>
          <div>{{ player.player_name }}</div>
          <div>{{ player.total_points }}</div>
        </div>
      </transition-group>
    </div>

    <router-link to="/" class="back-home">← Back to Game</router-link>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const leaderboard = ref([])

const fetchLeaderboard = async () => {
  try {
    const res = await axios.get('/api/method/kbc.api.leaderboard.get_leaderboard')
    leaderboard.value = res.data.message || []
  } catch (error) {
    console.error('Failed to fetch leaderboard:', error)
  }
}

const getRankClass = (index) => {
  const base = 'animate-slide-in'
  if (index === 0) return `${base} delay-200`
  if (index === 1) return `${base} delay-400`
  if (index === 2) return `${base} delay-600`
  return base
}

onMounted(() => {
  fetchLeaderboard()
})
</script>

<style scoped>
.leaderboard-container {
  padding: 2rem;
  background: linear-gradient(135deg, #1e3c72, #2a5298);
  min-height: 100vh;
  color: white;
  font-family: 'Segoe UI', sans-serif;
  text-align: center;
}

.leaderboard-title {
  font-size: 2.5rem;
  font-weight: bold;
  margin-bottom: 2rem;
  color: gold;
  text-shadow: 1px 1px 4px black;
}

.leaderboard-table {
  max-width: 600px;
  margin: auto;
  border-radius: 16px;
  background: #ffffff15;
  padding: 1rem;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
}

.leaderboard-header,
.leaderboard-row {
  display: flex;
  justify-content: space-between;
  padding: 0.75rem 1rem;
  font-size: 1.2rem;
}

.leaderboard-header {
  font-weight: bold;
  border-bottom: 2px solid #fff;
}

.leaderboard-row {
  border-bottom: 1px solid #ffffff30;
}

/* Back Button */
.back-home {
  margin-top: 2rem;
  display: inline-block;
  padding: 10px 20px;
  background: gold;
  color: black;
  border-radius: 10px;
  font-weight: bold;
  text-decoration: none;
  transition: background 0.3s ease;
}

.back-home:hover {
  background: orange;
}

/* Animation (from previous code) */
@keyframes slideIn {
  from { opacity: 0; transform: translateY(30px); }
  to { opacity: 1; transform: translateY(0); }
}
.animate-slide-in {
  animation: slideIn 0.8s ease forwards;
}

.delay-200 { animation-delay: 0.2s; }
.delay-400 { animation-delay: 0.4s; }
.delay-600 { animation-delay: 0.6s; }
</style>
