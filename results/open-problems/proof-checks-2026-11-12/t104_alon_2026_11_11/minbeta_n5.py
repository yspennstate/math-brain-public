"""n = 5: minimise over weighted graphs the bound s_beta(G) of beta_state_n5.py, for fixed beta.

    D_beta = sum over Laplacian eigenpairs with lam_k > lam_l (sum-zero space) of
             exp(beta (lam_k - lam)/lam) (lam_k - lam_l) a_kl a_kl^t / trace,
    a_kl = the [3,2] component of (u_k u_l^t + u_l u_k^t)/sqrt 2,
    s_beta(G) = 3 tr(D_beta L(G, [3,2])) - 4 lam + 2W  <=  slack(G)        (W = 1).

Four objectives are minimised from each start: s_beta for beta = 10, 30 and 1e6, and
H(G) = max of s_beta(G) over beta in GRID.  H >= 0 on every graph would give Conjecture F at n = 5 by states of this
one shape.  beta = 1e6 is the top-eigenvector state, known to be negative next to a double top eigenvalue: it is the
control that the search finds negative values where they exist.  A fixed finite beta is expected to be negative by
an amount of order exp(-1.6 beta) next to the uniform star (seen at beta = 10).

usage: minbeta_n5.py NSTARTS SEED [MAXITER]     pid file minbeta_n5.pid; stops between starts if STOP_minbeta_n5
exists.  Self-contained (numpy, scipy).
"""
import os
import sys
import time
import numpy as np
from scipy.optimize import minimize

n = 5
pairs = [(i, j) for i in range(n) for j in range(i + 1, n)]
idx = {p: k for k, p in enumerate(pairs)}
m = len(pairs)
GRID = np.array([3.0, 10.0, 30.0, 100.0, 300.0, 1e3, 1e4, 1e6])
BETAS = [10.0, 30.0, 1e6, "max"]          # the four objectives


def lap(w):
    L = np.zeros((n, n))
    for (i, j), v in zip(pairs, w):
        L[i, i] += v; L[j, j] += v; L[i, j] -= v; L[j, i] -= v
    return L


def basis32():
    rows = []
    for i in range(n):
        for j in range(i + 1, n):
            r = np.zeros((n, n)); r[i, j] = 1; r[j, i] = -1; rows.append(r.ravel())
        r = np.zeros((n, n)); r[i, i] = 1; rows.append(r.ravel())
        r = np.zeros((n, n)); r[i, :] = 1; rows.append(r.ravel())
    u, s, vt = np.linalg.svd(np.array(rows))
    B = vt[int((s > 1e-10).sum()):].T
    assert B.shape[1] == n * (n - 3) // 2
    return B


B = basis32()
d = B.shape[1]
SW = []
for (i, j) in pairs:
    P = np.eye(n); P[[i, j]] = P[[j, i]]
    SW.append(np.eye(d) - B.T @ np.kron(P, P) @ B)
SW = np.array(SW)
ONES = np.ones((n, n)) / n
R2 = np.sqrt(2.0)


def s_beta(w, beta, full=False):
    w = w / w.sum()
    ev, U = np.linalg.eigh(lap(w) - ONES)          # column 0: the constant vector, eigenvalue -1
    lam = ev[-1]
    M = np.tensordot(w, SW, axes=1)
    need = (n - 1) * lam - 2.0
    betas = GRID if beta == "max" else np.array([float(beta)])
    num = np.zeros(len(betas)); den = np.zeros(len(betas))
    for k in range(2, n):
        f = np.exp(betas * (ev[k] - lam) / lam)
        if f.max() < 1e-300:
            continue
        for l in range(1, k):
            g = ev[k] - ev[l]
            if g > 1e-13:
                a = B.T @ ((np.outer(U[:, k], U[:, l]) + np.outer(U[:, l], U[:, k])) / R2).ravel()
                num += f * g * float(a @ M @ a); den += f * g * float(a @ a)
    val = float(np.max(np.where(den > 1e-15, (n - 2) * num / np.maximum(den, 1e-300) - need, -need)))
    if full:
        return val, (n - 2) * np.linalg.eigvalsh(M)[-1] - need, ev[-1] - ev[-2], ev[-1] - ev[-3]
    return val


def graph(edges):
    w = np.zeros(m)
    for (i, j), v in edges:
        w[idx[(min(i, j), max(i, j))]] = v
    return w


BAD1 = np.array([0.00007132, 0.02226662, 0.20735806, 0.20834156, 0.30343969, 0.00292157, 0.00121865,
                 0.02462748, 0.02321798, 0.20653708])
BAD2 = np.array([0.21210057, 0.21352633, 0.01393605, 0.00089872, 0.21228140, 0.01567941, 0.00283654,
                 0.01366421, 0.00059663, 0.31448014])


