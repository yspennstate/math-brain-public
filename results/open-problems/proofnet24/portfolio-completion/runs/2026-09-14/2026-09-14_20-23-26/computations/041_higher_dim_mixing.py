#!/usr/bin/env python3
"""Exact-arithmetic checks accompanying agents/041.md.

The mathematical proof is in the report. This script independently evaluates
the finite coefficient formulas and constructs tensors attaining the proposed
uniform perturbation threshold; it is not a substitute for the universal proof.
Only Python's standard library is used. Run from the research-session root.
"""

from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import json


def equiprobable(n):
    return [
        [
            [F(0) if k in (i, j) else F(1, n - len({i, j})) for k in range(n)]
            for j in range(n)
        ]
        for i in range(n)
    ]


def validate(p):
    n = len(p)
    for i in range(n):
        for j in range(n):
            assert p[i][j] == p[j][i]
            assert sum(p[i][j]) == 1
            assert min(p[i][j]) >= 0
            assert p[i][j][i] == 0
            assert p[i][j][j] == 0


def norm1(v):
    return sum(map(abs, v))


def subtract(u, v):
    return [a - b for a, b in zip(u, v)]


def coefficient_lipschitz(p):
    n = len(p)
    return max(norm1(subtract(p[a][i], p[a][j]))
               for a in range(n) for i, j in combinations(range(n), 2))


def row_distance(p, q):
    return max(norm1(subtract(p[i][j], q[i][j]))
               for i in range(len(p)) for j in range(i, len(p)))


def quadratic(p, x):
    n = len(p)
    return [sum(p[i][j][k] * x[i] * x[j]
                for i in range(n) for j in range(n)) for k in range(n)]


def matrix_at(p, m):
    n = len(p)
    return [[sum(p[a][i][k] * m[a] for a in range(n))
             for i in range(n)] for k in range(n)]


def delta(a):
    n = len(a)
    return max(sum(abs(a[k][i] - a[k][j]) for k in range(n)) / 2
               for i, j in combinations(range(n), 2))


def sharp_perturbation(n, epsilon):
    """Two parent rows modified on disjoint donor sets, as in report Section 4."""
    p = equiprobable(n)
    common = list(range(3, n))
    b = common[:len(common) // 2]
    d = common[len(common) // 2:]
    assert b and d
    t = epsilon / 2
    assert t <= F(min(len(b), len(d)), n - 2)
    p[0][1][2] += t
    for k in b:
        p[0][1][k] -= t / len(b)
    p[1][0] = p[0][1][:]
    p[0][2][1] += t
    for k in d:
        p[0][2][k] -= t / len(d)
    p[2][0] = p[0][2][:]
    validate(p)
    return p


def cut_constant(p, q):
    """Exact cap coefficient for rational 1/3 <= q < 1/2, via sorted cut rows."""
    assert F(1, 3) <= q < F(1, 2)
    n = len(p)
    best = None
    cases = 0
    for mask in range(1, (1 << n) - 1):
        g = [k for k in range(n) if mask & (1 << k)]
        h = [k for k in range(n) if not mask & (1 << k)]
        for i in g:
            for j in h:
                ds = sorted((sum(p[a][i][k] - p[a][j][k] for k in g)
                             for a in range(n)), reverse=True)
                value = q * (ds[0] + ds[1]) + (1 - 2 * q) * ds[2]
                best = value if best is None else max(best, value)
                cases += 1
    return best, cases


def main():
    records = []
    total_cut_cases = 0
    for n in range(3, 13):
        e = equiprobable(n)
        validate(e)
        lip = coefficient_lipschitz(e)
        assert lip == F(2, n - 2)
        u = [F(1, n)] * n
        assert quadratic(e, u) == u
        # Nonuniform rational point; all matrix entries and deltas are exact.
        m = [F(k + 1, n * (n + 1) // 2) for k in range(n)]
        a = matrix_at(e, m)
        denominator = (n - 1) * (n - 2)
        for k in range(n):
            for i in range(n):
                formula = F(0) if k == i else (1 - m[k]) / (n - 2) - m[i] / denominator
                assert a[k][i] == formula
        expected_delta = F(n - 1, denominator) * (1 - m[0]) - m[1] / denominator
        assert delta(a) == expected_delta
        record = {"n": n, "L_E": str(lip), "delta_nonuniform_m": str(expected_delta)}
        if n >= 5:
            radius = F(n - 4, 2 * (n - 2))
            p = sharp_perturbation(n, radius)
            assert row_distance(p, e) == radius
            assert coefficient_lipschitz(p) == 1
            record.update({"sharp_raw_radius": str(radius), "L_at_radius": "1"})
        if 5 <= n <= 8:
            q = F(2, 5)
            tau, cases = cut_constant(e, q)
            assert tau == (n * q - (n - 1)) / denominator
            total_cut_cases += cases
            record.update({"cap_q": str(q), "tau_E_cap": str(tau), "cut_cases": cases})
        records.append(record)
    # A five-type tensor inside the cut neighborhood but outside raw contraction.
    p = sharp_perturbation(5, F(1, 5))
    assert row_distance(p, equiprobable(5)) == F(1, 5)
    assert coefficient_lipschitz(p) == F(16, 15)
    tau, cases = cut_constant(p, F(2, 5))
    assert tau < F(1, 2)
    total_cut_cases += cases
    result = {
        "status": "all exact assertions passed",
        "arithmetic": "fractions.Fraction; no floating point",
        "equiprobable_dimensions": records,
        "noncontractive_raw_example": {
            "n": 5, "epsilon": "1/5", "L_raw": "16/15", "cap_q": "2/5",
            "tau_cut": str(tau), "cut_cases": cases,
            "modified_parent_rows_one_based": {
                "12": list(map(str, p[0][1])), "13": list(map(str, p[0][2]))
            }
        },
        "total_exact_cut_cases": total_cut_cases,
        "limitations": "Finite checks validate these formulas and examples; the report contains the dimension-uniform proof."
    }
    destination = Path(__file__).with_suffix(".json")
    destination.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"status": result["status"], "cut_cases": total_cut_cases,
                      "raw_example_L": "16/15", "raw_example_tau_at_q_2_5": str(tau),
                      "output": str(destination)}, indent=2))


if __name__ == "__main__":
    main()
