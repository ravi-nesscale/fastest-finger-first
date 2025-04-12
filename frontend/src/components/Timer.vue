<template>
  <div class="timer">
    <div class="text-xl font-semibold text-white">
      {{ formattedTime }}
    </div>
  </div>
</template>


  <script setup>
  import { ref, computed, onMounted, onUnmounted } from 'vue';
  
  const startTime = ref(null);
  const elapsed = ref(0);
  let interval = null;
  
  const formattedTime = computed(() => {
    return getFormattedTime();
  });
  
  function getFormattedTime() {
    const totalMs = elapsed.value;
    const minutes = String(Math.floor(totalMs / 60000)).padStart(2, '0');
    const seconds = String(Math.floor((totalMs % 60000) / 1000)).padStart(2, '0');
    const milliseconds = String(Math.floor((totalMs % 1000) / 10)).padStart(2, '0');
    return `${minutes}:${seconds}:${milliseconds}`;
  }
  
  function updateElapsed() {
    if (startTime.value) {
      elapsed.value = Date.now() - startTime.value;
    }
  }
  
  function startInterval() {
    clearInterval(interval);
    interval = setInterval(updateElapsed, 50);
  }
  
  function startTimer() {
    if (!startTime.value) {
      startTime.value = Date.now() - elapsed.value;
      localStorage.setItem('timerStart', startTime.value);
      updateElapsed();
      startInterval();
    }
  }
  
  function pauseTimer() {
    clearInterval(interval);
    if (startTime.value) {
      updateElapsed();
      localStorage.removeItem('timerStart');
      startTime.value = null;
    }
  }
  
  function resetTimer() {
    pauseTimer();
    elapsed.value = 0;
  }
  
  onMounted(() => {
    const savedStart = localStorage.getItem('timerStart');
    if (savedStart) {
      startTime.value = parseInt(savedStart);
    } else {
      startTime.value = Date.now();
      localStorage.setItem('timerStart', startTime.value);
    }
    startInterval();
    updateElapsed();
  });
  
  onUnmounted(() => {
    clearInterval(interval);
  });
  
  // Expose functions for parent component
  defineExpose({
  startTimer,
  pauseTimer,
  resetTimer,
  getFormattedTime: () => formattedTime.value,
});

  </script>
  
<style scoped>
.timer {
  display: flex;
  justify-content: center;
  align-items: center;
  background: #1a1a1a;
  border: 1px solid #c6bc61;
  color: gold;
  padding: 20px;
  border-top-left-radius: 50px;
  border-top-right-radius: 50px;
  /* border-bottom-left-radius: 0;
  border-bottom-right-radius: 0; */
  width: 100px;
  height: 45px;
  margin: 0px auto;
  box-shadow: 0px 3px 20px rgb(201, 198, 36);
  position: relative;
  overflow: hidden;
}

/* Optional: add a subtle gradient glow inside */
/* .timer::before {
  content: "";
  position: absolute;
  top: -50%;
  left: -50%;
  width: 200%;
  height: 200%;
  z-index: 0;
} */


</style>