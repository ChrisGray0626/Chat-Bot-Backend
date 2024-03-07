# -*- coding: utf-8 -*-
"""
  @Description
  @Author Chris
  @Date 2024/3/7
"""
from langchain.tools.retriever import create_retriever_tool

from src.vector import get_dde_retriever


def create_dde_retriever_tool():
    retriever = get_dde_retriever()
    name = "DDE_search"
    description = """
    Search for information about DDE. For any questions about DDE, you must use this tool!
    """
    retriever_tool = create_retriever_tool(
        retriever=retriever,
        name=name,
        description=description,
    )

    return retriever_tool
