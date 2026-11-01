"""Numerical reproduction for the B14 scalar erasure-frontier theorem.

The proof in REPORT.md is analytic.  This script only reproduces the Hod-scale
numbers and tries to refute the claimed convex frontier by a discretized linear
program over fibre parameters q in (0,1).
"""

import math
import numpy as np
import mpmath as mp
from scipy.optimize import linprog

mp.mp.dps = 60
LN2 = mp.log(2)


def h(q):
    q = mp.mpf(q)
    if q == 0 or q == 1:
        return mp.mpf("0")
    return -(q * mp.log(q) + (1 - q) * mp.log(1 - q)) / LN2


def j(q):
    q = mp.mpf(q)
    if q == 0 or q == 1:
        return mp.mpf("0")
    s = mp.sqrt(q * (1 - q))
    return 1 - h(mp.mpf("0.5") + s)


def psi(q):
    return h(q) + j(q)


def kappa(q):
    return psi(q) / q


def beta(q):
    return h(q) / q


def hf(q):
    if q <= 0.0 or q >= 1.0:
        return 0.0
    return -q * math.log2(q) - (1.0 - q) * math.log2(1.0 - q)


def psif(q):
    if q <= 0.0 or q >= 1.0:
        return 0.0
    return hf(q) + 1.0 - hf(0.5 + math.sqrt(q * (1.0 - q)))


def kappaf(q):
    return psif(q) / q


def betaf(q):
    return hf(q) / q


r = mp.mpf("6.4547837")
tau = mp.findroot(lambda z: kappa(z) - r, (mp.mpf("0.17"), mp.mpf("0.19")))
lam = mp.diff(beta, tau) / mp.diff(kappa, tau)
d = lam * r - beta(tau)
c = 2 / LN2

print("r", mp.nstr(r, 24))
print("tau", mp.nstr(tau, 24))
print("beta(tau)", mp.nstr(beta(tau), 24))
print("tangent_lambda", mp.nstr(lam, 24))
print("tangent_d", mp.nstr(d, 24))
print("old_r_minus_2_over_ln2", mp.nstr(r - c, 24))
print("gain", mp.nstr(beta(tau) - (r - c), 24))
print("DTC_coefficient_r_minus_beta", mp.nstr(r - beta(tau), 24))
print("DTC_over_H", mp.nstr((r - beta(tau)) / r, 24))

# Refutation attempt: minimize E beta(Q) subject to E kappa(Q) >= r.
# If a two-point or q>1/2 mixture beat beta(tau), this LP should expose it
# on the grid.  This is a diagnostic only, not the proof.
qs = np.unique(
    np.concatenate(
        [
            np.logspace(-8, -2, 700),
            np.linspace(0.01, 0.4999, 1800),
            np.linspace(0.5001, 0.999999, 900),
            np.array([float(tau)]),
        ]
    )
)
obj = np.array([betaf(q) for q in qs])
kvec = np.array([kappaf(q) for q in qs])
res = linprog(
    obj,
    A_ub=np.array([-kvec]),
    b_ub=np.array([-float(r)]),
    A_eq=np.ones((1, len(qs))),
    b_eq=np.array([1.0]),
    bounds=(0, None),
    method="highs",
)
print("lp_success", res.success)
print("lp_objective", repr(float(res.fun)))
print("lp_mean_kappa", repr(float(kvec @ res.x)))
print("lp_gap_from_beta_tau", repr(float(res.fun - float(beta(tau)))))
for idx in np.where(res.x > 1e-7)[0]:
    print(
        "lp_support",
        repr(float(qs[idx])),
        repr(float(res.x[idx])),
        repr(float(kvec[idx])),
        repr(float(obj[idx])),
    )
