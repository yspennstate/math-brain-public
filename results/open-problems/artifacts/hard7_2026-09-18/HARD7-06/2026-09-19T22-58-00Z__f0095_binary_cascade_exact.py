#!/usr/bin/env python3
"""Exact certificate for HARD7-06 F0095 binary-cascade bounds.

All sign decisions use fractions.Fraction. Exponential signs are certified by
positive Taylor partial sums plus a geometric upper bound on the remaining
positive tail. No floating-point value is used in an assertion.
"""

from fractions import Fraction as F

D = F(46865076260769, 10**13)  # current certified degree 4.6865076260769
SMALL_LO = F(138, 1000)
SMALL_HI = F(139, 1000)
LARGE_LO = F(9319, 10000)
LARGE_HI = F(932, 1000)
QCAP = F(7, 50)  # 0.14


def exp_bounds(x: F, n: int = 40):
    """Return rigorous rational lower/upper bounds on exp(x), x>=0."""
    assert x >= 0
    term = F(1)
    partial = F(1)
    for k in range(1, n + 1):
        term = term * x / k
        partial += term
    next_term = term * x / (n + 1)
    ratio_cap = x / (n + 2)
    assert 0 <= ratio_cap < 1
    upper = partial + next_term / (1 - ratio_cap)
    return partial, upper


def h_sign(q: F) -> int:
    """Certify sign of h(q)=1-q-(1+D*q) exp(-D*q)."""
    exp_lo, exp_hi = exp_bounds(D * q)
    target = (1 + D * q) / (1 - q)
    # h(q)>0 iff exp(Dq)>target, h(q)<0 iff exp(Dq)<target.
    if exp_lo > target:
        return 1
    if exp_hi < target:
        return -1
    raise AssertionError("Taylor enclosure did not resolve sign")


# Current-degree scalar fixed-point root brackets.
assert h_sign(SMALL_LO) == -1
assert h_sign(SMALL_HI) == 1
assert h_sign(LARGE_LO) == 1
assert h_sign(LARGE_HI) == -1


# Re-certify the prior small-branch exclusion at this slightly smaller D.
# If K~Pois(a), the fixed-count cavity envelope is
# Mbar(a)=(2/7)P(K=2)+(2/5)P(K=3)+(1/2)P(K>=4)
#        =1/2-exp(-a) C(a).
A = D * QCAP
C = (
    F(1, 2) * (1 + A + A**2 / F(2) + A**3 / F(6))
    - F(2, 7) * (A**2 / F(2))
    - F(2, 5) * (A**3 / F(6))
)
assert C > 0
EXP_A_UPPER = exp_bounds(A, 10)[1]
EXP_MINUS_A_LOWER = 1 / EXP_A_UPPER
MBAR_UPPER = F(1, 2) - EXP_MINUS_A_LOWER * C
MEAN_LOWER = 1 / (D * D)
assert MBAR_UPPER < MEAN_LOWER


# On the surviving large branch, the fixed-point zero-atom equation removes
# the exponential from c*q:
#   c*q = D^2 q(1-q) / (2(1+Dq)).
def cq_from_q(q: F) -> F:
    return D * D * q * (1 - q) / (2 * (1 + D * q))


CQ_AT_LO = cq_from_q(LARGE_LO)
CQ_AT_HI = cq_from_q(LARGE_HI)

# q -> cq is strictly decreasing throughout the certified large-root box:
# derivative sign is sign(1-2q-Dq^2).
assert 1 - 2 * LARGE_LO - D * LARGE_LO**2 < 0
assert CQ_AT_HI < CQ_AT_LO

# beta_bin=log(cq)/log(2/3). Since log(2/3)<0,
# beta_bin>5.03 iff cq<(2/3)^5.03, and beta_bin<5.04 iff
# cq>(2/3)^5.04. Clear rational exponents by raising to powers 100 and 25.
assert CQ_AT_LO**100 < F(2, 3)**503
assert CQ_AT_HI**25 > F(2, 3)**126

# In particular beta_bin<6, so every s=6 negative moment is forced infinite.
assert CQ_AT_HI > F(2, 3)**6

print("d_exact =", D)
print("d_decimal =", float(D))
print("small_root_endpoint_signs =", h_sign(SMALL_LO), h_sign(SMALL_HI))
print("large_root_endpoint_signs =", h_sign(LARGE_LO), h_sign(LARGE_HI))
print("small_branch_Mbar_upper =", float(MBAR_UPPER))
print("small_branch_1_over_d2 =", float(MEAN_LOWER))
print("small_branch_strict_margin =", float(MEAN_LOWER - MBAR_UPPER))
print("cq_large_upper_at_qlo =", float(CQ_AT_LO))
print("cq_large_lower_at_qhi =", float(CQ_AT_HI))
print("beta_binary_interval_certified = (5.03, 5.04)")
print("sixth_negative_moment_forced_infinite =", CQ_AT_HI > F(2, 3)**6)
print("ALL_EXACT_CHECKS_PASS = True")
