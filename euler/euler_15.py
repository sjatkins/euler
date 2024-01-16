problem = """
Lattice Paths
[Show HTML problem content]  
Problem 15

Starting in the top left corner of a
grid, and only being able to move to the right and down, there are exactly

routes to the bottom right corner.

How many such routes are there through a
grid?
"""
thoughts = """
For nxn matrix we have to go right n times and down n times. You could look at this
as 2n binary digits with n 0s and n 1s.  But note if we pick one of the values for 
some selection of the n of the 2n slots then the rest are the other binary value. So 
we only care about the number of ways to place one of the binary values.  This is a 
classic n taken n at a time problem.  The number of combinations is n! / (k * (n-k)!)
"""

import math
from itertools import combinations

def fact(n):
    return math.prod(range(1, n+1))

def num_paths(dim):
    return fact(2*dim)/(fact(dim) * fact(dim))

def all_paths(dim):
    base = range(2*dim)
    combos = combinations(base, dim)
    def path(combo):
        res = ['right'] * (2*dim)
        for index in combo:
            res[index] = 'down'
        return res
    return (path(combo) for combo in combos)

def test():
    assert num_paths(6) == len(list(all_paths(6)))
    assert num_paths(2) == 6
