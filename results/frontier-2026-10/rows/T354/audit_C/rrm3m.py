"""rrm3v.py with momentum: exact root of the frozen-x Adam drift E[m_k/sqrt(v_k)] under random reshuffling, three-valued b, any
beta1 (agent C, 20 Oct 2026). Second audit of agent_B/NOTE.md "Momentum, uniform in n" and of "the same c holds at
every fixed beta1" (c(n d) in closed form), on a b with r1 != r2.

m_k = sum_i w_i g_{k-i}, w_i = (1 - beta1) beta1^i. With exp(-u v) factorized over epochs given u, the b-part of the numerator is
the lambda-derivative at 0 of the same placement mean with z_T,t replaced by z_T,t (1 + lambda w_t b_T). So each placement table M
gets a companion N built by the same recursion,
    N_h(t) = ((t-h1-h2)/t) (N + w_t b0 M)_h(t-1) + (h1/t) z1 (N + w_t b1 M)_{h-e1}(t-1) + (h2/t) z2 (N + w_t b2 M)_{h-e2}(t-1),
and an earlier epoch contributes f * beta1^(p + e n) R(y), R = N/M of its table with relative weights (1 - beta1) beta1^t.
usage: python rrm3m.py N BETA2 BETA1 [B1V B2V BO]; EPS=e in the environment runs the kernel 1/(sqrt(v) + eps) of rrm_eps.py and
reports (x*/(r x0) - 1)/d with r = sqrt(B2)/(sqrt(B2) + eps).
"""
import math
import os
import sys

import numpy as np
from scipy.interpolate import CubicSpline
from scipy.special import erfcx

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "agent_B"))
from kfactor import K_rr  # noqa: E402

from rrm3v import Solver3, step  # noqa: E402


def step2(M, N, t, z1, z2, wt, bv):
    """step() for M together with its momentum companion N."""
    m1, m2 = M.shape[0] - 1, M.shape[1] - 1
    h1 = np.arange(m1 + 1)[:, None, None]
    h2 = np.arange(m2 + 1)[None, :, None]
    A0 = N + wt * bv[2] * M
    A1 = N + wt * bv[0] * M
    A2 = N + wt * bv[1] * M
    new = np.clip((t - h1 - h2) / t, 0.0, None) * A0
    new[1:] += (h1[1:] / t) * z1 * A1[:-1]
    new[:, 1:] += (h2[:, 1:] / t) * z2 * A2[:, :-1]
    return step(M, t, z1, z2), new


