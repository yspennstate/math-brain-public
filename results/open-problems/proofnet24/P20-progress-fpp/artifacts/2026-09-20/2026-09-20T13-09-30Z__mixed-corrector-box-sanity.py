#!/usr/bin/env python3
"""
Exact rational sanity checks for P20's mixed-corrector upper-corner box theorem.

This is supplementary finite checking only. It does not prove asymptotic FPP
strict convexity. All arithmetic in the checker is fractions.Fraction.
"""
from fractions import Fraction
import heapq
import itertools


def dijkstra(vertices, adj, src):
    dist = {v: None for v in vertices}
    dist[src] = Fraction(0)
    pq = [(Fraction(0), src)]
    while pq:
        d, v = heapq.heappop(pq)
        if dist[v] != d:
            continue
        for w, c in adj[v]:
            nd = d + c
            if dist[w] is None or nd < dist[w]:
                dist[w] = nd
                heapq.heappush(pq, (nd, w))
    return dist


def build_env(seed, cols=4, rows=5):
    vertices = [(x, r) for x in range(cols + 1) for r in range(rows)]
    adj = {v: [] for v in vertices}
    def wt(code):
        val = ((code * 37 + seed * 53) % 17) + 4
        return Fraction(val, 10)
    edge_id = 0
    for x in range(cols + 1):
        for r in range(rows):
            if x < cols:
                c = wt(edge_id + 11); edge_id += 1
                a, b = (x, r), (x + 1, r)
                adj[a].append((b, c)); adj[b].append((a, c))
            if r + 1 < rows:
                c = wt(edge_id + 101); edge_id += 1
                a, b = (x, r), (x, r + 1)
                adj[a].append((b, c)); adj[b].append((a, c))
    return vertices, adj


M = 5
ENVS = []
for seed in [1, 2, 3, 4]:
    vertices, adj = build_env(seed)
    inputs = [(0, r) for r in range(M)]
    outputs = [(4, r) for r in range(M)]
    D = []
    for src in inputs:
        ds = dijkstra(vertices, adj, src)
        D.append([ds[o] for o in outputs])
    chain = [next(c for w, c in adj[(4, r)] if w == (4, r + 1)) for r in range(M - 1)]
    row_path = []
    for r in range(M):
        total = Fraction(0)
        for x in range(4):
            total += next(c for w, c in adj[(x, r)] if w == (x + 1, r))
        row_path.append(total)
    ENVS.append((D, chain, row_path))

KAPPA = Fraction(1, 2)
ALPHA = [Fraction(0), Fraction(1, 20), Fraction(1, 10), Fraction(1, 20), Fraction(0)]
A = sum(ALPHA)
assert KAPPA + A <= 1
assert sum(Fraction(j) * ALPHA[j] for j in range(M)) == A * Fraction(M - 1, 2)


def F_of(D, y):
    return [min(y[i] + D[i][j] for i in range(M)) for j in range(M)]


def Q_of(D, y):
    F = F_of(D, y)
    return ((1 - KAPPA - A) * min(F) + KAPPA * max(F)
            + sum(ALPHA[j] * F[j] for j in range(M)))


def B_of(y):
    eQ = sum(Q_of(D, y) for D, _, _ in ENVS) / len(ENVS)
    return eQ - KAPPA * (max(y) - min(y)) - sum(ALPHA[i] * y[i] for i in range(M))


def box_corner_bound(lower, upper):
    eQ = sum(Q_of(D, upper) for D, _, _ in ENVS) / len(ENVS)
    return eQ - KAPPA * max(lower) - sum(ALPHA[i] * lower[i] for i in range(M))


vals = [Fraction(0), Fraction(1, 2), Fraction(1), Fraction(3, 2), Fraction(2)]
profiles = [p for p in itertools.product(vals, repeat=M) if min(p) == 0]

monotonicity_checks = 0
for D, _, _ in ENVS:
    for y in profiles[::17]:
        for z in profiles[::19]:
            if all(y[i] <= z[i] for i in range(M)):
                assert Q_of(D, y) <= Q_of(D, z)
                monotonicity_checks += 1

boxes = []
for anchor in range(M):
    patterns = [
        [0, 0, 0, 0, 0],
        [0, Fraction(1, 2), 1, Fraction(3, 2), 2],
        [2, Fraction(3, 2), 1, Fraction(1, 2), 0],
        [1, 0, Fraction(3, 2), Fraction(1, 2), 2],
    ]
    for pattern in patterns:
        lower = [Fraction(x) for x in pattern]; lower[anchor] = Fraction(0)
        upper = [x + Fraction(1, 2) for x in lower]; upper[anchor] = Fraction(0)
        boxes.append((anchor, tuple(lower), tuple(upper)))

box_profile_checks = 0
max_box_slack = Fraction(0)
for anchor, lower, upper in boxes:
    bound = box_corner_bound(lower, upper)
    grids = []
    for i in range(M):
        grids.append([Fraction(0)] if i == anchor else [lower[i], (lower[i] + upper[i]) / 2, upper[i]])
    for y in itertools.product(*grids):
        slack = bound - B_of(y)
        assert min(y) == 0 and slack >= 0
        max_box_slack = max(max_box_slack, slack)
        box_profile_checks += 1

reset_checks = 0
for D, chain, row_path in ENVS:
    chain_total = sum(chain)
    weighted_radii = []
    for k in range(M):
        radius = Fraction(0)
        for j in range(M):
            lo, hi = min(j, k), max(j, k)
            radius += ALPHA[j] * sum(chain[lo:hi])
        weighted_radii.append(radius)
    alpha_chain = max(weighted_radii)
    for y in profiles[::13]:
        F = F_of(D, y); g = min(F); phi = [v - g for v in F]
        assert max(phi) - min(phi) <= chain_total
        assert sum(ALPHA[j] * phi[j] for j in range(M)) <= alpha_chain
        anchor = next(i for i, v in enumerate(y) if v == 0)
        assert g <= row_path[anchor]
        reset_checks += 1

print("P20-T10-MIXED-CORRECTOR-BOX-SANITY")
print("environments =", len(ENVS))
print("profiles =", len(profiles))
print("monotonicity_checks =", monotonicity_checks)
print("boxes =", len(boxes))
print("box_profile_checks =", box_profile_checks)
print("reset_checks =", reset_checks)
print("kappa =", KAPPA, "alpha =", ALPHA, "A =", A)
print("centered_moment =", sum(Fraction(j) * ALPHA[j] for j in range(M)))
print("max_box_slack =", max_box_slack)
print("ALL_EXACT_FRACTION_CHECKS_PASS")
