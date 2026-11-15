"""A monotone function with a hidden coordinate (FLOW 12(u)).

f(x, y) = MAJ_k(y) OR (x AND [y >= y0]),  y0 a fixed point of weight (k-1)/2, k odd.
f is monotone; x lies in one term of width (k+1)/2, the same width as every term of MAJ_k.
D_x f = 1[y = y0], so Inf_x = 2^-k, and the spectrum of D_x f is flat while the spectrum of E_x f is that of
majority plus a flat perturbation. Prediction: E_x / Inf_x ~ k/2.

Prints, for each odd k, Inf and E_i/Inf_i for x and for the two kinds of y variable (y0_j = 1, y0_j = 0).
Usage: python mono_hidden.py K [K ...]
"""
import sys
import numpy as np


def wht(v):
    v = v.astype(np.float64).copy()
    n = v.size.bit_length() - 1
    h = 1
    while h < v.size:
        v = v.reshape(-1, 2, h)
        a = v[:, 0, :] + v[:, 1, :]
        b = v[:, 0, :] - v[:, 1, :]
        v = np.stack([a, b], axis=1).reshape(-1)
        h *= 2
    return v / v.size


def phi(p, q):
    s = p + q
    out = np.zeros_like(s)
    for a in (p, q):
        m = a > 0
        out[m] -= a[m] * np.log2(a[m] / s[m])
    return out


def erasure(mu, n):
    idx = np.arange(mu.size)
    res = []
    for i in range(n):
        lo = idx[(idx >> i) & 1 == 0]
        p, q = mu[lo], mu[lo | (1 << i)]
        res.append((q.sum(), phi(p, q).sum()))
    return res


def build(k):
    n = k + 1
    N = 1 << n
    idx = np.arange(N)
    x = (idx >> k) & 1
    y = idx & ((1 << k) - 1)
    wt = np.zeros(N, dtype=np.int64)
    for j in range(k):
        wt += (idx >> j) & 1
    y0 = (1 << ((k - 1) // 2)) - 1          # the first (k-1)/2 variables are one
    maj = wt >= (k + 1) // 2
    ge = (y & y0) == y0
    f = maj | ((x == 1) & ge)
    return n, np.where(f, -1.0, 1.0)


def main():
    for k in [int(t) for t in sys.argv[1:]]:
        n, f = build(k)
        mu = wht(f) ** 2
        er = erasure(mu, n)
        I = sum(a for a, _ in er)
        H = -(mu[mu > 0] * np.log2(mu[mu > 0])).sum()
        row = lambda i: "Inf=%.3e E/Inf=%.4f" % (er[i][0], er[i][1] / er[i][0])
        print("k=%d n=%d  H/I=%.4f  x: %s | y in y0: %s | y not in y0: %s | min_i E/Inf=%.4f" % (
            k, n, H / I, row(k), row(0), row(k - 1), min(b / a for a, b in er)), flush=True)


if __name__ == "__main__":
    main()
