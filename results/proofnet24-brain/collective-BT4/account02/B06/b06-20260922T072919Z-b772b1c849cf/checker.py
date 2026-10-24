#!/usr/bin/env python3
"""Exact checker for BT4-RANK2-PORT-PARITY-v1 and a sharp digon deletion adversary."""

from itertools import permutations, combinations
import json

def fwd(order, start, end):
    i = order.index(start)
    out = []
    while True:
        out.append(order[i])
        if order[i] == end:
            return out
        i = (i + 1) % len(order)

def disjoint(p, q):
    return set(p).isdisjoint(q)

def canon_rotation(seq):
    seq = list(seq)
    return min(tuple(seq[i:] + seq[:i]) for i in range(len(seq)))

def support_state(order, starts, ends):
    s1, s2 = starts
    e1, e2 = ends
    id_ok = disjoint(fwd(order, s1, e1), fwd(order, s2, e2))
    sw_ok = disjoint(fwd(order, s2, e1), fwd(order, s1, e2))
    assert not (id_ok and sw_ok)
    return "ID" if id_ok else ("SW" if sw_ok else "BLOCK")

# Exact cyclic-order classification for four distinct ports on a directed cycle.
A_labels = ["d1", "d2", "a1", "a2"]
B_labels = ["b1", "b2", "c1", "c2"]
A_orders = sorted({canon_rotation(p) for p in permutations(A_labels)})
B_orders = sorted({canon_rotation(p) for p in permutations(B_labels)})
A_states = {
    "".join(o): support_state(list(o), ("d1", "d2"), ("a1", "a2"))
    for o in A_orders
}
B_states = {
    "".join(o): support_state(list(o), ("b1", "b2"), ("c1", "c2"))
    for o in B_orders
}
assert list(A_states.values()).count("ID") == 1
assert list(A_states.values()).count("SW") == 1
assert list(A_states.values()).count("BLOCK") == 4
assert list(B_states.values()).count("ID") == 1
assert list(B_states.values()).count("SW") == 1
assert list(B_states.values()).count("BLOCK") == 4

criterion_checked = 0
criterion_true = 0
for ao in A_orders:
    ast = support_state(list(ao), ("d1", "d2"), ("a1", "a2"))
    for bo in B_orders:
        bst = support_state(list(bo), ("b1", "b2"), ("c1", "c2"))
        id_ok = (
            disjoint(fwd(list(ao), "d1", "a1"), fwd(list(ao), "d2", "a2"))
            and disjoint(fwd(list(bo), "b1", "c1"), fwd(list(bo), "b2", "c2"))
        )
        sw_ok = (
            disjoint(fwd(list(ao), "d2", "a1"), fwd(list(ao), "d1", "a2"))
            and disjoint(fwd(list(bo), "b1", "c2"), fwd(list(bo), "b2", "c1"))
        )
        brute = id_ok or sw_ok
        formula = ast in ("ID", "SW") and ast == bst
        assert brute == formula
        criterion_checked += 1
        criterion_true += int(brute)

# A 19-vertex oriented, arc-dominated, 3-vertex-strong, delta+=7 adversary
# carrying the parity-mismatched prescribed rank-two connector interface.
# A=(d1,a1,d2,a2)=(0,1,2,3), B=(b1,c2,b2,c1)=(4,5,6,7).
adj = {
  0: [1,9,11,12,13,15,16,18],
  1: [2,4,9,13,14,15,16],
  2: [3,7,10,11,12,15,16],
  3: [0,6,9,11,12,13,14,18],
  4: [0,2,3,5,8,9,12,13,17,18],
  5: [0,1,2,3,6,8,13,14,16,18],
  6: [0,1,2,7,10,11,12,15,18],
  7: [0,1,3,4,10,11,12,14,16],
  8: [0,1,2,3,6,7,9,11,13,18],
  9: [2,5,6,7,10,12,13,15,18],
  10: [0,1,3,4,5,8,13,14],
  11: [1,4,5,9,10,13,15,17,18],
  12: [1,5,8,10,11,13,17],
  13: [2,6,7,14,15,17,18],
  14: [0,2,4,6,8,9,11,12,15],
  15: [3,4,5,7,8,10,12,17,18],
  16: [3,4,6,8,9,10,11,12,13,14,15],
  17: [0,1,2,3,5,6,7,8,9,10,14,16],
  18: [1,2,7,10,12,14,16,17],
}
V = list(range(19))
E = {(u,v) for u, outs in adj.items() for v in outs}
assert all(u != v for u,v in E)
for u,v in combinations(V,2):
    # Oriented: at most one direction. Four designated support diagonals are absent.
    assert not ((u,v) in E and (v,u) in E)
