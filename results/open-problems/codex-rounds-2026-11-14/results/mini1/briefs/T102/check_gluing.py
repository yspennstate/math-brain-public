#!/usr/bin/env python3
"""Exact rational checks of PROOF.md; standard library only, one process."""

import csv
from fractions import Fraction as F
import itertools
import json
import os
from pathlib import Path
import resource
import signal

ROOT = Path(__file__).resolve().parent
os.chdir(ROOT)
signal.alarm(120)
resource.setrlimit(resource.RLIMIT_CPU, (90, 90))
# The largest dense matrix below has 66 rows; no scientific-library imports.
# macOS rejects lowering AS and DATA limits in this sandbox. The largest
# matrix has 66 rows; check and report the actual resident-memory high-water mark.
assert os.environ.get("OMP_NUM_THREADS") == "1"
priority = os.getpriority(os.PRIO_PROCESS, 0)
assert priority >= 15, priority


def solve(matrix, rhs):
    """Gauss-Jordan elimination over the rationals, without tolerance tests."""
    n = len(rhs)
    a = [[F(v) for v in row] + [F(b)] for row, b in zip(matrix, rhs)]
    for k in range(n):
        pivot = next(i for i in range(k, n) if a[i][k])
        a[k], a[pivot] = a[pivot], a[k]
        c = a[k][k]
        a[k] = [v / c for v in a[k]]
        for i in range(n):
            if i != k and a[i][k]:
                c = a[i][k]
                a[i] = [u - c * v for u, v in zip(a[i], a[k])]
    return [a[i][-1] for i in range(n)]


def nodes(edges):
    return sorted({v for u, v, r in edges} | {u for u, v, r in edges})


def connected(edges, required):
    seen = {required[0]}
    while True:
        enlarged = seen | {v for u, v, r in edges if u in seen}
        enlarged |= {u for u, v, r in edges if v in seen}
        if enlarged == seen:
            return set(required) <= seen
        seen = enlarged


def currents(edges, injection):
    """Solve Kirchhoff equations, grounding separately in each component."""
    adjacency = {v: set() for v in nodes(edges)}
    for u, v, r in edges:
        adjacency[u].add(v)
        adjacency[v].add(u)
    unseen = set(adjacency)
    potential = {}
    while unseen:
        component = {min(unseen)}
        frontier = set(component)
        while frontier:
            new = set().union(*(adjacency[v] for v in frontier)) - component
            component |= new
            frontier = new
        unseen -= component
        assert sum(injection.get(v, 0) for v in component) == 0
        ground = min(component)
        free = sorted(component - {ground})
        index = {v: i for i, v in enumerate(free)}
        lap = [[F(0) for _ in free] for _ in free]
        for u, v, r in edges:
            if u not in component:
                continue
            c = F(1, r)
            if u != ground:
                lap[index[u]][index[u]] += c
            if v != ground:
                lap[index[v]][index[v]] += c
            if u != ground and v != ground:
                lap[index[u]][index[v]] -= c
                lap[index[v]][index[u]] -= c
        values = solve(lap, [injection.get(v, 0) for v in free])
        potential[ground] = F(0)
        potential.update(zip(free, values))
    result = [(potential[u] - potential[v]) / r for u, v, r in edges]
    divergence = {v: F(0) for v in adjacency}
    for (u, v, r), f in zip(edges, result):
        divergence[u] += f
        divergence[v] -= f
    assert all(divergence[v] == injection.get(v, 0) for v in divergence)
    return result


def energy(edges, flow):
    return sum((r * f * f for (u, v, r), f in zip(edges, flow)), F(0))


def wired(edges, left, right):
    """Return optimal unit flow on original edges, after terminal contraction."""
    assert set(left).isdisjoint(right)
    mapping = {v: "@L" if v in left else "@R" if v in right else v
               for v in nodes(edges)}
    quotient = [(mapping[u], mapping[v], r) for u, v, r in edges
                if mapping[u] != mapping[v]]
    f = iter(currents(quotient, {"@L": 1, "@R": -1}))
    return [next(f) if mapping[u] != mapping[v] else F(0)
            for u, v, r in edges]


