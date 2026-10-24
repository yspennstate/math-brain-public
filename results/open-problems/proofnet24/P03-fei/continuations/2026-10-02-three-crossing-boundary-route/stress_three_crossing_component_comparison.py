"""Exact finite stress of a conjectured three-crossing boundary comparison.

This is NOT a proof of a dimension-independent comparison. Positive
integer weights determine an exact graph on attained scores. Cuts occur
only between adjacent attained scores, so every retained component is
nonempty and every crossing is a genuine sign jump.
"""
from __future__ import annotations

from fractions import Fraction
import itertools
import json
import math
from pathlib import Path

import numpy as np

rng = np.random.default_rng(20261022)


def score_graph(weights):
    n = len(weights)
    indices = np.arange(1 << n, dtype=np.int64)
    scores = np.zeros(1 << n, dtype=np.int64)
    for coordinate, weight in enumerate(weights):
        scores += int(weight) * (2 * ((indices >> coordinate) & 1) - 1)
    attained, inverse = np.unique(scores, return_inverse=True)
    edges = np.zeros((len(attained), len(attained)), dtype=np.int64)
    for coordinate in range(n):
        lower = indices[(indices & (1 << coordinate)) == 0]
        upper = lower | (1 << coordinate)
        assert np.all(scores[lower] < scores[upper])
        np.add.at(edges, (inverse[lower], inverse[upper]), 1)
    prefix = np.pad(edges.cumsum(axis=0).cumsum(axis=1), ((1, 0), (1, 0)))
    return attained, prefix


def rectangles(prefix, left0, left1, right0, right1):
    return (prefix[left1, right1] - prefix[left0, right1]
            - prefix[left1, right0] + prefix[left0, right0])


def cut_patterns(u, m):
    total = math.comb(u - 1, m)
    limit = 50000 if m == 3 else 10000
    if total <= limit:
        return np.array(list(itertools.combinations(range(1, u), m)), dtype=np.int64), True
    samples = np.array([np.sort(rng.choice(np.arange(1, u), m, replace=False))
                        for _ in range(2500)], dtype=np.int64)
    # Include cuts isolating central individual scores and two narrow bands.
    center = u // 2
    extras = []
    for start in [1, max(1, center - m), min(u - m, center), u - m]:
        if 0 < start and start + m - 1 < u:
            extras.append(tuple(range(start, start + m)))
    if extras:
        samples = np.vstack([samples, np.array(extras, dtype=np.int64)])
    return np.unique(samples, axis=0), False


