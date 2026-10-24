import math
import json
import numpy as np


def schur0(A):
    a = A[0, 0]
    b = A[1:, 0]
    C = A[1:, 1:]
    return C - np.outer(b, b) / a


def opnorm(A):
    return np.linalg.norm(A, 2)


rng = np.random.default_rng(20260922)
max_rank_excess = 0
max_tail_ratio = 0.0
rank_trials = 0
tail_trials = 0

for n in [4, 5, 7, 9]:
    for r in [1, 2, 3]:
        if r >= n:
            continue
        for _ in range(40):
            M = rng.normal(size=(n, n))
            A0 = (M + M.T) / 2
            if abs(A0[0, 0]) < 1:
                A0[0, 0] += 3 if A0[0, 0] >= 0 else -3

            U = rng.normal(size=(n, r))
            d = rng.normal(size=r)
            R = U @ np.diag(d) @ U.T
            A = A0 + R
            if abs(A[0, 0]) < 1e-6:
                continue

            D = schur0(A) - schur0(A0)
            rr = np.linalg.matrix_rank(D, tol=1e-8)
            max_rank_excess = max(max_rank_excess, rr - r)
            rank_trials += 1

            E = rng.normal(size=(n, n))
            E = (E + E.T) / 2
            E = E / opnorm(E)
            delta = 0.2 * abs(A0[0, 0]) * rng.random()
            S = E * delta
            Hdiff = schur0(A0 + S) - schur0(A0)
            b0 = A0[1:, 0]
            a0 = A0[0, 0]
            eps = (
                opnorm(S)
                * (1 + np.linalg.norm(b0) / abs(a0)) ** 2
                / (1 - opnorm(S) / abs(a0))
            )
            ratio = opnorm(Hdiff) / eps if eps > 0 else 0.0
            max_tail_ratio = max(max_tail_ratio, ratio)
            tail_trials += 1

# Exact mechanism barrier from Section 8 of REPORT.md.
gamma = math.sqrt(3 / 2)
w0 = 1 / (3 / 2 + 1)
theta0 = 6 * w0
tau_star = 2 * (math.sqrt(3) - 1)
b = 1 + tau_star / 2
w = b * b / (3 / 2 + b * b)
theta = w + 2
qmin = 2 * w

out = {
    "rank_trials": rank_trials,
    "max_rank_excess": int(max_rank_excess),
    "tail_trials": tail_trials,
    "max_tail_ratio": float(max_tail_ratio),
    "base_ridge_w": w0,
    "base_theta": theta0,
    "tau_star": tau_star,
    "barrier_w": w,
    "barrier_theta": theta,
    "barrier_2qmin": 2 * qmin,
    "status": "PASS"
    if (
        max_rank_excess <= 0
        and max_tail_ratio <= 1 + 1e-8
        and abs(w - 2 / 3) < 1e-12
        and theta <= 2 * qmin + 1e-12
    )
    else "FAIL",
}
print(json.dumps(out, indent=2, sort_keys=True))
