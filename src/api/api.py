# -*- coding: utf-8 -*-
"""
  @Description
  @Author Chris
  @Date 2024/2/27
"""

import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

import src.service as service
from src.api.entity import *
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


@app.post("/outline_generation")
async def generate_outline(request: OutlineRequest):
    response = service.generate_outline(request)

    return response


@app.post("/doc_generation")
async def generate_doc(request: DocRequest):
    response = service.generate_doc(request)

    return response


if __name__ == '__main__':
    uvicorn.run(app, host=HOST, port=PORT)
