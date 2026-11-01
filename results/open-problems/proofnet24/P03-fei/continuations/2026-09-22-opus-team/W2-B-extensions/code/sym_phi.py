"""Exact Phi = Sigma_r/I (order-independent) and H/I for majority Maj_n, n odd, from the closed-form
level weights W_k = C(n,k) fhat_k^2, fhat_k = (-1)^((k-1)/2) C(m,(k-1)/2)/C(2m,k-1) 2^{1-n} C(2m,m), n = 2m+1.
For a symmetric function Pr[i in S | |S| = k] = k/n, so Sigma_r = sum_k W_k (k/n) sum_{t=1}^n ln+(t/k)."""
import numpy as np
from math import lgamma, log
from fei_lib import coords, sgn, wht, HI, phi_min

def lchoose(a, b):
    return lgamma(a + 1) - lgamma(b + 1) - lgamma(a - b + 1)

def maj_levels(n):
    m = (n - 1) // 2
    ks = np.arange(1, n + 1, 2)
    lf = np.array([lchoose(m, (k - 1) // 2) - lchoose(2 * m, k - 1) + (1 - n) * log(2) + lchoose(2 * m, m) for k in ks])
    lW = np.array([lchoose(n, k) for k in ks]) + 2 * lf
    return ks, lW

def stats(n):
    ks, lW = maj_levels(n)
    W = np.exp(lW)
    I = float((ks * W).sum())
    # entropy: each k-set has fhat^2 = exp(2 lf) = W_k / C(n,k)
    lc = lW - np.array([lchoose(n, k) for k in ks])
    H = float(-(W * lc).sum() / log(2))
    tot = []
    for k in ks:
        # sum_{t=k}^n ln(t/k) = lgamma(n+1) - lgamma(k) - (n-k+1) ln k
        tot.append(lgamma(n + 1) - lgamma(k) - (n - k + 1) * log(k))
    Sig = float((W * ks / n * np.array(tot)).sum())
    return W.sum(), H / I, Sig / I

if __name__ == "__main__":
    with open("../logs/sym_phi.log", "w") as lg:
        n = 17
        X = coords(n); c = wht(sgn(X.sum(1))); H, I = HI(c, n); v, _ = phi_min(c, n)
        print("check n=17 via Walsh: H/I=%.6f Phi=%.6f" % (H / I, v / I), file=lg)
        for n in (17, 23, 101, 1001, 10001, 100001, 1000001):
            w, hi, ph = stats(n)
            print("Maj_%d: total weight %.12f  H/I=%.6f  Phi=%.6f" % (n, w, hi, ph), file=lg)
