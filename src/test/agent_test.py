# -*- coding: utf-8 -*-
"""
  @Description
  @Author Chris
  @Date 2024/3/7
"""
from langchain.agents import initialize_agent, AgentType
from langchain_community.tools.human import HumanInputRun

from src.agent import create_dde_agent, create_react_agent_with_tool
from src.tool import create_human_input_run, create_shell


def dde_agent_test():
    agent = create_dde_agent()
    q = "What is the full name of DDE"
    a = agent.invoke({
        "question": q,
    })
    print(a)


def agent_with_human_test():
    tools = [
        create_human_input_run()
    ]
    agent = create_react_agent_with_tool(tools)
    q = "What is the full name of DDE"
    a = agent.invoke({
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
    agent_with_shell_test()
    pass
