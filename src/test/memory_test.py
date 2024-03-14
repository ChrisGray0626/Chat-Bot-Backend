# -*- coding: utf-8 -*-
"""
  @Description
  @Author Chris
  @Date 2024/3/12
"""
from src.memory import create_redis_history


def redis_test():
    chat_history = create_redis_history(session_id="1")
    # chat_history.add_user_message("hello")
    # chat_history.add_ai_message("hi")

    print(chat_history.messages)


if __name__ == '__main__':
    redis_test()
    pass
