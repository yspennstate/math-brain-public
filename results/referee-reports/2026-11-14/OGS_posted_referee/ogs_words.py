# Independent check of Lemmas 2.1-2.2 of one-generator-shuffle: build the words as the proofs do and
# evaluate them. Words for c^i and for (0,d) are evaluated in full; (i,i+d) = c^i (0,d) c^{-i} is exact,
# so the longest transposition word is max len(0,d) + 2 max len(c^i) (attained since i and d range freely).
import math

def compose(a, b):           # (a b)(x) = a(b(x))
    return [a[x] for x in b]

def evaluate(word, gens, n):
    g = list(range(n))
    for s in word:
        g = compose(g, gens[s])
    return g

def inv_word(w):
    return [{'t': 't', 'c': 'C', 'C': 'c', 's': 'S', 'S': 's'}[x] for x in reversed(w)]

def cpow(i):                 # word for c^i, 0 < i < n, via c^{2q+b} = s c^q S c^b
    w = ['c']
    for b in bin(i)[3:]:
        w = ['s'] + w + ['S'] + (['c'] if b == '1' else [])
    return w

def trans0(d, h):            # word for (0,d) = B t B^{-1}
    js = [j for j in range(h) if (d >> j) & 1]
    B = ['s'] * js[0]
    for a, b in zip(js, js[1:]):
        B += ['t', 'c'] + ['s'] * (b - a)
    return B + ['t'] + inv_word(B)

worst, bad = {}, 0
for n in range(5, 302, 2):
    h = math.ceil(math.log2(n))
    gens = {'t': [1, 0] + list(range(2, n)), 'c': [(x + 1) % n for x in range(n)],
            'C': [(x - 1) % n for x in range(n)], 's': [(2 * x) % n for x in range(n)]}
    gens['S'] = [0] * n
    for x, y in enumerate(gens['s']):
        gens['S'][y] = x
    lp = 0
    for i in range(1, n):
        w = cpow(i)
        if evaluate(w, gens, n) != [(x + i) % n for x in range(n)] or len(w) > 3 * h - 2:
            bad += 1
        lp = max(lp, len(w))
    l0 = 0
    for d in range(1, n):
        w0 = trans0(d, h)
        target = list(range(n)); target[0], target[d] = d, 0
        if evaluate(w0, gens, n) != target or len(w0) > 6 * h - 5:
            bad += 1
        l0 = max(l0, len(w0))
    worst[n] = (l0 + 2 * lp, 12 * h - 9)
    if worst[n][0] > worst[n][1]:
        bad += 1
print("failures:", bad)
for n in (5, 7, 9, 11, 101, 255, 257, 301):
    print(n, "longest", worst[n][0], "bound", worst[n][1])
