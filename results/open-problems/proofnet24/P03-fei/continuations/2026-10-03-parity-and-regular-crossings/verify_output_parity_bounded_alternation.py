"""Exact finite audit of output-parity bounded-alternation FEI.

No local imports. All Boolean functions through dimension four and all
their parity subsets are checked. Alternation and constant-label path
lengths, parity Fourier permutation, and coordinate influence identities
are integer calculations. Entropy/cotangent inequalities are numerical
supplements, not proofs or novelty certificates.
"""
from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np


RNG = np.random.default_rng(2026100210)
COUNTS = dict(truth_functions=0, parity_pairs=0, monotone_functions=0,
              unate_partial_bound_pairs=0, endpoint_score_cases=0,
              coordinate_orientation_cases=0, zero_weight_score_cases=0,
              constant_g_cases=0, constant_h_pairs=0)
MAX = dict(entropy_over_general_target=0.0, entropy_over_unate_target=0.0)
DIMENSIONS = []


def fwht_rows(values):
    a = np.array(values, dtype=np.int64, copy=True)
    width = 1
    while width < a.shape[1]:
        blocks = a.reshape(a.shape[0], -1, 2 * width)
        left = blocks[:, :, :width].copy()
        right = blocks[:, :, width:].copy()
        blocks[:, :, :width] = left + right
        blocks[:, :, width:] = left - right
        width *= 2
    return a


def inspect_rows(g, n, parity_subsets, scalar_crossing_counts=None):
    g = np.asarray(g, dtype=np.int64)
    if g.ndim == 1:
        g = g[None, :]
    rows, total = g.shape
    assert total == 1 << n
    assert np.all((g == -1) | (g == 1))
    vertices = np.arange(total, dtype=np.int64)
    predecessors = [[v ^ (1 << j) for j in range(n) if v & (1 << j)]
                    for v in range(total)]
    alternation = np.zeros((rows, total), dtype=np.int64)
    for v in range(1, total):
        previous = predecessors[v]
        alternation[:, v] = np.max(alternation[:, previous] + (g[:, previous] != g[:, v, None]), axis=1)
    # Every ascending path can be extended to a bottom-to-top path. The
    # maximum number of sign changes is therefore this exact DP value.
    m = alternation[:, -1]
    if scalar_crossing_counts is not None:
        assert np.all(m <= scalar_crossing_counts)
    boundary_by_coordinate = np.zeros((rows, n), dtype=np.int64)
    monotone = np.ones(rows, dtype=bool)
    for j in range(n):
        lower = vertices[(vertices & (1 << j)) == 0]
        upper = lower | (1 << j)
        boundary_by_coordinate[:, j] = np.sum(g[:, lower] != g[:, upper], axis=1)
        monotone &= np.all(g[:, lower] <= g[:, upper], axis=1)
    base_boundary = np.sum(boundary_by_coordinate, axis=1)
    walsh_g = fwht_rows(g)
    assert np.all(np.sum(walsh_g ** 2, axis=1) == total ** 2)
    spectral = (walsh_g.astype(float) / total) ** 2
    entropy = np.zeros(rows)
    positive = spectral > 0
    logs = np.zeros_like(spectral)
    logs[positive] = np.log2(spectral[positive])
    entropy = -np.sum(spectral * logs, axis=1)
    COUNTS["truth_functions"] += rows
    COUNTS["monotone_functions"] += int(np.count_nonzero(monotone))
    COUNTS["constant_g_cases"] += int(np.count_nonzero(m == 0))
    for T in parity_subsets:
        t = int(T).bit_count()
        q = n - t
        # +/- coordinate convention differs from the bit Walsh convention
        # by the same global (-1)^|T|, which does not affect squared masses.
        parity = np.array([(-1) ** ((int(v) & T).bit_count()) for v in vertices], dtype=np.int64)
        h = g * parity[None, :]
        expected_walsh = walsh_g[:, vertices ^ T]
        walsh_h = fwht_rows(h)
        assert np.array_equal(walsh_h, expected_walsh)
        expected_boundary = base_boundary.copy()
        for j in range(n):
            if T & (1 << j):
                expected_boundary += total // 2 - 2 * boundary_by_coordinate[:, j]
        actual_boundary = np.zeros(rows, dtype=np.int64)
        for j in range(n):
            lower = vertices[(vertices & (1 << j)) == 0]
            upper = lower | (1 << j)
            count = np.sum(h[:, lower] != h[:, upper], axis=1)
            expected = (total // 2 - boundary_by_coordinate[:, j]
                        if T & (1 << j) else boundary_by_coordinate[:, j])
            assert np.array_equal(count, expected)
            actual_boundary += count
        assert np.array_equal(actual_boundary, expected_boundary)
        # Counts <= m+q edges, hence <= m+q+1 vertices, for each h label.
        constant_depth = np.ones((rows, total), dtype=np.int64)
        for v in range(1, total):
            previous = predecessors[v]
            candidates = constant_depth[:, previous] * (h[:, previous] == h[:, v, None])
            constant_depth[:, v] = 1 + np.max(candidates, axis=1)
        max_vertices = np.max(constant_depth, axis=1)
        assert np.all(max_vertices <= m + q + 1)
        inf_h = 2 * actual_boundary / total
        nonconstant_h = actual_boundary > 0
        assert np.all(entropy[~nonconstant_h] < 3e-11)
        target = 4 / np.tan(math.pi / (2 * (m + q + 2))) ** 2 * inf_h
        assert np.all(entropy <= target + 3e-11)
        if np.any(nonconstant_h):
            MAX["entropy_over_general_target"] = max(MAX["entropy_over_general_target"],
                float(np.max(entropy[nonconstant_h] / target[nonconstant_h])))
        if t >= 2:
            selected = monotone & nonconstant_h
            assert np.all(entropy[monotone] <= (q + 2) * inf_h[monotone] + 3e-11)
            COUNTS["unate_partial_bound_pairs"] += int(np.count_nonzero(monotone))
            if np.any(selected):
                MAX["entropy_over_unate_target"] = max(MAX["entropy_over_unate_target"],
                    float(np.max(entropy[selected] / ((q + 2) * inf_h[selected]))))
        if T == total - 1:
            assert np.array_equal(2 * actual_boundary, n * total - 2 * base_boundary)
            if n <= 1:
                assert np.all(entropy < 3e-11)
            else:
                assert np.all(entropy[monotone] <= 2 * inf_h[monotone] + 3e-11)
        COUNTS["parity_pairs"] += rows
        COUNTS["constant_h_pairs"] += int(np.count_nonzero(~nonconstant_h))


