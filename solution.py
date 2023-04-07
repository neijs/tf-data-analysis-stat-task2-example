import pandas as pd
import numpy as np

from scipy.stats import gamma


chat_id = 891686040

def solution(p: float, x: np.array) -> tuple:
    alpha = 1 - p
    time = 8
    n = len(x)
    loc = np.sum(x)

    lower = ((loc + gamma.ppf(alpha/2, a=n)) / n - 1/2) * 2 / time ** 2
    upper = ((loc + gamma.ppf(1 - alpha/2, a=n)) / n - 1/2) * 2 / time ** 2

    return (lower, upper)
