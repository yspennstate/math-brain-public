"""T357 Target 1, random-feature case: logistic ridge on N tanh features phi(Fx)/sqrt? (F rows N(0, I/d)), same teacher as
calib_path.py. Along a 33-point lambda grid (warm starts) the population (z*, zhat) moments q^2 = E zhat^2, c = E zhat z* are
estimated on 200k fresh points and fed to the Gaussian-equivalence formula of calib_path.py (CE, OC, excess risk); the same fresh
points give a binned CE/OC (40 quantile bins) as the check on Gaussian equivalence. Reports lam_cal (OC sign change) and lam_risk
(argmin of the binned-free GE risk and of the direct test risk).
argv: d alpha(n/d) psi(N/d) beta seeds
"""
import sys, math
import numpy as np
from scipy.optimize import minimize
d = int(sys.argv[1]); alpha = float(sys.argv[2]); psi = float(sys.argv[3]); beta = float(sys.argv[4]); seeds = int(sys.argv[5])
n = int(alpha * d); N = int(psi * d); nt = int(min(200000, 3e7 / N))
gh_x, gh_w = np.polynomial.hermite_e.hermegauss(80); gh_w = gh_w / gh_w.sum()
sig = lambda t: 0.5 * (1 + np.tanh(t / 2)); sp = lambda t: np.logaddexp(0, t)
bayes = ((sig(beta * gh_x) * sp(-beta * gh_x) + (1 - sig(beta * gh_x)) * sp(beta * gh_x)) * gh_w).sum()
def pop(q, c):
    s = q * gh_x; mu = (c / q ** 2) * s[:, None]; sd = math.sqrt(max(1 - c ** 2 / q ** 2, 0))
    ey = (sig(beta * (mu + sd * gh_x[None, :])) * gh_w[None, :]).sum(1); p = sig(s)
    return (np.abs(ey - p) * gh_w).sum(), ((p - ey) * np.sign(p - .5) * gh_w).sum(), ((ey * sp(-s) + (1 - ey) * sp(s)) * gh_w).sum() - bayes
def binned(zh, ey):
    o = np.argsort(zh); B = np.array_split(o, 40); ce = oc = 0.0
    for b in B:
        p = sig(zh[b]).mean(); e = ey[b].mean(); ce += abs(p - e) * len(b); oc += (p - e) * np.sign(p - .5) * len(b)
    return ce / len(zh), oc / len(zh)
def fit(Phi, s, lam, a0):
    f = lambda a: sp(-s * (Phi @ a)).mean() + .5 * lam * a @ a
    g = lambda a: -(Phi.T @ (s * sig(-s * (Phi @ a)))) / len(s) + lam * a
    return minimize(f, a0, jac=g, method="L-BFGS-B", options={"maxiter": 5000, "gtol": 1e-10}).x
grid = np.exp(np.linspace(math.log(10), math.log(1e-4), 33))
allr = []
for sd in range(seeds):
    rng = np.random.default_rng(100 + sd)
    F = rng.standard_normal((N, d)) / math.sqrt(d)
    X = rng.standard_normal((n, d)); s = np.where(rng.random(n) < sig(beta * X[:, 0]), 1., -1.)
    Phi = np.tanh(X @ F.T); Xt = rng.standard_normal((nt, d)); Pt = np.tanh(Xt @ F.T); zt = Xt[:, 0]; eyt = sig(beta * zt)
    a = np.zeros(N); res = []
    for lam in grid:
        a = fit(Phi, s, lam, a); zh = Pt @ a
        q = math.sqrt((zh ** 2).mean()); c = (zh * zt).mean()
        ce, oc, ex = pop(q, c); bce, boc = binned(zh, eyt)
        tr = (eyt * sp(-zh) + (1 - eyt) * sp(zh)).mean() - bayes
        res.append((lam, q, c, ce, oc, ex, bce, boc, tr))
    allr.append(np.array(res))
A = np.median(np.array(allr), axis=0)
print(f"d={d} n={n} N={N} beta={beta} seeds={seeds}")
print("   lambda     q      c     CE_GE    OC_GE   excess_GE  CE_bin   OC_bin  excess_test")
for r in A[::2]:
    print(f"{r[0]:9.4g} {r[1]:6.3f} {r[2]:6.3f} {r[3]:7.4f} {r[4]:+8.4f} {r[5]:9.5f} {r[6]:7.4f} {r[7]:+8.4f} {r[8]:9.5f}")
def cross(res, col):
    o = res[:, col]; i = np.where(np.sign(o[:-1]) != np.sign(o[1:]))[0]
    if not len(i): return float("nan")
    i = i[0]; l0, l1 = math.log(res[i, 0]), math.log(res[i + 1, 0]); return math.exp(l0 + (l1 - l0) * o[i] / (o[i] - o[i + 1]))
def argm(res, col):
    j = min(max(int(np.argmin(res[:, col])), 1), len(res) - 2); xs = np.log(res[j-1:j+2, 0]); P = np.polyfit(xs, res[j-1:j+2, col], 2)
    return math.exp(-P[1] / (2 * P[0])) if P[0] > 0 else res[j, 0]
lc = [cross(r, 4) for r in allr]; lcb = [cross(r, 7) for r in allr]; lr = [argm(r, 8) for r in allr]
print("lam_cal GE  per seed:", ", ".join(f"{x:.4g}" for x in lc))
print("lam_cal bin per seed:", ", ".join(f"{x:.4g}" for x in lcb))
print("lam_risk    per seed:", ", ".join(f"{x:.4g}" for x in lr))
print("ratio cal/risk (GE):", ", ".join(f"{a/b:.3f}" for a, b in zip(lc, lr)), flush=True)
