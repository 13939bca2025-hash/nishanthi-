from typing import Literal

from pydantic import BaseModel, Field


TaskType = Literal[
    "answer",
    "explain",
    "summary",
    "notes",
    "quiz",
    "exam",
]


class GenerateRequest(BaseModel):
    """
    Request received from the frontend.
    """

    message: str = Field(
        ...,
        min_length=1,
        max_length=5000,
    )

    task: TaskType = "answer"

    subject: str = Field(
        default="General",
        max_length=100,
    )

    difficulty: Literal[
        "beginner",
        "intermediate",
        "advanced",
    ] = "beginner"


class GenerateResponse(BaseModel):
    """
    Response returned to the frontend.
    """

    success: bool

    task: TaskType

    answer: str