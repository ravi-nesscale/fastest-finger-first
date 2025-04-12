<template>
  <div class="min-h-screen bg-gradient-to-br from-[#0f2027] via-[#203a43] to-[#2c5364] text-white py-10 px-4 font-['Poppins']">
    <h1 class="text-5xl font-extrabold text-center text-yellow-300 mb-14 animate-slide-in glow-text tracking-wider">
      👑 KBC Leaderboard
    </h1>

    <!-- Top 3 Podium -->
    <div class="flex flex-wrap justify-center items-end gap-6 md:gap-10 mb-14 animate-slide-in">
      <!-- 2nd Place -->
      <div class="flex flex-col items-center space-y-2 w-24 md:w-auto">
        <img src="/media/silver.png" class="w-16 h-16 md:w-20 md:h-20 rounded-full bg-white border-4 border-slate-300 shadow-md" />
        <div class="bg-white/10 px-3 py-0.5 rounded-full text-xs md:text-sm font-semibold text-center truncate w-full">
          🥈 {{ topThree[1]?.player_name || '---' }}
        </div>
        <div class="text-blue-300 text-xs md:text-sm font-semibold">🏅 {{ topThree[1]?.total_points || 0 }}</div>
        <div class="bg-gray-600 w-20 h-20 md:w-28 md:h-28 flex items-center justify-center text-lg md:text-xl font-bold rounded-t-xl podium-glass">2</div>
      </div>

      <!-- 1st Place -->
      <div class="flex flex-col items-center space-y-3 w-28 md:w-auto relative">
        <div class="absolute -top-8 text-3xl md:text-4xl animate-bounce">👑</div>
        <img src="/media/gold.jpg" class="w-20 h-20 md:w-24 md:h-24 rounded-full border-4 border-yellow-400 shadow-2xl animate-pulse" />
        <div class="bg-yellow-300 text-black px-3 py-0.5 rounded-full font-bold text-xs md:text-sm text-center truncate w-full">
          🥇 {{ topThree[0]?.player_name || '---' }}
        </div>
        <div class="text-yellow-100 text-xs md:text-sm font-bold">🏅 {{ topThree[0]?.total_points || 0 }}</div>
        <div class="bg-yellow-500 w-24 h-28 md:w-32 md:h-36 flex items-center justify-center text-2xl md:text-3xl font-extrabold rounded-t-xl podium-glass">1</div>
      </div>

      <!-- 3rd Place -->
      <div class="flex flex-col items-center space-y-2 w-24 md:w-auto">
        <img src="/media/bronze.jpg" class="w-16 h-16 md:w-20 md:h-20 rounded-full border-4 border-orange-400 shadow-md" />
        <div class="bg-orange-400 text-black px-3 py-0.5 rounded-full text-xs md:text-sm font-semibold text-center truncate w-full">
          🥉 {{ topThree[2]?.player_name || '---' }}
        </div>
        <div class="text-orange-200 text-xs md:text-sm font-semibold">🏅 {{ topThree[2]?.total_points || 0 }}</div>
        <div class="bg-gray-700 w-20 h-20 md:w-24 md:h-24 flex items-center justify-center text-lg md:text-xl font-bold rounded-t-xl podium-glass">3</div>
      </div>
    </div>

    <!-- Other Players -->
    <div class="max-w-2xl mx-auto space-y-3 px-2 md:px-0">
      <div
        v-for="(player, index) in leaderboard.slice(3)"
        :key="player.player_id"
        class="flex items-center justify-between gap-2 md:gap-4 backdrop-blur-md bg-white/10 hover:bg-white/20 transition-all duration-200 px-3 md:px-4 py-2 md:py-3 rounded-xl shadow-lg"
      >
        <div class="flex items-center gap-2 md:gap-4">
          <span class="text-base md:text-lg font-bold text-gray-300">{{ index + 4 }}</span>
          <span class="text-sm md:text-base font-medium truncate max-w-[140px] md:max-w-none">{{ player.player_name }}</span>
        </div>
        <div class="text-green-300 font-semibold text-sm md:text-base">🏅 {{ player.total_points }}</div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import axios from 'axios'

const leaderboard = ref([])

// Fetch leaderboard from the API
const fetchLeaderboard = async () => {
  try {
    const res = await axios.get('/api/method/kbc.api.leaderboard.get_leaderboard')
    leaderboard.value = res.data.message || []
  } catch (err) {
    console.error('Error fetching leaderboard:', err)
  }
}

// Call the fetchLeaderboard function when the component is mounted
onMounted(() => {
  fetchLeaderboard()
  // Auto-refresh every 10 seconds to get updated leaderboard
  setInterval(fetchLeaderboard, 10000)
})

// Get top 3 players for the podium
const topThree = computed(() => leaderboard.value.slice(0, 3))
</script>

<style scoped>
@keyframes slideIn {
  from {
    opacity: 0;
    transform: translateY(50px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.animate-slide-in {
  animation: slideIn 1s ease-out;
}

.glow-text {
  text-shadow: 0 0 10px #facc15, 0 0 20px #facc15, 0 0 30px #facc15;
}

.podium-glass {
  backdrop-filter: blur(6px);
  background-color: rgba(255, 255, 255, 0.1);
  border-top: 2px solid rgba(255, 255, 255, 0.3);
}
</style>
