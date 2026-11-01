"""Checks for "The layer tail of the random recursive tree".

Run: python checks.py   (numpy only; a few minutes).  Every number quoted in the paper is printed here.
A  layer = second largest branch height; max layer = floor(diam/2) <= height  (all recursive trees, n <= 9)
B  the recursion (Theorem 2 of Stepanyants et al.): lbar_1 = 1/2, lbar_2 = 3 - e; b_k = lbar_k e^{k/e} k^{3/(2e)}
C  Proposition 2.1: P(M_k <= y) = s_k(y) and E exp(-M_k) = lbar_k, by direct simulation of the Poisson-weighted tree
D  random recursive trees: fraction of vertices at layer >= k against lbar_k; max layer, floor(diam/2), height
"""
import itertools
import math

import numpy as np

E = math.e
ok_all = True


def check(name, cond):
    global ok_all
    ok_all &= bool(cond)
    print(("PASS " if cond else "FAIL ") + name)


def layers_by_stripping(adj):
    n = len(adj)
    deg = [len(a) for a in adj]
    layer = [-1] * n
    alive = set(range(n))
    r = 0
    while alive:
        leaves = [v for v in alive if deg[v] <= 1]
        for v in leaves:
            layer[v] = r
        for v in leaves:
            alive.discard(v)
            for u in adj[v]:
                if u in alive:
                    deg[u] -= 1
        r += 1
    return layer


def branch_height(adj, u, parent):
    """Number of vertices on the longest path that starts at u and avoids parent."""
    best = 0
    stack = [(u, parent, 1)]
    while stack:
        x, p, d = stack.pop()
        best = max(best, d)
        for z in adj[x]:
            if z != p:
                stack.append((z, x, d + 1))
    return best


def ecc(adj, s):
    dist = {s: 0}
    q = [s]
    for x in q:
        for z in adj[x]:
            if z not in dist:
                dist[z] = dist[x] + 1
                q.append(z)
    return dist


