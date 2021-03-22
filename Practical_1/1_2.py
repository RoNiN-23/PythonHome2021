import math


def f12(x):
    if x < 91:
        return 81 * (x ** 8 + (math.log1p(x))) ** 4 + math.exp(x)

    elif 91 <= x < 175:
        return (math.log1p(((x ** 7) / 83) - x ** 2)) - math.tan(40 * x ** 8)

    elif 175 <= x < 258:
        return 39 * x ** 4 + x ** 3 - x ** 7

    else:
        return 87 * x ** 6 - ((x ** 3) / 77) + 63