#!/usr/bin/env python3
"""Finite audit of monotone erosion and split-increment continuity.

The divergent separator family needs huge majority gates and is proved
analytically. The small erosion test below checks the same construction's
Booleanity, monotonicity, and absence of direct +/− edges independently.
"""
import json
import math
from pathlib import Path

import numpy as np

from verify import binary_entropy, fwht, split_statistics, tribes_outer


def eroded_small(k=2, majority_size=3):
    assert majority_size % 2 == 1
    old_n = 3 * k
    dimension = old_n * majority_size
    indices = np.arange(1 << dimension, dtype=np.uint32)
    outer_indices = np.zeros(len(indices), dtype=np.uint32)
    majority_margin = np.zeros(len(indices), dtype=bool)
    mask = (1 << majority_size) - 1
    popcount = np.array([i.bit_count() for i in range(mask + 1)])
    for block in range(old_n):
        counts = popcount[(indices >> (majority_size * block)) & mask]
        outer_indices |= (counts > majority_size // 2).astype(np.uint32) << block
        majority_margin |= abs(2 * counts - majority_size) == 1
    f, minus = tribes_outer(k)
    outer_A = (f + minus) // 2
    A = outer_A[outer_indices].astype(np.int8)
    original_B = (A == 0).astype(np.int8)
    P, N = A == 1, A == -1
    P_eroded, N_eroded = P.copy(), N.copy()
    for bit in range(dimension):
        neighbor = A[indices ^ (1 << bit)]
        P_eroded &= neighbor == 1
        N_eroded &= neighbor == -1
    eroded_A = P_eroded.astype(np.int8) - N_eroded.astype(np.int8)
    eroded_B = (eroded_A == 0).astype(np.int8)
    changed = A != eroded_A
    assert np.all(~changed | majority_margin)
    assert np.all(original_B <= eroded_B)
    for bit in range(dimension):
        neighbors = eroded_A[indices ^ (1 << bit)]
        assert not np.any(eroded_A * neighbors == -1)
        lower = (indices & (1 << bit)) == 0
        assert np.all(eroded_A[lower] <= neighbors[lower])
        plus = eroded_A + eroded_B
        minustable = eroded_A - eroded_B
        assert np.all(plus[lower] <= plus[indices[lower] ^ (1 << bit)])
        assert np.all(minustable[lower] <= minustable[indices[lower] ^ (1 << bit)])
    old_stats = split_statistics(fwht(A + original_B), fwht(A - original_B))
    new_stats = split_statistics(fwht(eroded_A + eroded_B), fwht(eroded_A - eroded_B))
    outer_stats = split_statistics(fwht(f), fwht(minus))
    assert abs(old_stats["entropy_increment"] - outer_stats["entropy_increment"]) < 1e-10
    delta = float(np.mean(changed))
    assert abs(new_stats["influence"] - old_stats["influence"] - delta) < 1e-12
    return {"k": k, "majority_size": majority_size, "base_dimension": dimension,
            "points_checked": len(indices), "added_zero_mass": delta,
            "original_increment": old_stats["entropy_increment"],
            "eroded_increment": new_stats["entropy_increment"],
            "original_pivotal_mass": old_stats["influence"],
            "eroded_pivotal_mass": new_stats["influence"],
            "all_monotonicity_edges_checked": True, "no_direct_sign_edges": True}


def continuity_checks():
    rng = np.random.default_rng(6302)
    results = []
    for n in [8, 12, 16]:
        size = 1 << n
        table = rng.choice(np.array([-1, 1]), size=size)
        modified = table.copy()
        # A single point modification suffices for a nontrivial, small bound.
        modified[int(rng.integers(size))] *= -1
        first = split_statistics(fwht(table[size // 2:]), fwht(table[:size // 2]))
        second = split_statistics(fwht(modified[size // 2:]), fwht(modified[:size // 2]))
        p = 1 / size
        t = 2 * math.sqrt(p)
        bound = 2 * (t + float(binary_entropy(np.array(t))))
        difference = abs(first["entropy_increment"] - second["entropy_increment"])
        assert difference <= bound
        results.append({"dimension": n, "disagreement_probability": p,
                        "actual_increment_change": difference,
                        "dimension_free_bound": bound})
    return results


result = {"claim_status": "separator_condition_refuted_analytically_FEI_open",
          "small_constructive_erosion": eroded_small(),
          "continuity_examples": continuity_checks(),
          "uniform_analytic_error_constant": 22 * math.sqrt(2) / 64}
encoded = json.dumps(result, indent=2) + "\n"
Path(__file__).with_name("separator_verification.json").write_text(encoded)
print(encoded)
