#!/bin/bash

IMAGE_TAG=0.4
# Change to the root directory
cd ..
# Build the image
docker build -t chat-bot-backend:latest .
# Tag the image
docker tag chat-bot-backend:latest chat-bot-backend:${IMAGE_TAG}