#!/usr/bin/env python3
from fractions import Fraction as F
from math import isqrt, comb, factorial

# HARD7-05 exact self-check for the r=q=22/25 edge-smoothed comparator.
# Every theorem-deciding numerical comparison uses exact integer/Fraction
# arithmetic or outward-rounded rational fixed-point intervals.
#
# It certifies:
#   (i) all-lag covariance domination of the H=1/4 Lamperti samples by the
#       edge-smoothed AR(1) comparator at r=q=22/25, using the previously
#       proved source envelope R(u)<=u for u<=287831/500000;
#   (ii) exact-interval Rayleigh/residual bounds for a frozen degree-18 trial;
#   (iii) a rational upper bound on tr(T_r^4);
#   (iv) Temple separation implying ||T_r|| < r^(3223/5000);
# hence the companion proof obtains theta_{2,1/4} > 3223/20000.

DEG = 18
SCALE = 10**45
DROOT = 10**60

# Frozen integer monomial trial, selected in exploratory Hermite/Ritz work.
PC = [
    475070328519883840,
    -1113365624702254592,
    338355124680512320,
    486984559837217408,
    -73074273788264896,
    -184395570674225728,
    11142920418922446,
    35806488273325944,
    -1000511422193268,
    -3754116414122802,
    51951802624470,
    218956419520117,
    -1519937907692,
    -7024152844024,
    23195558022,
    114707552620,
    -147987204,
    -737965295,
    112147,
]
assert len(PC) == DEG + 1

# ---------------------------------------------------------------------------
# Exact rational source-covariance tests at the four exceptional lags.
# The inherited source identity is
# R(u)-u = (1-u^2)/(6u^5) *
#   [-P(u^2)+2(1+u^2)(1-u^4)^(3/2)]
# with P(z)=2+2z-3z^2-2z^3-2z^4.
# For a rational cap c>u, R(u)<c follows from T=P(u^2)+D>0 and
# 4(1+u^2)^2(1-u^4)^3<T^2, where D=6u^5(c-u)/(1-u^2).
# ---------------------------------------------------------------------------
r = F(22, 25)
c1 = F(1 + r, 2)
r0 = F(287831, 500000)

def P(z):
    return 2 + 2*z - 3*z*z - 2*z**3 - 2*z**4

cov_margins = []
for k in range(1, 5):
    u = r**k
    cap = c1 * r**(k-1)
    assert cap > u
    z = u*u
    D = 6*u**5*(cap-u)/(1-u*u)
    T = P(z) + D
    margin = T*T - 4*(1+z)**2*(1-z*z)**3
    assert T > 0
    assert margin > 0
    cov_margins.append(margin)

assert r**5 < r0
assert c1 / r == F(47, 44) > 1

# ---------------------------------------------------------------------------
# Outward fixed-point interval arithmetic.
# ---------------------------------------------------------------------------
def floor_frac(x):
    return x.numerator // x.denominator

