from sjautils.math.primes import Primes, number_from_factors
from collections import defaultdict
from math import prod

def smallest_multiple(limit):
    factors = defaultdict(int)
    def merge_factors(new_factors):
        for prime, exp in new_factors.items():
            factors[prime] = max(factors[prime], exp)

    for n in range(2, limit+1):
        merge_factors(Primes.factor(n))

    return number_from_factors(factors)

# TODO put in test and comment block