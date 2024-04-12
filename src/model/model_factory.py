# -*- coding: utf-8 -*-
"""
  @Description
  @Author Chris
  @Date 2024/4/12
"""
from src.model.base import *
from src.model.model_config import ModelConfig


def create_model(model_name: str, config: ModelConfig = None):
    if model_name == GPT_3:
        model = create_gpt_3()
    elif model_name == GPT_4:
        model = create_gpt_4()
    elif model_name == MOONSHOT:
        model = create_moonshot()
    elif model_name == TONGYI:
        model = create_tongyi()
    else:
        raise ValueError(f"Unsupported model name: {model_name}")
    # Config the model
    if config is not None:
        model.temperature = config.temperature

    return model


DEFAULT_MODEL = create_model(GPT_3)
