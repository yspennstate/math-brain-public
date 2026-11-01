#!/usr/bin/env python3
from fractions import Fraction
from itertools import product
from math import comb

# Exact algebraic sanity checks for the stochastic-superblock variational
# mechanism.  This finite min-plus toy is NOT an FPP curvature certificate.

MATS = [
    [
        [Fraction(3,4), Fraction(1,2), Fraction(5,4)],
        [Fraction(1,2), Fraction(2),   Fraction(2)],
        [Fraction(2),   Fraction(7,4), Fraction(1)],
    ],
    [
        [Fraction(1,2), Fraction(2),   Fraction(1,4)],
        [Fraction(7,4), Fraction(7,4), Fraction(1,4)],
        [Fraction(2),   Fraction(5,4), Fraction(1)],
    ],
]

def F(D, y):
    return [min(y[i] + D[i][j] for i in range(len(y)))
            for j in range(len(y))]

def S1(y):
    vals = [F(D, y) for D in MATS]
    return [sum(v[j] for v in vals) / len(vals) for j in range(len(y))]

def Sm(y, m):
    vals = []
    for seq in product(range(len(MATS)), repeat=m):
        v = list(y)
        for a in seq:
            v = F(MATS[a], v)
        vals.append(v)
    return [sum(v[j] for v in vals) / len(vals) for j in range(len(y))]

def ceil_half(x):
    assert x >= 0
    q = (2*x.numerator + x.denominator - 1) // x.denominator
    return Fraction(q, 2)

def projected_step(D, y):
    f = F(D, y)
    g = min(f)
    phi = [x-g for x in f]
    # Upward half-grid projection of the normalized profile.
    return [g + ceil_half(x) for x in phi]

z = [Fraction(0), Fraction(0), Fraction(0)]
s1 = S1(z)
s2 = Sm(z, 2)
s1s1 = S1(s1)

# Coordinatewise Jensen inequality for the expected concave min-plus map:
# S_2(z) <= S_1(S_1(z)).
assert all(a <= b for a, b in zip(s2, s1s1))

lambda1 = max(a-b for a,b in zip(s1,z))
lambda2_per_block = max(a-b for a,b in zip(s2,z)) / 2
assert lambda2_per_block < lambda1
assert lambda1 == Fraction(7,8)
assert lambda2_per_block == Fraction(23,32)

# Internal upward projection gives a pathwise upper macro-map.  Verify over
# all 2^3 environments in a length-three toy macroblock.
for seq in product(range(2), repeat=3):
    raw = list(z)
    projected = list(z)
    for a in seq:
        raw = F(MATS[a], raw)
        projected = projected_step(MATS[a], projected)
        assert all(p >= r for p, r in zip(projected, raw))

# Exact boundary-chain constant used in the FPP report.
W = 48
M_W = Fraction(W,1) + Fraction(W*comb(2*W,W), 4**W)
assert M_W == Fraction(64247422146097977376474165077,
                       1237940039285380274899124224)

print('P20-STOCHASTIC-MACRO-EXACT-SANITY: ALL_EXACT_CHECKS_PASS')
print('toy_reference =', z)
print('S1(z) =', s1)
print('S2(z) =', s2)
print('S1(S1(z)) =', s1s1)
print('Lambda1 =', lambda1, '=', float(lambda1))
print('Lambda2_per_block =', lambda2_per_block, '=', float(lambda2_per_block))
print('strict_toy_macro_gain =', lambda1-lambda2_per_block, '=', float(lambda1-lambda2_per_block))
print('jensen_gap =', [b-a for a,b in zip(s2,s1s1)])
print('upward_projection_length3_sequences_checked = 8')
print('M_48 =', M_W, '=', float(M_W))
print('2*M_48 =', float(2*M_W))
print('2*M_48+2W =', float(2*M_W+2*W))
print('NOTE = algebraic sanity only; no source-level FPP claim')
