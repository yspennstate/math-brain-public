"""het_test.py - check the unequal-bias composition rule of het_search.py against explicit truth tables.
Builds F(g_1,...,g_k) for random gates F and small children on disjoint variables, computes (p, G, J) of the
composite directly from its uniform Walsh transform, and compares with Gate.sweep + the rule.
"""
import itertools
import sys

import numpy as np

from het_search import Gate, pair_ops


def direct(tt):
    """tt: 0/1 array of length 2^n (1 means f = -1).  Returns p, G, J."""
    n = int(np.log2(len(tt)))
    a = 1.0 - 2.0 * tt.astype(np.float64)
    h = 1
    while h < len(a):
        a = a.reshape(-1, 2, h)
        lo, hi = a[:, 0, :].copy(), a[:, 1, :].copy()
        a[:, 0, :] = (lo + hi) / 2
        a[:, 1, :] = (lo - hi) / 2
        a = a.reshape(-1)
        h *= 2
    var = 1 - a[0] ** 2
    w = a * a / var
    w[0] = 0
    size = np.array([bin(t).count("1") for t in range(len(a))])
    nz = w > 1e-300
    return (1 - a[0]) / 2, float(-(w[nz] * np.log2(w[nz])).sum()), float((w * size).sum())


def compose(F_tt, kids):
    """kids: list of 0/1 truth tables on disjoint variable blocks; input j of F is 1 when kid j is 1."""
    ns = [int(np.log2(len(k))) for k in kids]
    N = sum(ns)
    out = np.zeros(1 << N, dtype=np.uint8)
    offs = np.cumsum([0] + ns)
    for x in range(1 << N):
        idx = 0
        for j, k in enumerate(kids):
            if k[(x >> offs[j]) & ((1 << ns[j]) - 1)]:
                idx |= 1 << j
        out[x] = F_tt[idx]
    return out


def main():
    rng = np.random.default_rng(int(sys.argv[1]) if len(sys.argv) > 1 else 7)
    pool = []
    for n in (1, 2, 3):
        for _ in range(6):
            tt = rng.integers(0, 2, size=1 << n).astype(np.uint8)
            if 0 < tt.sum() < len(tt):
                pool.append(tt)
    pool.append(np.array([0, 1], dtype=np.uint8))
    worst = 0.0
    for trial in range(60):
        k = int(rng.integers(3, 5))
        while True:
            F = rng.integers(0, 2, size=1 << k).astype(np.uint8)
            if 0 < F.sum() < len(F):
                break
        kids = [pool[int(rng.integers(len(pool)))] for _ in range(k)]
        tt = compose(F, kids)
        if tt.sum() in (0, len(tt)):
            continue
        p_d, G_d, J_d = direct(tt)
        st = [direct(c) for c in kids]
        hx = "%x" % sum(int(b) << i for i, b in enumerate(F))
        gt = Gate(k, hx, "t")
        pv = np.array([s[0] for s in st])
        j = int(rng.integers(k))
        pp, g, Jm = gt.sweep(pv, j, np.array([pv[j], 0.3]))
        G_r = g[0] + sum(Jm[0, i] * st[i][1] for i in range(k))
        J_r = sum(Jm[0, i] * st[i][2] for i in range(k))
        err = max(abs(pp[0] - p_d), abs(G_r - G_d), abs(J_r - J_d))
        worst = max(worst, err)
        if err > 1e-9:
            print("MISMATCH trial", trial, k, hx, p_d, pp[0], G_d, G_r, J_d, J_r)
    print("worst error over trials: %.3e" % worst)
    # pair_ops against direct
    a, b = pool[0], pool[3]
    sa, sb = direct(a), direct(b)
    for name, F, res in (("AND", np.array([0, 0, 0, 1], dtype=np.uint8), 0), ("XOR", np.array([0, 1, 1, 0], dtype=np.uint8), 1)):
        tt = compose(F, [a, b])
        if tt.sum() in (0, len(tt)):
            continue
        d = direct(tt)
        q, g, j1, j2 = pair_ops(np.array([sa[0]]), np.array([sb[0]]))[res]
        print(name, "direct", d, "rule", float(q[0]), float(g[0] + j1[0] * sa[1] + j2[0] * sb[1]), float(j1[0] * sa[2] + j2[0] * sb[2]))


if __name__ == "__main__":
    main()