A_num = [0,1,2,3]
B_num = [4,5,6,7]
for C in (A_num, B_num):
    assert all((C[i], C[(i+1)%4]) in E for i in range(4))
    # Chordless designated support.
    induced = {(u,v) for u,v in E if u in C and v in C}
    assert induced == {(C[i], C[(i+1)%4]) for i in range(4)}
# Prescribed connectors P1,P2,Q1,Q2 are all direct and endpoint-distinct.
assert all(e in E for e in [(1,4),(3,6),(7,0),(5,2)])

degrees = [len(adj[u]) for u in V]
assert min(degrees) == 7
assert max(degrees) == 12

def reachable(start, allowed, reverse=False):
    seen = {start}
    stack = [start]
    while stack:
        u = stack.pop()
        for v in allowed:
            if v in seen:
                continue
            edge = (v,u) if reverse else (u,v)
            if edge in E:
                seen.add(v)
                stack.append(v)
    return seen

# 3-vertex-strong: deletion of any <=2 vertices leaves strong connectivity.
for k in range(3):
    for deleted in combinations(V,k):
        allowed = set(V) - set(deleted)
        s = min(allowed)
        assert reachable(s, allowed) == allowed
        assert reachable(s, allowed, reverse=True) == allowed

# Every arc is dominated by a common predecessor.
for u,v in E:
    assert any(z not in (u,v) and (z,u) in E and (z,v) in E for z in V)

four_pack = [(0,1,4),(2,3,6),(5,8,9),(7,10,13)]
for tri in four_pack:
    assert all((tri[i],tri[(i+1)%3]) in E for i in range(3))
assert len(set().union(*(set(t) for t in four_pack))) == 12

# Port mismatch on the prescribed connector families.
A_order = ["d1","a1","d2","a2"]  # ID-preferred
B_order = ["b1","c2","b2","c1"]  # SW-preferred
assert support_state(A_order, ("d1","d2"), ("a1","a2")) == "ID"
assert support_state(B_order, ("b1","b2"), ("c1","c2")) == "SW"
id_A = [fwd(A_order,"d1","a1"), fwd(A_order,"d2","a2")]
id_B = [fwd(B_order,"b1","c1"), fwd(B_order,"b2","c2")]
sw_A = [fwd(A_order,"d2","a1"), fwd(A_order,"d1","a2")]
sw_B = [fwd(B_order,"b1","c2"), fwd(B_order,"b2","c1")]
assert disjoint(*id_A) and not disjoint(*id_B)
assert not disjoint(*sw_A) and disjoint(*sw_B)

# Highly asymmetric digon deletion boundary on 10 vertices.
DV = [f"v{i}" for i in range(10)]
DE = {(u,v) for u in DV for v in DV if u != v}
DE.remove(("v0","v6"))
DE.remove(("v0","v7"))
DE.remove(("v1","v7"))
def dout(v, W):
    W = set(W)
    return sum((v,w) in DE for w in W if w != v)
before = [dout(v,DV) for v in DV]
assert before == [7,8,9,9,9,9,9,9,9,9]
assert ("v8","v9") in DE and ("v9","v8") in DE
survivors = [v for v in DV if v not in {"v8","v9"}]
after = [dout(v,survivors) for v in survivors]
assert min(after) == 5 and after[0] == 5

payload = {
  "status": "PASS",
  "rank2_port_parity": {
    "cyclic_orders_per_support": 6,
    "state_counts_per_support": {"ID":1,"SW":1,"BLOCK":4},
    "order_pairs_checked": criterion_checked,
    "order_pairs_with_canonical_two_splice": criterion_true,
    "prescribed_A_order": A_order,
    "prescribed_B_order": B_order,
    "identity_A_disjoint": disjoint(*id_A),
    "identity_B_disjoint": disjoint(*id_B),
    "swap_A_disjoint": disjoint(*sw_A),
    "swap_B_disjoint": disjoint(*sw_B),
  },
  "oriented_adversary": {
    "vertices": len(V),
    "arcs": len(E),
    "minimum_outdegree": min(degrees),
    "maximum_outdegree": max(degrees),
    "outdegrees": degrees,
    "chordless_supports": [A_num,B_num],
    "direct_connectors": [[1,4],[3,6],[7,0],[5,2]],
    "three_vertex_strong": True,
    "every_arc_dominated": True,
    "explicit_four_pack": [list(t) for t in four_pack],
  },
  "digon_boundary": {
    "vertices": len(DV),
    "chosen_digon": ["v8","v9"],
    "outdegrees_before": before,
    "surviving_outdegrees_after_delete": after,
    "minimum_before": min(before),
    "minimum_after": min(after),
  }
}
print(json.dumps(payload, sort_keys=True, indent=2))
