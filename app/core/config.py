from pydantic_settings import BaseSettings
from pydantic import field_validator

class Settings(BaseSettings):
    APP_TITLE: str = "AI Text Summarization API"
    APP_VERSION: str = "1.0.0"

    MODEL_NAME: str = "facebook/bart-large-cnn"
    MODEL_MAX_LENGTH: int = 1024

    DEFAULT_MAX_SUMMARY: int = 130
    DEFAULT_MIN_SUMMARY: int = 30

    NUM_BEAMS: int = 4
    LENGTH_PENALTY: float = 2.0

    @field_validator("DEFAULT_MIN_SUMMARY")
    @classmethod
    def validate_summary_lengths(cls, v, info):
        max_len = info.data.get("DEFAULT_MAX_SUMMARY")
        if max_len and v >= max_len:
            raise ValueError("DEFAULT_MIN_SUMMARY must be smaller than DEFAULT_MAX_SUMMARY")
        return v

    class Config:
        case_sensitive = True
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()