# -*- coding: utf-8 -*-
"""
  @Description
  @Author Chris
  @Date 2024/3/12
"""
from langchain_community.chat_message_histories import RedisChatMessageHistory

from src.constant import REDIS_URL


def create_redis_chat_history(session_id: str, url=REDIS_URL):
    chat_history = RedisChatMessageHistory(session_id=session_id, url=url)

    return chat_history


if __name__ == '__main__':
    pass
