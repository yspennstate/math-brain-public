#!/usr/bin/env python3
"""
Exact SELF-CHECK for R7-03 C0036, Z/5Z orbit reduction and one-spike theorem.

This is owner-track validation, not an independent audit and not a proof of
Lyons Conjecture 5.7 for arbitrary order-five spectra.

Checks:
  1. exact translation-orbit poset of 2^(Z/5Z): 8 orbits, 11 invariant upper
     sets, exactly 4 non-cardinality upper sets;
  2. symbolic factor identities for the one-exceptional-Fourier-eigenvalue
     family (a,b,b,b,b), with a=b*t^5 and p=b*t;
  3. exact Q(sqrt(5)) sign check of the four order-five non-cardinality gaps on
     the 5^5 grid lambda_i=(m_i/4)^5, m_i=0,...,4.
"""
from fractions import Fraction
from itertools import product
from functools import reduce
import sympy as sp

N = 5

def translate(mask, g):
    out = 0
    for i in range(N):
        if (mask >> i) & 1:
            out |= 1 << ((i + g) % N)
    return out

# Translation orbits of subsets.
seen = set()
orbits = []
for mask in range(1 << N):
    if mask in seen:
        continue
    orb = sorted({translate(mask, g) for g in range(N)})
    seen.update(orb)
    orbits.append(orb)
assert len(orbits) == 8

# Orbit partial order: O_i <= O_j iff some A in O_i is contained in some B in O_j.
leq = [[False] * len(orbits) for _ in orbits]
for i, oi in enumerate(orbits):
    for j, oj in enumerate(orbits):
        leq[i][j] = any((a & ~b) == 0 for a in oi for b in oj)

upper_sets = []
for bits in range(1 << len(orbits)):
    ok = True
    for i in range(len(orbits)):
        if (bits >> i) & 1:
            for j in range(len(orbits)):
                if leq[i][j] and not ((bits >> j) & 1):
                    ok = False
                    break
        if not ok:
            break
    if ok:
        upper_sets.append(bits)

# For five points there are 7 cardinality-only upper sets:
# empty, whole space, and the five thresholds |X| >= m, m=1,...,5.
assert len(upper_sets) == 11
assert len(upper_sets) - 7 == 4

# Symbolic one-spike identities.
t, b = sp.symbols("t b", nonnegative=True)
p = b * t
D2 = b**2 * (3 + 2*t**5) / 5
T3 = b**3 * (2 + 3*t**5) / 5
D4 = b**4 * (1 + 4*t**5) / 5

P = 2*t**3 + 4*t**2 + 6*t + 3
Q = 3*t**3 + 6*t**2 + 4*t + 2
R = 4*t**3 + 3*t**2 + 2*t + 1

pair_gap = sp.factor(D2 - T3 - p**2 * (1-p))
trip_gap = sp.factor(T3 - D4 - p**3 * (1-p))
pair_expected = sp.factor(b**2 * (t-1)**2 * (P - b*Q) / 5)
trip_expected = sp.factor(b**3 * (t-1)**2 * (Q - b*R) / 5)
assert sp.expand(pair_gap - pair_expected) == 0
assert sp.expand(trip_gap - trip_expected) == 0
assert sp.expand((P-Q) + (t-1)*(t**2 + 3*t + 1)) == 0
assert sp.expand((t**5 * P - Q) - (
    (t-1)*(t+1)*
    (2*t**6 + 4*t**5 + 8*t**4 + 7*t**3 + 8*t**2 + 4*t + 2)
)) == 0

# Exact sign in Q(sqrt(5)).
def sign_qsqrt5(r, s):
    """Return sign of r + s*sqrt(5), with r,s rational."""
    if s == 0:
        return (r > 0) - (r < 0)
    if s > 0:
        if r >= 0:
            return 1
        return (5*s*s > r*r) - (5*s*s < r*r)
    # s < 0
    if r <= 0:
        return -1
    return (r*r > 5*s*s) - (r*r < 5*s*s)

def prod_frac(xs):
    return reduce(lambda x, y: x*y, xs, Fraction(1))

# On the exact grid lambda_i=(m_i/4)^5, the geometric mean is rational:
# p = prod_i m_i / 4^5.
den = 4**5
counts = [[0, 0, 0] for _ in range(4)]  # negative, zero, positive
bad = []
for ms in product(range(5), repeat=5):
    lam = [Fraction(m**5, den) for m in ms]
    pp = Fraction(prod_frac(ms), den)

    A = sum(lam[i] * lam[(i+1) % 5] for i in range(5))
    B = sum(lam[i] * lam[(i+2) % 5] for i in range(5))
    C1 = sum(
        prod_frac([lam[j] for j in range(5)
                   if j not in {i, (i+1) % 5}])
        for i in range(5)
    )
    C2 = sum(
        prod_frac([lam[j] for j in range(5)
                   if j not in {i, (i+2) % 5}])
        for i in range(5)
    )
    e4 = sum(
        prod_frac([lam[j] for j in range(5) if j != i])
        for i in range(5)
    )

    # alpha=(5-sqrt5)/50, beta=(5+sqrt5)/50.
    # The four non-cardinality lower-domination gaps are:
    # pair shape 1, pair shape 2, triple shape 1, triple shape 2.
    pair_r = (A + B - C1 - C2) / 10 - pp**2 * (1-pp)
    pair_s = (B - A - C2 + C1) / 50
    trip_r = (C1 + C2) / 10 - e4 / 5 - pp**3 * (1-pp)
    trip_s = (C2 - C1) / 50

    vals = [
        (pair_r, pair_s),
        (pair_r, -pair_s),
        (trip_r, trip_s),
        (trip_r, -trip_s),
    ]
    for idx, (r, s) in enumerate(vals):
        sg = sign_qsqrt5(r, s)
        counts[idx][sg+1] += 1
        if sg < 0:
            bad.append((idx, ms, r, s))

assert not bad

print("Z5_TRANSLATION_ORBITS=8")
print("Z5_INVARIANT_UPPER_SETS=11")
print("Z5_NONCARDINALITY_UPPER_SETS=4")
print("ONE_SPIKE_FACTOR_IDENTITIES=PASS")
print("EXACT_GRID_SPECTRA=3125")
for idx, label in enumerate(
    ["PAIR_ORBIT_1", "PAIR_ORBIT_2", "TRIPLE_ORBIT_1", "TRIPLE_ORBIT_2"]
):
    neg, zero, pos = counts[idx]
    print(f"{label}: negative={neg} zero={zero} positive={pos}")
print("ALL_EXACT_CHECKS_PASS")
