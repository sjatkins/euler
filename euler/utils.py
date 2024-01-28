from math import prod, sqrt, log
from sjautils.math.primes import primes, factor, gcd, lcm
from itertools import product, chain, combinations


def fact(n):
    return prod(i for i in range(1, n + 1))


def num_paths(dimension):
    return fact(2 * dimension) // fact(dimension) ** 2



def take_while(seq, test):
    """
    yields sequence items while test is true. Does not preserve first item that
    fails test in seq.
    :param seq:
    :param test:
    :return:
    """
    for i in seq:
        if test(i):
            yield i
        else:
            break
