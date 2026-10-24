"""Brute-force check of the tower recursion (tower_erasure.py logic) on a small balanced monotone g:
compute G_2 = g(g,...,g) explicitly, compare B/I and min_i B_i/Inf_i with the recursion."""
import sys, os, itertools
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from feilib import *
from check_composition import compose, E

def monotone(tt, n):
    for x in range(1 << n):
        for i in range(n):
            if not (x >> i) & 1 and tt[x] == -1 and tt[x | (1 << i)] == 1:
                return False
    return True

# find balanced monotone g on 4 variables that is not odd (has nonzero even-level mass) and depends on all vars
n = 4; found = []
for code in range(1 << 16):
    tt = np.array([1 - 2 * ((code >> x) & 1) for x in range(16)], dtype=np.int8)
    if tt.sum() != 0 or not monotone(tt, n): continue
    fh = wht(tt[None, :].astype(float))[0]
    cq = coord_quantities(fh[None, :], n)
    if (cq["Inf"][0] < 1e-12).any(): continue
    even = sum(fh[s] ** 2 for s in range(16) if bin(s).count("1") % 2 == 0)
    if even > 1e-9 and cq["B"][0].sum() > 1e-9:
        found.append(tt)
print("candidates:", len(found))
g = found[0]
print("g =", g.tolist())
gh = wht(g[None, :].astype(float))[0]; p = gh ** 2
cg = coord_quantities(gh[None, :], n)
Inf = cg["Inf"][0]; Bg = cg["B"][0]
lvl1 = np.array([gh[1 << j] for j in range(n)])
# recursion prediction for G_2
S = np.arange(16)
def Xi(j, c2):
    lo = S[((S >> j) & 1) == 0]
    return float(E(p[lo], c2 * p[lo | (1 << j)]).sum())
ratios = []; Btot = 0.0
for j in range(n):
    for w in range(n):
        c2 = lvl1[w] ** 2
        Bw = Inf[j] * Bg[w] + Xi(j, c2)
        Iw = Inf[j] * Inf[w]
        ratios.append(Bw / Iw); Btot += Bw
I2 = cg["Inf"][0].sum() ** 2
print("recursion: B/I =", Btot / I2, " exist =", min(ratios))
# brute force
tt2, n2, offs, sizes = compose(g, n, [(g, n)] * n)
fh2 = wht(tt2[None, :].astype(float)); c2q = coord_quantities(fh2, n2)
r2 = c2q["B"][0] / c2q["Inf"][0]
print("brute   : B/I =", c2q["B"][0].sum() / c2q["Inf"][0].sum(), " exist =", r2.min(), " n2 =", n2)
