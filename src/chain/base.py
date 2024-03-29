# -*- coding: utf-8 -*-
"""
  @Description
  @Author Chris
  @Date 2024/3/5
"""
from operator import itemgetter

from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough, RunnableParallel

from src.model import create_openai_model
from src.prompt import get_rag_prompt, get_condense_question_prompt
from src.util import format_docs
from src.vector import get_dde_retriever


def create_rag_chain(retriever=get_dde_retriever(), prompt=get_rag_prompt(), model=create_openai_model()):
    input_parser = {
        "context": RunnablePassthrough() | retriever | format_docs,
        "question": RunnablePassthrough(),
    }
    output_parser = StrOutputParser()

    chain = (
            input_parser
            | prompt
            | model
            | output_parser
    )

    return chain


def create_condense_question_chain(prompt=get_condense_question_prompt(), model=create_openai_model()):
    input_parser = {
        "history": itemgetter("history"),
        "question": itemgetter("question")
    }
    output_parser = StrOutputParser()

    chain = (
            input_parser
            | prompt
            | model
            | output_parser
    )

    return chain


def create_conversation_rag_chain():
    chain = create_condense_question_chain() | create_rag_chain()

    return chain


def create_rag_chain_with_citation(retriever=get_dde_retriever(), prompt=get_rag_prompt(), model=create_openai_model()):
    input_parser = {
        "context": RunnablePassthrough() | retriever | format_docs,
        "question": RunnablePassthrough(),
    }
    output_parser = StrOutputParser()

    chain = RunnableParallel(input_parser).assign(answer=(
            prompt
            | model
            | output_parser
    ))

    return chain
