"""Lexicographic (threshold-of-binary-number) functions: f_t(x) = -1 iff value(x) < t, where
value(x) = sum_i bit_i 2^(n-1-i) (bit_i = 1 iff x_i = -1; coordinate 0 most significant).
Hod (arXiv 1711.00762) uses this family for FEI lower bounds.  Exhaustive in t for n<=11, periodic
binary expansions for larger n.  Floats here; the final witness is re-certified with intervals.
"""
import numpy as np
from fei_lib import fwht_int, entropy_from_W, influence_from_W, H_interval


def lex_table(n, t):
    # index i of the truth table: bit j of i <-> x_j = -1.  value(x) uses bit j with weight 2^(n-1-j)
    idx = np.arange(1 << n, dtype=np.int64)
    val = np.zeros(1 << n, dtype=np.int64)
    for j in range(n):
        val += ((idx >> j) & 1) << (n - 1 - j)
    return np.where(val < t, -1, 1).astype(np.int64)


def best_exhaustive(n):
    best = (0.0, None)
    for t in range(1, 1 << n):
        f = lex_table(n, t)
        W = fwht_int(f)
        I = influence_from_W(W, n)
        if I == 0:
            continue
        H = entropy_from_W(W, n)
        r = H / float(I)
        if r > best[0]:
            best = (r, t, H, I)
    return best


if __name__ == '__main__':
    for n in range(2, 12):
        r, t, H, I = best_exhaustive(n)
        print(n, round(r, 6), 't=', t, bin(t)[2:].zfill(n), 'H=', round(H, 6), 'I=', I)
    # periodic expansions for larger n
    for n in (12, 14, 16):
        cands = []
        for period in range(1, 7):
            for pat in range(1, 1 << period):
                bits = ''.join(format(pat, 'b').zfill(period) for _ in range(n // period + 1))[:n]
                t = int(bits, 2)
                if t == 0:
                    continue
                f = lex_table(n, t)
                W = fwht_int(f)
                I = influence_from_W(W, n)
                H = entropy_from_W(W, n)
                cands.append((H / float(I), bits, H, float(I)))
        cands.sort(reverse=True)
        print(n, cands[:3])
