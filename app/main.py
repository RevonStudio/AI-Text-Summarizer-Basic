from fastapi import FastAPI
from app.api.endpoints import router
from app.core.config import settings

app = FastAPI(
    title=settings.APP_TITLE,
    version=settings.APP_VERSION
)

app.include_router(router)

@app.get("/")
async def root():
    return {"message": "AI Summarization API is running"}
