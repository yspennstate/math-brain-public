"""Reproducible checks for agent 003. No empirical check is used as proof."""
import json
import math
from fractions import Fraction

import numpy as np


def harmonic_dimension(d, s):
    return math.comb(d + s - 1, s) - (math.comb(d + s - 3, s - 2) if s >= 2 else 0)


checks = 0
for d in range(3, 15):
    for s in range(0, 20):
        lhs = Fraction(harmonic_dimension(d, s + 1), harmonic_dimension(d, s))
        rhs = Fraction((2 * s + d) * (d + s - 2), (s + 1) * (2 * s + d - 2))
        assert lhs == rhs
        # Multiplicity times the exact Mercer ratio upper bound.
        trace_ratio_bound = lhs / (d + 2 * s)
        assert trace_ratio_bound == Fraction(d + s - 2, (s + 1) * (d + 2 * s - 2))
        assert trace_ratio_bound <= Fraction(1, s + 1)
        checks += 1

phase_rows = []
for ell in range(2, 10):
    R = 2**ell
    d = 2**R
    n = 2**(R * R)
    k = R + ell - 1
    Nk = harmonic_dimension(d, k)
    D = sum(harmonic_dimension(d, s) for s in range(k))
    # Logarithms of exact integer dimensions; floating output is diagnostic.
    ln_d = R * math.log(2)
    exp_high = (math.log(Nk) - math.log(n)) / ln_d
    exp_low = (math.log(D) - math.log(n)) / ln_d
    # h=1, gamma=1 exact upper bound on tau/(n lambda_{k-1}).
    shrink = Fraction(Nk, n * (d + 2 * k - 2)) / (1 - Fraction(1, k + 1))
    exp_shrink = (math.log(shrink.numerator) - math.log(shrink.denominator)) / ln_d
    phase_rows.append(dict(ell=ell, R=R, k=k,
                           log_d_Nk_over_n=exp_high,
                           log_d_D_over_n=exp_low,
                           log_d_shrink_upper=exp_shrink))

# Finite deterministic transfer sanity check, using the worst allowed covariance H_T=lambda_k T.
rng = np.random.default_rng(3003)
n, D, Nk = 40, 7, 200
tau = 0.03
lam_k = tau / Nk
psi_frame, _ = np.linalg.qr(rng.normal(size=(n, D)))
Psi = psi_frame * math.sqrt(n)
w_frame, _ = np.linalg.qr(rng.normal(size=(n, n)))
W = (w_frame * np.linspace(2 / 3, 2, n)) @ w_frame.T
low_eigs = np.geomspace(0.001, 0.2, D)
penalty = np.diag(tau / low_eigs)
G = penalty + Psi.T @ W @ Psi
Ginv = np.linalg.inv(G)
L = Ginv @ Psi.T @ W
Q = np.eye(n) - Psi @ L
E = -Ginv @ penalty
a = tau / (n * low_eigs.min())
b = n * lam_k / tau
signal_risk_matrix = E.T @ E + (lam_k / tau) * E.T @ Psi.T @ W @ Psi @ E
signal_norm2 = np.linalg.eigvalsh(signal_risk_matrix).max()
signal_bound = 9 * a * a * (1 + 3 * b)
noise_trace = np.trace(L @ L.T) + (lam_k / tau) * np.trace(Q.T @ W @ Q)
noise_bound = 6 * D / n + 2 * b
weighted_contraction_defect = np.linalg.eigvalsh(Q.T @ W @ Q - W).max()
assert signal_norm2 <= signal_bound + 1e-10
assert noise_trace <= noise_bound + 1e-10
assert weighted_contraction_defect < 1e-10

print(json.dumps({
    "exact_multiplicity_and_trace_ratio_checks": checks,
    "delta_star": 1 / math.log(2) - 1,
    "phase_diagnostics": phase_rows,
    "deterministic_transfer_sanity_check": {
        "signal_operator_norm_squared": float(signal_norm2),
        "signal_upper_bound": float(signal_bound),
        "noise_risk_trace": float(noise_trace),
        "noise_upper_bound": float(noise_bound),
        "max_eigenvalue_QtWQ_minus_W": float(weighted_contraction_defect),
    },
    "limitations": "Numerics do not prove concentration, growing-dimension limits, or hard-edge universality."
}, indent=2))
