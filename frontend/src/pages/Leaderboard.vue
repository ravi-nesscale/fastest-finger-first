<!-- <template>
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
</style> -->

<template>
  <div class="min-h-screen bg-gradient-to-br from-gray-900 to-gray-800 text-white py-10 px-4">
    <h1 class="text-4xl font-extrabold text-center text-yellow-400 mb-12 animate-slide-in tracking-wide glow-text">
      🏆 KBC Champions
    </h1>

    <!-- Top 3 Podium -->
    <div class="flex flex-wrap justify-center items-end gap-8 mb-16 animate-slide-in">
      <!-- 2nd Place -->
      <div class="flex flex-col items-center space-y-2">
        <img src="/media/silver.png" class="w-20 h-20 rounded-full border-4 border-gray-300 shadow-md" />
        <div class="bg-gray-700 px-3 py-1 rounded-lg text-white text-sm font-semibold">🥈 {{ topThree[1]?.player_name || '---' }}</div>
        <div class="text-blue-300 text-sm font-semibold">🏅 {{ topThree[1]?.total_points || 0 }}</div>
        <div class="bg-gray-600 w-20 h-28 flex items-center justify-center text-2xl font-bold rounded-t-xl podium">2</div>
      </div>

      <!-- 1st Place -->
      <div class="flex flex-col items-center space-y-2 relative">
        <!-- <div class="confetti"></div> -->
        <img src="/media/gold.jpg" class="w-24 h-24 rounded-full border-4 border-yellow-400 shadow-lg animate-pulse" />
        <div class="bg-yellow-400 text-black px-3 py-1 rounded-lg font-bold">🥇 {{ topThree[0]?.player_name || '---' }}</div>
        <div class="text-yellow-100 text-sm font-bold">🏅 {{ topThree[0]?.total_points || 0 }}</div>
        <div class="bg-yellow-500 w-24 h-36 flex items-center justify-center text-3xl font-extrabold rounded-t-xl podium">1</div>
      </div>

      <!-- 3rd Place -->
      <div class="flex flex-col items-center space-y-2">
        <img src="/media/bronze.jpg" class="w-20 h-20 rounded-full border-4 border-orange-400 shadow-md" />
        <div class="bg-orange-400 text-black px-3 py-1 rounded-lg text-sm font-semibold">🥉 {{ topThree[2]?.player_name || '---' }}</div>
        <div class="text-orange-200 text-sm font-semibold">🏅 {{ topThree[2]?.total_points || 0 }}</div>
        <div class="bg-gray-700 w-20 h-24 flex items-center justify-center text-xl font-bold rounded-t-xl podium">3</div>
      </div>
    </div>

    <!-- Other Players -->
    <div class="max-w-2xl mx-auto space-y-4">
      <div
        v-for="(player, index) in leaderboard.slice(3)"
        :key="player.player_id"
        class="flex items-center justify-between bg-gray-700 px-4 py-3 rounded-lg shadow-md hover:bg-gray-600 transition duration-200"
      >
        <div class="flex items-center gap-3">
          <span class="text-lg font-bold text-gray-400">{{ index + 4 }}</span>
          <span class="font-medium text-white">{{ player.player_name }}</span>
        </div>
        <div class="text-purple-400 font-semibold">🏅 {{ player.total_points }}</div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import axios from 'axios'

const leaderboard = ref([])

const fetchLeaderboard = async () => {
  try {
    const res = await axios.get('/api/method/kbc.api.leaderboard.get_leaderboard')
    leaderboard.value = res.data.message || []
  } catch (err) {
    console.error('Error fetching leaderboard:', err)
  }
}

onMounted(() => {
  fetchLeaderboard()
})

const topThree = computed(() => leaderboard.value.slice(0, 3))
</script>

<style scoped>
@keyframes slideIn {
  from {
    opacity: 0;
    transform: translateY(40px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.animate-slide-in {
  animation: slideIn 0.8s ease-in-out;
}

.podium {
  box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.4);
}

.glow-text {
  text-shadow: 0 0 10px #ffc107, 0 0 20px #ffc107, 0 0 30px #ffd700;
}

.confetti::before {
  content: "🎉";
  font-size: 2rem;
  position: absolute;
  top: -30px;
  animation: bounce 1.2s infinite;
}

@keyframes bounce {
  0%, 100% {
    transform: translateY(0)
  }
  50% {
    transform: translateY(-10px)
  }
}

</style>
