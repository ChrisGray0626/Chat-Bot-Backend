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
    {history}
    Follow Up Input: {question}
    Standalone question:
    """
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system_prompt_template),
            MessagesPlaceholder(variable_name="history"),
            ("human", "{question}"),
        ]
    )

    return prompt


def create_react_prompt():
    # TODO optimize the prompt
    prompt_template = """
    Answer the following questions as best you can. You have access to the following tools:
    
    {tools}
    
    Use the following format:
    
    Question: the input question you must answer
    Thought: you should always think about what to do
    Action: the action to take, should be one of [{tool_names}]
    Action Input: the input to the action
    Observation: the result of the action
    ... (this Thought/Action/Action Input/Observation can repeat N times)
    Thought: I now know the final answer
    Final Answer: the final answer to the original input question
    
    If you don't know the answer, just say that you don't know.
    
    Begin!
    
    Question: {question}
    Thought:{agent_scratchpad}
    """
    prompt = ChatPromptTemplate.from_template(prompt_template)

    return prompt
