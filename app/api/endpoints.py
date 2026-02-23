from fastapi import APIRouter, HTTPException
from app.models.schemas import SummaryRequest, SummaryResponse
from app.services.summarizer import summarizer_service
from app.core.config import settings

router = APIRouter()

@router.post("/summarize", response_model=SummaryResponse)
async def summarize(request: SummaryRequest):
    try:
        result = await summarizer_service.generate_summary(
            request.text, 
            request.max_length, 
            request.min_length
        )
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/health")
async def health_check():
    return {
        "status": "healthy", 
        "model": settings.MODEL_NAME, 
        "device": "cpu"
    }
