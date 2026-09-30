import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "").strip()
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-3.8-flash").strip()
DEMO_MODE = os.getenv("DEMO_MODE", "false").strip().lower() == "true"
FRONTEND_ORIGINS = os.getenv(
    "FRONTEND_ORIGINS",
    "http://127.0.0.1:8000,http://localhost:8000"
).split(",")
