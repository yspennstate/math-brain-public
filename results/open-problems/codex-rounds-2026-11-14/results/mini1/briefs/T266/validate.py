#!/usr/bin/env python3
"""Small audits for PROOF.md; writes only beside this script."""
import os

for key in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS",
            "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS", "BLIS_NUM_THREADS"):
    os.environ[key] = "1"

import csv
import json
import math
from pathlib import Path
import resource
import signal
import sys
import time

# BSD nice can print an error yet still execute its command under a sandbox.
# Refuse scientific work unless the requested low priority actually took effect.
try:
    process_nice = os.getpriority(os.PRIO_PROCESS, 0)
except (AttributeError, OSError) as exc:
    sys.exit(f"Refusing audit: cannot verify process nice value: {exc}")
if process_nice < 15:
    sys.exit(f"Refusing audit: nice value is {process_nice}; require at least 15")

def timeout_handler(signum, frame):
    raise TimeoutError("Audit exceeded 90 seconds")

signal.signal(signal.SIGALRM, timeout_handler)
signal.alarm(90)
started = time.monotonic()

import numpy as np
from scipy import special, stats

# Treat the floating-point warnings observed in the original run as failures.
np.seterr(divide="raise", over="raise", invalid="raise")

ROOT = Path(__file__).resolve().parent
rng = np.random.default_rng(2661411)


def gradient_audit(n, d):
    # Controlled singular values exercise the deterministic optimization theorem.
    # The risk-distribution tests below use unmodified iid Gaussian designs.
    rank = min(n, d)
    u, _ = np.linalg.qr(rng.normal(size=(n, rank)))
    v, _ = np.linalg.qr(rng.normal(size=(d, rank)))
    A = (u * np.linspace(1.0, 2.0, rank)) @ v.T
    b = rng.normal(size=n) / math.sqrt(n)
    beta_star = np.linalg.lstsq(A, b, rcond=None)[0]
    svals = np.linalg.svd(A, compute_uv=False)
    s = float(svals[-1])
    h = float(svals[0] ** 2)
    L0 = float(b @ b / 2)
    B = 2 * np.linalg.norm(b) / s
    M = math.sqrt(1 + 4 * B * B)
    G = math.sqrt(h) * np.linalg.norm(b)
    D = 6 * h * M + G
    eta = min(1 / (1 + G), 1 / (1 + D), 1 / (1 + 8 * L0))
    summaries = []
    final_betas = []
    for p in (1, 3, 11):
        q = np.ones(p) / math.sqrt(p)
        a = q.copy()
        W = np.zeros((p, d))
        c = 1.0
        w = np.zeros(d)
        min_K = 1.0
        descent_violation = 0.0
        imbalance_error = 0.0
        factor_reduction_error = 0.0
        predictor_recurrence_error = 0.0
        for t in range(25000):
            beta = W.T @ a
            residual = A @ beta - b
            g = A.T @ residual
            grad_a = W @ g
            grad_W = np.outer(a, g)
            loss = float(residual @ residual / 2)
            grad_sq = float(grad_a @ grad_a + np.sum(grad_W * grad_W))
            old_K = float(a @ a - np.sum(W * W))
            a_next = a - eta * grad_a
            W_next = W - eta * grad_W
            beta_next = W_next.T @ a_next
            # Independently expand the full matrix update for the predictor.
            predicted_beta = (
                beta - eta * ((a @ a) * g + W.T @ (W @ g))
                + eta * eta * (beta @ g) * g
            )
            predictor_recurrence_error = max(
                predictor_recurrence_error,
                float(np.linalg.norm(beta_next - predicted_beta)))
            reduced_g = A.T @ (A @ (c * w) - b)
            c_next = c - eta * float(w @ reduced_g)
            w_next = w - eta * c * reduced_g
            factor_reduction_error = max(
                factor_reduction_error,
                float(np.linalg.norm(a_next - c_next * q)),
                float(np.linalg.norm(W_next - np.outer(q, w_next))))
            next_residual = A @ beta_next - b
            next_loss = float(next_residual @ next_residual / 2)
            descent_violation = max(
                descent_violation, next_loss - loss + eta * grad_sq / 2)
            new_K = float(a_next @ a_next - np.sum(W_next * W_next))
            expected_K = old_K + eta * eta * (
                float(grad_a @ grad_a) - float(a @ a) * float(g @ g))
            imbalance_error = max(imbalance_error, abs(new_K - expected_K))
            min_K = min(min_K, new_K)
            a, W, c, w = a_next, W_next, c_next, w_next
            if np.linalg.norm(beta_next - beta_star) < 1e-9:
                break
        error = float(np.linalg.norm(W.T @ a - beta_star))
        assert error < 1e-8, (n, d, p, t, error)
        assert min_K >= 1 - 2 * eta * L0 - 1e-11
        assert descent_violation < 1e-12
        assert imbalance_error < 1e-12
        assert factor_reduction_error < 1e-10
        assert predictor_recurrence_error < 1e-12
        final_betas.append(W.T @ a)
        summaries.append({
            "p": p, "steps": t + 1, "predictor_error": error,
            "min_K": min_K, "descent_violation": descent_violation,
            "imbalance_identity_error": imbalance_error,
            "full_vs_reduced_factor_error": factor_reduction_error,
            "predictor_recurrence_error": predictor_recurrence_error,
        })
    width_difference = max(float(np.linalg.norm(z - final_betas[0]))
                           for z in final_betas)
    assert width_difference < 1e-11
    # Central finite differences check both actual layer gradients at a point
    # off the special rank-one trajectory.
    a = rng.normal(size=3)
    W = rng.normal(size=(3, d)) / math.sqrt(d)
    g = A.T @ (A @ W.T @ a - b)
    grad_a = W @ g
    grad_W = np.outer(a, g)
    da = rng.normal(size=3)
    dW = rng.normal(size=(3, d))
    da /= np.linalg.norm(da)
    dW /= np.linalg.norm(dW)
    def F(aa, WW):
        rr = A @ WW.T @ aa - b
        return float(rr @ rr / 2)
    eps = 1e-5
    finite_difference = (F(a + eps * da, W + eps * dW)
                         - F(a - eps * da, W - eps * dW)) / (2 * eps)
    analytic_derivative = float(grad_a @ da + np.sum(grad_W * dW))
    derivative_error = abs(finite_difference - analytic_derivative)
    assert derivative_error < 1e-7
    return {"n": n, "d": d, "eta": eta,
            "proved_K_lower_bound": float(1 - 2 * eta * L0),
            "width_difference": width_difference,
            "finite_difference_gradient_error": derivative_error,
            "runs": summaries}


