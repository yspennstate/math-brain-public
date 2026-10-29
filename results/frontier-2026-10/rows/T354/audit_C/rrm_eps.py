"""Exact root of the frozen-x drift E[g/(sqrt(v) + eps)] under random reshuffling at any n, eps >= 0 (agent C, 20 Oct 2026).

Audit of the eps > 0 sentence of agent_B/NOTE.md, "The remainder, uniform in n" (push 59a1d8df). Same model and route as
rrm_indep.py (b = 9 on n/10 samples, -1 on the rest, beta1 = 0, frozen x). The only change is the kernel:
    1/(sqrt(v) + eps) = (2/sqrt(pi)) int_0^inf h(s) exp(-s^2 v) ds,   h(s) = 1 - eps sqrt(pi) s erfcx(eps s),
which is k(u) = (pi u)^(-1/2) [1 - eps sqrt(pi u) erfcx(eps sqrt(u))] after u = s^2. The script checks this on a grid of v first.

usage: python rrm_eps.py root N BETA2 EPS        -> x*, and (x*/(r x0) - 1)/d with r = 3/(3 + eps)
       python rrm_eps.py e2 N BETA2 EPS X        -> E2 = N(x) - x - p1 d K (2 x B2 + B3)/V at x, N = (s + eps) D, s = sqrt(V)
       python rrm_eps.py kernel EPS
"""
import math
import sys

import numpy as np
from scipy.optimize import brentq
from scipy.special import erfcx

from rrm_indep import Solver, K_rr_b1zero


def h(s, eps):
    return 1.0 - eps * math.sqrt(math.pi) * s * erfcx(eps * s)


class EpsSolver(Solver):
    def __init__(self, n, b2, eps, snodes=200, ygrid=2400):
        super().__init__(n, b2, snodes, ygrid)
        self.eps = eps

    def drift(self, x):
        n, m, b2, d = self.n, self.m, self.b2, self.d
        A, q = (x + 9.0) ** 2, (x - 1.0) ** 2
        smax = math.sqrt(50.0 / q)
        s = 0.5 * smax * (self.sx + 1.0)
        ws = 0.5 * smax * self.sw * h(s, self.eps)
        w = s * s * d * (A - q)
        base = np.exp(-s * s * q)
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
        Mh = np.zeros((m + 1, s.size))
        Mh[0] = 1.0
        z0 = np.exp(-w)
        Is = np.empty(n)
        Io = np.empty(n)
        for p in range(n):
            if p >= 1:
                z = np.exp(-w * b2 ** p)
                hmax = min(p, m)
                hh = np.arange(1, hmax + 1)[:, None]
                Mh[1:hmax + 1] = ((p - hh) / p) * Mh[1:hmax + 1] + (hh / p) * z * Mh[0:hmax]
            fs = self.Hs[p] @ Mh
            fo = self.Ho[p] @ Mh
            Pp = np.exp(logP[p])
            Is[p] = (2 / math.sqrt(math.pi)) * np.sum(ws * base * z0 * fs * Pp)
            Io[p] = (2 / math.sqrt(math.pi)) * np.sum(ws * base * fo * Pp)
        return (m / n) * (x + 9.0) * Is.mean() + (1 - m / n) * (x - 1.0) * Io.mean()


def kernel_check(eps, snodes=200):
    sx, sw = np.polynomial.legendre.leggauss(snodes)
    worst = 0.0
    for x in (0.0, 0.1):
        q = (x - 1) ** 2
        smax = math.sqrt(50.0 / q)
        s = 0.5 * smax * (sx + 1.0)
        ws = 0.5 * smax * sw * h(s, eps)
        for v in np.linspace(q, (x + 9) ** 2, 41):
            val = (2 / math.sqrt(math.pi)) * np.sum(ws * np.exp(-s * s * v))
            worst = max(worst, abs(val * (math.sqrt(v) + eps) - 1))
    print("KERNEL eps %g: max relative error of the quadrature for 1/(sqrt v + eps), v in [q, A], x 0 and 0.1: %.2e" % (eps, worst))


if __name__ == "__main__":
    mode = sys.argv[1]
    if mode == "kernel":
        kernel_check(float(sys.argv[2]))
        sys.exit()
    n, b2, eps = int(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4])
    S = EpsSolver(n, b2, eps)
    d = 1 - b2
    K = K_rr_b1zero(n, b2)
    if mode == "root":
        x0 = d * K * 72.0 / 18.0
        r = 3.0 / (3.0 + eps)
        xs = brentq(S.drift, 0.3 * r * x0, 1.7 * r * x0, xtol=1e-16, rtol=1e-13)
        print("EPSROOT n %d beta2 %g nd %g eps %g: K %.12f r x0 %.12g x* %.12g (x*/(r x0)-1)/d %.6f"
              % (n, b2, n * d, eps, K, r * x0, xs, (xs / (r * x0) - 1) / d), flush=True)
    elif mode == "e2":
        x = float(sys.argv[5])
        V = x * x + 9.0
        s = math.sqrt(V)
        p1 = -0.5 * s / (s + eps)
        N = (s + eps) * S.drift(x)
        E2 = N - x - p1 * d * K * (2 * x * 9.0 + 72.0) / V
        print("EPSE2 n %d beta2 %g nd %g eps %g x %g: E2 %.10e" % (n, b2, n * d, eps, x, E2), flush=True)
