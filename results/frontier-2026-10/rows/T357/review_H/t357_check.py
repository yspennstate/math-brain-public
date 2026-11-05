"""T357 review, independent checks (agent H).

1. Size of the Thm B constants C_*, Lambda at beta = 1, gamma = 1, from the synthesis's own formulas (Sec. 4).
2. The first-update normalization (11): A_1 = c a^2 mu_beta and Q_1 - A_1^2 = c^2 tau^2, checked against a
   direct finite-d simulation of one GD step (1) with a fresh test sample. This does not use the package's code.
Output: t357_check.json beside this file.
"""
import json
import math
import os

import numpy as np
from scipy import integrate

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "t357_check.json")
phi = lambda u: math.exp(-u * u / 2) / math.sqrt(2 * math.pi)
sig = lambda u: 1 / (1 + math.exp(-u))


def gauss(f):
    return integrate.quad(lambda u: f(u) * phi(u), -12, 12, limit=400, epsabs=1e-13)[0]


res = {}
a = gauss(lambda u: u * math.tanh(u))
v = gauss(lambda u: math.tanh(u) ** 2)
nu = v - a * a
res["a"], res["v"], res["nu"] = a, v, nu

# 1. Thm B constants
for beta, gamma in [(1.0, 1.0), (0.5, 1.0), (1.0, 0.25)]:
    L = 8 * math.sqrt(1 + gamma)
    s0 = nu / 2
    k0 = math.sqrt(s0 / 2)
    p0 = s0 ** 2 / (20 * L ** 4)
    B0 = math.sqrt(2 * math.log(4 / p0))
    p1 = sig(-beta * B0) * p0 / 2
    Cstar = max(1.0, (32 * L / (k0 * p1)) ** 2)
    Lam = 16 * L * L
    res[f"thmB_beta{beta}_gamma{gamma}"] = {
        "L": L, "p0": p0, "p1": p1, "C_star": Cstar, "log10_C_star": math.log10(Cstar),
        "Lambda": Lam, "c_max": gamma / (2 * Lam),
    }

# 2. first-update normalization
beta, alpha, gamma, c = 1.0, 2.0, 1.0, 1.0
mu = gauss(lambda u: u * (sig(beta * u) - 0.5))
A1 = c * a * a * mu
tau2 = mu ** 2 * a * a * v / gamma + (a ** 4 + v * v / gamma) / (4 * alpha)
res["first_step_theory"] = {"beta": beta, "alpha": alpha, "gamma": gamma, "c": c, "mu_beta": mu,
                            "A1": A1, "Q1_minus_A1sq": c * c * tau2}

rng = np.random.default_rng(20261103)
sims = []
for d in (400, 800):
    n, m = int(alpha * d), int(gamma * d)
    rows = []
    for rep in range(4):
        theta = np.zeros(d); theta[0] = 1.0
        X = rng.standard_normal((n, d))
        W = rng.standard_normal((m, d)) / math.sqrt(d)
        Y = (rng.random(n) < 1 / (1 + np.exp(-beta * X[:, 0]))).astype(float)
        H = np.tanh(X @ W.T)
        b1 = c * d / (n * m) * H.T @ (Y - 0.5)
        Xt = rng.standard_normal((40000, d))
        S = np.tanh(Xt @ W.T) @ b1
        Z = Xt[:, 0]
        A = float(np.mean(Z * S)); Q = float(np.mean(S * S))
        rows.append((A, Q - A * A))
    arr = np.array(rows)
    sims.append({"d": d, "n": n, "m": m, "reps": 4, "A1_mean": float(arr[:, 0].mean()), "A1_sd": float(arr[:, 0].std()),
                 "Q1mA1sq_mean": float(arr[:, 1].mean()), "Q1mA1sq_sd": float(arr[:, 1].std())})
res["first_step_sim"] = sims
json.dump(res, open(OUT, "w"), indent=1)
print(json.dumps(res, indent=1))
