from sjautils.math.primes import Primes
from itertools import islice

def nth_prime(n):
    primes = list(islice(Primes(), n))
    return primes[-1]


def test():
    assert nth_prime(6) == 13