# -*- coding: utf-8 -*-
"""
  @Description
  @Author Chris
  @Date 2024/3/7
"""
from langchain.tools.retriever import create_retriever_tool
from langchain_community.tools.human import HumanInputRun
from langchain_community.tools.shell import ShellTool
from langchain_core.tools import tool

from src.vector import get_dde_retriever

# TODO Web search tool


def create_dde_search():
    retriever = get_dde_retriever()
    name = "DDE-Search"
    description = """
    Search for information about DDE. For any questions about DDE, you must use this tool!
    """
    retriever_tool = create_retriever_tool(
        retriever=retriever,
        name=name,
        description=description,
    )

    return retriever_tool


@tool("Adder")
def create_adder(x: int, y: int) -> int:
    """Add x to y. For any questions about the additive calculation, you must use this tool"""
    return x + y


def create_shell():
    tool = ShellTool()
    tool.description = tool.description + f"args {tool.args}".replace("{", "{{").replace("}", "}}")

    return tool


def create_human_input_run():
    tool = HumanInputRun()
    tool.name = "HumanInputRun"

    return tool
