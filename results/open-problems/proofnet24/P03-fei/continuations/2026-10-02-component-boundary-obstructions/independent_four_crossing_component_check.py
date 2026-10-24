"""Independent exact check of the four-crossing boundary obstruction.

Integer scores reconstruct all components. Integer Walsh numerators
verify the full Fourier magnitude formula. Fractions verify all physical
influences. Large asymptotic examples use exact symbolic formulas only.
"""
from __future__ import annotations

from fractions import Fraction
import json
import math
from pathlib import Path

import numpy as np


def walsh(values: np.ndarray) -> np.ndarray:
    result = values.astype(np.int32, copy=True)
    width = 1
    while width < len(result):
        view = result.reshape(-1, 2 * width)
        left, right = view[:, :width].copy(), view[:, width:].copy()
        view[:, :width], view[:, width:] = left + right, left - right
        width *= 2
    return result


def exact_formulas(k: int, n: int):
    p, q = Fraction(1, 1 << k), Fraction(1, 1 << n)
    majority = Fraction(n * math.comb(n, n // 2), 1 << n)
    influence = 2 * k * p * (1 - q) + 2 * p * n * q
    positive = 2 + 2 * (k - 2) * p + 2 * (k + n) * p * q
    negative = 2 * k * p * (1 - q) + 2 * p * majority
    return p, q, majority, influence, positive, negative


def entropy_term(probability: float) -> float:
    return -probability * math.log2(probability) if probability else 0.0


def truth_table_case(k: int, n: int) -> dict:
    dimension, size, scale = k + n, 1 << (k + n), 1 << n
    coarse_scale = 2 * n + 4
    indices = np.arange(size, dtype=np.int64)
    weights = [coarse_scale * (1 << j) * scale for j in range(k)]
    weights += [scale + (1 << (n - i)) for i in range(1, n + 1)]
    scores = np.zeros(size, dtype=np.int64)
    for coordinate, weight in enumerate(weights):
        scores += weight * (2 * ((indices >> coordinate) & 1) - 1)
    t_num = scale - (1 << (n + 1 - n // 2)) + 1
    crossings = [0, coarse_scale * scale + t_num - 1,
                 coarse_scale * scale + t_num + 1, 2 * coarse_scale * scale]
    assert all(a < b for a, b in zip(crossings, crossings[1:]))
    assert all(not np.any(scores == crossing) for crossing in crossings)
    assert len(np.unique(scores)) == size
    components = np.searchsorted(np.array(crossings, dtype=np.int64), scores)
    counts = np.bincount(components, minlength=5)
    assert np.all(counts > 0)
    assert counts[2] == 1
    coarse_pattern = 1 << (k - 1)
    fine_pattern = (1 << (n // 2)) - 1
    point = coarse_pattern | (fine_pattern << k)
    coarse_selected = (indices & ((1 << k) - 1)) == coarse_pattern
    predicted_negative = coarse_selected & (indices != point)
    positive_label = (components % 2) == 0
    assert np.array_equal(~positive_label, predicted_negative)
    influence_num = positive_num = negative_num = 0
    positive_join_num = negative_join_num = 0
    for coordinate in range(dimension):
        flipped = indices ^ (1 << coordinate)
        other_positive = positive_label[flipped]
        different_component = components != components[flipped]
        different_sign = positive_label != other_positive
        influence_num += int(np.count_nonzero(different_sign))
        selected = positive_label.astype(np.int8) + other_positive.astype(np.int8)
        positive_num += int(np.sum(selected[different_component]))
        negative_num += int(np.sum((2 - selected)[different_component]))
        positive_join_num += int(np.count_nonzero(
            different_component & positive_label & other_positive))
        negative_join_num += int(np.count_nonzero(
            different_component & ~positive_label & ~other_positive))
    p, q, majority, expected_i, expected_pos, expected_neg = exact_formulas(k, n)
    assert Fraction(influence_num, size) == expected_i
    assert Fraction(positive_num, size) == expected_pos
    assert Fraction(negative_num, size) == expected_neg
    assert positive_num == influence_num + 2 * positive_join_num
    assert negative_num == influence_num + 2 * negative_join_num
    truth = 2 * positive_label.astype(np.int32) - 1
    coefficients = walsh(truth)
    assert coefficients[0] == size - 2 * (scale - 1)
    assert np.all(np.abs(coefficients[1:(1 << k)]) == 2 * (scale - 1))
    assert np.all(np.abs(coefficients[(1 << k):]) == 2)
    # Check the independently reconstructed integer spectrum's degree sum.
    degrees = np.array([int(i).bit_count() for i in indices], dtype=np.int64)
    walsh_influence = Fraction(int(np.sum(
        coefficients.astype(np.int64) ** 2 * degrees)), size * size)
    assert walsh_influence == expected_i
    squared = coefficients.astype(float) ** 2 / (size * size)
    entropy = float(-np.sum(squared[squared > 0] * np.log2(squared[squared > 0])))
    predicted_h = entropy_term(float((1 - 2 * p * (1 - q)) ** 2))
    predicted_h += ((1 << k) - 1) * entropy_term(float(4 * p * p * (1 - q) ** 2))
    predicted_h += (1 << k) * ((1 << n) - 1) * entropy_term(float(4 * p * p * q * q))
    assert abs(entropy - predicted_h) < 2e-11
    assert entropy <= (4 + 1.5 * math.log2(math.e)) * float(expected_i) + 2e-11
    return dict(k=k, N=n, dimension=dimension, vertices=size,
                component_sizes=counts.tolist(), I=str(expected_i),
                B_positive=str(expected_pos), B_negative=str(expected_neg),
                min_component_ratio=float(min(expected_pos, expected_neg) / expected_i),
                entropy=entropy, entropy_over_influence=entropy / float(expected_i),
                integer_score_and_walsh_checks="PASS")


def main() -> None:
    truth_cases = [truth_table_case(k, n) for k in [2, 3, 4]
                   for n in [2, 4, 6, 8, 10, 12]]
    truth_cases.append(truth_table_case(2, 16))
    symbolic = []
    for k in range(2, 9):
        n = 1 << (2 * k)
        p, q, majority, influence, positive, negative = exact_formulas(k, n)
        assert 2 * majority * majority >= n
        assert positive >= 2
        assert negative * negative >= 2
        assert influence <= 2 * p * (k + 1)
        symbolic.append(dict(k=k, N=n, dimension=k + n,
                             exact_symbolic_inequalities="PASS",
                             I_approx=float(influence),
                             B_positive_approx=float(positive),
                             B_negative_approx=float(negative),
                             min_component_ratio_approx=float(min(positive, negative) / influence),
                             proved_ratio_lower_bound_approx=(1 << k) / (math.sqrt(2) * (k + 1))))
    report = dict(status="PASS", crossings=4,
                  scope="Exact finite checks support the written asymptotic proof; no FEI counterexample",
                  truth_table_cases=truth_cases,
                  truth_table_case_count=len(truth_cases),
                  truth_table_vertex_total=sum(case["vertices"] for case in truth_cases),
                  exact_symbolic_sequence=symbolic,
                  entropy_tolerance=2e-11,
                  dependencies="Python stdlib and NumPy; no local helper imports")
    target = Path(__file__).with_name("independent_four_crossing_component_checks.json")
    target.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({key: value for key, value in report.items()
                      if key not in {"truth_table_cases", "exact_symbolic_sequence"}}, indent=2))
    print(json.dumps(symbolic, indent=2))


if __name__ == "__main__":
    main()
