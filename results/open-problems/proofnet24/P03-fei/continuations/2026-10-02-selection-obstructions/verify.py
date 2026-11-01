#!/usr/bin/env python3
"""Independent finite Fourier checks for the FEI research checkpoint.

These numerical checks complement analytic proofs. They do not verify a
universal conjecture. Requires only numpy from the execution environment.
"""
import argparse
import json
import math
from pathlib import Path

import numpy as np


def fwht(v):
    """Uniformly normalized Walsh transform; bit 1 denotes input +1."""
    c = np.asarray(v, dtype=float).copy()
    size = len(c)
    assert size and not (size & (size - 1))
    for exponent in range(size.bit_length() - 1):
        step = 1 << exponent
        c = c.reshape(-1, 2 * step)
        left = c[:, :step].copy()
        right = c[:, step:].copy()
        c[:, :step] = left + right
        c[:, step:] = left - right
        c = c.reshape(-1)
    return c / size


def entropy(c):
    p = np.asarray(c) ** 2
    nonzero = p > 0
    return float(-np.dot(p[nonzero], np.log2(p[nonzero])))


def binary_entropy(p):
    p = np.asarray(p, dtype=float)
    answer = np.zeros_like(p)
    inner = (p > 0) & (p < 1)
    answer[inner] = -p[inner] * np.log2(p[inner]) - (1 - p[inner]) * np.log2(1 - p[inner])
    return answer


def influences(c):
    n = len(c).bit_length() - 1
    indices = np.arange(len(c))
    p = c * c
    return np.array([np.sum(p[(indices & (1 << bit)) != 0]) for bit in range(n)])


def split_statistics(a, b):
    full = np.concatenate(((a + b) / 2, (a - b) / 2))
    delta = entropy(full) - (entropy(a) + entropy(b)) / 2
    w = (a * a + b * b) / 2
    nz = w > 0
    q = (a[nz] - b[nz]) ** 2 / (4 * w[nz])
    r = a[nz] ** 2 / (2 * w[nz])
    exact = float(np.dot(w[nz], 1 + binary_entropy(q) - binary_entropy(r)))
    surrogate = float(np.dot(w[nz], binary_entropy(q)))
    influence = float(np.sum((a - b) ** 2) / 4)
    assert abs(exact - delta) < 1e-10
    assert surrogate <= delta + 1e-10
    assert delta <= 2 * surrogate + 1e-10
    return {"entropy_increment": delta, "influence": influence,
            "ratio": delta / influence if influence else None,
            "surrogate": surrogate}


def tribes_outer(k):
    n = 3 * k
    indices = np.arange(1 << n, dtype=np.uint64)
    positive = np.zeros(len(indices), dtype=bool)
    for block in range(k):
        positive |= ((indices >> (3 * block)) & 7) == 7
    f = np.where(positive, 1, -1)
    minus = f.copy()
    minus[7] = -1  # minimal positive point with first block all +1
    return f, minus


def check_family(max_k=6):
    output = []
    for k in range(1, max_k + 1):
        f, minus = tribes_outer(k)
        row = split_statistics(fwht(f), fwht(minus))
        eps = 8.0 ** (-k)
        c = math.log2(7) / 4
        rigorous_lower = c * k - 2 * k * eps * math.log2(7)
        rigorous_upper = (c * k - 2 * k * eps * math.log2(7)
                          + (1 - eps) * math.log2(10)
                          + eps * (6 * k + 1) + math.log2(math.e) + 4)
        assert abs(row["influence"] - eps) < 1e-12
        assert rigorous_lower <= row["ratio"] <= rigorous_upper
        r_majority = 64 ** k
        # The product proof, not floating point lgamma, establishes this bound.
        majority_influence_bound = 1 / math.sqrt(r_majority + 1)
        assert majority_influence_bound < eps
        row.update({"k": k, "dimension_outer": 3 * k + 1,
                    "analytic_lower": rigorous_lower,
                    "analytic_upper": rigorous_upper,
                    "majority_size": 2 * r_majority + 1,
                    "dimension_after_substitution": 3 * k * (2 * r_majority + 1) + 1,
                    "majority_leaf_influence_upper": majority_influence_bound,
                    "special_is_unique_max_by_proved_bound": True})
        output.append(row)
    return output


