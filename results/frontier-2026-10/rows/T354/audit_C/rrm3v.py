"""Exact root of the frozen-x Adam drift under random reshuffling at any n, three-valued b (agent C, 20 Oct 2026).

Audit of agent_B/NOTE.md, "c(n d) in closed form" (push 56ed125c): the closed form can only be told apart from a wrong
one on a distribution with r1 = z2/V^2 != r2 = E[bZ^2]/(B2 B3), which a two-valued b cannot give. This is rrm_indep.py with two
special types instead of one.

Model: per epoch m1 = n/10 samples with b = B1V, m2 = n/10 with b = B2V, the rest b = BO (mean 0; default 6, 2, -1: B2 4.8,
B3 21.6, r1 4.729, r2 5.523). beta1 = 0, eps = 0, frozen x. q = (x + BO)^2, a_T = d ((x + b_T)^2 - q).
  1/sqrt(v) = (2/sqrt(pi)) int exp(-s^2 v) ds, v = q + sum over special lags of a_T beta2^lag.
  Current epoch, step at position p: given g_k's type, the counts (h1, h2) of specials among the p visited lags are multivariate
  hypergeometric; given them the specials are a uniform placement, whose mean of exp(-s^2 ...) is M_{h1,h2}, built by
      M_{h1,h2}(t) = ((t-h1-h2)/t) M_{h1,h2}(t-1) + (h1/t) z1_t M_{h1-1,h2}(t-1) + (h2/t) z2_t M_{h1,h2-1}(t-1).
  Each earlier epoch: G(y) = M_{m1,m2} over n consecutive lags with z_T,t = exp(-y a_T beta2^t), tabulated in log y for the
  current x (the ratio a2/a1 depends on x) and splined.
The root is found by secant from the closed-form prediction, so a run costs four to six tables.
usage: python rrm3v.py N BETA2 [B1V B2V BO] [SNODES] [YGRID]
"""
import math
import sys

import numpy as np
from scipy.interpolate import CubicSpline
from scipy.special import gammaln


def K_rr_b1zero(n, b2):
    j = np.arange(1, n)
    return 1.0 - np.sum((n - j) * b2 ** j) / (n * (n - 1))


def step(M, t, z1, z2):
    """One slot of the two-type placement recursion. M has shape (m1+1, m2+1, ...)."""
    m1, m2 = M.shape[0] - 1, M.shape[1] - 1
    h1 = np.arange(m1 + 1)[:, None, None]
    h2 = np.arange(m2 + 1)[None, :, None]
    new = np.clip((t - h1 - h2) / t, 0.0, None) * M
    new[1:] += (h1[1:] / t) * z1 * M[:-1]
    new[:, 1:] += (h2[:, 1:] / t) * z2 * M[:, :-1]
    return new


def mvhyper(c1, c2, c0, p, m1, m2):
    """P(h1, h2) for p draws from c1 + c2 + c0 without replacement, as an (m1+1, m2+1) array."""
    h1 = np.arange(m1 + 1)[:, None]
    h2 = np.arange(m2 + 1)[None, :]
    h0 = p - h1 - h2
    ok = (h1 <= c1) & (h2 <= c2) & (h0 >= 0) & (h0 <= c0)
    lc = lambda a, b: gammaln(a + 1) - gammaln(b + 1) - gammaln(a - b + 1)
    with np.errstate(invalid="ignore"):
        lp = lc(c1, np.minimum(h1, c1)) + lc(c2, np.minimum(h2, c2)) + lc(c0, np.clip(h0, 0, c0)) - lc(c1 + c2 + c0, p)
    return np.where(ok, np.exp(lp), 0.0)


