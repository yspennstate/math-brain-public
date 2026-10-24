from functools import lru_cache
from fractions import Fraction
from itertools import product
import math
import sympy as sp

Q = 4
C = 0

@lru_cache(None)
def B(w):
    w = tuple(w)
    n = len(w)
    if n == 0:
        return 1
    if any(w[i] == w[i + 1] for i in range(n - 1)):
        return 0
    return sum(B(w[:i] + w[i + 1:]) for i in range(n))

def prob(w):
    n = len(w)
    return Fraction(B(tuple(w)), math.factorial(n + 1) * (2 ** n))

def proper_words(n):
    return [w for w in product(range(Q), repeat=n)
            if all(w[i] != w[i + 1] for i in range(n - 1))]

def cond_matrix(m):
    left = [u for u in proper_words(m) if u[-1] != C]
    right = [v for v in proper_words(m) if v[0] != C]
    den = prob((C,))
    H = [[prob(u + (C,) + v) / den for v in right] for u in left]
    assert sum(sum(row, Fraction(0)) for row in H) == 1
    return left, right, H

def rank_integer_core(m):
    left, right, _ = cond_matrix(m)
    M = sp.Matrix([[B(u + (C,) + v) for v in right] for u in left])
    return M.rank(), len(left), len(right)

def row_marginal_minorant_mass(m):
    left, right, H = cond_matrix(m)
    rho = [sum(row, Fraction(0)) for row in H]
    y = []
    for j in range(len(right)):
        yj = min(H[i][j] / rho[i] for i in range(len(left)) if rho[i] > 0)
        y.append(yj)
    for i in range(len(left)):
        for j in range(len(right)):
            assert rho[i] * y[j] <= H[i][j]
    return sum(rho, Fraction(0)) * sum(y, Fraction(0))

def one_sided_cond(u, a):
    u = tuple(u)
    m = len(u)
    if u and u[-1] == a:
        return Fraction(0)
    return Fraction(B(u + (a,)), 2 * (m + 2) * B(u))

for n in range(1, 7):
    total = sum((prob(w) for w in product(range(Q), repeat=n)), Fraction(0))
    assert total == 1, (n, total)
print("NORMALIZATION n=1..6: PASS")

expected_ranks = [3, 6, 10, 15]
for m, expected in enumerate(expected_ranks, 1):
    rank, nl, nr = rank_integer_core(m)
    assert rank == expected, (m, rank, expected)
    print(f"CONTEXT_RANK m={m}: {rank} on {nl}x{nr} matrix PASS")

for m in range(1, 6):
    mass = row_marginal_minorant_mass(m)
    expected = Fraction(3, m + 3)
    assert mass == expected, (m, mass, expected)
    print(f"ROW_MARGINAL_MINORANT m={m}: {mass} = 3/{m+3} PASS")

left, right, H = cond_matrix(1)
assert len(left) == len(right) == 3
x = [Fraction(1, 4), Fraction(3, 8), Fraction(3, 8)]
y = [Fraction(1, 3), Fraction(2, 9), Fraction(2, 9)]
for i in range(3):
    for j in range(3):
        assert x[i] * y[j] <= H[i][j]
mass = sum(x, Fraction(0)) * sum(y, Fraction(0))
assert mass == Fraction(7, 9)
print("M1_EXPLICIT_PRODUCT_MINORANT mass=7/9: PASS")

for m in range(1, 13):
    A = tuple(i % 2 for i in range(m))
    assert B(A) == 2 ** (m - 1)
    partner = m % 2
    assert B(A + (partner,)) == 2 ** m
    assert B(A + (2,)) == (m + 1) * 2 ** (m - 1)
    g_alt = one_sided_cond(A, partner)
    g_third = one_sided_cond(A, 2)
    assert g_alt == Fraction(1, m + 2)
    assert g_third == Fraction(m + 1, 2 * (m + 2))
    print(f"ALTERNATING m={m}: g_alt={g_alt}, g_third={g_third} PASS")

for m in range(1, 9):
    vals = []
    for u in proper_words(m):
        for a in range(Q):
            if u[-1] != a:
                vals.append(one_sided_cond(u, a))
    mn, mx = min(vals), max(vals)
    assert mn == Fraction(1, m + 2)
    expected_max = Fraction(1, 3) if m == 1 else Fraction(m + 1, 2 * (m + 2))
    assert mx == expected_max
    print(f"FINITE_G_EXTREMA m={m}: min={mn}, max={mx} PASS")

print("ALL_EXACT_CHECKS_PASS")