def start(kind, rng):
    eps = 10 ** rng.uniform(-4, -1)
    if kind == "random":
        w = rng.random(m) ** rng.integers(1, 5)
    elif kind == "sparse":
        w = rng.random(m) * (rng.random(m) < 0.5)
    elif kind == "near_star":
        w = graph([((0, j), 1.0) for j in range(1, n)]) + eps * rng.random(m)
    elif kind == "star_unequal":
        w = graph([((0, j), rng.uniform(0.2, 2.0)) for j in range(1, n)]) + eps * rng.random(m)
    elif kind == "near_edge":
        w = graph([((0, 1), 1.0)]) + eps * rng.random(m)
    elif kind == "k12":
        w = graph([((0, 1), 1.0), ((0, 2), 1.0)]) + eps * rng.random(m)
    elif kind == "k13":
        w = graph([((0, 1), 1.0), ((0, 2), 1.0), ((0, 3), 1.0)]) + eps * rng.random(m)
    elif kind == "two_edges":
        w = graph([((0, 1), 1.0), ((2, 3), rng.uniform(0.5, 1.5))]) + 0.1 * rng.random(m)
    elif kind == "bad1":
        w = BAD1 + 10 ** rng.uniform(-6, -2) * rng.normal(0, 1, m)
    elif kind == "bad2":
        w = BAD2 + 10 ** rng.uniform(-6, -2) * rng.normal(0, 1, m)
    elif kind == "triangle_edge":
        w = graph([((0, 1), 1.0), ((1, 2), 1.0), ((0, 2), 1.0), ((3, 4), rng.uniform(0.5, 3.0))]) + 0.1 * rng.random(m)
    elif kind == "path":
        w = graph([((0, 1), rng.random() + 0.2), ((1, 2), rng.random() + 0.2), ((2, 3), rng.random() + 0.2),
                   ((3, 4), rng.random() + 0.2)]) + 0.05 * rng.random(m)
    else:
        w = 1.0 + 0.3 * rng.normal(0, 1, m)
    w = np.abs(w)
    return w if w.sum() > 1e-9 else np.ones(m)


KINDS = ["random", "sparse", "near_star", "star_unequal", "near_edge", "k12", "k13", "two_edges", "bad1", "bad2",
         "triangle_edge", "path", "complete"]


def main():
    nstarts, seed = int(sys.argv[1]), int(sys.argv[2])
    maxiter = int(sys.argv[3]) if len(sys.argv) > 3 else 4000
    with open("minbeta_n5.pid", "w") as fh:
        fh.write(str(os.getpid()))
    rng = np.random.default_rng(seed)
    best = {}
    count = {b: 0 for b in BETAS}
    neg = {b: 0 for b in BETAS}
    t0 = time.time()
    for it in range(nstarts):
        if os.path.exists("STOP_minbeta_n5"):
            print("STOP file seen, stopping after %d starts" % it); break
        kind = KINDS[it % len(KINDS)]
        z0 = np.sqrt(start(kind, rng))
        for beta in BETAS:
            obj = lambda z: s_beta(z * z + 1e-300, beta)
            res = minimize(obj, z0, method="Nelder-Mead", options={"xatol": 1e-10, "fatol": 1e-13, "maxiter": maxiter})
            res = minimize(obj, res.x, method="Nelder-Mead", options={"xatol": 1e-11, "fatol": 1e-14, "maxiter": maxiter})
            w = res.x ** 2; w = w / w.sum()
            val, slack, g1, g2 = s_beta(w, beta, full=True)
            count[beta] += 1
            if val < -1e-10:
                neg[beta] += 1
            if beta not in best or val < best[beta][0]:
                best[beta] = (val, slack, g1, g2, w, kind, it)
            print("start %5d %-13s beta %-7s S %+.9e  slack %+.6e  gap12 %.2e gap13 %.2e  %.0fs"
                  % (it, kind, str(beta), val, slack, g1, g2, time.time() - t0), flush=True)
            if val < -1e-10:
                print("   NEGATIVE: beta %s weights " % str(beta) + " ".join("%d%d:%.10f" % (i + 1, j + 1, v) for (i, j), v in zip(pairs, w)), flush=True)
    print("--- smallest S by beta")
    for beta in BETAS:
        if beta in best:
            val, slack, g1, g2, w, kind, it = best[beta]
            print("beta %-7s minimisations %d  below -1e-10: %d  smallest S %+.9e (start %d, %s)  slack %+.6e  gap12 %.2e  weights %s"
                  % (str(beta), count[beta], neg[beta], val, it, kind, slack, g1,
                     " ".join("%d%d:%.6f" % (i + 1, j + 1, v) for (i, j), v in zip(pairs, w) if v > 1e-7)))
    print("done in %.0fs" % (time.time() - t0))


if __name__ == "__main__":
    main()
