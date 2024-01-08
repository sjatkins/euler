from sjautils.math.primes import Primes, number_from_factors, lcm
from collections import defaultdict
from math import prod

def smallest_multiple(limit):
    return lcm(*list(range(2, limit +1)))


def test():
    assert smallest_multiple(10) == 2520