from sjautils.math.primes import all_divisors
def proper_divisors(n):
    divisors = {1} | all_divisors(n)
    return divisors - {n}


def d(n):
    return sum(proper_divisors(n))


def amicable_lt(limit):
    res = set()
    for i in range(2, limit):
        d_a = d(i)
        if d_a == i:
            continue
        if d(d_a) == i:
            res |= {i, d_a}
    return res


def solve():
    return sum(amicable_lt(10000))


