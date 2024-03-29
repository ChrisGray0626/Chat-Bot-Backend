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
    <context>
    {context}
    </context>
    Question: {input}
    """
    prompt = ChatPromptTemplate.from_template(prompt_template)

    return prompt


def get_condense_question_prompt():
    system_prompt_template = """
    Given the following conversation and a follow up question, rephrase the follow up question to be a standalone question.
    Chat History:
    {history}
    Follow Up Input: {input}
    Standalone question:
    """
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system_prompt_template),
            MessagesPlaceholder(variable_name="history"),
            ("human", "{input}"),
        ]
    )

    return prompt


def create_react_prompt():
    prompt_template = """
    Answer the following questions as best you can. You have access to the following tools:
    
    {tools}
    
    Use the following format:
    
    Question: the input question you must answer
    Thought: you should always think about what to do
    Action: the action to take, should be one of [{tool_names}]
    Action Input: the input to the action, in a JSON format representing the kwargs (e.g. {{"text": "hello world", "num_beams": 5}})
    Observation: the result of the action
    ... (this Thought/Action/Action Input/Observation can repeat N times)
    Thought: I now know the final answer
    Final Answer: the final answer to the original input question
    
    If you don't know the answer, just say that you don't know.
    
    Begin!
    
    Question: {input}
    Thought:{agent_scratchpad}
    """
    prompt = ChatPromptTemplate.from_template(prompt_template)

    return prompt


def create_doc_writing_prompt():
    prompt_template = """
    # Character
    You are an professional Document Writing Assistant. 
    Your expertise lies in creating professional documents that match the user's requirements based on the context.
    # Constraint
    - The needs of the user must be strictly met.
    
    Here is the context:
    {context}
    
    User's writing requirements: {input}
    """

    prompt = ChatPromptTemplate.from_template(prompt_template)

    return prompt


def create_doc_writing_react_prompt():
    system_prompt_template = """
    # Character
    You are an professional Document Writing Assistant. 
    Your expertise lies in creating professional documents that match the user's requirements based on the context.
    # Constraint
    - Adhere to the professional standards and language appropriate to the document's purpose.
    # Tool
    You have access to the following tools:
    {tools}
    # Output Format
    ## To use a tool
    Please use the following format:
    ```
    Thought: you should always think about what to do
    Action: the action to take, should be one of [{tool_names}]
    Action Input: the input to the action
    Observation: the result of the action
    ```
    ... (this Thought/Action/Action Input/Observation can repeat N times)
    ```
    ## To answer the question
    When you have enough information to answer the question without using any more tools, 
    you should respond in the following format:
    ```
    Thought: I now know the final answer
    Final Answer: [your response here]
    ```
    
    Begin!
    
    Here is the user's Requirements: 
    {input}

    {agent_scratchpad}
    """

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system_prompt_template),
            ("human", "{input}"),
        ]
    )
    return prompt


def create_openai_tools_prompt():
    system_prompt_template = """
    # Character
    You are an professional Document Writing Assistant. 
    Your expertise lies in creating professional documents that match the user's requirements based on the context.
    # Constraint
    - The needs of the user must be strictly met. 
    """
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system_prompt_template),
            ("human", "{input}"),
            MessagesPlaceholder("agent_scratchpad"),
        ]
    )

    return prompt


def creat_outline_generation_rag_prompt():
    prompt_template = """
    Use the following pieces of retrieved context to generate the outline based on the document title. 
    <context>
    {context}
    </context>
    Title: {input}
    
    The output format should conform to the markdown format:
    
    # Heading 1
    ## Heading 2
    # Heading 1
    ## Heading 2
    ...
    
    Please do not generate any other content just the outline that includes the title.
    """

    prompt = ChatPromptTemplate.from_template(prompt_template)

    return prompt


def creat_content_generation_rag_prompt():
    prompt_template = """
    Use the following pieces of retrieved context to generate the content based on the heading and its parent headings. 
    <context>
    {context}
    </context>
    Heading: {input} (format: ...Parent Parent Heading > Parent Heading > Heading)

    Please do not generate any other content just the content for this heading.
    """

    prompt = ChatPromptTemplate.from_template(prompt_template)

    return prompt


def creat_outline_generation_prompt():
    prompt_template = """
    Generate the outline based on the document title. 

    Title: {input}

    The output format should conform to the markdown format:

    # Heading 1
    ## Heading 2
    # Heading 1
    ## Heading 2
    ...

    Please do not generate any other content just the outline that includes the title.
    """

    prompt = ChatPromptTemplate.from_template(prompt_template)

    return prompt


def creat_content_generation_prompt():
    prompt_template = """
    Generate the content based on the heading and its parent headings. 

    Heading: {input} (format: ...Parent Parent Heading > Parent Heading > Heading)
    
    Please do not generate any other content just the content.
    """

    prompt = ChatPromptTemplate.from_template(prompt_template)

    return prompt
