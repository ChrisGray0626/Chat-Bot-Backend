# -*- coding: utf-8 -*-
"""
  @Description
  @Author Chris
  @Date 2024/3/5
"""
import logging
from operator import itemgetter

from dotenv import load_dotenv
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.runnables import RunnableParallel, RunnablePassthrough

from src.bot import ChatBot
from src.chain import create_rag_chain, create_condense_question_chain, create_rag_chain_with_citation

logging.basicConfig(level=logging.INFO)


def runnable_parallel_test():
    runnable = RunnableParallel(
        passed=RunnablePassthrough(),
        extra=RunnablePassthrough.assign(chat_history=itemgetter("num")),
        modified=itemgetter("num")
    )

    answer = runnable.invoke({"num": 1})
    print(answer)


def rag_test():
    chain = create_rag_chain()
    question = "请问什么是 DDE Platform"
    response = chain.invoke(question)
    print(response)


def condense_question_test():
    chain = create_condense_question_chain()
    chat_history = ChatMessageHistory()
    chat_history.add_user_message("请问什么是 DDE Platform")
    chat_history.add_ai_message("DDE Platform 是一个大平台")
    question = "请问它的全称是什么"
    response = chain.invoke(
        {
            "chat_history": chat_history,
            "question": question
        }
    )
    print(response)


def condense_question_rag_test():
    load_dotenv()
    chat_history = ChatMessageHistory()
    chat_history.add_user_message("请问什么是 DDE Platform")
    chat_history.add_ai_message(
        "DDE Platform是一个集成了DDE Knowledge组和DDE Data组产品的平台，通过引擎整合了统一数据系统和统一模型系统，用于在DeepLake中导入数据中心、模型中心和知识中心。它是一个用于地球科学数据预处理和分析的一站式平台，让研究人员使用各种算法和模型访问和分析现有数据，从而解决地球科学领域的重要问题。同时，它也是一个全球性的电子科学平台，旨在为全球分布的IT基础设施上的地球科学的CPU密集型或IO密集型数据分析实验提供集成的科学研究环境。")
    chat_history.add_user_message("请问它有哪些功能")
    chat_history.add_ai_message(
        "DDE 平台提供数据准备、计算资源发放、API 生命周期管理、访问控制和流控等服务。支持弹性扩容、数据融合、亲属关系分析、数据溯源、数据价值和质量评估、数据归档销毁等功能。此外，它还通过无限的云资源促进了协作科学分析，专注于创新研究工作的数据、模型和计算资源。")
    question = "请问它的使命是什么"

    chain = create_condense_question_chain() | create_rag_chain()
    response = chain.invoke({
        "chat_history": chat_history.messages,
        "question": question
    })
    print(response)


def conversation_bot_test():
    # Create bot
    bot = ChatBot()
    q1 = "请问什么是 DDE Platform"
    q2 = "请问它有哪些功能"
    q3 = "请问它的全称是什么"
    q4 = "请问它的使命是什么"
    qs = [q1, q2, q3, q4]
    for q in qs:
        print(q)
        a = bot.chat(question=q)
        print(a)


def rag_with_citation_test():
    chain = create_rag_chain_with_citation()
    question = "请问什么是 DDE Platform"
    a = chain.invoke(question)
    print(a)


if __name__ == '__main__':
    conversation_bot_test()
    pass
