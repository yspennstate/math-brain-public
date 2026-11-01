"""Bounded exact controls, not a proof or simulation of no bigeodesics."""
from collections import Counter
from datetime import datetime, timezone
from fractions import Fraction as Q
import heapq
import json
from pathlib import Path
import time
import psutil

ROOT = Path(__file__).resolve().parent
started = time.perf_counter()
gate = {"checked_at": datetime.now(timezone.utc).isoformat(),
        "cpu_percent": psutil.cpu_percent(interval=0.25),
        "available_memory_bytes": psutil.virtual_memory().available,
        "maximum_cpu_percent": 80, "minimum_available_memory_bytes": 512 * 1024**2,
        "bounded_work": "4096-state exact selector model; 3 finite 25-vertex graphs; one process; no GPU, network, or children"}
gate["passed"] = gate["cpu_percent"] <= gate["maximum_cpu_percent"] and gate["available_memory_bytes"] >= gate["minimum_available_memory_bytes"]
(ROOT / "COMPUTE_GATE.json").write_text(json.dumps(gate, indent=2) + "\n", encoding="utf-8")
if not gate["passed"]:
    receipt = {"status": "SKIPPED_FRESH_GATE", "gate": gate, "command": "python -X utf8 check_controls.py"}
    (ROOT / "MEASUREMENTS.json").write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(receipt))
    raise SystemExit(0)

def edge(a, b):
    return tuple(sorted((a, b)))

def grid(radius):
    vertices = [(x, y) for x in range(-radius, radius + 1) for y in range(-radius, radius + 1)]
    vset = set(vertices)
    edges = {edge(a, (a[0] + dx, a[1] + dy)) for a in vertices for dx, dy in [(1, 0), (0, 1)] if (a[0] + dx, a[1] + dy) in vset}
    return vertices, edges

def distances(vertices, weights, start):
    adj = {v: [] for v in vertices}
    for (a, b), value in weights.items():
        if a in adj and b in adj:
            adj[a].append((b, value))
            adj[b].append((a, value))
    out = {start: Q(0)}
    heap = [(Q(0), start)]
    while heap:
        value, vertex = heapq.heappop(heap)
        if out[vertex] != value:
            continue
        for neighbor, weight in adj[vertex]:
            candidate = value + weight
            if neighbor not in out or candidate < out[neighbor]:
                out[neighbor] = candidate
                heapq.heappush(heap, (candidate, neighbor))
    return out

# Exact finite partitions match all first-12-level probabilities of a uniform U.
selector_rows = []
states = 4096
for n in range(1, 13):
    indexes = [r // (states // 2**n) for r in range(states)]
    counts = Counter(indexes)
    assert len(counts) == 2**n
    assert set(counts.values()) == {states // 2**n}
    selected_count = sum(indexes[r] == indexes[r] for r in range(states))
    assert selected_count == states
    for m in range(1, n):
        refinements = Counter((r // (states // 2**m), indexes[r]) for r in range(states))
        assert set(refinements.values()) == {states // 2**n}
    selector_rows.append({"level": n, "index_count": 2**n,
                          "maximum_fixed_probability": str(Q(1, 2**n)),
                          "union_probability": "1", "selected_probability": "1"})

vertices, edges = grid(2)
origin, u, v = (0, 0), (-1, 0), (1, 0)
detour = [u, (-2, 0), (-2, 1), (-2, 2), (-1, 2), (0, 2), (1, 2), (2, 2), (2, 1), (2, 0), v]
control = {e: Q(10) for e in edges}
control[edge(u, origin)] = control[edge(origin, v)] = Q(1)
detour_edges = {edge(a, b) for a, b in zip(detour, detour[1:])}
for e in detour_edges:
    control[e] = Q(1, 10)
small_vertices, small_edges = grid(1)
small_weights = {e: control[e] for e in small_edges}
box_distance = distances(small_vertices, small_weights, u)[v]
full_distance = distances(vertices, control, u)[v]
full_through_origin = distances(vertices, control, u)[origin] + distances(vertices, control, origin)[v]
assert box_distance == 2 and full_distance == 1 and full_through_origin == 2
assert len(small_edges) == 12 and len(detour_edges) == 10 and not small_edges.intersection(detour_edges)
assert Q(21, 10) < 2 * 9 and Q(1) < Q(19, 10)
cylinder_probability = Q(2, 199)**2 * Q(20, 199)**10 * Q(1, 199)**10
assert cylinder_probability > 0

# Check w384's closed metric formula against independent shortest-path costs.
test_edge = edge(origin, (1, 0))
cases = [
    {e: Q(1) for e in edges},
    {e: Q(1 + ((sum(e[0]) + 3 * sum(e[1])) % 7)) for e in edges},
    control,
]
formula_count = strict_use = strict_avoid = ties = 0
for base in cases:
    deleted = {e: value for e, value in base.items() if e != test_edge}
    d = {x: distances(vertices, deleted, x) for x in vertices}
    a, b = test_edge
    for s in [Q(1, 10), Q(1), Q(2), Q(3), Q(7)]:
        modified = dict(deleted)
        modified[test_edge] = s
        actual = {x: distances(vertices, modified, x) for x in vertices}
        for x in vertices:
            for y in vertices:
                via = min(d[x][a] + d[b][y], d[x][b] + d[a][y])
                threshold = d[x][y] - via
                expected = min(d[x][y], s + via)
                assert actual[x][y] == expected
                if s < threshold:
                    assert actual[x][y] < d[x][y]
                    strict_use += 1
                elif s > threshold:
                    assert actual[x][y] == d[x][y]
                    strict_avoid += 1
                else:
                    assert actual[x][y] == d[x][y] == s + via
                    ties += 1
                formula_count += 1
assert formula_count == 9375 and ties > 0 and strict_use > 0 and strict_avoid > 0

receipt = {
    "status": "PASS", "command": "python -X utf8 check_controls.py",
    "elapsed_seconds": round(time.perf_counter() - started, 4), "gate": gate,
    "selector": {"states": states, "levels": len(selector_rows), "rows": selector_rows,
                 "baseline_false_selected_bound": "1/4096", "measured_selected_probability": "1",
                 "corrected_selected_bound": "1", "underestimate_factor": 4096},
    "box_metric": {"box_vertices": 9, "comparison_vertices": 25,
                   "box_shortest_cost": str(box_distance), "larger_graph_shortest_cost": str(full_distance),
                   "cost_of_shortest_walk_forced_through_origin": str(full_through_origin),
                   "iid_cylinder_independent_edges": 22, "iid_cylinder_probability_exact": str(cylinder_probability)},
    "deleted_edge_formula": {"outside_graphs": len(cases), "replacement_weights": 5,
                             "ordered_pairs_per_case": 625, "checked_equalities": formula_count,
                             "strict_use_cases": strict_use, "strict_avoid_cases": strict_avoid,
                             "tie_cases": ties, "maximum_exact_error": "0"},
    "not_certified": ["No infinite-volume FPP theorem", "No support-collapse proof",
                      "No formal theorem checker or axiom receipt", "No deployed recall improvement"]
}
(ROOT / "MEASUREMENTS.json").write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"status": receipt["status"], "elapsed_seconds": receipt["elapsed_seconds"],
                  "selector_levels": 12, "selector_underestimate_factor": 4096,
                  "box_cost": str(box_distance), "larger_graph_cost": str(full_distance),
                  "formula_equalities": formula_count, "formula_maximum_error": "0", "tie_cases": ties}))
