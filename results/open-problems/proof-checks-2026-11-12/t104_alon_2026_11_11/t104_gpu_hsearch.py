"""Batched GPU search for negative values of H(G) = max over beta of s_beta(G), weighted graphs on n vertices.

    D_beta = sum over Laplacian eigenpairs with lam_k > lam_l (sum-zero space) of
             exp(beta (lam_k - lam)/lam) (lam_k - lam_l) a_kl a_kl^t / trace,
    a_kl = the [n-2,2] component of (u_k u_l^t + u_l u_k^t)/sqrt 2,
    s_beta(G) = (n-2) tr(D_beta L(G,[n-2,2])) - (n-1) lam + 2W  <=  slack(G),   W = 1.

Same quantity as minbeta_n5.py, vectorised in float64 with torch. Two populations are minimised by a (1+1)
evolution strategy per individual in square-root weight coordinates: objective H (beta over GRID) and the
control beta = 1e6 (the top-eigenvector state, which must come out negative next to a double top eigenvalue).
Each round starts a fresh population from the start families and runs ITERS steps; every round's end points are
summarised in one line, and every end point below -1e-10 is printed with its weights.

usage: t104_gpu_hsearch.py N POP ITERS MINUTES SEED [--check]
pid file t104_gpu_n<N>.pid; stops between rounds if STOP_t104_gpu_n<N> exists or MINUTES have passed.
--check compares the batched value with a direct numpy evaluation at 200 random graphs and exits.
"""
import os
import sys
import time
import numpy as np
import torch

n = int(sys.argv[1]); POP = int(sys.argv[2]); ITERS = int(sys.argv[3])
MINUTES = float(sys.argv[4]); SEED = int(sys.argv[5]); CHECK = "--check" in sys.argv
dev = torch.device("cpu" if "--cpu" in sys.argv or not torch.cuda.is_available() else "cuda")
CB = float(sys.argv[sys.argv.index("--control") + 1]) if "--control" in sys.argv else 1e6   # beta of the control run
NK = 12 if n >= 5 else 10                        # kind 10 (triangle plus a disjoint edge) needs five vertices
dt = torch.float64
pairs = [(i, j) for i in range(n) for j in range(i + 1, n)]
m = len(pairs)
GRID = [3.0, 10.0, 30.0, 100.0, 300.0, 1e3, 1e4, 1e6]


def basis():
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


Bn = basis(); d = Bn.shape[1]
SWn = []
for (i, j) in pairs:
    P = np.eye(n); P[[i, j]] = P[[j, i]]
    SWn.append(np.eye(d) - Bn.T @ np.kron(P, P) @ Bn)
SWn = np.array(SWn)
E = np.zeros((m, n))
for k, (i, j) in enumerate(pairs):
    E[k, i] = 1; E[k, j] = -1
B = torch.tensor(Bn, dtype=dt, device=dev)
SW = torch.tensor(SWn, dtype=dt, device=dev)
Et = torch.tensor(E, dtype=dt, device=dev)
ONES = torch.full((n, n), 1.0 / n, dtype=dt, device=dev)
R2 = 2.0 ** 0.5


def values(w, grid):
    """w (N, m) nonnegative; returns (val (N,), slack (N,), gap12 (N,)) with val = max over grid of s_beta."""
    w = w / w.sum(1, keepdim=True)
    L = torch.einsum("km,nk,kj->nmj", Et, w, Et)
    ev, U = torch.linalg.eigh(L - ONES)
    lam = ev[:, -1]
    M = torch.einsum("nk,kab->nab", w, SW)
    need = (n - 1) * lam - 2.0
    g = torch.tensor(grid, dtype=dt, device=dev)
    num = torch.zeros(w.shape[0], len(grid), dtype=dt, device=dev); den = torch.zeros_like(num)
    for k in range(2, n):
        f = torch.exp(g[None, :] * ((ev[:, k] - lam) / lam)[:, None])
        for l in range(1, k):
            gap = ev[:, k] - ev[:, l]
            o = (U[:, :, k, None] * U[:, None, :, l] + U[:, :, l, None] * U[:, None, :, k]) / R2
            a = o.reshape(-1, n * n) @ B
            q = torch.einsum("na,nab,nb->n", a, M, a)
            aa = (a * a).sum(1)
            gm = torch.where(gap > 1e-13, gap, torch.zeros_like(gap))
            num += f * (gm * q)[:, None]; den += f * (gm * aa)[:, None]
    s = torch.where(den > 1e-15, (n - 2) * num / den.clamp_min(1e-300) - need[:, None], -need[:, None])
    val = s.max(1).values
    slack = (n - 2) * torch.linalg.eigvalsh(M)[:, -1] - need
    return val, slack, ev[:, -1] - ev[:, -2]


