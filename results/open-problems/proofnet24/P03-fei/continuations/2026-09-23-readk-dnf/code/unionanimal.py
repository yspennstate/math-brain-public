"""Rooted-animal reference for read-k unions of regular (threshold) functions.
Per nonempty S: G_j(l) = (a/ln2) F^j_l + c2 log2(1/pi_l) [l not dense]; tau(j) = argmin_l G_j(l);
A_l = tau^{-1}(l); F = {l : A_l nonempty}; digraph l -> l' iff A_l meets R_l'; one root per initial SCC
(roots activated with prob lam pi_l/(1+lam pi_l), lam = 1/k); BFS children attached through an element of
the parent's A_l and an index among <= k functions; each A_l drawn from the level-normalised rank law of h_l
at level s_l = |A_l| (theta_s(i) = min(1,(s/r_l(i))^a), exact normaliser e_s).
Checks: Kraft sum over all sets <= 1, H <= h(Var) + Var Lam + sum P L, and the growth with k."""
import math, numpy as np
from collections import deque
from feicore import spectrum, entropy, total_influence, popcounts, polite
from unionltf import build, ltf_on
polite()
import sys
LN2 = math.log(2); A_EXP = 1.44; BETA = float(sys.argv[1]) if len(sys.argv) > 1 else 10.0; C2 = 1.0

def esym(vals, s):
    e = np.zeros(s + 1); e[0] = 1.0
    for v in vals:
        for t in range(s, 0, -1):
            e[t] += e[t - 1] * v
    return e[s]

def scc_initial(nodes, adj):
    # Tarjan; returns list of SCCs and which are initial (no incoming edge from another SCC)
    index = {}; low = {}; st = []; on = set(); comps = []; cnt = [0]
    import sys
    sys.setrecursionlimit(10000)
    def strong(v):
        index[v] = low[v] = cnt[0]; cnt[0] += 1; st.append(v); on.add(v)
        for w in adj[v]:
            if w not in index:
                strong(w); low[v] = min(low[v], low[w])
            elif w in on:
                low[v] = min(low[v], index[w])
        if low[v] == index[v]:
            comp = []
            while True:
                w = st.pop(); on.discard(w); comp.append(w)
                if w == v: break
            comps.append(comp)
    for v in nodes:
        if v not in index: strong(v)
    cid = {v: i for i, c in enumerate(comps) for v in c}
    has_in = [False] * len(comps)
    for v in nodes:
        for w in adj[v]:
            if cid[v] != cid[w]: has_in[cid[w]] = True
    return comps, [not h for h in has_in]

