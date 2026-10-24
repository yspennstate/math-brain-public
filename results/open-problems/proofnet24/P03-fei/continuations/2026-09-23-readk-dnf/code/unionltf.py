"""Read-k unions of threshold functions: f = h_1 v ... v h_m, h_l an LTF on R_l, every variable in <= k of the R_l.
Checks for the proof of H <= (C0 + C1 k) I:
 (a) H/I and the FEI+ ratio;
 (b) path lemma  p0 * sum_l Pr[h_l=1] <= (k/4) I;
 (c) per piece (least pivotal h_l through j): rank tail E F_l <= L1 = 4.1511, and the level tail
     K = log2(1/pi'_l) * nu_{j,s}(|S cap R_l| < log2(1/pi'_l)/beta), pi' = min(pi, 1/2);
 (d) the realized proof bound  h(eps) + eps*Lambda + E[(beta+c1) sum_{l in D(S)} kappa_l + sum_{j in S}(1 + G_j(S))]
     against H (it must be >= H - it is an upper bound on the Gibbs bound of a valid reference)."""
import math, numpy as np
from feicore import spectrum, entropy, total_influence, popcounts, polite, wht
polite()
LN2 = math.log(2); B = 3 * math.sqrt(3 / math.pi); L1 = 2 * math.log(B) + 2
A_EXP = 1.44; BETA = 5.0; C1 = 1 + A_EXP / (A_EXP - 1); C2 = 1 + C1 / BETA   # the paper's parameters

def build(n, k, rng, mmax=12):
    deg = np.zeros(n, dtype=int); fam = []
    for _ in range(200):
        if len(fam) >= mmax: break
        size = int(rng.integers(1, min(6, n) + 1))
        cand = [j for j in range(n) if deg[j] < k]
        if len(cand) < size: continue
        R = sorted(rng.choice(cand, size=size, replace=False).tolist())
        for j in R: deg[j] += 1
        fam.append(R)
    return fam

def ltf_on(R, n, rng):
    xs = np.arange(1 << n)
    bits = ((xs[:, None] >> np.arange(n)[None, :]) & 1) * 2 - 1
    w = np.zeros(n); s = rng.choice([-1, 1], size=len(R)); mag = rng.exponential(size=len(R)) + 0.05
    w[R] = s * mag
    theta = float(rng.uniform(-1, 1) * mag.sum() * rng.choice([0.3, 0.8, 1.0]))
    h = (bits @ w - theta) > 0
    return h, w

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
    kk = int(deg.max())
    V = np.stack(H_l); out = V.any(axis=0)
    if out.all() or (~out).all(): return None
    g = np.where(out, -1.0, 1.0)
    P = spectrum(g); H = entropy(P); I = total_influence(P, n)
    Var = float(P[1:].sum()); Hplus = float(-(P[1:][P[1:] > 1e-300] * np.log2(P[1:][P[1:] > 1e-300])).sum())
    p0 = float((~out).mean()); pis = V.mean(axis=1); pip = np.minimum(pis, 0.5)
    m = len(H_l)
    # ranks within each h_l (by |w| decreasing over its relevant set)
    rank = np.full((m, n), 10 ** 6, dtype=float); Umask = np.zeros((m, n), dtype=np.int64); Rmask = np.zeros(m, dtype=np.int64)
    for l in range(m):
        order = sorted(R_l[l], key=lambda j: (-abs(W_l[l][j]), j))
        acc = 0
        for pos, j in enumerate(order):
            rank[l, j] = pos + 1; Umask[l, j] = acc; acc |= 1 << j
        Rmask[l] = acc
    kappa = np.stack([pc[xs & int(Rmask[l])] for l in range(m)])        # m x N : |S cap R_l|
    lam = np.log2(1 / pip) / BETA
    dense = kappa >= lam[:, None]                                         # m x N
    # (c) pieces
    worst_rank = 0.0; worst_K = 0.0
    for j in range(n):
        rest = xs[(xs >> j) & 1 == 0]; up = rest | (1 << j)
        d = out[up].astype(float) - out[rest].astype(float)
        if not np.any(d): continue
        taken = np.zeros(len(rest), dtype=bool)
        for l in range(m):
            if j not in R_l[l]: continue
            piv = V[l][up] != V[l][rest]
            sel = piv & (d != 0) & ~taken
            taken |= piv & (d != 0)
            if not sel.any(): continue
            Dl = np.zeros(N); Dl[rest] = d * sel; Dl[up] = d * sel
            c = wht(Dl) / N; nu = c ** 2; nu /= nu.sum()                   # law of T (subsets not containing j)
            Fl = np.log(rank[l, j] / (pc[xs & int(Umask[l, j])] + 1.0))
            worst_rank = max(worst_rank, float((nu * Fl).sum()))
            kS = pc[xs & int(Rmask[l])] + 1                                  # |S cap R_l| with S = T + j
            tail = float(nu[kS < lam[l]].sum())
            worst_K = max(worst_K, math.log2(1 / pip[l]) * tail)
    # (d) realized proof bound
    Lam = float(np.sum(np.log2(1 / (1 - pip))))
    eps = Var
    hE = 0.0 if eps in (0, 1) else -(eps * math.log2(eps) + (1 - eps) * math.log2(1 - eps))
    cost = np.zeros(N)
    cost += (BETA + C1) * (kappa * dense).sum(axis=0)
    for j in range(n):
        inS = ((xs >> j) & 1) == 1
        best = np.full(N, np.inf)
        for l in range(m):
            if j not in R_l[l]: continue
            Fl = np.log(rank[l, j] / (pc[xs & int(Umask[l, j])] + 1.0))
            val = A_EXP * Fl / LN2 + C2 * math.log2(1 / pip[l]) * (~dense[l])
            best = np.minimum(best, val)
        cost += inS * (1 + np.where(np.isfinite(best), best, 0))
    bound = hE + eps * Lam + float((P[1:] * cost[1:]).sum())
    return dict(HI=H / I, FP=Hplus / (I - Var) if I - Var > 1e-12 else 0, path=p0 * float(pis.sum()) / (kk / 4 * I),
                rank=worst_rank, K=worst_K, bound=bound / I, gap=bound - H, k=kk, m=m)

if __name__ == '__main__':
    rng = np.random.default_rng(99)
    res = {}
    for n in (10, 12, 14):
        for k in (1, 2, 3, 4):
            for rep in range(8 if n < 14 else 3):
                a = analyse(n, k, rng)
                if a is None: continue
                key = a['k']
                w = res.setdefault(key, dict(HI=0, FP=0, path=0, rank=0, K=0, bound=0, gapmin=1e9, cnt=0))
                for f in ('HI', 'FP', 'path', 'rank', 'K', 'bound'): w[f] = max(w[f], a[f])
                w['gapmin'] = min(w['gapmin'], a['gap']); w['cnt'] += 1
    for key in sorted(res):
        w = res[key]
        print(f"k={key} ({w['cnt']} formulas): max H/I {w['HI']:.3f}, max FEI+ {w['FP']:.3f}, "
              f"max path ratio {w['path']:.3f} (<=1), max piece rank E F {w['rank']:.3f} (L1 {L1:.3f}), "
              f"max K {w['K']:.3f}, max bound/I {w['bound']:.2f}, min (bound - H) {w['gapmin']:.3f}", flush=True)
