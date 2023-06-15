import numpy as np


# 오버플로우가 해결되지 않은 소프트맥스 개념 (exp에 의해 너무 큰 값이 나오는데 표현 불가능할 때가 있음)
def softmax0(a):
    exp_a = np.exp(a)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a
    return y


def softmax(a):
    c = np.max(a)
    exp_a = np.exp(a - c)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a

    return y
