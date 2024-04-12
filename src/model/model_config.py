# -*- coding: utf-8 -*-
"""
  @Description
  @Author Chris
  @Date 2024/4/12
"""
from pydantic import BaseModel


class ModelConfig(BaseModel):
    model_name: str
    temperature: float
