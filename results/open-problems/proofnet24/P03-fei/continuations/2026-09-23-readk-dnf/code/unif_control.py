import numpy as np
from feicore import popcounts, wht
from readk_nonmono import random_nonmono
rng = np.random.default_rng(99)
n = 12; N = 1 << n; xs = np.arange(N, dtype=np.int64); pc = popcounts(n)
pos = neg = 0; worst_piece = 0.0; best_full = 0.0; best_corrupt = 0.0
for rep in range(30):
    terms = random_nonmono(n, 3, [2,3,3,4,4,2,3,5,2], rng, pneg=0.4)
    sat = np.array([((xs & mm) == v) for (mm, v) in terms]); fval = sat.any(axis=0)
    for i in range(n):
        Ti = [t for t in range(len(terms)) if terms[t][0] >> i & 1]
        if not Ti: continue
        rest = xs[(xs >> i) & 1 == 0]; up = rest | (1 << i)
        d = fval[up].astype(float) - fval[rest].astype(float)
        if not np.any(d): continue
        prev = np.zeros(len(rest), dtype=bool)
        for t in Ti:
            mm, v = terms[t]; Vm = mm & ~(1 << i)
            wit = (rest & Vm) == (v & Vm)
            piece = (d != 0) & wit & ~prev; prev |= wit
            if not piece.any() or bin(Vm).count('1') == 0: continue
            def dev(mask_vals):
                F = np.zeros(N); F[rest] = mask_vals; F[up] = mask_vals
                c2 = (wht(F) / N) ** 2; key = xs & Vm; u = np.unique(key)
                marg = np.bincount(key, weights=c2, minlength=N)[u]
                return float(np.max(np.abs(marg / c2.sum() - 1.0 / len(u))))
            worst_piece = max(worst_piece, dev(d * piece))                 # must be 0
            best_full = max(best_full, dev(d))                              # whole derivative: expected nonzero
            # corrupted piece: add one pivotal point from outside the witness subcube
            outside = np.nonzero((d != 0) & ~wit)[0]
            if len(outside):
                cp = piece.copy(); cp[outside[0]] = True
                best_corrupt = max(best_corrupt, dev(d * cp))              # expected nonzero
print(f"pieces (should be 0): {worst_piece:.2e}; whole derivative (control, should be >0): {best_full:.3f}; "
      f"piece + one outside point (control, should be >0): {best_corrupt:.3e}")
