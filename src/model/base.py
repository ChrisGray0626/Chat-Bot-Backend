# -*- coding: utf-8 -*-
"""
  @Description
  @Author Chris
  @Date 2024/3/11
"""
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI


def create_gpt_3():
    load_dotenv()
    model = ChatOpenAI()

    return model


def create_gpt_4():
    load_dotenv()
    model = ChatOpenAI(model_name="gpt-4")

    return model
