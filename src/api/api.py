# -*- coding: utf-8 -*-
"""
  @Description
  @Author Chris
  @Date 2024/2/27
"""

import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

import src.service as service
from src.api.entity import ChatRequest, QaRequest
from src.bot import ChatBot
from src.chain import create_rag_chain_with_citation
from src.constant import HOST, PORT

app = FastAPI()

# Set all CORS enabled origins
app.add_middleware(
    CORSMiddleware,  # type: ignore
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)

# Load environment variables
load_dotenv()
# Create conversation bot
bot = ChatBot()

qa_chain = create_rag_chain_with_citation()


@app.get("/session/{session_id}")
async def find_session(session_id: str):
    session = service.find_session(session_id)

    return session


@app.post("/dde_rag_chat")
async def dde_rag_chat(request: ChatRequest):
    response = service.dde_rag_chat(request)

    return response


@app.post("/dde_rag_qa")
async def dde_rag_qa(request: QaRequest):
    response = service.dde_rag_qa(request)

    return response


if __name__ == '__main__':
    uvicorn.run(app, host=HOST, port=PORT)
    # uvicorn src.api.api:app --host 127.0.0.1 --port 8000 --reload
