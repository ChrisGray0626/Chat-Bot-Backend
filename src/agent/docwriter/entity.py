# -*- coding: utf-8 -*-
"""
  @Description
  @Author Chris
  @Date 2024/3/25
"""
from __future__ import annotations


class Node:
    def __init__(self, heading: str, level: int):
        self.heading = heading
        self.level = level
        self.content = None
        self.children = []
        self.parent = None

    def add_child(self, node: Node):
        self.children.append(node)

    def is_leaf(self):
        return len(self.children) == 0