def direct(w, grid):
    """Plain numpy evaluation of one graph, written as in minbeta_n5.py."""
    w = w / w.sum()
    L = E.T @ np.diag(w) @ E
    ev, U = np.linalg.eigh(L - np.ones((n, n)) / n)
    lam = ev[-1]; M = np.tensordot(w, SWn, axes=1); need = (n - 1) * lam - 2.0
    best = -np.inf
    for beta in grid:
        num = den = 0.0
        for k in range(2, n):
            f = np.exp(beta * (ev[k] - lam) / lam)
            for l in range(1, k):
                gp = ev[k] - ev[l]
                if gp > 1e-13:
                    a = Bn.T @ ((np.outer(U[:, k], U[:, l]) + np.outer(U[:, l], U[:, k])) / R2).ravel()
                    num += f * gp * float(a @ M @ a); den += f * gp * float(a @ a)
        best = max(best, (n - 2) * num / den - need if den > 1e-15 else -need)
    return best


def starts(N, rng):
    w = np.zeros((N, m))
    for r in range(N):
        kind = r % NK
        eps = 10 ** rng.uniform(-4, -1)
        x = np.zeros(m)
        if kind == 0:
            x = rng.random(m) ** rng.integers(1, 5)
        elif kind == 1:
            x = rng.random(m) * (rng.random(m) < 0.5)
        elif kind in (2, 3):                       # stars K_{1,k} plus isolated vertices, near uniform or not
            k = rng.integers(2, n)
            for j in range(1, k + 1):
                x[pairs.index((0, j))] = 1.0 if kind == 2 else rng.uniform(0.2, 2.0)
            x += eps * rng.random(m)
        elif kind == 4:                            # near a single edge
            x[0] = 1.0; x += eps * rng.random(m)
        elif kind == 5:                            # two disjoint edges
            x[pairs.index((0, 1))] = 1.0; x[pairs.index((2, 3))] = rng.uniform(0.5, 1.5); x += 0.1 * rng.random(m)
        elif kind == 6:                            # a path
            for i in range(n - 1):
                x[pairs.index((i, i + 1))] = rng.random() + 0.2
            x += 0.05 * rng.random(m)
        elif kind == 7:                            # triangle plus an edge
            for p in [(0, 1), (1, 2), (0, 2), (3, 4)]:
                x[pairs.index(p)] = 1.0
            x += 0.1 * rng.random(m)
        elif kind == 8:                            # two components with nearly equal top eigenvalues
            perm = rng.permutation(n)
            a = int(rng.integers(2, n - 1)); b = int(rng.integers(2, n - a + 1))
            A, Bv = perm[:a], perm[a:a + b]
            for comp in (A, Bv):                   # complete graph or star on k vertices, weight w: top eigenvalue k w
                k = len(comp); star = rng.random() < 0.5 and k > 2
                for u in range(k):
                    for v in range(u + 1, k):
                        if star and u != 0:
                            continue
                        x[pairs.index((min(comp[u], comp[v]), max(comp[u], comp[v])))] = 1.0 / k
            x *= 1.0 + 10 ** rng.uniform(-3, -1) * rng.normal(0, 1, m) * (x > 0)
            x += 10 ** rng.uniform(-6, -2) * rng.random(m)
        elif kind == 10:                           # triangle of weight 1/3 plus a disjoint edge of weight 1/2: double top eigenvalue 1
            perm = rng.permutation(n)
            for (u, v), wt in (((0, 1), 1 / 3), ((1, 2), 1 / 3), ((0, 2), 1 / 3), ((3, 4), 1 / 2)):
                x[pairs.index((min(perm[u], perm[v]), max(perm[u], perm[v])))] = wt
            x *= 1.0 + 10 ** rng.uniform(-6, -2) * rng.normal(0, 1, m) * (x > 0)
            x += 10 ** rng.uniform(-3, -1.3) * rng.random(m)   # the known failures carry connecting edges of order 0.01
        elif kind == 11:                           # the uniform star K_{1,n-1}, only its leaf weights perturbed
            c = int(rng.integers(0, n))
            for j in range(n):
                if j != c:
                    x[pairs.index((min(c, j), max(c, j)))] = 1.0 + 10 ** rng.uniform(-5, -2.5) * rng.normal()
        else:
            x = np.abs(1.0 + 0.3 * rng.normal(0, 1, m))
        w[r] = np.abs(x) if np.abs(x).sum() > 1e-9 else np.ones(m)
    return w


