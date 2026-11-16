"""Is C_5 a local maximum of the margin ratio sum g Q / sum g P on the double-top stratum (n = 5)?
Perturb the C_5 weights (z = sqrt w; chords start at 0 and move one-sidedly), pull the point back onto the stratum by
minimising |z - z_pert|^2 + K relgap^2 (relgap = (lambda_1 - lambda_2)/lambda_1), keep points with relgap < 1e-7, and
print the ratio against the distance |w - w_C5|_1 from C_5. usage: python t104_c5_local.py seed
"""
import sys
import numpy as np
from scipy.optimize import minimize

SEED = int(sys.argv[1]); n = 5
here = __file__.replace("t104_c5_local.py", "t104_circulant_ratio.py")
src = open(here, encoding="utf-8").read().split("\nhalf = ")[0]
sys.argv = ["t104_circulant_ratio.py", str(n), "0"]
g = {"__file__": here, "__name__": "cr_mod"}
exec(compile(src, here, "exec"), g)
ratio, circ, Bs, h = g["ratio"], g["circ"], g["Bs"], g["h"]

w0 = circ(np.array([1.0, 0.0])); w0 /= w0.sum()
lam0, D0, r0 = ratio(w0)
print("C_5  lambda %.6f  D %d  ratio %.6f" % (lam0, D0, r0), flush=True)


def relgap(z):
    w = z ** 2; w = w / w.sum()
    ev = np.linalg.eigvalsh(Bs.T @ np.diag(w) @ Bs)
    return (ev[-1] - ev[-2]) / ev[-1]


rng = np.random.default_rng(SEED)
rows = []
for eps in (0.01, 0.03, 0.1, 0.2):
    worst = -9.0
    for t in range(25):
        zp = np.sqrt(w0) + eps * rng.standard_normal(h.m) * np.where(w0 > 0, 1.0, 0.0) \
             + eps * np.abs(rng.standard_normal(h.m)) * np.where(w0 > 0, 0.0, 1.0)
        f = lambda z: np.sum((z - zp) ** 2) + 1e4 * relgap(z) ** 2
        r = minimize(f, zp, method="Nelder-Mead", options={"xatol": 1e-12, "fatol": 1e-16, "maxiter": 40000})
        z = r.x
        for _ in range(3):
            if relgap(z) < 1e-7:
                break
            z = minimize(relgap, z, method="Nelder-Mead", options={"xatol": 1e-13, "fatol": 1e-15, "maxiter": 20000}).x
        if relgap(z) > 1e-7:
            continue
        w = z ** 2; w /= w.sum()
        lam, D, rr = ratio(w)
        if D != 2:
            continue
        dist = np.abs(w - w0).sum()
        rows.append((eps, dist, rr)); worst = max(worst, rr)
    sel = [x for x in rows if x[0] == eps]
    print("eps %.2f  kept %2d  dist %.4f..%.4f  ratio max %.6f  min %.6f  above C_5: %d"
          % (eps, len(sel), min(x[1] for x in sel), max(x[1] for x in sel), max(x[2] for x in sel),
             min(x[2] for x in sel), sum(x[2] > r0 + 1e-9 for x in sel)), flush=True)
best = max(rows, key=lambda x: x[2])
print("largest ratio %.6f at distance %.4f (C_5 %.6f)" % (best[2], best[1], r0), flush=True)
