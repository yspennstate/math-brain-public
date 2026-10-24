#!/usr/bin/env python3
"""Deterministic corroboration for QFORM-PUNCTURED-STAR-TETRAD-RANKONE-COMPILER-v1.

This checks finite-dimensional algebra only; it is not evidence for the universal
probabilistic theorem. The proof is symbolic in REPORT.md.
"""
import itertools
import math
import numpy as np

SEED = 20260924
TRIALS = 300
rng = np.random.default_rng(SEED)


def w_dis(S):
    n = S.shape[0]
    pairs = list(itertools.combinations(range(n), 2))
    total = 0.0
    for I in pairs:
        for J in pairs:
            if set(I).isdisjoint(J):
                total += float(np.linalg.det(S[np.ix_(I, J)]) ** 2)
    return total


def compiler_quantities(S):
    d = S[0, 1:].copy()
    C = S[1:, 1:].copy()
    m = len(d)
    r2 = float(d @ d)
    E = 0.0
    alpha = np.zeros(m)
    e = np.zeros((m, m))
    for i in range(m):
        mask = [j for j in range(m) if j != i]
        x = d[mask]
        y = C[i, mask]
        wedge_i = float((x @ x) * (y @ y) - (x @ y) ** 2)
        # floating cancellation can make a true nonnegative quantity tiny negative
        E += max(wedge_i, 0.0)
        denom = float(x @ x)
        if denom <= 0:
            raise AssertionError("diffuse nonzero d should force every d_-i nonzero")
        alpha[i] = float(x @ y) / denom
        for j in mask:
            e[i, j] = C[i, j] - alpha[i] * d[j]
    lam = float(alpha @ d) / r2
    err = sum(
        (C[i, j] - lam * d[i] * d[j]) ** 2
        for i in range(m) for j in range(m) if i != j
    )
    eerr = float(np.sum(e ** 2))
    awedge = sum(
        (alpha[i] * d[j] - alpha[j] * d[i]) ** 2
        for i in range(m) for j in range(i + 1, m)
    )
    return r2, E, lam, float(err), eerr, float(awedge)


violations = 0
max_alignment_ratio = 0.0
max_root_fraction = 0.0
min_diffuse_margin = float("inf")

for trial in range(TRIALS):
    m = int(rng.integers(3, 8))
    for _ in range(10000):
        d = rng.normal(size=m)
        r2 = float(d @ d)
        margin = 0.5 * r2 - float(np.max(d * d))
        if r2 > 1e-10 and margin >= 0:
            break
    else:
        raise AssertionError("failed to sample diffuse d")

    C = rng.normal(size=(m, m))
    C = (C + C.T) / 2.0
    c = float(rng.normal())
    S = np.block([[np.array([[c]]), d[None, :]], [d[:, None], C]])

    W = w_dis(S)
    r2, E, lam, err, eerr, awedge = compiler_quantities(S)

    claims = [
        W + 1e-9 >= 2.0 * E,
        eerr <= 2.0 * E / r2 + 1e-8,
        2.0 * E / r2 <= W / r2 + 1e-8,
        awedge <= 2.0 * eerr + 1e-8,
        err <= 6.0 * W / r2 + 1e-8,
    ]
    if not all(claims):
        violations += 1
        print("VIOLATION", trial, m, W, E, r2, eerr, awedge, err, claims)

    if W > 0:
        max_alignment_ratio = max(max_alignment_ratio, err * r2 / W)
        max_root_fraction = max(max_root_fraction, 2.0 * E / W)
    min_diffuse_margin = min(min_diffuse_margin, margin)

print(f"seed={SEED}")
print(f"trials={TRIALS}")
print(f"violations={violations}")
print(f"max_observed_alignment_ratio_err_r2_over_W={max_alignment_ratio:.15g}")
print(f"rigorous_alignment_ratio_bound=6")
print(f"max_observed_root_fraction_2E_over_W={max_root_fraction:.15g}")
print(f"rigorous_root_fraction_bound=1")
print(f"min_sampled_diffuse_margin={min_diffuse_margin:.15g}")

# Live-scale constants used in REPORT.md.
delta = 1.0 / 228.0
Cw = 8.0 * math.sqrt(2.0) * math.exp(0.25)
print(f"delta={delta:.15g}")
print(f"delta4={delta**4:.15g}")
print(f"Cw={Cw:.15g}")
print(f"live_density_bound_Cw_over_delta={Cw/delta:.15g}")
print(f"live_alignment_frobenius_bound_sqrt6_delta={math.sqrt(6.0)*delta:.15g}")
print(f"live_structured_s2_floor=1-sqrt6_delta={1.0-math.sqrt(6.0)*delta:.15g}")

if violations:
    raise SystemExit(1)
