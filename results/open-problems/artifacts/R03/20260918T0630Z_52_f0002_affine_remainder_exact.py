#!/usr/bin/env python3
from fractions import Fraction
from collections import Counter
from itertools import product


def inv_fraction(A):
    n = len(A)
    M = [[Fraction(A[i][j]) for j in range(n)] +
         [Fraction(int(i == j)) for j in range(n)] for i in range(n)]
    for col in range(n):
        piv = next((r for r in range(col, n) if M[r][col] != 0), None)
        if piv is None:
            return None
        M[col], M[piv] = M[piv], M[col]
        p = M[col][col]
        M[col] = [x / p for x in M[col]]
        for r in range(n):
            if r == col:
                continue
            f = M[r][col]
            if f:
                M[r] = [M[r][j] - f * M[col][j] for j in range(2*n)]
    return [row[n:] for row in M]


def sym01_from_bits(d, bits):
    A = [[0]*d for _ in range(d)]
    k = 0
    for i in range(d):
        for j in range(i, d):
            b = (bits >> k) & 1
            k += 1
            A[i][j] = A[j][i] = b
    return A


def transversality_richness(D):
    inv = inv_fraction(D)
    if inv is None:
        return None
    d = len(D)
    T = 0
    for z in product((0, 1), repeat=d):
        if not any(z):
            continue
        w = [sum(inv[i][j] * z[j] for j in range(d)) for i in range(d)]
        q = sum(Fraction(z[i]) * w[i] for i in range(d))
        ell = sum(w)
        if q in (0, 1) and ell != 1:
            T += 1
    return T


def main():
    expected = {
        1: (1, Counter({0: 1}), Fraction(0, 1)),
        2: (4, Counter({0: 4}), Fraction(0, 1)),
        3: (32, Counter({0: 8, 1: 12, 2: 12}), Fraction(9, 16)),
        4: (528, Counter({0: 55, 1: 48, 2: 132, 3: 248, 4: 21, 5: 24}), Fraction(315, 256)),
        5: (18596, Counter({0: 761, 1: 1160, 2: 1920, 3: 1300, 4: 2410,
                           5: 2100, 6: 2820, 7: 1080, 8: 1320, 9: 2360,
                           10: 990, 11: 240, 12: 75, 13: 60}), Fraction(24885, 8192)),
    }
    for d in range(1, 6):
        total = 1 << (d*(d+1)//2)
        dist = Counter()
        inv_count = 0
        sum_T = 0
        for bits in range(total):
            D = sym01_from_bits(d, bits)
            T = transversality_richness(D)
            if T is None:
                continue
            inv_count += 1
            dist[T] += 1
            sum_T += T
        ET = Fraction(sum_T, total)
        exp_inv, exp_dist, exp_ET = expected[d]
        assert inv_count == exp_inv
        assert dist == exp_dist
        assert ET == exp_ET
        print(f"d={d} total={total} invertible={inv_count} dist={dict(sorted(dist.items()))} E_T={ET}")
    print("EXACT_CHECK_PASS")

if __name__ == '__main__':
    main()
