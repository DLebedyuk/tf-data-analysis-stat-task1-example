import pandas as pd
import numpy as np


chat_id = 461920076 # Ваш chat ID, не меняйте название переменной


def solution(x: np.array) -> float:
  t = 10
  a = x / t
  return a.mean() ** 2
