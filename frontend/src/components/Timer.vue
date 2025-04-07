<template>
    <div class="flex justify-center items-center mt-[10px]">
      <div class="flex flex-col items-center gap-4 p-4 bg-gray-100 rounded-xl shadow w-72">
        <div class="text-3xl font-semibold text-blue-500">
          {{ formattedTime }}
        </div>
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
  