#!/usr/bin/env python3
from fractions import Fraction
from decimal import Decimal, getcontext

# Exact self-check for the non-C4 size-4 D2 sink-SCC family.
# No floating-point comparisons are used for the certified inequalities.

a = Fraction(9, 40)
b = Fraction(1, 2)

# Normalized family:
# p1=(0,0), p2=(1,0),
# x3 in [71/40,89/40], y3 in [-1/2,1/2],
# x4 in [111/40,129/40], y4 in [-1/2,1/2].
# Bounds below are exact interval extrema sufficient to force the intended D2 topology.
d13_max = Fraction(89, 40)**2 + b*b
d14_min = Fraction(111, 40)**2
d23_max = Fraction(49, 40)**2 + b*b
d24_min = Fraction(71, 40)**2
d34_max = Fraction(29, 20)**2 + (2*b)**2
d31_min = Fraction(71, 40)**2
d42_max = Fraction(89, 40)**2 + b*b
d41_min = Fraction(111, 40)**2

topology_gaps = [
    d14_min - d13_max,   # p1: p4 is behind p2,p3
    d24_min - d23_max,   # p2: p4 is behind p1,p3
    d31_min - d34_max,   # p3: p1 is behind p2,p4
    d41_min - d42_max,   # p4: p1 is behind p3,p2
]
min_gap = min(topology_gaps)

# A uniform upper bound on every internal second-neighbor distance.
U = Fraction(229, 100)
U2_slack = U*U - d13_max

# Global guard radius and local Hamiltonian-boundary surplus.
H = Fraction(57, 20)
delta = H - U

# Four-dimensional normalized shape volume.
V = (2*a) * (2*b) * (2*a) * (2*b)

# All centers lie in a rectangle of width 129/40 and height 1.
# Its H-parallel body contains the union of the four H-disks.
# pi < 22/7 gives this exact guard-area coefficient.
w = Fraction(129, 40)
h = Fraction(1)
Q = w*h + 2*H*(w+h) + Fraction(22, 7)*H*H
sqrtQ_up = Fraction(727, 100)
sqrt_slack = sqrtQ_up*sqrtQ_up - Q

# Four-point Campbell-Mecke coefficient:
# (5*pi^(3/2)/64) * V * delta * Q^(-7/2).
# Use pi > 3, sqrt(pi) > 17/10, and sqrt(Q) < 727/100.
pi32_lo = Fraction(3) * Fraction(17, 10)
Delta_chain = Fraction(5, 64) * pi32_lo * V * delta / (Q**3 * sqrtQ_up)

# Frozen predecessor endpoint from 2026-09-19T18-00-30Z.
B_prev = Fraction(
    1036840803576585538238788458409057357623753998433226173823634661443281840749793585890028594106544121959770829209188511,
    1647719764425586367726663550234487807993856583136701789232573772690085937500000000000000000000000000000000000000000000,
)
B_new = B_prev + Delta_chain

# Exact assertions.
assert V == Fraction(81, 400)
assert d13_max == Fraction(8321, 1600)
assert d14_min == Fraction(12321, 1600)
assert d23_max == Fraction(2801, 1600)
assert d24_min == Fraction(5041, 1600)
assert d34_max == Fraction(1241, 400)
assert d31_min == Fraction(5041, 1600)
assert min_gap == Fraction(77, 1600)
assert U2_slack == Fraction(1739, 40000)
assert delta == Fraction(14, 25)
assert Q == Fraction(147939, 2800)
assert sqrt_slack == Fraction(307, 17500)
assert Delta_chain == Fraction(3673530000, 87180364995004919)
assert Delta_chain > Fraction(42, 10**9)
assert B_new > Fraction(629258, 10**6)

getcontext().prec = 80
def dec(fr):
    return Decimal(fr.numerator) / Decimal(fr.denominator)

print(f"V_CHAIN = {V}")
print(f"TOPOLOGY_GAPS = {[str(x) for x in topology_gaps]}")
print(f"MIN_TOPOLOGY_GAP = {min_gap}")
print(f"D13_MAX = {d13_max}")
print(f"U2_SLACK = {U2_slack}")
print(f"H_MINUS_U = {delta}")
print(f"Q_UPPER = {Q}")
print(f"SQRTQ_UPPER = {sqrtQ_up}")
print(f"SQRTQ_SQUARE_SLACK = {sqrt_slack}")
print(f"DELTA_CHAIN_EXACT = {Delta_chain}")
print(f"DELTA_CHAIN_DECIMAL = {dec(Delta_chain)}")
print(f"B_PREV = {B_prev}")
print(f"B_PREV_DECIMAL = {dec(B_prev)}")
print(f"B_NEW = {B_new}")
print(f"B_NEW_DECIMAL = {dec(B_new)}")
print(f"DELTA_CHAIN_GT_4_2E_8 = {Delta_chain > Fraction(42, 10**9)}")
print(f"B_NEW_GT_0_629258 = {B_new > Fraction(629258, 10**6)}")
print("ALL_EXACT_FINITE_CHECKS_PASS")
