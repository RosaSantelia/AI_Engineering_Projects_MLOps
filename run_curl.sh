#!/bin/bash

API_URL="http://127.0.0.1:8001/predict"

# Testo di esempio da inviare
TEXT="I love this product!"

echo "Sending POST request to $API_URL with text: $TEXT"

curl -s -X POST "$API_URL" \
     -H "Content-Type: application/json" \
     -d "{\"text\": \"$TEXT\"}" | jq
