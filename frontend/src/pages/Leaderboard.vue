<template>
  <div class="min-h-screen bg-gradient-to-br from-[#0a0e1a] via-[#1a1f3a] to-[#2a2f5a] text-white py-10 px-4 font-['Poppins'] relative overflow-hidden">
    <!-- Background elements -->
    <div class="absolute inset-0 overflow-hidden">
      <div class="absolute top-0 left-0 w-40 h-40 bg-blue-500/10 rounded-full filter blur-3xl"></div>
      <div class="absolute bottom-0 right-0 w-60 h-60 bg-purple-500/10 rounded-full filter blur-3xl"></div>
      <div class="absolute top-1/3 right-1/4 w-80 h-80 bg-teal-500/5 rounded-full filter blur-3xl"></div>
    </div>

    <!-- Main content -->
    <div class="relative z-10">
      <h1 class="text-5xl font-extrabold text-center text-yellow-300 mb-14 glow-text tracking-wider animate-title">
        👑 KBC LEADERBOARD
      </h1>

      <!-- Top 3 Podium -->
      <div class="flex flex-wrap justify-center items-end gap-6 md:gap-10 mb-14">
        <!-- 2nd Place -->
        <div class="podium-player-silver flex flex-col items-center space-y-2 w-24 md:w-auto">
          <div class="relative">
            <div class="absolute -inset-2 bg-silver-gradient rounded-full blur-md opacity-70"></div>
            <img src="/media/silver.png" class="relative w-16 h-16 md:w-20 md:h-20 rounded-full bg-white border-4 border-slate-300 shadow-lg z-10" />
          </div>
          <div class="bg-gradient-to-r from-slate-400 to-slate-500 px-3 py-1 rounded-full text-xs md:text-sm font-bold text-center truncate w-full">
            🥈 {{ topThree[1]?.player_name || '---' }}
          </div>
          <div class="text-blue-300 text-xs md:text-sm font-bold flex items-center gap-1">
            <span class="text-blue-100">🏅</span> {{ topThree[1]?.total_points || 0 }}
          </div>
          <div class="bg-gradient-to-b from-slate-500 to-slate-700 w-20 h-20 md:w-28 md:h-28 flex items-center justify-center text-lg md:text-xl font-bold rounded-t-xl podium-glass shadow-lg">
            2
          </div>
        </div>

        <!-- 1st Place -->
        <div class="podium-player-gold flex flex-col items-center space-y-3 w-28 md:w-auto relative">
          <div class="absolute -top-8 text-3xl md:text-4xl animate-bounce">👑</div>
          <div class="relative">
            <div class="absolute -inset-2 bg-gold-gradient rounded-full blur-md opacity-70"></div>
            <img src="/media/gold.jpg" class="relative w-20 h-20 md:w-24 md:h-24 rounded-full border-4 border-yellow-400 shadow-xl z-10 animate-pulse" />
          </div>
          <div class="bg-gradient-to-r from-yellow-300 to-yellow-500 px-3 py-1 rounded-full font-bold text-xs md:text-sm text-center truncate w-full text-black">
            🥇 {{ topThree[0]?.player_name || '---' }}
          </div>
          <div class="text-yellow-100 text-xs md:text-sm font-bold flex items-center gap-1">
            <span class="text-yellow-300">🏅</span> {{ topThree[0]?.total_points || 0 }}
          </div>
          <div class="bg-gradient-to-b from-yellow-500 to-yellow-700 w-24 h-28 md:w-32 md:h-36 flex items-center justify-center text-2xl md:text-3xl font-extrabold rounded-t-xl podium-glass shadow-xl">
            1
          </div>
        </div>

        <!-- 3rd Place -->
        <div class="podium-player-bronze flex flex-col items-center space-y-2 w-24 md:w-auto">
          <div class="relative">
            <div class="absolute -inset-2 bg-bronze-gradient rounded-full blur-md opacity-70"></div>
            <img src="/media/bronze.jpg" class="relative w-16 h-16 md:w-20 md:h-20 rounded-full border-4 border-orange-400 shadow-lg z-10" />
          </div>
          <div class="bg-gradient-to-r from-orange-400 to-orange-500 px-3 py-1 rounded-full text-xs md:text-sm font-bold text-center truncate w-full text-black">
            🥉 {{ topThree[2]?.player_name || '---' }}
          </div>
          <div class="text-orange-200 text-xs md:text-sm font-bold flex items-center gap-1">
            <span class="text-orange-300">🏅</span> {{ topThree[2]?.total_points || 0 }}
          </div>
          <div class="bg-gradient-to-b from-orange-600 to-orange-800 w-20 h-20 md:w-24 md:h-24 flex items-center justify-center text-lg md:text-xl font-bold rounded-t-xl podium-glass shadow-lg">
            3
          </div>
        </div>
      </div>

      <!-- Other Players -->
      <div class="max-w-2xl mx-auto space-y-3 px-2 md:px-0">
        <div
          v-for="(player, index) in leaderboard.slice(3)"
          :key="player.player_id"
          class="leaderboard-item flex items-center justify-between gap-2 md:gap-4 backdrop-blur-md bg-white/5 hover:bg-white/10 transition-all duration-300 px-4 py-3 rounded-xl shadow-lg border border-white/5 hover:border-white/10"
          :style="{ animationDelay: `${(index * 0.1) + 1.8}s` }"
        >
          <div class="flex items-center gap-2 md:gap-4">
            <div class="rank-circle bg-gradient-to-br from-blue-500 to-purple-600 w-8 h-8 flex items-center justify-center rounded-full text-sm font-bold">
              {{ index + 4 }}
            </div>
            <span class="text-sm md:text-base font-medium truncate max-w-[140px] md:max-w-none">{{ player.player_name }}</span>
          </div>
          <div class="text-green-300 font-semibold text-sm md:text-base flex items-center gap-1">
            <span class="text-green-200">🏅</span> {{ player.total_points }}
          </div>
        </div>
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
  setInterval(fetchLeaderboard, 10000)
})

