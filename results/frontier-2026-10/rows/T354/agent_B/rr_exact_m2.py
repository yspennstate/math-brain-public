# T354: rr_exact_m.py made fast enough for n in the hundreds (agent B, 20 Oct 2026). Same model and same exact drift.
# Two facts do it. (1) An earlier epoch e contributes Phi(u A b2^(p + e n)), Phi(c) = E exp(-c sum_{q in S} b2^(-q)) over a uniform
# m-subset S of the n slots, a function of c alone: computed once by the elementary-symmetric recursion on a grid in log c and
# read off by a cubic spline in log c (below c r_max = 1e-4 the two-cumulant series). (2) In the current epoch the past slots of
# position p have lags 1..p, nested in p, so one recursion pass over lags 1..n-1 gives every p; the number of specials among
# the p past slots is hypergeometric (n - 1 slots, m - 1 or m specials).
# Argv: n beta2 [eps] [h]. n a multiple of 10.
import sys, math, numpy as np
from scipy.optimize import brentq
from scipy.special import erfcx, gammaln
from scipy.interpolate import CubicSpline
from kclosed import K_closed
n = int(sys.argv[1]); b2 = float(sys.argv[2]); eps = float(sys.argv[3]) if len(sys.argv) > 3 else 0.0
h = float(sys.argv[4]) if len(sys.argv) > 4 else 0.02
assert n % 10 == 0; m = n // 10; d = 1 - b2
t = np.arange(-45.0, math.log(60.0) + h / 2, h); u = np.exp(t)
k = (np.pi * u) ** -0.5 * (1 - eps * np.sqrt(np.pi * u) * erfcx(eps * np.sqrt(u))); wt = h * u * k
r = b2 ** (-np.arange(n, dtype=float)); mu = r.mean(); var_sub = m * (n - m) / (n - 1) * r.var(); rmax = r.max()
def esym_step(f, i, w):
    j = np.arange(1, f.shape[0])[:, None]
    f[1:] = ((i - j) / i) * f[1:] + (j / i) * w * f[:-1]
def lnC(a, b): return gammaln(a + 1) - gammaln(b + 1) - gammaln(a - b + 1)
# Phi on log c, from c r_max = 1e-4 up to the largest argument any x in the bracket needs
A_hi = d * ((9 + 1.0) ** 2 - (-1 + 1.0) ** 2) * 1.5
lc_lo = math.log(1e-4 / rmax); lc_hi = math.log(u.max() * A_hi) + 0.5; dl = 0.002
lc = np.arange(lc_lo, lc_hi + dl, dl); c = np.exp(lc)
f = np.zeros((m + 1, lc.size)); f[0] = 1.0
for i in range(1, n + 1): esym_step(f, i, np.exp(-c * r[i - 1]))
logPhi = CubicSpline(lc, np.log(np.maximum(f[m], 1e-300)))
def logPhi_at(cc):
    out = -cc * m * mu + 0.5 * cc * cc * var_sub          # series below the grid
    big = cc >= c[0]
    out[big] = logPhi(np.log(cc[big]))
    return out
P_past = {}
for jj in (m - 1, m):                                    # hypergeometric weights P(k of jj specials in the p past slots)
    W = np.zeros((n, m + 1))
    for p in range(n):
        for kk in range(0, min(p, jj) + 1):
            if jj - kk <= n - 1 - p:
                W[p, kk] = math.exp(lnC(p, kk) + lnC(n - 1 - p, jj - kk) - lnC(n - 1, jj))
    P_past[jj] = W
def D(x):
    gs, go = 9 + x, -1 + x; A = d * (gs * gs - go * go); uA = u * A; tot = 0.0
    fc = np.zeros((m + 1, u.size)); fc[0] = 1.0
    for p in range(n):
        if p >= 1: esym_step(fc, p, np.exp(-uA * b2 ** p))      # add past slot with lag p (lags 1..p after this step)
        cur_s = P_past[m - 1][p] @ fc; cur_o = P_past[m][p] @ fc
        logP = np.zeros_like(u); e = 1
        while True:
            cc = uA * b2 ** (p + e * n)
            if cc.max() * rmax < 1e-4: break
            logP += logPhi_at(cc); e += 1
        base = b2 ** (p + e * n)
        logP += -uA * m * mu * base / (1 - b2 ** n) + 0.5 * uA ** 2 * var_sub * base ** 2 / (1 - b2 ** (2 * n))
        common = wt * np.exp(-u * go * go + logP)
        tot += 0.1 * gs * (common * np.exp(-uA) * cur_s).sum() + 0.9 * go * (common * cur_o).sum()
    return tot / n
K = K_closed(n, 0.0, b2); rr = 3 / (3 + eps); x0 = rr * d * K * 72 / 18
xs = brentq(D, 0.3 * x0, 3 * x0, xtol=1e-13 * x0)
print("RRm2 n %d m %d beta2 %s eps %g h %g n(1-b2) %.3f K %.8f x0 %.8g exact x* %.12g x*/x0 %.9f (x*/x0-1)/d %.5f"
      % (n, m, sys.argv[2], eps, h, n * d, K, x0, xs, xs / x0, (xs / x0 - 1) / d), flush=True)
