# -*- coding: utf-8 -*-
"""
  @Description
  @Author Chris
  @Date 2024/3/7
"""
from typing import Sequence

from langchain.agents import AgentExecutor, create_react_agent
from langchain_core.tools import BaseTool
from langchain_openai import ChatOpenAI

from src.prompt import create_react_prompt
from src.tool import create_dde_search


def create_dde_agent():
    tools = [
        create_dde_search(),
    ]
    model = ChatOpenAI()
    agent = create_react_agent(
        llm=model,
        tools=tools,
        prompt=create_react_prompt(),
    )

    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

    return agent_executor


def create_react_agent_with_tool(tools=Sequence[BaseTool]):
    model = ChatOpenAI()

    agent = create_react_agent(
        llm=model,
        tools=tools,
        prompt=create_react_prompt(),
    )

    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

    return agent_executor
