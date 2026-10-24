#!/usr/bin/env python3
"""Finite sanity checks for the binomial-ratio part of PROB20-20.

This is diagnostic code, not a proof.  It checks:
  1. discrete convexity of R_{N,d}(x)=Bin(N,x+d)/Bin(N,x);
  2. the posterior-mean bound at material local maxima of arbitrary
     random residual convolutions with Bin(N,1/2);
  3. the Jensen inequality f(s+d)/f(s) >= R_{N,d}(E[B|S=s])
     using the piecewise-linear interpolation of R.
"""

import math
from collections import defaultdict
import numpy as np

SEED = 20260915


def binom_pmf(N: int) -> np.ndarray:
    return np.array([math.comb(N, k) for k in range(N + 1)], dtype=float) / (2.0 ** N)


def main() -> None:
    # 1. Discrete convexity grid.
    min_second = float("inf")
    convex_failures = []
    for N in range(4, 121):
        b = binom_pmf(N)
        for d in range(1, min(N, 25)):
            R = np.zeros(N + 1)
            for x in range(N - d + 1):
                R[x] = b[x + d] / b[x]
            second = R[:-2] - 2.0 * R[1:-1] + R[2:]
            local_min = float(second.min()) if len(second) else 0.0
            min_second = min(min_second, local_min)
            if local_min < -1e-10:
                convex_failures.append((N, d, local_min))

    # 2--3. Random residual convolutions.
    rng = np.random.default_rng(SEED)
    posterior_checks = 0
    min_jensen_margin = float("inf")
    max_mean_dev = 0.0
    failures = []

    for N in (30, 50, 80, 120):
        b = binom_pmf(N)
        for trial in range(25):
            residual_support = np.sort(
                rng.choice(np.arange(0, 2 * N + 1), size=min(25, 2 * N + 1), replace=False)
            )
            residual_weights = rng.random(len(residual_support))
            residual_weights /= residual_weights.sum()

            f = defaultdict(float)
            contrib_by_sum = defaultdict(list)
            for r, wr in zip(residual_support, residual_weights):
                for k, pk in enumerate(b):
                    value = float(wr * pk)
                    f[int(r + k)] += value
                    contrib_by_sum[int(r + k)].append((k, value))

            max_mass = max(f.values())
            for s in sorted(f):
                fs = f[s]
                # Ignore floating-point ghost extrema far below the meaningful mass scale.
                if fs < 1e-6 * max_mass:
                    continue
                if fs + 1e-18 < f.get(s - 1, 0.0) or fs + 1e-18 < f.get(s + 1, 0.0):
                    continue

                posterior = contrib_by_sum[s]
                EB = sum(k * value for k, value in posterior) / fs
                mean_dev = abs(EB - N / 2.0)
                max_mean_dev = max(max_mean_dev, mean_dev)
                if mean_dev > 0.5000001:
                    failures.append(("posterior_mean", N, trial, s, mean_dev))

                for d in range(1, max(2, N // 8 + 1)):
                    ratio = f.get(s + d, 0.0) / fs
                    R = np.zeros(N + 1)
                    for x in range(N - d + 1):
                        R[x] = b[x + d] / b[x]

                    lo = int(math.floor(EB))
                    hi = min(lo + 1, N)
                    t = EB - lo
                    R_interp = (1.0 - t) * R[lo] + t * R[hi]
                    margin = ratio - R_interp
                    min_jensen_margin = min(min_jensen_margin, margin)
                    posterior_checks += 1
                    if margin < -2e-12:
                        failures.append(("jensen", N, trial, s, d, margin))

    print("seed", SEED)
    print("convexity_grid_failures", len(convex_failures))
    print("minimum_discrete_second_difference", min_second)
    print("posterior_checks", posterior_checks)
    print("max_abs_posterior_mean_minus_N_over_2", max_mean_dev)
    print("minimum_Jensen_margin_positive_d", min_jensen_margin)
    print("failures", failures[:10])

    if convex_failures or failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
