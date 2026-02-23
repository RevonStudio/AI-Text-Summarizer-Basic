import torch
import time
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from app.core.config import settings

class SummarizerService:
    def __init__(self):
        self.device = torch.device("cpu")
        self.tokenizer = AutoTokenizer.from_pretrained(
            settings.MODEL_NAME, 
            model_max_length=settings.MODEL_MAX_LENGTH
        )
        self.model = AutoModelForSeq2SeqLM.from_pretrained(settings.MODEL_NAME).to(self.device)

    async def generate_summary(self, text: str, max_length: int, min_length: int):
        start_time = time.time()
        
        inputs = self.tokenizer(
            text, 
            max_length=settings.MODEL_MAX_LENGTH, 
            return_tensors="pt", 
            truncation=True
        ).to(self.device)
        
        summary_ids = self.model.generate(
            inputs["input_ids"],
            num_beams=settings.NUM_BEAMS,
            length_penalty=settings.LENGTH_PENALTY,
            max_length=max_length,
            min_length=min_length,
            early_stopping=True
        )
        
        summary_text = self.tokenizer.decode(summary_ids[0], skip_special_tokens=True)
        execution_time = round(time.time() - start_time, 3)
        
        return {
            "summary": summary_text,
            "original_length": len(text),
            "summary_length": len(summary_text),
            "execution_time_seconds": execution_time,
            "model_used": settings.MODEL_NAME
        }

summarizer_service = SummarizerService()
