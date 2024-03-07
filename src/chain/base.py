# -*- coding: utf-8 -*-
"""
  @Description
  @Author Chris
  @Date 2024/3/5
"""
from operator import itemgetter

from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI

from src.prompt import get_rag_prompt, get_condense_question_prompt
from src.vector import get_dde_retriever


def get_rag_chain(retriever=get_dde_retriever(), prompt=get_rag_prompt(), model=ChatOpenAI()):
    input_parser = {
        "context": RunnablePassthrough() | retriever,
        "question": RunnablePassthrough()
    }
    output_parser = StrOutputParser()

    chain = (
            input_parser |
            prompt |
            model |
            output_parser
    )

    return chain


def get_condense_question_chain(prompt=get_condense_question_prompt(), model=ChatOpenAI()):
    input_parser = {
        "chat_history": itemgetter("chat_history"),
        "question": itemgetter("question")
    }
    output_parser = StrOutputParser()

    chain = (
            input_parser |
            prompt |
            model |
            output_parser
    )

    return chain


def get_conversation_rag_chain():
    chain = get_condense_question_chain() | get_rag_chain()

    return chain
