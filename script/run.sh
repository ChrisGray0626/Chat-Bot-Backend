#!/bin/bash

# Change to the root directory
cd ..
# Run the server
uvicorn src.api.api:app --host 127.0.0.1 --port 8000 --reload