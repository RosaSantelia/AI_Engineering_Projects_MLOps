import csv
import os
from sklearn.metrics import classification_report
from src.dataset import load_tweet_eval
from src.inference import SentimentAnalyzer

def evaluate_and_save():
    dataset = load_tweet_eval()
    analyzer = SentimentAnalyzer()

    y_true = dataset["test"]["label"]
    y_pred = []
    results = []

    print("Running inference on test set...")
    for text in dataset["test"]["text"]:
        label, confidence = analyzer.predict(text)
        y_pred.append(SentimentAnalyzer.LABELS.index(label))
        results.append({"text": text, "predicted_label": label, "confidence": confidence})

    print("Classification Report:")
    print(classification_report(y_true, y_pred, target_names=SentimentAnalyzer.LABELS))

    # Salva i risultati
    os.makedirs("results", exist_ok=True)
    csv_path = "results/predictions.csv"
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["text", "predicted_label", "confidence"])
        writer.writeheader()
        writer.writerows(results)

    print(f"Predictions saved to {csv_path}")

if __name__ == "__main__":
    evaluate_and_save()
