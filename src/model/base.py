# -*- coding: utf-8 -*-
"""
  @Description
  @Author Chris
  @Date 2024/3/11
"""
from dotenv import load_dotenv
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_openai import ChatOpenAI
from langchain_community.chat_models.moonshot import MoonshotChat


def create_gpt_3():
    load_dotenv()
    model = ChatOpenAI()

    return model


def create_gpt_4():
    load_dotenv()
    model = ChatOpenAI(model_name="gpt-4")

    return model


def create_moonshot():
    load_dotenv()
    model = MoonshotChat()

    return model


def create_tongyi():
    load_dotenv()
    model = ChatTongyi(model_name="qwen-plus")

    return model


DEFAULT_MODEL = create_gpt_3()
