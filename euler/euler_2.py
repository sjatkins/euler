from euler.utils import take_while
def fibs():
    a,b = 0,1
    while True:
        yield b
        temp = a + b
        a = b
        b = temp

def even(seq):
    return (i for i in seq if i%2 == 0)

def sum_even_fibs(inclusive_limit):
    even_fibs = even(fibs())
    return sum(take_while(even_fibs, lambda n: n <= inclusive_limit))

def test_euler2():
    should_give = {10:10, 34:44, 60:44, 1000:798, 100000:60696, 4000000:4613732}
    for limit, expected in should_give.items():
        label = f'sum_even_fibs({limit}) should give {expected}'
        assert sum_even_fibs(limit) == expected, label

        