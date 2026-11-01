"""Small exhaustive dependence checks; not a test of asymptotic FPP exponents."""
from __future__ import annotations

import heapq
import itertools
import json
import math
import pathlib
import time
from fractions import Fraction

ROOT = pathlib.Path(__file__).resolve().parents[1]
GATE = json.loads((ROOT / "compute_gate.json").read_text(encoding="utf-8"))
START = time.perf_counter()


def shortest(adjacency, source, target):
    dist = {source: 0}
    queue = [(0, source)]
    while queue:
        value, node = heapq.heappop(queue)
        if value != dist[node]:
            continue
        if node == target:
            return value
        for neighbor, weight in adjacency[node]:
            candidate = value + weight
            if candidate < dist.get(neighbor, math.inf):
                dist[neighbor] = candidate
                heapq.heappush(queue, (candidate, neighbor))
    raise AssertionError("disconnected test graph")


def variance(total, squares, count):
    return Fraction(squares, count) - Fraction(total, count) ** 2


def ladder(n):
    horizontal = [[(2*x+y, 2*(x+1)+y) for x in range(n)] for y in (0, 1)]
    edges = horizontal[0] + horizontal[1] + [(2*x, 2*x+1) for x in range(n+1)]
    count = 2 ** len(edges)
    assert count <= GATE["max_configurations"]
    totals = [0] * 7
    squares = [0] * 7
    cross = 0
    departures = [0, 0]
    for j, weights in enumerate(itertools.product((1, 2), repeat=len(edges))):
        if j % 128 == 0 and time.perf_counter() - START > GATE["max_wall_seconds"]:
            raise SystemExit("compute gate exhausted; no asymptotic claim permitted")
        adjacency = [[] for _ in range(2*(n+1))]
        for (left, right), weight in zip(edges, weights):
            adjacency[left].append((right, weight))
            adjacency[right].append((left, weight))
        f1 = shortest(adjacency, 0, 2*n)
        f2 = shortest(adjacency, 1, 2*n+1)
        g1, g2 = sum(weights[:n]), sum(weights[n:2*n])
        d1, d2 = g1-f1, g2-f2
        assert 0 <= d1 <= n and 0 <= d2 <= n
        values = (f1, f2, g1, g2, d1, d2, f1-f2)
        for i, value in enumerate(values):
            totals[i] += value
            squares[i] += value*value
        cross += f1*f2
        departures[0] += d1 != 0
        departures[1] += d2 != 0
    assert totals[0] == totals[1] and squares[0] == squares[1]
    assert totals[2] == totals[3] and squares[2] == squares[3]
    assert squares[4] == squares[5] and departures[0] == departures[1]
    var_f = variance(totals[0], squares[0], count)
    var_g = variance(totals[2], squares[2], count)
    var_diff = variance(totals[6], squares[6], count)
    cov = Fraction(cross, count) - Fraction(totals[0]*totals[1], count*count)
    p = Fraction(departures[0], count)
    delta2 = Fraction(squares[4], count)
    assert var_g == Fraction(n, 4)  # independent horizontal sums
    assert var_diff == 2*var_f-2*cov  # exact dependence identity
    assert cov > 0 and var_diff != 2*var_f  # naive decoupling is falsified
    checks = []
    for label, delta in [("actual L2 error", math.sqrt(float(delta2))),
                         ("n sqrt(p) certificate", n*math.sqrt(float(p)))]:
        s = math.sqrt(float(var_f))
        lower = 2*max(s-2*delta, 0)**2
        upper = 2*(s+2*delta)**2
        assert lower-1e-12 <= float(var_diff) <= upper+1e-12
        checks.append({"certificate": label, "lower": lower, "upper": upper})
    return {"n": n, "edge_count": len(edges), "environments": count,
            "var_f_exact": str(var_f), "var_g_exact": str(var_g),
            "covariance_exact": str(cov), "var_difference_exact": str(var_diff),
            "departure_probability_exact": str(p), "error_second_moment_exact": str(delta2),
            "difference_variance_ratio": float(var_diff/(2*var_f)),
            "corrected_bounds": checks,
            "naive_independence_verdict": "FAIL", "transfer_verdict": "PASS"}


def common_shock(n):
    p = Fraction(1, n)  # b=1/2, q=2(1-b)=1
    var_f = n*n*p*(1-p)
    assert var_f == n-1
    return {"n": n, "p_exact": str(p), "var_f_exact": str(var_f),
            "var_difference_exact": "0", "naive_prediction_exact": str(2*var_f),
            "counterexample": "exact common shock, not an iid FPP construction"}


def main():
    cases = [ladder(3), ladder(4)]
    count = sum(case["environments"] for case in cases)
    assert count <= GATE["max_configurations"]
    result = {"command": "python -X utf8 tests/verify_transfer.py",
              "exhaustive_environments": count,
              "finite_graph_cases": cases,
              "common_shock_cases": [common_shock(n) for n in (16, 64, 256)],
              "naive_decoupling_failures": len(cases),
              "corrected_transfer_passes": len(cases),
              "elapsed_seconds": time.perf_counter()-START,
              "formal_proof": False, "parent_problem_solved": False,
              "limitations": "Atomic finite ladders check the coupling algebra only; they do not test continuous-law exponent existence."}
    (ROOT / "measurements.json").write_text(json.dumps(result, indent=2)+"\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
