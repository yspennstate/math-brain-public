"""Predictor bound of predictor.py for majority on n variables (n odd), by the closed form of its spectrum.

Maj_n: fhat(S)^2 = [C(h, (k-1)/2) / C(n-1, k-1)]^2 * [2^(1-n) C(n-1, h)]^2 for |S| = k odd, h = (n-1)/2; zero for k even
(O'Donnell, Analysis of Boolean Functions, Theorem 5.19). Everything depends on |T| only, so
    up_lam(k) = sum_{j >= k} C(n-k, j-k) mu_j lam^(j-k),
    K I    = sum_k C(n,k) (n-k) (mu_k + mu_{k+1}) p_k,
    cost I = sum_k C(n,k) (n-k) mu_{k+1} log2(1 / p_k),
with p_k one of the three predictors of predictor.py. Log domain throughout (float64).
The exact erasure cost L is 0 for majority (odd function), so the printed bound is pure overhead.

Usage: python predictor_sym.py [n ...]
"""
import math
import sys

import numpy as np
from scipy.special import gammaln, logsumexp


def logc(a, b):
    return gammaln(a + 1) - gammaln(b + 1) - gammaln(a - b + 1)


def run(n, lams=(0.1, 0.25, 0.5, 0.75)):
    h = (n - 1) // 2
    k = np.arange(n + 1)
    lmu = np.full(n + 1, -np.inf)
    odd = k[k % 2 == 1]
    base = 2 * (math.log(2.0) * (1 - n) + logc(n - 1, h))
    lmu[odd] = 2 * (logc(h, (odd - 1) // 2) - logc(n - 1, odd - 1)) + base
    lW = lmu + logc(n, k)
    I = float(np.exp(logsumexp(lW[1:] + np.log(k[1:]))))
    tot = float(np.exp(logsumexp(lW)))
    res = []
    for lam in lams:
        lup = np.empty(n + 1)
        for kk in range(n + 1):
            j = np.arange(kk, n + 1)
            lup[kk] = logsumexp(lmu[j] + logc(n - kk, j - kk) + (j - kk) * math.log(lam))
        kk = np.arange(n)
        lpairs = logc(n, kk) + np.log(n - kk)
        lr = lup[kk + 1] - lup[kk]
        r = np.exp(lr)
        preds = {
            "thin": (1 - lam) * r / (1.0 + (1 - lam) * r),
            "ratio": np.minimum(1.0, r),
            "lrat": lam * r,
        }
        lnu = np.logaddexp(lmu[kk], lmu[kk + 1])
        for name, p in preds.items():
            KI = float(np.exp(logsumexp(lpairs + lnu + np.log(p))))
            m = np.isfinite(lmu[kk + 1])
            cI = float((np.exp(lpairs[m] + lmu[kk + 1][m]) * np.log2(1.0 / p[m])).sum())
            res.append((lam, name, math.log2(KI / I), cI / I))
    return I, tot, res


def main():
    ns = [int(a) for a in sys.argv[1:]] or [5, 9, 13, 51, 201, 801, 3201]
    for n in ns:
        I, tot, res = run(n)
        best = min(res, key=lambda t: t[2] + t[3])
        print("maj n %5d  I %.4f  sum mu %.6f  best %s@%.2f %.3f" % (n, I, tot, best[1], best[0], best[2] + best[3]))
        print("   " + "  ".join("%s@%.2f %.3f(=%.2f+%.2f)" % (nm, lam, a + b, a, b) for lam, nm, a, b in res))
        sys.stdout.flush()


if __name__ == "__main__":
    main()
