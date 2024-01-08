from euler.palindrome import largest_palindrome_pair
from sjautils.math.primes import Primes, number_from_factors, has_ndigit_product
from math import prod
"""
Problem 4: Largest palindrome product

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two n-digit numbers.
"""

def largest_palindrome_product(n_digits):
    """
    Note that this produces a palindrom of 2 * n_digits.  Playing about I had suspicion
    that even number of digits palindromes are divisible by 11. Googling, this is so.
    Decided to only look for products that start and end with 9. This is reflected in
    underlying algoritm.

    :param n_digits:
    :return:
    """
    return prod(largest_palindrome_pair(n_digits))

def palindrome_number(num):
    s = str(num)
    l = len(s)
    if not (l % 2):
        mid = l // 2
        return s[:mid] == (s[mid:][::-1])
    return False

def is_ndigit_prod(n, num):
    """returns whether num can be factored into the product of two n digit
    numbers.
    NOTE: 11 is known to be a factor. Might be useful to make n digit
    rumbers from factors including 11, m and check whether num // m is n digits.
    """
    factors = Primes.factor(num)
    assert 11 in factors

    return True

def min_max_digits(n):
    return 10**(n-1), 10**n

def has_n_digits(n, num):
    low, high = min_max_digits(n)
    return low <= num < high

def largest_palindrome_number(n):
    biggest = (10**n-1) ** 2
    smallest = (10**(n-1)) ** 2
    working = biggest - (biggest % 11)
    while working > smallest:
        if palindrome_number(working):
            if has_ndigit_product(n, working):
                return working
        working -= 11


def test_euler_4():
    assert largest_palindrome_number(2) == 9009
    assert largest_palindrome_number(3) == 906609
