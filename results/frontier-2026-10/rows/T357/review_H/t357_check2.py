"""T357 review, check 2 (agent H).

1. How weak the teacher must be in the common-regime corollary: beta < log(3)/B0 and
   a^2 alpha gamma beta^2 / v^2 < gamma/(64 L^2), with alpha just above C_0 (gamma = 1).
2. Thm C at a point outside the corollary (beta = 1, alpha = 2, gamma = 1): first-step score
   S = c (k Z + tau G), k = a^2 mu_beta, label P(Y=1|Z) = sigma(beta Z). Find the risk-optimal c_*
   by quadrature, then compute signed overconfidence OC = E[max(p,1-p)] - P(correct) at c_*,
   and the exact calibration error CE = E|E[Y|S] - sigma(S)|.
Output: t357_check2.json beside this file.
"""
import json
import math
import os

import numpy as np
from scipy import integrate, optimize

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "t357_check2.json")
phi = lambda u: math.exp(-u * u / 2) / math.sqrt(2 * math.pi)
sig = lambda u: 1 / (1 + math.exp(-u)) if u > -700 else 0.0


def gauss(f):
    return integrate.quad(lambda u: f(u) * phi(u), -12, 12, limit=400, epsabs=1e-13)[0]


res = {}
a = gauss(lambda u: u * math.tanh(u))
v = gauss(lambda u: math.tanh(u) ** 2)
nu = v - a * a

# 1. common regime size (gamma = 1)
gamma = 1.0
L = 8 * math.sqrt(1 + gamma)
s0 = nu / 2
k0 = math.sqrt(s0 / 2)
p0 = s0 ** 2 / (20 * L ** 4)
B0 = math.sqrt(2 * math.log(4 / p0))
C0 = (32 * L / (k0 * p0 / 8)) ** 2  # p1 > p0/8 under beta < log(3)/B0
alpha = 2 * C0
beta_max1 = math.log(3) / B0
beta_max2 = math.sqrt(v * v / (64 * L * L * a * a * alpha))
res["common_regime"] = {"gamma": gamma, "B0": B0, "C0_conservative": C0, "alpha_used": alpha,
                        "beta_max_from_log3_over_B0": beta_max1, "beta_max_from_step": beta_max2,
                        "beta_max": min(beta_max1, beta_max2)}

# 2. Thm C at beta = 1, alpha = 2, gamma = 1
beta, alpha = 1.0, 2.0
mu = gauss(lambda u: u * (sig(beta * u) - 0.5))
k = a * a * mu
tau2 = mu ** 2 * a * a * v / gamma + (a ** 4 + v * v / gamma) / (4 * alpha)
sd = math.sqrt(k * k + tau2)

# Gauss-Hermite grid over (Z, G)
x, w = np.polynomial.hermite_e.hermegauss(120)
w = w / w.sum()
Z, G = np.meshgrid(x, x, indexing="ij")
W = np.outer(w, w)
pY = 1 / (1 + np.exp(-beta * Z))
U = k * Z + math.sqrt(tau2) * G  # score per unit c


def risk(c):
    S = c * U
    return float(np.sum(W * (np.logaddexp(0, S) - pY * S)))


opt = optimize.minimize_scalar(risk, bounds=(1e-6, 200), method="bounded", options={"xatol": 1e-10})
cs = opt.x


def stats(c):
    S = c * U
    p = 1 / (1 + np.exp(-S))
    conf = np.maximum(p, 1 - p)
    correct = np.where(S >= 0, pY, 1 - pY)
    oc = float(np.sum(W * (conf - correct)))
    # E[Y | U = u]: U ~ N(0, sd^2), Z | U ~ N(k u / sd^2, tau2 / sd^2)
    ug, uw = np.polynomial.hermite_e.hermegauss(200)
    uw = uw / uw.sum()
    ce = 0.0
    for ui, wi in zip(ug * sd, uw):
        m = k * ui / sd ** 2
        s = math.sqrt(tau2) / sd
        ey = float(np.sum(w / (1 + np.exp(-beta * (m + s * x)))))
        ce += wi * abs(ey - sig(c * ui))
    return oc, ce


oc_s, ce_s = stats(cs)
res["thmC_beta1_alpha2_gamma1"] = {"k": k, "tau2": tau2, "c_star": cs, "risk_c_star": risk(cs),
                                   "risk_0": math.log(2), "OC_at_c_star": oc_s, "CE_at_c_star": ce_s,
                                   "bracket_lo_4gprime0": None, "bracket_hi_beta_k_over_var": beta * k / (k * k + tau2)}
for c in (0.5 * cs, 2 * cs):
    o, e = stats(c)
    res["thmC_beta1_alpha2_gamma1"][f"OC_CE_at_{c / cs:.1f}c_star"] = [o, e]
json.dump(res, open(OUT, "w"), indent=1)
print(json.dumps(res, indent=1))
