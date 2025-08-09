from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

MODEL_NAME = "cardiffnlp/twitter-roberta-base-sentiment-latest"

class SentimentAnalyzer:
    LABELS = ["negative", "neutral", "positive"]

    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
        self.model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)
        self.model.eval()

    def predict(self, text: str):
        inputs = self.tokenizer(text, return_tensors="pt", truncation=True, max_length=512)
        with torch.no_grad():
            outputs = self.model(**inputs)
        scores = torch.nn.functional.softmax(outputs.logits, dim=1)[0].tolist()
        max_idx = scores.index(max(scores))
        return self.LABELS[max_idx], scores[max_idx]
