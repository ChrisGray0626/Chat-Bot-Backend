# -*- coding: utf-8 -*-
"""
  @Description
  @Author Chris
  @Date 2024/3/1
"""


def read_txt(file_path):
    with open(file_path, "r", encoding='utf-8') as f:
        return f.read()


def read_lines_txt(file_path):
    with open(file_path, "r", encoding='utf-8') as f:
        lines = f.readlines()
        return list(map(lambda line: line.strip('\n'), lines))


def format_docs(docs: list):
    return desensitize_docs(docs)


def desensitize_docs(docs: list):
    docs = [doc.page_content for doc in docs]

    return docs
