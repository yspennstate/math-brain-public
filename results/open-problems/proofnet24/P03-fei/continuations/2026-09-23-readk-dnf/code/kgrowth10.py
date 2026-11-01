"""Supplement to kgrowth.py: random monotone and non-monotone read-k formulas with k = 9, 10 (<= 20 terms)."""
import numpy as np
from feicore import spectrum, entropy, total_influence, polite
from termref import term_ref_cost
from readk_nonmono import random_nonmono
polite()
rng = np.random.default_rng(1010)
worst = 0.0
for (n, k, w) in [(14, 10, 5), (13, 9, 5), (14, 10, 4), (12, 10, 5)]:
    for r in range(4):
        for pneg in (0.0, 0.5):
            terms = random_nonmono(n, k, [w] * 40, rng, pneg=pneg)[:20]
            N = 1 << n; xs = np.arange(N, dtype=np.int64); sat = np.zeros(N, dtype=bool)
            for (mm, v) in terms: sat |= (xs & mm) == v
            tt = np.where(sat, -1, 1).astype(np.int8)
            P = spectrum(tt); H = entropy(P); I = total_influence(P, n)
            kk = max(sum(1 for (mm, v) in terms if mm >> j & 1) for j in range(n))
            best = min(term_ref_cost(P, n, [mm for (mm, v) in terms], c)[0] for c in (1/16, 1/4, 1/2, 1, 2, 4, 8))
            worst = max(worst, best / I)
            print(f"n={n} k={kk} m={len(terms)} pneg={pneg} H/I={H/I:.3f} gibbs/I={best/I:.3f}", flush=True)
print(f"max gibbs/I = {worst:.3f}")
