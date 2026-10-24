#!/usr/bin/env python3
from fractions import Fraction as F
from math import isqrt, comb, factorial

# HARD7-05 exact self-check for the r=4/5 edge-smoothed Gaussian comparator.
# The theorem-deciding calculations use exact integer/fixed-point interval arithmetic.
# It certifies
#   ||T_{4/5}|| < 701/800
# and hence, using the already-certified all-lag Slepian comparison at q=r=4/5,
#   theta_{2,1/4} > 37/250 = 0.148.

DEG = 24
SCALE = 10**55
DROOT = 10**70

# Fixed integer trial polynomial f(x)=sum_{k=0}^{24} PC[k] x^k.
# It was selected by a degree-24 Hermite/Ritz reconnaissance and then frozen.
PC = [
    601716466463396560,
    -1161082935847059089,
    64741600028092416,
    646043639354741501,
    140690660426611064,
    -318116949117253776,
    -79827783402180372,
    87798604874975957,
    20614790861843223,
    -14234596064767693,
    -3012022328878110,
    1419460589875966,
    269496925366968,
    -89554541808439,
    -15322036208832,
    3610117135887,
    560282931279,
    -91988880341,
    -13038897567,
    1422952887,
    185395311,
    -12115086,
    -1459361,
    43287,
    4846,
]
assert len(PC) == DEG + 1

# ---------------------------------------------------------------------------
# Exact fixed-point intervals.  An interval (L,U) represents [L/SCALE,U/SCALE].
# Every product/division is rounded outward using integer arithmetic.
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
    return floor_frac(lo * SCALE), ceil_frac(hi * SCALE)


def iadd(a, b):
    return a[0] + b[0], a[1] + b[1]


def ineg(a):
    return -a[1], -a[0]


def isub(a, b):
    return iadd(a, ineg(b))


def imul(a, b):
    vals = (a[0] * b[0], a[0] * b[1], a[1] * b[0], a[1] * b[1])
    lo, hi = min(vals), max(vals)
    return lo // SCALE, -((-hi) // SCALE)


def iscale(a, q):
    q = F(q)
    if q >= 0:
        lo, hi = F(a[0]) * q, F(a[1]) * q
    else:
        lo, hi = F(a[1]) * q, F(a[0]) * q
    return floor_frac(lo), ceil_frac(hi)


def iinv(a):
    assert a[0] > 0
    lo = F(SCALE * SCALE, a[1])
    hi = F(SCALE * SCALE, a[0])
    return floor_frac(lo), ceil_frac(hi)


def idiv(a, b):
    return imul(a, iinv(b))


def mid_float(a):
    return (a[0] + a[1]) / (2 * SCALE)


def width_float(a):
    return (a[1] - a[0]) / SCALE


# ---------------------------------------------------------------------------
# Exact elementary constants: pi, square roots, asin(9/10), 1/sqrt(2*pi).
# ---------------------------------------------------------------------------

def atan_series_bounds(x, m):
    x = F(x)
    s = F(0)
    for k in range(m + 1):
        s += F((-1) ** k, 2 * k + 1) * x ** (2 * k + 1)
    nxt = F((-1) ** (m + 1), 2 * (m + 1) + 1) * x ** (2 * (m + 1) + 1)
    return min(s, s + nxt), max(s, s + nxt)


a5 = atan_series_bounds(F(1, 5), 80)
a239 = atan_series_bounds(F(1, 239), 25)
PI = (16 * a5[0] - 4 * a239[1], 16 * a5[1] - 4 * a239[0])


