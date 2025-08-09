#!/bin/bash

# Imposta PYTHONPATH alla root del progetto
export PYTHONPATH=$(pwd)

# Esegui pytest sulla cartella tests
pytest tests/
