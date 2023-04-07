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
    aс = (x - (1/2 - np.exp(1))) * 2/ time**2

    lower = aс.mean() - np.sqrt(np.var(ac)) * norm.ppf(1 - alpha / 2) / np.sqrt(len(ac))
    upper = ac.mean() - np.sqrt(np.var(ac)) * norm.ppf(alpha / 2) / np.sqrt(len(ac))

    return (lower, upper)
