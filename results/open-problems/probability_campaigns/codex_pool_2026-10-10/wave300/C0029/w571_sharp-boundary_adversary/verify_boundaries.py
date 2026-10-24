"""Small, deterministic checks for the C0029 adversary packet; no store writes."""
from __future__ import annotations

from fractions import Fraction
from itertools import combinations, product
from pathlib import Path
import json
import math
import time

ROOT = Path(__file__).resolve().parent


def rank(rows: list[list[int]]) -> int:
    if not rows:
        return 0
    a = [[Fraction(x) for x in row] for row in rows]
    pivot = 0
    for col in range(len(a[0])):
        found = next((i for i in range(pivot, len(a)) if a[i][col]), None)
        if found is None:
            continue
        a[pivot], a[found] = a[found], a[pivot]
        scale = a[pivot][col]
        a[pivot] = [x / scale for x in a[pivot]]
        for i in range(pivot + 1, len(a)):
            scale = a[i][col]
            a[i] = [x - scale * y for x, y in zip(a[i], a[pivot])]
        pivot += 1
        if pivot == len(a):
            break
    return pivot


def hard_edge(t: float) -> float:
    return -math.expm1(-t - t * t / 2)


def main() -> None:
    started = time.perf_counter()
    gate = {
        "kind": "fresh deterministic CPU gate",
        "max_dimension": 10,
        "max_sign_rows_enumerated_per_dimension": 1024,
        "no_gpu": True,
        "no_external_compute": True,
        "writes": "this worker folder only",
    }
    two_by_two = {"singular": 0, "orthogonal": 0}
    for a, b, c, d in product((-1, 1), repeat=4):
        if a * d == b * c:
            two_by_two["singular"] += 1
        else:
            assert a * b + c * d == 0
            two_by_two["orthogonal"] += 1
    assert two_by_two == {"singular": 8, "orthogonal": 8}

    a4 = [[1, 1, -1, -1], [1, -1, 1, -1], [1, -1, -1, 1]]
    gram = [[sum(x * y for x, y in zip(r, s)) for s in a4] for r in a4]
    assert gram == [[4, 0, 0], [0, 4, 0], [0, 0, 4]]
    assert rank(a4) == 3

    flat_atoms = []
    for n in (2, 4, 6, 8, 10):
        basis: list[list[int]] = []
        for positives in combinations(range(n), n // 2):
            chosen = set(positives)
            row = [1 if i in chosen else -1 for i in range(n)]
            if rank(basis + [row]) > len(basis):
                basis.append(row)
            if len(basis) == n - 1:
                break
        assert len(basis) == n - 1 and rank(basis) == n - 1
        assert all(sum(row) == 0 for row in basis)
        zeros = sum(sum(x) == 0 for x in product((-1, 1), repeat=n))
        assert zeros == math.comb(n, n // 2)
        atom = Fraction(zeros, 2**n)
        assert atom >= Fraction(1, n + 1)
        flat_atoms.append({"n": n, "rank": n - 1, "zero_count": zeros,
                           "total": 2**n, "atom": str(atom), "basis": basis})

    delta_checks = []
    comparison_checks = 0
    for delta in (1.0, 0.5, 0.1, 0.01, 0.001, 0.0001, 0.000001):
        t = math.sqrt(delta) / 2
        excess = hard_edge((1 + delta) * t) - t
        lower = delta**1.5 / 6
        assert excess >= lower - 1e-15
        delta_checks.append({"delta": delta, "t": t, "excess": excess,
                             "proved_lower_bound": lower,
                             "excess_over_lower_bound": excess / lower})
        for j in range(65):
            u = j / 16
            h = hard_edge(u)
            shifted = hard_edge((1 + delta) * u)
            assert h <= shifted + 1e-15
            assert shifted <= (1 + delta) * h + 1e-15
            assert h >= u - u**3 / 3 - 1e-15
            comparison_checks += 1

    result = {
        "gate": gate,
        "B01": {"matrices": 16, "counts": two_by_two,
                "scaled_singular_values": {"0": "1/2", "2": "1/2"}},
        "B02": {"delta_checks": delta_checks, "comparison_checks": comparison_checks,
                "scope": "numerical checks of an analytic scalar-CDF obstruction; not matrix simulations"},
        "B03": {"witness_gram": gram, "flat_atoms": flat_atoms,
                "n4_gaussian_projection_atom_at_zero": 0,
                "n4_actual_rademacher_projection_atom_at_zero": "3/8"},
        "B04": {"n": 1, "t": 1,
                "actual_gaussian_cdf": math.erf(1 / math.sqrt(2)),
                "hard_edge_limiting_cdf": hard_edge(1),
                "actual_right_derivative_at_zero": math.sqrt(2 / math.pi),
                "limiting_right_derivative_at_zero": 1},
        "elapsed_seconds": time.perf_counter() - started,
        "verdict": "PASS",
        "formal_check": False,
        "independent_mathematical_review": "pending w572",
    }
    assert abs(result["B04"]["actual_gaussian_cdf"] - result["B04"]["hard_edge_limiting_cdf"]) > 0.09
    (ROOT / "MEASUREMENTS.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"verdict": result["verdict"], "elapsed_seconds": result["elapsed_seconds"],
                      "B01_matrices": 16, "B02_comparison_checks": comparison_checks,
                      "B03_dimensions": len(flat_atoms), "n4_atom": "3/8"}))


if __name__ == "__main__":
    main()
