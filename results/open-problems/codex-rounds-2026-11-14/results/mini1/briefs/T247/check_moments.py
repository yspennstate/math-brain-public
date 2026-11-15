#!/usr/bin/env python3
"""Small independent checks of PROOF.md; writes results.json in this folder."""

import os

for variable in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS",
                 "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ[variable] = "1"

import itertools
import json
import math
from pathlib import Path
import resource
import signal
import time
from fractions import Fraction as F

signal.alarm(180)
START = time.monotonic()
import numpy as np


def exact_check(n, variances):
    s = t = F(1)
    product = F(1)
    for v in variances:
        h = (2 * s + n * t) / (n + 2)
        s, t = s + v * h, t + v * h / n
        product *= 1 + 3 * v / (n + 2)
    closed_s = 1 + F(n + 2, 3) * (product - 1)
    closed_t = 1 + F(n + 2, 3 * n) * (product - 1)
    assert s == closed_s and t == closed_t
    assert n * t + 2 * s == (n + 2) * product
    total = sum(variances, F(0))
    error = s - 1 - total
    assert error >= 0
    bound = 3 * float(total)**2 / (2*(n+2)) * math.exp(3*float(total)/(n+2))
    assert float(error) <= bound + 1e-12
    if variances and len(set(variances)) == 1:
        depth, v = len(variances), variances[0]
        assert error >= F(3, 2*(n+2)) * v*v * depth*(depth-1)
    return s, t


def direct_circle_check():
    """Integrate the actual n=2,L=2 traces over gates and Haar angle.

    The first O cancels from X. For the second O, only cos^4, sin^4,
    and cos^2 sin^2 occur, whose circle integrals are 3/8,3/8,1/8.
    Both determinant components of O(2) have these same expressions.
    No recurrence or product formula is used in this calculation.
    """
    total_q = F(0)
    total_t2 = F(0)
    for a, b, c, d in itertools.product((0, 2), repeat=4):
        diag_sq = F(3, 8) * (a*a + b*b) + F(1, 4) * a*b
        q = (c*c + d*d) * diag_sq + F(1, 4) * c*d * (a-b)**2
        u, w = c*a + d*b, c*b + d*a
        t2 = F(3, 8) * (u*u + w*w) + F(1, 4) * u*w
        total_q += q / 16
        total_t2 += t2 / 16
    s, t = total_q / 2, total_t2 / 4
    assert s == F(15, 4) and t == F(19, 8)
    return {"n": 2, "L": 2, "v": 1,
            "direct_s": str(s), "direct_t": str(t),
            "direct_expected_Z": str(s - 1)}


def moments(n, variances):
    log_p = math.fsum(math.log1p(3 * v / (n + 2)) for v in variances)
    spread = (n + 2) / 3 * math.expm1(log_p)
    return 1 + spread, 1 + spread / n, math.exp(log_p)


def mean_se(values):
    values = np.asarray(values, dtype=float)
    return float(values.mean()), float(values.std(ddof=1) / math.sqrt(len(values)))


def monte_carlo(n, deltas, samples, seed):
    rng = np.random.default_rng(seed)
    observations = []
    for unused in range(samples):
        j = np.eye(n)
        for delta in deltas:
            q, r = np.linalg.qr(rng.standard_normal((n, n)))
            signs = np.where(np.diag(r) >= 0, 1.0, -1.0)
            o = q * signs[None, :]
            a = 1 + delta * rng.choice((-1.0, 1.0), size=n)
            j = np.sqrt(a)[:, None] * (o @ j)
        x = j @ j.T
        tr = np.trace(x) / n
        m2 = np.sum(x*x) / n
        z = np.sum((x-np.eye(n))**2) / n
        norm4 = np.sum(j[:, 0]**2)**2
        observations.append((tr, m2, tr*tr, z, norm4))
    values = np.asarray(observations)
    s, t, p = moments(n, [d*d for d in deltas])
    predictions = (1.0, s, t, s-1, p)
    names = ("trace_mean", "spectral_second_moment", "trace_mean_squared",
             "distortion_Z", "fixed_vector_norm_fourth")
    results = {}
    for k, name in enumerate(names):
        estimate, se = mean_se(values[:, k])
        error = abs(estimate - predictions[k])
        assert error <= 6 * se + 1e-12, (name, estimate, se, predictions[k])
        results[name] = {"predicted": predictions[k], "sample_mean": estimate,
                         "standard_error": se, "error_in_se": error/se if se else 0}
    return {"n": n, "L": len(deltas), "deltas": deltas, "samples": samples,
            "seed": seed, "observations": results}


