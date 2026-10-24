"""Remark 3.9 check: monotone functions of desirability width w satisfy H <= (15.1 + log2 w) I.
Family: f(x) = 1[sum_l phi_l(|x cap B_l|) >= theta] with random increasing phi_l (block-symmetric, monotone).
Computes the desirability preorder exactly, its width w (max antichain, via Dilworth/bipartite matching), the
poset ranks r(i) = |{j above i}| + 1 (classes refined by index), H/I, and the Gibbs bound of the rank reference
E[H(|S|)] + E[ln Z_|S| + a sum_{i in S} ln+(r(i)/|S|)]/ln2 with Z_k the elementary symmetric polynomial."""
import math, itertools, numpy as np
from feicore import spectrum, entropy, total_influence, popcounts, polite
polite()
A = 1.2006

def desirability(f, n):
    xs = np.arange(1 << n); geq = np.zeros((n, n), dtype=bool)
    for i in range(n):
        for j in range(n):
            if i == j: geq[i, j] = True; continue
            # x with x_i = 1, x_j = 0 versus x_i = 0, x_j = 1 (other coordinates free)
            base = xs[((xs >> i) & 1 == 0) & ((xs >> j) & 1 == 0)]
            a = f[base | (1 << i)]; b = f[base | (1 << j)]
            geq[i, j] = bool(np.all(a >= b))
    return geq

def width(geq, n):
    # strict order refined by index inside equivalence classes: i above j if geq[i,j] and (not geq[j,i] or i<j)
    above = np.array([[i != j and geq[i, j] and (not geq[j, i] or i < j) for j in range(n)] for i in range(n)])
    # Dilworth: width = n - max matching in the comparability bipartite graph (i -> j if i above j)
    match = [-1] * n
    def try_(u, seen):
        for v in range(n):
            if above[u, v] and not seen[v]:
                seen[v] = True
                if match[v] < 0 or try_(match[v], seen): match[v] = u; return True
        return False
    mm = sum(try_(u, [False] * n) for u in range(n))
    r = [1 + int(above[:, i].sum()) for i in range(n)]      # number of coordinates above i, plus one
    return n - mm, r

def gibbs_bound(P, n, r):
    xs = np.arange(1 << n); pc = popcounts(n)
    lev = np.bincount(pc, weights=P, minlength=n + 1)
    Hlev = float(-(lev[lev > 0] * np.log2(lev[lev > 0])).sum())
    tot = Hlev; r = np.array(r, dtype=float)
    for k in range(1, n + 1):
        sel = pc == k
        if not P[sel].any(): continue
        th = np.minimum(1.0, (k / r) ** A)
        e = np.zeros(n + 1); e[0] = 1.0
        for t in th: e[1:] = e[1:] + t * e[:-1]
        rk = np.zeros(1 << n)
        for i in range(n): rk += ((xs >> i) & 1) * np.log(np.maximum(1.0, r[i] / k))
        tot += float((P[sel] * (math.log(e[k]) + A * rk[sel])).sum()) / math.log(2)
    return tot

rng = np.random.default_rng(3)
worst = -1e9; rows = []
for rep in range(40):
    w = int(rng.integers(1, 5)); sizes = [int(s) for s in rng.integers(1, 5, size=w)]
    n = sum(sizes)
    if n > 13 or n < 3: continue
    blocks = []; start = 0
    for s in sizes: blocks.append(list(range(start, start + s))); start += s
    phis = [np.cumsum(np.concatenate([[0], rng.exponential(size=s) * rng.choice([0.3, 1, 3])])) for s in sizes]
    xs = np.arange(1 << n)
    counts = [np.zeros(1 << n, dtype=int) for _ in blocks]
    for l, B in enumerate(blocks):
        for i in B: counts[l] += (xs >> i) & 1
    score = sum(phis[l][counts[l]] for l in range(w))
    theta = float(rng.uniform(0.2, 0.8) * score.max())
    f = (score >= theta).astype(int)
    if f.all() or not f.any(): continue
    geq = desirability(f, n); wd, r = width(geq, n)
    P = spectrum(1.0 - 2.0 * f); H = entropy(P); I = total_influence(P, n)
    G = gibbs_bound(P, n, r)
    rows.append((w, wd, H / I, G / I, 15.1 + math.log2(max(wd, 1))))
    assert wd <= w, (wd, w)
    assert G >= H - 1e-9
    worst = max(worst, G / I - (15.1 + math.log2(max(wd, 1))))
print(f"{len(rows)} monotone block-symmetric functions: blocks w <= 4; measured width <= blocks in all; "
      f"max H/I {max(x[2] for x in rows):.3f}; max Gibbs/I {max(x[3] for x in rows):.3f}; "
      f"max (Gibbs/I - (15.1 + log2 width)) = {worst:.3f} (must be <= 0)")
