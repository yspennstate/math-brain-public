"""Exact table for the paper: reference measure of the proof (pi_t = 2^{-|V_t|}, eta = Var)."""
import math, numpy as np
from feicore import spectrum, entropy, total_influence, polite
from termref import dnf_tt, term_ref_cost, random_readk, random_regular, star_terms
from readk_linear import analyse as analyse_signed
from readk_nonmono import random_nonmono
polite()
def row(name, n, terms):
    tt = dnf_tt(n, terms); P = spectrum(tt); H = entropy(P); I = total_influence(P, n)
    tot, _ = term_ref_cost(P, n, terms, 1.0)
    k = max(sum(1 for t in terms if t >> j & 1) for j in range(n))
    print(f"{name:52s} n={n:2d} k={k} H/I={H/I:.3f} gibbs/I={tot/I:.3f} gap={tot/I-H/I:.3f}", flush=True)
    return H/I, tot/I
rng = np.random.default_rng(3)
row('tribes, 3 terms of width 5', 15, [((1<<5)-1) << (5*t) for t in range(3)])
for (s, d) in [(12, 3), (16, 3), (12, 4)]:
    E = random_regular(s, d, rng); row(f'stars of random {d}-regular graph on {s} vertices', len(E), star_terms(s, E))
for r in range(2):
    row('random monotone read-3, widths 5', 20, random_readk(20, 3, [5]*12, rng))
# the 192 signed formulas of readk_linear.py, same seed and order
rng2 = np.random.default_rng(23)
configs = [(10, 2, [2, 2, 3, 3, 3, 4]), (12, 2, [3] * 8), (12, 3, [2, 3, 3, 4, 4, 2, 3, 5, 2]),
           (14, 2, [4] * 7), (14, 3, [3, 3, 4, 4, 5, 5, 3, 4, 5, 6]), (14, 4, [2, 3, 3, 4, 4, 5, 2, 3, 4, 5, 6, 3]),
           (16, 3, [4] * 12), (12, 5, [2, 2, 2, 3, 3, 3, 4, 4, 2, 3, 2, 5])]
mh = mg = mgap = 0.0; cnt = 0
for n, k, wl in configs:
    for r in range(8):
        for pneg in (0.0, 0.3, 0.5):
            terms = random_nonmono(n, k, wl, rng2, pneg=pneg)
            if len(terms) < 1: continue
            a = analyse_signed(n, terms); cnt += 1
            mh = max(mh, a['HI']); mg = max(mg, a['gibI']); mgap = max(mgap, a['gibI'] - a['HI'])
print(f"signed random read-k formulas: count={cnt} max H/I={mh:.3f} max gibbs/I={mg:.3f} max gap={mgap:.3f}")