def tanh_check(nodes):
    # Gauss-Hermite quadrature for a standard real normal.
    x, w = np.polynomial.hermite.hermgauss(nodes)
    g, weights = math.sqrt(2) * x, w / math.sqrt(math.pi)
    records = []
    for q in (0.1, 0.03, 0.01, 0.003, 0.001, 0.0003, 0.0001):
        b = np.cosh(math.sqrt(q) * g)**(-4)
        mean = float(weights @ b)
        variance = float(weights @ (b-mean)**2) / mean**2
        records.append({"q": q, "v": variance, "v_over_q_squared": variance/q**2})
    return records


def main():
    assert os.getpriority(os.PRIO_PROCESS, 0) >= 15
    exact_count = 0
    for n in (1, 2, 3, 10, 97):
        for depth in (0, 1, 2, 3, 9, 27):
            for v in (F(0), F(1, 4), F(1)):
                exact_check(n, [v] * depth)
                exact_count += 1
        exact_check(n, [F(1, 4), F(1), F(0), F(2, 7)])
        exact_count += 1

    circle = direct_circle_check()
    simulations = [
        monte_carlo(2, [1.0, 1.0], 12000, 24701),
        monte_carlo(4, [0.5] * 8, 8000, 24702),
        monte_carlo(8, [0.0, 0.25, 0.5, 0.75, 0.25, 0.5], 6000, 24703),
    ]
    tanh128, tanh256 = tanh_check(128), tanh_check(256)
    quadrature_difference = max(abs(a["v"]-b["v"])/a["v"]
                                for a, b in zip(tanh128, tanh256))
    assert quadrature_difference < 1e-7
    assert abs(tanh256[-1]["v_over_q_squared"] - 8) < 0.02

    joint_examples = []
    for n in (100, 1000, 10000):
        # Constant v=1 and L=n, evaluated without allocating L matrices.
        log_p = n * math.log1p(3 / (n + 2))
        spread = (n+2) / 3 * math.expm1(log_p)
        joint_examples.append({"n": n, "L": n, "v": 1,
                               "spread_over_n": spread/n,
                               "free_spread_over_n": 1})
    kernel_examples = []
    for n in (100, 10000, 1000000):
        depth = math.isqrt(n)
        v = 1 / (n-1)
        spread = (n+2)/3 * math.expm1(depth * math.log1p(3*v/(n+2)))
        log_invertible_probability = n * depth * math.log1p(-1/n)
        kernel_examples.append({"n": n, "L": depth, "V": depth*v,
                                "expected_Z": spread,
                                "log_invertible_probability": log_invertible_probability})

    # macOS reports ru_maxrss in bytes. Linux reports KiB.
    import sys
    peak = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    peak_bytes = peak if sys.platform == "darwin" else peak * 1024
    assert peak_bytes < 1024**3
    result = {"exact_rational_cases_passed": exact_count,
              "circle_integral": circle,
              "monte_carlo": simulations,
              "tanh_quadrature_256": tanh256,
              "quadrature_128_vs_256_max_relative_difference": quadrature_difference,
              "joint_examples": joint_examples,
              "kernel_examples": kernel_examples,
              "runtime_seconds": time.monotonic()-START,
              "peak_rss_bytes": peak_bytes,
              "niceness": os.getpriority(os.PRIO_PROCESS, 0),
              "numpy_version": np.__version__,
              "thread_environment": {k: os.environ[k] for k in
                  ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS",
                   "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS")}}
    output = Path(__file__).resolve().parent / "results.json"
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(f"Exact rational cases: {exact_count} passed (including error-bound checks)")
    print(f"Independent circle integration: s={circle['direct_s']}, t={circle['direct_t']}")
    for simulation in simulations:
        worst = max(x["error_in_se"] for x in simulation["observations"].values())
        print(f"Monte Carlo n={simulation['n']}, L={simulation['L']}, "
              f"samples={simulation['samples']}: max error {worst:.3f} SE")
    print(f"tanh v(q)/q^2 at q=0.0001: {tanh256[-1]['v_over_q_squared']:.9f} (limit 8)")
    print(f"128/256-node quadrature max relative difference: {quadrature_difference:.3g}")
    for record in joint_examples:
        print(f"v=1, L=n={record['n']}: E Z/n={record['spread_over_n']:.9f} (free 1)")
    for record in kernel_examples:
        print(f"Kernel example n={record['n']}, L={record['L']}: "
              f"E Z={record['expected_Z']:.9g}, log P(invertible)="
              f"{record['log_invertible_probability']:.9g}")
    print(f"Niceness: {result['niceness']}; peak RSS: {peak_bytes/1024**2:.1f} MiB; "
          f"runtime: {result['runtime_seconds']:.2f} s")
    print("All checks passed; data written to results.json")


if __name__ == "__main__":
    main()
