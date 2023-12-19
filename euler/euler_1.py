from functools import reduce, partial
def mults(n):
    i = 0
    while True:
        yield i
        i += n

def while_less(seq, n):
    return (i for i in seq if i < n)

def mults_less(n, limit):
    return while_less(mults(n), limit)

def multi_mults_less(limit, *bases):
    return reduce(lambda a,b: a | set(mults_less(b, limit)), bases, set())

def sum_multiples(limit, *bases):
    return sum(multi_mults_less(limit, *bases))

def sum_3_5(limit):
    return multi_mults_less(limit, 3, 5)

def test_euler1():
    should_give = {49: 543, 1000:233168, 8456:16687353, 19564:89301183}
    for limit, expected in should_give.items():
        label = f'sum_3_5({limit}) should give {expected}'
        assert sum_3_5(limit) == expected, label
