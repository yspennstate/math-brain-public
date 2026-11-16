"""numpy version of t104_gpu_hsearch.py (same quantity, same start families, same optimiser), for machines without
torch, with one addition: --away DELTA keeps the search at L1 distance at least DELTA from both equality cases of H.

    H(G) = max over beta in GRID of s_beta(G),  s_beta = (n-2) tr(D_beta L(G,[n-2,2])) - (n-1) lam + 2W,  W = 1.

The two equality cases are the uniform star K_{1,n-1} (any centre) and a single edge. With w normalised to sum 1,
the L1 distance to the nearest single edge is 2(1 - max w) and to the nearest uniform star is the minimum over the
centre c of |w - star_c|_1. With --away the objective is H + 10 max(0, DELTA - dist), and each round reports, among
the end points at distance >= DELTA, the smallest H and the smallest H / slack (slack = (n-2) top eig M - need).

usage: t104_np_hsearch.py N POP ITERS MINUTES SEED [--away DELTA] [--control BETA] [--check]
Stops between rounds after MINUTES or if STOP_t104_np_n<N> exists.
"""
import os
import sys
import time
import numpy as np

n = int(sys.argv[1]); POP = int(sys.argv[2]); ITERS = int(sys.argv[3])
MINUTES = float(sys.argv[4]); SEED = int(sys.argv[5]); CHECK = "--check" in sys.argv
CB = float(sys.argv[sys.argv.index("--control") + 1]) if "--control" in sys.argv else 10.0
AWAY = float(sys.argv[sys.argv.index("--away") + 1]) if "--away" in sys.argv else 0.0
NK = 12 if n >= 5 else 10
pairs = [(i, j) for i in range(n) for j in range(i + 1, n)]
m = len(pairs)
GRID = [3.0, 10.0, 30.0, 100.0, 300.0, 1e3, 1e4, 1e6]
R2 = 2.0 ** 0.5


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


B = basis(); d = B.shape[1]
SW = []
for (i, j) in pairs:
    P = np.eye(n); P[[i, j]] = P[[j, i]]
    SW.append(np.eye(d) - B.T @ np.kron(P, P) @ B)
SW = np.array(SW)
E = np.zeros((m, n))
for k, (i, j) in enumerate(pairs):
    E[k, i] = 1; E[k, j] = -1
ONES = np.full((n, n), 1.0 / n)
STARS = np.zeros((n, m))
for c in range(n):
    for k, (i, j) in enumerate(pairs):
        if c in (i, j):
            STARS[c, k] = 1.0 / (n - 1)


def dist_eq(w):
    """L1 distance of normalised weights to the nearest equality case (uniform star or single edge), or to the
    uniform K_n, where the empty quotient makes the code return H = 0 (not an equality case: H tends to 4(n-2)/n
    nearby, GAP_STATE_FORM.md; masked so the search does not stop there)."""
    w = w / w.sum(1, keepdims=True)
    de = 2.0 * (1.0 - w.max(1))
    ds = np.abs(w[:, None, :] - STARS[None, :, :]).sum(2).min(1)
    du = np.abs(w - 1.0 / w.shape[1]).sum(1)
    return np.minimum(np.minimum(de, ds), du)


def values(w, grid):
    """w (N, m) nonnegative; returns (val, slack, gap12) with val = max over grid of s_beta."""
    w = w / w.sum(1, keepdims=True)
    L = np.einsum("km,nk,kj->nmj", E, w, E)
    ev, U = np.linalg.eigh(L - ONES)
    lam = ev[:, -1]
    M = np.einsum("nk,kab->nab", w, SW)
    need = (n - 1) * lam - 2.0
    g = np.array(grid)
    num = np.zeros((w.shape[0], len(grid))); den = np.zeros_like(num)
    for k in range(2, n):
        f = np.exp(g[None, :] * ((ev[:, k] - lam) / lam)[:, None])
        for l in range(1, k):
            gap = ev[:, k] - ev[:, l]
            o = (U[:, :, k, None] * U[:, None, :, l] + U[:, :, l, None] * U[:, None, :, k]) / R2
            a = o.reshape(-1, n * n) @ B
            q = np.einsum("na,nab,nb->n", a, M, a)
            aa = (a * a).sum(1)
            gm = np.where(gap > 1e-13, gap, 0.0)
            num += f * (gm * q)[:, None]; den += f * (gm * aa)[:, None]
    with np.errstate(divide="ignore", invalid="ignore"):
        s = np.where(den > 1e-15, (n - 2) * num / np.maximum(den, 1e-300) - need[:, None], -need[:, None])
    val = s.max(1)
    slack = (n - 2) * np.linalg.eigvalsh(M)[:, -1] - need
    return val, slack, ev[:, -1] - ev[:, -2]


