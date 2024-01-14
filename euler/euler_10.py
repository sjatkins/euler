from sjautils.math.primes2 import primes
def sum_up_to(n):
    return sum(primes.satisfying(lambda x: x < n))

def test():
    assert sum_up_to(10) == 17
