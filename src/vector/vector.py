# -*- coding: utf-8 -*-
"""
  @Description
  @Author Chris
  @Date 2024/3/4
"""
import logging
import os
import threading
from typing import Iterable

import chromadb
from chromadb import Settings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader, Docx2txtLoader, \
    UnstructuredPowerPointLoader, PyPDFLoader
from langchain_community.vectorstores.chroma import Chroma
from langchain_core.documents import Document
from langchain_openai import OpenAIEmbeddings

from src.constant import CORPUS_PATH, DATABASE_PATH

logging.basicConfig(level=logging.INFO)


def get_vector_db(embeddings=OpenAIEmbeddings()):
    return Chroma(
        embedding_function=embeddings,
        persist_directory=DATABASE_PATH,
    )


def get_retriever():
    return get_vector_db().as_retriever()


def load_doc(file_path: str):
    # 提取后缀
    suffix = file_path.split('.')[-1]
    if suffix == 'txt':
        loader = TextLoader(file_path=file_path)
    elif suffix == 'docx' or suffix == 'doc':
        loader = Docx2txtLoader(file_path=file_path)
    elif suffix == 'pptx' or suffix == 'ppt':
        loader = UnstructuredPowerPointLoader(file_path=file_path)
    elif suffix == 'pdf':
        loader = PyPDFLoader(file_path=file_path)
    else:
        raise ValueError(f"Unsupported file type: {suffix}")
    doc = loader.load()
    return doc


def split_doc(doc: Iterable[Document]):
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    docs = splitter.split_documents(doc)
    return docs


def preprocess_doc(file_path: str, docs: list):
    logging.info(f"Preprocessing {file_path}")
    doc = load_doc(file_path)
    docs.extend(split_doc(doc))
    logging.info(f"Preprocessed {file_path}")


def preprocess_corpus(corpus_path=CORPUS_PATH):
    docs = []
    threads = []
    # Parallel preprocess documents
    # TODO 线程池
    for filename in os.listdir(corpus_path):
        file_path = corpus_path + filename
        thread = threading.Thread(target=preprocess_doc, args=(file_path, docs))
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()
    return docs


def vectorize_corpus():
    # Load documents
    docs = preprocess_corpus()
    # Vectorize documents
    logging.info("Vectorizing corpus")
    Chroma.from_documents(
        documents=docs,
        embedding=OpenAIEmbeddings(),
        persist_directory=DATABASE_PATH,
    )
    logging.info("Vectorized corpus")


if __name__ == '__main__':
    vectorize_corpus()
    pass
