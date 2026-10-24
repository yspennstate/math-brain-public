#!/usr/bin/env python3
from fractions import Fraction as F
from math import isqrt, factorial

# PROB10-05 exact synthesis checker: finite even-Hermite ladder for the
# r=22/25 softened four-cycle. Theorem-deciding signs use exact Fraction /
# integer arithmetic and outward rational bounds for pi/arcsin.

DROOT = 10**190
N = 100

def atan_series_bounds(x, m):
    x = F(x)
    assert 0 <= x < 1
    s = F(0)
    for k in range(m + 1):
        s += F((-1)**k, 2*k + 1) * x**(2*k + 1)
    nxt = F((-1)**(m+1), 2*(m+1)+1) * x**(2*(m+1)+1)
    return min(s, s+nxt), max(s, s+nxt)

a5 = atan_series_bounds(F(1,5), 120)
a239 = atan_series_bounds(F(1,239), 40)
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
        return atan_series_bounds(t, 145)
    if t <= 2:
        u = (t-1)/(t+1)
        lo, hi = atan_series_bounds(u, 145)
        return PI[0]/4 + lo, PI[1]/4 + hi
    lo, hi = atan_series_bounds(1/t, 145)
    return PI[0]/2 - hi, PI[1]/2 - lo

def asin_bounds_pos(rho):
    rho = F(rho)
    assert 0 < rho < 1
    slo, shi = sqrt_bounds(1-rho*rho)
    tlo, thi = slo/rho, shi/rho
    alo = atan_point_bounds(tlo)[0]
    ahi = atan_point_bounds(thi)[1]
    return PI[0]/2 - ahi, PI[1]/2 - alo

# Exact comparator inherited from the previous all-lag covariance certificate.
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
kappa = 2*rho_adj/(1+rho_opp)
assert 0 < kappa < 1

# Re-certify the all-lag Lamperti covariance bridge for this exact comparator.
c = F(936901,1_000_000)
assert s*(1+r)/2 == c
radical_margins = []
for kk in (1,2):
    u = r**kk
    cap = c*r**(kk-1)
    AA = 6*u**5*cap + 2*u**10 - 5*u**6 - 5*u**4 + 2
    margin = AA*AA - 4*(1-u**4)**5
    assert AA > 0 and margin > 0
    radical_margins.append(margin)
# For k>=3, (1-z)^(5/2) <= 1-(5/2)z+(15/8)z^2 gives
# R(u) <= 5u/6+5u^3/8-u^5/3. The quotient by u is increasing
# on u^2<=r^6, so k=3 is the worst tail point.
deriv_margin = F(5,8) - F(2,3)*r**6
tail_endpoint = r*(F(5,6)+F(5,8)*r**6-F(1,3)*r**12)
assert deriv_margin > 0 and tail_endpoint < c

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

# Exact conditional second moment from the opposite-pair trivariate orthant.
Eh2_lo = -1 - 2*qopp_hi + 4*q2_lo
Eh2_hi = -1 - 2*qopp_lo + 4*q2_hi
assert 0 < Eh2_lo <= Eh2_hi < 1

# Hermite-ladder coefficients. Let E={|B|<q|X|}, alpha=atan(q), and
# J_m=int_0^alpha cos(t)^(2m) dt. Write
# J_m=A_m alpha + sqrt(1-rho_opp^2) B_m. The recurrence is exact.
A = [F(1)]
B = [F(0)]
for m in range(1, N+1):
    A.append(F(2*m-1,2*m)*A[-1])
    B.append(F(2*m-1,2*m)*B[-1]
             + F(1,4*m)*((1-rho_opp)/2)**(m-1))

def he_even_terms(n):
    # He_{2n}(x)=sum_{m=0}^n coeff_m x^(2m).
    nn = 2*n
    for m in range(n+1):
        j = n-m
        yield m, F(factorial(nn)*((-1)**j),
                   (2**j)*factorial(j)*factorial(2*m))

