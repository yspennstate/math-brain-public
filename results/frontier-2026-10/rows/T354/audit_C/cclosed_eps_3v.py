"""eps > 0 version of c(s) (agent_B/NOTE.md "eps > 0 in closed form", 09:1x, candidate), evaluated for the three-valued b
(agent C, 20 Oct 2026). psi(y) = (sq + eps)/(sq sqrt(y) + eps), sq = sqrt(B2); r = sq/(sq + eps), p2 = psi''(1),
p3 = psi'''(1) taken by sympy here, not from c_closed_eps.py. Claimed:
    c(s) = r K - (p2/2) r1 avg Q - p2 r2 cb/(r K) - p3 r1 avg[k Q]/(r K),   x0 = r d K B3/(2 B2).
At eps = 0 this is cclosed_3v.py's c(s) (r 1, p2 3/4, p3 -15/8).
usage: python cclosed_eps_3v.py [EPS ...]
"""
import sys

import numpy as np
import sympy as sp

bv = np.array([6.0, 2.0, -1.0])
p = np.array([0.1, 0.1, 0.8])
B = {k: p @ bv ** k for k in (1, 2, 3, 4)}
r1 = (B[4] - B[2] ** 2) / B[2] ** 2
r2 = (p @ (bv * (bv ** 2 - B[2]) ** 2)) / (B[2] * B[3])
x, w = np.polynomial.legendre.leggauss(400)


def coeffs(eps):
    y = sp.Symbol("y")
    sq = sp.sqrt(sp.Rational(str(B[2])))
    psi = (sq + eps) / (sq * sp.sqrt(y) + eps)
    d = [float(sp.diff(psi, y, k).subs(y, 1)) for k in (1, 2, 3)]
    return -2 * d[0], d[1], d[2]


def c(s, eps):
    r, p2, p3 = coeffs(eps)
    t = 0.5 * s * (x + 1)
    ww = 0.5 * w
    em = 1 - np.exp(-t)
    k = 1 - em / s
    Q = 0.5 - em ** 2 / s - np.exp(-2 * t) * np.tanh(s / 2) / s
    cbi = 1 - 2 * em / s - (1 - np.exp(-2 * t)) / (2 * s) + 2 * em ** 2 / s ** 2
    K, aQ, cb, akQ = ww @ k, ww @ Q, ww @ cbi, ww @ (k * Q)
    return r * K - p2 / 2 * r1 * aQ - p2 * r2 * cb / (r * K) - p3 * r1 * akQ / (r * K), (r, p2, p3)


for eps in [float(e) for e in sys.argv[1:]] or [0.0, 1.0]:
    for s in (0.2, 1, 2, 5):
        v, (r, p2, p3) = c(s, eps)
        print("eps %g (r %.6f p2 %.6f p3 %.6f)  s %g  c %+.6f" % (eps, r, p2, p3, s, v))
