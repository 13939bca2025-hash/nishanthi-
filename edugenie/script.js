const API = window.location.origin;

const $ = (id) => document.getElementById(id);

async function checkHealth() {
  try {
    const r = await fetch(`${API}/api/health`);
    const data = await r.json();
    $("status").textContent = data.demo_mode ? "Demo Mode" : `AI Ready: ${data.model}`;
  } catch {
    $("status").textContent = "API Offline";
  }
}

$("ask").addEventListener("click", async () => {
  const prompt = $("prompt").value.trim();
  $("error").textContent = "";
  if (!prompt) {
    $("error").textContent = "Please enter a question.";
    return;
  }

  $("ask").disabled = true;
  $("answer").textContent = "EduGenie is thinking...";

  try {
    const r = await fetch(`${API}/api/generate`, {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify({
        task: $("task").value,
        prompt,
        subject: $("subject").value.trim(),
        difficulty: $("difficulty").value
      })
    });
    const data = await r.json();
    if (!r.ok) throw new Error(data.detail || "Request failed.");
    $("answer").textContent = data.answer;
  } catch (e) {
    $("answer").textContent = "";
    $("error").textContent = `Sorry, EduGenie could not complete that request. ${e.message}`;
  } finally {
    $("ask").disabled = false;
  }
});

checkHealth();
