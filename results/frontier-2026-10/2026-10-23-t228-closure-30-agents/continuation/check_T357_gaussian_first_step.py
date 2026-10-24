#!/usr/bin/env python3
"""Reproducible finite-d Gaussian random-feature moment sanity checks.

Numerical evidence only: no fitted coefficients, extrapolation, or CLT proof.
Each training set and feature matrix is an independent replication.  Multiple
test queries within one replication are treated as one uncertainty cluster.
"""
import os
for _name in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[_name] = "1"

import argparse
import hashlib
import json
import math
from pathlib import Path
import platform
import time

import numpy as np
import scipy
from scipy.integrate import quad
from scipy.special import expit, roots_hermitenorm
from scipy.stats import t as student_t

SEEDS = [1729, 2027, 4211, 8089]
DIMENSIONS = [64, 128, 256, 512, 1024]
RATIOS = [(1, 1), (1, 2), (2, 1), (2, 2)]
TEST_QUERIES = 512
C = 1.0
NORMALIZER = math.sqrt(2 * math.pi)
GH128_X, GH128_W = roots_hermitenorm(128)
GH256_X, GH256_W = roots_hermitenorm(256)
GH128_W /= NORMALIZER
GH256_W /= NORMALIZER


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def reference(beta):
    def integrate(function):
        return quad(lambda z: function(z) * math.exp(-z * z / 2) / NORMALIZER,
                    -np.inf, np.inf, epsabs=2e-13, epsrel=2e-13, limit=200)
    a, aerr = integrate(lambda z: z * math.tanh(z))
    b, berr = integrate(lambda z: math.tanh(z) ** 2)
    mu, muerr = integrate(lambda z: z * (float(expit(beta * z)) - 0.5))
    gh = {
        "a": float(np.dot(GH256_W, GH256_X * np.tanh(GH256_X))),
        "b": float(np.dot(GH256_W, np.tanh(GH256_X) ** 2)),
        "mu": float(np.dot(GH256_W, GH256_X * (expit(beta * GH256_X) - 0.5))),
    }
    require(abs(a + b - 1) < 1e-11, "Stein identity a=1-b failed numerically")
    if beta == 2:
        require(abs(mu - a / 2) < 1e-11, "Beta=2 identity mu=a/2 failed")
    return {"beta": beta, "a": a, "b": b, "mu": mu,
            "quad_reported_errors": {"a": aerr, "b": berr, "mu": muerr},
            "independent_256_point_gauss_hermite": gh,
            "max_quad_gauss_hermite_difference": max(abs(gh[k] - value)
                for k, value in [("a", a), ("b", b), ("mu", mu)])}


def prediction(constants, alpha, gamma):
    a, b, mu = constants["a"], constants["b"], constants["mu"]
    covariance = C * a * a * mu
    terms = {
        "signal_square": C * C * (a * a * mu) ** 2,
        "feature_signal": C * C * mu * mu * a * a * b / gamma,
        "sample_linear": C * C * a ** 4 / (4 * alpha),
        "sample_feature": C * C * b * b / (4 * alpha * gamma),
    }
    return {"covariance": covariance, "variance": sum(terms.values()),
            "variance_terms": terms}


def one_replication(d, alpha, gamma, beta, seed, replicate_index, queries):
    n, m = int(alpha * d), int(gamma * d)
    seed_words = [seed, d, n, m, int(beta * 1000), replicate_index]
    rng = np.random.default_rng(np.random.SeedSequence(seed_words))
    features = rng.standard_normal((d, m)) / math.sqrt(d)
    x = rng.standard_normal((n, d))
    labels = (rng.random(n) < expit(beta * x[:, 0])).astype(np.float64)
    train_hidden = np.tanh(x @ features)
    # score(x0) = (c*d/n) * tanh(x0 F) @ [H_train.T (Y-.5)/m].
    weights = train_hidden.T @ (labels - 0.5) / m
    x0 = rng.standard_normal((queries, d))
    score = (C * d / n) * (np.tanh(x0 @ features) @ weights)
    z = x0[:, 0]
    # Oddness gives exactly zero conditional test means. Antithetic pairs
    # (x0,-x0) have the same ZS and S^2, so queries is the independent count,
    # not twice that count. No artificial doubling of effective samples.
    cov_query = float(np.mean(z * score))
    variance_query = float(np.mean(score * score))

    # Optional variance-reduced covariance check. Conditional on train/F,
    # Gaussian integration by parts gives E[Z tanh(f_j.X0)]
    # = f_(1,j) E[sech^2(||f_j|| G)].  Two quadrature orders monitor error.
    norms = np.linalg.norm(features, axis=0)
    psi128 = (1 - np.tanh(norms[:, None] * GH128_X[None, :]) ** 2) @ GH128_W
    psi256 = (1 - np.tanh(norms[:, None] * GH256_X[None, :]) ** 2) @ GH256_W
    cov_cond128 = float((C * d / n) * np.dot(weights * features[0], psi128))
    cov_cond256 = float((C * d / n) * np.dot(weights * features[0], psi256))
    require(np.isfinite([cov_query, variance_query, cov_cond256]).all(),
            "Nonfinite simulation output")
    return {"seed": seed, "replicate_index": replicate_index,
            "seed_sequence_entropy": seed_words,
            "covariance_query": cov_query, "variance_query": variance_query,
            "covariance_conditional_stein": cov_cond256,
            "conditional_covariance_quadrature_difference": abs(cov_cond256 - cov_cond128),
            "feature_norm_min": float(norms.min()), "feature_norm_max": float(norms.max()),
            "unpaired_query_mean_z": float(np.mean(z)),
            "unpaired_query_mean_score": float(np.mean(score))}


