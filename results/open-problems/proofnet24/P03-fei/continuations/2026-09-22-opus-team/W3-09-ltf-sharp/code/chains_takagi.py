"""AND/OR chains (lexicographic threshold functions, decision lists) through the doubling map.

A chain of length n is determined by t = Pr[f true] = j/2^n, j odd.  With d(t) = min(t, 1-t) and T t = 2t mod 1,
    H(t) = sum_k 2^-k A(2 d(T^k t)),     I(t) = sum_k 2^-k 2 d(T^k t)   (= 2 Takagi(t)),
    A(p) = phi(p^2) + phi((1-p)^2) - phi((1-2p)^2)/2 + 4p(1-p),   phi(u) = u log2(1/u).
This file (1) checks the formula against the Walsh transform of the lexicographic LTF for every t = j/2^n, n <= 10,
(2) scans t for the largest H/I and (3) tabulates D(t) = 4 I(t) - H(t).
"""
import sys, math
import numpy as np
from ltfcore import ltf_HI


def phi(u):
    u = np.asarray(u, dtype=np.float64)
    out = np.zeros_like(u)
    m = u > 1e-300
    out[m] = -u[m] * np.log2(u[m])
    return out


def A(p):
    p = np.asarray(p, dtype=np.float64)
    return phi(p * p) + phi((1 - p) ** 2) - phi((1 - 2 * p) ** 2) / 2 + 4 * p * (1 - p)


def HI_t(t, depth=64):
    """Vectorised H(t), I(t) for real t in [0,1] (float, truncated after `depth` doublings)."""
    t = np.array(t, dtype=np.float64, copy=True)
    H = np.zeros_like(t)
    I = np.zeros_like(t)
    w = 1.0
    for k in range(depth):
        d = np.minimum(t, 1 - t)
        H += w * A(2 * d)
        I += w * 2 * d
        t = (2 * t) % 1.0
        w *= 0.5
    return H, I


def HI_dyadic(j, n):
    """Exact orbit for t = j/2^n (integer arithmetic for the orbit, floats for A)."""
    H = 0.0
    I = 0.0
    w = 1.0
    M = 1 << n
    while j % M != 0:
        d = min(j, M - j) / M
        H += w * float(A(2 * d))
        I += w * 2 * d
        j = (2 * j) % M
        w *= 0.5
    return H, I


def check_walsh(nmax=10):
    worst = 0.0
    for n in range(1, nmax + 1):
        w = np.array([2.0 ** i for i in range(n)])
        vals = np.sort(np.unique(np.array([sum(w[i] * (1 - 2 * ((x >> i) & 1)) for i in range(n)) for x in range(1 << n)])))
        for j in range(1, 1 << n):
            theta = 0.5 * (vals[j - 1] + vals[j])   # f = -1 (true) iff w.x <= theta: Pr[true] = j/2^n
            H, I, f, c = ltf_HI(w, theta)
            p_true = np.mean(f < 0)
            assert abs(p_true - j / 2 ** n) < 1e-12
            Hc, Ic = HI_dyadic(j, n)
            worst = max(worst, abs(H - Hc), abs(I - Ic))
    return worst


if __name__ == "__main__":
    print("max |Walsh - formula| over all lexicographic LTFs, n <= 10:", check_walsh(10))
    # all chains of length n: best H/I
    for n in [10, 12, 16, 20, 22, 24, 26]:
        M = 1 << n
        js = np.arange(1, M, 2, dtype=np.float64)
        H, I = HI_t(js / M, depth=n + 2)
        r = H / I
        k = int(np.argmax(r))
        print("n=%d best chain H/I=%.8f at t=%.10g (j=%d)  AND_n: %.8f" % (n, r[k], js[k] / M, int(js[k]), r[0]))
        sys.stdout.flush()
