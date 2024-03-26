# -*- coding: utf-8 -*-
"""
  @Description
  @Author Chris
  @Date 2024/3/14
"""
import logging

from src.agent import create_doc_writer_agent
from src.api.entity import *
from src.chain import *
from src.memory import create_redis_history
from src.util import create_uuid


def find_session(session_id: str):
    history = create_redis_history(session_id)
    messages = [{'role': message.type, 'content': message.content} for message in history.messages]

    session = Session(session_id=session_id, messages=messages)

    return session


def dde_rag_chat(request: ChatRequest):
    logging.info("Chat Request: %s", request)
    session_id = request.session_id
    question = request.question
    if session_id is None or session_id == "":
        session_id = create_uuid()
    history = create_redis_history(session_id)
    history.add_user_message(question)

    chain = create_conversation_rag_chain()
    output = chain.invoke({
        "history": history.messages,
        "question": question
    })
    history.add_ai_message(output)
    response = ChatResponse(session_id=session_id, question=question, answer=output)
    logging.info("Chat Response: %s", response)

    return response


def dde_rag_qa(request: QaRequest):
    logging.info("QA Request: %s", request)
    question = request.question
    chain = create_rag_chain_with_citation()
    output = chain.invoke(question)
    logging.info("output: %s", output)
    response = QAResponse(question=question, answer=output["answer"], citation=output["context"])
    logging.info("QA Response: %s", response)

    return response


def generate_outline(request: OutlineRequest):
    logging.info("Outline Request: %s", request)
    title = request.title
    chain = create_outline_generation_chain()
    outline = chain.invoke(title)
    response = OutlineResponse(outline=outline)
    logging.info("Outline Response: %s", response)

    return response


def generate_doc(request: DocRequest):
    logging.info("Doc Request: %s", request)
    outline = request.outline
    agent = create_doc_writer_agent()
    doc = agent.invoke({"outline": outline})
    response = DocResponse(doc=doc)
    logging.info("Doc Response: %s", response)

    return response