def risk_audit():
    # Direct Gaussian matrices, no training approximations and no target bias.
    cases = [(24, 12), (16, 16), (12, 24), (24, 23), (23, 24)]
    rows = []
    summaries = []
    max_solve_difference = 0.0
    for n, d in cases:
        r = min(n, d)
        nu = abs(n - d) + 1
        values = []
        bias_values = []
        theta = np.zeros(d)
        theta[0] = 1.0
        for rep in range(1200):
            X = rng.normal(size=(n, d))
            noise = rng.normal(size=n)
            # QR, independently of the Gram inverse used in the lemma.
            if n >= d:
                Q, T = np.linalg.qr(X, mode="reduced")
                error = np.linalg.solve(T, Q.T @ noise)
                bias = 0.0
            else:
                Q, T = np.linalg.qr(X.T, mode="reduced")
                error = Q @ np.linalg.solve(T.T, noise)
                bias = float(np.linalg.norm(theta - Q @ (Q.T @ theta)) ** 2)
            value = float(error @ error)
            if rep < 20:
                independently = np.linalg.lstsq(X, noise, rcond=None)[0]
                relative = np.linalg.norm(error - independently) / max(
                    1.0, np.linalg.norm(error))
                max_solve_difference = max(max_solve_difference, float(relative))
            independent_ratio = float(rng.chisquare(r) / rng.chisquare(nu))
            pit = float(special.betainc(r / 2, nu / 2, value / (1 + value)))
            values.append(value)
            bias_values.append(bias)
            rows.append([n, d, rep, value, independent_ratio, pit, bias])
        pits = np.array([z[5] for z in rows[-1200:]])
        result = stats.kstest(pits, "uniform")
        # A diagnostic, not a proof or a search over seeds. Fixed seed throughout.
        assert result.statistic < 0.065, (n, d, result)
        expected_mean = None if nu <= 2 else r / (nu - 2)
        summaries.append({
            "n": n, "d": d, "r": r, "nu": nu, "replicates": 1200,
            "pit_KS_statistic": float(result.statistic),
            "pit_KS_pvalue": float(result.pvalue),
            "noise_median": float(np.median(values)),
            "exact_noise_median": float(r / nu * stats.f.ppf(0.5, r, nu)),
            "noise_sample_mean": float(np.mean(values)),
            "noise_exact_mean": expected_mean,
            "bias_mean": float(np.mean(bias_values)),
            "bias_exact_mean": max(0.0, 1 - n / d),
        })
    assert max_solve_difference < 1e-8
    with (ROOT / "risk_samples.csv").open("w", newline="") as fp:
        writer = csv.writer(fp)
        writer.writerow(["n", "d", "rep", "noise_risk", "independent_ratio",
                         "probability_integral_transform", "unit_signal_bias"])
        writer.writerows(rows)
    return summaries, max_solve_difference


