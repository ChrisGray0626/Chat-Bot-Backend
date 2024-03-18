# -*- coding: utf-8 -*-
"""
  @Description
  @Author Chris
  @Date 2024/3/14
"""
import logging

from langchain_community.utilities.redis import get_client

from src.api.entity import Session, ChatResponse, ChatRequest, QaRequest, QAResponse
from src.chain import create_rag_chain_with_citation, create_conversation_rag_chain
from src.constant import REDIS_URL
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


def dde_rag_qa(qa_request: QaRequest):
    logging.info("QA Request: %s", qa_request)
    question = qa_request.question
    chain = create_rag_chain_with_citation()
    output = chain.invoke(question)
    logging.info("output: %s", output)
    response = QAResponse(question=question, answer=output["answer"], citation=output["context"])
    logging.info("QA Response: %s", response)
    return response
