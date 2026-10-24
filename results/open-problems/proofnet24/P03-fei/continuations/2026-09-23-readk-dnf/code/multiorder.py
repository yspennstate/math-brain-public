"""Functions of m linear threshold functions with ARBITRARY (different) weight orders.
Claim to test: H(f) <= [3.886 + (ln m + ln(ea/(a-1)) + a*R/I)/ln2] I, where
R = E_S sum_{i in S} min_l ln+(r_l(i)/|S|)  (r_l = rank of i by |w_l| decreasing),
and the proof bounds R <= I * inf_lambda (ln m - ln(1-2 lambda))/lambda + 2 ln B  (Donsker-Varadhan),
via the per-piece rank tail E_{nu_{i,l}} ln(r_l(i)/(|T cap U_i^l|+1)) <= L_1.
Also reports the single-order quantity (order of h_1 only) to show why one order is not enough."""
import math, numpy as np
from feicore import spectrum, entropy, total_influence, popcounts, polite, wht
polite()
LN2 = math.log(2); B = 3 * math.sqrt(3 / math.pi); L1 = 2 * math.log(B) + 2

def ltf_tt(w, theta, n):
    xs = np.arange(1 << n)
    bits = ((xs[:, None] >> np.arange(n)[None, :]) & 1) * 2 - 1
    return (bits @ w - theta) > 0            # True = +1 side

def dv_bound(m):
    if m == 1: return L1
    best = min((math.log(m) - math.log(1 - 2 * lam)) / lam for lam in np.linspace(0.01, 0.49, 481))
    return best + 2 * math.log(B)

def analyse(n, Ws, thetas, gate):
    m = len(Ws); N = 1 << n; xs = np.arange(N); pc = popcounts(n)
    H_l = [ltf_tt(w, th, n) for w, th in zip(Ws, thetas)]
    V = np.stack(H_l)
    if gate == 'AND': out = V.all(axis=0)
    elif gate == 'OR': out = V.any(axis=0)
    elif gate == 'MAJ': out = V.sum(axis=0) * 2 > m
    else: out = (V.sum(axis=0) % 2) == 1
    if out.all() or (~out).all(): return None
    g = np.where(out, -1.0, 1.0)
    P = spectrum(g); H = entropy(P); I = total_influence(P, n)
    # ranks r_l(i) in 1..n by |w_l| decreasing (ties by index)
    ranks = []
    for w in Ws:
        order = sorted(range(n), key=lambda j: (-abs(w[j]), j))
        r = np.empty(n, dtype=int)
        for pos, j in enumerate(order): r[j] = pos + 1
        ranks.append(r)
    ranks = np.array(ranks)                 # m x n
    # R_multi and R_single exactly
    size = np.maximum(pc, 1)
    Rm = 0.0; Rs = 0.0
    for i in range(n):
        inS = ((xs >> i) & 1) == 1
        vals = np.log(np.maximum(1.0, ranks[:, i][:, None] / size[None, :]))   # m x N
        Rm += float((P * inS * vals.min(axis=0)).sum())
        Rs += float((P * inS * vals[0]).sum())
    # per-piece rank tails (first responsible LTF), worst over (i, l)
    worst_tail = 0.0
    for i in range(n):
        rest = xs[(xs >> i) & 1 == 0]; up = rest | (1 << i)
        d = out[up].astype(float) - out[rest].astype(float)
        if not np.any(d): continue
        piv = [(V[l][up] != V[l][rest]) for l in range(m)]
        taken = np.zeros(len(rest), dtype=bool)
        for l in range(m):
            sel = piv[l] & (d != 0) & ~taken
            taken |= piv[l] & (d != 0)
            if not sel.any(): continue
            Dl = np.zeros(N); Dl[rest] = d * sel; Dl[up] = d * sel
            c = wht(Dl) / N; nu = c ** 2; nu /= nu.sum()
            Umask = 0
            for j in range(n):
                if ranks[l][j] < ranks[l][i]: Umask |= 1 << j
            kap = pc[xs & Umask]
            val = float((nu * np.log(ranks[l][i] / (kap + 1.0))).sum())
            worst_tail = max(worst_tail, val)
    return dict(HI=H / I, Rm=Rm / I, Rs=Rs / I, tail=worst_tail, m=m)

if __name__ == '__main__':
    rng = np.random.default_rng(2026)
    res = {}
    for n in (8, 10, 12):
        for m in (2, 3, 4):
            for gate in ('AND', 'OR', 'MAJ', 'XOR'):
                if gate == 'MAJ' and m % 2 == 0: continue
                for r in range(6):
                    if r < 2:   # adversarial: opposite orders
                        base = np.arange(n, 0, -1).astype(float)
                        Ws = [base if l % 2 == 0 else base[::-1].copy() for l in range(m)]
                        Ws = [w * rng.choice([-1, 1], size=n) for w in Ws]
                    else:
                        Ws = [rng.normal(size=n) * rng.exponential(size=n) for _ in range(m)]
                    thetas = [float(rng.uniform(-0.5, 0.5) * np.abs(w).sum()) for w in Ws]
                    a = analyse(n, Ws, thetas, gate)
                    if a is None: continue
                    key = (m, gate)
                    w = res.setdefault(key, dict(HI=0.0, Rm=0.0, Rs=0.0, tail=0.0))
                    for kk in w: w[kk] = max(w[kk], a[kk])
    for (m, gate), w in sorted(res.items()):
        print(f"m={m} {gate:3s}: max H/I={w['HI']:.3f}  max R_multi/I={w['Rm']:.3f} (DV bound {dv_bound(m):.3f})  "
              f"max R_single/I={w['Rs']:.3f}  worst piece tail={w['tail']:.3f} (L1={L1:.3f})", flush=True)