def test_family(name, weights, record):
    attained, prefix = score_graph(weights)
    u, n = len(attained), len(weights)
    row = dict(name=name, weights=list(map(int, weights)), dimension=n,
               attained_score_count=u, crossings=[])
    for m in range(1, min(5, u - 1) + 1):
        cuts, exhaustive = cut_patterns(u, m)
        ends = np.hstack([np.zeros((len(cuts), 1), dtype=np.int64), cuts,
                          np.full((len(cuts), 1), u, dtype=np.int64)])
        influence = np.zeros(len(cuts), dtype=np.int64)
        positive = np.zeros(len(cuts), dtype=np.int64)
        negative = np.zeros(len(cuts), dtype=np.int64)
        joins_positive = np.zeros(len(cuts), dtype=np.int64)
        joins_negative = np.zeros(len(cuts), dtype=np.int64)
        odd_middle = np.zeros(len(cuts), dtype=np.int64)
        for first in range(m + 1):
            for second in range(first + 1, m + 1):
                count = rectangles(prefix, ends[:, first], ends[:, first + 1],
                                   ends[:, second], ends[:, second + 1])
                first_positive, second_positive = first % 2 == 0, second % 2 == 0
                if first_positive != second_positive:
                    influence += count
                positive += (int(first_positive) + int(second_positive)) * count
                negative += (2 - int(first_positive) - int(second_positive)) * count
                if m == 3:
                    if (first, second) == (0, 2):
                        joins_positive += count
                    if (first, second) == (1, 3):
                        joins_negative += count
                    if (first, second) in {(0, 3), (1, 2)}:
                        odd_middle += count
        assert np.all(influence > 0)
        assert np.all(positive >= influence)
        assert np.all(negative >= influence)
        minimum = np.minimum(positive, negative)
        # Counts are small enough that floating division only selects the
        # candidate maximum; the reported ratio and any violations are exact.
        index = int(np.argmax(minimum / influence))
        ratio = Fraction(int(minimum[index]), int(influence[index]))
        source = dict(name=name, weights=list(map(int, weights)), dimension=n,
                      cut_indices=cuts[index].tolist(),
                      crossing_midpoints_twice=[int(attained[c - 1] + attained[c])
                                               for c in cuts[index]],
                      attained_scores=attained.tolist(),
                      unnormalized_I=int(influence[index]),
                      unnormalized_B_positive=int(positive[index]),
                      unnormalized_B_negative=int(negative[index]),
                      ratio=str(ratio), ratio_approx=float(ratio))
        key = str(m)
        previous = record["maxima"].get(key)
        if previous is None or ratio > Fraction(previous["ratio"]):
            record["maxima"][key] = source
        violations2 = int(np.count_nonzero(minimum > 2 * influence))
        row["crossings"].append(dict(m=m, cases=len(cuts), exhaustive_gaps=exhaustive,
                                      max_ratio=str(ratio), violations_of_D2=violations2))
        record["pattern_count"] += len(cuts)
        record["by_crossing_count"][key] = record["by_crossing_count"].get(key, 0) + len(cuts)
        if m == 3 and violations2:
            bad = int(np.flatnonzero(minimum > 2 * influence)[0])
            record["three_crossing_D2_witnesses"].append(dict(
                weights=list(map(int, weights)), cut_indices=cuts[bad].tolist(),
                unnormalized_I=int(influence[bad]),
                unnormalized_B_positive=int(positive[bad]),
                unnormalized_B_negative=int(negative[bad])))
        if m == 3:
            middle_i = joins_positive + joins_negative + odd_middle
            trace_num = (2 * joins_positive + odd_middle) * (2 * joins_negative + odd_middle)
            trace_den = middle_i * influence
            assert np.all(trace_den > 0)
            trace_index = int(np.argmax(trace_num / trace_den))
            trace_ratio = Fraction(int(trace_num[trace_index]), int(trace_den[trace_index]))
            if record["max_trace_ratio"] is None or trace_ratio > Fraction(record["max_trace_ratio"]["ratio"]):
                record["max_trace_ratio"] = dict(name=name, weights=list(map(int, weights)),
                    cut_indices=cuts[trace_index].tolist(), ratio=str(trace_ratio),
                    ratio_approx=float(trace_ratio),
                    I_unnormalized=int(influence[trace_index]),
                    middle_I_unnormalized=int(middle_i[trace_index]),
                    positive_joins_unnormalized=int(joins_positive[trace_index]),
                    negative_joins_unnormalized=int(joins_negative[trace_index]),
                    odd_middle_unnormalized=int(odd_middle[trace_index]))
            trace_violations = int(np.count_nonzero(trace_num > 2 * trace_den))
            record["trace_D2_violation_count"] += trace_violations
            row["crossings"][-1]["trace_D2_violations"] = trace_violations
    record["families"].append(row)


def main():
    record = dict(status="finite checks completed", seed=20261022,
                  scope="Exact integer stress only; no asymptotic theorem",
                  pattern_count=0, by_crossing_count={}, maxima={}, families=[],
                  three_crossing_D2_witnesses=[], max_trace_ratio=None,
                  trace_D2_violation_count=0)
    for n in range(2, 11):
        scale = 1 << n
        families = [
            ("equal", [1] * n),
            ("binary-lacunary", [1 << i for i in range(n)]),
            ("near-uniform-unique", [scale + (1 << i) for i in range(n)]),
            ("one-dominant", [2 * n] + [1] * (n - 1)),
            ("two-dominant", [8 * n, 4 * n] + [1] * (n - 2)),
        ]
        for trial in range(4):
            families.append((f"random-{trial}", rng.integers(1, 128, n).tolist()))
        for name, weights in families:
            test_family(f"n{n}-{name}", weights, record)
    target = Path(__file__).with_name("three_crossing_component_stress_results.json")
    target.write_text(json.dumps(record, indent=2) + "\n")
    summary = {key: value for key, value in record.items() if key not in {"families", "maxima"}}
    summary["family_count"] = len(record["families"])
    summary["maxima"] = {m: {key: val for key, val in example.items()
                              if key not in {"attained_scores"}}
                          for m, example in record["maxima"].items()}
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
