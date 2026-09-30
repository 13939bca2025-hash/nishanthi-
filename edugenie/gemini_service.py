from google import genai
from .config import GEMINI_API_KEY, GEMINI_MODEL, DEMO_MODE

class AIServiceError(Exception):
    pass

def _demo_answer(task: str, prompt: str, subject: str, difficulty: str) -> str:
    return (
        "EduGenie Demo Mode\\n\\n"
        f"Task: {task}\\n"
        f"Subject: {subject or 'General'}\\n"
        f"Difficulty: {difficulty}\\n\\n"
        f"Your question: {prompt}\\n\\n"
        "Demo response: This is a sample educational response. "
        "Add a valid Gemini API key and set DEMO_MODE=false to receive "
        "a live Gemini-generated answer."
    )

def generate_answer(task: str, prompt: str, subject: str = "", difficulty: str = "medium") -> str:
    if DEMO_MODE:
        return _demo_answer(task, prompt, subject, difficulty)

    if not GEMINI_API_KEY:
        raise AIServiceError("GEMINI_API_KEY is missing.")

    try:
        client = genai.Client(api_key=GEMINI_API_KEY)
        instruction = f"""
You are EduGenie, an educational AI assistant.
Task: {task}
Subject: {subject or 'General'}
Difficulty: {difficulty}

Student request:
{prompt}

Give a clear, accurate, student-friendly answer.
Use simple language and helpful structure.
"""
        response = client.models.generate_content(
            model=GEMINI_MODEL,
            contents=instruction,
        )
        text = getattr(response, "text", None)
        if not text:
            raise AIServiceError("Gemini returned an empty response.")
        return text.strip()
    except Exception as exc:
        raise AIServiceError(str(exc)) from exc