const topThree = computed(() => leaderboard.value.slice(0, 3))
</script>

<style scoped>
@keyframes slideIn {
  from { 
    opacity: 0; 
    transform: translateY(50px) scale(0.9); 
  }
  to { 
    opacity: 1; 
    transform: translateY(0) scale(1); 
  }
}

@keyframes fadeUp {
  from { 
    opacity: 0; 
    transform: translateY(20px); 
    filter: blur(2px);
  }
  to { 
    opacity: 1; 
    transform: translateY(0); 
    filter: blur(0);
  }
}

@keyframes glowPulse {
  0%, 100% { 
    text-shadow: 0 0 10px #facc15, 0 0 20px #facc15, 0 0 30px #facc15; 
  }
  50% { 
    text-shadow: 0 0 20px #fde047, 0 0 30px #fde047, 0 0 40px #fde047; 
  }
}

@keyframes titleEntrance {
  0% {
    opacity: 0;
    transform: translateY(-30px) scale(1.2);
    filter: blur(4px);
  }
  100% {
    opacity: 1;
    transform: translateY(0) scale(1);
    filter: blur(0);
  }
}

.glow-text {
  animation: glowPulse 2s infinite ease-in-out;
}

.animate-title {
  animation: titleEntrance 1s ease-out forwards;
}

.podium-glass {
  backdrop-filter: blur(6px);
  background-color: rgba(255, 255, 255, 0.1);
  border-top: 2px solid rgba(255, 255, 255, 0.3);
  box-shadow: inset 0 10px 20px rgba(255, 255, 255, 0.1);
}

.bg-gold-gradient {
  background: linear-gradient(135deg, rgba(255,215,0,0.8) 0%, rgba(255,255,0,0.8) 100%);
}

.bg-silver-gradient {
  background: linear-gradient(135deg, rgba(192,192,192,0.8) 0%, rgba(230,230,230,0.8) 100%);
}

.bg-bronze-gradient {
  background: linear-gradient(135deg, rgba(205,127,50,0.8) 0%, rgba(210,180,140,0.8) 100%);
}

/* Sequential podium animations */
.podium-player-gold {
  opacity: 0;
  animation: slideIn 0.8s cubic-bezier(0.175, 0.885, 0.32, 1.275) forwards;
  animation-delay: 0.3s;
}
.podium-player-silver {
  opacity: 0;
  animation: slideIn 0.8s cubic-bezier(0.175, 0.885, 0.32, 1.275) forwards;
  animation-delay: 0.6s;
}
.podium-player-bronze {
  opacity: 0;
  animation: slideIn 0.8s cubic-bezier(0.175, 0.885, 0.32, 1.275) forwards;
  animation-delay: 0.9s;
}

/* Leaderboard items animate after podium */
.leaderboard-item {
  opacity: 0;
  animation: fadeUp 0.6s ease-out forwards;
  transform-origin: center;
  transition: all 0.3s ease;
}

.leaderboard-item:hover {
  transform: translateY(-2px);
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
}

.rank-circle {
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2), inset 0 1px 2px rgba(255, 255, 255, 0.3);
}

/* Responsive adjustments */
@media (max-width: 768px) {
  .podium-player-gold {
    animation-delay: 0.2s;
  }
  .podium-player-silver {
    animation-delay: 0.4s;
  }
  .podium-player-bronze {
    animation-delay: 0.6s;
  }
  .leaderboard-item {
    animation-delay: 0.8s !important;
  }
}
</style>