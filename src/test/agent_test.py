# -*- coding: utf-8 -*-
"""
  @Description
  @Author Chris
  @Date 2024/3/7
"""
from src.agent import create_dde_agent


def dde_agent_test():
    agent = create_dde_agent()
    q = "What is the full name of DDE"
    a = agent.invoke({
        "question": q,
    })
    print(a)


if __name__ == '__main__':
    dde_agent_test()
    pass
