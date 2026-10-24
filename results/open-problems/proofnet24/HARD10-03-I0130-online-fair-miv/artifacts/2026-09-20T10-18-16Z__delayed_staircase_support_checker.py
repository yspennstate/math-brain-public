#!/usr/bin/env python3
from fractions import Fraction as F

# I0130 delayed-staircase support checker.
# All inequalities are exact rational arithmetic.
p = F(231987093666883409713408842559789945917,
      52664345525950501687094998553955322162130)
q0 = F(18) - 20*p
qs = F(400, 9)*p

def D(q):
    return ((200*p + q)*(40 - q))/(110*p + q + 81)

def N(q):
    # Positive denominator omitted from D'(q).
    return F(3240) - 162*q - q*q - 220*p*q - 19800*p - 22000*p*p

def ceilF(x):
    return (x.numerator + x.denominator - 1)//x.denominator

# Explicit tail-to-core ladder; core-to-tail order is reversed.
r = [
    qs,
    F(18,25),
    F(297,200),
    F(2583,1000),
    F(1031,250),
    F(6221,1000),
    F(2239,250),
    F(3083,250),
    F(4057,250),
]
assert all(r[i] < r[i+1] for i in range(len(r)-1))
assert r[-1] < q0

# For the first eight boundaries D is increasing throughout the needed range.
# N is strictly decreasing in q, so N(r[-1])>0 proves D'>0 on [qs,r8].
assert N(r[-1]) > 0
for i in range(8):
    assert r[i+1] - r[i] <= D(r[i])

# On [r8,q0], N is strictly decreasing, hence D is unimodal.
# The endpoint comparison makes D(r8) the lower endpoint value,
# sufficient for the final q0/r8 boundary.
assert D(q0) > D(r[-1])
assert q0 - r[-1] <= D(r[-1])

# Previous full-continuous report uses height BQ and proves F0<=42301440 Q
# on support J<20800. Keeping q0 through J=20800 preserves that domination.
B = F(42675840)
assert B - q0*20800 > F(42301440)

# Every action queries total span <=7680. Boundaries 7681 apart imply
# at most one slope boundary is crossed by a Bellman comparison.
L = 7681
assert L > 7680

# Delay the transition almost to the zero crossing.
# Core-to-tail transition blocks have slopes r8,r7,...,r1.
Atrans = L*sum(r[1:])
R = 2359880
E = R + 8*L
rho = B - q0*R - Atrans

# A >=7680-edge q* terminal zone is retained so positive-part clipping
# cannot expose a pre-tail slope in either the forward-crossing or backward branch.
assert rho > 0
k = ceilF(rho/qs)
Z = E + k
assert E == 2421328
assert k == 7708
assert Z == 2429036
assert k >= 7680
assert rho - (k-1)*qs > 0
assert rho - k*qs <= 0

# Sanity: strict improvement over the inherited uniform cutoff.
assert Z < 240051600

margins = [D(r[i])-(r[i+1]-r[i]) for i in range(8)]
print("I0130_DELAYED_STAIRCASE_SUPPORT_PASS")
print("R =", R)
print("E =", E)
print("tail_qstar_edges =", k)
print("support_cutoff_Z =", Z)
print("old_cutoff =", 240051600)
print("old_over_new =", float(F(240051600, Z)))
print("handoff_margin_over_Q =", float(B-q0*20800-F(42301440)))
print("min_boundary_margin_exact =", min(margins))
print("final_boundary_margin_exact =", D(r[-1])-(q0-r[-1]))
