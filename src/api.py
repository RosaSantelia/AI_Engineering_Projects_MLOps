from fastapi import FastAPI, Response
from pydantic import BaseModel
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST
from src.inference import SentimentAnalyzer

app = FastAPI(title="Sentiment Analysis API")

analyzer = SentimentAnalyzer()

# Metriche Prometheus
REQUEST_COUNT = Counter("request_count", "Numero di richieste", ["endpoint", "method", "http_status"])
SENTIMENT_DISTRIBUTION = Counter("sentiment_distribution", "Distribuzione sentiment predetto", ["label"])

class TextRequest(BaseModel):
    text: str

class SentimentResponse(BaseModel):
    label: str
    confidence: float

@app.post("/predict", response_model=SentimentResponse)
def predict_sentiment(request: TextRequest):
    label, confidence = analyzer.predict(request.text)
    # Aggiorna metriche
    REQUEST_COUNT.labels(endpoint="/predict", method="POST", http_status="200").inc()
    SENTIMENT_DISTRIBUTION.labels(label=label).inc()
    return SentimentResponse(label=label, confidence=confidence)

@app.get("/metrics")
def metrics():
    data = generate_latest()
    return Response(content=data, media_type=CONTENT_TYPE_LATEST)