def direct(w, grid):
    """Plain per-graph evaluation, written as in minbeta_n5.py."""
    w = w / w.sum()
    L = E.T @ np.diag(w) @ E
    ev, U = np.linalg.eigh(L - np.ones((n, n)) / n)
    lam = ev[-1]; M = np.tensordot(w, SW, axes=1); need = (n - 1) * lam - 2.0
    best = -np.inf
    for beta in grid:
        num = den = 0.0
        for k in range(2, n):
            f = np.exp(beta * (ev[k] - lam) / lam)
            for l in range(1, k):
                gp = ev[k] - ev[l]
                if gp > 1e-13:
                    a = B.T @ ((np.outer(U[:, k], U[:, l]) + np.outer(U[:, l], U[:, k])) / R2).ravel()
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
        elif kind in (2, 3):
            k = rng.integers(2, n)
            for j in range(1, k + 1):
                x[pairs.index((0, j))] = 1.0 if kind == 2 else rng.uniform(0.2, 2.0)
            x += eps * rng.random(m)
        elif kind == 4:
            x[0] = 1.0; x += eps * rng.random(m)
        elif kind == 5:
            x[pairs.index((0, 1))] = 1.0; x[pairs.index((2, 3))] = rng.uniform(0.5, 1.5); x += 0.1 * rng.random(m)
        elif kind == 6:
            for i in range(n - 1):
                x[pairs.index((i, i + 1))] = rng.random() + 0.2
            x += 0.05 * rng.random(m)
        elif kind == 7:
            for p in [(0, 1), (1, 2), (0, 2), (3, 4)]:
                x[pairs.index(p)] = 1.0
            x += 0.1 * rng.random(m)
        elif kind == 8:
            perm = rng.permutation(n)
            a = int(rng.integers(2, n - 1)); b = int(rng.integers(2, n - a + 1))
            A, Bv = perm[:a], perm[a:a + b]
            for comp in (A, Bv):
                k = len(comp); star = rng.random() < 0.5 and k > 2
                for u in range(k):
                    for v in range(u + 1, k):
                        if star and u != 0:
                            continue
                        x[pairs.index((min(comp[u], comp[v]), max(comp[u], comp[v])))] = 1.0 / k
            x *= 1.0 + 10 ** rng.uniform(-3, -1) * rng.normal(0, 1, m) * (x > 0)
            x += 10 ** rng.uniform(-6, -2) * rng.random(m)
        elif kind == 10:
            perm = rng.permutation(n)
            for (u, v), wt in (((0, 1), 1 / 3), ((1, 2), 1 / 3), ((0, 2), 1 / 3), ((3, 4), 1 / 2)):
                x[pairs.index((min(perm[u], perm[v]), max(perm[u], perm[v])))] = wt
            x *= 1.0 + 10 ** rng.uniform(-6, -2) * rng.normal(0, 1, m) * (x > 0)
            x += 10 ** rng.uniform(-3, -1.3) * rng.random(m)
        elif kind == 11:
            c = int(rng.integers(0, n))
            for j in range(n):
                if j != c:
                    x[pairs.index((min(c, j), max(c, j)))] = 1.0 + 10 ** rng.uniform(-5, -2.5) * rng.normal()
        else:
            x = np.abs(1.0 + 0.3 * rng.normal(0, 1, m))
        w[r] = np.abs(x) if np.abs(x).sum() > 1e-9 else np.ones(m)
    return w


def objective(z, grid):
    w = z * z + 1e-300
    v, sl, g = values(w, grid)
    if AWAY > 0:
        v = v + 10.0 * np.maximum(0.0, AWAY - dist_eq(w))
    return v


