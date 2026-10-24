"""At a saved fixed point V, list the best balanced (r = 1/2) configurations of every g-family, and the best AND splits.
Usage: python inspect_center.py <vig npz> [families] [npar]
"""
import sys
import numpy as np
from ro_gamma import Grid
from vi_g import FAMILIES, build_family, h2
from ro_gamma_nb import psi_s

d = np.load(sys.argv[1])
C = float(d["C"]); G = d["G"]; grid = Grid(int(d["M"]), int(d["K"]))
names = sys.argv[2].split(",") if len(sys.argv) > 2 else list(FAMILIES)
npar = int(sys.argv[3]) if len(sys.argv) > 3 else 256
gam = lambda q: grid.gamma_at(G, q)
print("C = %.15f, V(1/2) - C = %+.3e" % (C, gam(np.array([0.5]))[0] - C))
free_grid = np.arange(1, npar) / npar
rnodes = np.array([0.5])
for nm in names:
    K, j = FAMILIES[nm]
    fam = build_family(K, j, rnodes, free_grid)
    if len(fam["r_idx"]) == 0:
        print("%-4s: no balanced configs" % nm); continue
    p = fam["p"]; V = 4 * p * (1 - p)
    s = (fam["It"] / V * (gam(p) + h2(V))).sum(axis=1) + C * fam["Irest"] - fam["Ht"]
    o = np.argsort(s)
    # skip the trivial all-1/2 config
    print("%-4s K=%s  best balanced s - C:" % (nm, K))
    shown = 0
    for q in o:
        if np.all(np.abs(p[q] - 0.5) < 1e-12):
            continue
        print("    p=%s  s-C=%+.4e" % (np.array2string(p[q], precision=5), s[q] - C))
        shown += 1
        if shown >= 3:
            break
# AND split at 1/2: V(1/2) <= q (V(p)+h(V_p)) + p (V(q)+h(V_q)) - Ht_AND(p,q), pq = 1/2
from ro_gamma import psi, E_fun
ps = np.linspace(0.5005, 0.9995, 4000)
qs = 0.5 / ps
ok = qs < 1
ps, qs = ps[ok], qs[ok]
Lp = np.log2(1 / ps); Lq = np.log2(1 / qs)
val = qs * gam(ps) + ps * gam(qs) - ps * qs * E_fun(ps, qs, Lp, Lq)
k = np.argmin(val)
print("best AND split at 1/2: p=%.5f q=%.5f  value - C = %+.4e" % (ps[k], qs[k], val[k] - C))