one_minus_rho2 = 1-rho_opp*rho_opp
a2sq_lo = []
a2sq_hi = []
Cvals = []
for n in range(1, N+1):
    alpha_coeff = F(0)
    Cn = F(0)
    for m, coeff in he_even_terms(n):
        fac = F(2**(m+1)*factorial(m))
        alpha_coeff += coeff*fac*A[m]
        Cn += coeff*fac*B[m]
    assert alpha_coeff == 0
    Cvals.append(Cn)
    numer = F(4)*one_minus_rho2*Cn*Cn/F(factorial(2*n))
    # a_{2n}^2 = numer/pi^2.
    a2sq_lo.append(numer/(PI[1]*PI[1]))
    a2sq_hi.append(numer/(PI[0]*PI[0]))
    assert 0 <= a2sq_lo[-1] <= a2sq_hi[-1]

# Parseval tail is nonnegative; certify this outwardly rather than merely rely
# on numerical cancellation.
sum_a_hi = sum(a2sq_hi, F(0))
parseval_tail_lo = Eh2_lo - qopp_hi*qopp_hi - sum_a_hi
assert parseval_tail_lo > 0

# Mehler + exact first N even coefficients:
# m4 <= k^(2N+2) Eh2 +(1-k^(2N+2))m^2
#       + sum a_{2n}^2 (k^(2n)-k^(2N+2)).
k_tail = kappa**(2*N+2)
m4_hi = k_tail*Eh2_hi + (1-k_tail)*qopp_hi*qopp_hi
for n, aa_hi in enumerate(a2sq_hi, 1):
    weight = kappa**(2*n) - k_tail
    assert weight >= 0
    m4_hi += aa_hi*weight

p4_hi = (1 + 4*qadj_hi + 2*qopp_hi + m4_hi)/16
trace_hi = p4_hi/(1-r**4)
trace_cap = F(56609,50000)  # 1.13218
assert trace_hi < trace_cap

# Same-operator degree-56 Perron data already certified by immutable checker
# blob b8f1e859678a900c8fe942383180580e1918db7c.
mu_lo = F(9155053441, 10_000_000_000)
mu_hi = F(9155053442, 10_000_000_000)
eps2_hi = F(270154, 10_000_000_000)
assert 0 < eps2_hi and mu_lo < mu_hi

# Candidate target and Kato-Temple separation.
theta = F(6217,36124)  # 0.1721016498726608...
# 4 theta reduces to 6217/9031.
assert 4*theta == F(6217,9031)
x = F(91575965,100_000_000)     # 0.91575965
beta = F(80926347,100_000_000) # 0.80926347
assert x**9031 < r**6217
assert x > mu_hi > mu_lo > beta > 0
spectral_tail_margin = beta**4 - (trace_cap - x**4)
temple_margin = (x-mu_hi)*(mu_lo-beta) - eps2_hi
assert spectral_tail_margin > 0
assert temple_margin > 0

incoming = F(1738,10099)
upper = F(1,4)
assert theta > incoming
assert upper-theta < upper-incoming

print('N =', N)
print('rho_adj =', float(rho_adj))
print('rho_opp =', float(rho_opp))
print('kappa =', float(kappa))
print('covariance k=1,2 squared margins =', [float(z) for z in radical_margins])
print('covariance tail c-margin =', float(c-tail_endpoint))
print('Eh2 interval =', float(Eh2_lo), float(Eh2_hi))
print('sum first-N Hermite squares upper =', float(sum_a_hi))
print('Parseval tail lower =', float(parseval_tail_lo))
print('C1,C2,C3 =', Cvals[:3])
print('trace outward upper =', float(trace_hi))
print('trace cap =', float(trace_cap), 'margin =', float(trace_cap-trace_hi))
print('theta =', theta, float(theta))
print('x =', float(x), 'beta =', float(beta))
print('spectral-tail margin =', float(spectral_tail_margin))
print('Temple margin =', float(temple_margin))
print('incoming lower =', incoming, float(incoming))
print('incoming width =', float(upper-incoming))
print('new lower =', float(theta), 'new width =', float(upper-theta))
print('source-level gain =', theta-incoming, float(theta-incoming))
print('ALL_EXACT_CHECKS_PASS = True')
