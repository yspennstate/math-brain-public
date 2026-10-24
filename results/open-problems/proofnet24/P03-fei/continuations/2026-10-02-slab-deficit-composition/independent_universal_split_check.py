"""Independent all-Boolean audit of the universal split-deficit lemma.

Integer Walsh numerators verify the exact identities. Entropy checks use
double precision with an explicit numerical tolerance and are not proofs.
"""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np


def walsh(x: np.ndarray) -> np.ndarray:
    y = x.astype(np.int32, copy=True)
    width = 1
    while width < y.shape[1]:
        view = y.reshape(y.shape[0], -1, 2 * width)
        left = view[:, :, :width].copy()
        right = view[:, :, width:].copy()
        view[:, :, :width] = left + right
        view[:, :, width:] = left - right
        width *= 2
    return y


def entropy_from_numerators(c: np.ndarray, denominator: int) -> np.ndarray:
    p = c.astype(np.float64) ** 2 / denominator
    terms = np.zeros_like(p)
    np.log2(p, out=terms, where=p > 0)
    return -(p * terms).sum(axis=1)


def binary_entropy(q: np.ndarray) -> np.ndarray:
    a = np.zeros_like(q)
    b = np.zeros_like(q)
    np.log2(q, out=a, where=q > 0)
    np.log2(1 - q, out=b, where=q < 1)
    return -q * a - (1 - q) * b


def main() -> None:
    report = {"status": "PASS", "scope": "Every Boolean function through n=4, every pivot", "dimensions": []}
    totals = dict(functions=0, splits=0, high_influence=0, beta_zero_high=0, alpha_one=0,
                  alpha_one_nonconstant_B=0, alpha_zero=0)
    maxima = dict(delta_over_nu_high=0.0, delta_over_conditional_entropy=0.0,
                  empty_entropy_over_delta=0.0)
    tolerance = 2e-11
    for n in range(5):
        size = 1 << n
        ids = np.arange(1 << size, dtype=np.uint32)
        inputs = np.arange(size, dtype=np.uint32)
        truth = (2 * ((ids[:, None] >> inputs[None, :]) & 1).astype(np.int32) - 1)
        full = walsh(truth)
        full_h = entropy_from_numerators(full, size * size)
        degree = np.array([int(i).bit_count() for i in inputs], dtype=np.int64)
        full_i_num = (full.astype(np.int64) ** 2 * degree[None, :]).sum(axis=1)
        row = dict(n=n, functions=len(ids), splits=len(ids) * n)
        totals["functions"] += len(ids)
        for pivot in range(n):
            minus_idx = inputs[(inputs & (1 << pivot)) == 0]
            plus_idx = minus_idx | (1 << pivot)
            fm, fp = truth[:, minus_idx], truth[:, plus_idx]
            a = (fp + fm) // 2
            b = (fp - fm) // 2
            m = size // 2
            a_sum = a.sum(axis=1).astype(np.int64)
            b_sum = b.sum(axis=1).astype(np.int64)
            alpha_num = (b * b).sum(axis=1).astype(np.int64)
            nu_num = alpha_num * m - b_sum * b_sum
            assert np.all(np.abs(b_sum) <= alpha_num)
            assert np.all(np.abs(a_sum) <= m - alpha_num)
            assert np.all(nu_num >= alpha_num * (m - alpha_num))
            cm, cp = walsh(fm), walsh(fp)
            restricted_degree = np.array([i.bit_count() for i in range(m)], dtype=np.int64)
            im = (cm.astype(np.int64) ** 2 * restricted_degree[None, :]).sum(axis=1)
            ip = (cp.astype(np.int64) ** 2 * restricted_degree[None, :]).sum(axis=1)
            # All terms are multiplied by the common denominator 4*m*m.
            influence_gap_num = full_i_num - 2 * (im + ip)
            assert np.array_equal(influence_gap_num, 4 * m * alpha_num)
            sm, sp = fm.sum(axis=1).astype(np.int64), fp.sum(axis=1).astype(np.int64)
            variance_gap_num = 2 * (sm * sm + sp * sp) - (sm + sp) ** 2
            assert np.array_equal(variance_gap_num, 4 * b_sum * b_sum)
            assert np.array_equal(influence_gap_num - variance_gap_num, 4 * nu_num)
            delta_h = full_h - (entropy_from_numerators(cm, m * m)
                                + entropy_from_numerators(cp, m * m)) / 2
            ca, cb = cm + cp, cp - cm
            pa, pb = ca.astype(np.float64) ** 2 / (4 * m * m), cb.astype(np.float64) ** 2 / (4 * m * m)
            pair_mass = pa + pb
            q = np.divide(pb, pair_mass, out=np.zeros_like(pb), where=pair_mass > 0)
            conditional = (pair_mass * binary_entropy(q)).sum(axis=1)
            assert np.all(delta_h <= 2 * conditional + tolerance)
            ratio = np.divide(delta_h, conditional, out=np.zeros_like(delta_h), where=conditional > tolerance)
            maxima["delta_over_conditional_entropy"] = max(maxima["delta_over_conditional_entropy"], float(ratio.max()))
            high = 2 * alpha_num > m
            alpha_one = alpha_num == m
            nu = nu_num / (m * m)
            assert np.all(delta_h[high] <= 14 * nu[high] + tolerance)
            ratio = np.divide(delta_h, nu, out=np.zeros_like(delta_h), where=high & (nu > 0))
            maxima["delta_over_nu_high"] = max(maxima["delta_over_nu_high"], float(ratio.max()))
            assert np.all(np.abs(delta_h[alpha_one]) <= tolerance)
            low = ~high
            assert np.all(2 * nu_num[low] >= alpha_num[low] * m)
            delta = (m - alpha_num) / m
            empty_entropy = pair_mass[:, 0] * binary_entropy(q[:, 0])
            high_with_delta = high & (delta > 0)
            assert np.all(empty_entropy[high_with_delta] < 2 * delta[high_with_delta] + tolerance)
            ratio = np.divide(empty_entropy, delta, out=np.zeros_like(delta), where=high_with_delta)
            maxima["empty_entropy_over_delta"] = max(maxima["empty_entropy_over_delta"], float(ratio.max()))
            nonempty_entropy = conditional - empty_entropy
            assert np.all(nonempty_entropy[high] <= nu[high] + delta[high] + tolerance)
            totals["splits"] += len(ids)
            totals["high_influence"] += int(high.sum())
            totals["beta_zero_high"] += int((high & (b_sum == 0)).sum())
            totals["alpha_one"] += int(alpha_one.sum())
            totals["alpha_one_nonconstant_B"] += int((alpha_one & (np.abs(b_sum) < m)).sum())
            totals["alpha_zero"] += int((alpha_num == 0).sum())
        report["dimensions"].append(row)
    report["totals"] = totals
    report["observed_maxima"] = maxima
    report["entropy_tolerance"] = tolerance
    report["exact_checks"] = ["signed derivative mean and A mean bounds", "nu >= alpha(1-alpha)",
                               "influence gap alpha", "variance gap beta^2", "I-Var gap nu",
                               "low-alpha nu >= alpha/2"]
    report["numerical_checks"] = ["Delta <= 2 conditional bit entropy", "high-alpha Delta <= 14 nu",
                                   "alpha=1 Delta=0", "empty entropy <2 delta", "nonempty entropy <=nu+delta"]
    target = Path(__file__).with_name("independent_universal_split_checks.json")
    target.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
