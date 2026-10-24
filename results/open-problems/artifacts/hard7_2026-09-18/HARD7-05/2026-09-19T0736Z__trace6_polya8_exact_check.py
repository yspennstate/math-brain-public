#!/usr/bin/env python3
"""Exact rational checker for HARD7-05, six-step trace/Pólya-series bound.

Certifies the finite/arithmetic core of
    theta_{2,1/4} >= 71/500.

External analytic inputs used by the written proof:
  * Slepian's Gaussian comparison lemma;
  * Pólya's erf inequality erf(x)^2 < 1-exp(-4x^2/pi), x>0;
  * the centered trivariate Gaussian orthant formula;
  * 333/106 < pi < 355/113.

All matrix algebra, square-root enclosures, arcsine enclosures, the 729-term
six-cycle expansion, and the final exponential comparison are checked with
fractions/integers only.
"""

from fractions import Fraction as F
from math import comb, isqrt
from itertools import combinations_with_replacement


def mat_inv(A):
    n = len(A)
    M = [[F(A[i][j]) for j in range(n)] +
         [F(int(i == j)) for j in range(n)] for i in range(n)]
    for col in range(n):
        p = next(i for i in range(col, n) if M[i][col])
        if p != col:
            M[col], M[p] = M[p], M[col]
        pv = M[col][col]
        M[col] = [x / pv for x in M[col]]
        for i in range(n):
            if i != col and M[i][col]:
                q = M[i][col]
                M[i] = [M[i][j] - q * M[col][j] for j in range(2*n)]
    return [row[n:] for row in M]


def mat_mul(A, B):
    return [[sum((A[i][k] * B[k][j] for k in range(len(B))), F(0))
             for j in range(len(B[0]))] for i in range(len(A))]


def mat_add(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))]
            for i in range(len(A))]


def mat_scale(A, c):
    return [[c*x for x in row] for row in A]


def eye(n):
    return [[F(int(i == j)) for j in range(n)] for i in range(n)]


def det(A):
    n = len(A)
    M = [[F(x) for x in row] for row in A]
    ans = F(1)
    for col in range(n):
        p = next((i for i in range(col, n) if M[i][col]), None)
        if p is None:
            return F(0)
        if p != col:
            M[col], M[p] = M[p], M[col]
            ans = -ans
        pv = M[col][col]
        ans *= pv
        for i in range(col+1, n):
            q = M[i][col] / pv
            for j in range(col+1, n):
                M[i][j] -= q * M[col][j]
    return ans


