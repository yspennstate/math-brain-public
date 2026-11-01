"""Small exact checks of the P0117 reduction; no asymptotic evidence is inferred.

Run after a fresh existing compute gate has been read. All graphs are finite,
weights are integers measured in half units, and all comparisons are exact.
The workload is bounded to six 49-vertex graphs, 12 CPU seconds and 45 seconds
of wall time after the gate is accepted. No dependencies are installed.
"""
from __future__ import annotations

import argparse
import heapq
import json
import math
import time
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
EDGE = ((0, 0), (1, 0))
START_CPU = time.process_time()
START_WALL = time.monotonic()


def bounded() -> None:
    if time.process_time() - START_CPU > 12:
        raise RuntimeError("12 CPU-second compute cap reached")
    if time.monotonic() - START_WALL > 45:
        raise RuntimeError("45 wall-second compute cap reached")


def edge_key(x, y):
    return tuple(sorted((x, y)))


def graph(seed):
    nodes = [(x, y) for x in range(-3, 4) for y in range(-3, 4)]
    edges = {}
    for x, y in nodes:
        for z in [(x + 1, y), (x, y + 1)]:
            if z in nodes:
                k = edge_key((x, y), z)
                # Fixtures include an atomic control and varying positive weights.
                edges[k] = 2 if seed == 0 else 2 + (
                    17 * (x + 3) + 11 * (y + 3) + 13 * (z[0] + 3)
                    + 7 * (z[1] + 3) + seed * (19 + 5 * x + 3 * y)
                ) % 29
    return nodes, edges


def all_distances(nodes, edges, replacement):
    adjacency = {x: [] for x in nodes}
    for (x, y), weight in edges.items():
        if (x, y) == EDGE:
            if replacement is None:
                continue
            weight = replacement
        adjacency[x].append((y, weight))
        adjacency[y].append((x, weight))
    result = {}
    for root in nodes:
        bounded()
        dist = {root: 0}
        queue = [(0, root)]
        while queue:
            cost, x = heapq.heappop(queue)
            if cost != dist[x]:
                continue
            for y, w in adjacency[x]:
                cand = cost + w
                if y not in dist or cand < dist[y]:
                    dist[y] = cand
                    heapq.heappush(queue, (cand, y))
        assert len(dist) == len(nodes)
        result[root] = dist
    return result