def run_round(grid, rng):
    z = np.sqrt(starts(POP, rng))
    sig = np.full(POP, 0.05)
    if NK == 12:
        sig[np.arange(POP) % NK >= 10] = 1e-3
    cur = objective(z, grid)
    for it in range(ITERS):
        step = rng.standard_normal((POP, m)) * sig[:, None] * np.abs(z).mean(1, keepdims=True)
        zn = z + step
        if it % 7 == 3:
            j = rng.integers(0, m, POP)
            zn[np.arange(POP), j] = 0.0
        vn = objective(zn, grid)
        ok = np.isfinite(vn) & (vn < cur)
        z = np.where(ok[:, None], zn, z); cur = np.where(ok, vn, cur)
        sig = np.clip(np.where(ok, sig * 1.5, sig * 0.92), 1e-12, 0.5)
    w = z * z; w = w / w.sum(1, keepdims=True)
    val, slack, g12 = values(w + 1e-300, grid)
    return w, val, slack, g12


def fmt(w, cut):
    return " ".join("%d%d:%.8f" % (a + 1, b + 1, x) for (a, b), x in zip(pairs, w) if x > cut)


def main():
    tag = "t104_np_n%d" % n
    rng = np.random.default_rng(SEED)
    if CHECK:
        W = rng.random((200, m)) ** rng.integers(1, 4, (200, 1))
        v, _, _ = values(W, GRID)
        dif = max(abs(float(v[i]) - direct(W[i], GRID)) for i in range(200))
        print("numpy  n %d  d %d  max |batched - direct| over 200 graphs: %.3e" % (n, d, dif), flush=True)
        st = np.vstack([STARS[0], np.eye(m)[0]])
        print("dist_eq at the star and at an edge (must be 0 0):", dist_eq(st), flush=True)
        return
    t0 = time.time(); rnd = 0
    tot = {"H": [0, 0, 0], "c%g" % CB: [0, 0, 0]}
    best = {"H": (np.inf, None), "c%g" % CB: (np.inf, None)}
    print("numpy  n %d  pop %d  iters %d  minutes %g  seed %d  away %g  control beta %g" %
          (n, POP, ITERS, MINUTES, SEED, AWAY, CB), flush=True)
    while time.time() - t0 < MINUTES * 60 and not os.path.exists("STOP_" + tag):
        for name, grid in (("H", GRID), ("c%g" % CB, [CB])):
            w, v, sl, g = run_round(grid, rng)
            dist = dist_eq(w)
            far = dist >= AWAY - 1e-12
            negs = np.where(far & (v < -1e-10))[0]
            tot[name][0] += len(v); tot[name][1] += int(far.sum()); tot[name][2] += len(negs)
            if far.any():
                iv = np.where(far)[0]
                i0 = iv[int(np.argmin(v[iv]))]
                big = iv[sl[iv] > 1e-3]
                if len(big):
                    r = v[big] / sl[big]; i1 = big[int(np.argmin(r))]; rmin = float(r.min())
                else:
                    i1 = -1; rmin = float("inf")
                if v[i0] < best[name][0]:
                    best[name] = (float(v[i0]), w[i0].copy())
                print("round %3d %-5s ends %d  far %d  far below -1e-10: %d  far min %+.6e (slack %+.3e gap12 %.2e dist %.3f)"
                      "  far min ratio %.5f  %.0fs" % (rnd, name, len(v), len(iv), len(negs), v[i0], sl[i0], g[i0],
                                                       dist[i0], rmin, time.time() - t0), flush=True)
                print("   far min weights %s" % fmt(w[i0], 1e-7), flush=True)
                if i1 >= 0:
                    print("   far lowest ratio weights (dist %.3f) %s" % (dist[i1], fmt(w[i1], 1e-7)), flush=True)
            else:
                print("round %3d %-5s ends %d  none at distance >= %g  %.0fs" % (rnd, name, len(v), AWAY,
                                                                              time.time() - t0), flush=True)
            for i in negs[np.argsort(v[negs])][:3]:
                print("   NEGATIVE %s S %+.6e slack %+.4e gap12 %.2e dist %.3f weights %s" %
                      (name, v[i], sl[i], g[i], dist[i], fmt(w[i], 1e-9)), flush=True)
        rnd += 1
    for name in tot:
        print("totals %s: ends %d, at distance >= %g: %d, of them below -1e-10: %d, smallest %+.6e" %
              (name, tot[name][0], AWAY, tot[name][1], tot[name][2], best[name][0]), flush=True)
        if best[name][1] is not None:
            print("   smallest at %s" % fmt(best[name][1], 1e-9), flush=True)
    print("done in %.0fs" % (time.time() - t0), flush=True)


if __name__ == "__main__":
    main()
