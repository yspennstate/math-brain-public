"""Exhaustive sweep over all 65,536 Boolean functions of 4 variables (functions of fewer variables
appear with dummy coordinates).  Reproduces the published maxima and records candidate ratios."""
import sys, json, time
import numpy as np
sys.path.insert(0, __file__.rsplit("/", 1)[0] if "/" in __file__ else ".")
from feilib import *

set_polite()
n = 4
N = 1 << n
t0 = time.time()
codes = np.arange(1 << N, dtype=np.int64)
tt = (1 - 2 * ((codes[:, None] >> np.arange(N)[None, :]) & 1)).astype(np.float64)
fh, p = spectra(tt)
H = entropy(p)
I = total_influence(p, n)
cq = coord_quantities(fh, n)
Inf, eta, B, JS, Delta = cq["Inf"], cq["eta"], cq["B"], cq["JS"], cq["Delta"]
nc = I > 1e-12
res = {}
res["max_H_over_I"] = float((H[nc] / I[nc]).max())
Bt = B.sum(axis=1)
res["max_B_over_I"] = float((Bt[nc] / I[nc]).max())
# per-coordinate ratios over relevant coordinates
rel = Inf > 1e-12
with np.errstate(divide="ignore", invalid="ignore"):
    rB = np.where(rel, B / np.where(rel, Inf, 1), np.inf)
    rD = np.where(rel, Delta / np.where(rel, Inf, 1), np.inf)
res["max_i_B_i_over_Inf_i"] = float(np.where(rel, rB, -np.inf)[nc].max())
res["max_f_min_i_B_i_over_Inf_i (existential)"] = float(rB[nc].min(axis=1).max())
res["max_f_rho0 = min_i Delta_i/Inf_i"] = float(rD[nc].min(axis=1).max())
# checks of elementary inequalities
res["max JS - (2/ln2) eta"] = float((JS - 2 * LOG2E * eta).max())
res["max B - h2(eta)"] = float((B - h2(eta)).max())
res["max eta - Inf"] = float((eta - Inf).max())
# max-influence coordinate selector
imax = np.argmax(Inf, axis=1)
rsel = rB[np.arange(len(imax)), imax]
res["max_f B_{i*}/Inf_{i*}, i* = argmax Inf"] = float(rsel[nc].max())
# existential Hellinger selector: B_i <= K eta_i  (0/0 counted as 0)
with np.errstate(divide="ignore", invalid="ignore"):
    rBe = np.where(eta > 1e-14, B / np.where(eta > 1e-14, eta, 1), np.where(B > 1e-14, np.inf, 0.0))
rBe_rel = np.where(rel, rBe, np.inf)
res["max_f min_i B_i/eta_i (rel. coords)"] = float(rBe_rel[nc].min(axis=1).max())
M = eta.sum(axis=1)
with np.errstate(divide="ignore", invalid="ignore"):
    rBM = np.where(M > 1e-14, Bt / np.where(M > 1e-14, M, 1), np.where(Bt > 1e-14, np.inf, 0))
res["max B/M (M = sum eta)"] = float(rBM[nc].max())
res["seconds"] = time.time() - t0
print(json.dumps(res, indent=1))
k = int(np.argmax(np.where(nc, rB.min(axis=1), -1)))
print("existential argmax code", k, "tt", tt[k].astype(int).tolist(), "B", B[k], "Inf", Inf[k])
k = int(np.argmax(np.where(nc, rsel, -1)))
print("max-inf selector argmax code", k, "tt", tt[k].astype(int).tolist(), "B", B[k], "Inf", Inf[k])
