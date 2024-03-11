# -*- coding: utf-8 -*-
"""
  @Description
  @Author Chris
  @Date 2024/3/11
"""
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI


def create_openai_model():
    load_dotenv()
    model = ChatOpenAI()

    return model
