# -*- coding: utf-8 -*-
"""
  @Description
  @Author Chris
  @Date 2024/3/4
"""
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder


def get_qa_prompt():
    return ChatPromptTemplate.from_template(
        """Answer the following question:
        <context>
        {context}
        </context>
        Question: {input}"""
    )


def get_conversation_prompt():
    system_prompt = """
    You are an assistant for question-answering tasks. Use the following pieces of retrieved 
    context to answer the question. If you don't know the answer, just say that you don't know. Use three sentences 
    maximum and keep the answer concise. 
    <context>
    {context}
    </context>
    """

    return ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        MessagesPlaceholder(variable_name="chat_history"),
        ("user", "{input}"),
    ])


def get_rag_prompt():
    prompt_template = """
    Use the following pieces of retrieved context to answer the question. 
    If you don't know the answer, just say that you don't know. 
    Use three sentences maximum and keep the answer concise. 
    
    <context>
    {context}
    </context>
    Question: {question}
    """
    prompt = ChatPromptTemplate.from_template(prompt_template)

    return prompt


def get_condense_question_prompt():
    system_prompt_template = """
    Given the following conversation and a follow up question, rephrase the follow up question to be a standalone question.
    Chat History:
    {chat_history}
    Follow Up Input: {question}
    Standalone question:
    """
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system_prompt_template),
            MessagesPlaceholder(variable_name="chat_history"),
            ("human", "{question}"),
        ]
    )

    return prompt
