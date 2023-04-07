import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 891686040 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 1 - p
    time = 8
    a = (x - (1/2 - np.exp(1)))*2 / time**2

    lower = a.mean() - np.sqrt(np.var(a)) * norm.ppf(1 - alpha / 2) / np.sqrt(len(a))
    upper = a.mean() - np.sqrt(np.var(a)) * norm.ppf(    alpha / 2) / np.sqrt(len(a))

    return (lower, upper)
