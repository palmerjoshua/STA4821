from random import random
from math import log, e


class BadCaseNumberException(Exception):
    pass

LAMBDA = 2
A = 0.4
B = 1.7


def case2_Fx(t):
    return 1 - e**(-LAMBDA*t) if t >= 0 else 0

def case1_Fx(t):
    if t < 0:
        return 0
    elif 0 <= t <= 1:
        return t
    else:
        return 1

def case3_Px(t):
    if t < 0.3:
        return 0
    elif 0.3 <= t < 1.3:
        return 0.8
    else:
        return 1

def generate_x(case_number):
    if case_number == 1:
        return random()
    elif case_number == 2:
        return -(1/LAMBDA) * log((1-random()))
    elif case_number == 3:
        return 0.5
    elif case_number == 4:
        if random() < 0.8:
            return 0.3
        else:
            return 1.3
    else:
        raise BadCaseNumberException("Case number should be 1-4. Input: {}".format(case_number))


def main():
    sum1 = sum2 = c = 0
    for i in range(10000):
        x = generate_x(1)
        sum1 += x
        sum2 += x**2
        if A < x <= B:
            c += 1
    moment = sum1/10000
    variance = (sum2/10000) - (sum1/10000)**2
    p_a_x_b = c/10000
    print("{:.5f}    {:.5f}    {:.5f}".format(moment, variance, p_a_x_b))

if __name__ == '__main__':
    main()
