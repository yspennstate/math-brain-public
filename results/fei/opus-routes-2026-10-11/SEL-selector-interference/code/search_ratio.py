"""Search for explicit Boolean functions with H(f) > 4 I(f) (needed as an exact witness that the
orthogonal-neighbour closure constant max(4, C_leaf) fails once selector coordinates are reused).

1. exhaustive n<=4: max H/I.
2. structured n<=10: compositions OR/AND of ANDs (tribes-like), read-once formulas, symmetric functions.
"""
import itertools
import numpy as np
from fractions import Fraction
from fei_lib import fwht_int, entropy_from_W, influence_from_W, H_interval


def ratio(table, n):
    W = fwht_int(table)
    H = entropy_from_W(W, n)
    I = influence_from_W(W, n)
    return H, I, (H / float(I) if I > 0 else 0.0), W


def exhaustive4():
    best = (0, None)
    n = 4
    for code in range(1 << 16):
        t = np.array([1 - 2 * ((code >> i) & 1) for i in range(16)], dtype=np.int64)
        H, I, r, _ = ratio(t, n)
        if r > best[0]:
            best = (r, code, H, I)
    return best


def tribes_table(w, s):
    """OR of s ANDs of width w (true=-1).  n = w*s."""
    n = w * s
    idx = np.arange(1 << n)
    out = np.ones(1 << n, dtype=np.int64)
    anyt = np.zeros(1 << n, dtype=bool)
    for t in range(s):
        allt = np.ones(1 << n, dtype=bool)
        for k in range(w):
            j = t * w + k
            allt &= ((idx >> j) & 1) == 1
        anyt |= allt
    out[anyt] = -1
    return out, n


def and_table(n):
    out = np.ones(1 << n, dtype=np.int64)
    out[(1 << n) - 1] = -1
    return out


def compose_and_of_or(w, s):
    """AND of s ORs of width w."""
    n = w * s
    idx = np.arange(1 << n)
    allt = np.ones(1 << n, dtype=bool)
    for t in range(s):
        anyt = np.zeros(1 << n, dtype=bool)
        for k in range(w):
            j = t * w + k
            anyt |= ((idx >> j) & 1) == 1
        allt &= anyt
    out = np.ones(1 << n, dtype=np.int64)
    out[allt] = -1
    return out, n


if __name__ == '__main__':
    b = exhaustive4()
    print('n<=4 exhaustive best H/I:', b)
    res = []
    for w in range(1, 6):
        for s in range(1, 6):
            if w * s > 14:
                continue
            t, n = tribes_table(w, s)
            H, I, r, W = ratio(t, n)
            res.append(('tribes', w, s, n, H, float(I), r))
            t, n = compose_and_of_or(w, s)
            H, I, r, W = ratio(t, n)
            res.append(('andor', w, s, n, H, float(I), r))
    for n in range(2, 15):
        t = and_table(n)
        H, I, r, W = ratio(t, n)
        res.append(('and', n, 1, n, H, float(I), r))
    res.sort(key=lambda z: -z[-1])
    for z in res[:15]:
        print(z)
