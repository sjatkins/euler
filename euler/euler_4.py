from palindrome import largest_palindrome_pair
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

def test_euler_4():
    assert largest_palindrome_product(2) == 9009
    assert largest_palindrome_product(3) == 906609
