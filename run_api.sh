#!/bin/bash

PORT=8001

# Controlla se la porta è libera
if lsof -i :$PORT > /dev/null
then
  echo "Port $PORT is in use. Trying to kill the process..."
  PID=$(lsof -ti :$PORT)
  kill $PID
  echo "Process $PID killed."
fi

# Avvia uvicorn
echo "Starting FastAPI server on port $PORT..."
uvicorn src.api:app --reload --port $PORT
