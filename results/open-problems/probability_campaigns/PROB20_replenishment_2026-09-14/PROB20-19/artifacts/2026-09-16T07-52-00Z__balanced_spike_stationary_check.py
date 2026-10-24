#!/usr/bin/env python3
"""Reproducible self-checks for the balanced-support stationary-spike theorem.

This script is supporting numerical evidence only. The theorem in the report is analytic.
It checks:
  1. the strict majorization chain y^(1) > ... > y^(p);
  2. Monte Carlo near-zero pair-gradient matrix K for balanced support spikes;
  3. strict decreasing objective values across positive-spike support sizes;
  4. opposite-value perturbations around an intermediate positive-spike saddle;
  5. near-zero K also for a negative spike, for which stationarity is analytic but the
     landscape classification remains open.
"""

import numpy as np

SEED = 20260916
P = 6
D = 3
A = 1.0
C_POS = 0.8
C_NEG = -0.5
N = 600_000
EPS = 0.10


def balanced_u(p, m):
    u = np.zeros(p)
    u[:m] = 1.0 / np.sqrt(m)
    return u


def spike_samples(z, u, a, c):
    if not (a > 0 and a + c > 0):
        raise ValueError("need a>0 and a+c>0")
    # Positive-definite square root of a I + c u u^T.
    coeff = np.sqrt(a + c) - np.sqrt(a)
    return np.sqrt(a) * z + coeff * (z @ u)[:, None] * u[None, :]


def topd_and_indicators(x, d):
    sq = x * x
    p = x.shape[1]
    idx = np.argpartition(sq, -d, axis=1)[:, -d:]
    ind = np.zeros_like(sq, dtype=np.int8)
    rows = np.arange(x.shape[0])[:, None]
    ind[rows, idx] = 1
    val = np.take_along_axis(sq, idx, axis=1).sum(axis=1)
    return val, ind


def k_matrix(x, d):
    value, ind = topd_and_indicators(x, d)
    p = x.shape[1]
    k = np.zeros((p, p))
    for i in range(p):
        for j in range(i + 1, p):
            kij = 2.0 * np.mean(x[:, i] * x[:, j] * (ind[:, i] - ind[:, j]))
            k[i, j] = kij
            k[j, i] = -kij
    return value, k


def sorted_partial_sums(y):
    return np.cumsum(np.sort(np.asarray(y))[::-1])


def majorizes(x, y, tol=1e-14):
    sx = sorted_partial_sums(x)
    sy = sorted_partial_sums(y)
    return np.all(sx[:-1] >= sy[:-1] - tol) and abs(sx[-1] - sy[-1]) <= tol


def objective(z, y, a, c, d):
    y = np.asarray(y, dtype=float)
    u = np.sqrt(y / y.sum())
    x = spike_samples(z, u, a, c)
    return topd_and_indicators(x, d)[0]


def main():
    rng = np.random.default_rng(SEED)
    z = rng.standard_normal((N, P))

    print("PARAMETERS")
    print(f"seed={SEED} p={P} d={D} a={A} c_pos={C_POS} c_neg={C_NEG} n={N}")
    print()

    ys = []
    for m in range(1, P + 1):
        y = np.zeros(P)
        y[:m] = 1.0 / m
        ys.append(y)

    chain_ok = all(majorizes(ys[m - 1], ys[m]) for m in range(1, P))
    print("EXACT MAJORIZATION CHAIN")
    print("y^(1) >=_maj ... >=_maj y^(p):", chain_ok)
    assert chain_ok
    print()

    print("POSITIVE SPIKE: objective and sampled K")
    pos_values = []
    for m in range(1, P + 1):
        u = balanced_u(P, m)
        x = spike_samples(z, u, A, C_POS)
        val, k = k_matrix(x, D)
        mean = float(val.mean())
        pos_values.append(mean)
        print(
            f"m={m} mean={mean:.12f} "
            f"max_abs_K={np.max(np.abs(k)):.8f} fro_K={np.linalg.norm(k):.8f}"
        )
    monotone_sample = all(pos_values[m - 1] > pos_values[m] for m in range(1, P))
    print("sampled strict descending support-size values:", monotone_sample)
    print()

    print("INTERMEDIATE SADDLE CHECK, m=3")
    y0 = np.array([1/3, 1/3, 1/3, 0, 0, 0.0])
    y_plus = np.array([1/3 + EPS, 1/3 - EPS, 1/3, 0, 0, 0.0])
    y_minus = np.array([1/3 - EPS, 1/3, 1/3, EPS, 0, 0.0])
    assert majorizes(y_plus, y0)
    assert majorizes(y0, y_minus)
    f0 = objective(z, y0, A, C_POS, D)
    fp = objective(z, y_plus, A, C_POS, D)
    fm = objective(z, y_minus, A, C_POS, D)
    for label, diff in (("concentrating", fp - f0), ("spreading", fm - f0)):
        mean = float(diff.mean())
        se = float(diff.std(ddof=1) / np.sqrt(N))
        print(f"{label}: mean_diff={mean:.12g} se={se:.12g} z={mean/se:.6f}")
    print()

    print("NEGATIVE SPIKE: sampled K remains near zero at balanced supports")
    for m in range(1, P + 1):
        u = balanced_u(P, m)
        x = spike_samples(z, u, A, C_NEG)
        val, k = k_matrix(x, D)
        print(
            f"m={m} mean={val.mean():.12f} "
            f"max_abs_K={np.max(np.abs(k)):.8f} fro_K={np.linalg.norm(k):.8f}"
        )

    print()
    print("NOTE: Monte Carlo checks are self-review only; stationarity and the positive-spike")
    print("landscape classification are proved analytically in the companion report.")


if __name__ == "__main__":
    main()
