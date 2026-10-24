"""Corollary 2 check: f(x) = G(w.x) with G changing sign t times (t = 2: slabs, t = 3).
Lemma 2 bound gets factor t; Lemma 3/4 constant L1 + 2 ln t.  Prints worst value/bound ratios and max H/I."""
import math
import numpy as np
from ltf_core import linform, spectrum, HI
import check_rank as cr

def table(w, ts):
    v = linform(np.asarray(w, float))
    # G(u) = (-1)^{#thresholds below u}: sign changes at each t in ts
    cnt = np.zeros(v.shape[0], int)
    for t in ts:
        cnt += (v > t)
    return np.where(cnt % 2 == 0, -1.0, 1.0)

rng = np.random.default_rng(21)
worst = dict(p1=0, p2=0, sig=0); maxratio = 0
for tr in range(240):
    n = int(rng.integers(4, 14)); t = 2 + tr % 2
    w = np.exp(rng.normal(0, 0.8, n)) if tr % 3 else rng.uniform(1, 2, n)
    s = np.linalg.norm(w)
    ts = np.sort(rng.normal(0, 1, t) * s) + 1e-9
    f = table(w, ts); c = spectrum(f); H, I = HI(c)
    if I < 1e-12: continue
    maxratio = max(maxratio, H / I)
    a = np.abs(w); order = np.argsort(-a, kind="stable"); rank = np.empty(n, np.int64); rank[order] = np.arange(1, n + 1)
    B = 3 * math.sqrt(3 / math.pi) * t; L = 2 * math.log(B) + 2
    for i in range(n):
        U = [j for j in range(n) if j != i and a[j] >= a[i] - 1e-12]; N = len(U) + 1
        if N < 2: continue
        um = sum(1 << j for j in U); cs = np.array([x for x in [0.25, 1.0, 4.0, 16.0] if x <= N], float)
        stab, elog, inf = cr.per_coord(c, n, i, um, float(N), cs)
        if inf < 1e-15: continue
        for q, cc in enumerate(cs):
            worst['p1'] = max(worst['p1'], stab[q] / (t * (2 / math.sqrt(math.pi)) / math.sqrt(cc) * inf))
        worst['p2'] = max(worst['p2'], (elog / inf) / L)
    sig, Hlev, Hcond = cr.sigma_and_cond(c, n, rank)
    worst['sig'] = max(worst['sig'], sig / (L * I))
print("max H/I over %s = %.4f" % ("t in {2,3}", maxratio))
print("worst ratios:", {k: round(v, 4) for k, v in worst.items()})
