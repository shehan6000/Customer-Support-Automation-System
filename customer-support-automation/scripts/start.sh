#!/bin/bash

# Load environment variables
if [ -f .env ]; then
    export $(cat .env | grep -v '^#' | xargs)
fi

# Start the application
uvicorn app.main:app --host 0.0.0.0 --port 8000