"""Corollary of Theorem 4.6: read-k unions of arbitrary w-juntas (each h_l a Boolean function of its <= w variables,
viewed as a function of w dictators, M = w).  Same reference and checks as unionmulti.py with sub-functions =
dictators (rank 1 in their own order)."""
import math, sys, numpy as np
from collections import deque
from feicore import spectrum, entropy, total_influence, polite
from unionanimal import esym, scc_initial
polite()
LN2 = math.log(2); A_EXP = 1.44; BETA = 10.0
def analyse(n, k, w, rng, mmax=8):
    deg = np.zeros(n, dtype=int); fam = []
    N = 1 << n; xs = np.arange(N)
    for _ in range(300):
        if len(fam) >= mmax: break
        size = int(rng.integers(2, w + 1))
        cand = [j for j in range(n) if deg[j] < k]
        if len(cand) < size: continue
        R = sorted(rng.choice(cand, size=size, replace=False).tolist())
        tt = rng.random(1 << size) < rng.uniform(0.05, 0.6)
        idx = np.zeros(N, dtype=int)
        for b, j in enumerate(R): idx |= ((xs >> j) & 1) << b
        h = tt[idx]
        if h.all() or (~h).all(): continue
        rel = [j for j in R if np.any(h[xs[(xs >> j) & 1 == 0]] != h[xs[(xs >> j) & 1 == 0] | (1 << j)])]
        if not rel: continue
        for j in R: deg[j] += 1
        fam.append((h, rel))
    if not fam: return None
    m = len(fam); kk = int(max(1, max(sum(1 for f in fam if j in f[1]) for j in range(n))))
    V = np.stack([f[0] for f in fam]); out = V.any(axis=0)
    if out.all() or (~out).all(): return None
    g = np.where(out, -1.0, 1.0)
    P = spectrum(g); H = entropy(P); I = total_influence(P, n); Var = float(P[1:].sum())
    pis = np.minimum(V.mean(axis=1), 0.5); lam = 1.0 / kk
    Lam = float(np.sum(np.log2(1 + lam * pis)))
    Rmask = [sum(1 << j for j in f[1]) for f in fam]
    lamd = np.log2(1 / pis) / BETA
    funcs_of = {j: [l for l in range(m) if Rmask[l] >> j & 1] for j in range(n)}
    rel_all = 0
    for Rm in Rmask: rel_all |= Rm
    popc = lambda x: bin(x).count("1")
    Mmax = max(len(f[1]) for f in fam)
    Ku = (1 + A_EXP) * math.log2(kk) + BETA + 1 + 2 * math.log2(3) + math.log2(math.e * A_EXP / (A_EXP - 1)) + math.log2(2 * math.e)
    kraft = 0.0; EL = 0.0; worst = float('inf')
    for S in range(1, N):
        if S & ~rel_all: continue
        els = [j for j in range(n) if S >> j & 1]
        kap = [popc(S & Rmask[l]) for l in range(m)]
        tau = {}; Gsum = 0.0
        for j in els:
            best = None
            for l in funcs_of[j]:
                G = math.log2(1 / pis[l]) * (kap[l] < lamd[l])        # F = 0 for a dictator
                if best is None or G < best[0]: best = (G, l)
            tau[j] = best[1]; Gsum += best[0]
        A = {}
        for j, l in tau.items(): A.setdefault(l, []).append(j)
        Fl = list(A.keys()); Amask = {l: sum(1 << j for j in A[l]) for l in Fl}
        adj = {l: [l2 for l2 in Fl if l2 != l and (Amask[l] & Rmask[l2])] for l in Fl}
        comps, initial = scc_initial(Fl, adj)
        roots = [min(c, key=lambda l: math.log2(1 / (lam * pis[l]))) for c, ini in zip(comps, initial) if ini]
        par = {r: None for r in roots}; order = list(roots); dq = deque(roots)
        while dq:
            u = dq.popleft()
            for v in adj[u]:
                if v not in par: par[v] = u; order.append(v); dq.append(v)
        L = sum(math.log2(1 / (lam * pis[r])) for r in roots)
        for l in order:
            s = len(A[l]); c = sum(1 for v in order if par.get(v) == l)
            Z = esym([1.0] * popc(Rmask[l]), s)                       # theta = 1 on every variable of R_l
            L += math.log2(s * (s + 1)) + math.log2(Z) + math.log2((c + 1) * (c + 2))
            if c: L += (math.lgamma(s + c) - math.lgamma(c + 1) - math.lgamma(s)) / LN2 + c * math.log2(kk)
        kraft += 2.0 ** -(L + Lam)
        worst = min(worst, len(els) * (Ku + math.log2(Mmax)) + Gsum - L)
        if P[S] > 0: EL += P[S] * L
    hE = 0.0 if Var in (0, 1) else -(Var * math.log2(Var) + (1 - Var) * math.log2(1 - Var))
    bound = hE + Var * Lam + EL
    assert H <= bound + 1e-9 and kraft <= 1 + 1e-9
    return dict(k=kk, m=m, w=Mmax, HI=H / I, bound=bound / I, kraft=kraft, slack=worst)
rng = np.random.default_rng(3)
for n in (10, 12):
    for k in (1, 2, 3):
        for w in (3, 4, 5):
            a = analyse(n, k, w, rng)
            if a: print(f"n={n} k={a['k']} pieces={a['m']} w={a['w']}: H/I={a['HI']:5.2f} bound/I={a['bound']:6.2f} kraft={a['kraft']:.3f} min per-set slack={a['slack']:.2f}", flush=True)
