"""n = 5: minimise over weighted graphs the best lower bound for slack(G) from the states D_x, x in the plane of the
top two Laplacian eigenvectors.

    slack(G) = 3 lambda_max(G, [3,2]) - 4 lam + 2W  >=  F(G) := max_{x in the top two-plane, |x| = 1} s(G, x),
    s(G, x) = 3 tr(D_x L(G, [3,2])) - 4 lam + 2W,

D_x as in state_mix_n5.py (W = 1 throughout).  F(G) >= 0 for every G would give Conjecture F at n = 5 by states of
this one shape.  The search is Nelder-Mead on w = z^2 from several families of starting graphs.

usage: minmax_n5.py NSTARTS SEED [MAXITER]      writes a pid file minmax_n5.pid, stops between starts if the file
STOP_minmax_n5 exists.  Self-contained (numpy, scipy).
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
Pi = np.eye(n) - 1.0 / n


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


def L32(w):
    return np.tensordot(w, SW, axes=1)


def s_of(L, M, x, need):
    Q = Pi - np.outer(x, x)
    g, Y = np.linalg.eigh(Q @ (float(x @ L @ x) * Pi - L) @ Q)
    num = den = 0.0
    for k in range(n):
        if g[k] > 1e-13:
            y = Y[:, k]
            a = B.T @ ((np.outer(x, y) + np.outer(y, x)) / np.sqrt(2.0)).ravel()
            num += g[k] * float(a @ M @ a); den += g[k] * float(a @ a)
    if den < 1e-15:
        return -need
    return (n - 2) * num / den - need


TS = np.linspace(0.0, np.pi, 61, endpoint=False)


def F(w, full=False):
    w = w / w.sum()
    L = lap(w)
    ev, U = np.linalg.eigh(L)
    M = L32(w)
    need = (n - 1) * ev[-1] - 2.0
    u1, u2 = U[:, -1], U[:, -2]
    f = lambda t: s_of(L, M, np.cos(t) * u1 + np.sin(t) * u2, need)
    vals = np.array([f(t) for t in TS])
    k = int(vals.argmax())
    lo, hi, best_t, best = TS[k] - TS[1], TS[k] + TS[1], TS[k], vals[k]
    gr = (np.sqrt(5.0) - 1) / 2
    c, e = hi - gr * (hi - lo), lo + gr * (hi - lo)
    fc, fe = f(c), f(e)
    for _ in range(14):
        if fc > fe:
            hi, e, fe = e, c, fc; c = hi - gr * (hi - lo); fc = f(c)
        else:
            lo, c, fc = c, e, fe; e = lo + gr * (hi - lo); fe = f(e)
    for t, v in ((c, fc), (e, fe)):
        if v > best:
            best, best_t = v, t
    if full:
        direct = (n - 2) * np.linalg.eigvalsh(M)[-1] - need
        return best, vals[0], direct, ev[-1] - ev[-2], ev[-1] - ev[-3], best_t
    return best


def graph(edges):
    w = np.zeros(m)
    for (i, j), v in edges:
        w[idx[(min(i, j), max(i, j))]] = v
    return w


def start(kind, rng):
    if kind == "random":
        w = rng.random(m) ** rng.integers(1, 5)
    elif kind == "sparse":
        w = rng.random(m) * (rng.random(m) < 0.5)
    elif kind == "star":
        w = graph([((0, j), 1.0) for j in range(1, n)]) + 0.05 * rng.random(m) * rng.random()
    elif kind == "edge":
        w = graph([((0, 1), 1.0)]) + 0.05 * rng.random(m) * rng.random()
    elif kind == "two_edges":
        w = graph([((0, 1), 1.0), ((2, 3), rng.uniform(0.5, 1.5))]) + 0.1 * rng.random(m)
    elif kind == "bad1":
        w = np.array([0.00007132, 0.02226662, 0.20735806, 0.20834156, 0.30343969, 0.00292157, 0.00121865,
                      0.02462748, 0.02321798, 0.20653708]) + 0.01 * rng.normal(0, 1, m) * rng.random()
    elif kind == "bad2":
        w = np.array([0.21210057, 0.21352633, 0.01393605, 0.00089872, 0.21228140, 0.01567941, 0.00283654,
                      0.01366421, 0.00059663, 0.31448014]) + 0.01 * rng.normal(0, 1, m) * rng.random()
    elif kind == "triangle_edge":
        w = graph([((0, 1), 1.0), ((1, 2), 1.0), ((0, 2), 1.0), ((3, 4), rng.uniform(0.5, 3.0))]) + 0.1 * rng.random(m)
    elif kind == "path":
        w = graph([((0, 1), rng.random() + 0.2), ((1, 2), rng.random() + 0.2), ((2, 3), rng.random() + 0.2),
                   ((3, 4), rng.random() + 0.2)]) + 0.05 * rng.random(m)
    else:
        w = 1.0 + 0.3 * rng.normal(0, 1, m)
    w = np.abs(w)
    return w if w.sum() > 1e-9 else np.ones(m)


KINDS = ["random", "sparse", "star", "edge", "two_edges", "bad1", "bad2", "triangle_edge", "path", "complete"]


def main():
    nstarts, seed = int(sys.argv[1]), int(sys.argv[2])
    maxiter = int(sys.argv[3]) if len(sys.argv) > 3 else 4000
    with open("minmax_n5.pid", "w") as fh:
        fh.write(str(os.getpid()))
    rng = np.random.default_rng(seed)
    obj = lambda z: F(z * z + 1e-300)
    best = {}
    t0 = time.time()
    overall = None
    for it in range(nstarts):
        if os.path.exists("STOP_minmax_n5"):
            print("STOP file seen, stopping after %d starts" % it); break
        kind = KINDS[it % len(KINDS)]
        z0 = np.sqrt(start(kind, rng))
        res = minimize(obj, z0, method="Nelder-Mead", options={"xatol": 1e-10, "fatol": 1e-13, "maxiter": maxiter})
        res = minimize(obj, res.x, method="Nelder-Mead", options={"xatol": 1e-11, "fatol": 1e-14, "maxiter": maxiter})
        w = res.x ** 2; w = w / w.sum()
        fb, ftop, direct, g1, g2, tb = F(w, full=True)
        if kind not in best or fb < best[kind][0]:
            best[kind] = (fb, ftop, direct, g1, g2, w)
        if overall is None or fb < overall[0]:
            overall = (fb, ftop, direct, g1, g2, w, kind)
        print("start %4d %-13s F %+.9e  s(top x) %+.6e  slack %+.6e  gap12 %.2e gap13 %.2e  %.0fs"
              % (it, kind, fb, ftop, direct, g1, g2, time.time() - t0), flush=True)
        if fb < -1e-7:
            print("   NEGATIVE: weights " + " ".join("%d%d:%.10f" % (i + 1, j + 1, v) for (i, j), v in zip(pairs, w)), flush=True)
    print("--- smallest F by family")
    for kind in KINDS:
        if kind in best:
            fb, ftop, direct, g1, g2, w = best[kind]
            print("%-13s F %+.9e  s(top x) %+.6e  slack %+.6e  gap12 %.2e  weights %s"
                  % (kind, fb, ftop, direct, g1, " ".join("%d%d:%.6f" % (i + 1, j + 1, v) for (i, j), v in zip(pairs, w) if v > 1e-7)))
    if overall:
        print("overall smallest F %+.9e (family %s)" % (overall[0], overall[6]))
    print("done in %.0fs" % (time.time() - t0))


if __name__ == "__main__":
    main()
