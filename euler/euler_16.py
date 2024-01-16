def sum_power_digits(p):
    power = 2**p
    return sum(int(c) for c in str(power))

def solve():
    return sum_power_digits(1000)

def test():
    assert sum_power_digits(15) == 26

