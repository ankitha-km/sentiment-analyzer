from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from predict import predict
# Initialize FastAPI app FIRST
app = FastAPI(
    title="SentimentIQ",
    description="Real-time Sentiment Analysis API with explainable AI",
    version="1.0.0"
)

# Mount static files AFTER app is created
# ✅ Correct
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
app.mount("/static", StaticFiles(directory=os.path.join(BASE_DIR, "static")), name="static")
# Request model
class TextInput(BaseModel):
    text: str

# Response model
class PredictionResponse(BaseModel):
    sentiment:     str
    confidence:    float
    probabilities: dict

# Endpoints
@app.get("/ui")
def ui():
    return FileResponse(os.path.join(BASE_DIR, "static", "index.html"))

@app.get("/")
def root():
    return {
        "message": "Welcome to SentimentIQ!",
        "docs":    "Visit /docs to test the API"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy",
        "model":  "TF-IDF + Logistic Regression",
        "classes": ["Positive", "Negative", "Neutral", "Irrelevant"]
    }

@app.post("/predict", response_model=PredictionResponse)
def predict_sentiment(input: TextInput):
    if not input.text.strip():
        raise HTTPException(
            status_code=400,
            detail="Text cannot be empty"
        )
    result = predict(input.text)
    return result

