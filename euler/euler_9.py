from itertools import combinations
from math import prod

problem = """
A Pythagorean triplet is a set of three natural numbers, , for which,
a++2 + b**2  = C**2
and a < b < c


There exists exactly one Pythagorean triplet for which
 a + b + c = 1000

Find the product abc 
"""

thoughts = """
can be express as b = a + m, c = a + n so
a**2 + (a+m)**2 = (a+n)**2
2(a**2) + 2am + m2 = a**2 + 2an + n**2
a**2 + 2am + + m2 = 2an + n**2
and we know
3a + n + m = 1000
n = m + b where b > 0
so
3a + 2n + b = 1000

Doesn't look promising. So maybe just make generator for triplets by picking all pairs
and checking sum of squares is an exact square then that they sum to 1000?  Or better to just 
pick triplets first that sum to 1000?  Yeah, that sounds good. We will cap that one high. 
"""

def triplets_sum_to(n):
    limit = n-5
    raw = combinations(range(1, limit+1), 3)
    return (r for r in raw if sum(r) == 1000)

def find_triplet(iter, test):
    for i in iter:
        a, b, c = sorted(i)
        if test(a,b,c):
            return a,b,c

def find_triplet_product(n):
    test = lambda a,b,c: a**2 + b**2 == c**2
    a,b,c = find_triplet(triplets_sum_to(n), test)
    print(a,b,c)
    return a*b*c, (a, b, c)


def test():
    answer, nums = find_triplet_product(1000)
    a,b,c = nums
    assert a**2 + b**2 == c**2
    assert a + b + c == 1000






    
