# -*- coding: utf-8 -*-
"""
  @Description
  @Author Chris
  @Date 2024/3/25
"""
import re
from typing import Dict, Any, Union

from src.agent.docwriter.entity import Node
from src.chain import create_content_generation_chain, create_outline_generation_chain


def create_doc_writer_agent():
    return DocWriterAgent()


class DocWriterAgent:
    def __init__(self):
        self.input_keys = ["input"]

    def invoke(self, input_: Dict[str, Any]):
        input_ = self.prep_input(input_)
        if "outline" not in input_:
            outline = self.generate_outline(input_)
        else:
            outline = input_["outline"]
        doc_node = self.markdown2node(outline)
        self.generate_content(doc_node)
        doc = self.node2doc(doc_node)

        return doc

    def prep_input(self, input_: Union[Dict[str, Any], Any]) -> Dict[str, str]:
        if not isinstance(input_, dict):
            input_ = {self.input_keys[0]: input_}
        return input_

    @staticmethod
    def generate_outline(input_: Dict[str, Any]):
        chain = create_outline_generation_chain()
        outline = chain.invoke(input_)

        return outline

    def generate_content(self, doc_node):
        self.execute_node(doc_node, "")

    @staticmethod
    def markdown2node(md_content):
        heading_re = re.compile(r'(#+)\s*(.*)', re.MULTILINE)
        headings = heading_re.findall(md_content)
        root = Node(heading="", level=0)
        cur = root
        for level_hash, heading in headings:
            level = len(level_hash)
            node = Node(heading=heading, level=level)
            if node.level > cur.level:
                cur.add_child(node)
                node.parent = cur
                cur = node
            else:
                while node.level <= cur.level:
                    cur = cur.parent
                cur.add_child(node)
                node.parent = cur
                cur = node
        return root

    @classmethod
    def execute_node(cls, node, input_):
        if node.is_leaf():
            input_ += node.heading
            chain = create_content_generation_chain()
            content = chain.invoke(input_)
            node.content = content
        else:
            for child in node.children:
                cls.execute_node(child, input_ + node.heading + " > ")

        return node

    def node2doc(self, doc_node):
        doc_list = []
        self.build_doc(doc_node, doc_list)
        doc = self.list2str(doc_list)

        return doc

    @classmethod
    def build_doc(cls, node, doc_list):
        hash_level = cls.generate_hash_level(node.level)
        doc_list.append(hash_level + " " + node.heading + "\n")
        if node.is_leaf():
            doc_list.append(node.content + "\n")
        else:
            for child in node.children:
                cls.build_doc(child, doc_list)
        return doc_list

    @staticmethod
    def generate_hash_level(level):
        hash_level = ""
        for _ in range(level):
            hash_level += "#"
        return hash_level

    @staticmethod
    def list2str(doc_list):
        return "".join(doc_list)
