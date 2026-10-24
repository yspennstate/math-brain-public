"""Exact exhaustive three-crossing stress for integer weights 1..8.

All dimensions through eight are covered modulo coordinate permutation
and common integer rescaling. This finite domain is not all real weights.
Every triple of nonempty attained-score gaps is checked. No local imports.
"""
from __future__ import annotations

from fractions import Fraction
import itertools
import json
import math
from pathlib import Path

import numpy as np


def main():
    report = dict(status="PASS finite domain only", max_dimension=8,
                  weight_values=list(range(1, 9)), families=0, triple_cuts=0,
                  max_component_ratio=None, max_trace_ratio=None,
                  violations_trace_constant2=0, violations_component_constant3=0,
                  dimensions=[],
                  scope="All positive integer weights 1..8 modulo permutations/rescaling; not an asymptotic proof")
    for n in range(1, 9):
        row = dict(dimension=n, families=0, triple_cuts=0)
        indices = np.arange(1 << n, dtype=np.int64)
        signs = np.array([2 * ((indices >> j) & 1) - 1 for j in range(n)], dtype=np.int64)
        edge_indices = [(indices[(indices & (1 << j)) == 0], j) for j in range(n)]
        for weights in itertools.combinations_with_replacement(range(1, 9), n):
            if math.gcd(*weights) != 1:
                continue
            scores = np.array(weights, dtype=np.int64) @ signs
            attained, inverse = np.unique(scores, return_inverse=True)
            u = len(attained)
            if u < 4:
                continue
            edges = np.zeros((u, u), dtype=np.int64)
            for lower, j in edge_indices:
                upper = lower | (1 << j)
                assert np.all(scores[lower] < scores[upper])
                np.add.at(edges, (inverse[lower], inverse[upper]), 1)
            p = np.pad(edges.cumsum(axis=0).cumsum(axis=1), ((1, 0), (1, 0)))
            cuts = np.array(list(itertools.combinations(range(1, u), 3)), dtype=np.int64)
            a, b, c = cuts[:, 0], cuts[:, 1], cuts[:, 2]
            e01 = p[a, b] - p[a, a]
            e03 = p[a, u] - p[a, c]
            e12 = p[b, c] - p[a, c] - p[b, b] + p[a, b]
            e23 = p[c, u] - p[b, u] - p[c, c] + p[b, c]
            jpos = p[a, c] - p[a, b]
            jneg = p[b, u] - p[a, u] - p[b, c] + p[a, c]
            influence = e01 + e03 + e12 + e23
            assert np.all(influence > 0)
            middle_odd = e03 + e12
            middle = jpos + jneg + middle_odd
            positive = influence + 2 * jpos
            negative = influence + 2 * jneg
            minimum = np.minimum(positive, negative)
            trace_num = (2 * jpos + middle_odd) * (2 * jneg + middle_odd)
            trace_den = middle * influence
            assert np.all(trace_den > 0)
            comparisons = [
                ("max_component_ratio", minimum, influence),
                ("max_trace_ratio", trace_num, trace_den),
            ]
            for key, numerator, denominator in comparisons:
                best = int(np.argmax(numerator / denominator))
                ratio = Fraction(int(numerator[best]), int(denominator[best]))
                if report[key] is None or ratio > Fraction(report[key]["ratio"]):
                    report[key] = dict(weights=list(weights), dimension=n,
                        cut_indices=cuts[best].tolist(),
                        crossing_midpoints_twice=[int(attained[t - 1] + attained[t])
                                                   for t in cuts[best]],
                        ratio=str(ratio), ratio_approx=float(ratio),
                        I_unnormalized=int(influence[best]),
                        middle_I_unnormalized=int(middle[best]),
                        J_positive_unnormalized=int(jpos[best]),
                        J_negative_unnormalized=int(jneg[best]),
                        odd_middle_unnormalized=int(middle_odd[best]))
            report["violations_trace_constant2"] += int(np.count_nonzero(trace_num > 2 * trace_den))
            report["violations_component_constant3"] += int(np.count_nonzero(minimum > 3 * influence))
            row["families"] += 1
            row["triple_cuts"] += len(cuts)
        report["dimensions"].append(row)
        report["families"] += row["families"]
        report["triple_cuts"] += row["triple_cuts"]
        print(json.dumps(row), flush=True)
    target = Path(__file__).with_name("exhaustive_small_weights_three_crossing_results.json")
    target.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