def profile(edges, flow, interface, sign):
    d = {v: F(0) for v in interface}
    for (u, v, r), f in zip(edges, flow):
        if u in d:
            d[u] += sign * f
        if v in d:
            d[v] -= sign * f
    return [d[v] for v in interface]


def matrix_q(edges, interface):
    basis = [{v: F(int(v == interface[i]) - int(v == interface[-1]))
              for v in interface} for i in range(len(interface) - 1)]
    flow = [currents(edges, b) for b in basis]
    return [[sum((r * f * g for (u, v, r), f, g in zip(edges, fi, fj)), F(0))
             for fj in flow] for fi in flow]


def inverse(matrix):
    n = len(matrix)
    cols = [solve(matrix, [int(i == j) for i in range(n)]) for j in range(n)]
    return [[cols[j][i] for j in range(n)] for i in range(n)]


def check_two(a_edges, b_edges, interface):
    fa = wired(a_edges, ["x"], interface)
    fb = wired(b_edges, interface, ["y"])
    ra, rb = energy(a_edges, fa), energy(b_edges, fb)
    qa = profile(a_edges, fa, interface, -1)
    qb = profile(b_edges, fb, interface, 1)
    ma, mb = matrix_q(a_edges, interface), matrix_q(b_edges, interface)
    ia, ib = inverse(ma), inverse(mb)
    delta = [u - v for u, v in zip(qa[:-1], qb[:-1])]
    k = [[u + v for u, v in zip(ai, bi)] for ai, bi in zip(ia, ib)]
    w = solve(k, delta)
    correction = sum((u * v for u, v in zip(delta, w)), F(0))
    edges = a_edges + b_edges
    whole_flow = currents(edges, {"x": 1, "y": -1})
    whole = energy(edges, whole_flow)
    assert whole == ra + rb + correction
    assert correction >= 0
    assert (correction == 0) == (qa == qb)
    return ra, rb, whole, correction


def cycle(length):
    def path(start, end, count, prefix):
        vertices = [start] + [prefix + str(i) for i in range(count - 1)] + [end]
        return [(u, v, 1) for u, v in zip(vertices, vertices[1:])]
    return (path("x", "u", 1, "a") + path("x", "v", length, "b"),
            path("u", "y", length, "c") + path("v", "y", 1, "d"))


cycle_rows = []
for length in [1, 2, 3, 4, 8, 16, 32]:
    a, b = cycle(length)
    ra, rb, whole, correction = check_two(a, b, ["u", "v"])
    assert ra == rb == F(length, length + 1)
    assert whole == F(length + 1, 2)
    assert correction == F((length - 1)**2, 2 * (length + 1))
    cycle_rows.append([length, str(ra), str(rb), str(whole), str(correction),
                       str(whole / (ra + rb))])
with (ROOT / "cycle_data.csv").open("w", newline="") as out:
    writer = csv.writer(out)
    writer.writerow(["L", "R_A", "R_B", "R_full", "D", "ratio"])
    writer.writerows(cycle_rows)

# Exhaust all assignments of three interface edges: absent, A, or B.
# Also exhaust nonempty terminal neighbor sets; retain connected A and B.
interface = ["u", "v", "w"]
pairs = list(itertools.combinations(interface, 2))
rows = []
for left_mask in range(1, 8):
    for right_mask in range(1, 8):
        for choices in itertools.product(range(3), repeat=3):
            a = [("x", s, 1) for i, s in enumerate(interface) if left_mask >> i & 1]
            b = [(s, "y", 1) for i, s in enumerate(interface) if right_mask >> i & 1]
            a += [(u, v, 1) for (u, v), choice in zip(pairs, choices) if choice == 1]
            b += [(u, v, 1) for (u, v), choice in zip(pairs, choices) if choice == 2]
            if not connected(a, ["x"] + interface) or not connected(b, ["y"] + interface):
                continue
            ra, rb, whole, correction = check_two(a, b, interface)
            rows.append([left_mask, right_mask, "".join(map(str, choices)),
                         str(ra), str(rb), str(whole), str(correction)])
