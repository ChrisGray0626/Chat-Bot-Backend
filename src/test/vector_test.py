# -*- coding: utf-8 -*-
"""
  @Description
  @Author Chris
  @Date 2024/3/7
"""
import chromadb

from src.constant import DATABASE_PATH
from src.vector import vectorize_corpus, create_vector_db, create_dde_vector_db


def similarity_search_test():
    vector_db = create_dde_vector_db()
    result = vector_db.similarity_search_with_score(
        query="full name of DDE",

    )
    for r in result:
        print(r)


def vectorize_test():
    vectorize_corpus()


if __name__ == '__main__':
    similarity_search_test()
    pass
