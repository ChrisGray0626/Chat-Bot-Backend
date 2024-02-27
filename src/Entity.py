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
    sessionId: str
    messages: list[Message]


if __name__ == '__main__':
    pass
