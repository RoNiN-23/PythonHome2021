import math


def f13(n, m):
    x = 0
    y = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            x += (81 * j ** 4) + (85 * j ** 5)

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            y += (54 * j ** 8) - math.log1p(i)

    return x - y