def check_composition_small():
    """Full truth-table check of cancellation using majority of three.

    The small substitution proves the exact identity computationally but
    does not give unique maximum influence. The larger explicit majority
    construction is covered by the analytic product bound above.
    """
    f, minus = tribes_outer(1)
    outer = np.concatenate((minus, f))
    outer_c = fwht(outer)
    n_full = 10  # three old bits replaced by three-bit majority, plus z
    inputs = np.arange(1 << n_full, dtype=np.uint64)
    old = np.zeros(len(inputs), dtype=np.uint64)
    for block in range(3):
        block_bits = (inputs >> (3 * block)) & 7
        popcounts = np.array([int(value).bit_count() for value in block_bits])
        old |= (popcounts >= 2).astype(np.uint64) << block
    z = (inputs >> 9) & 1
    table = outer[old + (z << 3)]
    composed = fwht(table)
    majority = np.array([-1 if i.bit_count() < 2 else 1 for i in range(8)])
    h_majority = entropy(fwht(majority))
    expected_h = entropy(outer_c) + np.sum(influences(outer_c)[:3]) * h_majority
    assert abs(entropy(composed) - expected_h) < 1e-10
    stats_outer = split_statistics(fwht(f), fwht(minus))
    stats_composed = split_statistics(fwht(table[1 << 9:]), fwht(table[:1 << 9]))
    assert abs(stats_composed["entropy_increment"] - stats_outer["entropy_increment"]) < 1e-10
    assert abs(stats_composed["influence"] - stats_outer["influence"]) < 1e-10
    expected_inf = np.repeat(influences(outer_c)[:3] / 2, 3)
    actual_inf = influences(composed)
    assert np.max(abs(actual_inf[:9] - expected_inf)) < 1e-12
    assert abs(actual_inf[9] - influences(outer_c)[3]) < 1e-12
    return {"dimension": n_full, "entropy": entropy(composed),
            "entropy_composition_expected": expected_h,
            "outer_special_increment": stats_outer["entropy_increment"],
            "composed_special_increment": stats_composed["entropy_increment"],
            "outer_special_influence": stats_outer["influence"],
            "composed_special_influence": stats_composed["influence"]}


def exhaustive_four_bits():
    n = 4
    size = 1 << n
    truth_codes = np.arange(1 << size, dtype=np.uint32)
    tables = 1 - 2 * ((truth_codes[:, None] >> np.arange(size)) & 1).astype(float)
    coefficients = tables.copy()
    for bit in range(n):
        step = 1 << bit
        for start in range(0, size, 2 * step):
            a = coefficients[:, start:start + step].copy()
            b = coefficients[:, start + step:start + 2 * step].copy()
            coefficients[:, start:start + step] = a + b
            coefficients[:, start + step:start + 2 * step] = a - b
    coefficients /= size
    p = coefficients ** 2
    h = -np.sum(p * np.log2(np.where(p > 0, p, 1)), axis=1)
    degree = np.array([i.bit_count() for i in range(size)])
    total_influence = p @ degree
    best_coordinate_ratio = np.full(len(tables), np.inf)
    max_identity_error = 0.0
    for bit in range(n):
        S = np.array([i for i in range(size) if not ((i >> bit) & 1)])
        a = coefficients[:, S] + coefficients[:, S + (1 << bit)]
        b = coefficients[:, S] - coefficients[:, S + (1 << bit)]
        pa, pb = a * a, b * b
        ha = -np.sum(pa * np.log2(np.where(pa > 0, pa, 1)), axis=1)
        hb = -np.sum(pb * np.log2(np.where(pb > 0, pb, 1)), axis=1)
        delta = h - (ha + hb) / 2
        inf = np.sum(p[:, S + (1 << bit)], axis=1)
        w = (pa + pb) / 2
        q = np.divide((a - b) ** 2, 4 * w, out=np.zeros_like(w), where=w > 0)
        r = np.divide(pa, 2 * w, out=np.zeros_like(w), where=w > 0)
        exact = np.sum(w * (1 + binary_entropy(q) - binary_entropy(r)), axis=1)
        max_identity_error = max(max_identity_error, float(np.max(abs(exact - delta))))
        ratios = np.divide(delta, inf, out=np.full(len(tables), np.inf), where=inf > 0)
        best_coordinate_ratio = np.minimum(best_coordinate_ratio, ratios)
    relevant = total_influence > 0
    idx = int(np.argmax(np.where(relevant, best_coordinate_ratio, -1)))
    expected = 12 - 4.5 * math.log2(3)
    assert abs(best_coordinate_ratio[idx] - expected) < 1e-12
    assert max_identity_error < 1e-12
    return {"functions_checked": len(tables), "dimension": n,
            "max_min_coordinate_ratio": float(best_coordinate_ratio[idx]),
            "extremizer_truth_code": int(truth_codes[idx]),
            "and3_exact_ratio": expected,
            "max_split_identity_error": max_identity_error}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    parser.add_argument("--max-k", type=int, default=6)
    args = parser.parse_args()
    result = {"claim_status": "classical_FEI_not_solved",
              "family": check_family(args.max_k),
              "balanced_composition": check_composition_small(),
              "all_four_bit_functions": exhaustive_four_bits()}
    encoded = json.dumps(result, indent=2) + "\n"
    if args.output:
        args.output.write_text(encoded)
    print(encoded)


if __name__ == "__main__":
    main()
