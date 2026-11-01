#!/usr/bin/env python3
"""Exact certificate for improved I0075 counterexample.

Cities: Z^2. Start with square grid. Select every unit square with lower-left
corner (a,b) satisfying a+3b == 0 mod 8. Delete its four sides and add the
center-to-corner star. Selected squares are edge-disjoint. For city routing,
each star is represented by the metric closure K4 on the four corners, every
shortcut costing sqrt(2), because the two spoke lengths sum to sqrt(2).

The proof has:
  * exact density calculation: L=(6+sqrt(2))/4 < (14+2sqrt(2))/9 < 2;
  * exact finite macro certificates for 8Z^2 translations;
  * exact residual certificates for e in [-4,4]^2;
  * analytic large-distance bound for ||d|| >= 130 using a 13/10 macro
    coefficient;
  * exact all-phase/all-displacement finite core for 0<||d||<130.

All comparisons relevant to the proof use integer arithmetic in Q(sqrt(2)).
"""
from heapq import heappush, heappop
from functools import total_ordering

LO, HI = -170, 180
MAX_CUTOFF = (186, 0)
RADIUS = 130


def sign_qsqrt2(p, q):
    """Exact sign of p + q*sqrt(2), p,q integers."""
    if p == 0:
        return (q > 0) - (q < 0)
    if q == 0:
        return (p > 0) - (p < 0)
    if p > 0 and q > 0:
        return 1
    if p < 0 and q < 0:
        return -1
    if p > 0 and q < 0:
        c = p*p - 2*q*q
        return (c > 0) - (c < 0)
    c = 2*q*q - p*p
    return (c > 0) - (c < 0)


def alg_lt(x, y):
    return sign_qsqrt2(x[0]-y[0], x[1]-y[1]) < 0


def alg_leq(x, y):
    return sign_qsqrt2(x[0]-y[0], x[1]-y[1]) <= 0


@total_ordering
class HeapItem:
    __slots__ = ("a", "b", "v")
    def __init__(self, a, b, v):
        self.a, self.b, self.v = a, b, v
    def __lt__(self, other):
        s = sign_qsqrt2(self.a-other.a, self.b-other.b)
        return (s < 0) if s else (self.v < other.v)
    def __eq__(self, other):
        return (self.a, self.b, self.v) == (other.a, other.b, other.v)


def selected_square(a, b):
    return (a + 3*b) % 8 == 0


def deleted_unit_edge(x1, y1, x2, y2):
    assert abs(x1-x2) + abs(y1-y2) == 1
    if y1 == y2:
        x, y = min(x1, x2), y1
        return selected_square(x, y) or selected_square(x, y-1)
    x, y = x1, min(y1, y2)
    return selected_square(x, y) or selected_square(x-1, y)


def incident_selected_squares(x, y):
    for a in (x, x-1):
        for b in (y, y-1):
            if selected_square(a, b):
                yield a, b


def neighbors(v):
    x, y = v
    for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
        nx, ny = x+dx, y+dy
        if LO <= nx <= HI and LO <= ny <= HI:
            if not deleted_unit_edge(x, y, nx, ny):
                yield (nx, ny), (1, 0)
    for a, b in incident_selected_squares(x, y):
        for w in ((a,b),(a+1,b),(a,b+1),(a+1,b+1)):
            if w != v and LO <= w[0] <= HI and LO <= w[1] <= HI:
                yield w, (0, 1)


def dijkstra_exact(src):
    dist = {src: (0, 0)}
    pred = {src: None}
    pq = [HeapItem(0, 0, src)]
    while pq:
        item = heappop(pq)
        v = item.v
        cur = dist.get(v)
        if cur != (item.a, item.b):
            continue
        if not alg_leq(cur, MAX_CUTOFF):
            break
        A, B = cur
        for w, (da, db) in neighbors(v):
            nd = (A+da, B+db)
            if w not in dist or alg_lt(nd, dist[w]):
                dist[w] = nd
                pred[w] = (v, (da, db))
                heappush(pq, HeapItem(nd[0], nd[1], w))
    return dist, pred


def check_predecessor_certificate(src, dist, pred):
    """Every discovered label has a strictly shorter valid predecessor."""
    for v, dv in dist.items():
        if v == src:
            assert dv == (0,0) and pred[v] is None
            continue
        assert pred[v] is not None
        u, cost = pred[v]
        assert u in dist
        assert alg_lt(dist[u], dv)
        assert dv == (dist[u][0]+cost[0], dist[u][1]+cost[1])
        assert any(w == v and c == cost for w, c in neighbors(u))


