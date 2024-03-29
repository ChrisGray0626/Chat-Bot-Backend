# -*- coding: utf-8 -*-
"""
  @Description
  @Author Chris
  @Date 2024/3/7
"""
from langchain.tools.retriever import create_retriever_tool
from langchain_community.tools.human import HumanInputRun
from langchain_community.tools.shell import ShellTool
from langchain_community.utilities.google_search import GoogleSearchAPIWrapper
from langchain_community.utilities.serpapi import SerpAPIWrapper
from langchain_core.tools import tool, Tool

from src.chain import create_rag_chain
from src.vector import create_dde_retriever


def create_dde_search():
    retriever = create_dde_retriever()
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
def adder(x: int, y: int) -> int:
    """Add x to y. For any questions about the additive calculation, you must use this tool"""
    return x + y


def create_shell():
    tool = ShellTool()
    tool.description = tool.description + f"args {tool.args}".replace("{", "{{").replace("}", "}}")

    return tool


def create_human_input_run():
    tool = HumanInputRun()
    tool.name = "Human-Input-Run"

    return tool


def create_serp_google_search():
    search = SerpAPIWrapper()
    tool = Tool(
        name="Google-Search",
        description="If you do not know the answer, you can try to use it to search the answer online.",
        func=search.run,
    )

    return tool


def create_google_search():
    search = GoogleSearchAPIWrapper()
    tool = Tool(
        name="Google-Search",
        description="If you do not know the answer, you can try to use it to search the answer online.",
        func=search.run,
    )

    return tool


@tool("Outline-Generator")
def outline_generator(doc_title: str) -> str:
    """Generate an outline based on the given doc title"""
    chain = create_rag_chain()
    input_ = "Here is the title: " + doc_title + ". Please generate an outline for this title."
    output = chain.invoke(input_)

    return output


@tool("Document-Writer")
def doc_writer(outline: str, doc_title: str) -> str:
    """Write a document based on the given outline and doc title"""
    chain = create_rag_chain()
    input_ = "Here is the title: " + doc_title + ". Here is the outline: " + outline
    output = chain.invoke(input_)

    return output
