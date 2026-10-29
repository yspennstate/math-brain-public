"""Finite-N online SGD for the K=M=2 erf soft committee (noiseless, output weights 1): specialization time against log N.
Prediction from the ODE (scm_plateau.py, eta 0.5): lambda = 0.0316182, slope of tau_N in log N = 1/(2 lambda) = 15.81.
Usage: python -X utf8 scm_sgd_escape.py [eta] [runs] [N ...]   (runs are batched; BelowNormal priority)"""
import sys
import time
import numpy as np
from scipy.special import erf

try:
    import psutil
    psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception:
    pass

eta = float(sys.argv[1]) if len(sys.argv) > 1 else 0.5
runs = int(sys.argv[2]) if len(sys.argv) > 2 else 20
Ns = [int(a) for a in sys.argv[3:]] or [500, 1000, 2000, 4000]
q0, delta, tmax = 0.2, 0.2, 2000.0
c = np.sqrt(2 / np.pi)
rng = np.random.default_rng(20261016)
res = {}
for N in Ns:
    t0 = time.time()
    W = rng.standard_normal((runs, 2, N))
    W *= np.sqrt(N * q0) / np.linalg.norm(W, axis=2, keepdims=True)
    tau = np.full(runs, np.nan)
    steps = int(tmax * N)
    for s in range(steps):
        x = rng.standard_normal((runs, N))
        h = np.einsum("rkn,rn->rk", W, x) / np.sqrt(N)
        y = erf(x[:, 0] / np.sqrt(2)) + erf(x[:, 1] / np.sqrt(2))
        err = y - erf(h / np.sqrt(2)).sum(1)
        dlt = c * np.exp(-h * h / 2) * err[:, None]
        W += (eta / np.sqrt(N)) * dlt[:, :, None] * x[:, None, :]
        if s % (N // 10) == 0:
            R = W[:, :, :2] / np.sqrt(N)
            gap = np.abs(R[:, 0, 0] - R[:, 0, 1])
            new = np.isnan(tau) & (gap > delta)
            tau[new] = s / N
            if not np.isnan(tau).any():
                break
    res[N] = tau
    print("N %5d: tau median %.1f, mean %.1f, sd %.1f, unescaped %d/%d (%.0f s)"
          % (N, np.nanmedian(tau), np.nanmean(tau), np.nanstd(tau), np.isnan(tau).sum(), runs, time.time() - t0), flush=True)
L = np.array([np.log(N) for N in Ns])
m = np.array([np.nanmean(res[N]) for N in Ns])
slope, icpt = np.polyfit(L, m, 1)
print("fit mean tau = %.2f * log N + %.1f   (ODE prediction for the slope: %.2f)" % (slope, icpt, 1 / (2 * 0.0316182)))
