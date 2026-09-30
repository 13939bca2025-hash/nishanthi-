from pydantic import BaseModel, Field

class GenerateRequest(BaseModel):
    task: str = Field(default="answer", min_length=1)
    prompt: str = Field(min_length=1)
    subject: str = ""
    difficulty: str = "medium"

class GenerateResponse(BaseModel):
    success: bool
    task: str
    answer: str
