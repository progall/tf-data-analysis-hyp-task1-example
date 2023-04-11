import pandas as pd
import numpy as np

from scipy.stats import pareto, cauchy, norm, ttest_ind, ks_2samp, mannwhitneyu, permutation_test

chat_id = 322172960 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    #return ttest_ind(x_success/x_cnt, y_success/y_cnt, equal_var=False, alternative="greater").pvalue < 0.04 # Ваш ответ, True или False
    return mannwhitneyu(x_success/x_cnt, y_success/y_cnt, alternative="greater").pvalue > 0.04 # Ваш ответ, True или False
