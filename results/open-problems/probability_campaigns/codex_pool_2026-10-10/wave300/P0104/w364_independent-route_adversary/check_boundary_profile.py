"""Exact, bounded arithmetic checks for the P0104 boundary-profile obstruction.

No randomness, network, external stores, or subprocesses. Writes only beside this file.
This is a reproducibility check, not an independent referee certificate.
"""
from collections import Counter
from fractions import Fraction
import csv
import heapq
import itertools
import json
from pathlib import Path
import time

ROOT = Path(__file__).resolve().parent
GATE = {
    "purpose": "exact four-edge path-composition counterexample",
    "max_assignments": 16,
    "max_vertices_per_graph": 16,
    "max_completions_per_assignment": 2,
    "max_single_edge_checks": 64,
    "max_elapsed_seconds": 10,
    "processes": 1,
    "gpu": False,
    "random_samples": 0,
    "writes_confined_to": "worker folder",
}


def edge(a, b):
    return tuple(sorted((a, b)))


def shortest_path(weights, completion):
    vertices = list(itertools.product(range(-1, 3), repeat=2))
    assert len(vertices) <= GATE["max_vertices_per_graph"]
    graph = {v: [] for v in vertices}
    for x, y in vertices:
        for q in ((x + 1, y), (x, y + 1)):
            if q in graph:
                w = weights.get(edge((x, y), q), completion)
                graph[(x, y)].append((q, w))
                graph[q].append(((x, y), w))
    costs = {(0, 0): 0}
    todo = [(0, (0, 0))]
    while todo:
        cost, vertex = heapq.heappop(todo)
        if cost != costs[vertex]:
            continue
        if vertex == (1, 1):
            return cost
        for q, w in graph[vertex]:
            candidate = cost + w
            if candidate < costs.get(q, 10**9):
                costs[q] = candidate
                heapq.heappush(todo, (candidate, q))
    raise AssertionError("Disconnected graph")


def mean(values):
    return Fraction(sum(values), len(values))


def variance(values):
    m = mean(values)
    return mean([Fraction(x) ** 2 for x in values]) - m**2


def main():
    started = time.monotonic()
    output = ROOT / "measurements"
    output.mkdir(exist_ok=True)
    (output / "compute_gate.json").write_text(
        json.dumps(GATE, indent=2) + "\n", encoding="utf-8"
    )
    rows = []
    dijkstra_checks = 0
    forcing_checks = 0
    selected_geodesic_false_positives = 0
    s, t, u, v = (0, 0), (1, 1), (1, 0), (0, 1)
    for a1, a2, b1, b2 in itertools.product((1, 2), repeat=4):
        assert len(rows) < GATE["max_assignments"]
        assert time.monotonic() - started < GATE["max_elapsed_seconds"]
        paired = min(a1 + b1, a2 + b2)
        scalar = min(a1, a2) + min(b1, b2)
        local = {
            edge(s, u): a1,
            edge(s, v): a2,
            edge(u, t): b1,
            edge(v, t): b2,
        }
        checks = [shortest_path(local, w) for w in (1, 2)]
        assert len(checks) <= GATE["max_completions_per_assignment"]
        assert checks == [paired, paired], (local, paired, checks)
        dijkstra_checks += len(checks)
        routes = ((edge(s, u), edge(u, t)), (edge(s, v), edge(v, t)))
        for test_edge in local:
            assert forcing_checks < GATE["max_single_edge_checks"]
            low = dict(local)
            high = dict(local)
            low[test_edge], high[test_edge] = 1, 2
            low_value = shortest_path(low, 2)
            high_value = shortest_path(high, 2)
            minimizing_low_routes = [
                route for route in routes if sum(low[e] for e in route) == low_value
            ]
            assert minimizing_low_routes
            forced_low_pivotal = all(test_edge in route for route in minimizing_low_routes)
            assert high_value - low_value == int(forced_low_pivotal)
            # A chosen optimal path can contain an edge whose finite difference is zero.
            selected_contains = test_edge in minimizing_low_routes[0]
            if selected_contains and not forced_low_pivotal:
                selected_geodesic_false_positives += 1
            forcing_checks += 1
        rows.append({
            "a1": a1, "a2": a2, "b1": b1, "b2": b2,
            "true_time": paired, "scalar_stitch": scalar,
            "matching_penalty": paired - scalar,
            "dijkstra_min_completion": checks[0],
            "dijkstra_max_completion": checks[1],
        })
    ts = [r["true_time"] for r in rows]
    ls = [r["scalar_stitch"] for r in rows]
    gs = [r["matching_penalty"] for r in rows]
    covariance = mean([l * g for l, g in zip(ls, gs)]) - mean(ls) * mean(gs)
    expected = {
        "mean_T": Fraction(21, 8), "variance_T": Fraction(23, 64),
        "mean_L": Fraction(5, 2), "variance_L": Fraction(3, 8),
        "mean_G": Fraction(1, 8), "variance_G": Fraction(7, 64),
        "covariance_L_G": Fraction(-1, 16),
    }
    actual = {
        "mean_T": mean(ts), "variance_T": variance(ts),
        "mean_L": mean(ls), "variance_L": variance(ls),
        "mean_G": mean(gs), "variance_G": variance(gs),
        "covariance_L_G": covariance,
    }
    assert actual == expected, actual
    assert Counter(ts) == {2: 7, 3: 8, 4: 1}
    assert Counter(ls) == {2: 9, 3: 6, 4: 1}
    assert variance(ts) == variance(ls) + variance(gs) + 2 * covariance
    mismatches = [r for r in rows if r["matching_penalty"]]
    assert [tuple(r[k] for k in ("a1", "a2", "b1", "b2")) for r in mismatches] == [
        (1, 2, 2, 1), (2, 1, 1, 2)
    ]
    with (output / "boundary_assignments.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    report = {
        "status": "passed",
        "proof_status": "exact reproduction; independent mathematical review pending",
        "assignments": len(rows), "dijkstra_checks": dijkstra_checks,
        "single_edge_forcing_checks": forcing_checks,
        "chosen_geodesic_membership_false_positives": selected_geodesic_false_positives,
        "exact_moments": {k: str(v) for k, v in actual.items()},
        "T_counts": dict(Counter(ts)), "L_counts": dict(Counter(ls)),
        "before_scalar_stitch": {
            "wrong_predictions": len(mismatches),
            "total_predictions": len(rows),
            "mean_absolute_error": str(mean(gs)),
            "absolute_variance_error": str(abs(variance(ts) - variance(ls))),
        },
        "after_matched_boundary_composition": {
            "wrong_predictions": 0,
            "total_predictions": len(rows),
            "mean_absolute_error": "0",
            "absolute_variance_error": "0",
        },
        "elapsed_seconds": time.monotonic() - started,
        "command": "python -X utf8 check_boundary_profile.py",
        "infinite_lattice_extension": (
            "Positive weights remove loops. Every alternative simple path has at least "
            "four edges, hence cost >=4; either two-edge path has cost <=4. "
            "Finite-box Dijkstra is an independent computational cross-check, "
            "while this argument supplies the infinite-lattice extension."
        ),
        "forcing_scope": (
            "Forcing the tested edge to 1 gives a two-edge route of cost at most 3. "
            "All other simple paths cost at least 4. Hence all forced-low minimizing "
            "paths are among the two checked routes, also on the full lattice."
        ),
    }
    assert report["elapsed_seconds"] < GATE["max_elapsed_seconds"]
    (output / "exact_boundary_counterexample.json").write_text(
        json.dumps(report, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
