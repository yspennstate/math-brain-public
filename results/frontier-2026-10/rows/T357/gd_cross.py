"""T357: gradient descent (early stopping) against the ridge path, for calibration. Same teacher and exact (q, c) formulas as
calib_path.py. GD on the unregularized logistic loss from w = 0, step eta = 1 (below 2/L: L <= (1 + 1/sqrt(alpha))^2/4), sampled
at log-spaced steps up to T. Per seed: t_cal (OC sign change), t_risk (argmin excess risk), excess at t_cal, CE at t_risk; and the
GD path against ridge at matched norm q, where c_GD(q) - c_ridge(q) and OC_GD(q) - OC_ridge(q) are interpolated on q.
argv: d alpha beta seeds T
"""
import sys, math
import numpy as np
T = int(sys.argv[5])
import os
ETA = float(os.environ.get("ETA", "1"))      # step; times below are printed as steps * ETA
sys.argv = sys.argv[:1] + sys.argv[1:5] + ["1"]
exec(open("calib_path.py", encoding="utf-8").read().split('print(f"d={d}')[0])
ts = sorted(set(np.unique(np.round(np.exp(np.linspace(0, math.log(T), 120))).astype(int))))
lgrid = np.exp(np.linspace(math.log(30), math.log(1e-4), 49))
out = []
for sd in range(seeds):
    rng = np.random.default_rng(sd)
    X = rng.standard_normal((n, d)); wstar = np.zeros(d); wstar[0] = 1.0
    s = np.where(rng.random(n) < sig(beta * X[:, 0]), 1.0, -1.0)
    w = np.zeros(d); gd = []; k = 0
    for t in ts:
        while k < t:
            m = s * (X @ w); w = w + ETA * (X.T @ (s * sig(-m))) / n; k += 1
        q = float(np.linalg.norm(w)); c = float(w @ wstar); ce, oc, r = pop(q, c); gd.append((t, q, c, ce, oc, r - bayes))
    gd = np.array(gd)
    w = np.zeros(d); rd = []
    for lam in lgrid:
        w = fit(X, s, lam, w); q = float(np.linalg.norm(w)); c = float(w @ wstar); ce, oc, r = pop(q, c); rd.append((lam, q, c, ce, oc, r - bayes))
    rd = np.array(rd)                                            # q increasing along lgrid (lam decreasing)
    oc = gd[:, 4]; i = np.where((oc[:-1] < 0) & (oc[1:] >= 0))[0]
    if len(i):
        i = i[0]; f = -oc[i] / (oc[i + 1] - oc[i]); tcal = gd[i, 0] + f * (gd[i + 1, 0] - gd[i, 0]); excal = gd[i, 5] + f * (gd[i + 1, 5] - gd[i, 5]); qcal = gd[i, 1] + f * (gd[i + 1, 1] - gd[i, 1])
    else:
        tcal = excal = qcal = float("nan")
    j = int(np.argmin(gd[:, 5]))
    o2 = rd[:, 4]; i2 = np.where(np.sign(o2[:-1]) != np.sign(o2[1:]))[0][0]; f2 = o2[i2] / (o2[i2] - o2[i2 + 1])
    qcal_r = rd[i2, 1] + f2 * (rd[i2 + 1, 1] - rd[i2, 1]); ex_r = rd[:, 5].min()
    qq = np.linspace(max(gd[1, 1], rd[0, 1]), min(gd[-1, 1], rd[-1, 1]), 50)
    dc = np.interp(qq, gd[:, 1], gd[:, 2]) - np.interp(qq, rd[:, 1], rd[:, 2])
    out.append((tcal, gd[j, 0], excal, gd[j, 5], gd[j, 3], qcal, gd[j, 1], qcal_r, ex_r, np.abs(dc).max(), gd[-1, 4]))
o = np.array(out); med = np.nanmedian(o, axis=0)
print(f"alpha={alpha} beta={beta} d={d} seeds={seeds} T={T}: eta={ETA} GD time_cal={med[0]*ETA:.4g} time_risk={med[1]*ETA:.4g} ratio={med[0]/med[1]:.3f} | "
      f"GD excess at t_cal={med[2]:.5f} GD min excess={med[3]:.5f} CE at t_risk={med[4]:.4f} | q_cal GD={med[5]:.3f} q at t_risk={med[6]:.3f} "
      f"q_cal ridge={med[7]:.3f} | ridge min excess={med[8]:.5f} | max |c_GD - c_ridge| at matched q={med[9]:.4f} | OC at t=T {med[10]:+.4f}", flush=True)
