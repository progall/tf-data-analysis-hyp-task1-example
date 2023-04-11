import pandas as pd
import numpy as np

from scipy.stats import ttest_ind

chat_id = 322172960 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    pz = ttest_ind(x_success, y_success, equal_var=False, alternative="greater").pvalue
    p = ttest_ind(x_success, y_success, equal_var=False, alternative="greater").pvalue
    return p < 0.04 and p > pz # Ваш ответ, True или False
