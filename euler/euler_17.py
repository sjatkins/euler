from functools import reduce

digits = ['one', 'two', 'three', 'four', 'five',
          'six', 'seven', 'eight', 'nine']
tens = ['twenty', 'thirty', 'forty', 'fifty',
        'sixty', 'seventy', 'eighty', 'ninety']
tens_1 = ['eleven', 'twelve', 'thirteen', 'fourteen',
          'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']

def tensies(t):
    return [t] + [t + d for d in digits]

def tens_values():
    return reduce(lambda a,b: a + b, [tensies(t) for t in tens], [])


up_to_100 = digits + ['ten'] + tens_1 + tens_values()
hundreds = [''] + [d + 'hundred' for d in digits]
def a_hundred(h):
    first = [h] if h else []
    suffix = 'and' if h else ''
    return first + [h + suffix + d for d in up_to_100]
all_1000 = reduce(lambda a,b: a+b, [a_hundred(h) for h in hundreds], []) + ['onethousand']

def solve(n):
    return sum(len(n) for n in all_1000[:n])

def test():
    assert solve(5) == 19
