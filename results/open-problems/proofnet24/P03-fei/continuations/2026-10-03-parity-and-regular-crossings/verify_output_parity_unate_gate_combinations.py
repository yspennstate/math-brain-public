"""Independent finite arithmetic checks of parity/influence-vector FEI.

No local imports. All Boolean functions through n=4 and all parity
subsets test the universal rho version. Additional overlapping unate-gate
combinations test exact flip-union and Parseval influence-vector bounds.
Fourier entropy and irrational constants are numerical supplements.
"""
from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np


RNG = np.random.default_rng(2026100211)
COUNTS = dict(universal_truth_functions=0, universal_parity_pairs=0,
              unate_gate_combinations=0, gate_parity_pairs=0,
              unate_gates=0, differently_oriented_combinations=0,
              overlapping_inputs_combinations=0, constant_functions=0)
MAX = dict(entropy_over_universal_target=0.0,
           entropy_over_gate_target=0.0, rho_over_gate_count=0.0)


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


def coordinate_boundaries(f, n):
    f = np.asarray(f, dtype=np.int64)
    if f.ndim == 1:
        f = f[None, :]
    vertices = np.arange(1 << n)
    counts = np.zeros((len(f), n), dtype=np.int64)
    for i in range(n):
        lower = vertices[(vertices & (1 << i)) == 0]
        counts[:, i] = np.sum(f[:, lower] != f[:, lower | (1 << i)], axis=1)
    return counts


def inspect(f, n, subsets, gate_count=None):
    f = np.asarray(f, dtype=np.int64)
    if f.ndim == 1:
        f = f[None, :]
    rows, total = f.shape
    assert total == 1 << n
    b = coordinate_boundaries(f, n)
    boundary = np.sum(b, axis=1)
    walsh = fwht_rows(f)
    assert np.all(np.sum(walsh ** 2, axis=1) == total ** 2)
    spectral = (walsh / total) ** 2
    logs = np.zeros_like(spectral)
    positive = spectral > 0
    logs[positive] = np.log2(spectral[positive])
    entropy = -np.sum(spectral * logs, axis=1)
    rho_squared = np.sum((2 * b) ** 2, axis=1) / total ** 2
    rho = np.sqrt(rho_squared)
    if gate_count is not None:
        assert np.all(np.sum((2 * b) ** 2, axis=1) <= gate_count ** 2 * total ** 2)
        MAX["rho_over_gate_count"] = max(MAX["rho_over_gate_count"], float(np.max(rho / gate_count)))
    COUNTS["constant_functions"] += int(np.count_nonzero(boundary == 0))
    vertices = np.arange(total, dtype=np.int64)
    for T in subsets:
        ell = int(T).bit_count()
        q = n - ell
        parity = np.array([(-1) ** ((int(v) & int(T)).bit_count()) for v in vertices])
        h = f * parity[None, :]
        direct_b = coordinate_boundaries(h, n)
        expected_b = b.copy()
        for i in range(n):
            if T & (1 << i):
                expected_b[:, i] = total // 2 - b[:, i]
        assert np.array_equal(direct_b, expected_b)
        assert np.array_equal(fwht_rows(h), walsh[:, vertices ^ T])
        inf_h = 2 * np.sum(direct_b, axis=1) / total
        assert np.all(inf_h + 3e-12 >= ell - rho * math.sqrt(ell))
        minority_count = np.minimum(np.sum(h == 1, axis=1), np.sum(h == -1, axis=1))
        # Exact Fourier Poincare weaker bound I>=2*minority_probability.
        assert np.all(np.sum(direct_b, axis=1) >= minority_count)
        assert np.all(entropy <= 8 * n * minority_count / total + 3e-11)
        assert np.all(entropy <= 4 * n * inf_h + 3e-11)
        t_rho = ((rho + np.sqrt(rho ** 2 + 1)) / 2) ** 2
        target = 4 * (q + t_rho) * inf_h
        assert np.all(entropy <= target + 3e-11)
        nonconstant_h = inf_h > 0
        if np.any(nonconstant_h):
            MAX["entropy_over_universal_target"] = max(MAX["entropy_over_universal_target"],
                float(np.max(entropy[nonconstant_h] / target[nonconstant_h])))
        if gate_count is None:
            COUNTS["universal_parity_pairs"] += rows
        else:
            t_m = ((gate_count + math.sqrt(gate_count ** 2 + 1)) / 2) ** 2
            gate_target = 4 * (q + t_m) * inf_h
            assert np.all(entropy <= gate_target + 3e-11)
            if np.any(nonconstant_h):
                MAX["entropy_over_gate_target"] = max(MAX["entropy_over_gate_target"],
                    float(np.max(entropy[nonconstant_h] / gate_target[nonconstant_h])))
            COUNTS["gate_parity_pairs"] += rows