class Solver3:
    def __init__(self, n, b2, bv=(6.0, 2.0, -1.0), snodes=200, ygrid=1200):
        self.n, self.b2, self.bv = n, b2, bv
        self.m1 = self.m2 = n // 10
        assert self.m1 * 10 == n
        self.m0 = n - self.m1 - self.m2
        self.d = 1.0 - b2
        self.sx, self.sw = np.polynomial.legendre.leggauss(snodes)
        self.ygrid = ygrid
        m1, m2, m0 = self.m1, self.m2, self.m0
        # hypergeometric weights for the visited lags, by g_k's own type
        self.H = {}
        for T, (c1, c2, c0) in {1: (m1 - 1, m2, m0), 2: (m1, m2 - 1, m0), 0: (m1, m2, m0 - 1)}.items():
            self.H[T] = np.array([mvhyper(c1, c2, c0, p, m1, m2) for p in range(n)])

    def table(self, a1, a2):
        n, b2 = self.n, self.b2
        lo, hi = -40.0, math.log(60.0 / self.q)
        ly = np.linspace(lo, hi, self.ygrid)
        y = np.exp(ly)
        M = np.zeros((self.m1 + 1, self.m2 + 1, y.size))
        M[0, 0] = 1.0
        lsc = np.zeros(y.size)
        for t in range(1, n + 1):
            M = step(M, t, np.exp(-y * a1 * b2 ** (t - 1)), np.exp(-y * a2 * b2 ** (t - 1)))
            mx = M.max(axis=(0, 1))
            M /= mx
            lsc += np.log(mx)
        lg = np.log(M[self.m1, self.m2]) + lsc
        slope0 = -(self.m1 * a1 + self.m2 * a2) / n * (1 - b2 ** n) / self.d
        return CubicSpline(ly, lg), lo, hi, slope0

    def drift(self, x):
        n, b2, d = self.n, self.b2, self.d
        bv = self.bv
        self.q = q = (x + bv[2]) ** 2
        A = [(x + bv[0]) ** 2, (x + bv[1]) ** 2]
        a1, a2 = d * (A[0] - q), d * (A[1] - q)
        spl, lo, hi, slope0 = self.table(a1, a2)

        def logG(y):
            out = np.empty_like(y)
            small = y < math.exp(lo)
            out[small] = slope0 * y[small]
            ly = np.log(np.maximum(y[~small], 1e-300))
            assert np.all(ly <= hi + 1e-9), "extend the y grid"
            out[~small] = spl(ly)
            return out

        smax = math.sqrt(50.0 / q)
        s = 0.5 * smax * (self.sx + 1.0)
        ws = 0.5 * smax * self.sw
        u = s * s
        base = np.exp(-u * q)
        L = np.arange(1, n + 1)
        logP = np.zeros((n, s.size))
        e = 0
        while True:
            y = u[None, :] * b2 ** (L[:, None] + e * n).astype(float)
            if y.max() * max(a1, a2) < 1e-18:
                break
            logP += logG(y.ravel()).reshape(y.shape)
            e += 1
        M = np.zeros((self.m1 + 1, self.m2 + 1, s.size))
        M[0, 0] = 1.0
        z0 = {1: np.exp(-u * a1), 2: np.exp(-u * a2), 0: np.ones_like(u)}
        I = {1: np.empty(n), 2: np.empty(n), 0: np.empty(n)}
        for p in range(n):
            if p >= 1:
                M = step(M, p, np.exp(-u * a1 * b2 ** p), np.exp(-u * a2 * b2 ** p))
            Pp = np.exp(logP[p])
            for T in (1, 2, 0):
                f = np.tensordot(self.H[T][p], M, axes=([0, 1], [0, 1]))
                I[T][p] = (2 / math.sqrt(math.pi)) * np.sum(ws * base * z0[T] * f * Pp)
        P = {1: self.m1 / n, 2: self.m2 / n, 0: self.m0 / n}
        g = {1: x + bv[0], 2: x + bv[1], 0: x + bv[2]}
        return sum(P[T] * g[T] * I[T].mean() for T in (1, 2, 0))


if __name__ == "__main__":
    n, b2 = int(sys.argv[1]), float(sys.argv[2])
    bv = tuple(float(v) for v in sys.argv[3:6]) if len(sys.argv) > 5 else (6.0, 2.0, -1.0)
    sn = int(sys.argv[6]) if len(sys.argv) > 6 else 200
    yg = int(sys.argv[7]) if len(sys.argv) > 7 else 1200
    p = np.array([0.1, 0.1, 0.8])
    b = np.array(bv)
    B2, B3 = p @ b ** 2, p @ b ** 3
    S = Solver3(n, b2, bv, sn, yg)
    d = 1 - b2
    K = K_rr_b1zero(n, b2)
    x0 = d * K * B3 / (2 * B2)
    xa, xb = x0 * (1 - 0.6 * d), x0 * (1 - 0.6 * d) * (1 + 0.3 * d)
    fa, fb = S.drift(xa), S.drift(xb)
    for it in range(12):
        if fb == fa or fb == 0.0:
            break
        xc = xb - fb * (xb - xa) / (fb - fa)
        if abs(xc - xb) < 1e-13 * abs(xb):
            xb = xc
            break
        xa, fa, xb, fb = xb, fb, xc, S.drift(xc)
    print("THREE n %d beta2 %g nd %g b %s snodes %d ygrid %d: K %.12f x0 %.12g x* %.14g (x*/x0-1)/d %.6f  [%d secant steps]"
          % (n, b2, n * d, list(bv), sn, yg, K, x0, xb, (xb / x0 - 1) / d, it + 1), flush=True)
