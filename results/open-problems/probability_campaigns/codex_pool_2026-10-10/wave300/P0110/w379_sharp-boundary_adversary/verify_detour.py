"""Exact finite-graph checks; no simulations, external writes, or live-store access."""
from __future__ import annotations

from datetime import datetime, timezone
from fractions import Fraction
from heapq import heappop, heappush
from itertools import product
from pathlib import Path
import json
import time

ROOT = Path(__file__).resolve().parent
STATE = Path(r"~\.claude\compute\compute_state.json")


def edge(u, v):
    return tuple(sorted((u, v)))


def paths(n, start=0):
    direct = [edge((x, 0), (x + 1, 0)) for x in range(start, start + n)]
    detour = [edge((start, 0), (start, 1))]
    detour += [edge((x, 1), (x + 1, 1)) for x in range(start, start + n)]
    detour += [edge((start + n, 1), (start + n, 0))]
    return direct, detour


def shortest(edges, start, end):
    adj = {}
    for (u, v), w in edges.items():
        adj.setdefault(u, []).append((v, w))
        adj.setdefault(v, []).append((u, w))
    queue = [(0, start)]
    dist = {start: 0}
    while queue:
        cost, u = heappop(queue)
        if cost != dist[u]:
            continue
        if u == end:
            return cost
        for v, weight in adj[u]:
            new = cost + weight
            if new < dist.get(v, float("inf")):
                dist[v] = new
                heappush(queue, (new, v))
    raise AssertionError("No connecting path")


def gate():
    state = json.loads(STATE.read_text(encoding="utf-8-sig"))
    age = time.time() - STATE.stat().st_mtime
    receipt = {k: state.get(k) for k in (
        "ts", "status", "mode", "reasons", "cpu_pct", "commit_used_pct", "commit_avail_mb"
    )}
    receipt.update({
        "observed_at": datetime.now(timezone.utc).isoformat(),
        "file_age_seconds": age,
        "planned_configurations": 320,
        "workload": "one short single-process CPU-only exact finite-graph check; no models, random simulation, sweeps, GPU, or parallel children",
        "throttle_action": "reduced from 1344 to 320 fixed configurations; retain launcher priority and finish one bounded atomic check",
    })
    if age > 90 or age < -2 or state.get("commit_used_pct") is None or state.get("commit_avail_mb") is None:
        receipt["decision"] = "BLOCK: stale or missing commit telemetry"
        (ROOT / "COMPUTE_GATE.json").write_text(json.dumps(receipt, indent=2), encoding="utf-8")
        raise RuntimeError(receipt["decision"])
    receipt["decision"] = "LIGHT_CHECK_ONLY: follow published throttle; no model-heavy computation"
    (ROOT / "COMPUTE_GATE.json").write_text(json.dumps(receipt, indent=2), encoding="utf-8")
    return receipt


def check(n, deadline):
    direct, detour = paths(n)
    all_edges = direct + detour
    assert len(all_edges) == 2 * n + 2
    assert len(set(all_edges)) == len(all_edges)
    count = positive = ties = 0
    saving = 0
    for values in product((1, 2), repeat=len(all_edges)):
        if time.monotonic() > deadline:
            raise RuntimeError("Bounded check exceeded 15-second work budget")
        weights = dict(zip(all_edges, values))
        axis_cost = sum(weights[e] for e in direct)
        upper_cost = sum(weights[e] for e in detour)
        actual = shortest(weights, (0, 0), (n, 0))
        assert actual == min(axis_cost, upper_cost)
        gap = axis_cost - actual
        positive += gap > 0
        ties += axis_cost == upper_cost
        saving += gap
        count += 1
    return {
        "n": n, "configurations": count, "dijkstra_checks_passed": count,
        "positive_detour_cases": positive, "tie_cases": ties,
        "mean_block_saving_exact": str(Fraction(saving, count)),
        "naive_axis_equals_unrestricted_failures": positive,
    }


def main():
    receipt = gate()
    start = time.monotonic()
    deadline = start + 15
    rows = [check(n, deadline) for n in (2, 3)]
    assert rows[0]["positive_detour_cases"] == 0
    assert rows[0]["tie_cases"] == 1
    assert rows[1]["positive_detour_cases"] == 1
    assert rows[1]["mean_block_saving_exact"] == "1/256"
    used = set()
    for k in range(20):
        axis, upper = paths(3, k * 5)
        block = set(axis + upper)
        assert used.isdisjoint(block)
        used.update(block)
    c = Fraction(1, 256) / 5
    assert c == Fraction(1, 1280)
    result = {
        "status": "PASS", "gate": receipt,
        "command": "python -X utf8 ~/brain_workers/w379/verify_detour.py",
        "elapsed_check_seconds": time.monotonic() - start,
        "total_configurations": sum(r["configurations"] for r in rows),
        "rows": rows,
        "independent_translated_blocks_checked": 20,
        "shared_block_edges": 0,
        "rigorous_c2_bound_for_fair_1_2_weights": str(c),
        "scope": "Finite exact checks corroborate the construction and equality boundary; the infinite-volume result requires INDEPENDENT.md's proof and an independent referee. No exponent or novelty claim."
    }
    (ROOT / "MEASUREMENTS.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
