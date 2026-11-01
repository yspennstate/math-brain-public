"""Exact frozen-x drift and root x* under random reshuffling, with momentum and eps (agent C, 20 Oct 2026, T354 audit).
Test model only: n = 10, b = (9, -1 x 9), a = 1. With the step at position p of its epoch and the special sample at q_0 in the
current epoch and q_m in the m-th earlier one (independent, uniform on 0..n-1):
  m = g_o + (g_s - g_o)(1 - b1)[b1^(p-q0) 1{q0<=p} + sum_m b1^(p+mn-q_m)],
  v = g_o^2 + d (g_s^2 - g_o^2)[b2^(p-q0) 1{q0<=p} + sum_m b2^(p+mn-q_m)].
1/(sqrt v + eps) = int_0^inf h(t) e^(-t^2 v) dt, h(t) = (2/sqrt pi)[1 - eps sqrt(pi) t erfcx(eps t)], so the earlier epochs
factorize: E[m e^(-uv)] = e^(-u(g_o^2 + d dv c0)) prod F_m [g_o + dg (1-b1)(a0 + sum G_m/F_m)], F_m = E_q e^(-u d dv b2^(p+mn-q)),
G_m = E_q b1^(p+mn-q) e^(...). Epochs with b2^(mn) < 1e-3 enter log prod F through the first four cumulants of b2^(p-q).
usage: python rr_exact_mom_eps.py BETA1 BETA2 EPS [NODES]"""
import math
import sys
import numpy as np
from scipy.optimize import brentq
from scipy.special import erfcx

n = 10


def D(x, b1, b2, eps, Nt=160, T=6.5):
    d = 1 - b2
    gs, go = x + 9.0, x - 1.0
    dg, dv = gs - go, gs * gs - go * go
    tn, tw = np.polynomial.legendre.leggauss(Nt)
    t = (tn + 1) * T / 2
    w = tw * T / 2
    h = (2 / math.sqrt(math.pi)) * (1 - eps * math.sqrt(math.pi) * t * erfcx(eps * t))
    u = t * t
    M0 = int(math.ceil(math.log(1e3) / (-n * math.log(b2))))
    Mb = 0 if b1 == 0 else int(math.ceil(40 / (-n * math.log(b1)))) + 1
    M0 = max(M0, Mb)  # the momentum sum needs its epochs explicit too
    q = np.arange(n)
    mm = np.arange(1, M0 + 1)
    tot = 0.0
    for p in range(n):
        logF = np.zeros(Nt)
        GF = np.zeros(Nt)
        for lo in range(0, M0, 500):  # chunks of epochs
            ms = mm[lo:lo + 500]
            cm = b2 ** (p + ms[:, None] * n - q[None, :])  # (M, n)
            E = np.exp(-u[:, None, None] * (d * dv) * cm[None])  # (Nt, M, n)
            F = E.mean(axis=2)
            logF += np.log(F).sum(axis=1)
            if Mb and lo < Mb:
                k = min(Mb - lo, len(ms))
                am = b1 ** (p + ms[:k, None] * n - q[None, :])
                GF += ((E[:, :k, :] * am[None]).mean(axis=2) / F[:, :k]).sum(axis=1)
        cp = b2 ** (p - q).astype(float)  # tail: epochs m > M0 through the cumulants of b2^(p-q)
        mu = cp.mean()
        c2, c3, c4 = [np.mean((cp - mu) ** j) for j in (2, 3, 4)]
        kap = [mu, c2, c3, c4 - 3 * c2 * c2]
        z = u * d * dv
        for j in range(1, 5):
            tail = b2 ** (j * (M0 + 1) * n) / (1 - b2 ** (j * n))
            logF += kap[j - 1] * (-z) ** j / math.factorial(j) * tail
        for q0 in range(n):
            c0 = b2 ** (p - q0) if q0 <= p else 0.0
            a0 = (b1 ** (p - q0) if q0 <= p else 0.0) if b1 > 0 else (1.0 if q0 == p else 0.0)
            br = go + dg * (1 - b1) * (a0 + GF)
            tot += np.dot(w, h * np.exp(-u * (go * go + d * dv * c0) + logF) * br)
    return tot / n ** 2


def K_rr(b1, b2):
    sys.path.insert(0, "../agent_B")
    from kfactor import K_rr as K
    return K(n, b1, b2)


if __name__ == "__main__":
    b1, b2, eps = float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3])
    Nt = int(sys.argv[4]) if len(sys.argv) > 4 else 160
    x0 = (1 - b2) * K_rr(b1, b2) * 4 * 3 / (3 + eps)
    xs = brentq(lambda x: D(x, b1, b2, eps, Nt), 0.3 * x0, 1.7 * x0, xtol=1e-15, rtol=1e-13)
    print("RR beta1 %g beta2 %g eps %g nodes %d: x0 %.6g  x* %.9g  x*/x0 %.6f" % (b1, b2, eps, Nt, x0, xs, xs / x0), flush=True)
