"""Direct check of cgmt_ridge.py: fit logistic ridge at d (alpha 3, beta 2, lam 0.110806), report q = |w| and rho = w.w*/|w|
over seeds; CGMT predicts q = 1.19180, rho = 0.765061. argv: d seeds"""
import sys, math, numpy as np
from scipy.optimize import minimize
d = int(sys.argv[1]); seeds = int(sys.argv[2]); alpha, beta, lam = 3.0, 2.0, 0.110806
sig = lambda t: 0.5 * (1 + np.tanh(0.5 * t)); n = int(alpha * d)
for sd in range(seeds):
    rng = np.random.default_rng(100 + sd)
    X = rng.standard_normal((n, d)); s = np.where(rng.random(n) < sig(beta * X[:, 0]), 1.0, -1.0)
    f = lambda w: np.logaddexp(0, -s * (X @ w)).mean() + 0.5 * lam * w @ w
    g = lambda w: -(X.T @ (s * sig(-s * (X @ w)))) / n + lam * w
    w = minimize(f, np.zeros(d), jac=g, method="L-BFGS-B", options={"maxiter": 5000, "gtol": 1e-10}).x
    q = float(np.linalg.norm(w)); print(f"d={d} seed={sd}: q={q:.4f} rho={w[0]/q:.4f}", flush=True)