def main():
    for n in range(0, 5):
        total = 1 << n
        truth_masks = np.arange(1 << total, dtype=np.uint64)
        support = ((truth_masks[:, None] >> np.arange(total, dtype=np.uint64)) & 1).astype(np.int64)
        g = 2 * support - 1
        inspect_rows(g, n, range(total))
        DIMENSIONS.append(dict(dimension=n, truth_functions=len(g), parity_subsets=total))
    for n in range(5, 13):
        total = 1 << n
        vertices = np.arange(total, dtype=np.int64)
        signs = 2 * ((vertices[:, None] >> np.arange(n)) & 1) - 1
        functions = []
        crossing_bounds = []
        for trial in range(12):
            weights = RNG.integers(1, 15, size=n)
            if trial % 4 == 0:
                weights[trial % n] = 0
                COUNTS["zero_weight_score_cases"] += 1
            score = signs @ weights
            attained = np.unique(score)
            crossings = RNG.choice(attained, min(1 + trial % 5, len(attained)), replace=False)
            g = np.ones(total, dtype=np.int64)
            for crossing in crossings:
                right_at_point = bool(RNG.integers(0, 2))
                single = np.where(score >= crossing if right_at_point else score > crossing, 1, -1)
                g *= single
            functions.append(g)
            crossing_bounds.append(len(crossings))
            COUNTS["endpoint_score_cases"] += 1
            # Coordinate flips produce the same entropy/influence after
            # adopting the flipped order. Explicitly transform back before
            # checking the ascending-path premise, rather than assuming it
            # for the untransformed arbitrary signed score.
            orientation = int(RNG.integers(0, total))
            signed_g = g[vertices ^ orientation]
            assert np.array_equal(signed_g[vertices ^ orientation], g)
            assert np.array_equal(fwht_rows(signed_g[None, :]) ** 2, fwht_rows(g[None, :]) ** 2)
            for j in range(n):
                assert np.count_nonzero(signed_g != signed_g[vertices ^ (1 << j)]) == np.count_nonzero(g != g[vertices ^ (1 << j)])
            COUNTS["coordinate_orientation_cases"] += 1
        subsets = sorted({0, total - 1, 1, 3, total // 2 - 1,
                          *[int(RNG.integers(0, total)) for _ in range(3)]})
        inspect_rows(np.stack(functions), n, subsets, np.array(crossing_bounds))
    # The sharp two-dimensional monotone example has all coefficient
    # magnitudes 1/2, entropy2 and full-parity physical influence1.
    g = np.array([-1, 1, 1, 1], dtype=np.int64)
    assert np.all(np.abs(fwht_rows(g[None, :])) == 2)
    parity = np.array([1, -1, -1, 1])
    h = g * parity
    undirected_boundary = sum(np.count_nonzero(h[np.array([v for v in range(4) if not v & (1 << j)])]
                              != h[np.array([v | (1 << j) for v in range(4) if not v & (1 << j)])])
                              for j in range(2))
    assert undirected_boundary == 2
    report = dict(status="PASS finite validation; analytic proof separately supplied",
                  dimensions=DIMENSIONS, counts=COUNTS, maxima=MAX,
                  sharp_unate_example=dict(dimension=2, truth_values=g.tolist(), entropy=2, full_parity_influence=1),
                  exact_checks=["all-function maximum path sign alternation",
                                "constant-output path vertices <= m+q+1",
                                "Fourier coefficient parity permutation",
                                "each coordinate influence complemented exactly on T",
                                "I(h)=|T|+I(g)-2*sum_T I_i(g)",
                                "full T specialization and coordinate orientations"],
                  numerical_checks=["cotangent FEI bound", "sharp unate partial-parity bound"],
                  entropy_tolerance=3e-11,
                  scope="Finite checks; no ordinary FEI for g or novelty certificate")
    Path(__file__).with_name("output_parity_bounded_alternation_checks.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
