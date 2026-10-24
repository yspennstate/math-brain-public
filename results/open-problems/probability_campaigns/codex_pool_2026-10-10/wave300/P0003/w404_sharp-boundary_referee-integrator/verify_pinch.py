"""Bounded, exact rational verification of the P0003 auxiliary counterexample."""
from __future__ import annotations

from fractions import Fraction as F
from pathlib import Path
import json
import math
import time

ROOT = Path(__file__).resolve().parent
ANCHORS = [(-2, F(0)), (0, F(0)), (0, F(3)), (1, F(3)),
           (1, F(0)), (0, F(0)), (0, F(-3, 2)), (2, F(-3, 2))]


def horizontal(start: tuple[int, int], end_i: int) -> list[tuple[int, int]]:
    i, j = start
    step = 1 if end_i > i else -1
    return [(k, j) for k in range(i, end_i + step, step)]


def vertical(start: tuple[int, int], end_j: int,
             cols: tuple[int, int]) -> list[tuple[int, int]]:
    i, j = start
    direction = 1 if end_j > j else -1
    route = [(i, j)]
    while j != end_j:
        assert (i + j) % 2 == (0 if direction == 1 else 1)
        j += direction
        route.append((i, j))
        if j != end_j:
            i = cols[1] if i == cols[0] else cols[0]
            route.append((i, j))
    return route


def honeycomb_route(n: int) -> list[list[tuple[int, int]]]:
    assert n >= 8 and n % 2 == 0
    routes = [horizontal((-4 * n, 0), -4)]
    routes.append(vertical(routes[-1][-1], 2 * n, (-4, -3)))
    routes.append(horizontal(routes[-1][-1], 2 * n - 1))
    routes.append(vertical(routes[-1][-1], 0, (2 * n - 1, 2 * n)))
    routes.append(horizontal(routes[-1][-1], 3))
    routes.append(vertical(routes[-1][-1], -n, (3, 4)))
    routes.append(horizontal(routes[-1][-1], 4 * n))
    return routes


def rational_xy(v: tuple[int, int], n: int) -> tuple[F, F]:
    """Physical x is sqrt(3) times the first returned coefficient."""
    i, j = v
    return F(i, 2 * n), F(3 * j - ((i + j) % 2), 2 * n)


def distance_squared(p: tuple[F, F], q: tuple[F, F]) -> F:
    return 3 * (p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2


def is_edge(u: tuple[int, int], v: tuple[int, int]) -> bool:
    i, j = u
    k, l = v
    if j == l and abs(i - k) == 1:
        return True
    if i == k and abs(j - l) == 1:
        lower_j = min(j, l)
        return (i + lower_j) % 2 == 0
    return False


def check_case(n: int) -> dict:
    routes = honeycomb_route(n)
    path = routes[0] + [v for route in routes[1:] for v in route[1:]]
    assert len(path) == len(set(path)), "Repeated lattice vertex"
    assert len(path) - 1 == 22 * n - 12
    assert path[0] == (-4 * n, 0) and path[-1] == (4 * n, -n)
    for u, v in zip(path, path[1:]):
        assert is_edge(u, v), (u, v)
        assert distance_squared(rational_xy(u, n), rational_xy(v, n)) == F(1, n * n)
    for v in path[1:-1]:
        x, y = rational_xy(v, n)
        assert -2 < x < 2 and -2 < y < 4
    maximum_squared_error = F(0)
    maximum_vertical_error = F(0)
    for section, route in enumerate(routes):
        m = len(route) - 1
        left, right = ANCHORS[section:section + 2]
        assert F(7 * m, n) <= 28
        for k, v in enumerate(route):
            r = F(k, m)
            target = (F(left[0]) + r * (right[0] - left[0]),
                      F(left[1]) + r * (right[1] - left[1]))
            actual = rational_xy(v, n)
            maximum_squared_error = max(maximum_squared_error,
                                        distance_squared(actual, target))
            maximum_vertical_error = max(maximum_vertical_error, abs(actual[1] - target[1]))
    # On each edge interval both paths are affine. The squared norm of their
    # difference is convex, so its maximum occurs at an interval endpoint.
    # Thus checking vertices proves the whole continuous uniform bound.
    assert maximum_squared_error <= F(25, n * n)
    assert maximum_vertical_error <= F(1, n)
    neck_squared = distance_squared(rational_xy(routes[0][-1], n),
                                    rational_xy(routes[4][-1], n))
    assert neck_squared == F(37, n * n)
    excursion_squared = distance_squared(rational_xy(routes[1][-1], n),
                                         rational_xy(routes[3][-1], n))
    assert excursion_squared > 1
    return {
        "N": n,
        "vertices": len(path),
        "edges": len(path) - 1,
        "unique_vertices": len(set(path)),
        "section_edge_counts": [len(x) - 1 for x in routes],
        "maximum_speed": float(max(F(7 * (len(x) - 1), n) for x in routes)),
        "uniform_error_squared_exact": str(maximum_squared_error),
        "uniform_error": math.sqrt(float(maximum_squared_error)),
        "uniform_error_upper_bound": 5 / n,
        "neck_distance_squared_exact": str(neck_squared),
        "neck_distance": math.sqrt(float(neck_squared)),
        "excursion_diameter_lower_bound": math.sqrt(float(excursion_squared)),
        "honeycomb_edges_valid": True,
        "inside_fixed_domain": True,
        "vertex_simple": True,
        "continuous_uniform_bound_verified": True,
    }


def main() -> None:
    started = time.monotonic()
    gate = json.loads((ROOT / "COMPUTE_GATE.json").read_text(encoding="utf-8"))
    results = []
    total_vertices = 0
    for n in gate["N_values"]:
        result = check_case(n)
        total_vertices += result["vertices"]
        assert result["vertices"] <= gate["maximum_vertices_per_case"]
        assert total_vertices <= gate["maximum_total_vertices"]
        assert time.monotonic() - started < gate["wall_seconds_cap"]
        results.append(result)
    output = {
        "command": "python -X utf8 ~/brain_workers/w403/check_honeycomb_pinch.py",
        "cases_checked": len(results),
        "total_vertices_checked": total_vertices,
        "all_passed": True,
        "arithmetic": "exact rational comparisons; displayed distances are floats",
        "runtime_seconds": time.monotonic() - started,
        "cases": results,
        "limiting_trace_contains_closed_rectangle": {
            "width": "sqrt(3)", "height": 3, "enclosed_area": "3*sqrt(3)"},
        "scope": "finite reproducibility checks of an auxiliary counterexample; not proof of P0003",
    }
    destination = ROOT / "measurements" / "honeycomb_pinch.json"
    destination.parent.mkdir(exist_ok=True)
    destination.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
