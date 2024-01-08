def sum_of_squares(limit):
    return int(sum([n**2 for n in range(1, limit+1)]))

def square_of_sum(limit):
    return int((limit * (limit + 1)/2) ** 2)

def square_diff(limit):
    return square_of_sum(limit) - sum_of_squares(limit)

def test():
    assert square_diff(10) == 2640