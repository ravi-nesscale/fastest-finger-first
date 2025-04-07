<template>
    <button @click="clearStoredAnswers" class="mt-4 mr-1 px-4 py-2 bg-red-500 text-white rounded">
      Clear Stored Answers
    </button>
  </template>
  
  <script setup>
  const clearStoredAnswers = () => {
    if (confirm("Are you sure you want to clear all stored answers?")) {
      localStorage.removeItem("submitted_answers");
      alert("Stored answers cleared!");
    }
  };
  </script>
  