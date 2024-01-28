from euler.utils import fact
def sum_fact_digits(n):
    digits = [int(d) for d in str(fact(n))]
    return sum(digits)

def solve():
    assert sum_fact_digits(10) == 27
    return sum_fact_digits(100)

solve()