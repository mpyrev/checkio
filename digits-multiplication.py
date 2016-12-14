from functools import reduce
from operator import mul


def checkio(number):
    return reduce(mul, (int(c) for c in str(number).replace('0', '')), 1)
