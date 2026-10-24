#!/usr/bin/env python3
from fractions import Fraction as F
from math import isqrt

# PROB10-05 exact synthesis checker: sharpen the r=22/25 softened four-cycle
# trace by exploiting the even Hermite expansion of the opposite-pair sign
# observable.  All theorem-deciding signs below use exact Fraction/integer
# arithmetic plus outward rational bounds for pi/arcsin.
#
# The degree-56 quasimode constants mu_lo, mu_hi, eps2_hi below were already
# certified for this exact (r,s) operator by immutable checker blob
# b8f1e859678a900c8fe942383180580e1918db7c
# (2026-09-20T1157Z__mesh22_25_exact_check.py).  This checker certifies the new
# trace estimate and its Kato-Temple synthesis; it does not silently import a
# spectral number from a different operator.

DROOT = 10**180

def atan_series_bounds(x, m):
    x = F(x)
    assert 0 <= x < 1
    s = F(0)
    for k in range(m + 1):
        s += F((-1)**k, 2*k + 1) * x**(2*k + 1)
    nxt = F((-1)**(m+1), 2*(m+1)+1) * x**(2*(m+1)+1)
    return min(s, s+nxt), max(s, s+nxt)

a5 = atan_series_bounds(F(1,5), 110)
a239 = atan_series_bounds(F(1,239), 35)
PI = (16*a5[0] - 4*a239[1], 16*a5[1] - 4*a239[0])

def sqrt_bounds(x):
    x = F(x)
    assert x >= 0
    if x == 0:
        return F(0), F(0)
    m = isqrt((DROOT*DROOT*x.numerator)//x.denominator)
    lo, hi = F(m,DROOT), F(m+1,DROOT)
    assert lo*lo <= x < hi*hi
    return lo, hi

def atan_point_bounds(t):
    t = F(t)
    if t < 0:
        lo, hi = atan_point_bounds(-t)
        return -hi, -lo
    if t <= F(1,2):
        return atan_series_bounds(t, 130)
    if t <= 2:
        u = (t-1)/(t+1)
        lo, hi = atan_series_bounds(u, 130)
        return PI[0]/4 + lo, PI[1]/4 + hi
    lo, hi = atan_series_bounds(1/t, 130)
    return PI[0]/2 - hi, PI[1]/2 - lo

def asin_bounds_pos(rho):
    rho = F(rho)
    assert 0 < rho < 1
    slo, shi = sqrt_bounds(1-rho*rho)
    tlo, thi = slo/rho, shi/rho
    alo = atan_point_bounds(tlo)[0]
    ahi = atan_point_bounds(thi)[1]
    return PI[0]/2 - ahi, PI[1]/2 - alo

# Exact softened comparator already admitted and all-lag certified in the
# preceding immutable PROB10-05 report/checker.
r = F(22,25)
s = F(936901,940000)
a = (r+r**3)/(1+r**4)
b = 2*r*r/(1+r**4)
v = (1+a)/(1+r)
g = (1+b+2*a)/(2*(1+r))
h = (a+b)/(1+r)
varV = s*v + (1-s)
rho_adj = s*g/varV
rho_opp = s*h/varV
assert 0 < rho_opp < rho_adj < 1

# Orthogonal opposite-pair coordinates show that the normalized shared modes
# have correlation kappa.  For F0=sgn(V0)sgn(V2), conditioning on the shared
# mode X gives h(X)=4 Phi(c|X|)-3, an even function.  Therefore all centered
# Hermite coefficients have degree >=2, and the Gaussian noise operator gives
#   E[F0 F1] <= m^2 + kappa^2 (E[h^2]-m^2).
kappa = 2*rho_adj/(1+rho_opp)
assert 0 < kappa < 1

asin_adj = asin_bounds_pos(rho_adj)
asin_opp = asin_bounds_pos(rho_opp)
rho_two = (1+rho_opp)/2
asin_two = asin_bounds_pos(rho_two)

qadj_lo = 2*asin_adj[0]/PI[1]
qadj_hi = 2*asin_adj[1]/PI[0]
qopp_lo = 2*asin_opp[0]/PI[1]
qopp_hi = 2*asin_opp[1]/PI[0]
q2_lo = 2*asin_two[0]/PI[1]
q2_hi = 2*asin_two[1]/PI[0]
assert 0 < qopp_lo <= qopp_hi < qadj_lo <= qadj_hi < 1

# Exact conditional second moment.  If p(X)=Phi(c|X|), then a centered
# trivariate orthant formula with correlations d,d,d^2 and d^2=(1+rho_opp)/2
# gives
#   E[h(X)^2] = -1 - 2 qopp + 4 q2,
# q2=(2/pi) asin((1+rho_opp)/2).
Eh2_lo = -1 - 2*qopp_hi + 4*q2_lo
Eh2_hi = -1 - 2*qopp_lo + 4*q2_hi
assert 0 < Eh2_lo <= Eh2_hi < 1

m4_hi = kappa*kappa*Eh2_hi + (1-kappa*kappa)*qopp_hi*qopp_hi
p4_hi = (1 + 4*qadj_hi + 2*qopp_hi + m4_hi)/16
trace_hi = p4_hi/(1-r**4)
trace_cap = F(56721,50000)   # 1.13442
assert trace_hi < trace_cap

# Certified degree-56 data for this same operator, from immutable prior checker.
mu_lo = F(9155053441, 10_000_000_000)
mu_hi = F(9155053442, 10_000_000_000)
eps2_hi = F(270154, 10_000_000_000)
assert 0 < eps2_hi and mu_lo < mu_hi

# New target.  4 theta = 6952/10099, so x < r^(4 theta) is the exact
# integer-power inequality x^10099 < r^6952.
theta = F(1738,10099)
x = F(183152435,200_000_000)  # 0.915762175
beta = F(202579,250000)        # 0.810316
assert x**10099 < r**6952
assert x > mu_hi > mu_lo > beta > 0

# If lambda_1 >= r^(4 theta) > x, the fourth-trace cap forces every
# non-Perron spectral point to have |lambda_j|<beta.  Kato-Temple then forces
# eps^2 >= (lambda_1-mu)(mu-beta), contradicted by the certified residual.
spectral_tail_margin = beta**4 - (trace_cap - x**4)
temple_margin = (x-mu_hi)*(mu_lo-beta) - eps2_hi
assert spectral_tail_margin > 0
assert temple_margin > 0

incoming = F(43013,250000)
upper = F(1,4)
assert theta > incoming
assert upper-theta < upper-incoming

print('rho_adj =', float(rho_adj))
print('rho_opp =', float(rho_opp))
print('kappa =', float(kappa))
print('Eh2 interval =', float(Eh2_lo), float(Eh2_hi))
print('trace outward upper =', float(trace_hi))
print('trace cap =', float(trace_cap), 'margin =', float(trace_cap-trace_hi))
print('theta =', theta, float(theta))
print('x =', float(x), 'beta =', float(beta))
print('spectral-tail margin =', float(spectral_tail_margin))
print('Temple margin =', float(temple_margin))
print('incoming lower =', float(incoming), 'incoming width =', float(upper-incoming))
print('new lower =', float(theta), 'new width =', float(upper-theta))
print('source-level gain =', float(theta-incoming))
print('ALL_EXACT_CHECKS_PASS = True')