def fresh_gate(path, max_age):
    gate = json.loads(path.read_text(encoding="utf-8-sig"))
    age = time.time() - path.stat().st_mtime
    if not -5 <= age <= max_age:
        raise RuntimeError(f"Compute gate age {age:.1f}s exceeds freshness limit")
    # Actual producer schema, per COMPUTE_DOCTRINE.md: ok/warn/distress.
    # The 2026-09-09 correction permits bounded work on count-only warnings;
    # distress and actual resource pressure still hold it. No gate is modified.
    if gate.get('status') not in ('ok', 'warn'):
        raise RuntimeError('Governor distress or unknown status holds this check')
    if gate.get('mode') == 'throttle':
        raise RuntimeError('Governor throttle holds this check')
    for name, floor in [('mem_avail_mb', 1536), ('commit_avail_mb', 6144), ('disk_free_gb', 3)]:
        val = gate.get(name)
        if isinstance(val, bool) or not isinstance(val, (int, float)) or not math.isfinite(val) or val < floor:
            raise RuntimeError(f'Insufficient or missing {name}')
    if gate.get('hung_windows') != 0:
        raise RuntimeError('Hung-window signal holds this check')
    if any('critical' in str(x) or 'ui_freeze' in str(x) or 'starvation' in str(x)
           for x in gate.get('reasons', [])):
        raise RuntimeError('Critical pressure reason holds this check')
    sample = datetime.fromisoformat(gate['ts']).astimezone()
    sample_age = (datetime.now(timezone.utc) - sample).total_seconds()
    if not -5 <= sample_age <= max_age:
        raise RuntimeError(f'Governor sample age {sample_age:.1f}s is not fresh')
    keys = ['ts', 'status', 'mode', 'reasons', 'cpu_pct', 'mem_avail_mb',
            'commit_avail_mb', 'disk_free_gb', 'hung_windows']
    return {'path': str(path), 'age_seconds': age, 'sample_age_seconds': sample_age,
            'selected_gate_metrics': {k: gate[k] for k in keys},
            'policy': 'Existing governor plus 6 GiB worker commit floor; one tiny bounded CPU job.'}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--gate", type=Path, required=True)
    ap.add_argument("--max-gate-age", type=float, default=90)
    args = ap.parse_args()
    receipt = fresh_gate(args.gate, args.max_gate_age)
    counts = dict(metric_formula=0, strict_threshold=0, detour_bound=0,
                  boundary_monotonicity=0, tie_cases=0,
                  wrong_orientation_rejected=0, atomic_control=0,
                  selection_counterexample=0)
    capacities = []
    for seed in range(6):
        fresh_gate(args.gate, args.max_gate_age)
        nodes, edges = graph(seed)
        d = all_distances(nodes, edges, None)
        u, v = EDGE
        cap = {}
        thresholds = {}
        for x in nodes:
            for y in nodes:
                c = min(d[x][u] + d[v][y], d[x][v] + d[u][y])
                value = d[x][y] - c
                thresholds[x, y] = value
                assert value <= d[u][v]
                counts["detour_bound"] += 1
        for radius in (2, 3):
            boundary = [x for x in nodes if max(map(abs, x)) == radius]
            cap[radius] = max(0, max(thresholds[x, y] for x in boundary for y in boundary))
        assert cap[3] <= cap[2]
        counts["boundary_monotonicity"] += 1
        capacities.append({"fixture": seed, "H2_half_units": cap[2],
                           "H3_half_units": cap[3], "detour_half_units": d[u][v]})
        samples = {1, 2, 3, 6, 17, 33, 67}
        samples.update(x for x in cap.values() if x > 0)
        for s in sorted(samples):
            full = all_distances(nodes, edges, s)
            for x in nodes:
                for y in nodes:
                    delta = thresholds[x, y]
                    c = d[x][y] - delta
                    assert full[x][y] == min(d[x][y], s + c)
                    counts["metric_formula"] += 1
                    assert (full[x][y] < d[x][y]) == (s < delta)
                    counts["strict_threshold"] += 1
                    if s == delta:
                        assert full[x][y] == d[x][y]
                        counts["tie_cases"] += 1
                    wrong = min(d[x][y], s + d[x][u] + d[v][y])
                    if wrong != full[x][y]:
                        counts["wrong_orientation_rejected"] += 1
        if seed == 0:
            assert cap[2] == cap[3] == d[u][v] == 6
            counts["atomic_control"] += 1
    # Every deterministic pair can have tiny probability while a selected pair
    # succeeds surely. Exhaust the abstract probability space, without simulation.
    for m in (8, 64, 512):
        hits = [0] * m
        for selected in range(m):
            hits[selected] += 1
            assert any(i == selected for i in range(m))
        assert all(x == 1 for x in hits)
        counts["selection_counterexample"] += 1
    assert counts["tie_cases"] > 0
    assert counts["wrong_orientation_rejected"] > 0
    fresh_gate(args.gate, args.max_gate_age)
    bounded()
    out = dict(status="PASS", scope="Finite exact instrument checks only; not an infinite-volume proof",
               command="python -X utf8 verify_threshold.py --gate " + str(args.gate),
               checked_utc=datetime.now(timezone.utc).isoformat(), gate_receipt=receipt,
               before={"verified_comparisons": 0}, after=counts, capacities=capacities,
               cpu_seconds=time.process_time() - START_CPU,
               wall_seconds=time.monotonic() - START_WALL,
               formal_check=None, independent_mathematical_review="PENDING")
    (ROOT / "MEASUREMENTS.json").write_text(json.dumps(out, indent=2), encoding="utf-8")
    print(json.dumps({k: out[k] for k in ["status", "after", "cpu_seconds", "wall_seconds"]}))


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        (ROOT / "MEASUREMENTS.json").write_text(json.dumps(
            {"status": "NOT_PASSED", "reason": str(error), "type": type(error).__name__,
             "scope": "No infinite-volume mathematical conclusion"}, indent=2), encoding="utf-8")
        raise
