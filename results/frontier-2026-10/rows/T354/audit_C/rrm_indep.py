"""Independent exact root of the frozen-x Adam drift under random reshuffling at any n (agent C, 20 Oct 2026).

Audit of agent_B/NOTE.md, section "Every n" (push 17c04a29). Written without reading rr_exact_m.py / rr_exact_m2.py.

Model: n samples per epoch, m = n/10 of them have b = 9 and the rest b = -1 (B2 = 9, B3 = 72). beta1 = 0, eps = 0, frozen x,
g = x + b, v_k = (1 - beta2) sum_{j>=0} beta2^j g_{k-j}^2 over an infinite past. Drift D(x) = E[g_k / sqrt(v_k)], k uniform over
epoch positions.

Route:
  v = q + d (A - q) S, A = (x+9)^2, q = (x-1)^2, d = 1 - beta2, S = sum over special lags of beta2^lag.
  1/sqrt(v) = (2/sqrt(pi)) int_0^inf exp(-s^2 v) ds, Gauss-Legendre in s on [0, sqrt(50/q)].
  E exp(-w S) (w = s^2 d (A - q)) factorizes over epochs:
    - current epoch, step at position p (0-based): lag 0 is g_k itself; lags 1..p are the visited part of the epoch. Given g_k's
      type, the number h of specials among them is hypergeometric (n-1 others, m-1 or m specials, p draws), and given h they are
      a uniform h-subset. Factor = sum_h P(h) M_h(z_1..z_p), M_h the normalized elementary-symmetric mean, z_j = exp(-w beta2^j).
    - each earlier epoch is a full uniform m-subset of n consecutive lags L..L+n-1: factor G(w beta2^L),
      G(y) = M_m(exp(-y beta2^t), t = 0..n-1), tabulated on a log grid of y and splined in log-log.
  M_h is built by the convex recursion M_h(t) = ((t-h)/t) M_h(t-1) + (h/t) z_t M_{h-1}(t-1).
K_rr at beta1 = 0 from the lag sum: K = 1 - sum_{j=1}^{n-1} (n-j) beta2^j / (n (n-1)).
usage: python rrm_indep.py N BETA2 [SNODES] [YGRID]
"""
import math
import sys

import numpy as np
from scipy.interpolate import CubicSpline
from scipy.optimize import brentq
from scipy.stats import hypergeom


def K_rr_b1zero(n, b2):
    j = np.arange(1, n)
    return 1.0 - np.sum((n - j) * b2 ** j) / (n * (n - 1))


def table_G(n, m, b2, ygrid):
    """log G(y) for every y in ygrid (vector), G(y) = mean over m-subsets T of exp(-y sum_{t in T} b2^t)."""
    M = np.zeros((m + 1, ygrid.size))
    M[0] = 1.0
    lsc = np.zeros(ygrid.size)  # M_true = M * exp(lsc), rescaled every step so nothing underflows
    for t in range(1, n + 1):
        z = np.exp(-ygrid * b2 ** (t - 1))
        hmax = min(t, m)
        h = np.arange(1, hmax + 1)[:, None]
        new = ((t - h) / t) * M[1:hmax + 1] + (h / t) * z * M[0:hmax]
        M[1:hmax + 1] = new
        mx = M.max(axis=0)
        M /= mx
        lsc += np.log(mx)
    return np.log(M[m]) + lsc


class Solver:
    def __init__(self, n, b2, snodes=200, ygrid=2400):
        self.n, self.b2 = n, b2
        self.m = n // 10
        assert self.m * 10 == n
        self.d = 1.0 - b2
        self.sx, self.sw = np.polynomial.legendre.leggauss(snodes)
        lo, hi = -40.0, math.log(60.0 * self.d * 100.0)
        self.ly = np.linspace(lo, hi, ygrid)
        lg = table_G(n, self.m, b2, np.exp(self.ly))
        self.spl = CubicSpline(self.ly, lg)
        self.lo, self.hi = lo, hi
        # first-order slope of log G at y -> 0: -(m/n) sum_t b2^t
        self.slope0 = -(self.m / n) * (1 - b2 ** n) / self.d
        p = np.arange(n)
        self.Hs = np.array([hypergeom.pmf(np.arange(self.m + 1), n - 1, self.m - 1, pp) for pp in p])
        self.Ho = np.array([hypergeom.pmf(np.arange(self.m + 1), n - 1, self.m, pp) for pp in p])

    def logG(self, y):
        out = np.empty_like(y)
        small = y < math.exp(self.lo)
        out[small] = self.slope0 * y[small]
        ly = np.log(np.maximum(y[~small], 1e-300))
        assert np.all(ly <= self.hi + 1e-9), "extend the y grid"
        out[~small] = self.spl(ly)
        return out

    def drift(self, x):
        n, m, b2, d = self.n, self.m, self.b2, self.d
        A, q = (x + 9.0) ** 2, (x - 1.0) ** 2
        smax = math.sqrt(50.0 / q)
        s = 0.5 * smax * (self.sx + 1.0)
        ws = 0.5 * smax * self.sw
        w = s * s * d * (A - q)
        base = np.exp(-s * s * q)
        # earlier epochs: P(L) = prod_{e>=0} G(w b2^(L + e n)), needed for L = 1..n
        L = np.arange(1, n + 1)
        logP = np.zeros((n, s.size))
        e = 0
        while True:
            y = w[None, :] * b2 ** (L[:, None] + e * n).astype(float)
            if y.max() < 1e-300:
                break
            logP += self.logG(y.ravel()).reshape(y.shape)
            e += 1
            if y.max() < 1e-18:
                break
        # current epoch, DP over visited lags 1..p
        Mh = np.zeros((m + 1, s.size))
        Mh[0] = 1.0
        z0 = np.exp(-w)
        Is = np.empty(n)
        Io = np.empty(n)
        for p in range(n):
            if p >= 1:
                z = np.exp(-w * b2 ** p)
                hmax = min(p, m)
                h = np.arange(1, hmax + 1)[:, None]
                Mh[1:hmax + 1] = ((p - h) / p) * Mh[1:hmax + 1] + (h / p) * z * Mh[0:hmax]
            fs = self.Hs[p] @ Mh
            fo = self.Ho[p] @ Mh
            Pp = np.exp(logP[p])  # earlier epochs start at lag p + 1
            Is[p] = (2 / math.sqrt(math.pi)) * np.sum(ws * base * z0 * fs * Pp)
            Io[p] = (2 / math.sqrt(math.pi)) * np.sum(ws * base * fo * Pp)
        return (m / n) * (x + 9.0) * Is.mean() + (1 - m / n) * (x - 1.0) * Io.mean()


if __name__ == "__main__":
    n, b2 = int(sys.argv[1]), float(sys.argv[2])
    sn = int(sys.argv[3]) if len(sys.argv) > 3 else 200
    yg = int(sys.argv[4]) if len(sys.argv) > 4 else 2400
    S = Solver(n, b2, sn, yg)
    d = 1 - b2
    K = K_rr_b1zero(n, b2)
    x0 = d * K * 72.0 / (2 * 9.0)
    xs = brentq(S.drift, 0.5 * x0, 1.5 * x0, xtol=1e-15, rtol=1e-13)
    print("INDEP n %d beta2 %g nd %g snodes %d ygrid %d: K %.12f x0 %.12g x* %.12g (x*/x0-1)/d %.6f"
          % (n, b2, n * d, sn, yg, K, x0, xs, (xs / x0 - 1) / d), flush=True)
