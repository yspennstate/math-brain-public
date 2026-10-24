"""Small exact graph check, independent of the infinite-lattice analytic proof."""
from __future__ import annotations

import heapq
import json
import time
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parent
GATE = json.loads((ROOT / "COMPUTE_GATE.json").read_text(encoding="utf-8"))
START = time.monotonic()
CONFIGURATIONS = 0


def check_gate() -> None:
    if time.monotonic() - START > GATE["limits"]["wall_seconds"]:
        raise RuntimeError("compute gate time exceeded; no conclusion recorded")
    if CONFIGURATIONS > GATE["limits"]["maximum_configurations"]:
        raise RuntimeError("compute gate configuration cap exceeded")


def ladder(n: int) -> tuple[list[tuple[int, int]], list[int], int, int]:
    # Vertex (x,y) is 2*x+y; bottom edges come first.
    bottom = [(2 * x, 2 * (x + 1)) for x in range(n)]
    top = [(2 * x + 1, 2 * (x + 1) + 1) for x in range(n)]
    vertical = [(2 * x, 2 * x + 1) for x in range(n + 1)]
    return bottom + top + vertical, list(range(n)), 2 * (n + 1), 2 * n


def shortest(edges, weights, vertices, target):
    adjacent = [[] for _ in range(vertices)]
    for (u, v), weight in zip(edges, weights):
        adjacent[u].append((v, weight))
        adjacent[v].append((u, weight))
    infinity = sum(weights) + 1
    distance = [infinity] * vertices
    count = [0] * vertices
    distance[0], count[0] = 0, 1
    queue = [(0, 0)]
    while queue:
        old, u = heapq.heappop(queue)
        if old != distance[u]:
            continue
        if u == target:
            return old, count[u]
        for v, weight in adjacent[u]:
            new = old + weight
            if new < distance[v]:
                distance[v], count[v] = new, count[u]
                heapq.heappush(queue, (new, v))
            elif new == distance[v]:
                count[v] += count[u]
    raise AssertionError("ladder disconnected")


def exact_case(n: int, a: int, b: int, scale: int, label: str) -> dict:
    global CONFIGURATIONS
    edges, axial, vertices, target = ladder(n)
    assert vertices <= GATE["limits"]["maximum_vertices_per_graph"]
    total = 1 << len(edges)
    failed = tied = unique = 0
    sum_t = sum_t2 = 0
    for mask in range(total):
        CONFIGURATIONS += 1
        if CONFIGURATIONS % 128 == 0:
            check_gate()
        weights = [b if mask & (1 << i) else a for i in range(len(edges))]
        cost, paths = shortest(edges, weights, vertices, target)
        straight = sum(weights[i] for i in axial)
        assert cost <= straight
        if cost < straight:
            failed += 1
        elif paths > 1:
            tied += 1
        else:
            unique += 1
        sum_t += cost
        sum_t2 += cost * cost
    mean = Fraction(sum_t, total * scale)
    variance = Fraction(sum_t2, total * scale * scale) - mean * mean
    if n * (b - a) < 2 * a:
        assert unique == total and failed == tied == 0
        assert variance == n * Fraction((b - a) ** 2, 4 * scale * scale)
    if label == "equality":
        assert failed == 0 and tied > 0
    if label == "above":
        assert failed > 0
    return {"label": label, "n": n, "a": str(Fraction(a, scale)),
            "b": str(Fraction(b, scale)), "edge_count": len(edges),
            "configurations": total, "axial_unique": unique,
            "axial_optimal_with_tie": tied, "axial_suboptimal": failed,
            "mean": str(mean), "variance": str(variance)}


def main() -> None:
    cases = [exact_case(2, 2, 3, 2, "below"),
             exact_case(2, 1, 2, 1, "equality"),
             exact_case(2, 2, 5, 2, "above"),
             exact_case(2, 4, 5, 4, "contraction_n"),
             exact_case(4, 4, 5, 4, "contraction_2n")]
    variance_n = Fraction(cases[-2]["variance"])
    variance_2n = Fraction(cases[-1]["variance"])
    ratio = variance_2n / (2 * variance_n)
    assert ratio == 1
    # Independent exact integrals for Uniform[1,1+epsilon].
    epsilon = Fraction(1, 4)
    first = 1 + epsilon / 2
    second = 1 + epsilon + epsilon * epsilon / 3
    single_variance = second - first * first
    assert single_variance == epsilon * epsilon / 12
    # Geometric identity used in the deterministic tube bound.
    identity_cases = 0
    for n in range(1, 5):
        for x in range(-3, n + 4):
            for y in range(-3, 4):
                delta = abs(y) + max(-x, 0, x - n)
                assert abs(x) + abs(y) + abs(n - x) + abs(y) == n + 2 * delta
                identity_cases += 1
    check_gate()
    result = {"verdict": "PASS", "arithmetic": "exact integers and rational moments",
              "cases": cases, "total_configurations": CONFIGURATIONS,
              "variance_ratio_V2n_over_2Vn": str(ratio),
              "rho_half_bridge": "REFUTED on the tested fixed law and scale",
              "uniform_epsilon": str(epsilon),
              "uniform_single_edge_variance": str(single_variance),
              "uniform_V2": str(2 * single_variance),
              "uniform_V4": str(4 * single_variance),
              "tube_identity_cases": identity_cases,
              "elapsed_seconds": round(time.monotonic() - START, 6),
              "scope": "Finite ladder sanity checks only. Infinite-lattice proof is analytic. No exponent, novelty, or formal-proof certificate."}
    destination = ROOT / "measurements" / "boundary_exact.json"
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: result[key] for key in
                      ("verdict", "total_configurations", "variance_ratio_V2n_over_2Vn", "tube_identity_cases", "elapsed_seconds")}))


if __name__ == "__main__":
    main()
