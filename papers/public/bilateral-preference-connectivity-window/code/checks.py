"""Checks for "The connectivity window of bilateral preference random graphs".

1. The numerical constants used in the proofs, in exact rational arithmetic.
2. Formula (2.1) and inequality (2.2) of Lemma 2.1 against Monte Carlo.
3. M e^k for the quantity M of Lemma 2.2, by numerical integration, for n up to 10^7.

Run: python checks.py   (numpy and scipy; writes checks_out.txt beside this file)
"""
import math
import os
from fractions import Fraction as F

import numpy as np
from scipy import integrate, stats

OUT = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "checks_out.txt"), "w", encoding="utf-8")


def P(*a):
    print(*a)
    print(*a, file=OUT)
    OUT.flush()


def exp_lower(x, terms=40):
    """A rational lower bound for e^x, x >= 0 rational: a partial sum of the series."""
    s, t = F(0), F(1)
    for j in range(terms):
        s += t
        t = t * x / (j + 1)
    return s


def exp_upper(x, terms=40):
    """A rational upper bound for e^x, 0 <= x < terms: the partial sum plus a geometric bound on the tail."""
    s, t = F(0), F(1)
    for j in range(terms):
        s += t
        t = t * x / (j + 1)
    # tail sum_{j >= terms} x^j / j! <= t / (1 - x/(terms+1)), where t = x^terms / terms!
    return s + t / (1 - x / (terms + 1))


def log_gt(y, c):
    """Certify log y > c, i.e. y > e^c (y > 0, c >= 0 rational)."""
    return y > exp_upper(c)


def log_lt(y, c):
    """Certify log y < c, i.e. y < e^c."""
    return y < exp_lower(c)


P("== 1. constants (exact rational arithmetic)")
a, b = F(5, 32), F(32, 5)
checks = [
    ("a - 1 - log a > 1.0125, a = 5/32   [log(32/5) > 2.0125 - 5/32]", log_gt(1 / a, F(20125, 10000) - a)),
    ("b - 1 - log b > 1, b = 32/5        [log(32/5) < 32/5 - 2]", log_lt(b, b - 2)),
    ("B - 1 - log B >= B/2 at B = 6      [log 6 < 2; B/2 - 1 - log B increases for B > 2]", log_lt(F(6), F(2))),
    ("log 3 > 1", log_gt(F(3), F(1))),
    ("phi(2) = 2 log 2 - 1 > 0            [log 2 > 1/2]", log_gt(F(2), F(1, 2))),
    ("gamma = log(2/3) + 1/2 > 0          [log(3/2) < 1/2]", log_lt(F(3, 2), F(1, 2))),
    ("7a = 35/32 > 1", 7 * a > 1),
    ("13a/2 = 65/64 > 1", 13 * a / 2 > 1),
]
for name, ok in checks:
    P(f"  {'PASS' if ok else 'FAIL'}  {name}")
P(f"  (floating point: a-1-log a = {float(a) - 1 - math.log(float(a)):.6f}, b-1-log b = {float(b) - 1 - math.log(float(b)):.6f},"
  f" phi(2) = {2 * math.log(2) - 1:.6f}, gamma = {math.log(2 / 3) + 0.5:.6f})")
assert all(ok for _, ok in checks)

P("\n== 2. Lemma 2.1 against Monte Carlo (g = q, q(x) = P(Bin(N,x) >= k))")
rng = np.random.default_rng(20261029)


def lemma_sides(m, k, N, A, T=400000):
    q = lambda x: stats.binom.sf(k - 1, N, x)                       # P(Bin(N,x) >= k)
    Bk = stats.beta(k, N - k + 1)
    mu = k / (N + 1)
    Bp = stats.beta(k + 1, N - k + 1)
    Q = lambda x: x * Bk.cdf(x) - mu * Bp.cdf(x)                    # E(x - B)^+
    # Monte Carlo: the k smallest of m uniforms
    X = np.sort(rng.random((T, m)), axis=1)[:, :k]
    qX = q(X)
    mc = np.prod(qX[:, [i - 1 for i in A]], axis=1)
    mc_mean, mc_se = mc.mean(), mc.std(ddof=1) / math.sqrt(T)
    d = k - len(A)
    lf = math.lgamma(m + 1) - math.lgamma(m - k + 1)                # log (m)_k
    if d == 0:
        c = math.exp(lf + math.log(m - k) - math.lgamma(k + 1))     # (m)_{k+1}/k!
        f = lambda x: c * Q(x) ** k * (1 - x) ** (m - k - 1)
    else:
        c = math.comb(k - 1, d) * math.exp(lf - math.lgamma(k))     # binom(k-1,d) (m)_k/(k-1)!
        f = lambda x: c * q(x) * Q(x) ** (k - 1 - d) * x ** d * (1 - x) ** (m - k)
    val, _ = integrate.quad(f, 0, 1, limit=400, points=[mu, 2 * mu, 4 * mu])
    return mc_mean, mc_se, val


for m, k, N in [(40, 3, 40), (60, 4, 55)]:
    full = list(range(1, k + 1))
    mcm, se, rhs = lemma_sides(m, k, N, full)
    P(f"  m={m} k={k} N={N}  A=all      MC = {mcm:.6f} +- {se:.6f}   formula (2.1) = {rhs:.6f}")
    for A in ([1, k], [k], list(range(2, k + 1))):
        mcm, se, rhs = lemma_sides(m, k, N, A)
        P(f"  m={m} k={k} N={N}  A={A!s:10s} MC = {mcm:.6f} +- {se:.6f}   bound (2.2) = {rhs:.6f}   "
          f"{'ok' if mcm <= rhs + 3 * se else 'VIOLATED'}")

P("\n== 3. M e^k for Lemma 2.2 (m = N = n, k = round(log n)); also (1-mu)^m e^k")
for n in [10 ** 3, 10 ** 4, 10 ** 5, 10 ** 6, 10 ** 7]:
    for k in sorted({int(math.floor(math.log(n))), int(math.ceil(math.log(n)))}):
        m = N = n
        mu = k / (N + 1)
        Bk = stats.beta(k, N - k + 1)
        Bp = stats.beta(k + 1, N - k + 1)
        logc = math.lgamma(m + 1) - math.lgamma(m - k) - math.lgamma(k + 1)    # log (m)_{k+1}/k!

        def f(x):
            Qx = x * Bk.cdf(x) - mu * Bp.cdf(x)
            if Qx <= 0:
                return 0.0
            return math.exp(logc + k * math.log(Qx) + (m - k - 1) * math.log1p(-x) + k)

        hi = 12 * k / n
        val, err = integrate.quad(f, 0, hi, limit=800, points=[mu, 2 * mu, 3 * mu])
        lower = math.exp(m * math.log1p(-mu) + k)
        P(f"  n={n:>8d} k={k:2d}   M e^k = {val:.6f}   (1-mu)^m e^k = {lower:.6f}")
P("done")
OUT.close()
