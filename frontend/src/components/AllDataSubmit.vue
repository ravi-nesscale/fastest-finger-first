<template>
  <div class="text-center mt-6">
    <button
      @click="submitAll"
      class="bg-green-600 hover:bg-green-700 text-white px-4 py-2 rounded shadow"
    >
      🚀 Submit All Answers
    </button>
  </div>
</template>

<script setup>
const submitAll = async () => {
  const rawAnswers = JSON.parse(localStorage.getItem("submitted_answers") || "[]");

  if (!rawAnswers.length) {
    alert("❌ No answers found.");
    return;
  }

  // Only pick needed fields
  const questions = rawAnswers.map((a) => ({
    question_name: a.question_name,
    selected_option: a.selected_option,
    time_spent: a.time_spent,
  }));

  const payload = {
    user_id: frappe.session.user, // Email of the user
    questions, // Filtered list of questions
  };

  try {
    const res = await fetch(
      "/api/method/kbc.kbc.api.game_session.submit_game_session",
      {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ data: JSON.stringify(payload) }),
      }
    );

    const result = await res.json();

    if (result.message?.status === "success") {
      alert("✅ Answers submitted!");
      localStorage.removeItem("submitted_answers");
    } else {
      alert("❌ Error: " + (result.message?.message || "Unknown error"));
    }
  } catch (err) {
    console.error("❌ Submission failed", err);
    alert("Something went wrong.");
  }
};
</script>

<style scoped>
button {
  font-weight: bold;
  font-size: 16px;
}
</style>
