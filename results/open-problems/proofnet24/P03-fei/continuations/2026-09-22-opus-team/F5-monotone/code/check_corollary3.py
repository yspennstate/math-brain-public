"""Corollary 3 check: f = F(sgn(w1.x - t1), ..., sgn(wk.x - tk)) with co-monotone weight vectors (same order of
|w_j| in every vector) and F in {AND, parity, majority-of-3}.  Lemma 2 bound with factor k; Lemma 3/4 with
L1 + 2 ln k.  Prints worst value/bound ratios and max H/I."""
import math
import numpy as np
from ltf_core import linform, spectrum, HI
import check_rank as cr

rng = np.random.default_rng(31)
worst = dict(p1=0, p2=0, sig=0); maxratio = 0; cnt = 0
for tr in range(240):
    n = int(rng.integers(4, 13)); k = 2 + tr % 2
    base = np.sort(np.exp(rng.normal(0, 1.0, n)))[::-1]          # common order: coordinate 0 heaviest
    Ws = []
    for l in range(k):
        v = np.sort(np.exp(rng.normal(0, 1.0, n)))[::-1]         # any nonincreasing vector is co-monotone
        Ws.append(v * rng.choice([-1, 1], n))                    # signs are free
    outs = []
    for v in Ws:
        L = linform(v); th = rng.normal() * np.linalg.norm(v) * 0.8 + 1e-9
        outs.append(np.where(L > th, 1.0, -1.0))
    kind = tr % 3
    if kind == 0: f = np.where(np.all(np.array(outs) > 0, axis=0), 1.0, -1.0)
    elif kind == 1: f = np.prod(np.array(outs), axis=0)
    else:
        s = np.sum(np.array(outs[:3]) if k >= 3 else np.array(outs + [outs[0]]), axis=0); f = np.sign(s)
    c = spectrum(f); H, I = HI(c)
    if I < 1e-12: continue
    cnt += 1; maxratio = max(maxratio, H / I)
    rank = np.arange(1, n + 1)                                    # common order = index order
    B = 3 * math.sqrt(3 / math.pi) * k; Lc = 2 * math.log(B) + 2
    for i in range(n):
        U = [j for j in range(n) if j < i]                        # strictly heavier in every vector
        N = len(U) + 1
        if N < 2: continue
        um = sum(1 << j for j in U); cs = np.array([x for x in [0.25, 1.0, 4.0] if x <= N], float)
        stab, elog, inf = cr.per_coord(c, n, i, um, float(N), cs)
        if inf < 1e-15: continue
        for q, cc in enumerate(cs):
            worst['p1'] = max(worst['p1'], stab[q] / (k * (2 / math.sqrt(math.pi)) / math.sqrt(cc) * inf))
        worst['p2'] = max(worst['p2'], (elog / inf) / Lc)
    sig, Hlev, Hcond = cr.sigma_and_cond(c, n, rank.astype(np.int64))
    worst['sig'] = max(worst['sig'], sig / (Lc * I))
print("functions tested: %d   max H/I = %.4f" % (cnt, maxratio))
print("worst ratios:", {kk: round(v, 4) for kk, v in worst.items()})
