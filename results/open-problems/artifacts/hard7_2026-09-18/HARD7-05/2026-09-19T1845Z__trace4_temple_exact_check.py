#!/usr/bin/env python3
from fractions import Fraction as F

# HARD7-05 exact self-check: four-cycle trace + fourth-moment Temple certificate.
# All theorem-deciding numerical comparisons in this file are exact Fraction arithmetic.
# The companion report proves
#   tr(T_{4/5}^4) = (625/369) * asin(41/42)/pi.
# The degree-24 mu/eps^2 envelopes below are conservative coarsenings of the
# already-executed exact fixed-point certificate archived at
#   2026-09-19T1745Z__edge_ritz_exact_check.py/.out
# (SCALE=10^55 there).  Thus this checker composes two exact certificates.


def atan_bounds(x, m):
    """Alternating-series enclosure for atan(x), 0<=x<1."""
    x = F(x)
    assert 0 <= x < 1
    s = F(0)
    for k in range(m + 1):
        s += F((-1) ** k, 2*k + 1) * x ** (2*k + 1)
    nxt = F((-1) ** (m + 1), 2*(m + 1) + 1) * x ** (2*(m + 1) + 1)
    return min(s, s + nxt), max(s, s + nxt)


# 1. Four-cycle loop covariance and adjacent edge-sum correlation.
r = F(4, 5)
g0 = (1 + r**4) / (1 - r**4)
g1 = (r + r**3) / (1 - r**4)
g2 = 2*r**2 / (1 - r**4)
rho = (g0 + 2*g1 + g2) / (2*(g0 + g1))
assert g0 == F(881, 369)
assert g1 == F(20, 9)
assert g2 == F(800, 369)
assert rho == F(41, 42)
trace_prefactor = 1 / (1-r**4)
assert trace_prefactor == F(625, 369)

# 2. Rigorous rational upper bound for asin(41/42)/pi.
# asin(41/42)=pi/2-atan(sqrt(83)/41).
# Take tL=1111/5000 < sqrt(83)/41 and bound atan(tL) from below.
tL = F(1111, 5000)
assert tL*tL < F(83, 41*41)

a5_lo, a5_hi = atan_bounds(F(1,5), 30)
a239_lo, a239_hi = atan_bounds(F(1,239), 12)
pi_lo = 16*a5_lo - 4*a239_hi
pi_hi = 16*a5_hi - 4*a239_lo
assert pi_lo > 3 and pi_hi < 4 and pi_lo < pi_hi

atan_t_lo, atan_t_hi = atan_bounds(tL, 30)
asin_ratio_upper = F(1,2) - atan_t_lo/pi_hi
t4_upper = F(72901, 100000)
ratio_target = t4_upper / trace_prefactor
assert asin_ratio_upper < ratio_target
# Therefore tr(T^4) < t4_upper.

# 3. Conservative envelopes inherited from the prior exact degree-24 Ritz output.
# Prior exact certificate gives mu=0.8740897351626367... and
# eps^2<0.00015495409397826696... .
mu_lo = F(874089735, 10**9)
mu_hi = F(874089736, 10**9)
eps2_hi = F(154955, 10**9)
assert mu_lo < mu_hi

# 4. Rational threshold below x_*=(4/5)^(3/5).
# xL^5 < (4/5)^3 = 64/125, hence xL<x_*.
xL = F(87468965, 10**8)
x_power_margin = F(64,125) - xL**5
assert x_power_margin > 0
assert xL > mu_hi

# 5. Fourth-moment tail cap.
# If lambda_1 >= x_* > xL, then every non-Perron eigenvalue satisfies
# |lambda_j|^4 < t4_upper-xL^4.
# Choose beta=0.6157 and certify beta^4 exceeds that tail.
beta = F(6157, 10000)
trace_tail_margin = beta**4 - (t4_upper - xL**4)
assert trace_tail_margin > 0
assert mu_lo > beta

# 6. Temple contradiction using the inherited exact residual.
# For self-adjoint T with all non-top eigenvalues <= beta < mu,
# eps^2 >= (lambda_1-mu)(mu-beta).
# Under lambda_1>=x_*>xL, the RHS is bounded below by the expression below.
temple_lower = (xL - mu_hi) * (mu_lo - beta)
temple_margin = temple_lower - eps2_hi
assert temple_margin > 0

# 7. Frozen metric arithmetic.
old_lower = F(37,250)
new_lower = F(3,20)
source_upper = F(1,4)
old_width = source_upper - old_lower
new_width = source_upper - new_lower
assert old_width == F(51,500)
assert new_width == F(1,10)
assert old_width-new_width == F(1,500)

print("r =", r)
print("loop covariances g0,g1,g2 =", g0, g1, g2)
print("adjacent edge-sum rho =", rho)
print("trace prefactor =", trace_prefactor)
print("atan test tL =", tL, float(tL))
print("pi interval =", float(pi_lo), float(pi_hi))
print("asin(41/42)/pi upper =", float(asin_ratio_upper))
print("ratio target =", float(ratio_target))
print("trace4 certified upper =", t4_upper, float(t4_upper))
print("xL =", xL, float(xL))
print("xL^5 margin below 64/125 =", x_power_margin, float(x_power_margin))
print("beta =", beta, float(beta))
print("fourth-moment tail margin =", trace_tail_margin, float(trace_tail_margin))
print("Temple lower =", temple_lower, float(temple_lower))
print("eps2 certified upper =", eps2_hi, float(eps2_hi))
print("Temple contradiction margin =", temple_margin, float(temple_margin))
print("old theta lower =", old_lower, float(old_lower))
print("new theta lower =", new_lower, float(new_lower))
print("old width =", old_width, float(old_width))
print("new width =", new_width, float(new_width))
print("width improvement =", old_width-new_width, float(old_width-new_width))
print("ALL_EXACT_CHECKS_PASS = True")