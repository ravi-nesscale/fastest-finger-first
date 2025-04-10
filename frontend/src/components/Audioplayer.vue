<template>
  <div class="audio-control">
    <audio ref="audio" src="/media/kbc_theme.mp3" hidden></audio>
    <button @click="toggleAudio" :aria-label="isPlaying ? 'Stop background music' : 'Play background music'">
      {{ isPlaying ? '⏸ Stop Music' : '▶️ Play Music' }}
    </button>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref, onMounted, onUnmounted } from "vue";

export default defineComponent({
  name: "AudioPlayer",
  setup() {
    const audio = ref<HTMLAudioElement | null>(null);
    const isPlaying = ref(false);

    const playAudio = async () => {
      try {
        if (!audio.value) return;
        await audio.value.play();
        isPlaying.value = true;
        console.log("Audio playing");
      } catch (err) {
        console.warn("Audio play failed (possibly due to autoplay restrictions):", err);
      }
    };

    const toggleAudio = () => {
      if (!audio.value) return;

      if (isPlaying.value) {
        audio.value.pause();
        isPlaying.value = false;
      } else {
        playAudio();
      }
    };

    const tryAutoPlayOnce = () => {
      if (!isPlaying.value) {
        playAudio();
      }
      window.removeEventListener("click", tryAutoPlayOnce);
    };

    onMounted(() => {
      if (audio.value) {
        audio.value.loop = true;
        audio.value.volume = 0.5;
      }

      // Autoplay fallback — user clicks anywhere
      window.addEventListener("click", tryAutoPlayOnce);
    });

    onUnmounted(() => {
      window.removeEventListener("click", tryAutoPlayOnce);
    });

    return {
      audio,
      isPlaying,
      toggleAudio,
    };
  },
});
</script>

<style scoped>
.audio-control {
  position: absolute;
  top: 20px;
  right: 20px;
  z-index: 1000;
}

.audio-control button {
  padding: 10px 20px;
  font-size: 1rem;
  background-color: #1f1f1f;
  color: gold;
  border: 2px solid gold;
  border-radius: 20px;
  cursor: pointer;
  transition: background 0.3s ease;
}

.audio-control button:hover {
  background-color: gold;
  color: #1f1f1f;
}
</style>
