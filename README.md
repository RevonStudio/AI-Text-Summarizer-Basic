# AI Text Summarization API

A professional, high-performance API for text summarization using Facebook's **BART Large CNN** model.

## Architecture
The project follows a modular structure for scalability and maintainability:
- `app/api`: Route definitions and controllers.
- `app/core`: Global configurations and environment variables.
- `app/models`: Data schemas and validation (Pydantic).
- `app/services`: AI/ML processing logic.

## Requirements
- Python 3.9+
- 2GB+ free disk space (to store the pre-trained model)
- 4GB+ RAM recommended for optimal performance

## Installation & Execution

1. Activate the virtual environment:
   ```powershell
   .\venv\Scripts\activate
   ```

2. Install dependencies:
   ```powershell
   pip install -r requirements.txt
   ```

3. Start the server:
   ```powershell
   python run.py
   ```

The API will be available at `http://localhost:8001`.

## Main Endpoints

### POST `/summarize`
Generates a concise summary of the provided English text.

**Payload:**
```json
{
  "text": "Your long text here...",
  "max_length": 130,
  "min_length": 30
}
```

**Response:**
```json
{
  "summary": "The generated summary text...",
  "original_length": 1024,
  "summary_length": 150,
  "execution_time_seconds": 1.45,
  "model_used": "facebook/bart-large-cnn"
}
```

### GET `/health`
Check the API heartbeat and verify if the model is correctly loaded.

## Documentation
Interactive Swagger UI documentation is available at: `http://localhost:8001/docs`