# ---- A
print("== A: deterministic identities, every recursive tree with n <= 9 vertices")
cnt_v = cnt_t = 0
good = True
for n in range(1, 10):
    for parents in itertools.product(*[range(i) for i in range(1, n)]):
        adj = [[] for _ in range(n)]
        for i, p in enumerate(parents, start=1):
            adj[i].append(p)
            adj[p].append(i)
        lay = layers_by_stripping(adj)
        for v in range(n):
            hs = sorted((branch_height(adj, u, v) for u in adj[v]), reverse=True)
            sec = hs[1] if len(hs) >= 2 else 0
            good &= sec == lay[v]
            cnt_v += 1
        d0 = ecc(adj, 0)
        far = max(d0, key=d0.get)
        diam = max(ecc(adj, far).values())
        H = max(d0.values())
        good &= (max(lay) == diam // 2) and (max(lay) <= H)
        cnt_t += 1
print(f"   trees {cnt_t}, vertices {cnt_v}")
check("A layer = second largest branch height; max layer = floor(diam/2) <= height", good)

# ---- B
print("== B: the recursion")
h = 0.002
Y = 160.0
y = np.arange(0.0, Y + h / 2, h)
w = np.exp(-y) * h
w[0] *= 0.5
w[-1] *= 0.5


def step(s, h):
    S = np.concatenate(([0.0], np.cumsum(0.5 * (s[1:] + s[:-1]) * h)))
    return -np.expm1(-S)


s = np.ones_like(y)
lb = [1.0]
med = [0.0]
KMAX = 300
for k in range(1, KMAX + 2):
    s = step(s, h)
    lb.append(float(np.dot(s, w)))
    med.append(float(np.interp(0.5, s, y)))
check(f"B lbar_1 = 1/2 (got {lb[1]:.8f})", abs(lb[1] - 0.5) < 1e-6)
check(f"B lbar_2 = 3 - e (got {lb[2]:.8f}, exact {3 - E:.8f})", abs(lb[2] - (3 - E)) < 1e-6)
b = {k: lb[k] * math.exp(k / E) * k ** (1.5 / E) for k in range(1, KMAX + 1)}
for k in (1, 2, 5, 10, 20, 50, 100, 200, 300):
    print(f"   k={k:4d} lbar={lb[k]:.6e} l_k={lb[k] - lb[k + 1]:.6e} median M_k={med[k]:9.4f}"
          f"  median - k/e - 3/(2e) log k = {med[k] - k / E - 1.5 / E * math.log(k):+.4f}  b_k={b[k]:.5f}")
bk = [b[k] for k in range(1, KMAX + 1)]
print(f"   min b_k = {min(bk):.4f}, max b_k = {max(bk):.4f} over 1 <= k <= {KMAX}")
check("B b_k stays in [0.5, 2] for 1 <= k <= 300", 0.5 <= min(bk) and max(bk) <= 2)
ratio = [(lb[k] - lb[k + 1]) / lb[k] for k in (100, 200, 300)]
print("   l_k / lbar_k at k=100,200,300:", [f"{r:.5f}" for r in ratio], f" 1 - e^(-1/e) = {1 - math.exp(-1 / E):.5f}")
check("B l_k/lbar_k within 0.01 of 1 - e^{-1/e} at k = 300", abs(ratio[-1] - (1 - math.exp(-1 / E))) < 0.01)
h2 = 0.004
y2 = np.arange(0.0, Y + h2 / 2, h2)
w2 = np.exp(-y2) * h2
w2[0] *= 0.5
w2[-1] *= 0.5
s2 = np.ones_like(y2)
for k in range(1, 101):
    s2 = step(s2, h2)
rel = abs(float(np.dot(s2, w2)) / lb[100] - 1)
print(f"   step control: lbar_100 at h=0.004 vs h=0.002, relative difference {rel:.2e}")
check("B step-size control at k = 100 (relative difference < 1e-3)", rel < 1e-3)

# ---- C
print("== C: direct simulation of the Poisson-weighted infinite tree (no recursion)")
rng = np.random.default_rng(20261018)
CUT = 12.0
REPS = 3000
KC = 8
mins = np.full((REPS, KC + 1), np.inf)
for r in range(REPS):
    pos = np.array([0.0])
    mins[r, 0] = 0.0
    for k in range(1, KC + 1):
        # children of a particle at x below CUT: Poisson process of rate one on (x, CUT)
        nchild = rng.poisson(CUT - pos)
        par = np.repeat(pos, nchild)
        pos = par + rng.uniform(0.0, 1.0, par.size) * (CUT - par)
        if pos.size:
            mins[r, k] = pos.min()
i3 = int(round(3.0 / h))
s = np.ones_like(y)
sk3 = [1.0]
for k in range(1, KC + 1):
    s = step(s, h)
    sk3.append(float(s[i3]))
good = True
for k in (1, 2, 4, 6, 8):
    p = float(np.mean(mins[:, k] <= 3.0))
    se = math.sqrt(max(p * (1 - p), 1e-12) / REPS)
    ex = np.where(np.isfinite(mins[:, k]), np.exp(-mins[:, k]), 0.0)  # M_k > 12 contributes < e^-12
    m = float(ex.mean())
    sem = float(ex.std() / math.sqrt(REPS))
    z1 = (p - sk3[k]) / se
    z2 = (m - lb[k]) / sem
    good &= abs(z1) < 4 and abs(m - lb[k]) < math.exp(-CUT) + 4 * sem
    print(f"   k={k}: P(M_k<=3) sim {p:.4f}+-{se:.4f} vs s_k(3) {sk3[k]:.4f} (z={z1:+.2f});"
          f" E e^-M_k sim {m:.5f}+-{sem:.5f} vs lbar_k {lb[k]:.5f} (z={z2:+.2f})")
check("C simulation agrees with the recursion within 4 standard errors", good)

# ---- D
print("== D: random recursive trees")


def rrt(n, rng):
    par = np.empty(n, dtype=np.int64)
    par[0] = -1
    par[1:] = (rng.random(n - 1) * np.arange(1, n)).astype(np.int64)
    return par


def tree_stats(par):
    n = par.size
    ends = np.concatenate((np.arange(1, n), par[1:]))
    other = np.concatenate((par[1:], np.arange(1, n)))
    order = np.argsort(ends, kind="stable")
    ends = ends[order]
    other = other[order]
    start = np.zeros(n + 1, dtype=np.int64)
    start[1:] = np.cumsum(np.bincount(ends, minlength=n))
    d = np.diff(start).copy()
    layer = np.full(n, -1, dtype=np.int64)
    removed = np.zeros(n, dtype=bool)
    cur = np.flatnonzero(d <= 1)
    r = 0
    while cur.size:
        layer[cur] = r
        removed[cur] = True
        nb = np.concatenate([other[start[v]:start[v + 1]] for v in cur])
        nb = nb[~removed[nb]]
        np.subtract.at(d, nb, 1)
        cand = np.unique(nb)
        cur = cand[d[cand] <= 1]
        r += 1
    depth = np.zeros(n, dtype=np.int64)
    for i in range(1, n):
        depth[i] = depth[par[i]] + 1
    far = int(np.argmax(depth))
    dist = np.full(n, -1, dtype=np.int64)
    dist[far] = 0
    q = [far]
    for x in q:
        for z in other[start[x]:start[x + 1]]:
            if dist[z] < 0:
                dist[z] = dist[x] + 1
                q.append(int(z))
    return layer, int(depth.max()), int(dist.max())


rng = np.random.default_rng(7)
N = 200000
T = 10
frac = np.zeros(8)
good = True
for t in range(T):
    lay, H, diam = tree_stats(rrt(N, rng))
    for k in range(8):
        frac[k] += np.mean(lay >= k) / T
    good &= (lay.max() == diam // 2) and lay.max() <= H
    print(f"   tree {t}: n={N} max layer {lay.max()}, floor(diam/2) {diam // 2}, height {H},"
          f" e log n - 1.5 log log n = {E * math.log(N) - 1.5 * math.log(math.log(N)):.2f}")
check("D max layer = floor(diam/2) <= height in every simulated tree", good)
good = True
for k in range(1, 8):
    print(f"   k={k}: fraction at layer >= k {frac[k]:.5f} vs lbar_k {lb[k]:.5f}  (difference {frac[k] - lb[k]:+.5f})")
    good &= abs(frac[k] - lb[k]) < 2e-3
check("D layer fractions of 10 trees of size 200000 within 0.002 of lbar_k (k = 1..7)", good)
print("ALL CHECKS PASS" if ok_all else "SOME CHECK FAILED")
