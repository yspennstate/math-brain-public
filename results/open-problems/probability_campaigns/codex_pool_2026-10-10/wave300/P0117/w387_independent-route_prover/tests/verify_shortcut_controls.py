"""Small exact controls, not a test bank or a proof of no bigeodesics.

Run only after a fresh compute gate. Uses rational arithmetic, 256 square
assignments, and deterministic lattice geometry; no sampling or training.
"""

from fractions import Fraction as F
from itertools import product
from math import log1p
from heapq import heappop, heappush
from pathlib import Path
import json
import time


ROOT = Path(__file__).resolve().parents[1]


def edge(a, b):
    assert abs(a[0] - b[0]) + abs(a[1] - b[1]) == 1
    return tuple(sorted((a, b)))


def edges(path):
    return {edge(a, b) for a, b in zip(path, path[1:])}


def shortest(weights, start, goal):
    graph = {}
    for (a, b), weight in weights.items():
        graph.setdefault(a, []).append((b, weight))
        graph.setdefault(b, []).append((a, weight))
    queue, distances = [(F(0), start)], {start: F(0)}
    while queue:
        distance, vertex = heappop(queue)
        if distance != distances[vertex]:
            continue
        if vertex == goal:
            return distance
        for adjacent, weight in graph[vertex]:
            candidate = distance + weight
            if adjacent not in distances or candidate < distances[adjacent]:
                distances[adjacent] = candidate
                heappush(queue, (candidate, adjacent))
    raise AssertionError('No path')


def main():
    started = time.perf_counter()
    # Representatives of four equal-probability Uniform[1,2] strata.
    # The high/low event counts are exact because whole strata are classified.
    # Other probabilities involving ordering of sums are not inferred from this grid.
    values = [F(9, 8), F(11, 8), F(13, 8), F(15, 8)]
    lo, hi = F(5, 4), F(7, 4)
    fixed, selected, worlds = 0, 0, 0
    for a1, a2, b1, b2 in product(values, repeat=4):
        worlds += 1
        fixed += int(a1 >= hi and a2 >= hi and b1 <= lo and b2 <= lo)
        own, alternate = ((a1, a2), (b1, b2)) if a1 + a2 <= b1 + b2 else ((b1, b2), (a1, a2))
        selected += int(min(own) >= hi and max(alternate) <= lo)
    assert (worlds, fixed, selected) == (256, 1, 0)

    # All eight oriented turns have a disjoint two-edge square alternative.
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    turns = 0
    for u, v in product(dirs, repeat=2):
        if u[0] * v[0] + u[1] * v[1] != 0:
            continue
        destination = (u[0] + v[0], u[1] + v[1])
        original = [(0, 0), u, destination]
        alternate = [(0, 0), v, destination]
        assert not (edges(original) & edges(alternate))
        assert len(edges(original)) == len(edges(alternate)) == 2
        assert 2 * hi > 2 * lo
        turns += 1
    assert turns == 8

    # A six-edge straight path admits an eight-edge disjoint detour, in every direction.
    length = 6
    assert length * (hi - lo) > 2 * lo
    straights = 0
    for u in dirs:
        perpendicular = (-u[1], u[0])
        original = [(i * u[0], i * u[1]) for i in range(length + 1)]
        shifted = [(x + perpendicular[0], y + perpendicular[1]) for x, y in original]
        alternate = [original[0]] + shifted + [original[-1]]
        assert not (edges(original) & edges(alternate))
        assert len(edges(alternate)) == length + 2
        assert len(set(alternate)) == len(alternate)
        assert all(abs(x) + abs(y) <= length + 1 for x, y in alternate)
        assert length * hi > (length + 2) * lo
        straights += 1
    assert straights == 4

    radius = 2 * (length + 1)
    ball_count = sum(abs(x) + abs(y) <= radius for x in range(-radius, radius + 1) for y in range(-radius, radius + 1))
    assert ball_count == 1 + 2 * radius * (radius + 1) == 421
    eta = F(1, 4) ** (2 * length + 2)
    c = -log1p(-float(eta)) / (length * ball_count)
    assert c > 0
    # A box-shortest witness is not necessarily globally shortest.
    # West--origin--east costs 4 in B_1. Its four-edge upper detour costs 1.
    origin, west, east = (0, 0), (-1, 0), (1, 0)
    box_weights = {edge(origin, neighbor): F(2) for neighbor in dirs}
    assert shortest(box_weights, west, east) == F(4)
    expanded_weights = dict(box_weights)
    detour = [west, (-1, 1), (0, 1), (1, 1), east]
    for e in edges(detour):
        expanded_weights[e] = F(1, 4)
    assert shortest(expanded_weights, west, east) == F(1)

    result = {
        "kind": "exact finite controls; not a formal theorem checker",
        "control_batch_executed": True,
        "worlds": worlds,
        "fixed_route_high_low_pattern_count": fixed,
        "selected_route_high_low_pattern_count": selected,
        "fixed_route_pattern_probability": str(F(fixed, worlds)),
        "selected_route_pattern_probability": str(F(selected, worlds)),
        "turn_orientations_checked": turns,
        "straight_orientations_checked": straights,
        "L": length,
        "R": radius,
        "D": ball_count,
        "eta": str(eta),
        "c": c,
        "box_witness_cost": "4",
        "expanded_graph_shorter_cost": "1",
        "elapsed_seconds": time.perf_counter() - started,
        "scope": "Checks L3 high/low stratification counts and L4 detour geometry/constants. Does not check the infinite compactness argument or establish candidate entropy control.",
    }
    (ROOT / "MEASUREMENTS.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