def sqrt_interval(x, D=10**18):
    """Exact lo <= sqrt(x) < hi, with denominator D."""
    assert x > 0
    m = isqrt((D*D*x.numerator)//x.denominator)
    lo, hi = F(m, D), F(m+1, D)
    assert lo*lo <= x < hi*hi
    return lo, hi


def asin_partial(x, N=20):
    assert 0 <= x < 1
    ans = F(0)
    for n in range(N+1):
        a = F(comb(2*n, n), 4**n * (2*n+1))
        assert 0 < a <= 1
        ans += a*x**(2*n+1)
    return ans


def asin_point_interval(x, N=20):
    if x >= 0:
        p = asin_partial(x, N)
        # Every omitted arcsin coefficient is <= 1.
        u = p + x**(2*N+3)/(1-x*x)
        return p, u
    lo, hi = asin_point_interval(-x, N)
    return -hi, -lo


def asin_interval(xlo, xhi, N=20):
    assert -1 < xlo <= xhi < 1
    lo, _ = asin_point_interval(xlo, N)
    _, hi = asin_point_interval(xhi, N)
    return lo, hi


pi_lo = F(333, 106)
pi_hi = F(355, 113)
inv4pi_lo = F(1, 4)/pi_hi
inv4pi_hi = F(1, 4)/pi_lo


def orth3_interval(C):
    """Exact rational enclosure for P(N(0,C)>0 in all 3 coordinates)."""
    aa = []
    for i, j in ((0, 1), (0, 2), (1, 2)):
        slo, shi = sqrt_interval(C[i][i]*C[j][j])
        c = C[i][j]
        if c >= 0:
            rlo, rhi = c/shi, c/slo
        else:
            rlo, rhi = c/slo, c/shi
        assert -1 < rlo <= rhi < 1
        aa.append(asin_interval(rlo, rhi))
    Slo = sum((x[0] for x in aa), F(0))
    Shi = sum((x[1] for x in aa), F(0))
    vals = (Slo*inv4pi_lo, Slo*inv4pi_hi,
            Shi*inv4pi_lo, Shi*inv4pi_hi)
    return F(1, 8)+min(vals), F(1, 8)+max(vals)


# ---------------------------------------------------------------------------
# 1. Same admissible grid as predecessor: r=23/40, Delta=4 log(40/23).
#    The predecessor proved R(k Delta) <= r^k for every k>=1.
# ---------------------------------------------------------------------------
r = F(23, 40)
beta = F(51, 80)
assert F(2, 1)/pi_lo < beta   # beta > 2/pi

# Six-cycle Gaussian loop precision for the AR(1) chain.
sig2 = 1-r*r
diag = (1+r*r)/sig2
off = -r/sig2
Q6 = [[F(0) for _ in range(6)] for _ in range(6)]
for i in range(6):
    Q6[i][i] = diag
    Q6[i][(i+1) % 6] = off
    Q6[i][(i-1) % 6] = off
S6 = mat_inv(Q6)

# Marginal covariance of the even loop sites 0,2,4.
even = (0, 2, 4)
C = [[S6[i][j] for j in even] for i in even]
assert C[0][0] == C[1][1] == C[2][2]
assert C[0][1] == C[0][2] == C[1][2]
Cinv = mat_inv(C)

# Standardized conditional means of odd sites are
# u1 = r(y0+y1)/sqrt(1-r^4), u2 = r(y1+y2)/sqrt(...),
# u3 = r(y2+y0)/sqrt(...). Their squared linear forms are rational.
fac = r*r/(1-r**4)
B = (
    ((F(1), F(1), F(0)), (F(1), F(1), F(0)), (F(0), F(0), F(0))),
    ((F(0), F(0), F(0)), (F(0), F(1), F(1)), (F(0), F(1), F(1))),
    ((F(1), F(0), F(1)), (F(0), F(0), F(0)), (F(1), F(0), F(1))),
)


def tilt_interval(ks):
    """Enclose E[1_{Y>0} exp(-beta sum_i ks_i u_i^2)]."""
    A = [[F(0) for _ in range(3)] for _ in range(3)]
    for h, k in enumerate(ks):
        if not k:
            continue
        sc = beta*F(k)*fac
        for i in range(3):
            for j in range(3):
                A[i][j] += sc*B[h][i][j]
    M = mat_add(eye(3), mat_scale(mat_mul(C, A), F(2)))
    d = det(M)
    assert d > 0
    pref_lo, pref_hi = sqrt_interval(F(1, 1)/d)
    Ct = mat_inv(mat_add(Cinv, mat_scale(A, F(2))))
    o_lo, o_hi = orth3_interval(Ct)
    assert 0 < o_lo <= o_hi < 1
    return pref_lo*o_lo, pref_hi*o_hi


# ---------------------------------------------------------------------------
# 2. Pólya-series envelope.
#
# q=1-Phi(u), u>=0. Pólya gives q(1-q) >= exp(-beta u^2)/4.
# Hence q >= h(x):=(1-sqrt(1-x))/2, x=exp(-beta u^2).
# The first eight positive Taylor coefficients of h are below.
# Therefore Phi(u) <= 1-g_8(x).
# ---------------------------------------------------------------------------
a = {
    0: F(1),
    1: -F(1, 4),
    2: -F(1, 16),
    3: -F(1, 32),
    4: -F(5, 256),
    5: -F(7, 512),
    6: -F(21, 2048),
    7: -F(33, 4096),
    8: -F(429, 65536),
}
assert all(a[k] < 0 for k in range(1, 9))
assert sum((-a[k] for k in range(1, 9)), F(0)) < F(1, 2)

# Expand product_i (1-g_8(exp(-beta u_i^2))).  The even marginal is
# equicorrelated and u1,u2,u3 are the three edge sums of its triangle, so
# T(k1,k2,k3) is invariant under permutation of k1,k2,k3.  We evaluate the
# 165 sorted triples and include their exact multiplicities (729 total terms).
P6_lo = F(0)
P6_hi = F(0)
terms = 0
for ks in combinations_with_replacement(range(9), 3):
    if ks[0] == ks[2]:
        mult = 1
    elif ks[0] == ks[1] or ks[1] == ks[2]:
        mult = 3
    else:
        mult = 6
    cf = mult*a[ks[0]]*a[ks[1]]*a[ks[2]]
    lo, hi = tilt_interval(ks)
    if cf >= 0:
        P6_lo += cf*lo
        P6_hi += cf*hi
    else:
        P6_lo += cf*hi
        P6_hi += cf*lo
    terms += mult

assert terms == 729
assert 0 < P6_lo <= P6_hi < F(1, 2)

# ---------------------------------------------------------------------------
# 3. Six-step trace and the clean exponent 71/500.
# tr K^6 = P6/(1-r^6), ||K||^6 <= tr K^6.
# It suffices to prove tr K^6 < 474/3125 = 0.15168 and then
# (474/3125)^500 < r^1704, since 24*(71/500)=1704/500.
# ---------------------------------------------------------------------------
trace_hi = P6_hi/(1-r**6)
coarse_trace = F(474, 3125)
assert trace_hi < coarse_trace
target = F(71, 500)
assert 24*target == F(1704, 500)
assert coarse_trace**500 < r**1704

print("terms =", terms)
print("P6 lower enclosure ~", float(P6_lo))
print("P6 upper enclosure ~", float(P6_hi))
print("trace K^6 upper enclosure ~", float(trace_hi))
print("coarse trace upper =", coarse_trace, "=", float(coarse_trace))
print("power_certificate =", coarse_trace**500 < r**1704)
print("certified theta lower =", target, "=", float(target))
print("new bracket width =", F(1, 4)-target, "=", float(F(1, 4)-target))
print("ALL_EXACT_CHECKS_PASS = True")
