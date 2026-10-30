#!/usr/bin/env python3
import itertools, json
from collections import deque

N = 19
ARCS = set([(0, 2), (0, 3), (0, 4), (0, 6), (0, 7), (0, 9), (0, 10), (0, 11), (0, 12), (0, 17), (1, 0), (1, 2), (1, 3), (1, 4), (1, 7), (1, 8), (1, 9), (1, 11), (1, 12), (1, 14), (1, 18), (2, 3), (2, 4), (2, 5), (2, 6), (2, 8), (2, 11), (2, 12), (2, 13), (3, 6), (3, 7), (3, 8), (3, 10), (3, 11), (3, 12), (3, 13), (3, 14), (3, 15), (3, 16), (3, 18), (4, 0), (4, 3), (4, 5), (4, 8), (4, 10), (4, 11), (4, 12), (4, 14), (4, 15), (4, 18), (5, 0), (5, 1), (5, 3), (5, 4), (5, 7), (5, 8), (5, 11), (5, 14), (5, 16), (5, 17), (6, 1), (6, 2), (6, 4), (6, 5), (6, 9), (6, 10), (6, 11), (6, 13), (6, 16), (7, 2), (7, 4), (7, 6), (7, 8), (7, 10), (7, 11), (7, 15), (7, 17), (7, 18), (8, 0), (8, 5), (8, 6), (8, 9), (8, 11), (8, 12), (8, 13), (9, 1), (9, 2), (9, 3), (9, 4), (9, 5), (9, 7), (9, 11), (9, 13), (9, 15), (10, 1), (10, 2), (10, 5), (10, 6), (10, 8), (10, 9), (10, 12), (10, 15), (10, 16), (11, 2), (11, 6), (11, 7), (11, 9), (11, 10), (11, 13), (11, 15), (11, 17), (11, 18), (12, 5), (12, 6), (12, 7), (12, 9), (12, 10), (12, 11), (12, 13), (12, 14), (12, 15), (12, 16), (12, 18), (13, 0), (13, 1), (13, 2), (13, 4), (13, 5), (13, 7), (13, 10), (13, 12), (13, 17), (14, 0), (14, 2), (14, 3), (14, 5), (14, 6), (14, 7), (14, 8), (14, 9), (14, 10), (14, 13), (14, 16), (15, 0), (15, 1), (15, 2), (15, 5), (15, 6), (15, 8), (15, 9), (15, 11), (15, 13), (16, 0), (16, 1), (16, 2), (16, 4), (16, 7), (16, 8), (16, 9), (16, 10), (16, 11), (16, 13), (16, 14), (16, 15), (16, 17), (17, 0), (17, 2), (17, 3), (17, 4), (17, 6), (17, 8), (17, 10), (17, 12), (17, 13), (17, 14), (17, 15), (17, 16), (17, 18), (18, 0), (18, 1), (18, 2), (18, 5), (18, 6), (18, 8), (18, 9), (18, 10), (18, 13), (18, 14), (18, 15), (18, 16)])
MISSING_PAIR = (1, 17)
RETURN_PATH = [17, 2, 5, 1]
AUGMENTED_CYCLE = [1, 17, 2, 5]
CERTIFICATE_TRIANGLES = [(0, 3, 6), (4, 8, 7), (9, 11, 10)]
FOUR_PACK_IN_BASE = [(0, 3, 1), (2, 5, 4), (6, 9, 7), (8, 11, 10)]

def outdegrees(arcs):
    return [sum((u,v) in arcs for v in range(N) if v != u) for u in range(N)]

def is_directed_cycle(cyc, arcs):
    return len(set(cyc)) == len(cyc) and all((cyc[i], cyc[(i+1)%len(cyc)]) in arcs for i in range(len(cyc)))

