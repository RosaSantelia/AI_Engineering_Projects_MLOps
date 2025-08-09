import re
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import csv
import os

MODEL_NAME = "cardiffnlp/twitter-roberta-base-sentiment-latest"

# Etichette corrispondenti (ordine importante)
LABELS = ["negative", "neutral", "positive"]

class SentimentAnalyzer:
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
        self.model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)
        self.model.eval()

    @staticmethod
    def preprocess(text: str) -> str:
        # Rimpiazza URL con token "http"
        text = re.sub(r'http\S+', 'http', text)
        # Rimpiazza menzioni @user
        text = re.sub(r'@\w+', '@user', text)
        return text

    def predict(self, text: str):
        text = self.preprocess(text)
        inputs = self.tokenizer(text, return_tensors="pt", truncation=True)
        with torch.no_grad():
            outputs = self.model(**inputs)
        scores = torch.nn.functional.softmax(outputs.logits, dim=1)[0].tolist()
        max_idx = scores.index(max(scores))
        return LABELS[max_idx], scores[max_idx]

def run_inference(input_texts, output_csv="results/predictions.csv"):
    if not os.path.exists("results"):
        os.makedirs("results")

    analyzer = SentimentAnalyzer()
    results = []

    for text in input_texts:
        label, confidence = analyzer.predict(text)
        results.append({"text": text, "label": label, "confidence": confidence})

    # Salva i risultati su CSV
    with open(output_csv, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["text", "label", "confidence"])
        writer.writeheader()
        writer.writerows(results)
    print(f"Inference results saved to {output_csv}")

if __name__ == "__main__":
    sample_texts = [
        "I love this product! It's amazing.",
        "I'm not sure about this service.",
        "This is the worst experience I've ever had.",
        "Check out http://example.com @friend",
    ]
    run_inference(sample_texts)