def estimate(rows, key, target):
    values = np.array([row[key] for row in rows])
    count = len(values)
    mean = float(values.mean())
    se = float(values.std(ddof=1) / math.sqrt(count))
    half_width = float(student_t.ppf(0.975, count - 1) * se)
    return {"mean": mean, "cluster_standard_error": se,
            "approximate_pointwise_95_percent_interval": [mean - half_width, mean + half_width],
            "asymptotic_target": target, "difference_from_target": mean - target,
            "relative_difference": None if target == 0 else (mean - target) / target,
            "difference_in_standard_errors": None if se == 0 else (mean - target) / se,
            "independent_train_feature_clusters": count}


def run_configuration(d, alpha, gamma, beta, per_seed, queries, constants):
    start = time.monotonic()
    target = prediction(constants, alpha, gamma)
    rows = [one_replication(d, alpha, gamma, beta, seed, index, queries)
            for seed in SEEDS for index in range(per_seed)]
    summaries = {
        "covariance_query": estimate(rows, "covariance_query", target["covariance"]),
        "covariance_conditional_stein": estimate(rows, "covariance_conditional_stein", target["covariance"]),
        "variance_query": estimate(rows, "variance_query", target["variance"]),
    }
    per_seed_means = [{"seed": seed, **{key: float(np.mean([row[key] for row in rows if row["seed"] == seed]))
                                      for key in summaries}} for seed in SEEDS]
    result = {"dimension": d, "alpha": alpha, "gamma": gamma, "beta": beta,
              "c": C, "n": alpha * d, "m": gamma * d,
              "replicates_per_seed": per_seed, "independent_queries_per_cluster": queries,
              "prediction": target, "estimates": summaries, "per_seed_means": per_seed_means,
              "largest_conditional_covariance_quadrature_difference": max(
                  row["conditional_covariance_quadrature_difference"] for row in rows),
              "feature_norm_range": [min(row["feature_norm_min"] for row in rows),
                                     max(row["feature_norm_max"] for row in rows)],
              "seconds": time.monotonic() - start, "replications": rows}
    print(f"d={d:4d} alpha={alpha} gamma={gamma} beta={beta}: "
          f"cov={summaries['covariance_conditional_stein']['mean']:.6f} "
          f"(target {target['covariance']:.6f}); "
          f"var={summaries['variance_query']['mean']:.6f} "
          f"(target {target['variance']:.6f}); {result['seconds']:.1f}s", flush=True)
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pilot", action="store_true")
    parser.add_argument("--output", type=Path,
                        default=Path(__file__).with_suffix(".json"))
    args = parser.parse_args()
    constants = {str(beta): reference(beta) for beta in [0, 1, 2, 4]}
    configurations = ([(64, 1, 1, 2, 2)] if args.pilot else
        [(d, alpha, gamma, 2, 8 if d == 1024 else 16)
         for d in DIMENSIONS for alpha, gamma in RATIOS]
        + [(d, 1, 1, beta, 8) for beta in [1, 4] for d in [256, 1024]]
        + [(512, 1, 1, 0, 16)])
    output = {
        "status": "RUNNING",
        "scope": "Finite-dimensional Monte Carlo moment sanity checks, not proof or fitted theory",
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "python": platform.python_version(), "numpy": np.__version__, "scipy": scipy.__version__,
        "rng": "NumPy default_rng / PCG64 with recorded SeedSequence entropy per replication",
        "blas_threads_requested": 1, "seeds": SEEDS, "pilot": args.pilot,
        "reference_integrals": constants,
        "uncertainty": "Student-t intervals across independent training/features replications; pointwise approximate Monte Carlo intervals, no finite-d asymptotic-bias allowance and no simultaneous coverage claim",
        "means": "E[Z]=E[S]=0 exactly by symmetric independent test inputs and odd tanh; ZS and S^2 estimate covariance and variance without fitting or centering",
        "configurations": [],
    }
    start = time.monotonic()
    for d, alpha, gamma, beta, repetitions in configurations:
        output["configurations"].append(run_configuration(d, alpha, gamma, beta, repetitions,
                                                           TEST_QUERIES, constants[str(beta)]))
        args.output.write_text(json.dumps(output, indent=2) + "\n")
    output["status"] = "COMPLETE"
    output["elapsed_seconds"] = time.monotonic() - start
    require(hashlib.sha256(Path(__file__).read_bytes()).hexdigest() == output["script_sha256"],
            "Script changed during run")
    args.output.write_text(json.dumps(output, indent=2) + "\n")
    print(f"Saved {args.output}; {len(configurations)} configurations in {output['elapsed_seconds']:.1f}s")


if __name__ == "__main__":
    main()
