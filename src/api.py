from fastapi import FastAPI
from pydantic import BaseModel
from src.inference import SentimentAnalyzer

app = FastAPI(title="Sentiment Analysis API")

analyzer = SentimentAnalyzer()

class TextRequest(BaseModel):
    text: str

class SentimentResponse(BaseModel):
    label: str
    confidence: float

@app.post("/predict", response_model=SentimentResponse)
def predict_sentiment(request: TextRequest):
    label, confidence = analyzer.predict(request.text)
    return SentimentResponse(label=label, confidence=confidence)
