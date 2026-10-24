"""Exact rational certificate for PROB20-13 run 2026-09-15T16-59-30Z.

Checks on the 7-vertex diameter-two graph H (graph6 FJa^W):
  * all listed paths are valid;
  * each unordered stationary-product demand 2*pi_u*pi_v is met exactly;
  * every physical edge load is exactly 5/32, hence congestion 15/4;
  * the cut S={1,2,3} gives a normalized dual cut metric of value 15/4;
  * hard-coded exact electrical potentials solve L v^(a)=delta_a-pi;
  * canonical electrical congestion is exactly 81/20 on edge (3,5).

Only Python's fractions module is required.
"""
from fractions import Fraction as Q

VTX = range(7)
EDGES = {
    tuple(sorted(e))
    for e in [
        (0,4),(0,5),(0,6),(1,2),(1,3),(1,6),
        (2,3),(2,6),(3,5),(4,5),(4,6),(5,6),
    ]
}
M = len(EDGES)
assert M == 12

DEG = {v: 0 for v in VTX}
for u,v in EDGES:
    DEG[u] += 1
    DEG[v] += 1
assert [DEG[v] for v in VTX] == [3,3,3,3,3,4,5]
PI = {v: Q(DEG[v], 2*M) for v in VTX}
CAP = Q(1, 2*M)

# Exact sparse primal path certificate. Each record is
# (amount, unordered commodity (u,v), path starting at u and ending at v).
ROUTES = [
    (Q(1,32),(0,1),(0,5,3,1)),
    (Q(1,32),(0,2),(0,5,3,2)),
    (Q(1,36),(0,3),(0,5,3)),
    (Q(1,288),(0,3),(0,6,2,3)),
    (Q(1,32),(0,4),(0,6,4)),
    (Q(1,288),(0,5),(0,4,5)),
    (Q(11,288),(0,5),(0,4,6,5)),
    (Q(1,144),(0,6),(0,4,5,6)),
    (Q(13,288),(0,6),(0,5,6)),
    (Q(1,288),(1,2),(1,2)),
    (Q(1,36),(1,2),(1,3,2)),
    (Q(1,36),(1,3),(1,2,3)),
    (Q(1,288),(1,3),(1,3)),
    (Q(1,32),(1,4),(1,6,4)),
    (Q(1,24),(1,5),(1,6,5)),
    (Q(5,96),(1,6),(1,2,6)),
    (Q(7,288),(2,3),(2,1,3)),
    (Q(1,144),(2,3),(2,3)),
    (Q(1,32),(2,4),(2,1,6,0,4)),
    (Q(5,144),(2,5),(2,3,5)),
    (Q(1,144),(2,5),(2,6,0,4,5)),
    (Q(5,96),(2,6),(2,6)),
    (Q(1,32),(3,4),(3,5,4)),
    (Q(5,288),(3,5),(3,1,6,0,5)),
    (Q(7,288),(3,5),(3,2,6,5)),
    (Q(5,288),(3,6),(3,1,2,6)),
    (Q(5,144),(3,6),(3,1,6)),
    (Q(1,288),(4,5),(4,0,5)),
    (Q(11,288),(4,5),(4,5)),
    (Q(5,96),(4,6),(4,0,6)),
    (Q(1,72),(5,6),(5,4,0,6)),
    (Q(1,18),(5,6),(5,4,6)),
]

PAIR_SUM = {(u,v): Q(0) for u in VTX for v in VTX if u < v}
LOAD = {e: Q(0) for e in EDGES}
for amount, pair, path in ROUTES:
    assert amount >= 0
    assert path[0] == pair[0] and path[-1] == pair[1]
    PAIR_SUM[pair] += amount
    for a,b in zip(path, path[1:]):
        e = tuple(sorted((a,b)))
        assert e in EDGES, (pair, path, e)
        LOAD[e] += amount

for (u,v), amount in PAIR_SUM.items():
    required = 2 * PI[u] * PI[v]
    assert amount == required, ((u,v), amount, required)

assert set(LOAD.values()) == {Q(5,32)}, LOAD
PRIMAL_CONGESTION = Q(5,32) / CAP
assert PRIMAL_CONGESTION == Q(15,4)

# Exact dual cut certificate: length 8 across S|T and 0 inside sides.
S = {1,2,3}
CUT_EDGES = [e for e in EDGES if ((e[0] in S) != (e[1] in S))]
assert set(CUT_EDGES) == {(1,6),(2,6),(3,5)}
DUAL_NORM = sum(CAP * 8 for _ in CUT_EDGES)
assert DUAL_NORM == 1
DUAL_OBJECTIVE = sum(
    PI[u] * PI[v] * (0 if ((u in S) == (v in S)) else 8)
    for u in VTX for v in VTX
)
assert DUAL_OBJECTIVE == Q(15,4)
assert DUAL_OBJECTIVE == PRIMAL_CONGESTION

# Exact canonical electrical potentials. Row a is v^(a), gauge v_6=0.
POT = {
0:[Q(79,240),Q(-7,60),Q(-7,60),Q(-13,120),Q(19,240),Q(1,30),Q(0)],
1:[Q(-23,240),Q(43,120),Q(13,120),Q(11,120),Q(-23,240),Q(-1,15),Q(0)],
2:[Q(-23,240),Q(13,120),Q(43,120),Q(11,120),Q(-23,240),Q(-1,15),Q(0)],
3:[Q(-11,240),Q(2,15),Q(2,15),Q(47,120),Q(-11,240),Q(1,30),Q(0)],
4:[Q(19,240),Q(-7,60),Q(-7,60),Q(-13,120),Q(79,240),Q(1,30),Q(0)],
5:[Q(13,240),Q(-1,15),Q(-1,15),Q(-1,120),Q(13,240),Q(7,30),Q(0)],
6:[Q(-7,48),Q(-1,6),Q(-1,6),Q(-5,24),Q(-7,48),Q(-1,6),Q(0)],
}

# Check L v^(a) = delta_a - pi exactly.
for source in VTX:
    v = POT[source]
    for x in VTX:
        nbrs = [y for y in VTX if tuple(sorted((x,y))) in EDGES]
        Lv = DEG[x] * v[x] - sum(v[y] for y in nbrs)
        rhs = (Q(1) if x == source else Q(0)) - PI[x]
        assert Lv == rhs, (source, x, Lv, rhs)

ELECTRICAL = {}
for e in EDGES:
    i,j = e
    weighted_abs = sum(
        PI[a] * abs(POT[a][i] - POT[a][j])
        for a in VTX
    )
    ELECTRICAL[e] = weighted_abs / CAP

assert ELECTRICAL[(3,5)] == Q(81,20)
assert max(ELECTRICAL.values()) == Q(81,20)
assert Q(81,20) > 4 > Q(15,4)

print("Exact stationary-product optimum:", PRIMAL_CONGESTION)
print("Dual cut objective:", DUAL_OBJECTIVE)
print("All physical primal loads:", sorted(set(LOAD.values())))
print("Canonical electrical maximum:", max(ELECTRICAL.values()))
print("Electrical worst edge(s):", sorted(e for e,v in ELECTRICAL.items() if v == max(ELECTRICAL.values())))
print("ALL EXACT CHECKS PASSED")
