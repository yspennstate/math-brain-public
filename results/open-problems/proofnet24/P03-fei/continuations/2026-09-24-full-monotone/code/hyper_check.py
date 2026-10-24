"""Exact checks for r-uniform hypergraph clique properties (r = 3) on 5 and 6 vertices.

Variables: the triples of [n]. f = [some k-set has all its triples present]. Checked:
 (1) the vertex-coding inequality H <= h(eps) + eps log2(eI/eps) + log2(3) T + I log2(e E C(v,r)/I);
 (2) the r-set lemma: for every triple R, with A_i = hyperedges containing u_i other than R,
     Pr[S meets A_1, A_2, A_3] = ||prod (1 - E_{A_i}) F||^2 <= 4 E[ (sum over covers of sqrt(E_fibre prod a_J))^2 1(g=0) ]
     <= 4 c_r sum_covers E[prod a_J] Pr[g = 0],
     where a_J = [a copy touching exactly R_J is present], g = [a copy avoiding R is present].
Printed: exact ratios of the successive sides (each must be <= 1).
"""
import itertools, math, functools
import numpy as np
print = functools.partial(print, flush=True)


def wht(v):
    a = v.astype(np.float64).copy(); n = a.size; h = 1
    while h < n:
        a = a.reshape(-1, 2 * h); x = a[:, :h].copy(); y = a[:, h:].copy()
        a[:, :h] = x + y; a[:, h:] = x - y; a = a.reshape(n); h *= 2
    return a / n


def popcount(x):
    x = x.astype(np.int64); c = np.zeros_like(x)
    while x.any():
        c += x & 1; x >>= 1
    return c


def tree_nodes(n):
    out = []
    def rec(lo, hi):
        if hi - lo <= 1:
            return
        out.append(list(range(lo, hi)))
        mid = (lo + hi) // 2
        rec(lo, mid); rec(mid, hi)
    rec(0, n)
    return out


def covers(r):
    subsets = [frozenset(c) for s in range(1, r + 1) for c in itertools.combinations(range(r), s)]
    out = []
    for mask in range(1, 1 << len(subsets)):
        fam = [subsets[i] for i in range(len(subsets)) if (mask >> i) & 1]
        if frozenset().union(*fam) == frozenset(range(r)):
            out.append(fam)
    return out


def run(n, k, r=3):
    E = list(itertools.combinations(range(n), r)); idx = {e: i for i, e in enumerate(E)}; N = len(E)
    X = np.arange(1 << N, dtype=np.int64)
    size = popcount(X)
    vmask = [sum(1 << idx[e] for e in E if u in e) for u in range(n)]
    touch = np.stack([(X & vmask[u]) != 0 for u in range(n)], axis=1)
    v = touch.sum(axis=1)
    copies = [(set(c), sum(1 << idx[e] for e in itertools.combinations(c, r))) for c in itertools.combinations(range(n), k)]
    present = [(X & mk) == mk for _, mk in copies]
    f = np.zeros(1 << N, dtype=bool)
    for p in present:
        f |= p
    F = np.where(f, -1.0, 1.0)
    P = wht(F) ** 2
    nz = P > 1e-300
    H = float(-(P[nz] * np.log2(P[nz])).sum()); I = float((P * size).sum()); eps = 1 - float(P[0])
    T = sum(float(P[touch[:, node].any(axis=1)].sum()) for node in tree_nodes(n))
    ECr = float((P * np.array([math.comb(int(t), r) for t in v])).sum())
    h = (lambda e: 0 if e <= 0 or e >= 1 else -e * math.log2(e) - (1 - e) * math.log2(1 - e))(eps)
    bound = h + eps * math.log2(math.e * I / eps) + math.log2(3) * T + I * math.log2(math.e * ECr / I)
    cov = covers(r)
    worst1 = worst2 = 0.0
    for R in itertools.combinations(range(n), r):
        Rbit = 1 << idx[R]
        A = [vmask[u] & ~Rbit for u in R]
        # exact Pr[S meets all A_i]
        meets = np.ones(1 << N, dtype=bool)
        for a in A:
            meets &= (X & a) != 0
        lhs = float(P[meets].sum())
        # a_J and g
        aJ = {}
        g = np.zeros(1 << N, dtype=bool)
        for (V, mk), p in zip(copies, present):
            J = frozenset(i for i, u in enumerate(R) if u in V)
            if not J:
                g |= p
            else:
                aJ[J] = aJ.get(J, np.zeros(1 << N, dtype=bool)) | p
        # fibre-level middle bound: fibre = assignment of variables outside union(A)
        Aall = A[0] | A[1] | A[2]
        out_key = X & ~Aall
        # E_fibre prod a_J for each cover, then (sum sqrt)^2 averaged with 1(g=0); covers streamed, not stored
        uniq, inv = np.unique(out_key, return_inverse=True)
        cnt = np.bincount(inv).astype(np.float64)
        s = np.zeros(len(uniq))
        mean_sum = 0.0
        zero = np.zeros(1 << N, dtype=bool)
        for fam in cov:
            prod = np.ones(1 << N, dtype=bool)
            for J in fam:
                prod &= aJ.get(frozenset(J), zero)
            t = prod.astype(np.float64)
            s += np.sqrt(np.bincount(inv, weights=t, minlength=len(uniq)) / cnt)
            mean_sum += float(t.mean())
        g_f = np.bincount(inv, weights=g.astype(np.float64), minlength=len(uniq)) / cnt   # g is constant on fibres
        mid = 4 * float(((s ** 2) * (g_f < 0.5) * cnt).sum() / (1 << N))
        top = 4 * len(cov) * mean_sum * (1 - float(g.mean()))
        worst1 = max(worst1, lhs / mid if mid > 0 else (0 if lhs < 1e-15 else float('inf')))
        worst2 = max(worst2, mid / top if top > 0 else 0)
    ok = H <= bound + 1e-9 and worst1 <= 1 + 1e-9 and worst2 <= 1 + 1e-9
    print(f"r=3 n={n} k={k}: H/I={H/I:.4f} vertex-coding bound/I={bound/I:.4f} E C(v,3)/I={ECr/I:.3f} "
          f"T/I={T/I:.3f} | r-set lemma: exact/middle max {worst1:.4f}, middle/final max {worst2:.4f} "
          f"(c_3 = {len(cov)}) {'ok' if ok else 'FAIL'}")


if __name__ == "__main__":
    for n, k in [(5, 4), (5, 5), (6, 4), (6, 5)]:
        run(n, k)
