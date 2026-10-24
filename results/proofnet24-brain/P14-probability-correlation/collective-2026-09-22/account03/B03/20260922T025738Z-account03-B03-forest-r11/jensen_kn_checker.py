#!/usr/bin/env python3
"""Exact regression for FOREST-KN-HERMITE-JENSEN-v1.

Standard-library only. This is regression evidence; the all-n proof is in report.md.
"""
from fractions import Fraction
from itertools import combinations


def he_values(kmax, x):
    h = [0] * (kmax + 1)
    h[0] = 1
    if kmax >= 1:
        h[1] = x
    for k in range(1, kmax):
        h[k + 1] = x * h[k] - k * h[k - 1]
    return h


def formula_counts(n):
    h = he_values(n, n + 1)

    def D(j):
        return h[j] - (j * h[j - 1] if j else 0)

    Z = D(n)
    E = D(n - 2)
    J_adj = D(n - 3)
    J_dis = D(n - 4) + 4 * h[n - 4] if n >= 4 else None
    return Z, E, J_adj, J_dis


def brute_counts(n):
    edges = list(combinations(range(n), 2))
    idx = {e: i for i, e in enumerate(edges)}
    e0 = idx[(0, 1)]
    fa = idx[(0, 2)] if n >= 3 else None
    fd = idx[(2, 3)] if n >= 4 else None
    Z = E = Ja = Jd = 0
    m = len(edges)
    for mask in range(1 << m):
        parent = list(range(n))

        def find(a):
            while parent[a] != a:
                parent[a] = parent[parent[a]]
                a = parent[a]
            return a

        ok = True
        for i, (u, v) in enumerate(edges):
            if not (mask >> i) & 1:
                continue
            ru, rv = find(u), find(v)
            if ru == rv:
                ok = False
                break
            parent[ru] = rv
        if not ok:
            continue
        Z += 1
        if (mask >> e0) & 1:
            E += 1
            if fa is not None and ((mask >> fa) & 1):
                Ja += 1
            if fd is not None and ((mask >> fd) & 1):
                Jd += 1
    return Z, E, Ja, Jd if n >= 4 else None


def G(n, s):
    return (5 - n) * s * s + (n * n - 4 * n - 6) * s - n * n + 9 * n - 14


def jensen_bound(n):
    return Fraction((n - 4) * (n + 1), n * n + n + 6)


def actual_s(n):
    k = n - 4
    h = he_values(k, n + 1)
    return Fraction(k * h[k - 1], h[k])


for n in range(3, 7):
    b = brute_counts(n)
    f = formula_counts(n)
    assert b == f, (n, b, f)
print("BRUTE_FORMULA_PASS n=3..6")

for n in range(4, 31):
    Z, E, Ja, Jd = formula_counts(n)
    assert E * E - Z * Ja >= 0
    assert E * E - Z * Jd >= 0
print("EXACT_GAPS_PASS n=4..30")

for n in range(6, 501):
    s = actual_s(n)
    J = jensen_bound(n)
    assert J <= s < 1
    assert G(n, J) > 0
    assert G(n, s) > 0
print("JENSEN_SIGN_PASS n=6..500")

for n in range(6, 501):
    J = jensen_bound(n)
    lhs = G(n, J)
    num = 3 * n**4 + 40 * n**3 - 59 * n**2 + 488 * n - 280
    den = (n * n + n + 6) ** 2
    assert lhs == Fraction(num, den)
print("RATIONAL_IDENTITY_PASS n=6..500")

for n in range(4, 11):
    Z, E, Ja, Jd = formula_counts(n)
    ga = E * E - Z * Ja
    gd = E * E - Z * Jd
    print(
        f"n={n} Z={Z} E={E} J_adj={Ja} J_dis={Jd} "
        f"gap_adj={ga} gap_dis={gd}"
    )
