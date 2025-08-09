# AI_Engineering_Projects_MLOps
My AI Engineering Master's Projects - MLOps and Machine Learning Models Deployment

# Sentiment Analysis con FastText e Pipeline MLOps


## Descrizione del Progetto

Questo progetto implementa un sistema di analisi del sentiment sui testi provenienti dai social media utilizzando un modello pre-addestrato FastText (modello `twitter-roberta-base-sentiment-latest` di HuggingFace). La soluzione è integrata in una pipeline CI/CD che automatizza training, testing, deploy e monitoraggio continuo del modello.

L'obiettivo è automatizzare e migliorare il monitoraggio della reputazione online di un'azienda tramite analisi automatica del sentiment, con aggiornamenti e retraining automatici per mantenere alta la qualità delle previsioni.


## Scelte Progettuali

- Modello: utilizzo del modello cardiffnlp/twitter-roberta-base-sentiment-latest per sfruttare la robustezza di un modello RoBERTa fine-tuned su dati Twitter

- Dataset: dataset pubblico test-eval di testi social con etichette sentiment (positivo, neutro, negativo) per training e validazione 

- Architettura software: API REST realizzata con FastAPI per facilità d’integrazione e scalabilità

- Monitoraggio: sistema custom semplice basato su endpoint REST per raccogliere metriche di performance e distribuzione sentiment, con report salvati in JSON

- CI/CD: GitHub Actions per automazione completa (test, valutazione, deploy, monitoraggio)


## Risultati

Il modello è in grado di classificare testi social in sentiment positivo, neutro e negativo con alta accuratezza.
La pipeline automatizzata assicura affidabilità e riproducibilità del processo di training e deploy.
Il sistema di monitoraggio permette di tracciare le performance e la distribuzione dei sentiment nel tempo.


### Link utili

Modello pre-addestrato FastText usato: https://huggingface.co/cardiffnlp/twitter-roberta-base-sentiment-latest

Repository GitHub: https://github.com/RosaSantelia/AI_Engineering_Projects_MLOps
