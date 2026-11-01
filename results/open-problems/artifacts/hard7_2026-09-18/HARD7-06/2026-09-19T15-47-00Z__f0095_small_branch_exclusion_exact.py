#!/usr/bin/env python3
"""Exact finite certificate for HARD7-06 small cavity-branch exclusion.

All sign decisions use fractions.Fraction.  The only transcendental quantity
needed is exp(-a_cap).  We obtain a rigorous lower bound by upper-bounding
exp(a_cap) with a positive Taylor series plus a geometric tail bound and then
reciprocating.
"""

from fractions import Fraction

D = Fraction(46865076662, 10**10)   # 4.6865076662 exactly
QCAP = Fraction(7, 50)              # 0.14; previous branch has q<0.1389
A = D * QCAP
N = 8


def exp_upper_positive(x: Fraction, n: int) -> Fraction:
    """Rigorous upper bound on exp(x), x>=0.

    Sum through x^n/n!.  For k>=n+1, successive term ratios are at most
    x/(n+2), so the tail beginning at term n+1 is bounded geometrically.
    """
    assert x >= 0
    s = Fraction(1)
    term = Fraction(1)
    for k in range(1, n + 1):
        term = term * x / k
        s += term
    next_term = term * x / (n + 1)
    ratio_cap = x / (n + 2)
    assert ratio_cap < 1
    return s + next_term / (1 - ratio_cap)


# Fixed-count extremizers for the cavity output T when all positive inputs are 1/2.
def t(k: int) -> Fraction:
    if k < 2:
        return Fraction(0)
    return Fraction(2**k - 2, 2**(k + 1) - 1)


assert t(2) == Fraction(2, 7)
assert t(3) == Fraction(2, 5)
assert all(t(k) < Fraction(1, 2) for k in range(4, 30))
assert Fraction(1389, 10000) < QCAP

# If K~Pois(a), use t_2=2/7, t_3=2/5, and t_k<1/2 for k>=4:
#   Mbar(a) = (2/7)P(K=2) + (2/5)P(K=3) + (1/2)P(K>=4)
#           = 1/2 - exp(-a) C(a).
C = (
    Fraction(1, 2)
    * (1 + A + A**2 / Fraction(2) + A**3 / Fraction(6))
    - Fraction(2, 7) * (A**2 / Fraction(2))
    - Fraction(2, 5) * (A**3 / Fraction(6))
)
assert C > 0

exp_a_upper = exp_upper_positive(A, N)
exp_minus_a_lower = Fraction(1, 1) / exp_a_upper
Mbar_upper = Fraction(1, 2) - exp_minus_a_lower * C

# Any nonzero cavity fixed point has mean m>1/d^2 because
# m <= (1-exp(-dm))^2 < d^2 m^2.
mean_lower = Fraction(1, 1) / (D * D)
margin = mean_lower - Mbar_upper
assert margin > 0

print("d =", D)
print("d_decimal =", float(D))
print("q_cap =", QCAP)
print("q_cap_decimal =", float(QCAP))
print("a_cap=d*q_cap =", A)
print("a_cap_decimal =", float(A))
print("t2 =", t(2))
print("t3 =", t(3))
print("exp(a_cap)_upper =", exp_a_upper)
print("exp(-a_cap)_lower =", exp_minus_a_lower)
print("C(a_cap) =", C)
print("Mbar_upper =", Mbar_upper)
print("Mbar_upper_decimal =", float(Mbar_upper))
print("1/d^2 =", mean_lower)
print("1/d^2_decimal =", float(mean_lower))
print("strict_margin =", margin)
print("strict_margin_decimal =", float(margin))
print("small_root_upper_0.1389_lt_qcap =", Fraction(1389, 10000) < QCAP)
print("ALL_EXACT_CHECKS_PASS = True")
