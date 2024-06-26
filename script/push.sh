#!/bin/bash

REGISTRY_URL=10.130.11.12:5000
IMAGE_NAME=chat-bot-backend
IMAGE_TAG=0.4

echo "Pushing image ${IMAGE_NAME}:${IMAGE_TAG} to registry ${REGISTRY_URL}..."

# Add the tag to the image
docker tag ${IMAGE_NAME}:${IMAGE_TAG} ${REGISTRY_URL}/${IMAGE_NAME}:${IMAGE_TAG}
docker tag ${IMAGE_NAME}:latest ${REGISTRY_URL}/${IMAGE_NAME}:latest

# Push the image to the registry
docker push ${REGISTRY_URL}/${IMAGE_NAME}:${IMAGE_TAG}
docker push ${REGISTRY_URL}/${IMAGE_NAME}:latest

echo "Pushed successfully!"
