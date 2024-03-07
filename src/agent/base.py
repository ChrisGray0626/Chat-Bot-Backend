# -*- coding: utf-8 -*-
"""
  @Description
  @Author Chris
  @Date 2024/3/7
"""
from langchain.agents import initialize_agent, AgentType, AgentExecutor, create_react_agent
from langchain_openai import ChatOpenAI

from src.prompt import create_react_prompt
from src.tool import create_dde_retriever_tool


def create_dde_agent():
    tools = [
        create_dde_retriever_tool(),
    ]
    model = ChatOpenAI()
    agent = create_react_agent(
        llm=model,
        tools=tools,
        prompt=create_react_prompt(),
    )

    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

    return agent_executor