def analyse(n, k, rng):
    fam = build(n, k, rng)
    N = 1 << n; xs = np.arange(N); pc = popcounts(n)
    H_l, R_l, W_l = [], [], []
    for R in fam:
        h, w = ltf_on(R, n, rng)
        if h.all() or (~h).all(): continue
        rel = [j for j in R if np.any(h[xs[(xs >> j) & 1 == 0]] != h[xs[(xs >> j) & 1 == 0] | (1 << j)])]
        if not rel: continue
        H_l.append(h); R_l.append(rel); W_l.append(w)
    if not H_l: return None
    deg = np.zeros(n, dtype=int)
    for R in R_l:
        for j in R: deg[j] += 1
    kk = int(deg.max()); m = len(H_l)
    V = np.stack(H_l); out = V.any(axis=0)
    if out.all() or (~out).all(): return None
    g = np.where(out, -1.0, 1.0)
    P = spectrum(g); H = entropy(P); I = total_influence(P, n); Var = float(P[1:].sum())
    pis = np.minimum(V.mean(axis=1), 0.5)
    lam = 1.0 / kk
    Lam = float(np.sum(np.log2(1 + lam * pis)))
    rank = {}; Rmask = []; Umask = {}
    for l in range(m):
        order = sorted(R_l[l], key=lambda j: (-abs(W_l[l][j]), j))
        acc = 0
        for pos, j in enumerate(order):
            rank[(l, j)] = pos + 1; Umask[(l, j)] = acc; acc |= 1 << j
        Rmask.append(acc)
    lamd = np.log2(1 / pis) / BETA
    funcs_of = {j: [l for l in range(m) if Rmask[l] >> j & 1] for j in range(n)}
    rel = 0
    for Rm in Rmask: rel |= Rm
    popc = lambda x: bin(x).count("1")
    kraft = 0.0; EL = 0.0; EG = 0.0; worst = float('inf')
    Ku = (1 + A_EXP) * math.log2(kk) + BETA + 1 + 2 * math.log2(3) + math.log2(math.e * A_EXP / (A_EXP - 1)) + math.log2(2 * math.e)
    for S in range(1, N):
        if S & ~rel: continue
        els = [j for j in range(n) if S >> j & 1]
        kap = [popc(S & Rmask[l]) for l in range(m)]
        tau = {}; Gsum = 0.0
        for j in els:
            best = None
            for l in funcs_of[j]:
                F = math.log(rank[(l, j)] / (popc(S & Umask[(l, j)]) + 1))
                G = A_EXP * F / LN2 + C2 * math.log2(1 / pis[l]) * (kap[l] < lamd[l])
                if best is None or G < best[0]: best = (G, l)
            tau[j] = best[1]; Gsum += best[0]
        A = {}
        for j, l in tau.items(): A.setdefault(l, []).append(j)
        Fs = list(A.keys())
        Amask = {l: sum(1 << j for j in A[l]) for l in Fs}
        adj = {l: [l2 for l2 in Fs if l2 != l and (Amask[l] & Rmask[l2])] for l in Fs}
        comps, initial = scc_initial(Fs, adj)
        roots = [min(c, key=lambda l: math.log2(1 / (lam * pis[l]))) for c, ini in zip(comps, initial) if ini]
        par = {r: None for r in roots}; order = list(roots); dq = deque(roots)
        while dq:
            u = dq.popleft()
            for v in adj[u]:
                if v not in par: par[v] = u; order.append(v); dq.append(v)
        assert len(par) == len(Fs)
        L = sum(math.log2(1 / (lam * pis[r])) for r in roots)
        for l in order:
            s = len(A[l]); ch = [v for v in order if par.get(v) == l]; c = len(ch)
            th = [min(1.0, (s / rank[(l, i)]) ** A_EXP) for i in R_l[l]]
            Z = esym(th, s)
            L += math.log2(s * (s + 1)) + math.log2(Z) - sum(math.log2(min(1.0, (s / rank[(l, i)]) ** A_EXP)) for i in A[l])
            L += math.log2((c + 1) * (c + 2))
            if c:
                L += (math.lgamma(s + c) - math.lgamma(c + 1) - math.lgamma(s)) / LN2 + c * math.log2(kk)
        kraft += 2.0 ** -(L + Lam)
        worst = min(worst, len(els) * Ku + Gsum - L)
        if P[S] > 0:
            EL += P[S] * L; EG += P[S] * Gsum
    hE = 0.0 if Var in (0, 1) else -(Var * math.log2(Var) + (1 - Var) * math.log2(1 - Var))
    bound = hE + Var * Lam + EL
    assert H <= bound + 1e-9, (H, bound)
    return dict(k=kk, m=m, HI=H / I, bound=bound / I, kraft=kraft, VL=Var * Lam / I, EG=EG / I, slack=worst)

if __name__ == '__main__':
    rng = np.random.default_rng(7)
    for n in (10, 12):
        for k in (1, 2, 3, 4, 5, 6):
            for rep in range(3):
                a = analyse(n, k, rng)
                if a is None: continue
                print(f"n={n} k={a['k']} m={a['m']:2d}: H/I={a['HI']:5.2f} bound/I={a['bound']:6.2f} kraft={a['kraft']:.3f} VarLam/I={a['VL']:.2f} E sum G/I={a['EG']:.2f} min per-set slack={a['slack']:.3f}", flush=True)
