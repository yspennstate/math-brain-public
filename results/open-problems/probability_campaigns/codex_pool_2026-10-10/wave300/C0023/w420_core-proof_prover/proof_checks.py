"""Small exact checks for the handwritten lemmas, not a formal proof."""
from collections import deque
from fractions import Fraction
from itertools import product
import json
from pathlib import Path
import time

ROOT = Path(__file__).resolve().parent
NEIGHBORS = ((1, 0), (-1, 0), (0, 1), (0, -1))


def connected(sites):
    seen = {(0, 0)}
    todo = deque(seen)
    while todo:
        x, y = todo.popleft()
        for dx, dy in NEIGHBORS:
            v = x+dx, y+dy
            if v in sites and v not in seen:
                seen.add(v)
                todo.append(v)
    return seen == sites


def winding(cycle):
    value = 0
    for a, b in zip(cycle, cycle[1:] + cycle[:1]):
        cross = a[0]*b[1] - a[1]*b[0]
        if a[1] <= 0 < b[1] and cross > 0:
            value += 1
        elif b[1] <= 0 < a[1] and cross < 0:
            value -= 1
    return value


def enclosing_bad_cycle(sites):
    boundary = {(x+dx, y+dy) for x, y in sites for dx, dy in NEIGHBORS} - sites
    graph = {a: sorted(b for b in boundary if a != b and max(abs(a[0]-b[0]), abs(a[1]-b[1])) <= 1) for a in boundary}
    parent = {}
    for root in sorted(boundary):
        if root in parent:
            continue
        parent[root] = None
        todo = [root]
        while todo:
            u = todo.pop()
            for v in graph[u]:
                if v not in parent:
                    parent[v] = u
                    todo.append(v)
    def ancestors(v):
        result = []
        while v is not None:
            result.append(v)
            v = parent[v]
        return result
    for u in sorted(boundary):
        for v in graph[u]:
            if u >= v or parent[u] == v or parent[v] == u:
                continue
            au, av = ancestors(u), ancestors(v)
            lca = next(a for a in au if a in av)
            cycle = au[:au.index(lca)+1] + list(reversed(av[:av.index(lca)]))
            if len(cycle) >= 3 and winding(cycle):
                assert len(cycle) == len(set(cycle))
                assert not (set(cycle) & sites)
                assert all(max(abs(x), abs(y)) <= len(cycle) for x, y in cycle)
                return cycle
    raise AssertionError(f"No enclosing bad star-cycle for {sorted(sites)}")


def run_checks(gate_receipt):
    # The runner supplies a real, fresh compute_sense gate receipt.
    assert gate_receipt["allowed"] is True
    assert time.time() - gate_receipt["finished_epoch"] < 60
    start = time.perf_counter()
    q = Fraction(1, 2)
    states = list(product((0, 1), repeat=4))
    all_bad = sum(all(bit == 0 for bit in state for _ in (0, 1)) for state in states)
    actual = Fraction(all_bad, len(states))
    naive = q**8
    corrected = q**2  # R=1, K=4, m=8; only the independent color subfamily is multiplied.
    assert actual == Fraction(1, 16) and naive == Fraction(1, 256)
    assert naive < actual <= corrected

    t = Fraction(1, 100)
    contour_error = Fraction(1, 800) + 9*t*(1+t)/(1-t)**3
    assert contour_error < Fraction(1, 10)

    rest = [(x, y) for x in (-1, 0, 1) for y in (-1, 0, 1) if (x, y) != (0, 0)]
    count, max_cycle = 0, 0
    for mask in range(1 << len(rest)):
        sites = {(0, 0)} | {v for i, v in enumerate(rest) if mask & (1 << i)}
        if connected(sites):
            max_cycle = max(max_cycle, len(enclosing_bad_cycle(sites)))
            count += 1
    special = [
        {(x, y) for x in range(-2, 3) for y in range(-2, 3)} - {(1, 1)},
        {(x, 0) for x in range(-4, 5)} | {(0, y) for y in range(-4, 5)},
        {(0, 0), (1, 0), (1, 1), (2, 1), (2, 2)},
    ]
    for sites in special:
        assert connected(sites)
        max_cycle = max(max_cycle, len(enclosing_bad_cycle(sites)))

    counterexample_pairs = 0
    for inner in range(1, 6):
        transition = inner * 2**inner
        for outer in (inner, transition-1, transition, transition+inner, 2*transition):
            r = (2*(outer+inner)) // inner
            fake = Fraction(1, 1) if outer < transition else Fraction(1, 2**inner)
            delta = Fraction(1, 800**((r+1)**2))
            assert fake > delta
            counterexample_pairs += 1

    result = {
        "scope": "exact finite checks of supporting lemmas; no proof of the full target",
        "passed": True,
        "checks_seconds": time.perf_counter()-start,
        "dependency_counterexample": {"independent_domino_variables": 4, "duplicated_bad_sites": 8,
            "states_enumerated": len(states), "true_all_bad_probability": str(actual),
            "invalid_marginal_product": str(naive), "understatement_factor": str(actual/naive),
            "valid_color_bound": str(corrected)},
        "peierls_error_upper_bound": str(contour_error),
        "peierls_error_float": float(contour_error),
        "boundary_cases": {"connected_subsets_of_3x3": count, "additional_hole_and_corner_cases": len(special),
            "failures": 0, "largest_found_cycle": max_cycle},
        "quantifier_counterexample_pairs": counterexample_pairs,
        "gate_receipt": "COMPUTE_GATE_REPORT.json"
    }
    (ROOT / "MEASUREMENTS.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
    return result
