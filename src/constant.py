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
# Database
DATABASE_PATH = os.getenv("DATABASE_PATH", ROOT_PATH + "database/")
# Corpus
CORPUS_PATH = os.getenv("CORPUS_PATH", DATA_PATH + "corpus/")
# Redis
REDIS_URL = os.getenv("REDIS_URL")
# Server
HOST = os.getenv("HOST")
PORT = int(os.getenv("PORT"))
