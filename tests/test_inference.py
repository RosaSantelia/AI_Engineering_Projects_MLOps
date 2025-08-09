from src.inference import SentimentAnalyzer

def test_predict_labels():
    analyzer = SentimentAnalyzer()
    texts = ["I love it!", "It's okay.", "I hate it!"]
    for text in texts:
        label, confidence = analyzer.predict(text)
        assert label in ["positive", "neutral", "negative"]
        assert 0.0 <= confidence <= 1.0