def strongly_connected_after(arcs, removed):
    verts = [v for v in range(N) if v not in removed]
    if not verts:
        return True
    s = verts[0]
    def reach(reverse=False):
        seen = {s}
        stack = [s]
        while stack:
            u = stack.pop()
            for v in verts:
                if v in seen or v == u:
                    continue
                edge = (v,u) if reverse else (u,v)
                if edge in arcs:
                    seen.add(v)
                    stack.append(v)
        return seen
    return len(reach(False)) == len(verts) and len(reach(True)) == len(verts)

def shortest_distance(arcs, s, t):
    q = deque([(s,0)])
    seen = {s}
    while q:
        u,d = q.popleft()
        if u == t:
            return d
        for v in range(N):
            if v not in seen and (u,v) in arcs:
                seen.add(v)
                q.append((v,d+1))
    return None

assert all(u != v for u,v in ARCS)
for u,v in ARCS:
    assert (v,u) not in ARCS
for i in range(N):
    for j in range(i+1,N):
        if {i,j} == set(MISSING_PAIR):
            assert (i,j) not in ARCS and (j,i) not in ARCS
        else:
            assert ((i,j) in ARCS) ^ ((j,i) in ARCS)

deg = outdegrees(ARCS)
assert deg == [10,11,9,11,10,10,9,12,7,8,7,9,7,9,11,7,7,7,9]
assert min(deg) == 7 and max(deg) == 12

for r in range(3):
    for removed_tuple in itertools.combinations(range(N), r):
        assert strongly_connected_after(ARCS, set(removed_tuple))

for x,y in ARCS:
    assert any(z != x and z != y and (z,x) in ARCS and (z,y) in ARCS for z in range(N))

assert all((RETURN_PATH[i], RETURN_PATH[i+1]) in ARCS for i in range(len(RETURN_PATH)-1))
assert shortest_distance(ARCS, 17, 1) == 3
assert not any((17,w) in ARCS and (w,1) in ARCS for w in range(N))

AUG = set(ARCS)
AUG.add((1,17))
assert is_directed_cycle(AUGMENTED_CYCLE, AUG)
for T in CERTIFICATE_TRIANGLES:
    assert is_directed_cycle(T, ARCS)
all_cert = [AUGMENTED_CYCLE] + CERTIFICATE_TRIANGLES
assert len(set().union(*map(set, all_cert))) == sum(map(len, all_cert))

for T in FOUR_PACK_IN_BASE:
    assert is_directed_cycle(T, ARCS)
assert len(set().union(*map(set, FOUR_PACK_IN_BASE))) == 12

localization = {}
for m in range(3, 31):
    allowed = [k for k in range(1,m) if 2 + (m-k) >= m]
    assert allowed == [1,2]
    localization[m] = allowed

DN = 12
DARCS = {(i,j) for i in range(DN) for j in range(DN) if i != j}
for j in [8,9,10,11]:
    DARCS.remove((0,j))
pre = [sum((i,j) in DARCS for j in range(DN) if j != i) for i in range(DN)]
assert pre == [7] + [11]*11
assert (1,2) in DARCS and (2,1) in DARCS
survivors = [i for i in range(DN) if i not in {1,2}]
post = [sum((i,j) in DARCS for j in survivors if j != i) for i in survivors]
assert post == [5] + [9]*9

out = {
    "status": "PASS",
    "adversary_vertices": N,
    "adversary_arcs": len(ARCS),
    "adversary_outdegrees": deg,
    "missing_unordered_pair": list(MISSING_PAIR),
    "shortest_return_17_to_1_edges": shortest_distance(ARCS, 17, 1),
    "displayed_return_path": RETURN_PATH,
    "augmented_cycle_using_1_to_17": AUGMENTED_CYCLE,
    "three_disjoint_certificate_cycles": CERTIFICATE_TRIANGLES,
    "base_four_pack": FOUR_PACK_IN_BASE,
    "three_vertex_strong": True,
    "every_arc_dominated": True,
    "digon_pre_outdegrees": pre,
    "digon_post_outdegrees_after_delete_1_2": post,
    "localization_checked_cycle_lengths": [3,30]
}
print(json.dumps(out, sort_keys=True, separators=(",",":")))
