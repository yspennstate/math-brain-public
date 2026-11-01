"""Finite reproducibility checks for the two P0104 boundary lemmas.

This checks route geometry and explicit witnesses; the mathematical proof is in
ATTEMPT.md. It is not a formal proof of either lemma or of P0104.
"""
from heapq import heappop, heappush


def segment(a, b):
    x, y = a
    tx, ty = b
    assert (x == tx) != (y == ty)
    dx = (tx > x) - (tx < x)
    dy = (ty > y) - (ty < y)
    edges = []
    while (x, y) != (tx, ty):
        nxt = (x + dx, y + dy)
        edges.append(frozenset(((x, y), nxt)))
        x, y = nxt
    return edges


def route(turns):
    return [edge for a, b in zip(turns, turns[1:]) for edge in segment(a, b)]


def paths(n):
    return [
        route([(0, 0), (n, 0)]),
        route([(0, 0), (0, 1), (n, 1), (n, 0)]),
        route([(0, 0), (0, -1), (n, -1), (n, 0)]),
        route([(0, 0), (-1, 0), (-1, 2), (n + 1, 2), (n + 1, 0), (n, 0)]),
    ]


def shortest(n, a, b, straight_high=True):
    # All edges have weight a, except the straight-axis edges which have b.
    # A positive a lets a finite box witness the strict detour outside the
    # universal straight-path threshold.
    start, goal = (0, 0), (n, 0)
    box = (-2, n + 2, -2, 2)
    heap, distance = [(0.0, start)], {start: 0.0}
    while heap:
        cost, (x, y) = heappop(heap)
        if cost != distance[(x, y)]:
            continue
        if (x, y) == goal:
            return cost
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx, ny = x + dx, y + dy
            if not (box[0] <= nx <= box[1] and box[2] <= ny <= box[3]):
                continue
            on_axis = y == ny == 0 and 0 <= min(x, nx) < max(x, nx) <= n
            weight = b if on_axis and straight_high else a
            new_cost = cost + weight
            if new_cost < distance.get((nx, ny), float("inf")):
                distance[(nx, ny)] = new_cost
                heappush(heap, (new_cost, (nx, ny)))
    raise AssertionError("goal missing")


for n in range(1, 33):
    four = paths(n)
    assert tuple(map(len, four)) == (n, n + 2, n + 2, n + 8)
    assert sum(len(path) for path in four) == len(set().union(*map(set, four)))

assert shortest(4, 1, 1.5) == 6  # threshold equality; straight ties a detour
assert shortest(3, 1, 2) == 5  # threshold violated; a detour beats straight=6

theta = 2 / 3
n, epsilon = 1000, 1 / 1000
assert n * epsilon <= 2
edge_variance = epsilon**2 / 12
passage_variance = n * edge_variance
ratio = passage_variance / (edge_variance * n**theta)
assert ratio > 9.9  # n^(1/3) is 10 up to floating-point error
print(f"PASS: 32 four-route checks; sharp examples 6=6 and 5<6; ratio={ratio:.6f}")
