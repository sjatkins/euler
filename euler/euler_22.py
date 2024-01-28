with open('euler/0022_names.txt') as f:
    raw = f.read().strip()

names = sorted([n[1:-1] for n in raw.split(',')])
enumerated_names = {n: index+1 for index, n in enumerate(names)}

letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
l_val = {c:i+1 for i,c in enumerate(letters)}


def name_score(name):
    return sum(l_val[c] for c in name) * enumerated_names[name]

def solve():
    assert name_score('COLIN') == 49714
    return sum(name_score(name) for name in names)

solve()