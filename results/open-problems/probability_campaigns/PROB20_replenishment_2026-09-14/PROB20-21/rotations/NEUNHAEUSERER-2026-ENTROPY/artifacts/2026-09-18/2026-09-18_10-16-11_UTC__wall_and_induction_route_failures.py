#!/usr/bin/env python3
"""
Exact self-checks for NEUNHAEUSERER-2026-ENTROPY, B6/B13/B19 run.

All arithmetic below is rational except that log(2) is kept as a formal
positive symbol L.  We prove the one required positivity statement using
the elementary exact lower bound log(2)>2/3 coming from
log(2)=2*atanh(1/3)>2/3.
"""
from fractions import Fraction


def poly_deriv(c):
    return [Fraction(i) * c[i] for i in range(1, len(c))]


def poly_eval(c, x):
    s = Fraction(0)
    for a in reversed(c):
        s = s * x + a
    return s


# ----------------------------------------------------------------------
# 1. Source-valid one-wall example: weights (1,4,6,9).
# ----------------------------------------------------------------------
weights = (1, 4, 6, 9)
fibers = {}
for mask in range(1 << len(weights)):
    total = sum(weights[i] for i in range(len(weights)) if (mask >> i) & 1)
    subset = tuple(i for i in range(len(weights)) if (mask >> i) & 1)
    fibers.setdefault(total, []).append(subset)

collisions = {s: subs for s, subs in fibers.items() if len(subs) > 1}
assert collisions == {10: [(1, 2), (0, 3)]}, collisions
print("UNIQUE_WALL_COLLISION=PASS")
print("weights=(1,4,6,9)")
print("collision_sum=10 subsets={(4,6),(1,9)}")

# For an equal-cardinality primitive r=s=2 merge:
# L(p) = 2 [p(1-p)]^2 log 2.
# The rational polynomial multiplying log 2 in L'' is
# 4 - 24 p + 24 p^2.
Lpp_coeff = [Fraction(4), Fraction(-24), Fraction(24)]
at_half = poly_eval(Lpp_coeff, Fraction(1, 2))
at_tenth = poly_eval(Lpp_coeff, Fraction(1, 10))
assert at_half == -2
assert at_tenth == Fraction(46, 25)
print("EQUAL_CARDINALITY_WALL_LPP=PASS")
print("Lpp=(4-24p+24p^2)*log(2)")
print("Lpp(1/2)=-2*log(2)<0")
print("Lpp(1/10)=(46/25)*log(2)>0")
print("CONSEQUENCE=no pointwise monotonicity of entropy curvature under a collision-wall merge")

# ----------------------------------------------------------------------
# 2. Exact failure of naive "each insertion entropy increment is concave".
# Old weights (1,2) are injective, so H_2 = 2 h.
# Add a new unit weight -> weights (1,1,2), with output probabilities
# q^3, 2 p q^2, p q, 2 p^2 q, p^3.
# Evaluate H'' exactly at p=1/2 as A + B log 2.
# ----------------------------------------------------------------------
qs = [
    [Fraction(1), Fraction(-3), Fraction(3), Fraction(-1)],  # (1-p)^3
    [Fraction(0), Fraction(2), Fraction(-4), Fraction(2)],   # 2p(1-p)^2
    [Fraction(0), Fraction(1), Fraction(-1)],                # p(1-p)
    [Fraction(0), Fraction(0), Fraction(2), Fraction(-2)],   # 2p^2(1-p)
    [Fraction(0), Fraction(0), Fraction(0), Fraction(1)],    # p^3
]
x = Fraction(1, 2)
vals = []
for c in qs:
    qp = poly_deriv(c)
    qpp = poly_deriv(qp)
    vals.append((poly_eval(c, x), poly_eval(qp, x), poly_eval(qpp, x)))

expected = [
    (Fraction(1, 8), Fraction(-3, 4), Fraction(3)),
    (Fraction(1, 4), Fraction(-1, 2), Fraction(-2)),
    (Fraction(1, 4), Fraction(0), Fraction(-2)),
    (Fraction(1, 4), Fraction(1, 2), Fraction(-2)),
    (Fraction(1, 8), Fraction(3, 4), Fraction(3)),
]
assert vals == expected

# q is 1/8 or 1/4, so log q = exponent * log 2 with exponent -3 or -2.
log2_exponents = []
for q, _, _ in vals:
    if q == Fraction(1, 8):
        log2_exponents.append(Fraction(-3))
    elif q == Fraction(1, 4):
        log2_exponents.append(Fraction(-2))
    else:
        raise AssertionError(q)

T_log2_coeff = sum(qpp * e for (q, qp, qpp), e in zip(vals, log2_exponents))
J = sum(qp * qp / q for q, qp, qpp in vals)
assert T_log2_coeff == -6
assert J == 11

# H_3'' = -(T+J) = -11 + 6 log 2.
# H_2'' = 2 h'' = -8 at p=1/2.
# Thus Delta'' = H_3''-H_2'' = -3 + 6 log 2.
assert Fraction(-11) - Fraction(-8) == -3
print("INSERTION_INCREMENT_EXACT_MIDPOINT=PASS")
print("H3pp(1/2)=-11+6*log(2)")
print("H2pp(1/2)=-8")
print("increment_pp(1/2)=-3+6*log(2)")
print("exact_bound: log(2)=2*atanh(1/3)>2/3")
print("therefore increment_pp(1/2)>1>0")
print("NAIVE_INCREMENT_CONCAVITY=REFUTED_AS_AUXILIARY_ROUTE")

print("ALL_EXACT_CHECKS_PASS")
