#!/usr/bin/env python3
"""Exact finite core for HARD7-06 run 1.

Enumerate the 4^3 ordered joint-color labels for two balanced 2-colorings.
A triple is valid when neither coordinate is monochromatic.  N counts labels
00 or 11.  Fraction arithmetic then certifies the variance and the exact
curvature of the symmetric configuration-model overlap rate.
"""
from collections import Counter
from fractions import Fraction
from itertools import product

labels = [(0, 0), (0, 1), (1, 0), (1, 1)]
counts = Counter()
valid = []
for triple in product(range(4), repeat=3):
    first = [labels[i][0] for i in triple]
    second = [labels[i][1] for i in triple]
    if len(set(first)) > 1 and len(set(second)) > 1:
        N = sum(labels[i][0] == labels[i][1] for i in triple)
        counts[N] += 1
        valid.append(triple)

total = len(valid)
EN = sum((Fraction(n * c, total) for n, c in counts.items()), Fraction(0))
EN2 = sum((Fraction(n * n * c, total) for n, c in counts.items()), Fraction(0))
varN = EN2 - EN * EN

# s=(1+theta)/2 and the exponential-family saddle has E_u[N]=3s.
# At theta=0, u=log t=0, so du/dtheta=(3/2)/Var(N).
uprime0 = Fraction(3, 2) / varN
Hp2 = -Fraction(3, 2) * uprime0
Hq2 = Fraction(-1)

def S2(d):
    d = Fraction(d)
    return (1 - d) * Hq2 + d * Hp2 / 3

assert counts == Counter({1: 12, 2: 12, 0: 6, 3: 6})
assert total == 36
assert EN == Fraction(3, 2)
assert EN2 == Fraction(19, 6)
assert varN == Fraction(11, 12)
assert uprime0 == Fraction(18, 11)
assert Hp2 == Fraction(-27, 11)
assert S2(5) == Fraction(-1, 11)
assert S2(Fraction(11, 2)) == 0
assert S2(6) == Fraction(1, 11)
assert S2(7) == Fraction(3, 11)

print("valid ordered patterns:", total)
print("N-counts:", dict(sorted(counts.items())))
print("E[N] =", EN)
print("E[N^2] =", EN2)
print("Var(N) =", varN)
print("u'(0) =", uprime0)
print("H_q''(0) =", Hq2)
print("H_p''(0) =", Hp2)
for d in (5, Fraction(11, 2), 6, 7):
    print(f"S_{d}''(0) =", S2(d))
print("ALL_EXACT_CHECKS_PASS")
