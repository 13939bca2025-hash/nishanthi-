# EduGenie

Google Gemini Powered Learning Assistant.

## Run

1. Open this folder in VS Code.
2. Open Terminal.
3. Run:

```powershell
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

4. Open `.env` and set your Gemini API key:

```env
GEMINI_API_KEY=YOUR_REAL_KEY
GEMINI_MODEL=gemini-3.8-flash
DEMO_MODE=false
```

5. Start the backend from the project root:

```powershell
python -m uvicorn backend.main:app --reload
```

6. Open:

http://127.0.0.1:8000/docs

The frontend is served separately only as static files in this starter. For the easiest browser test, use the API docs. If you want the frontend at `/`, run a static server or mount it in FastAPI.

## Demo mode

For testing without Gemini:

```env
DEMO_MODE=true
```

Restart Uvicorn after changing `.env`.