with (ROOT / "interface_data.csv").open("w", newline="") as out:
    writer = csv.writer(out)
    writer.writerow(["left_mask", "right_mask", "interface_assignment",
                     "R_A", "R_B", "R_full", "D"])
    writer.writerows(rows)

# Independent combinatorial counts: for k interface edges, the numbers of
# terminal-neighbor subsets meeting every interface component are 1,3,7,7.
from math import factorial
neighbor_counts = [1, 3, 7, 7]
count_by_components = sum(
    factorial(3) // (factorial(ka) * factorial(kb) * factorial(3 - ka - kb))
    * neighbor_counts[ka] * neighbor_counts[kb]
    for ka in range(4) for kb in range(4 - ka))
assert len(rows) == count_by_components == 255
# Wired current profiles agree iff terminal neighbor masks agree. Equal
# masks of size 1 allow no assignments, size 2 allow 6 each, size 3 allow 27.
assert sum(F(row[-1]) == 0 for row in rows) == 3 * 6 + 27 == 45
assert all((F(row[-1]) == 0) == (row[0] == row[1]) for row in rows)

# Disconnected middle layer: x--u--p--y and x--v--q--y.
# The two middle edges have unequal resistances, and no within-layer connection.
pieces = [[("x", "u", 1), ("x", "v", 1)],
          [("u", "p", 1), ("v", "q", 3)],
          [("p", "y", 1), ("q", "y", 1)]]
boundaries = [["x"], ["u", "v"], ["p", "q"], ["y"]]
theta = [wired(e, left, right) for e, left, right
         in zip(pieces, boundaries, boundaries[1:])]
all_edges = sum(pieces, [])
global_flow = currents(all_edges, {"x": 1, "y": -1})
offset = 0
ri = []
corrections = []
for e, t in zip(pieces, theta):
    f = global_flow[offset:offset + len(e)]
    offset += len(e)
    eta = [u - v for u, v in zip(f, t)]
    assert sum((r * u * v for (x, y, r), u, v in zip(e, t, eta)), F(0)) == 0
    ri.append(energy(e, t))
    corrections.append(energy(e, eta))
disconnected_full = energy(all_edges, global_flow)
assert disconnected_full == F(15, 8)  # independent parallel paths 3 and 5
assert disconnected_full == sum(ri) + sum(corrections)
assert sum(corrections) == F(1, 8)

df = F(91, 48)
ao_beta = df / 2
assert 2 * df / (df + ao_beta) == F(4, 3)
assert df + ao_beta == F(91, 32)

summary = {
    "effective_nice": priority,
    "OMP_NUM_THREADS": os.environ["OMP_NUM_THREADS"],
    "peak_RSS_bytes_macOS": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
    "cycle_cases": len(cycle_rows),
    "three_vertex_interface_cases": len(rows),
    "nonzero_correction_cases": sum(F(row[-1]) > 0 for row in rows),
    "disconnected_layer_R_i": list(map(str, ri)),
    "disconnected_layer_correction_energies": list(map(str, corrections)),
    "disconnected_layer_R_full": str(disconnected_full),
    "AO_beta": str(ao_beta),
    "AO_walk_dimension": str(df + ao_beta),
    "result": "all exact rational checks passed",
}
assert summary["peak_RSS_bytes_macOS"] < 1024**3
(ROOT / "validation_summary.json").write_text(json.dumps(summary, indent=2) + "\n")
print(json.dumps(summary, indent=2))