def ceil_frac(x):
    return -((-x.numerator) // x.denominator)

def C(x):
    x = F(x)
    y = x * SCALE
    return floor_frac(y), ceil_frac(y)

def I_from_bounds(lo, hi):
    return floor_frac(lo*SCALE), ceil_frac(hi*SCALE)

def iadd(a, b):
    return a[0] + b[0], a[1] + b[1]

def ineg(a):
    return -a[1], -a[0]

def isub(a, b):
    return iadd(a, ineg(b))

def imul(a, b):
    vals = (a[0]*b[0], a[0]*b[1], a[1]*b[0], a[1]*b[1])
    lo, hi = min(vals), max(vals)
    return lo // SCALE, -((-hi) // SCALE)

def iscale(a, q):
    q = F(q)
    if q >= 0:
        lo, hi = F(a[0])*q, F(a[1])*q
    else:
        lo, hi = F(a[1])*q, F(a[0])*q
    return floor_frac(lo), ceil_frac(hi)

def iinv(a):
    assert a[0] > 0
    return (
        floor_frac(F(SCALE*SCALE, a[1])),
        ceil_frac(F(SCALE*SCALE, a[0])),
    )

def idiv(a, b):
    return imul(a, iinv(b))

def interval_float(a):
    return a[0]/SCALE, a[1]/SCALE

def atan_series_bounds(x, m):
    x = F(x)
    assert 0 <= x < 1
    s = F(0)
    for k in range(m + 1):
        s += F((-1)**k, 2*k+1) * x**(2*k+1)
    nxt = F((-1)**(m+1), 2*(m+1)+1) * x**(2*(m+1)+1)
    return min(s, s+nxt), max(s, s+nxt)

a5 = atan_series_bounds(F(1,5), 70)
a239 = atan_series_bounds(F(1,239), 20)
PI = (16*a5[0]-4*a239[1], 16*a5[1]-4*a239[0])

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
        return atan_series_bounds(t, 80)
    if t <= 2:
        u = (t-1)/(t+1)
        lo, hi = atan_series_bounds(u, 80)
        return PI[0]/4+lo, PI[1]/4+hi
    lo, hi = atan_series_bounds(1/t, 80)
    return PI[0]/2-hi, PI[1]/2-lo

sqrt2pi = (
    sqrt_bounds(2*PI[0])[0],
    sqrt_bounds(2*PI[1])[1],
)
tI = I_from_bounds(1/sqrt2pi[1], 1/sqrt2pi[0])
piI = I_from_bounds(*PI)

def std_moment(k):
    if k % 2:
        return 0
    out = 1
    for j in range(1, k, 2):
        out *= j
    return out

def trunc_negative_moment(k):
    if k % 2 == 0:
        return C(F(std_moment(k), 2))
    m = (k-1)//2
    return iscale(tI, -(2**m)*factorial(m))

def add_to(poly, key, val):
    poly[key] = iadd(poly.get(key, (0,0)), val)

def powers(x):
    out = [C(1)]
    for _ in range(DEG):
        out.append(imul(out[-1], x))
    return out

# ---------------------------------------------------------------------------
# q=<f,f> and m=<f,Tf>.
# For corr(X,Y)=r=22/25, put independent A,D~N(0,1):
#   X = sqrt(47/50) A + sqrt(3/50) D,
#   Y = sqrt(47/50) A - sqrt(3/50) D.
# Then X+Y<0 iff A<0.
# ---------------------------------------------------------------------------
sqrt_a = sqrt_bounds(F(47,50))
sqrt_d = sqrt_bounds(F(3,50))
aI = I_from_bounds(*sqrt_a)
dI = I_from_bounds(*sqrt_d)

q_exact = 0
for i, ci in enumerate(PC):
    for j, cj in enumerate(PC):
        q_exact += ci*cj*std_moment(i+j)
qI = C(q_exact)
assert qI[0] > 0

aP = powers(aI)
dP = powers(dI)
fX, fY = {}, {}
for k, pk in enumerate(PC):
    for ap in range(k+1):
        dp = k-ap
        base = imul(aP[ap], dP[dp])
        coeff = pk*comb(k,ap)
        add_to(fX, (ap,dp), iscale(base, coeff))
        add_to(fY, (ap,dp), iscale(base, coeff*((-1)**dp)))

mI = (0,0)
for (ap,dp), ca in fX.items():
    for (bp,ep), cb in fY.items():
        md = std_moment(dp+ep)
        if md == 0:
            continue
        term = imul(imul(ca,cb), trunc_negative_moment(ap+bp))
        mI = iadd(mI, iscale(term, md))

muI = idiv(mI, qI)
assert muI[0] > 0

# ---------------------------------------------------------------------------
# n=<Tf,Tf>=<f,T^2 f>.
# Let normalized edge sums
#   A=(X+Y)/sqrt(2(1+r)), B=(Y+Z)/sqrt(2(1+r)).
# Then corr(A,B)=c=(1+r)/2=47/50. Conditional on A,B,
#   X = alpha A + beta B + E,
#   Z = beta A + alpha B + E,
# where alpha=(144/97)sqrt(47/50), beta=-(50/97)sqrt(47/50),
# and E~N(0,3/97) is independent.
# Positive-quadrant moments Q[m,n] are generated by Gaussian
# integration-by-parts recurrences.
# ---------------------------------------------------------------------------
MAX = 2*DEG + 2
EXT = 3*DEG + 12
c = F(47,50)
s2 = 1-c*c
assert s2 == F(291,2500)
sqrt_s2 = sqrt_bounds(s2)
sI = I_from_bounds(*sqrt_s2)
ratioI = I_from_bounds(c/sqrt_s2[1], c/sqrt_s2[0])

asin_c = (
    atan_point_bounds(c/sqrt_s2[1])[0],
    atan_point_bounds(c/sqrt_s2[0])[1],
)
asinI = I_from_bounds(*asin_c)

B = [None]*EXT
B[0] = iscale(imul(sI,tI), F(1,2))
B[1] = iscale(imul(tI,tI), s2)
for k in range(2,EXT):
    B[k] = iscale(B[k-2], F(k-1)*s2)

A = [None]*EXT
A[0] = iadd(C(F(1,4)), iscale(idiv(asinI,piI), F(1,2)))
A[1] = iadd(iscale(tI,F(1,2)), imul(ratioI,B[0]))
for k in range(2,EXT):
    A[k] = iadd(iscale(A[k-2],k-1), imul(ratioI,B[k-1]))

Q = [[None]*EXT for _ in range(MAX+1)]
for n in range(EXT):
    Q[0][n] = A[n]
for n in range(EXT-1):
    Q[1][n] = iadd(iscale(A[n+1],c), imul(sI,B[n]))
for mm in range(2,MAX+1):
    for n in range(EXT-mm):
        Q[mm][n] = iadd(
            iscale(Q[mm-1][n+1],c),
            iscale(Q[mm-2][n],F(mm-1)*s2),
        )

# Exact interval symmetry consistency for every Q moment used.
for i in range(2*DEG+1):
    for j in range(2*DEG+1-i):
        qi, qj = Q[i][j], Q[j][i]
        assert max(qi[0],qj[0]) <= min(qi[1],qj[1])

def q_negative(a,b):
    z = Q[a][b]
    return ineg(z) if (a+b)%2 else z

alpha = iscale(aI, F(144,97))
beta_cond = iscale(aI, F(-50,97))
alphaP = powers(alpha)
betaP = powers(beta_cond)

FX = [{} for _ in range(DEG+1)]
FZ = [{} for _ in range(DEG+1)]
for k, pk in enumerate(PC):
    fk = factorial(k)
    for e in range(k+1):
        rem = k-e
        for ap in range(rem+1):
            bp = rem-ap
            mult = fk // (factorial(ap)*factorial(bp)*factorial(e))
            coeff = pk*mult
            add_to(FX[e], (ap,bp), iscale(imul(alphaP[ap],betaP[bp]), coeff))
            add_to(FZ[e], (ap,bp), iscale(imul(betaP[ap],alphaP[bp]), coeff))

nI = (0,0)
pair_count = 0
for e in range(DEG+1):
    for h in range(DEG+1):
        kk = e+h
        moment = std_moment(kk)
        if moment == 0:
            continue
        subtotal = (0,0)
        for (ap,bp), ca in FX[e].items():
            for (cp,dp), cb in FZ[h].items():
                pair_count += 1
                subtotal = iadd(
                    subtotal,
                    imul(imul(ca,cb), q_negative(ap+cp,bp+dp)),
                )
        subtotal = iscale(subtotal, F(moment)*F(3,97)**(kk//2))
        nI = iadd(nI, subtotal)

nNormI = idiv(nI, qI)
eps2I = isub(nNormI, imul(muI,muI))
assert eps2I[0] > 0

# Coarsen the exact intervals for a transparent final Temple certificate.
mu_lo = F(9155528, 10_000_000)
mu_hi = F(9155531, 10_000_000)
eps2_hi = F(566, 1_000_000)
assert muI[0] > floor_frac(mu_lo*SCALE)
assert muI[1] < ceil_frac(mu_hi*SCALE)
assert eps2I[1] < ceil_frac(eps2_hi*SCALE)

# ---------------------------------------------------------------------------
# Exact trace-four upper bound.
# General identity:
# tr(T_r^4)=1/(1-r^4) * asin(rho)/pi,
# rho=((1+r)(1+r^2))/(2(1+r^3)).
# At r=22/25, rho=1109/1118 and
# asin(rho)=pi/2-atan(3*sqrt(2227)/1109).
# ---------------------------------------------------------------------------
rho = ((1+r)*(1+r*r))/(2*(1+r**3))
pref = 1/(1-r**4)
assert rho == F(1109,1118)
assert pref == F(390625,156369)

# Rational lower bound on 3*sqrt(2227)/1109.
tL = F(1276585, 10_000_000)
assert tL*tL < F(9*2227,1109**2)
atan_t_lo, atan_t_hi = atan_series_bounds(tL, 30)
asin_ratio_upper = F(1,2) - atan_t_lo/PI[1]
trace4_upper = F(229617,200000)  # 1.148085
assert asin_ratio_upper < trace4_upper/pref

# ---------------------------------------------------------------------------
# Fourth-moment spectral tail + Temple contradiction.
# Target theta_* = 3223/20000, so x_* = r^(4 theta_*)=r^(3223/5000).
# Choose xL=9209/10000 and certify xL^5000 < r^3223, hence xL<x_*.
# If lambda_1>=x_*, trace(T^4) bounds all non-Perron eigenvalues.
# ---------------------------------------------------------------------------
theta_target = F(3223,20000)
xL = F(9209,10000)
assert xL**5000 < r**3223
assert xL > mu_hi

beta = F(8093,10000)
trace_tail_margin = beta**4 - (trace4_upper - xL**4)
assert trace_tail_margin > 0
assert mu_lo > beta

temple_lower = (xL-mu_hi)*(mu_lo-beta)
temple_margin = temple_lower - eps2_hi
assert temple_margin > 0

# Frozen metric arithmetic.
old_lower = F(3,20)
new_lower = theta_target
source_upper = F(1,4)
old_width = source_upper-old_lower
new_width = source_upper-new_lower
assert old_width == F(1,10)
assert new_width == F(1777,20000)
assert old_width-new_width == F(223,20000)

print("r=q =", r, float(r))
print("edge prefactor (1+r)/2 =", c1, float(c1))
for i, margin in enumerate(cov_margins, 1):
    print(f"lag {i} squared covariance margin =", margin, float(margin))
print("r^5 =", r**5, float(r**5), "< r0 =", r0, float(r0))
print("tail comparator/source-envelope ratio =", c1/r, float(c1/r))
print("trial degree =", DEG)
print("pair_count =", pair_count)
print("mu exact interval =", interval_float(muI))
print("eps2 exact interval =", interval_float(eps2I))
print("mu coarse =", mu_lo, mu_hi)
print("eps2 coarse upper =", eps2_hi)
print("trace4 rho =", rho, float(rho))
print("trace4 prefactor =", pref, float(pref))
print("asin/pi rigorous upper =", float(asin_ratio_upper))
print("trace4 certified upper =", trace4_upper, float(trace4_upper))
print("xL =", xL, float(xL))
print("threshold exact power check xL^5000 < r^3223 =", xL**5000 < r**3223)
print("beta =", beta, float(beta))
print("trace tail margin =", trace_tail_margin, float(trace_tail_margin))
print("Temple lower =", temple_lower, float(temple_lower))
print("Temple contradiction margin =", temple_margin, float(temple_margin))
print("old theta lower =", old_lower, float(old_lower))
print("new theta lower =", new_lower, float(new_lower))
print("old width =", old_width, float(old_width))
print("new width =", new_width, float(new_width))
print("width improvement =", old_width-new_width, float(old_width-new_width))
print("ALL_EXACT_CHECKS_PASS = True")
