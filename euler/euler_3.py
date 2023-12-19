from sjautils.math.primes import Primes

def largest_prime_factor(n:int):
    return max(Primes.factor(n).keys())

def test_euler3():
    expected = {2:2, 3:3, 5:5, 7:7, 8:2, 13195:29, 600851475143: 6857}
    for num, result in expected.items():
        label = f'largest_prime_factor({num}) should be {result}'
        assert largest_prime_factor(num) == result, label
