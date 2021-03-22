import math


def f14(x):
    if x == 0:
        return 7
    elif x == 1:
        return 9
    else:
        return math.cos(f14(x - 1)) - math.fabs(f14(x - 2))