# -*- coding: utf-8 -*-
"""
  @Description
  @Author Chris
  @Date 2024/3/1
"""
import logging

from langchain_community.chat_message_histories import ChatMessageHistory

from src.chain import create_conversation_rag_chain

logging.basicConfig(level=logging.INFO)


class ChatBot:
    def __init__(self, retrieval_chain=create_conversation_rag_chain(), chat_history=ChatMessageHistory()):
        self.retrieval_chain = retrieval_chain
        # Create chat history
        # TODO chat_history 解藕
        self.chat_history = chat_history

    def chat(self, question: str, with_history=True):
        # Add human question
        self.chat_history.add_user_message(question)
        logging.info(f"Human Question: {question}")
        # Handle chat history
        if with_history:
            chat_history = self.get_chat_history()
        else:
            chat_history = []
        # Get answer
        answer = self.retrieval_chain.invoke({
            "chat_history": chat_history,
            "question": question
        })
        # Add answer
        self.chat_history.add_ai_message(answer)
        logging.info(f"AI Answer: {answer}")
        return answer

    def conversation(self):
        while True:
            human_question = input("You: ")
            answer = self.chat(human_question)
            print("Bot:", answer)

    def get_chat_history(self):
        return self.chat_history.messages
