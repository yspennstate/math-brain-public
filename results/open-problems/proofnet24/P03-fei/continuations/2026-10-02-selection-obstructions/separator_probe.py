#!/usr/bin/env python3
"""Audit an unproved separator criterion for the deterministic LTF route.

Conjectural criterion: if A takes values -1,0,+1 and no edge joins A=+1
to A=-1, B=1_{A=0}, then the exact entropy increment of A+zB is O(E B).
This script provides finite evidence only, never a universal certificate.
"""
import argparse
import json
from pathlib import Path

import numpy as np

from verify import fwht, split_statistics


def separator_max(n=3):
    size = 1 << n
    largest = -1.0
    extremizer = None
    accepted = 0
    for code in range(3 ** size):
        tmp = code
        a = np.empty(size, dtype=np.int8)
        for pos in range(size):
            a[pos] = tmp % 3 - 1
            tmp //= 3
        b = (a == 0).astype(np.int8)
        if not np.any(b):
            continue
        admissible = True
        for bit in range(n):
            indices = np.arange(size)
            if np.any(a * a[indices ^ (1 << bit)] == -1):
                admissible = False
                break
        if not admissible:
            continue
        accepted += 1
        row = split_statistics(fwht(a + b), fwht(a - b))
        if row["ratio"] > largest:
            largest = row["ratio"]
            extremizer = {"ternary_truth_table": a.tolist(), "code": code, **row}
    return {"dimension_base": n, "admissible_separator_functions": accepted,
            "largest_ratio": largest, "extremizer": extremizer}


def ltf_samples(n, count, seed):
    rng = np.random.default_rng(seed)
    indices = np.arange(1 << n, dtype=np.uint32)
    bits = 2 * ((indices[:, None] >> np.arange(n)) & 1).astype(float) - 1
    largest = -1.0
    best = None
    nonconstant = 0
    for sample in range(count):
        if sample % 3 == 0:
            weights = rng.uniform(0.1, 1, n)
        elif sample % 3 == 1:
            weights = np.exp(rng.uniform(-6, 0, n))
        else:
            weights = rng.integers(1, 31, n).astype(float)
        weights = np.sort(weights)[::-1]
        sums = bits @ weights
        if sample % 5 == 0:
            threshold = rng.uniform(-1, 1) * np.sum(weights)
        else:
            threshold = rng.normal(0, 1) * np.linalg.norm(weights)
        f = np.where(sums >= threshold, 1, -1)
        if np.all(f == f[0]):
            continue
        nonconstant += 1
        # Split on bit 0, corresponding to a largest defining weight.
        minus = f[::2]
        plus = f[1::2]
        A = (plus + minus) // 2
        B = (plus - minus) // 2
        base_indices = np.arange(len(A))
        for bit in range(n - 1):
            assert not np.any(A * A[base_indices ^ (1 << bit)] == -1)
        assert np.array_equal(B, A == 0)
        row = split_statistics(fwht(plus), fwht(minus))
        if row["influence"] and row["ratio"] > largest:
            largest = row["ratio"]
            best = {"weights": weights.tolist(), "threshold": float(threshold),
                    "sample": sample, **row}
    return {"dimension": n, "samples": count, "nonconstant_samples": nonconstant,
            "seed": seed, "largest_largest_weight_split_ratio": largest,
            "extremizer": best}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    parser.add_argument("--samples", type=int, default=2000)
    args = parser.parse_args()
    result = {"criterion_status": "unproved_not_a_FEI_solution",
              "all_ternary_separators_on_three_bits": separator_max(),
              "weighted_ltf_samples": [ltf_samples(8, args.samples, 6102),
                                       ltf_samples(12, args.samples // 2, 6103)]}
    encoded = json.dumps(result, indent=2) + "\n"
    if args.output:
        args.output.write_text(encoded)
    print(encoded)


if __name__ == "__main__":
    main()
