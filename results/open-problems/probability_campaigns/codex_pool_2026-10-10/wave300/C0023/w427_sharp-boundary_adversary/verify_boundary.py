"""Bounded exact certificates for the strip constants and planar lower bound.

This verifies finite numerical consequences; it is not a proof of C0023.
"""
import json
from collections import Counter
from datetime import datetime, timezone
from fractions import Fraction
from pathlib import Path
from time import perf_counter

ROOT = Path(__file__).resolve().parent
started = perf_counter()
gate = {
    "opened_at": datetime.now(timezone.utc).isoformat(),
    "kind": "fresh bounded exact-enumeration gate",
    "max_configurations": 5000,
    "max_seconds": 30,
    "max_edges_per_graph": 12,
    "local_cpu_only": True,
    "gpu_or_training": False,
}
enumerated = 0


def arm_counts(k, radius):
    global enumerated
    vertices = [(x, y) for x in range(-radius, radius + 1)
                for y in range(-k, k + 1)]
    edges = [(u, v) for i, u in enumerate(vertices) for v in vertices[i + 1:]
             if abs(u[0] - v[0]) + abs(u[1] - v[1]) == 1]
    assert len(edges) <= gate["max_edges_per_graph"]
    configurations = 1 << len(edges)
    assert enumerated + configurations <= gate["max_configurations"]
    counts = Counter()
    for mask in range(configurations):
        if perf_counter() - started > gate["max_seconds"]:
            raise RuntimeError("fresh compute gate exhausted")
        adjacency = {v: [] for v in vertices}
        for i, (u, v) in enumerate(edges):
            if mask & (1 << i):
                adjacency[u].append(v)
                adjacency[v].append(u)
        reached = {(0, 0)}
        queue = [(0, 0)]
        for u in queue:
            for v in adjacency[u]:
                if v not in reached:
                    reached.add(v)
                    queue.append(v)
        if any(abs(x) == radius for x, _ in reached):
            counts[mask.bit_count()] += 1
    enumerated += configurations
    return len(edges), counts


checks = []
for k, radius in [(0, r) for r in range(1, 5)] + [(1, 1)]:
    edge_count, counts = arm_counts(k, radius)
    for p in [Fraction(1, 10), Fraction(1, 4), Fraction(1, 2), Fraction(3, 4)]:
        exact = sum((count * p ** opened * (1 - p) ** (edge_count - opened)
                     for opened, count in counts.items()), Fraction(0))
        bound = 2 * (1 - (1 - p) ** (2 * k + 1)) ** radius
        assert exact <= bound
        if k == 0:
            assert exact == 2 * p ** radius - p ** (2 * radius)
        checks.append({"k": k, "radius": radius, "p": str(p),
                       "exact_one_arm_probability": str(exact),
                       "strip_cut_bound": str(bound),
                       "incorrect_width_zero_bound": str(2 * p ** radius),
                       "incorrect_bound_fails": exact > 2 * p ** radius})

a = Fraction(3, 100)
peierls = Fraction(4, 3) * a ** 4 * (4 - 3 * a) / (1 - a) ** 2
assert peierls == Fraction(10557, 2352250000)
assert peierls < Fraction(1, 100000)
width_errors = [r for r in checks if r["incorrect_bound_fails"]]
assert width_errors, "exact enumeration must detect the missing strip-width factor"
result = {
    "gate": gate,
    "enumerated_configurations": enumerated,
    "finite_graph_probability_checks": len(checks),
    "all_correct_cut_bounds_pass": True,
    "wrong_width_bound_failures": width_errors,
    "planar_finite_cluster_upper_bound": str(peierls),
    "planar_percolation_lower_bound": str(1 - peierls),
    "planar_percolation_lower_bound_decimal": float(1 - peierls),
    "elapsed_seconds": perf_counter() - started,
    "limits": "Finite exact checks and rational arithmetic only; no independent referee or formal proof receipt.",
    "checks": checks,
}
(ROOT / "MEASUREMENTS.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps({k: v for k, v in result.items() if k != "checks"}, indent=2))
