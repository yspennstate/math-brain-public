"""Small exact checks of the deterministic inclusions; not an infinite-model proof."""
import heapq
import json
import random
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent
START = time.monotonic()


def check_budget():
    if time.monotonic() - START > 30:
        raise RuntimeError("Fresh 30-second compute gate exceeded")


def grid(n, seed):
    radius = 2 * n
    vertices = [(x, y) for x in range(-radius, radius + 1)
                for y in range(-radius, radius + 1)]
    if len(vertices) > 81:
        raise RuntimeError("Compute gate vertex bound exceeded")
    adjacency = {v: [] for v in vertices}
    generator = random.Random(seed)
    for x, y in vertices:
        for u in ((x + 1, y), (x, y + 1)):
            if u in adjacency:
                weight = 1 if seed is None else generator.randrange(1, 8)
                adjacency[(x, y)].append((u, weight))
                adjacency[u].append(((x, y), weight))
    return adjacency


def shortest_paths(adjacency, source):
    distances = {source: 0}
    queue = [(0, source)]
    while queue:
        distance, vertex = heapq.heappop(queue)
        if distance != distances[vertex]:
            continue
        for neighbor, weight in adjacency[vertex]:
            new = distance + weight
            if new < distances.get(neighbor, float("inf")):
                distances[neighbor] = new
                heapq.heappush(queue, (new, neighbor))
    return distances


def arms(adjacency, source, length):
    output = []

    def visit(path, cost):
        if len(path) == length + 1:
            output.append((path, cost, frozenset(path[1:])))
            return
        for neighbor, weight in adjacency[path[-1]]:
            if neighbor not in path:
                visit(path + (neighbor,), cost + weight)

    visit((source,), 0)
    return output


def centered_geodesic(adjacency, distances, vertex, length):
    choices = arms(adjacency, vertex, length)
    for first, first_cost, first_vertices in choices:
        for second, second_cost, second_vertices in choices:
            if first_vertices.isdisjoint(second_vertices):
                if first_cost + second_cost == distances[first[-1]][second[-1]]:
                    return True
    return False


def one_case(n, seed):
    adjacency = grid(n, seed)
    distances = {v: shortest_paths(adjacency, v) for v in adjacency}
    boundary = [v for v in adjacency if max(map(abs, v)) == 2 * n]
    interior = [v for v in adjacency if max(map(abs, v)) <= n]
    covered = []
    centered = []
    for vertex in interior:
        # Strictly positive weights ensure equality yields a SIMPLE minimizing path
        # through vertex: a repeated vertex in the concatenation would create a
        # positive loop and contradict optimality.
        member = any(distances[x][vertex] + distances[vertex][y] == distances[x][y]
                     for x in boundary for y in boundary if x != y)
        has_centered = centered_geodesic(adjacency, distances, vertex, n)
        if member and not has_centered:
            raise AssertionError(("D_n is not contained in H_n", n, seed, vertex))
        if n == 2 and has_centered:
            if not centered_geodesic(adjacency, distances, vertex, 1):
                raise AssertionError(("H_2 is not contained in H_1", seed, vertex))
        if member:
            covered.append(vertex)
        if has_centered:
            centered.append(vertex)
        check_budget()
    if seed is None and len(covered) != len(interior):
        raise AssertionError("Constant-weight model must cover all inner vertices")
    return {"n": n, "seed": seed, "vertices": len(adjacency),
            "inner_vertices": len(interior), "D_n_size": len(covered),
            "H_n_size_in_inner_box": len(centered), "inclusion": "PASS",
            "scope": "finite graph; random integer weights are diagnostic only"}


def main():
    cases = []
    for n in (1, 2):
        for seed in (None, 0, 1):
            cases.append(one_case(n, seed))
    radii = []
    for n in (8, 32, 128, 512):
        area = (2 * n + 1) ** 2
        lines = 2 * n + 1
        radii.append({"n": n, "crossing_horizontal_lines": lines,
                      "inner_vertices": area, "line_count_over_area": lines / area,
                      "occupied_density": 1, "source": "exact constant-weight formula"})
    # A partition example diagnoses endpoint union quantifiers without randomness:
    # an n^2-way uniform witness has marginal 1/n^2 but union probability 1.
    witnesses = [{"n": n, "endpoint_pairs": n * n,
                  "fixed_witness_probability": 1 / (n * n), "union_probability": 1}
                 for n in (2, 4, 16, 64)]
    result = {"command": "python -X utf8 check_congestion.py",
              "compute_gate": "COMPUTE_GATE.json", "finite_cases": cases,
              "inclusion_cases_passed": len(cases),
              "inner_vertex_cases_checked": sum(v["inner_vertices"] for v in cases),
              "constant_weight_density_counterexample": radii,
              "endpoint_partition_counterexample": witnesses,
              "elapsed_seconds": time.monotonic() - START,
              "parent_problem_solved": False,
              "limitations": "No iid continuous-law decay estimate and no infinite-model simulation."}
    (ROOT / "measurements.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"inclusion_cases_passed": result["inclusion_cases_passed"],
                      "inner_vertex_cases_checked": result["inner_vertex_cases_checked"],
                      "elapsed_seconds": round(result["elapsed_seconds"], 4),
                      "parent_problem_solved": False}))


if __name__ == "__main__":
    main()
