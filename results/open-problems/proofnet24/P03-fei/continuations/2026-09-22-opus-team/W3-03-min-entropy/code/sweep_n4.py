"""Exhaustive sweep over all Boolean functions of n <= 4 variables (65,536 at n = 4).

Reports max Hinf/I, max H2/I, max H/I, max (Hinf - c I) for several c, and the maximizers.
Exact check: for n <= 4 every coefficient is a multiple of 1/8, so maxsq is exact in floating point.
"""
import sys, json
import numpy as np
import psutil
_p = psutil.Process(); _p.nice(psutil.BELOW_NORMAL_PRIORITY_CLASS); _p.cpu_affinity([2, 3, 10, 11, 12, 13, 14, 15])
sys.path.insert(0, __file__.rsplit("/", 1)[0].rsplit("\\", 1)[0])
from fmei_lib import stats, bits_to_pm

out = {}
for n in range(1, 5):
    N = 1 << n
    masks = np.arange(1 << N, dtype=np.uint64)
    tt = bits_to_pm(masks, n)
    s = stats(tt)
    nc = s["I"] > 0
    Hinf, H2, H, I = s["Hinf"], s["H2"], s["H"], s["I"]
    r = np.where(nc, Hinf / np.where(nc, I, 1), -1)
    r2 = np.where(nc, H2 / np.where(nc, I, 1), -1)
    rH = np.where(nc, H / np.where(nc, I, 1), -1)
    bal = np.abs(s["mean"]) < 1e-12
    res = dict(n=n, count=int(len(masks)))
    k = int(np.argmax(r)); res["max_Hinf_over_I"] = [float(r[k]), int(masks[k]), float(Hinf[k]), float(I[k])]
    k = int(np.argmax(r2)); res["max_H2_over_I"] = [float(r2[k]), int(masks[k]), float(H2[k]), float(I[k])]
    k = int(np.argmax(rH)); res["max_H_over_I"] = [float(rH[k]), int(masks[k]), float(H[k]), float(I[k])]
    rb = np.where(bal & nc, r, -1); k = int(np.argmax(rb))
    res["max_Hinf_over_I_balanced"] = [float(rb[k]), int(masks[k]), float(Hinf[k]), float(I[k])]
    for c in (2.0, 2 / np.log(2), 4.0):
        d = np.where(nc, Hinf - c * I, -np.inf); k = int(np.argmax(d))
        res[f"max_Hinf_minus_{c:.4f}I"] = [float(d[k]), int(masks[k]), float(Hinf[k]), float(I[k])]
    # distribution of Hinf/I among nonconstant
    vals, cnts = np.unique(np.round(r[nc], 9), return_counts=True)
    top = sorted(zip(vals.tolist(), cnts.tolist()), reverse=True)[:8]
    res["top_ratio_values"] = top
    # check Hinf <= H2 <= 2 Hinf and Hinf <= H
    res["check_Hinf_le_H2_le_2Hinf"] = bool(np.all(Hinf[nc] <= H2[nc] + 1e-12) and np.all(H2[nc] <= 2 * Hinf[nc] + 1e-12))
    res["check_Hinf_le_H"] = bool(np.all(Hinf <= H + 1e-12))
    out[n] = res
    print(json.dumps(res))
