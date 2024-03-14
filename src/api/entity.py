# -*- coding: utf-8 -*-
"""
  @Description
  @Author Chris
  @Date 2024/2/27
"""
from pydantic import BaseModel


class Message(BaseModel):
    content: str
    role: str


class Session(BaseModel):
    session_id: str
    messages: list[Message]


class ChatRequest(BaseModel):
    session_id: str
    question: str


class ChatResponse(BaseModel):
    session_id: str
    question: str
    answer: str


class QaRequest(BaseModel):
    question: str


class QAResponse(BaseModel):
    question: str
    answer: str
