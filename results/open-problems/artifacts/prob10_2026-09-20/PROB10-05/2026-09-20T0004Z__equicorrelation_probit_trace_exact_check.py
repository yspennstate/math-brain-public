#!/usr/bin/env python3
from fractions import Fraction as F
from math import isqrt

# PROB10-05 exact self-check for the equicorrelation/probit trace envelope.
# All theorem-deciding finite comparisons are exact Fraction/integer arithmetic.
# Analytic ingredients proved in the report:
#   (i) Slepian comparison from the cyclic covariance to equicorrelation rho_adj;
#   (ii) Phi(x)Phi(-x) <= (1/4) exp(-x^2/2);
#   (iii) the one-factor moment identity for the equicorrelated four-orthant.
# The degree-18 quasimode bounds are inherited from the already archived
# HARD7-05 exact certificate chain; here they are used only as rational inputs.

r = F(7, 8)
s = F(24861, 25000)

# Exact softened four-cycle covariance, inherited/rederived algebraically.
a = (r + r**3) / (1 + r**4)
b = 2*r*r / (1 + r**4)
v = (1 + a) / (1 + r)
g = (1 + b + 2*a) / (2*(1+r))
h = (a + b) / (1 + r)
varV = s*v + (1-s)
rho_adj = s*g / varV
rho_opp = s*h / varV

assert a == F(6328,6497)
assert b == F(6272,6497)
assert v == F(6840,6497)
assert g == F(6780,6497)
assert h == F(6720,6497)
assert varV == F(170952323,162425000)
assert rho_adj == F(168557580,170952323)
assert rho_opp == F(167065920,170952323)
assert 0 < rho_opp < rho_adj < 1

# Equicorrelation matrix with off-diagonal rho_adj is positive definite.
# Its covariance entrywise dominates the cyclic matrix.
assert 1-rho_adj > 0
assert 1+3*rho_adj > 0

def atan_series_bounds(x, m):
    x = F(x)
    assert 0 <= x < 1
    ss = F(0)
    for k in range(m+1):
        ss += F((-1)**k, 2*k+1) * x**(2*k+1)
    nxt = F((-1)**(m+1), 2*(m+1)+1) * x**(2*(m+1)+1)
    return min(ss, ss+nxt), max(ss, ss+nxt)

# Machin: pi = 16 atan(1/5)-4 atan(1/239).
a5 = atan_series_bounds(F(1,5), 80)
a239 = atan_series_bounds(F(1,239), 25)
PI = (16*a5[0]-4*a239[1], 16*a5[1]-4*a239[0])
assert PI[0] > 3 and PI[1] < 4

DROOT = 10**70
def sqrt_bounds(x):
    x = F(x)
    assert x >= 0
    m = isqrt((DROOT*DROOT*x.numerator)//x.denominator)
    lo, hi = F(m,DROOT), F(m+1,DROOT)
    assert lo*lo <= x < hi*hi
    return lo, hi

def asin_bounds_pos(rho):
    rho = F(rho)
    assert 0 < rho < 1
    slo, shi = sqrt_bounds(1-rho*rho)
    tlo, thi = slo/rho, shi/rho
    assert thi < 1
    atan_lo, _ = atan_series_bounds(tlo, 120)
    _, atan_hi = atan_series_bounds(thi, 120)
    # asin(rho)=pi/2-atan(sqrt(1-rho^2)/rho).
    return PI[0]/2-atan_hi, PI[1]/2-atan_lo

asin_adj = asin_bounds_pos(rho_adj)

# Analytic one-factor bound proved in the report:
# p4_eq <= asin(rho)/pi + (1/16)*sqrt((1-rho)/(1+rho)).
sq_ratio = sqrt_bounds((1-rho_adj)/(1+rho_adj))
p4eq_upper = asin_adj[1]/PI[0] + sq_ratio[1]/16

pref = 1/(1-r**4)
trace_upper = pref*p4eq_upper
trace_cap = F(273011,250000)  # 1.092044
trace_margin = trace_cap-trace_upper
assert trace_margin > 0

# Inherited exact degree-18 quasimode coarsenings.
mu_lo = F(9116948312,10_000_000_000)
mu_hi = F(9116948313,10_000_000_000)
eps2_hi = F(47004495,100_000_000_000)

# New target theta*=16517/100000 = 0.16517.
# Since 4 theta*=16517/25000, x^25000 < r^16517 proves
# x < r^(4 theta*).
theta_target = F(16517,100000)
x = F(915557,1_000_000)
assert x**25000 < r**16517
assert x > mu_hi

# Fourth-trace tail separates every non-Perron spectral point.
beta = F(98743,125000)  # 0.789944
tail_margin = beta**4 - (trace_cap-x**4)
assert tail_margin > 0
assert mu_lo > beta

# Temple contradiction under lambda_1 >= r^(4 theta*).
temple_lower = (x-mu_hi)*(mu_lo-beta)
temple_margin = temple_lower-eps2_hi
assert temple_margin > 0

old_lower = F(103,625)
source_upper = F(1,4)
new_lower = theta_target
old_width = source_upper-old_lower
new_width = source_upper-new_lower
assert old_width == F(213,2500)
assert new_width == F(8483,100000)
assert old_width-new_width == F(37,100000)

print("rho_adj =", rho_adj, float(rho_adj))
print("rho_opp =", rho_opp, float(rho_opp))
print("equicorrelation dominance =", rho_adj >= rho_opp)
print("p4 equicorrelation upper <", float(p4eq_upper))
print("trace upper <", float(trace_upper))
print("trace cap =", trace_cap, float(trace_cap))
print("trace cap margin >", float(trace_margin))
print("x =", x, float(x), "power check =", x**25000 < r**16517)
print("beta =", beta, float(beta))
print("spectral-tail margin >", float(tail_margin))
print("Temple lower >", float(temple_lower))
print("Temple contradiction margin >", float(temple_margin))
print("old lower =", old_lower, float(old_lower))
print("new lower =", new_lower, float(new_lower))
print("new width =", new_width, float(new_width))
print("metric improvement =", old_width-new_width, float(old_width-new_width))
print("ALL_EXACT_CHECKS_PASS = True")
