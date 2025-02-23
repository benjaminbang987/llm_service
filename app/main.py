from fastapi import FastAPI, HTTPException
from app.config import settings
from app.models import llm
from app.schemas import PredictionRequest, PredictionResponse
from app.monitoring import setup_metrics, track_request
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="Scalable LLM API", version="1.0.0")

@app.on_event("startup")
def startup_event():
    setup_metrics()
    logger.info("API started with monitoring enabled")

@app.post("/predict")
@track_request
async def predict(request: PredictionRequest):
    """Endpoint to serve LLM predictions."""
    if not request.text.strip():  # Manual validation
        raise HTTPException(status_code=422, detail="Text cannot be empty")
    try:
        probs = llm.predict(request.text, max_length=settings.MAX_LENGTH)
        return PredictionResponse(probabilities=probs)
    except Exception as e:
        logger.error(f"Prediction failed: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")

@app.get("/health")
async def health_check():
    return {"status": "healthy"}