#!/bin/bash
set -e

# Usa il token passato come variabile d'ambiente per autenticazione
HF_SPACE_REPO="https://${HF_SPACE_PAT}@huggingface.co/spaces/RosaSantelia/rosa-twitter-sentiment"
TMP_DIR="./hf_space_tmp"

echo "Pulizia cartella temporanea..."
rm -rf $TMP_DIR
mkdir $TMP_DIR

echo "Clono repo HF Space in $TMP_DIR..."
git clone $HF_SPACE_REPO $TMP_DIR

echo "Copio contenuto hf_space/ nel repo temporaneo..."
rsync -av --delete hf_space/ $TMP_DIR/

cd $TMP_DIR

git config user.name "github-actions"
git config user.email "actions@github.com"

git add .

if git diff --quiet && git diff --staged --quiet; then
  echo "Nessuna modifica da pushare"
else
  git commit -m "Aggiornamento automatico da repo principale"
  git push
fi

echo "Fine deploy su HuggingFace Space."
