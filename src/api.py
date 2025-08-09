from fastapi import FastAPI
from pydantic import BaseModel
from src.inference import SentimentAnalyzer
from collections import defaultdict
import threading

app = FastAPI(title="Sentiment Analysis API")

analyzer = SentimentAnalyzer()

# Variabili di monitoraggio thread-safe
lock = threading.Lock()
total_requests = 0
sentiment_counts = defaultdict(int)
confidence_sums = defaultdict(float)

class TextRequest(BaseModel):
    text: str

class SentimentResponse(BaseModel):
    label: str
    confidence: float

@app.post("/predict", response_model=SentimentResponse)
def predict_sentiment(request: TextRequest):
    global total_requests, sentiment_counts, confidence_sums
    label, confidence = analyzer.predict(request.text)

    with lock:
        total_requests += 1
        sentiment_counts[label] += 1
        confidence_sums[label] += confidence

    return SentimentResponse(label=label, confidence=confidence)

@app.get("/monitoring")
def get_monitoring():
    with lock:
        avg_confidence = {
            label: (confidence_sums[label] / sentiment_counts[label]) if sentiment_counts[label] > 0 else 0
            for label in sentiment_counts
        }
        return {
            "total_requests": total_requests,
            "sentiment_counts": dict(sentiment_counts),
            "average_confidence_per_label": avg_confidence
        }




