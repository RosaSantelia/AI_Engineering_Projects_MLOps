# AI_Engineering_Projects_MLOps
My AI Engineering Master's Projects - MLOps and Machine Learning Models Deployment

# Sentiment Analysis con FastText e Pipeline MLOps

## Descrizione del Progetto

Questo progetto implementa un sistema di analisi del sentiment sui testi provenienti dai social media utilizzando un modello pre-addestrato FastText (modello `twitter-roberta-base-sentiment-latest` di HuggingFace). La soluzione è integrata in una pipeline CI/CD che automatizza training, testing, deploy e monitoraggio continuo del modello.

L'obiettivo è automatizzare e migliorare il monitoraggio della reputazione online di un'azienda tramite analisi automatica del sentiment, con aggiornamenti e retraining automatici per mantenere alta la qualità delle previsioni.

---

## Struttura del Repository

- `src/`: codice sorgente (modello, API, inferenza, monitoraggio)
- `tests/`: test automatici con pytest
- `monitor/`: script di monitoraggio e reportistica
- `.github/workflows/ci-cd.yml`: pipeline CI/CD GitHub Actions
- `requirements.txt`: dipendenze Python
- `README.md`: documentazione progetto

---

## Come usare

### 1. Setup ambiente

bash
pip install -r requirements.txt

### 2. Eseguire i test automatici

bash
pytest tests/

### 3. Avviare l'API FastAPI

bash
uvicorn src.api:app --host 0.0.0.0 --port 8001 --reload

### 4. Pipeline CI/CD
La pipeline automatizza test, valutazione del modello, deploy e generazione report di monitoraggio.

Viene eseguita automaticamente su push o pull request sul branch main.
