"""Does R >= lambda hold off the double-top stratum too? For a weighted graph with simple top eigenvalue lambda, R is the
gap-weighted Rayleigh average of M over the V_[n-2,2] parts of sym(u_top (x) e_l), the beta -> infinity weights in
s_beta (t104_sinf_stratum.py with Top = the top vector alone). Samples the search's start families plus uniform random
weights, prints the smallest R - lambda, the smallest R / lambda, and the graphs where they occur.
usage: python t104_R_vs_lambda.py n samples seed
"""
import sys
import numpy as np

n, NS, SEED = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
here = __file__.replace("t104_R_vs_lambda.py", "t104_sinf_stratum.py")
src = open(here, encoding="utf-8").read().split("\nrng = np.random")[0]
sys.argv = ["t104_sinf_stratum.py", str(n), "0", "0"]
g = {"__file__": here, "__name__": "sinf_mod"}
exec(compile(src, here, "exec"), g)
h, sinf = g["h"], g["sinf"]

rng = np.random.default_rng(SEED)
rows = []
for t in range(NS):
    if t % 2:
        w = h.starts(h.NK, rng)[t % h.NK] + 1e-9
    else:
        w = rng.random(h.m) ** rng.integers(1, 6) * (rng.random(h.m) < rng.uniform(0.3, 1.0)) + 1e-9
    w = w / w.sum()
    s, mult, lam, R = sinf(w, tol=1e-12)
    rows.append((R - lam, R / lam, lam, w))
d = np.array([r[0] for r in rows]); q = np.array([r[1] for r in rows])
print("n %d  samples %d  R - lambda: min %+.6f  median %+.6f   R / lambda: min %.6f  median %.6f  negative %d"
      % (n, NS, np.nanmin(d), np.nanmedian(d), np.nanmin(q), np.nanmedian(q), int((d < -1e-12).sum())), flush=True)
for name, key in (("min R-lam", d), ("min R/lam", q)):
    for i in np.argsort(np.nan_to_num(key, nan=np.inf))[:3]:
        print("  %s %+.6f  R/lam %.6f  lam %.6f  %s" % (name, rows[i][0], rows[i][1], rows[i][2], h.fmt(rows[i][3], 1e-4)),
              flush=True)