def route_leq_source_bound(A, B, dx, dy):
    """Exact check A+B*sqrt2 <= sqrt2*sqrt(dx^2+dy^2)."""
    R2 = dx*dx + dy*dy
    C = 2*R2 - (A*A + 2*B*B)
    if C < 0:
        return False
    return C*C >= 8*A*A*B*B


# Exact scalar checks used by the written analytic proof.
assert sign_qsqrt2(6-8, 1) < 0
# Improvement over period-3 witness: 9(6+s) < 4(14+2s) iff s<2.
assert sign_qsqrt2(-2, 1) < 0
# sqrt(62+32s)/8 < 13/10 follows from 400s<577.
assert 577*577 > 2*400*400
assert 2*10*10 > 13*13
# At R=130, the large-distance margin is (619s-875)/5 > 0.
assert 2*619*619 > 875*875

AXIAL = (6, 2)
DIAGONAL = (10, 3)
RESIDUAL = (6, 1)

axial_vecs = ((8,0),(-8,0),(0,8),(0,-8))
diag_vecs = ((8,8),(8,-8),(-8,8),(-8,-8))

checked_core = 0
checked_residual = 0
checked_macro = 0
nodes_total = 0
phase_summaries = []

for rho in range(8):
    src = (rho, 0)
    dist, pred = dijkstra_exact(src)
    check_predecessor_certificate(src, dist, pred)
    nodes_total += len(dist)

    for dx, dy in axial_vecs:
        t = (src[0]+dx, src[1]+dy)
        assert t in dist
        assert alg_leq(dist[t], AXIAL), (rho, (dx,dy), dist[t])
        checked_macro += 1
    for dx, dy in diag_vecs:
        t = (src[0]+dx, src[1]+dy)
        assert t in dist
        assert alg_leq(dist[t], DIAGONAL), (rho, (dx,dy), dist[t])
        checked_macro += 1

    local_res_max = (0,0)
    for ex in range(-4, 5):
        for ey in range(-4, 5):
            t = (src[0]+ex, src[1]+ey)
            assert t in dist
            assert alg_leq(dist[t], RESIDUAL), (rho, (ex,ey), dist[t])
            if alg_lt(local_res_max, dist[t]):
                local_res_max = dist[t]
            checked_residual += 1

    local_core = 0
    for dx in range(-(RADIUS-1), RADIUS):
        for dy in range(-(RADIUS-1), RADIUS):
            if dx == 0 and dy == 0:
                continue
            if dx*dx + dy*dy >= RADIUS*RADIUS:
                continue
            t = (src[0]+dx, src[1]+dy)
            assert t in dist, ("missing target", rho, (dx,dy))
            A, B = dist[t]
            assert route_leq_source_bound(A, B, dx, dy), (
                "stretch failure", rho, (dx,dy), (A,B)
            )
            checked_core += 1
            local_core += 1

    phase_summaries.append((rho, len(dist), local_core, local_res_max))

assert checked_macro == 8 * 8
assert checked_residual == 8 * 81
assert checked_core == 8 * 53040

print("I0075_PERIOD8_STAR_EXACT_CERTIFICATE")
print("selected_squares: a+3b == 0 mod 8")
print("density=(6+sqrt(2))/4 < (14+2*sqrt(2))/9 < 2 : PASS")
print("macro_axial_bound=6+2*sqrt(2) for +-8 axes : PASS")
print("macro_diagonal_bound=10+3*sqrt(2) for +-8,+-8 diagonals : PASS")
print("macro_cauchy_coefficient < 13/10 : PASS")
print("residual_box=[-4,4]^2 route_bound <= 6+sqrt(2) : PASS")
print("large_radius_threshold R>=130 : PASS")
print("source_phases=8")
print("finite_nonzero_displacements_per_phase=53040")
print("finite_cases_checked=%d" % checked_core)
print("macro_cases_checked=%d" % checked_macro)
print("residual_cases_checked=%d" % checked_residual)
print("discovered_nodes_total=%d" % nodes_total)
for row in phase_summaries:
    print("phase_summary=%r" % (row,))
print("finite_stretch_failures=0")
print("ALL_ASSERTIONS_PASSED")
