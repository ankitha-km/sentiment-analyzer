import os
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, RedirectResponse
from pydantic import BaseModel
from app.predict import predict

# Initialize FastAPI app FIRST
app = FastAPI(
    title="SentimentIQ",
    description="Real-time Sentiment Analysis API with explainable AI",
    version="1.0.0"
)

# Static files
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
@app.get("/")
def root():
    return RedirectResponse(url="/ui")

@app.get("/ui")
def ui():
    return FileResponse(os.path.join(BASE_DIR, "static", "index.html"))

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
        raise HTTPException(status_code=400, detail="Text cannot be empty")
    result = predict(input.text)
    return result