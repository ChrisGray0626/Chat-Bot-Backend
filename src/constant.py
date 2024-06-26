# -*- coding: utf-8 -*-
"""
  @Description
  @Author Chris
  @Date 2024/2/29
"""
import os

from dotenv import load_dotenv

ROOT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/"
DATA_PATH = ROOT_PATH + "data/"
# Load environment variables
load_dotenv()
# Corpus
CORPUS_PATH = os.getenv("CORPUS_PATH", DATA_PATH + "corpus/")
# Vector Database
VECTOR_DATABASE_PATH = os.getenv("VECTOR_DATABASE_PATH", ROOT_PATH + "database/")
# Redis
REDIS_URL = os.getenv("REDIS_URL")
# Server
HOST = os.getenv("HOST")
PORT = int(os.getenv("PORT"))
