
def palindrome(i:int):
    s = str(i)
    front, back = 0, len(s)-1
    while front < back:
        if s[front] != s[back]:
            return False
        front += 1
        back += -1
    return True

def largest_palindrome_pair(n_digits):
    max = 10 ** n_digits - 1
    abs_max = 10 ** (2 * n_digits)
    min = abs_max - abs_max // 10
    m = (max - max % 11) // 11
    print(m, max, min)
    ok_num = lambda x: str(x)[-1] in (1, 3, 9)

    def ends_with_digit(n, d):
        return n % 10 == d

    def comp9(n):
        return 9 // (n % 10)

    def lower_9_factor(n):
        d = n % 10
        base = n - d
        if d > 3:
            return base + 3
        if d > 1:
            return base + 1
        if d <= 1:
            return base - 1

    def find_m1(start, next_lower=True):
        next_lower = next_lower or not ok_num(start)
        if next_lower:
            start = lower_9_factor(start)
        return start

    def f2_for(f1):
        comp = comp9(f1)
        print(f'comp={comp} for {f1}')
        f2 = max - max % 10 + comp
        while True:
            prod = f1 * f2
            print(f1, f2, prod)
            if prod > min:
                if palindrome(prod):
                    return f2
            else:
                break
            f2 -= 10
        return None

    # return f2_for(99)

    m1 = find_m1(m, False)
    print(f'm1 = {m1}')
    f2 = None
    while m1 >= 1:
        f1 = m1 * 11
        f2 = f2_for(f1)
        if f2:
            return f1, f2
        m1 = find_m1(m1)

    return 0, 0