def sqrt_bounds(x):
    x = F(x)
    assert x >= 0
    if x == 0:
        return F(0), F(0)
    m = isqrt((DROOT * DROOT * x.numerator) // x.denominator)
    lo, hi = F(m, DROOT), F(m + 1, DROOT)
    assert lo * lo <= x < hi * hi
    return lo, hi


def atan_point_bounds(t):
    t = F(t)
    if t < 0:
        lo, hi = atan_point_bounds(-t)
        return -hi, -lo
    if t <= F(1, 2):
        return atan_series_bounds(t, 90)
    if t <= 2:
        u = (t - 1) / (t + 1)
        lo, hi = atan_series_bounds(u, 90)
        return PI[0] / 4 + lo, PI[1] / 4 + hi
    lo, hi = atan_series_bounds(1 / t, 90)
    return PI[0] / 2 - hi, PI[1] / 2 - lo


sqrt19 = sqrt_bounds(19)
asin09 = (
    atan_point_bounds(F(9) / sqrt19[1])[0],
    atan_point_bounds(F(9) / sqrt19[0])[1],
)
sqrt10 = sqrt_bounds(10)
inv_sqrt10 = I_from_bounds(1 / sqrt10[1], 1 / sqrt10[0])
sI = I_from_bounds(sqrt19[0] / 10, sqrt19[1] / 10)
aI = I_from_bounds(F(9) / sqrt19[1], F(9) / sqrt19[0])
sqrt2pi = (sqrt_bounds(2 * PI[0])[0], sqrt_bounds(2 * PI[1])[1])
tI = I_from_bounds(1 / sqrt2pi[1], 1 / sqrt2pi[0])
piI = I_from_bounds(*PI)
asin09I = I_from_bounds(*asin09)


# ---------------------------------------------------------------------------
# Gaussian moments.
# ---------------------------------------------------------------------------

def std_moment(k):
    if k % 2:
        return 0
    out = 1
    for j in range(1, k, 2):
        out *= j
    return out


def trunc_negative_moment(k):
    # E[Z^k 1_{Z<0}], Z standard normal.
    if k % 2 == 0:
        return C(F(std_moment(k), 2))
    m = (k - 1) // 2
    return iscale(tI, -(2 ** m) * factorial(m))


def add_to(poly, key, val):
    poly[key] = iadd(poly.get(key, (0, 0)), val)


# ---------------------------------------------------------------------------
# q=<f,f> and m=<f,Tf>.
# For r=4/5 rotate a correlated pair (X,Y) as
#   X=(3A+D)/sqrt(10),  Y=(3A-D)/sqrt(10),
# with A,D independent N(0,1), and X+Y<0 iff A<0.
# ---------------------------------------------------------------------------
q_exact = 0
for i, ci in enumerate(PC):
    for j, cj in enumerate(PC):
        q_exact += ci * cj * std_moment(i + j)
qI = C(q_exact)
assert qI[0] > 0

pow_inv_sqrt10 = [C(1)]
for _ in range(DEG):
    pow_inv_sqrt10.append(imul(pow_inv_sqrt10[-1], inv_sqrt10))

fX, fY = {}, {}
for k, pk in enumerate(PC):
    fac = iscale(pow_inv_sqrt10[k], pk)
    for ap in range(k + 1):
        dp = k - ap
        coeff = comb(k, ap) * (3 ** ap)
        add_to(fX, (ap, dp), iscale(fac, coeff))
        add_to(fY, (ap, dp), iscale(fac, coeff * ((-1) ** dp)))

mI = (0, 0)
for (ap, dp), ca in fX.items():
    for (bp, ep), cb in fY.items():
        md = std_moment(dp + ep)
        if md == 0:
            continue
        term = imul(imul(ca, cb), trunc_negative_moment(ap + bp))
        mI = iadd(mI, iscale(term, md))

muI = idiv(mI, qI)
assert muI[0] > 0


# ---------------------------------------------------------------------------
# n=<Tf,Tf>=<f,T^2 f>.
# For a stationary AR(1) triple (X,Y,Z) with r=4/5, put
#   A=(X+Y)/sqrt(2(1+r)), B=(Y+Z)/sqrt(2(1+r)).
# Then corr(A,B)=9/10 and, conditional on (A,B),
#   X=(84 A-30 B)/(19 sqrt(10)) + E,
#   Z=(-30 A+84 B)/(19 sqrt(10)) + E,
# where E~N(0,1/19) is independent.
# The event is A<0,B<0.
#
# Positive-quadrant moments Q[m,n]=E[A^m B^n 1_{A>0,B>0}]
# are generated by exact integration-by-parts recurrences.
# ---------------------------------------------------------------------------
MAX = 2 * DEG + 2
EXT = 3 * DEG + 12
s2 = F(19, 100)
c = F(9, 10)

B = [None] * EXT
B[0] = iscale(imul(sI, tI), F(1, 2))
B[1] = iscale(imul(tI, tI), s2)
for k in range(2, EXT):
    B[k] = iscale(B[k - 2], F((k - 1) * 19, 100))

A = [None] * EXT
A[0] = iadd(C(F(1, 4)), iscale(idiv(asin09I, piI), F(1, 2)))
A[1] = iadd(iscale(tI, F(1, 2)), imul(aI, B[0]))
for k in range(2, EXT):
    A[k] = iadd(iscale(A[k - 2], k - 1), imul(aI, B[k - 1]))

Q = [[None] * EXT for _ in range(MAX + 1)]
for n in range(EXT):
    Q[0][n] = A[n]
for n in range(EXT - 1):
    Q[1][n] = iadd(iscale(A[n + 1], c), imul(sI, B[n]))
for mm in range(2, MAX + 1):
    for n in range(EXT - mm):
        Q[mm][n] = iadd(
            iscale(Q[mm - 1][n + 1], c),
            iscale(Q[mm - 2][n], F((mm - 1) * 19, 100)),
        )

# Internal symmetry check on every moment used below.
for i in range(2 * DEG + 1):
    for j in range(2 * DEG + 1 - i):
        qi, qj = Q[i][j], Q[j][i]
        assert max(qi[0], qj[0]) <= min(qi[1], qj[1])


def q_negative(a, b):
    z = Q[a][b]
    return ineg(z) if (a + b) % 2 else z


lxa = iscale(inv_sqrt10, F(84, 19))
lxb = iscale(inv_sqrt10, F(-30, 19))
lza = iscale(inv_sqrt10, F(-30, 19))
lzb = iscale(inv_sqrt10, F(84, 19))


def powers(x):
    out = [C(1)]
    for _ in range(DEG):
        out.append(imul(out[-1], x))
    return out


lxaP, lxbP, lzaP, lzbP = map(powers, (lxa, lxb, lza, lzb))
FX = [{} for _ in range(DEG + 1)]
FZ = [{} for _ in range(DEG + 1)]
for k, pk in enumerate(PC):
    fk = factorial(k)
    for e in range(k + 1):
        rem = k - e
        for ap in range(rem + 1):
            bp = rem - ap
            mult = fk // (factorial(ap) * factorial(bp) * factorial(e))
            coeff = pk * mult
            add_to(FX[e], (ap, bp), iscale(imul(lxaP[ap], lxbP[bp]), coeff))
            add_to(FZ[e], (ap, bp), iscale(imul(lzaP[ap], lzbP[bp]), coeff))

nI = (0, 0)
pair_count = 0
for e in range(DEG + 1):
    for h in range(DEG + 1):
        kk = e + h
        moment = std_moment(kk)
        if moment == 0:
            continue
        subtotal = (0, 0)
        for (ap, bp), ca in FX[e].items():
            for (cp, dp), cb in FZ[h].items():
                pair_count += 1
                subtotal = iadd(
                    subtotal,
                    imul(imul(ca, cb), q_negative(ap + cp, bp + dp)),
                )
        subtotal = iscale(subtotal, F(moment, 19 ** (kk // 2)))
        nI = iadd(nI, subtotal)

nNormI = idiv(nI, qI)
eps2I = isub(nNormI, imul(muI, muI))
assert eps2I[0] > 0


# ---------------------------------------------------------------------------
# Spectral separation and Kato--Temple.
# T is self-adjoint; T^2 has strictly positive kernel, so its positive Perron
# root lambda_1 is simple and equals ||T||.  Moreover
#   tr T^2 = ||T||_HS^2 = 1/[2(1-r^2)] = 25/18.
# Since lambda_1 >= mu, every other eigenvalue has squared modulus at most
# 25/18-mu^2.  We certify this is below beta^2 with beta=791/1000.
# ---------------------------------------------------------------------------
trace2 = C(F(25, 18))
beta = F(791, 1000)
betaI = C(beta)
mu_lo_point = (muI[0], muI[0])
remainderI = isub(trace2, imul(mu_lo_point, mu_lo_point))
assert remainderI[1] < C(beta * beta)[0]
assert muI[0] > betaI[1]

gap_lo = muI[0] - betaI[1]
assert gap_lo > 0
# eps2/(mu-beta), converted back to the SCALE lattice with outward rounding.
kato_correction_hi = ceil_frac(F(eps2I[1] * SCALE, gap_lo))
lambda_upper_scaled = muI[1] + kato_correction_hi
lambda_cap = F(701, 800)
lambda_capI = C(lambda_cap)
assert lambda_upper_scaled < lambda_capI[0]


# ---------------------------------------------------------------------------
# Exact logarithm conversion.
# -log x = 2 sum_{m>=0} z^(2m+1)/(2m+1), z=(1-x)/(1+x),
# with a positive geometric tail bound.
# ---------------------------------------------------------------------------

def neglog_bounds(x, N=55):
    x = F(x)
    assert 0 < x < 1
    z = (1 - x) / (1 + x)
    partial = F(0)
    for k in range(N + 1):
        partial += z ** (2 * k + 1) / F(2 * k + 1)
    lo = 2 * partial
    m = 2 * N + 3
    tail = 2 * z ** m / F(m) / (1 - z * z)
    return lo, lo + tail


target = F(37, 250)
log_lam = neglog_bounds(lambda_cap)
log_grid = neglog_bounds(F(4, 5))
log_margin = log_lam[0] - 4 * target * log_grid[1]
assert log_margin > 0

old_lower = F(146611, 10**6)
old_width = F(103389, 10**6)
new_width = F(1, 4) - target
improvement = target - old_lower
assert new_width == F(51, 500)
assert improvement == F(1389, 10**6)
assert old_width - new_width == improvement

print('degree =', DEG)
print('pair_count =', pair_count)
print('trial_norm2 =', mid_float(qI))
print('grid_q =', 0.8)
print('mu interval =', muI[0] / SCALE, muI[1] / SCALE)
print('normalized T2 interval =', nNormI[0] / SCALE, nNormI[1] / SCALE)
print('residual^2 interval =', eps2I[0] / SCALE, eps2I[1] / SCALE)
print('trace2 =', float(F(25,18)))
print('spectral remainder upper =', remainderI[1] / SCALE)
print('beta^2 =', float(beta * beta))
print('Kato lambda1 upper =', lambda_upper_scaled / SCALE)
print('rational lambda1 cap =', float(lambda_cap))
print('log comparison margin =', float(log_margin))
print('old theta lower =', float(old_lower))
print('certified theta lower =', float(target))
print('old bracket width =', float(old_width))
print('new bracket width =', float(new_width))
print('width improvement =', float(improvement))
print('ALL_EXACT_CHECKS_PASS = True')
