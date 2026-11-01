#!/usr/bin/env python3
"""Exact independent enumeration of the five-crossing obstruction.

All weighted scores and all counts are integers. No floating threshold
comparisons, research helper imports, or third-party packages are used.
"""

from bisect import bisect_left
from fractions import Fraction
from math import comb
from pathlib import Path
import json


def check_dimension(n):
    assert n >= 2 and n % 2 == 0
    d = n // 2
    scale = 1 << n
    small_weights = [scale + (1 << (n - i)) for i in range(1, n + 1)]
    big_weight = (n + 2) * scale - 1
    central_point = (1 << d) - 1
    central_score = scale - (1 << (n + 1 - d)) + 1
    endpoints = [
        -big_weight + central_score - 1,
        -big_weight + central_score + 1,
        0,
        big_weight + central_score - 1,
        big_weight + central_score + 1,
    ]
    assert all(a < b for a, b in zip(endpoints, endpoints[1:]))

    vertex_count = 1 << (n + 1)
    scores = [0] * vertex_count
    labels = [0] * vertex_count
    for vertex in range(vertex_count):
        small_vertex = vertex & (scale - 1)
        z = 1 if vertex & scale else -1
        small_score = sum(
            weight if small_vertex & (1 << i) else -weight
            for i, weight in enumerate(small_weights)
        )
        score = z * big_weight + small_score
        assert score not in endpoints
        label = -1 if bisect_left(endpoints, score) % 2 == 0 else 1
        expected = z * (-1 if small_vertex == central_point else 1)
        assert label == expected
        scores[vertex] = score
        labels[vertex] = label
    assert len(set(scores)) == vertex_count

    # Reconstruct the actual maximal attained-score components, rather
    # than assuming their identity from the proposed proof.
    component = [-1] * vertex_count
    run_labels = []
    previous_label = None
    run = -1
    for vertex in sorted(range(vertex_count), key=scores.__getitem__):
        label = labels[vertex]
        if label != previous_label:
            run += 1
            run_labels.append(label)
            previous_label = label
        component[vertex] = run
    assert run_labels == [-1, 1, -1, 1, -1, 1]

    cut_edges = 0
    positive_component_edges = 0
    negative_component_edges = 0
    for vertex in range(vertex_count):
        for coordinate in range(n + 1):
            bit = 1 << coordinate
            if vertex & bit:
                continue
            other = vertex | bit
            first = labels[vertex]
            second = labels[other]
            cut_edges += first != second
            if first != second:
                positive_component_edges += 1
                negative_component_edges += 1
            elif component[vertex] != component[other]:
                if first == 1:
                    positive_component_edges += 2
                else:
                    negative_component_edges += 2

    actual_influence = Fraction(cut_edges, scale)
    positive_sum = Fraction(positive_component_edges, scale)
    negative_sum = Fraction(negative_component_edges, scale)
    expected_influence = Fraction(scale + 2 * n, scale)
    expected_sum = Fraction(scale + n * comb(n, d) + n, scale)
    assert actual_influence == expected_influence
    assert positive_sum == negative_sum == expected_sum
    return {
        "small_dimension": n,
        "full_dimension": n + 1,
        "vertices": vertex_count,
        "actual_sign_jumps": len(run_labels) - 1,
        "positive_components": run_labels.count(1),
        "negative_components": run_labels.count(-1),
        "actual_influence_exact": str(actual_influence),
        "both_component_sums_exact": str(positive_sum),
        "ratio_exact": str(positive_sum / actual_influence),
        "ratio_approximate": float(positive_sum / actual_influence),
    }


def main():
    enumerated = [check_dimension(n) for n in range(2, 15, 2)]
    formula_cases = []
    for n in [20, 50, 100, 200, 500, 1000, 2000]:
        scale = 1 << n
        ratio = Fraction(
            scale + n * comb(n, n // 2) + n,
            scale + 2 * n,
        )
        # The proven elementary lower bound squared is n/8.
        assert ratio * ratio >= Fraction(n, 8)
        formula_cases.append({
            "small_dimension": n,
            "ratio_approximate": float(ratio),
            "elementary_lower_bound_squared": str(Fraction(n, 8)),
        })
    result = {
        "status": "PASS",
        "scope": "Exact attained-score and component-boundary enumeration; asymptotic divergence is proved in the accompanying note.",
        "dependencies": "Python standard library only",
        "enumerated_dimensions": enumerated,
        "enumerated_vertices_total": sum(case["vertices"] for case in enumerated),
        "closed_formula_checks": formula_cases,
    }
    output = Path(__file__).with_name("global_component_boundary_obstruction_checks.json")
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({
        "status": result["status"],
        "exact_cases": len(enumerated),
        "enumerated_vertices_total": result["enumerated_vertices_total"],
        "output": str(output),
    }))


if __name__ == "__main__":
    main()
