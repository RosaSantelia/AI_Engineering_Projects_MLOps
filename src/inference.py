from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import csv
import json

MODEL_NAME = "cardiffnlp/twitter-roberta-base-sentiment-latest"

class SentimentAnalyzer:
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
        self.model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)
        self.labels = ['negative', 'neutral', 'positive']

    def predict(self, text):
        inputs = self.tokenizer(text, return_tensors="pt", truncation=True)
        with torch.no_grad():
            outputs = self.model(**inputs)
        scores = outputs.logits.softmax(dim=1).tolist()[0]
        max_idx = scores.index(max(scores))
        return self.labels[max_idx], scores[max_idx]

def run_inference(input_texts, output_csv="results/predictions.csv"):
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
        "This is the worst experience I've ever had."
    ]
    run_inference(sample_texts)
