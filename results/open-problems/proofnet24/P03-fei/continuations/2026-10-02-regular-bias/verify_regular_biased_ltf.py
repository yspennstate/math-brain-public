"""Finite checks for the arbitrary-bias regular-LTF known-results corollary."""

import json
import math
from pathlib import Path

import numpy as np


rng = np.random.default_rng(20261003)
report = {"status": "all assertions passed", "seed": 20261003,
          "ltfs": 0, "noise_checks": 0, "l2_regularity_checks": 0,
          "maximum_H_over_p_sqrt_nL": 0.0,
          "maximum_NS_over_p_sqrt_epsilonL": 0.0,
          "maximum_indicator_singleton_identity_error": 0.0,
          "scope": "finite checks; analytic proof uses established KOS and Keller-Klein theorems; novelty unconfirmed"}


def fwht(f):
    a = np.array(f, dtype=float)
    step = 1
    while step < len(a):
        block = a.reshape(-1, 2 * step)
        left, right = block[:, :step].copy(), block[:, step:].copy()
        block[:, :step], block[:, step:] = left + right, left - right
        step *= 2
    # Bit 1 represents x_i=+1, so the standard Walsh character differs
    # from the product-of-x convention by (-1)^degree.
    signs = np.array([(-1) ** int(j).bit_count() for j in range(len(a))])
    return a * signs / len(a)


def entropy(p):
    p = p[p > 0]
    return float(-np.sum(p * np.log2(p)))


for n in [1, 2, 3, 4, 6, 8, 10, 12, 14]:
    index = np.arange(1 << n)
    x = 2 * ((index[:, None] >> np.arange(n)) & 1) - 1
    degree = np.array([int(j).bit_count() for j in index])
    for law in ["nearuniform", "normal", "geometric"]:
        if law == "nearuniform":
            w = rng.uniform(.5, 1.5, n)
        elif law == "normal":
            w = abs(rng.normal(size=n)) + 1e-8
        else:
            w = .5 ** np.arange(n)
        score = x @ w
        distinct = np.unique(score)
        chosen = np.unique(np.r_[0, len(distinct) - 2,
                                 np.linspace(0, max(0, len(distinct) - 2), 17).astype(int)])
        for j in chosen:
            if len(distinct) == 1 or j < 0 or j >= len(distinct) - 1:
                continue
            theta = (distinct[j] + distinct[j + 1]) / 2
            f = np.where(score > theta, 1.0, -1.0)
            p = min(np.mean(f == 1), np.mean(f == -1))
            assert 2 ** -n <= p <= .5
            L = math.log(1 / p)
            coeff = fwht(f)
            spectral = coeff ** 2
            H = entropy(spectral)
            influences = np.array([np.mean(f != f[index ^ (1 << i)]) for i in range(n)])
            inf = float(sum(influences))
            assert abs(np.dot(degree, spectral) - inf) < 1e-10
            # Positive weights mean f is monotone. Indicator singletons are Ii/2.
            indicator_coeff = fwht((f + 1) / 2)
            identity_error = max(abs(2 * indicator_coeff[1 << i] - influences[i])
                                 for i in range(n))
            report["maximum_indicator_singleton_identity_error"] = max(
                report["maximum_indicator_singleton_identity_error"], float(identity_error))
            assert identity_error < 1e-10
            W1 = sum(indicator_coeff[1 << i] ** 2 for i in range(n))
            assert abs(4 * W1 - np.sum(influences ** 2)) < 1e-10
            assert inf >= 4 * W1 / max(influences) - 1e-10
            assert H <= 300 * p * math.sqrt(n * L) + 1e-10
            report["maximum_H_over_p_sqrt_nL"] = max(
                report["maximum_H_over_p_sqrt_nL"], H / (p * math.sqrt(n * L)))
            for epsilon in [2.0 ** -j for j in range(1, 21)]:
                ns = float(np.dot(spectral, 1 - (1 - 2 * epsilon) ** degree)) / 2
                assert ns <= min(2 * p, 20.5 * p * math.sqrt(epsilon * L)) + 1e-10
                report["maximum_NS_over_p_sqrt_epsilonL"] = max(
                    report["maximum_NS_over_p_sqrt_epsilonL"], ns / (p * math.sqrt(epsilon * L)))
                report["noise_checks"] += 1
            report["ltfs"] += 1


for n in [1, 2, 4, 10, 100, 1000]:
    for A in [0, .1, 1, 3, 10, 100]:
        for _ in range(20):
            u = rng.normal(size=n)
            u *= A / np.linalg.norm(u) if A else 0
            w = 1 + u
            if not np.linalg.norm(w):
                continue
            tau = max(abs(w)) / np.linalg.norm(w)
            assert tau * math.sqrt(n) <= 2 * (1 + A) + 1e-10
            report["l2_regularity_checks"] += 1


A = 20.5 * math.sqrt(2) / (1 - math.exp(-1))
report["analytic_entropy_constant"] = {
    "spectral_tail_A": A,
    "within_level": 4 * A / math.log(2),
    "zero_nonzero_bit": 4 / math.log(2) * (math.sqrt(math.log(2)) + 1 / math.sqrt(math.log(2))),
    "conditional_degree": 8 / (math.e * math.log(2) * math.sqrt(math.log(2)))}
report["analytic_entropy_constant"]["total"] = sum(
    report["analytic_entropy_constant"][key]
    for key in ["within_level", "zero_nonzero_bit", "conditional_degree"])
assert report["analytic_entropy_constant"]["total"] < 300

out = Path(__file__).with_name("regular_biased_ltf_verification.json")
out.write_text(json.dumps(report, indent=2) + "\n")
print(json.dumps(report, indent=2))
