"""Pseudo-likelihood form of FEI with predictors built from noisy derivative norms.

Notation: mu(S) = fhat(S)^2, I = sum |S| mu(S), Q(T, i) = mu(T + i) / I on pairs with i not in T.
Exact erasure cost (the "in" half):  L = E_Q log2(1 + mu(T) / mu(T + i)).  FEI holds iff L <= C for all Boolean f.

Variational principle (Gibbs inequality on pairs): for ANY p_i(T) >= 0 put K = (1/I) sum_i sum_{T without i}
(mu(T) + mu(T+i)) p_i(T). Then  L <= log2 K + E_Q log2(1 / p_i(T)),  with equality at
p_i(T) = mu(T+i) / (mu(T) + mu(T+i)).

Predictors tested, all functions of  up_lam(T) = sum_{U >= T} mu(U) lam^|U - T| = || T_sqrt(lam) D_T f ||^2 :
  thin   p = (1-lam) up(T+i) / (up(T) + (1-lam) up(T+i))     (the conditional law of the (1-lam)-thinned sample)
  ratio  p = min(1, up(T+i) / up(T))
  lrat   p = lam up(T+i) / up(T)                              (always <= 1)

Usage: python predictor.py            (runs the built-in families)
"""
import itertools
import math
import sys

import numpy as np


def wht(v):
    v = np.array(v, dtype=np.float64)
    n = v.size.bit_length() - 1
    h = 1
    while h < v.size:
        v = v.reshape(-1, 2, h)
        v = np.concatenate((v[:, 0, :] + v[:, 1, :], v[:, 0, :] - v[:, 1, :]), axis=1).reshape(-1)
        h *= 2
    return v / (1 << n)


def up_lam(mu, n, lam):
    up = mu.copy()
    idx = np.arange(1 << n)
    for i in range(n):
        lo = idx[(idx >> i) & 1 == 0]
        up[lo] += lam * up[lo | (1 << i)]
    return up


def analyse(f, n, lams=(0.25, 0.5, 0.75)):
    mu = wht(f) ** 2
    idx = np.arange(1 << n)
    pc = np.zeros(1 << n, dtype=np.int64)
    for i in range(n):
        pc += (idx >> i) & 1
    I = float((pc * mu).sum())
    H = float(-(mu[mu > 0] * np.log2(mu[mu > 0])).sum())
    exact = 0.0
    out = {}
    ups = {lam: up_lam(mu, n, lam) for lam in lams}
    acc = {(lam, k): [0.0, 0.0] for lam in lams for k in ("thin", "ratio", "lrat")}
    for i in range(n):
        lo = idx[(idx >> i) & 1 == 0]
        hi = lo | (1 << i)
        a = mu[lo]
        b = mu[hi]
        m = b > 0
        exact += float((b[m] * np.log2(1.0 + a[m] / b[m])).sum())
        nu = a + b
        for lam in lams:
            u0 = ups[lam][lo]
            u1 = ups[lam][hi]
            ok = u0 > 0
            r = np.zeros_like(u0)
            r[ok] = u1[ok] / u0[ok]
            preds = {
                "thin": (1 - lam) * r / (1.0 + (1 - lam) * r),
                "ratio": np.minimum(1.0, r),
                "lrat": lam * r,
            }
            for k, p in preds.items():
                acc[(lam, k)][0] += float((nu * p).sum())
                acc[(lam, k)][1] += float((b[m] * np.log2(1.0 / p[m])).sum())
    out["I"] = I
    out["H"] = H
    out["exact"] = exact / I
    for key, (ks, cs) in acc.items():
        out[key] = (math.log2(ks / I), cs / I)
    return out


def table_from(fn, n):
    x = np.arange(1 << n)
    bits = [((x >> i) & 1) for i in range(n)]
    return np.where(fn(bits), -1.0, 1.0)


def f_and(n):
    return table_from(lambda b: np.logical_and.reduce([bb == 1 for bb in b]), n)


def f_maj(n):
    return table_from(lambda b: sum(b) * 2 > n, n)


def f_tribes(w, s):
    def fn(b):
        t = np.zeros(b[0].shape, dtype=bool)
        for j in range(s):
            t |= np.logical_and.reduce([b[j * w + k] == 1 for k in range(w)])
        return t
    return table_from(fn, w * s)


def f_addr(k):
    n = k + (1 << k)
    def fn(b):
        a = np.zeros(b[0].shape, dtype=np.int64)
        for j in range(k):
            a |= b[j] << j
        res = np.zeros(b[0].shape, dtype=np.int64)
        for v in range(1 << k):
            res = np.where(a == v, b[k + v], res)
        return res == 1
    return table_from(fn, n)


def f_rand(n, seed, bias=0.5):
    rng = np.random.default_rng(seed)
    return np.where(rng.random(1 << n) < bias, -1.0, 1.0)


def compose(F, k, psi, m):
    n = k * m
    x = np.arange(1 << n)
    y = np.zeros_like(x)
    for j in range(k):
        blk = (x >> (j * m)) & ((1 << m) - 1)
        y |= (psi[blk] < 0).astype(np.int64) << j
    return F[y]


def f_pmk33():
    # perfect-matching function on K33: 9 edges (a, b), f = -1 iff the edge set contains a perfect matching
    perms = list(itertools.permutations(range(3)))
    def fn(b):
        t = np.zeros(b[0].shape, dtype=bool)
        for p in perms:
            t |= np.logical_and.reduce([b[3 * a + p[a]] == 1 for a in range(3)])
        return t
    return table_from(fn, 9)


def show(name, f, n):
    r = analyse(f, n)
    parts = []
    for lam in (0.25, 0.5, 0.75):
        for k in ("thin", "ratio", "lrat"):
            lk, c = r[(lam, k)]
            parts.append("%s@%.2f %.3f(=%.2f+%.2f)" % (k, lam, lk + c, lk, c))
    print("%-16s n %2d I %.4f H/I %.4f exact %.4f | %s" % (name, n, r["I"], r["H"] / r["I"], r["exact"], "  ".join(parts)))
    sys.stdout.flush()


def main():
    for n in (4, 8, 12, 14):
        show("and", f_and(n), n)
    for n in (5, 9, 13):
        show("maj", f_maj(n), n)
    for w, s in ((2, 2), (2, 4), (3, 3), (3, 4), (2, 6), (4, 3)):
        show("tribes%dx%d" % (w, s), f_tribes(w, s), w * s)
    for k in (1, 2, 3):
        show("addr%d" % k, f_addr(k), k + (1 << k))
    pm = f_pmk33()
    show("pmk33", pm, 9)
    m3 = f_maj(3)
    show("maj3^2", compose(m3, 3, m3, 3), 9)
    for seed in (1, 2):
        show("rand10", f_rand(10, seed), 10)
        show("rand10 b.1", f_rand(10, seed, 0.1), 10)
        show("rand12 b.02", f_rand(12, seed, 0.02), 12)


if __name__ == "__main__":
    main()
