"Longest Collatz Sequence"

def collatz(start):
    res = [start]
    while start != 1:
        if start % 2:
            start = 3 * start + 1
        else:
            start = start // 2
        res.append(start)

    return res

def longest_up_to(n):
    max_len, start_val = 0,0
    for start in range(1, n+1):
        length = len(collatz(start))
        if length > max_len:
            max_len, start_val = length, start
    return max_len, start_val



