#!/usr/bin/env python3
"""Exact rational checker for HARD7-05, 2026-09-19T0726Z.

Finite/arithmetic core of the sampled-OU comparison proving
    theta_{2,1/4} >= 703/5000.

External analytic inputs (not re-proved by this finite checker):
  * Slepian's Gaussian comparison lemma;
  * Polya's erf bound erf(x)^2 < 1-exp(-4 x^2/pi), x>0;
  * the standard bivariate Gaussian sign/arcsine formula;
  * 333/106 < pi < 355/113.
Everything after those inputs is checked using Fraction/integer arithmetic.
"""

from fractions import Fraction as F
from math import comb


def mat_inv(A):
    n = len(A)
    M = [[F(A[i][j]) for j in range(n)] + [F(int(i == j)) for j in range(n)] for i in range(n)]
    for col in range(n):
        pivot = next(i for i in range(col, n) if M[i][col])
        if pivot != col:
            M[col], M[pivot] = M[pivot], M[col]
        pv = M[col][col]
        M[col] = [x / pv for x in M[col]]
        for i in range(n):
            if i != col and M[i][col]:
                fac = M[i][col]
                M[i] = [M[i][j] - fac * M[col][j] for j in range(2 * n)]
    return [row[n:] for row in M]


def mat_mul(A, B):
    return [[sum((A[i][k] * B[k][j] for k in range(len(B))), F(0))
             for j in range(len(B[0]))] for i in range(len(A))]


def det2(A):
    return A[0][0] * A[1][1] - A[0][1] * A[1][0]


