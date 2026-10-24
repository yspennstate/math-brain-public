"""Adversarial search against the key step of Proposition 2 for halfspaces: maximise, over two threshold
functions with arbitrary weights and a gate G, the ratio

    max_x Pr[D_i f(y) != 0 | x]  /  sum_l E Erd(Bin(s, eta))

over coordinates i, initial segments of the round-robin order (all lengths t) and eta, among cases where
the bound is < 1.  The proof says the ratio is <= 1.  Usage: python adv_thmA.py N SEED ITERS
"""
import sys
from math import comb
import numpy as np
from fei_lib import *

setup_process()
ERD = [comb(m, m // 2) / 2.0 ** m for m in range(64)]


def erd_bin(s, eta):
    return sum(comb(s, m) * eta ** m * (1 - eta) ** (s - m) * ERD[m] for m in range(s + 1))


def worst_ratio(W, th, gate, n, X):
    k = len(W)
    vals = [sgn(X @ W[l] - th[l]) for l in range(k)]
    if gate == 0:
        f = np.where((vals[0] > 0) & (vals[1] > 0), 1.0, -1.0)
    elif gate == 1:
        f = vals[0] * vals[1]
    else:
        f = np.where((vals[0] > 0) | (vals[1] < 0), 1.0, -1.0)
    if np.all(f == f[0]):
        return 0.0
    orders = [list(np.argsort(-np.abs(W[l]), kind="stable")) for l in range(k)]
    rstar = round_robin(orders)
    worst = 0.0
    for pos in range(1, n):
        i = rstar[pos]
        for t in range(1, pos + 1):
            P = rstar[:t]
            s = 0
            while all(set(orders[l][: s + 1]) <= set(P) for l in range(k)):
                s += 1
            for eta in (0.35, 0.7, 1.0):
                bnd = k * erd_bin(s, eta)
                if bnd >= 1:
                    continue
                Pw, _ = pointwise_exit(f, n, i, [1 << int(u) for u in P], eta)
                worst = max(worst, float(Pw.max()) / bnd)
    return worst


def main(n, seed, iters):
    rng = np.random.default_rng(seed)
    X = coords(n)
    W = [rng.standard_normal(n) * 1.5 ** (-rng.permutation(n)) for _ in range(2)]
    th = [0.1, -0.1]
    gate = 0
    cur = worst_ratio(W, th, gate, n, X)
    best = cur
    log = open("../logs/adv_thmA_n%d_s%d.log" % (n, seed), "w")
    for it in range(iters):
        W2 = [w.copy() for w in W]
        th2 = list(th)
        g2 = gate
        mv = rng.integers(0, 4)
        l = rng.integers(0, 2)
        if mv == 0:
            j = rng.integers(0, n); W2[l][j] = rng.standard_normal() * np.abs(W2[l]).max() * rng.uniform(0.05, 1.5)
        elif mv == 1:
            th2[l] = th[l] + rng.normal(0, 0.3) * np.abs(W2[l]).sum() / np.sqrt(n)
        elif mv == 2:
            g2 = int(rng.integers(0, 3))
        else:
            W2[l] = W2[l][rng.permutation(n)]
        r = worst_ratio(W2, th2, g2, n, X)
        if r >= cur or rng.random() < np.exp((r - cur) / 0.03):
            W, th, gate, cur = W2, th2, g2, r
            best = max(best, cur)
        if it % 25 == 0:
            print("it=%d cur=%.4f best=%.4f" % (it, cur, best), file=log, flush=True)
    print("FINAL n=%d seed=%d worst ratio found %.5f (proof: <= 1)" % (n, seed, best), file=log, flush=True)


if __name__ == "__main__":
    main(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))
