# and gate의 퍼센트론 구현
# x1, x2는 0과 1의 값을 대입 가능

import numpy as np


# 일반적인 and 게이트의 개념
def And0(x1, x2):
    w1, w2, theta = 0.5, 0.5, 0.7
    tmp = x1 * w1 + x2 * w2
    if tmp <= theta:
        return 0
    else:
        return 1


# 넘파이 배열이 이용가능한 and gate
def And(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])  # 임의의 값임 조건만 되면 아무거나 가능
    b = -0.7  # 위의 theta로 and 게이트가 동작하는 부분을 편향으로 나타낸 것임
    tmp = np.sum(w * x) + b
    if tmp <= 0:
        return 0
    else:
        return 1


# or gate
def Or(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.3
    tmp = np.sum(x * w) + b
    if tmp <= 0:
        return 0
    else:
        return 1


# Nand gate
def Nand(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])
    b = 0.7
    tmp = np.sum(x * w) + b
    if tmp <= 0:
        return 0
    else:
        return 1


# Xor gate
'''
xor 게이트는 동작, 비동작 두 영역을 그래프로 표현했을때 명확히 나눠지지 않는다.
1차원(선)으로 동작 구분이 가능한 함수를 "선형" 이라고 하고
2차원이상(곡선)으로 동작 구분이 가능한 함수를 "비선형"이라고 한다.
즉 xor 게이트는 비선형 함수, 즉 다층 퍼셉트론이다.
그리고 xor 게이트는 or, nand를 통과하고 각각을 and로 연결한 것으로 표현가능하다.
'''


def Xor(x1, x2):
    w1 = Or(x1, x2)
    w2 = Nand(x1, x2)
    tmp = And(w1, w2)
    return tmp


if __name__ == '__main__':
    print(And(0, 0))
    print(And(1, 0))
    print(And(0, 1))
    print(And(1, 1))
    print('')

    print(Or(0, 0))
    print(Or(1, 0))
    print(Or(0, 1))
    print(Or(1, 1))
    print('')

    print(Nand(0, 0))
    print(Nand(1, 0))
    print(Nand(0, 1))
    print(Nand(1, 1))
    print('')

    print(Xor(0, 0))
    print(Xor(1, 0))
    print(Xor(0, 1))
    print(Xor(1, 1))
