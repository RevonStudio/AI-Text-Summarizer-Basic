from typing import Optional
from pydantic import BaseModel, Field

class SummaryRequest(BaseModel):
    text: str = Field(..., min_length=10)
    max_length: Optional[int] = Field(130, ge=10, le=512)
    min_length: Optional[int] = Field(30, ge=5, le=100)

class SummaryResponse(BaseModel):
    summary: str
    original_length: int
    summary_length: int
    execution_time_seconds: float
    model_used: str
