"""Phi(S) = min |V(U)| over term sets U whose union covers S (the cheapest union cover).
If E_P[Phi(S)] <= C * I with C independent of k, then an overlap-aware (sequential) activation reference gives
H <= O(C) I + O(log k) I for read-k DNFs.  Measure E_P[Phi]/I and E_P[|U*|]/I on many families, incl. adversarial."""
import itertools, math, numpy as np
from feicore import spectrum, entropy, total_influence, popcounts, polite
from termref import dnf_tt, random_readk
from readk_nonmono import random_nonmono
polite()

def superset_min(W, n):
    g = W.copy()
    for i in range(n):
        g = g.reshape(-1, 2, 1 << i)
        g[:, 0, :] = np.minimum(g[:, 0, :], g[:, 1, :])
        g = g.reshape(-1)
    return g

def phi_stats(n, masks, P=None):
    m = len(masks); N = 1 << n
    pc = popcounts(n)
    unions = np.zeros(1 << m, dtype=np.int64); cnt = np.zeros(1 << m, dtype=np.int64)
    for j in range(m):
        h = 1 << j
        unions[h:2 * h] = unions[:h] | masks[j]; cnt[h:2 * h] = cnt[:h] + 1
    BIG = 10 ** 6
    W = np.full(N, BIG, dtype=np.int64)
    np.minimum.at(W, unions, pc[unions])          # cheapest union exactly equal to V
    Phi = superset_min(W, n)                      # cheapest union containing S
    # min #terms among covers achieving a union of size Phi is not needed; report min #terms among ALL covers
    W2 = np.full(N, BIG, dtype=np.int64)
    np.minimum.at(W2, unions, cnt)
    Kmin = superset_min(W2, n)
    return Phi, Kmin

def measure(name, n, terms):
    masks = [t if isinstance(t, (int, np.integer)) else t[0] for t in terms]
    if isinstance(terms[0], tuple):
        N = 1 << n; xs = np.arange(N, dtype=np.int64); sat = np.zeros(N, dtype=bool)
        for (mm, v) in terms: sat |= (xs & mm) == v
        tt = np.where(sat, -1, 1)
    else:
        tt = dnf_tt(n, masks)
    P = spectrum(tt); H = entropy(P); I = total_influence(P, n)
    Phi, Kmin = phi_stats(n, masks)
    sel = P > 1e-300; sel[0] = False
    ePhi = float((P[sel] * Phi[sel]).sum()); eK = float((P[sel] * Kmin[sel]).sum())
    k = max(sum(1 for mm in masks if mm >> j & 1) for j in range(n))
    return dict(name=name, n=n, m=len(masks), k=k, HI=H / I, PhiI=ePhi / I, KI=eK / I)

def show(d):
    print(f"{d['name']:30s} n={d['n']:2d} m={d['m']:2d} k={d['k']:2d} H/I={d['HI']:.3f} E[Phi]/I={d['PhiI']:.3f} E[#terms]/I={d['KI']:.3f}", flush=True)

def bits(ix):
    m = 0
    for j in ix: m |= 1 << int(j)
    return m

if __name__ == '__main__':
    for (b, k, p) in [(4, 4, 2), (4, 8, 2), (6, 6, 2), (3, 4, 3), (2, 6, 2), (2, 8, 2)]:
        n = b + k * p
        if n > 20: continue
        core = list(range(b))
        show(measure(f"sunflower b={b} k={k} p={p}", n, [bits(core + list(range(b + j * p, b + (j + 1) * p))) for j in range(k)]))
    fano = [(0, 1, 2), (0, 3, 4), (0, 5, 6), (1, 3, 5), (1, 4, 6), (2, 3, 6), (2, 4, 5)]
    show(measure("Fano lines", 7, [bits(l) for l in fano]))
    for (s, r) in [(6, 2), (7, 2), (6, 3)]:
        E = list(itertools.combinations(range(s), r)); n = len(E)
        show(measure(f"hyperstars s={s} r={r}", n, [bits([j for j, e in enumerate(E) if u in e]) for u in range(s)]))
    for n in (5, 6, 7):
        show(measure(f"thr2 of {n}", n, [bits(pq) for pq in itertools.combinations(range(n), 2)]))
    rng = np.random.default_rng(11)
    worst = {}
    for (n, k, w) in [(12, 2, 3), (12, 4, 3), (12, 6, 4), (14, 6, 5), (12, 8, 5), (16, 5, 4), (14, 8, 4), (14, 10, 5)]:
        for r in range(4):
            for pneg in (0.0, 0.5):
                terms = random_nonmono(n, k, [w] * 40, rng, pneg=pneg)
                if len(terms) > 20: terms = terms[:20]
                d = measure(f"rand n={n} k<={k} w={w}", n, terms)
                key = d['k']
                if key not in worst or d['PhiI'] > worst[key]['PhiI']: worst[key] = d
    print("--- worst E[Phi]/I per k among random formulas")
    for key in sorted(worst): show(worst[key])
