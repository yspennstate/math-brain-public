"""T357 Target 1 (linear-feature case): population calibration of logistic ridge along lambda, no binning.

Teacher P(y = 1 | x) = sigma(beta <w*, x>), x ~ N(0, I_d), |w*| = 1, n = alpha d. Fit min (1/n) sum log(1 + e^(-s_i x_i.w))
+ (lam/2)|w|^2 (s = 2y - 1). For any linear predictor zhat = w.x, (z*, zhat) is jointly Gaussian with var 1, q^2 = |w|^2,
cov c = w.w*, so the population calibration curve and risk are exact functions of (q, c):
  E[y | zhat = s] = E sigma(beta z*), z* | s ~ N((c/q^2) s, 1 - c^2/q^2).
Reported per lambda (medians over seeds): q, c, the calibration error CE = E|E[y|p] - p| (p = sigma(zhat)), its signed
overconfidence OC = E[(p - E[y|p]) sign(p - 1/2)] (> 0: over-confident), and the excess logistic risk over Bayes.
argv: d alpha beta seeds lam-list
"""
import sys, math
import numpy as np
from scipy.optimize import minimize

d = int(sys.argv[1]); alpha = float(sys.argv[2]); beta = float(sys.argv[3]); seeds = int(sys.argv[4])
lams = [float(v) for v in sys.argv[5].split(",")]
n = int(alpha * d)
gh_x, gh_w = np.polynomial.hermite_e.hermegauss(80)
gh_w = gh_w / gh_w.sum()
sig = lambda t: 0.5 * (1 + np.tanh(t / 2))
softplus = lambda t: np.logaddexp(0, t)

def pop(q, c):
    s = q * gh_x                                   # zhat values (weights gh_w)
    mu = (c / q ** 2) * s[:, None]; sd = math.sqrt(max(1 - c ** 2 / q ** 2, 0))
    zs = mu + sd * gh_x[None, :]
    ey = (sig(beta * zs) * gh_w[None, :]).sum(1)  # E[y | zhat = s]
    p = sig(s)
    ce = (np.abs(ey - p) * gh_w).sum()
    oc = ((p - ey) * np.sign(p - 0.5) * gh_w).sum()
    risk = ((ey * softplus(-s) + (1 - ey) * softplus(s)) * gh_w).sum()
    return ce, oc, risk

zb = gh_x
bayes = ((sig(beta * zb) * softplus(-beta * zb) + (1 - sig(beta * zb)) * softplus(beta * zb)) * gh_w).sum()

def fit(X, s, lam, w0):
    def f(w):
        m = s * (X @ w)
        return softplus(-m).mean() + 0.5 * lam * w @ w
    def g(w):
        m = s * (X @ w)
        return -(X.T @ (s * sig(-m))) / len(s) + lam * w
    r = minimize(f, w0, jac=g, method="L-BFGS-B", options={"maxiter": 5000, "gtol": 1e-10})
    return r.x

print(f"d={d} n={n} alpha={alpha} beta={beta} seeds={seeds} Bayes risk={bayes:.5f}")
print("lambda      q       c      CE       OC      excess risk")
rows = {lam: [] for lam in lams}
for sd in range(seeds):
    rng = np.random.default_rng(sd)
    X = rng.standard_normal((n, d))
    wstar = np.zeros(d); wstar[0] = 1.0
    y = rng.random(n) < sig(beta * X[:, 0])
    s = np.where(y, 1.0, -1.0)
    w = np.zeros(d)
    for lam in sorted(lams, reverse=True):         # warm start from large lambda down
        w = fit(X, s, lam, w)
        q = float(np.linalg.norm(w)); c = float(w @ wstar)
        ce, oc, risk = pop(q, c)
        rows[lam].append((q, c, ce, oc, risk - bayes))
for lam in lams:
    a = np.median(np.array(rows[lam]), axis=0)
    print(f"{lam:8.4g} {a[0]:7.3f} {a[1]:7.3f} {a[2]:7.4f} {a[3]:+8.4f} {a[4]:9.5f}", flush=True)