def run_round(grid, rng, gen):
    z = torch.tensor(np.sqrt(starts(POP, rng)), dtype=dt, device=dev)
    sig = torch.full((POP,), 0.05, dtype=dt, device=dev)
    if NK == 12:                                   # the near-double-top and near-star starts begin with a small step
        sig[torch.arange(POP, device=dev) % NK >= 10] = 1e-3
    cur, _, _ = values(z * z + 1e-300, grid)
    for it in range(ITERS):
        step = torch.randn(POP, m, dtype=dt, device=dev, generator=gen) * sig[:, None] * z.abs().mean(1, keepdim=True)
        zn = z + step
        if it % 7 == 3:                            # occasionally push one coordinate to zero
            j = torch.randint(0, m, (POP,), device=dev, generator=gen)
            zn[torch.arange(POP, device=dev), j] = 0.0
        vn, _, _ = values(zn * zn + 1e-300, grid)
        ok = torch.isfinite(vn) & (vn < cur)
        z = torch.where(ok[:, None], zn, z); cur = torch.where(ok, vn, cur)
        sig = torch.where(ok, sig * 1.5, sig * 0.92).clamp(1e-12, 0.5)
    w = z * z; w = w / w.sum(1, keepdim=True)
    val, slack, g12 = values(w + 1e-300, grid)
    return w, val, slack, g12


def main():
    tag = "t104_gpu_n%d" % n
    torch.manual_seed(SEED)
    rng = np.random.default_rng(SEED)
    if CHECK:
        W = rng.random((200, m)) ** rng.integers(1, 4, (200, 1))
        v, _, _ = values(torch.tensor(W, dtype=dt, device=dev), GRID)
        dif = max(abs(float(v[i]) - direct(W[i], GRID)) for i in range(200))
        print("device %s  n %d  d %d  max |batched - direct| over 200 graphs: %.3e" % (dev, n, d, dif), flush=True)
        return
    with open(tag + ".pid", "w") as fh:
        fh.write(str(os.getpid()))
    gen = torch.Generator(device=dev); gen.manual_seed(SEED)
    t0 = time.time(); rnd = 0
    tot = {"H": [0, 0], "c%g" % CB: [0, 0]}
    print("device %s  n %d  pop %d  iters %d  minutes %g  seed %d" % (dev, n, POP, ITERS, MINUTES, SEED), flush=True)
    while time.time() - t0 < MINUTES * 60 and not os.path.exists("STOP_" + tag):
        for name, grid in (("H", GRID), ("c%g" % CB, [CB])):
            w, val, slack, g12 = run_round(grid, rng, gen)
            v = val.cpu().numpy(); sl = slack.cpu().numpy(); g = g12.cpu().numpy(); wc = w.cpu().numpy()
            negs = np.where(v < -1e-10)[0]
            tot[name][0] += len(v); tot[name][1] += len(negs)
            big = sl > 1e-3
            r = (v[big] / sl[big]) if big.any() else np.array([np.inf])
            i0 = int(np.argmin(v)); i1 = int(np.where(big)[0][np.argmin(r)]) if big.any() else -1
            print("round %3d %-5s ends %d  below -1e-10: %d  min %+.6e (slack %+.3e gap12 %.2e)  min ratio %.5f (slack %.4f)  %.0fs"
                  % (rnd, name, len(v), len(negs), v[i0], sl[i0], g[i0], float(r.min()),
                     float(sl[i1]) if i1 >= 0 else float("nan"), time.time() - t0), flush=True)
            for i in negs[np.argsort(v[negs])][:3]:
                print("   NEGATIVE %s S %+.6e slack %+.4e gap12 %.2e weights %s" % (name, v[i], sl[i], g[i],
                      " ".join("%d%d:%.8f" % (a + 1, b + 1, x) for (a, b), x in zip(pairs, wc[i]) if x > 1e-9)), flush=True)
            if i1 >= 0:
                print("   lowest ratio %s weights %s" % (name, " ".join("%d%d:%.6f" % (a + 1, b + 1, x)
                      for (a, b), x in zip(pairs, wc[i1]) if x > 1e-7)), flush=True)
        rnd += 1
    print("totals: H ends %d below -1e-10 %d; control ends %d below -1e-10 %d" % (tot["H"][0], tot["H"][1],
          tot["c%g" % CB][0], tot["c%g" % CB][1]), flush=True)
    print("done in %.0fs" % (time.time() - t0), flush=True)


if __name__ == "__main__":
    main()
