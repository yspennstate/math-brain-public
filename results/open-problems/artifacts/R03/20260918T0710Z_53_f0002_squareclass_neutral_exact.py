#!/usr/bin/env python3
from fractions import Fraction
from itertools import product
from collections import Counter, defaultdict


def det_bareiss(A):
    n = len(A)
    if n == 0:
        return 1
    M = [list(map(int, row)) for row in A]
    sign, prev = 1, 1
    for k in range(n - 1):
        piv = next((r for r in range(k, n) if M[r][k] != 0), None)
        if piv is None:
            return 0
        if piv != k:
            M[k], M[piv] = M[piv], M[k]
            sign *= -1
        pivot = M[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                M[i][j] = (M[i][j] * pivot - M[i][k] * M[k][j]) // prev
        prev = pivot
        for i in range(k + 1, n):
            M[i][k] = 0
    return sign * M[n - 1][n - 1]


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
                M[r] = [M[r][j] - f * M[col][j] for j in range(2 * n)]
    return [row[n:] for row in M]


def sym01_from_bits(d, bits):
    A = [[0] * d for _ in range(d)]
    k = 0
    for i in range(d):
        for j in range(i, d):
            b = (bits >> k) & 1
            k += 1
            A[i][j] = A[j][i] = b
    return A


def squarefree_part(n):
    n = abs(n)
    out, p = 1, 2
    while p * p <= n:
        parity = 0
        while n % p == 0:
            n //= p
            parity ^= 1
        if parity:
            out *= p
        p += 1
    return out * n


def richness(D):
    inv = inv_fraction(D)
    if inv is None:
        return None
    d = len(D)
    T = 0
    neutral = 0
    sols = []
    for z in product((0, 1), repeat=d):
        w = [sum(inv[i][j] * z[j] for j in range(d)) for i in range(d)]
        q = sum(Fraction(z[i]) * w[i] for i in range(d))
        ell = sum(w)
        if q == 0 and ell == 0:
            neutral += 1
        if any(z) and q in (0, 1) and ell != 1:
            T += 1
            sols.append((z, q, ell))
    return T, neutral, sols


def block_diag(blocks):
    n = sum(len(B) for B in blocks)
    A = [[0] * n for _ in range(n)]
    off = 0
    for B in blocks:
        r = len(B)
        for i in range(r):
            for j in range(r):
                A[off + i][off + j] = B[i][j]
        off += r
    return A


def main():
    for d in range(1, 6):
        total = 1 << (d * (d + 1) // 2)
        inv_count = 0
        max_T = 0
        max_neutral = 0
        max_T_by_sf = defaultdict(int)
        neutral_hist = Counter()
        square_identity_checks = 0

        for bits in range(total):
            D = sym01_from_bits(d, bits)
            a = det_bareiss(D)
            if a == 0:
                continue
            inv_count += 1
            T, neutral, sols = richness(D)
            max_T = max(max_T, T)
            max_neutral = max(max_neutral, neutral)
            max_T_by_sf[squarefree_part(a)] = max(max_T_by_sf[squarefree_part(a)], T)
            neutral_hist[neutral] += 1

            for z, q, ell in sols:
                C = [row[:] + [z[i]] for i, row in enumerate(D)]
                C.append(list(z) + [int(q)])
                assert det_bareiss(C) == 0
                E = [[1 - C[i][j] for j in range(d + 1)] for i in range(d + 1)]
                detE = det_bareiss(E)
                assert detE != 0
                b = Fraction(a) * (1 - ell)
                assert b.denominator == 1
                assert a * detE == ((-1) ** d) * (b.numerator ** 2)
                square_identity_checks += 1

        print(
            f"d={d} invertible={inv_count}/{total} max_T={max_T} "
            f"max_neutral={max_neutral} max_T_by_squarefree={dict(sorted(max_T_by_sf.items()))} "
            f"neutral_hist={dict(sorted(neutral_hist.items()))} "
            f"square_identity_checks={square_identity_checks}"
        )

    D0 = [[1, 1, 1],
          [1, 1, 0],
          [1, 0, 1]]
    T0, M0, _ = richness(D0)
    assert det_bareiss(D0) == -1
    assert T0 == 2 and M0 == 3
    neutral0 = []
    inv0 = inv_fraction(D0)
    for z in product((0, 1), repeat=3):
        w = [sum(inv0[i][j] * z[j] for j in range(3)) for i in range(3)]
        q = sum(Fraction(z[i]) * w[i] for i in range(3))
        ell = sum(w)
        if q == 0 and ell == 0:
            neutral0.append(z)
    assert neutral0 == [(0, 0, 0), (0, 0, 1), (0, 1, 0)]
    print(f"D0_det=-1 D0_T={T0} D0_neutral={M0} neutral_vectors={neutral0}")

    for k in range(1, 5):
        Dk = block_diag([D0] * k)
        assert det_bareiss(Dk) == (-1) ** k
        certified_neutral = M0 ** k
        certified_T_lower = certified_neutral - 1
        print(
            f"k={k} d={3*k} det={det_bareiss(Dk)} "
            f"certified_neutral={certified_neutral} certified_T_lower={certified_T_lower}"
        )

    print("EXACT_CHECK_PASS")


if __name__ == "__main__":
    main()
