#!/usr/bin/env python3
"""Bounded exact self-check for the B12 terminal-shadow equivalence report.

The universal results are proved algebraically in REPORT.md.  This program only
checks representative finite identities with Fraction arithmetic.
"""
from fractions import Fraction
from itertools import permutations
from math import comb, factorial, log2
import json

def pc(x):
    return int(x).bit_count()

def shadow(p, n):
    out = {}
    for A in range(1 << n):
        a = pc(A)
        out[A] = sum(
            (m / comb(pc(B), a))
            for B, m in p.items()
            if m and (B & A) == A
        )
    return out

n = 4
weights = {A: Fraction((A + 1) * (pc(A) + 1), 1) for A in range(1 << n)}
Z = sum(weights.values(), Fraction(0))
p = {A: w / Z for A, w in weights.items()}
v = shadow(p, n)
I = sum(m * pc(A) for A, m in p.items())

for a in range(n + 1):
    lhs = sum(v[A] for A in range(1 << n) if pc(A) == a)
    rhs = sum(m for B, m in p.items() if pc(B) >= a)
    assert lhs == rhs
assert sum(v.values(), Fraction(0)) == 1 + I

for A in range(1 << n):
    a = pc(A)
    lhs = sum(v[A | (1 << i)] for i in range(n) if not ((A >> i) & 1))
    assert lhs == (a + 1) * (v[A] - p[A])

def V(T):
    return sum(m for B, m in p.items() if (B & ~T) == 0)

def delta_A_V(A, T):
    bits = [i for i in range(n) if (A >> i) & 1]
    ans = Fraction(0)
    for cm in range(1 << len(bits)):
        C = 0
        for j, bit in enumerate(bits):
            if (cm >> j) & 1:
                C |= 1 << bit
        ans += (-1) ** (len(bits) - pc(cm)) * V(T | C)
    return ans

perms = list(permutations(range(n)))
for A in range(1, 1 << n):
    Abits = [i for i in range(n) if (A >> i) & 1]
    vals = []
    for perm in perms:
        pos = {x: j for j, x in enumerate(perm)}
        first = min(pos[i] for i in Abits)
        T = 0
        for j in perm[:first]:
            if not ((A >> j) & 1):
                T |= 1 << j
        vals.append(delta_A_V(A, T))
    assert sum(vals, Fraction(0)) / len(vals) == v[A]

for nn in range(2, 13):
    c = Fraction(1, 4 ** (nn - 1))
    closed = c * Fraction(2 ** nn - 1, nn)
    direct = sum(
        Fraction(comb(nn - 1, k - 1), 1) * c / k
        for k in range(1, nn + 1)
    )
    assert direct == closed

Bsh = sum(float(m) * log2(float(v[A] / m)) for A, m in p.items() if m)
jensen_rhs = log2(1 + float(I))
assert Bsh <= jensen_rhs + 1e-14

print(json.dumps({
    "status": "PASS",
    "scope": "finite self-check; universal proof is in REPORT.md",
    "rational_subset_dimension": n,
    "level_shadow_identities_exact": n + 1,
    "prefix_recurrence_cases_exact": 1 << n,
    "shapley_permutation_instances_exact": ((1 << n) - 1) * factorial(n),
    "and_singleton_formula_n": "2..12",
    "shadow_total_exact": str(sum(v.values(), Fraction(0))),
    "one_plus_I_exact": str(1 + I),
    "Bsh_float_sanity": Bsh,
    "log2_one_plus_I_float_sanity": jensen_rhs,
}, indent=2, sort_keys=True))
