from sjautils.math.primes2 import factor, all_divisors

def triangle_numbers():
    index = 1
    while True:
        yield (index * (index+1)) // 2
        index += 1

def trianglenum_more_than(n_factors):
    for t in triangle_numbers():
        divs = all_divisors(t) | {1}
        if len(divs) > n_factors:
            return t

def test():
    assert trianglenum_more_than(5) == 28