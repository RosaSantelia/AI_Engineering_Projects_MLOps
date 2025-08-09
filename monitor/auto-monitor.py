import requests
import json
import os
from datetime import datetime

MONITORING_URL = "http://localhost:8001/monitoring"
OUTPUT_DIR = "monitor"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "monitoring_report.json")

def fetch_and_save_monitoring():
    try:
        response = requests.get(MONITORING_URL)
        response.raise_for_status()
        data = response.json()

        timestamp = datetime.utcnow().isoformat()
        report = {
            "timestamp": timestamp,
            "data": data
        }

        # Crea la cartella monitor se non esiste
        os.makedirs(OUTPUT_DIR, exist_ok=True)

        # Stampa a video
        print(f"[{timestamp}] Monitoraggio ricevuto:")
        print(json.dumps(data, indent=4))

        # Salva nel file
        with open(OUTPUT_FILE, "a") as f:
            f.write(json.dumps(report) + "\n")

        print(f"Monitoraggio salvato su {OUTPUT_FILE}")

    except Exception as e:
        print(f"Errore durante fetch monitoring: {e}")

if __name__ == "__main__":
    fetch_and_save_monitoring()