def critical_audit():
    # Independent square-matrix derivation: R/sigma^2 = n F_{n,1}.
    # Its limiting inverse-chi-square(1) CDF is erfc(1/sqrt(2t)).
    quantiles = []
    for probability in (0.1, 0.5, 0.9):
        z = stats.norm.ppf(1 - probability / 2)
        quantile = float(1 / (z * z))
        cdf_erfc = math.erfc(1 / math.sqrt(2 * quantile))
        cdf_chi = float(stats.chi2.sf(1 / quantile, 1))
        assert abs(cdf_erfc - probability) < 1e-14
        assert abs(cdf_chi - probability) < 1e-14
        quantiles.append({"probability": probability, "limit_quantile": quantile,
                          "cdf_erfc": cdf_erfc, "cdf_chi2": cdf_chi})
    return quantiles


summary = {
    "seed": 2661411,
    "verified_process_nice": process_nice,
    "numpy_version": np.__version__,
    "thread_environment": {k: os.environ[k] for k in
                           ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS",
                            "VECLIB_MAXIMUM_THREADS", "MKL_NUM_THREADS")},
    "gd": [gradient_audit(n, d) for n, d in ((18, 8), (8, 18), (12, 12))],
}
summary["risk"], summary["max_QR_vs_SVD_relative_error"] = risk_audit()
summary["critical_quantiles"] = critical_audit()
rss_native = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
rss_bytes = int(rss_native if sys.platform == "darwin" else rss_native * 1024)
summary["peak_rss_bytes"] = rss_bytes
summary["elapsed_seconds"] = time.monotonic() - started
assert rss_bytes < 1024 ** 3
assert summary["elapsed_seconds"] < 90
summary["status"] = "PASS"
with (ROOT / "validation.json").open("w") as fp:
    json.dump(summary, fp, indent=2, allow_nan=False)
    fp.write("\n")
print("PASS: full two-layer GD, reduced GD, predictor recurrence, and finite differences")
for run in summary["gd"]:
    print(f"GD n={run['n']} d={run['d']} widths=1,3,11 "
          f"max_error={max(z['predictor_error'] for z in run['runs']):.3g} "
          f"width_difference={run['width_difference']:.3g}")
for run in summary["risk"]:
    print(f"RISK n={run['n']} d={run['d']} df=({run['r']},{run['nu']}) "
          f"KS={run['pit_KS_statistic']:.5f} p={run['pit_KS_pvalue']:.5f}")
print("CRITICAL inverse-chi-square(1) quantiles:",
      ", ".join(f"q{int(z['probability'] * 100)}={z['limit_quantile']:.9f}"
                for z in summary["critical_quantiles"]))
print(f"Peak RSS: {rss_bytes / 1024**2:.2f} MiB")
print(f"Elapsed: {summary['elapsed_seconds']:.3f} seconds")
print("Data: validation.json, risk_samples.csv")
