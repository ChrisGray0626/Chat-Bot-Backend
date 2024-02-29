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


class HumanQuestion(BaseModel):
    session_id: str
    content: str
