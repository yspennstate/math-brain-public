"""Exact frozen-x drift and root x* under random reshuffling, beta1 >= 0, eps = 0, for b with TWO special values
(agent C, 20 Oct 2026, T354 audit of the RR next-order term). b = (b1v, b2v, bo x (n-2)), mean 0.
Generalizes rr_exact_mom_eps.py (one special sample) to two: in every epoch the positions (q1, q2) of the two special
samples are a uniform ordered pair of distinct positions, independent across epochs. With c = beta2^lag, a = beta1^lag,
  v = go^2 + d sum_occurrences c (gi^2 - go^2),   m = go + (1 - beta1) sum_occurrences a (gi - go),
1/sqrt(v) = (2/sqrt pi) int_0^inf e^(-t^2 v) dt, and e^(-t^2 v) factorizes over epochs. Far epochs (beta2^(mn) < 1e-3) enter
log prod F through the first four cumulants of X = dv1 beta2^(p-q1) + dv2 beta2^(p-q2) over the pair.
usage: python rr_exact_two_special.py BETA1 BETA2 B1V B2V BO [NODES]"""
import math
import sys
import numpy as np
from scipy.optimize import brentq

n = 10


def D(x, b1, b2, bv, Nt=160, T=6.5):
    d = 1 - b2
    g1, g2, go = x + bv[0], x + bv[1], x + bv[2]
    dg = np.array([g1 - go, g2 - go])
    dv = np.array([g1 * g1 - go * go, g2 * g2 - go * go])
    tn, tw = np.polynomial.legendre.leggauss(Nt)
    t = (tn + 1) * T / 2
    w = tw * T / 2 * 2 / math.sqrt(math.pi)
    u = t * t
    Q1, Q2 = [a.ravel() for a in np.meshgrid(np.arange(n), np.arange(n), indexing="ij")]
    keep = Q1 != Q2
    Q1, Q2 = Q1[keep], Q2[keep]  # the n(n-1) ordered pairs
    M0 = int(math.ceil(math.log(1e3) / (-n * math.log(b2))))
    Mb = 0 if b1 == 0 else int(math.ceil(40 / (-n * math.log(b1)))) + 1
    M0 = max(M0, Mb)
    mm = np.arange(1, M0 + 1)
    tot = 0.0
    for p in range(n):
        logF = np.zeros(Nt)
        GF = np.zeros(Nt)
        for lo in range(0, M0, 200):
            ms = mm[lo:lo + 200]
            lag1 = p + ms[:, None] * n - Q1[None, :]
            lag2 = p + ms[:, None] * n - Q2[None, :]
            X = dv[0] * b2 ** lag1 + dv[1] * b2 ** lag2  # (M, P)
            E = np.exp(-u[:, None, None] * d * X[None])  # (Nt, M, P)
            F = E.mean(axis=2)
            logF += np.log(F).sum(axis=1)
            if Mb and lo < Mb:
                k = min(Mb - lo, len(ms))
                A = dg[0] * b1 ** lag1[:k] + dg[1] * b1 ** lag2[:k]
                GF += ((E[:, :k, :] * A[None]).mean(axis=2) / F[:, :k]).sum(axis=1)
        Xp = dv[0] * b2 ** (p - Q1).astype(float) + dv[1] * b2 ** (p - Q2).astype(float)
        mu = Xp.mean()
        c2, c3, c4 = [np.mean((Xp - mu) ** j) for j in (2, 3, 4)]
        kap = [mu, c2, c3, c4 - 3 * c2 * c2]
        for j in range(1, 5):
            tail = b2 ** (j * (M0 + 1) * n) / (1 - b2 ** (j * n))
            logF += kap[j - 1] * (-u * d) ** j / math.factorial(j) * tail
        # current epoch: special i at q_i contributes to v if q_i <= p, to m with weight beta1^(p - q_i) (beta1 = 0: q_i == p)
        for q1, q2 in zip(Q1, Q2):
            c0 = sum(dv[i] * b2 ** (p - q) for i, q in enumerate((q1, q2)) if q <= p)
            if b1 > 0:
                a0 = sum(dg[i] * b1 ** (p - q) for i, q in enumerate((q1, q2)) if q <= p)
            else:
                a0 = sum(dg[i] for i, q in enumerate((q1, q2)) if q == p)
            br = go + (1 - b1) * (a0 + GF)
            tot += np.dot(w, np.exp(-u * (go * go + d * c0) + logF) * br)
    return tot / (n * len(Q1))


def K_rr(b1, b2):
    sys.path.insert(0, "../agent_B")
    from kfactor import K_rr as K
    return K(n, b1, b2)


if __name__ == "__main__":
    b1, b2 = float(sys.argv[1]), float(sys.argv[2])
    bv = [float(s) for s in sys.argv[3:6]]
    Nt = int(sys.argv[6]) if len(sys.argv) > 6 else 160
    full = np.array([bv[0], bv[1]] + [bv[2]] * (n - 2))
    assert abs(full.mean()) < 1e-12, "b must have mean 0"
    B2, B3 = np.mean(full ** 2), np.mean(full ** 3)
    K = K_rr(b1, b2)
    x0 = (1 - b2) * K * B3 / (2 * B2)
    xs = brentq(lambda x: D(x, b1, b2, bv, Nt), 0.3 * x0, 1.7 * x0, xtol=1e-16, rtol=1e-14)
    print("RR2 b %s beta1 %g beta2 %g nodes %d: K %.9f x0 %.9g x* %.12g  (x*/x0-1)/d %.6f"
          % (bv, b1, b2, Nt, K, x0, xs, (xs / x0 - 1) / (1 - b2)), flush=True)
