# -*- coding: utf-8 -*-
"""
  @Description
  @Author Chris
  @Date 2024/3/7
"""
import asyncio

from src.agent import create_dde_agent, create_react_agent_with_tool
from src.tool import create_human_input_run, create_shell


async def dde_agent_test():
    agent = create_dde_agent()
    q = "What is the full name of DDE"
    a = await agent.ainvoke({
        "question": q,
    })
    print(a)


def agent_with_human_test():
    tools = [
        create_human_input_run()
    ]
    agent = create_react_agent_with_tool(tools)
    q = "What is the full name of DDE"
    a = agent.ainvoke({
        "question": q,
    })
    print(a)


def agent_with_shell_test():
    tools = [
        create_shell()
    ]
    agent = create_react_agent_with_tool(tools)
    q = "Please tell me the list of installed python denpendency and grep for all denpendencies. Return only a sorted list of them. Be sure to use double quotes."

    a = agent.invoke({
        "question": q,
    })
    print(a)


if __name__ == '__main__':
    asyncio.run(dde_agent_test())
    asyncio.run(dde_agent_test())
    pass