def poly_mul(a, b):
    out = [F(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def poly_pow(a, n):
    out = [F(1)]
    for _ in range(n):
        out = poly_mul(out, a)
    return out


def poly_sub(a, b):
    n = max(len(a), len(b))
    return [(a[i] if i < len(a) else F(0)) - (b[i] if i < len(b) else F(0))
            for i in range(n)]


def poly_scale(a, c):
    return [c * x for x in a]


def polyval(c, z):
    s = F(0)
    for cc in reversed(c):
        s = s * z + cc
    return s


def asin_partial(x, N):
    s = F(0)
    for n in range(N + 1):
        an = F(comb(2 * n, n), 4**n * (2 * n + 1))
        assert F(0) < an <= F(1)
        s += an * x**(2 * n + 1)
    return s


def asin_upper(x, N):
    # Since every remaining arcsin coefficient is <=1.
    return asin_partial(x, N) + x**(2 * N + 3) / (1 - x * x)


# ---------------------------------------------------------------------------
# 1. Exact grid covariance domination for H=1/4.
# q=exp(-t/4), z=q^2.  The proof on the page reduces R(t)<=q to
# 2(1+z)(1-z^2)^(3/2) <= P(z),
# P(z)=2+2z-3z^2-2z^3-2z^4.
# Squaring gives z^3 Q(z)>=0.
# ---------------------------------------------------------------------------
zmax = F(529, 1600)  # (23/40)^2
P = [F(2), F(2), F(-3), F(-2), F(-2)]
oneplus = [F(1), F(1)]
oneminusz2 = [F(1), F(0), F(-1)]
diff = poly_sub(poly_mul(P, P),
                poly_scale(poly_mul(poly_pow(oneplus, 2), poly_pow(oneminusz2, 3)), F(4)))
Q = [F(4), F(-7), F(-20), F(8), F(16), F(8)]
assert diff == [F(0), F(0), F(0)] + Q

Qend = polyval(Q, zmax)
pos_derivative_part = 40 * zmax**4 + 64 * zmax**3 + 24 * zmax**2
P_crude_lower = F(2) - 3 * zmax**2 - 2 * zmax**3 - 2 * zmax**4
assert Qend > 0
assert pos_derivative_part < 7  # Q'(z) <= positive_part - 7 < 0 on [0,zmax].
assert P_crude_lower > 0

# ---------------------------------------------------------------------------
# 2. Four-step stationary AR(1) loop at r=23/40.
# ---------------------------------------------------------------------------
r = F(23, 40)
sig2 = 1 - r * r
diag = (1 + r * r) / sig2
off = -r / sig2
Qmat = [[F(0) for _ in range(4)] for _ in range(4)]
for i in range(4):
    Qmat[i][i] = diag
    Qmat[i][(i + 1) % 4] = off
    Qmat[i][(i - 1) % 4] = off
Sigma = mat_inv(Qmat)
expected_diag = F(2839841, 2280159)
expected_adj = F(920, 1071)
expected_opp = F(1692800, 2280159)
for i in range(4):
    assert Sigma[i][i] == expected_diag
    assert Sigma[i][(i + 1) % 4] == expected_adj
    assert Sigma[i][(i + 2) % 4] == expected_opp
rho1 = expected_adj / expected_diag
rho2 = expected_opp / expected_diag
assert rho1 == F(1958680, 2839841)
assert rho2 == F(1692800, 2839841)

# ---------------------------------------------------------------------------
# 3. Conditional-independence / Polya correction.
# Given X2,X4, X1 and X3 are independent and each positive with probability
# Phi(u), u=r(X2+X4)/sqrt(1-r^4).  Use beta=51/80 > 2/pi.
# ---------------------------------------------------------------------------
beta = F(51, 80)
S2 = [[Sigma[1][1], Sigma[1][3]], [Sigma[3][1], Sigma[3][3]]]
a = beta * r * r / (1 - r**4)
A = [[a, a], [a, a]]
M = mat_mul(S2, A)
M = [[F(int(i == j)) + 2 * M[i][j] for j in range(2)] for i in range(2)]
detM = det2(M)
assert detM == F(64811, 22491)
S2inv = mat_inv(S2)
PrecTilt = [[S2inv[i][j] + 2 * A[i][j] for j in range(2)] for i in range(2)]
Tilt = mat_inv(PrecTilt)
rho_t = Tilt[0][1] / Tilt[0][0]
assert rho_t == F(613640, 3919001)

# Classical rational pi bounds and beta > 2/pi.
pi_lo = F(333, 106)
pi_hi = F(355, 113)
assert pi_lo < pi_hi
assert F(2) / pi_lo < beta

# Arcsine Taylor enclosures, all exact rationals.
N = 12
P3_ub = F(1, 8) + F(106, 333) * F(1, 4) * (
    2 * asin_upper(rho1, N) + asin_upper(rho2, N)
)
orth_lo = F(1, 4) + F(113, 355) * F(1, 2) * asin_partial(rho_t, N)
pref_lo = F(589087, 1000000)
assert pref_lo * pref_lo < F(1) / detM
E_lo = pref_lo * orth_lo
assert P3_ub < F(14849, 50000)
assert E_lo > F(81, 500)

# Thus P4 < P3 - E/4 < 0.29698 - 0.162/4 = 0.25648.
P4_coarse = F(14849, 50000) - F(81, 500) / 4
assert P4_coarse == F(1603, 6250)
assert P4_coarse < F(25649, 100000)

# ---------------------------------------------------------------------------
# 4. Trace bound and final exact exponent comparison.
# tr K^4 = P4/(1-r^4), ||K||^4 <= tr K^4.
# With Delta=4 log(40/23), theta >= -log(tr K^4)/(16 log(40/23)).
# To prove this exceeds 703/5000, avoid floating point by raising to power 625.
# ---------------------------------------------------------------------------
denom = 1 - r**4
trace_ub = P4_coarse / denom
assert trace_ub == F(468992, 1628685)
target = F(703, 5000)
assert 16 * target == F(1406, 625)
assert trace_ub**625 < r**1406

# The predecessor's optimized spectral lower bound is below 7/50 < 703/5000.
# D=pi^2/2-8G+416/25; an alternating 5-term Catalan upper bound and pi_lo suffice.
G_upper = sum((F(1, (2*n + 1)**2) if n % 2 == 0 else -F(1, (2*n + 1)**2))
              for n in range(5))
D_lower = pi_lo * pi_lo / 2 - 8 * G_upper + F(416, 25)
assert D_lower > F(6250, 441)  # => sqrt(5/(18D)) < 7/50
assert F(7, 50) < target

print("zmax =", zmax, "Q(zmax) =", Qend)
print("loop rho_adj =", rho1, "rho_opp =", rho2)
print("tilt det =", detM, "tilt rho =", rho_t)
print("P3_upper_exact =", P3_ub, "~", float(P3_ub))
print("E_lower_exact =", E_lo, "~", float(E_lo))
print("P4 <", P4_coarse, "=", float(P4_coarse))
print("trace K^4 <", trace_ub, "=", float(trace_ub))
print("power_certificate =", trace_ub**625 < r**1406)
print("certified theta lower =", target, "=", float(target))
print("new bracket width =", F(1, 4) - target, "=", float(F(1, 4) - target))
print("ALL_EXACT_CHECKS_PASS = True")