class Solver3M(Solver3):
    def __init__(self, n, b2, b1, bv=(6.0, 2.0, -1.0), snodes=200, ygrid=1200):
        super().__init__(n, b2, bv, snodes, ygrid)
        self.b1 = b1
        self.eps = float(os.environ.get("EPS", "0"))

    def table2(self, a1, a2):
        n, b2, b1 = self.n, self.b2, self.b1
        lo, hi = -40.0, math.log(60.0 / self.q)
        ly = np.linspace(lo, hi, self.ygrid)
        y = np.exp(ly)
        M = np.zeros((self.m1 + 1, self.m2 + 1, y.size))
        M[0, 0] = 1.0
        N = np.zeros_like(M)
        lsc = np.zeros(y.size)
        for t in range(1, n + 1):
            M, N = step2(M, N, t, np.exp(-y * a1 * b2 ** (t - 1)), np.exp(-y * a2 * b2 ** (t - 1)), (1 - b1) * b1 ** t, self.bv)
            mx = M.max(axis=(0, 1))
            M /= mx
            N /= mx
            lsc += np.log(mx)
        lg = np.log(M[self.m1, self.m2]) + lsc
        R = N[self.m1, self.m2] / M[self.m1, self.m2]
        slope0 = -(self.m1 * a1 + self.m2 * a2) / n * (1 - b2 ** n) / self.d
        return CubicSpline(ly, lg), CubicSpline(ly, R), lo, hi, slope0

    def drift(self, x):
        n, b2, b1, d, bv = self.n, self.b2, self.b1, self.d, self.bv
        self.q = q = (x + bv[2]) ** 2
        a1, a2 = d * ((x + bv[0]) ** 2 - q), d * ((x + bv[1]) ** 2 - q)
        spl, splR, lo, hi, slope0 = self.table2(a1, a2)
        ylo = math.exp(lo)
        Rlo = float(splR(lo))

        def ev(y):
            lg, R = np.empty_like(y), np.empty_like(y)
            small = y < ylo
            lg[small] = slope0 * y[small]
            R[small] = Rlo * y[small] / ylo
            ly = np.log(np.maximum(y[~small], 1e-300))
            assert np.all(ly <= hi + 1e-9), "extend the y grid"
            lg[~small] = spl(ly)
            R[~small] = splR(ly)
            return lg, R

        smax = math.sqrt(50.0 / q)
        s = 0.5 * smax * (self.sx + 1.0)
        ws = 0.5 * smax * self.sw * (1.0 - self.eps * math.sqrt(math.pi) * s * erfcx(self.eps * s))
        u = s * s
        base = np.exp(-u * q)
        L = np.arange(1, n + 1)
        logP = np.zeros((n, s.size))
        Rsum = np.zeros((n, s.size))
        e = 0
        while True:
            y = u[None, :] * b2 ** (L[:, None] + e * n).astype(float)
            mw = b1 ** (L[:, None] - 1 + e * n).astype(float) if b1 > 0 else np.zeros_like(y)
            if y.max() * max(a1, a2) < 1e-18 and mw.max() < 1e-18:
                break
            lg, R = ev(y.ravel())
            logP += lg.reshape(y.shape)
            Rsum += mw * R.reshape(y.shape)
            e += 1
        M = np.zeros((self.m1 + 1, self.m2 + 1, s.size))
        M[0, 0] = 1.0
        N = np.zeros_like(M)
        z0 = {1: np.exp(-u * a1), 2: np.exp(-u * a2), 0: np.ones_like(u)}
        bT = {1: bv[0], 2: bv[1], 0: bv[2]}
        I = {T: np.empty(n) for T in (1, 2, 0)}
        J = {T: np.empty(n) for T in (1, 2, 0)}
        c = 2 / math.sqrt(math.pi)
        for p in range(n):
            if p >= 1:
                M, N = step2(M, N, p, np.exp(-u * a1 * b2 ** p), np.exp(-u * a2 * b2 ** p), (1 - b1) * b1 ** p, bv)
            Pp = np.exp(logP[p])
            for T in (1, 2, 0):
                f = np.tensordot(self.H[T][p], M, axes=([0, 1], [0, 1]))
                g = np.tensordot(self.H[T][p], N, axes=([0, 1], [0, 1]))
                common = ws * base * z0[T] * Pp
                I[T][p] = c * np.sum(common * f)
                J[T][p] = c * np.sum(common * ((1 - b1) * bT[T] * f + g + f * Rsum[p]))
        P = {1: self.m1 / n, 2: self.m2 / n, 0: self.m0 / n}
        return sum(P[T] * (x * I[T].mean() + J[T].mean()) for T in (1, 2, 0))


if __name__ == "__main__":
    n, b2, b1 = int(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3])
    bv = tuple(float(v) for v in sys.argv[4:7]) if len(sys.argv) > 6 else (6.0, 2.0, -1.0)
    p = np.array([0.1, 0.1, 0.8])
    b = np.array(bv)
    B2, B3 = p @ b ** 2, p @ b ** 3
    S = Solver3M(n, b2, b1, bv)
    d = 1 - b2
    K = K_rr(n, b1, b2)
    x0 = d * K * B3 / (2 * B2) * math.sqrt(B2) / (math.sqrt(B2) + S.eps)
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
    print("THREEM n %d beta2 %g beta1 %g eps %g nd %g b %s: K %.12f x0 %.12g x* %.14g (x*/x0-1)/d %.6f  [%d secant steps]"
          % (n, b2, b1, S.eps, n * d, list(bv), K, x0, xb, (xb / x0 - 1) / d, it + 1), flush=True)
