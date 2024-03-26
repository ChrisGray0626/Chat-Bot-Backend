# -*- coding: utf-8 -*-
"""
  @Description
  @Author Chris
  @Date 2024/3/5
"""
from operator import itemgetter

from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough, RunnableParallel

from src.model import create_gpt_3, create_gpt_4
from src.prompt import *
from src.util import format_docs
from src.vector import create_dde_retriever


def create_rag_chain(retriever=create_dde_retriever(), prompt=get_rag_prompt(), model=create_gpt_3()):
    input_parser = {
        "context": RunnablePassthrough() | retriever | format_docs,
        "input": RunnablePassthrough(),
    }
    output_parser = StrOutputParser()

    chain = (
            input_parser
            | prompt
            | model
            | output_parser
    )

    return chain


def create_qa_chain(prompt=get_qa_prompt(), model=create_gpt_3()):
    input_parser = {
        "input": RunnablePassthrough()
    }
    output_parser = StrOutputParser()

    chain = (
            input_parser
            | prompt
            | model
            | output_parser
    )

    return chain


def create_condense_question_chain(prompt=get_condense_question_prompt(), model=create_gpt_3()):
    input_parser = {
        "history": itemgetter("history"),
        "input": itemgetter("input")
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


def create_rag_chain_with_citation(retriever=create_dde_retriever(), prompt=get_rag_prompt(),
                                   model=create_gpt_3()):
    input_parser = {
        "context": RunnablePassthrough() | retriever | format_docs,
        "input": RunnablePassthrough(),
    }
    output_parser = StrOutputParser()

    chain = RunnableParallel(input_parser).assign(answer=(
            prompt
            | model
            | output_parser
    ))

    return chain


def create_dde_doc_writing_chain():
    retriever = create_dde_retriever()
    prompt = create_doc_writing_prompt()
    model = create_gpt_3()
    chain = create_rag_chain_with_citation(retriever, prompt, model)

    return chain


def create_dde_outline_generation_chain():
    prompt = creat_outline_generation_rag_prompt()
    chain = create_rag_chain(
        prompt=prompt
    )

    return chain


def create_dde_content_generation_chain():
    prompt = creat_content_generation_rag_prompt()
    chain = create_rag_chain(
        prompt=prompt
    )

    return chain


def create_outline_generation_chain():
    model = create_gpt_4()
    prompt = creat_outline_generation_prompt()
    chain = create_qa_chain(
        prompt=prompt,
        model=model,
    )

    return chain


def create_content_generation_chain():
    model = create_gpt_4()
    prompt = creat_content_generation_prompt()
    chain = create_qa_chain(
        prompt=prompt,
        model=model,
    )

    return chain
