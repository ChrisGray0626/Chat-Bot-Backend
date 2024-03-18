# -*- coding: utf-8 -*-
"""
  @Description
  @Author Chris
  @Date 2024/3/8
"""

from src.tool import create_adder, create_shell


def adder_test():
    tool = create_adder
    print("name: ", tool.name)
    print("description: ", tool.description)
    print("args: ", tool.args)


def shell_test():
    tool = create_shell()
    result = tool.run({"commands": ["ls"]})
    print(result)


if __name__ == '__main__':
    shell_test()
    pass