def main():
    dimensions = []
    for n in range(0, 5):
        total = 1 << n
        truth_masks = np.arange(1 << total, dtype=np.uint64)
        support = ((truth_masks[:, None] >> np.arange(total, dtype=np.uint64)) & 1).astype(np.int64)
        f = 2 * support - 1
        inspect(f, n, range(total))
        COUNTS["universal_truth_functions"] += len(f)
        dimensions.append(dict(dimension=n, functions=len(f), parity_subsets=total))
    for n in range(2, 13):
        total = 1 << n
        vertices = np.arange(total, dtype=np.int64)
        signs = 2 * ((vertices[:, None] >> np.arange(n)) & 1) - 1
        for m in range(1, 6):
            for trial in range(8):
                gates = []
                orientations = []
                for j in range(m):
                    orientation = int(RNG.integers(0, total))
                    orientations.append(orientation)
                    oriented_signs = signs[vertices ^ orientation]
                    if trial % 2 == 0:
                        weights = RNG.integers(1, 10, size=n)
                        score = oriented_signs @ weights
                        threshold = int(RNG.integers(-n, n + 1))
                        gate = np.where(score >= threshold, 1, -1)
                    else:
                        # Monotone DNF in its own orientation, with all
                        # clauses drawing from the same input-coordinate set.
                        gate_positive = np.zeros(total, dtype=bool)
                        for _ in range(1 + j % 4):
                            clause = RNG.choice(n, size=min(n, 1 + j % 3), replace=False)
                            gate_positive |= np.all(oriented_signs[:, clause] == 1, axis=1)
                        gate = np.where(gate_positive, 1, -1)
                    gate_in_monotone_order = gate[vertices ^ orientation]
                    for i in range(n):
                        lower = vertices[(vertices & (1 << i)) == 0]
                        assert np.all(gate_in_monotone_order[lower] <= gate_in_monotone_order[lower | (1 << i)])
                    gates.append(gate)
                gates = np.stack(gates)
                gate_b = coordinate_boundaries(gates, n)
                assert np.all(np.sum((2 * gate_b) ** 2, axis=1) <= total ** 2)
                gate_walsh = fwht_rows(gates)
                for j in range(m):
                    # Each singleton coefficient differs from Ii by its
                    # gate-specific coordinate orientation sign.
                    for i in range(n):
                        assert abs(int(gate_walsh[j, 1 << i])) == 2 * int(gate_b[j, i])
                truth_table = RNG.choice([-1, 1], size=1 << m)
                gate_index = np.sum(((gates > 0).astype(np.int64) << np.arange(m)[:, None]), axis=0)
                f = truth_table[gate_index]
                combined_b = coordinate_boundaries(f, n)[0]
                assert np.all(combined_b <= np.sum(gate_b, axis=0))
                assert np.sum((2 * combined_b) ** 2) <= m ** 2 * total ** 2
                subsets = sorted({0, total - 1, 1, 3, total // 2 - 1,
                                  *[int(RNG.integers(0, total)) for _ in range(3)]})
                inspect(f, n, subsets, gate_count=m)
                COUNTS["unate_gates"] += m
                COUNTS["unate_gate_combinations"] += 1
                COUNTS["differently_oriented_combinations"] += int(len(set(orientations)) > 1)
                COUNTS["overlapping_inputs_combinations"] += int(m > 1)
    report = dict(status="PASS finite checks; analytic proof separately supplied",
                  dimensions=dimensions, counts=COUNTS, maxima=MAX,
                  exact_checks=["coordinate influence and parity complement identity",
                                "integer Fourier parity permutation",
                                "unate singleton coefficient magnitudes equal physical influences",
                                "unate Parseval influence-vector bound",
                                "pointwise gate flip union",
                                "combined influence-vector squared norm <= gate_count^2"],
                  numerical_checks=["generic H<=8*n*minority_probability and H<=4*n*I",
                                    "universal rho-parity FEI", "unate-gate-count FEI"],
                  entropy_tolerance=3e-11,
                  scope="No ordinary FEI for unmodulated composition; no novelty certificate")
    Path(__file__).with_name("output_parity_unate_gate_combinations_checks.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
