# Chat Bot Backend

## Description

A chatbot backend that provides some services.

## Usage

Here are some ways to use it:

1. From Docker image.
2. From source code.

### From docker image

#### Pull the image

```bash
docker pull {IMAGE_URL}
```

### From source code

#### Clone the repository

```bash
git clone {REPOSITORY_URL}
```

#### Install dependencies

```bash
pip install -r requirements.txt
```

### Prepare Redis

Please install and run Redis server by yourself.

### Prepare LLM

Currently, only `OpenAI` is supported.

Please prepare the `OpenAI API key` by yourself and config it in the following `.env` file.

### Prepare the vector database

If you want to use the RAG model, you need to prepare the vector database.

Currently, only `Chroma` databases is supported.

Here are some ways to use it:

1. From the database file.
2. From the corpus.

#### From the database file

Please config `VECTOR_DATABASE_PATH` in the following `.env` file.

#### From the corpus

Please config `CORPUS_PATH` in the following `.env` file.

Then vectorize the corpus:

```python
from src.vector import vectorize_corpus

vectorize_corpus(corpus_path={CORPUS_PATH})
```

### Prepare `.env` file

Here is the template:

```properties
# OpenAI
OPENAI_API_KEY=
# Corpus
CORPUS_PATH=
# Vector database
VECTOR_DATABASE_PATH=
# Redis
REDIS_URL=
# Server
HOST=
PORT=
```

## Run the server

Here are some ways to run it:

1. From Docker image.
2. From source code.

### From docker image

#### Run Docker Compose

Here is an example of `docker-compose.yaml`:

```yaml
services:
  backend:
    image: chat-bot-backend:latest
    ports:
      - "8000:8000"
    volumes:
      - {VECTOR_DATABASE_PATH}:/app/database
      - {.ENV_PATH}:/app/.env
```

### From source code

#### Run the server

Run `script/run.sh`.
