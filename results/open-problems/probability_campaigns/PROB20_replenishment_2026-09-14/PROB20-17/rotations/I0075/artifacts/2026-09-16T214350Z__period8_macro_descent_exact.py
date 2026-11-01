#!/usr/bin/env python3
"""Exact simplified all-pairs stretch certificate for I0075 period-8 star network.

Network N8:
  select unit squares with lower-left (a,b) satisfying a+3b == 0 mod 8;
  delete four boundary grid edges and add center-to-corner star.

This certificate proves:
  * phase-uniform macro routes for axis vectors (+/-8,0),(0,+/-8),
    each of cost <= A=6+2*sqrt(2);
  * phase-uniform macro routes for diagonal vectors (+/-16,+/-16),
    each of cost <= D=18+7*sqrt(2);
  * the normalized macro vectors v/c form an octagon with inradius > 3/4;
  * the resulting macro-descent inequality holds for every displacement
    of Euclidean norm >= 52;
  * all eight phases and all nonzero integer displacements of norm < 52
    satisfy the source stretch bound exactly.

All proof comparisons are exact in Q(sqrt(2)); no floating point decides a claim.
"""
from heapq import heappush, heappop
from functools import total_ordering

LO, HI = -90, 100
MAX_CUTOFF = (76, 0)
RADIUS = 52


def sign_qsqrt2(p, q):
    """Exact sign of p + q*sqrt(2), integers p,q."""
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


def check_predecessors(src, dist, pred):
    for v, dv in dist.items():
        if v == src:
            assert dv == (0,0) and pred[v] is None
            continue
        u, cost = pred[v]
        assert u in dist
        assert alg_lt(dist[u], dv)
        assert dv == (dist[u][0]+cost[0], dist[u][1]+cost[1])
        assert any(w == v and c == cost for w, c in neighbors(u))


def route_leq_source(A, B, dx, dy):
    """Exact check A+B sqrt2 <= sqrt(2)*sqrt(dx^2+dy^2)."""
    R2 = dx*dx + dy*dy
    C = 2*R2 - (A*A + 2*B*B)
    if C < 0:
        return False
    return C*C >= 8*A*A*B*B


# Analytic macro geometry, exact scalar checks.
# A = 6+2s, D = 18+7s.
A = (6, 2)
D = (18, 7)

# Coordinates of normalized macro vertices:
# a=8/A=(12-4s)/7, b=16/D=(144-56s)/113.
# Convex-octagon ordering needs a>b and 2b>a.
assert sign_qsqrt2(348, -60) > 0       # numerator of a-b after common positive denom
assert sign_qsqrt2(660, -332) > 0      # numerator of 2b-a after common positive denom

# Squared distance h^2 from origin to each octagon edge is
# (14720-8448s)/4513. Verify h^2 > 9/16.
assert sign_qsqrt2(194903, -135168) > 0

# Descent threshold r>=52.
# E_A = 2|v|^2-A^2 = 84-24s.
# (3-2s)*52*A - E_A = 436-288s >0.
assert sign_qsqrt2(436, -288) > 0
# E_D = 2|v|^2-D^2 = 602-252s.
# (3-2s)*52*D - E_D = 750-528s >0.
assert sign_qsqrt2(750, -528) > 0
# sqrt(2)*52 exceeds both macro-cost upper bounds, needed before squaring.
assert sign_qsqrt2(-6, 50) > 0         # 52s-(6+2s)
assert sign_qsqrt2(-18, 45) > 0        # 52s-(18+7s)

axis_vecs = ((8,0),(-8,0),(0,8),(0,-8))
diag_vecs = ((16,16),(16,-16),(-16,16),(-16,-16))

checked_macro = 0
checked_core = 0
nodes_total = 0
phase_summaries = []

for rho in range(8):
    src = (rho, 0)
    dist, pred = dijkstra_exact(src)
    check_predecessors(src, dist, pred)
    nodes_total += len(dist)

    for dx, dy in axis_vecs:
        t = (src[0]+dx, src[1]+dy)
        assert t in dist
        assert alg_leq(dist[t], A), (rho, (dx,dy), dist[t])
        checked_macro += 1
    for dx, dy in diag_vecs:
        t = (src[0]+dx, src[1]+dy)
        assert t in dist
        assert alg_leq(dist[t], D), (rho, (dx,dy), dist[t])
        checked_macro += 1

    local = 0
    for dx in range(-(RADIUS-1), RADIUS):
        for dy in range(-(RADIUS-1), RADIUS):
            if dx == 0 and dy == 0:
                continue
            if dx*dx + dy*dy >= RADIUS*RADIUS:
                continue
            t = (src[0]+dx, src[1]+dy)
            assert t in dist, ("missing", rho, (dx,dy))
            aa, bb = dist[t]
            assert route_leq_source(aa,bb,dx,dy), ("stretch",rho,(dx,dy),(aa,bb))
            checked_core += 1
            local += 1
    phase_summaries.append((rho, len(dist), local))

assert checked_macro == 8*8
assert checked_core == 8*8484

print("I0075_PERIOD8_SIMPLIFIED_EXACT_CERTIFICATE")
print("network: a+3b == 0 mod 8 square-star replacements")
print("axis_macros: +-8 axes <= 6+2*sqrt(2) : PASS")
print("diagonal_macros: (+-16,+-16) <= 18+7*sqrt(2) : PASS")
print("normalized_macro_octagon_inradius > 3/4 : PASS")
print("macro_descent_for_all_norm_ge_52 : PASS")
print("source_phases=8")
print("finite_nonzero_displacements_per_phase=8484")
print("finite_cases_checked=%d" % checked_core)
print("macro_cases_checked=%d" % checked_macro)
print("discovered_nodes_total=%d" % nodes_total)
for row in phase_summaries:
    print("phase_summary=%r" % (row,))
print("finite_stretch_failures=0")
print("ALL_ASSERTIONS_PASSED")
