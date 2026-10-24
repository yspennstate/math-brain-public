"""Theorem 4.5 extended: unions of pieces h_l = AND of up to m threshold functions (each on a subset of R_l),
every variable in at most k of the sets R_l.  The reference is that of Theorem 4.5 with
theta_s(i) = max_r min(1, (s / rank_{l,r}(i))^a) over the threshold functions r of piece l containing i, and
F^j_l = min_r ln(rank_{l,r}(j) / (|S cap U^{l,r}_j| + 1)).  Checks, per set: the run's code length L satisfies
L <= |A| (Ku + log2 m) + sum_j G_j (the proof's per-set inequality with the extra log m), the Kraft sum <= 1,
and H <= h(Var) + Var Lam + sum P L."""
import math, sys, numpy as np
from collections import deque
from feicore import spectrum, entropy, total_influence, popcounts, polite
from unionltf import ltf_on
from unionanimal import esym, scc_initial
polite()
LN2 = math.log(2); A_EXP = 1.44; BETA = 10.0; C2 = 1.0

def build(n, k, mm, rng, mmax=8):
    deg = np.zeros(n, dtype=int); fam = []
    for _ in range(300):
        if len(fam) >= mmax: break
        size = int(rng.integers(2, min(6, n) + 1))
        cand = [j for j in range(n) if deg[j] < k]
        if len(cand) < size: continue
        R = sorted(rng.choice(cand, size=size, replace=False).tolist())
        for j in R: deg[j] += 1
        parts = []
        for r in range(mm):
            sz = int(rng.integers(1, len(R) + 1))
            parts.append(sorted(rng.choice(R, size=sz, replace=False).tolist()))
        fam.append((R, parts))
    return fam

def analyse(n, k, mm, rng):
    fam = build(n, k, mm, rng)
    N = 1 << n; xs = np.arange(N)
    pieces = []
    for R, parts in fam:
        hs, ws, Rs = [], [], []
        for Rr in parts:
            h, w = ltf_on(Rr, n, rng)
            if h.all() or (~h).all(): continue
            rel = [j for j in Rr if np.any(h[xs[(xs >> j) & 1 == 0]] != h[xs[(xs >> j) & 1 == 0] | (1 << j)])]
            if not rel: continue
            hs.append(h); ws.append(w); Rs.append(rel)
        if not hs: continue
        hl = np.logical_and.reduce(hs)
        if hl.all() or (~hl).all(): continue
        rel = sorted({j for Rr in Rs for j in Rr if np.any(hl[xs[(xs >> j) & 1 == 0]] != hl[xs[(xs >> j) & 1 == 0] | (1 << j)])})
        if not rel: continue
        pieces.append((hl, Rs, ws, rel))
    if not pieces: return None
    deg = np.zeros(n, dtype=int)
    for p in pieces:
        for j in p[3]: deg[j] += 1
    kk = int(max(1, deg.max())); m = len(pieces)
    V = np.stack([p[0] for p in pieces]); out = V.any(axis=0)
    if out.all() or (~out).all(): return None
    g = np.where(out, -1.0, 1.0)
    P = spectrum(g); H = entropy(P); I = total_influence(P, n); Var = float(P[1:].sum())
    pis = np.minimum(V.mean(axis=1), 0.5)
    lam = 1.0 / kk
    Lam = float(np.sum(np.log2(1 + lam * pis)))
    mfun = max(len(p[1]) for p in pieces)
    rank = {}; Umask = {}; Rmask = []
    for l, (hl, Rs, ws, rel) in enumerate(pieces):
        acc_all = 0
        for r, (Rr, w) in enumerate(zip(Rs, ws)):
            order = sorted(Rr, key=lambda j: (-abs(w[j]), j)); acc = 0
            for pos, j in enumerate(order):
                rank[(l, r, j)] = pos + 1; Umask[(l, r, j)] = acc; acc |= 1 << j
        for j in rel: acc_all |= 1 << j
        Rmask.append(acc_all)
    lamd = np.log2(1 / pis) / BETA
    funcs_of = {j: [l for l in range(m) if Rmask[l] >> j & 1] for j in range(n)}
    rel_all = 0
    for Rm in Rmask: rel_all |= Rm
    popc = lambda x: bin(x).count("1")
    def theta(l, s, i):
        best = 0.0
        for r in range(len(pieces[l][1])):
            if (l, r, i) in rank: best = max(best, min(1.0, (s / rank[(l, r, i)]) ** A_EXP))
        return best
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
                Fs = [math.log(rank[(l, r, j)] / (popc(S & Umask[(l, r, j)]) + 1)) for r in range(len(pieces[l][1])) if (l, r, j) in rank]
                if not Fs: continue
                G = A_EXP * min(Fs) / LN2 + C2 * math.log2(1 / pis[l]) * (kap[l] < lamd[l])
                if best is None or G < best[0]: best = (G, l)
            tau[j] = best[1]; Gsum += best[0]
        A = {}
        for j, l in tau.items(): A.setdefault(l, []).append(j)
        Fl = list(A.keys())
        Amask = {l: sum(1 << j for j in A[l]) for l in Fl}
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
            members = [i for i in range(n) if Rmask[l] >> i & 1]
            Z = esym([theta(l, s, i) for i in members], s)
            L += math.log2(s * (s + 1)) + math.log2(Z) - sum(math.log2(theta(l, s, i)) for i in A[l])
            L += math.log2((c + 1) * (c + 2))
            if c: L += (math.lgamma(s + c) - math.lgamma(c + 1) - math.lgamma(s)) / LN2 + c * math.log2(kk)
        kraft += 2.0 ** -(L + Lam)
        worst = min(worst, len(els) * (Ku + math.log2(max(mfun, 1))) + Gsum - L)
        if P[S] > 0: EL += P[S] * L
    hE = 0.0 if Var in (0, 1) else -(Var * math.log2(Var) + (1 - Var) * math.log2(1 - Var))
    bound = hE + Var * Lam + EL
    assert H <= bound + 1e-9, (H, bound)
    assert kraft <= 1 + 1e-9
    return dict(k=kk, m=m, mfun=mfun, HI=H / I, bound=bound / I, kraft=kraft, slack=worst)

if __name__ == '__main__':
    rng = np.random.default_rng(11)
    for n in (10, 12):
        for k in (1, 2, 3):
            for mm in (2, 3):
                for rep in range(2):
                    a = analyse(n, k, mm, rng)
                    if a is None: continue
                    print(f"n={n} k={a['k']} pieces={a['m']} m={a['mfun']}: H/I={a['HI']:5.2f} bound/I={a['bound']:6.2f} kraft={a['kraft']:.3f} min per-set slack={a['slack']:.2f}", flush=True)
