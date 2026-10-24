#!/usr/bin/env python3
"""Deterministic numerical countersearch beyond the proved p,q family.

This is evidence only.  It samples six unrelated positive backbone weights
and real Rayleigh specializations for all ten spoke pairs.
"""

import json
from pathlib import Path

import numpy as np


def is_forest(n, edges):
    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for u, v in edges:
        ru, rv = find(u), find(v)
        if ru == rv:
            return False
        parent[ru] = rv
    return True


def main():
    rng = np.random.default_rng(20261003)
    backbone = [(0, j) for j in (2, 3, 4)] + [(1, j) for j in (2, 3, 4)]
    spokes = [(5, i) for i in range(5)]
    allowed = [[] for _ in range(32)]
    for smask in range(32):
        sedges = [spokes[k] for k in range(5) if smask >> k & 1]
        for bmask in range(64):
            bedges = [backbone[k] for k in range(6) if bmask >> k & 1]
            if is_forest(6, bedges + sedges):
                allowed[smask].append(bmask)

    def coefficients(weights):
        monomial = np.ones(64)
        for bmask in range(64):
            monomial[bmask] = np.prod(
                [weights[k] for k in range(6) if bmask >> k & 1]
            )
        return np.array(
            [sum(monomial[bmask] for bmask in allowed[smask]) for smask in range(32)]
        )

    def rayleigh_values(coeff, i, j, points):
        remaining = [k for k in range(5) if k not in (i, j)]
        pieces = [np.zeros(len(points)) for _ in range(4)]
        for smask, value in enumerate(coeff):
            kind = ((smask >> i) & 1) + 2 * ((smask >> j) & 1)
            term = np.full(len(points), value)
            for column, k in enumerate(remaining):
                if smask >> k & 1:
                    term *= points[:, column]
            pieces[kind] += term
        a, b, c, d = pieces
        return b * c - a * d

    pairs = [(i, j) for i in range(5) for j in range(i + 1, 5)]
    best = (float("inf"), None, None, None)
    weight_cases, points_per_pair = 120, 30_000
    negative = None
    for _ in range(weight_cases):
        weights = 10 ** rng.uniform(-2, 2, 6)
        coeff = coefficients(weights)
        scales = 10 ** rng.uniform(-1, 3, (points_per_pair, 1))
        points = rng.normal(size=(points_per_pair, 3)) * scales
        for pair in pairs:
            values = rayleigh_values(coeff, *pair, points)
            index = int(np.argmin(values))
            candidate = float(values[index])
            if candidate < best[0]:
                best = (candidate, weights.copy(), pair, points[index].copy())
            if candidate < -1e-6:
                negative = best
                break
        if negative is not None:
            break

    report = {
        "status": "NEGATIVE_FOUND" if negative is not None else "NO_NEGATIVE_FOUND",
        "proof_status": "NUMERICAL_EVIDENCE_ONLY",
        "seed": 20261003,
        "weight_cases": weight_cases,
        "points_per_pair": points_per_pair,
        "pairs_per_weight_case": len(pairs),
        "total_rayleigh_evaluations": weight_cases * points_per_pair * len(pairs),
        "weight_range_log10": [-2, 2],
        "point_scale_range_log10": [-1, 3],
        "smallest_observed_rayleigh": best[0],
        "witness_weights": best[1].tolist(),
        "witness_pair": list(best[2]),
        "witness_remaining_variables": best[3].tolist(),
    }
    out = Path(__file__).with_name("theta_arbitrary_weight_search_results.json")
    out.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
