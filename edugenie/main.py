from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from .config import FRONTEND_ORIGINS, GEMINI_MODEL, DEMO_MODE
from .schemas import GenerateRequest, GenerateResponse
from .gemini_service import generate_answer, AIServiceError

app = FastAPI(title="EduGenie API", version="1.0.0")

app.mount("/app", StaticFiles(directory="frontend", html=True), name="frontend")\n\napp.add_middleware(
    CORSMiddleware,
    allow_origins=[x.strip() for x in FRONTEND_ORIGINS if x.strip()],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"name": "EduGenie", "status": "running", "model": GEMINI_MODEL, "demo_mode": DEMO_MODE}

@app.get("/api/health")
def health():
    return {"status": "healthy", "demo_mode": DEMO_MODE, "model": GEMINI_MODEL}

@app.post("/api/generate", response_model=GenerateResponse)
def generate(request: GenerateRequest):
    try:
        answer = generate_answer(
            request.task,
            request.prompt,
            request.subject,
            request.difficulty,
        )
        return GenerateResponse(success=True, task=request.task, answer=answer)
    except AIServiceError as exc:
        raise HTTPException(status_code=500, detail=f"AI service error: {exc}") from exc
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"Unexpected server error: {exc}") from exc
