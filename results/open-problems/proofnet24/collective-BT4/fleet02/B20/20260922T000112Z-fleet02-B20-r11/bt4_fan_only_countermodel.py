#!/usr/bin/env python3
import json
from collections import deque

C1=[f"a{i}" for i in range(5)]
C2=[f"b{i}" for i in range(5)]
C3=[f"c{i}" for i in range(5)]
cycles={"C1":C1,"C2":C2,"C3":C3}
R=["x1","x2","x3"]
V=C1+C2+C3+R
arcs=set()

# Three designated chordless directed 5-cycles.
for cyc in cycles.values():
    for i,u in enumerate(cyc):
        arcs.add((u,cyc[(i+1)%5]))

# Complete oriented cross-cycle pairs. For each ordered cycle pair U,V,
# U_i -> V_j iff j-i mod 5 is 0,1,2; otherwise V_j -> U_i.
for U,Vv in [(C1,C2),(C2,C3),(C3,C1)]:
    for i,u in enumerate(U):
        for j,v in enumerate(Vv):
            if (j-i)%5 in {0,1,2}:
                arcs.add((u,v))
            else:
                arcs.add((v,u))

# R is independent. Each x has signature (2,3,2), (2,2,3), (3,2,2).
hits={
    "x1":{"a0","a1","b0","b2","b4","c0","c1"},
    "x2":{"a2","a3","b0","b1","c0","c2","c4"},
    "x3":{"a0","a2","a4","b2","b3","c2","c3"},
}
heavy={"x1":"C2","x2":"C3","x3":"C1"}
for x in R:
    for v in hits[x]:
        arcs.add((x,v))
    for cname,cyc in cycles.items():
        if cname == heavy[x]:
            # Heavy-cycle no-return: forbid every C_heavy -> x arc.
            continue
        # For light cycles, orient every non-hit pair back into x.
        for v in cyc:
            if v not in hits[x]:
                arcs.add((v,x))

def outdeg(u):
    return sum(a==u for a,b in arcs)

def reachable(s):
    q=deque([s]); seen={s}
    while q:
        u=q.popleft()
        for a,b in arcs:
            if a==u and b not in seen:
                seen.add(b); q.append(b)
    return seen

assert not any((v,u) in arcs for u,v in arcs), "digon present"
assert min(outdeg(v) for v in V) >= 7
assert all(len(reachable(v)) == len(V) for v in V)
assert all((u,v) not in arcs for u in R for v in R if u != v)

for cname,cyc in cycles.items():
    expected={(cyc[i],cyc[(i+1)%5]) for i in range(5)}
    internal={(u,v) for u,v in arcs if u in cyc and v in cyc}
    assert internal == expected, (cname, internal ^ expected)

signature={
    x:[sum((x,v) in arcs for v in C) for C in (C1,C2,C3)]
    for x in R
}
assert signature == {"x1":[2,3,2],"x2":[2,2,3],"x3":[3,2,2]}
for x,cname in heavy.items():
    assert all((v,x) not in arcs for v in cycles[cname])

# x1 witnesses q1<=2 and five-fan into C2 U C3; similarly cyclically.
for x,low in [("x1",0),("x2",1),("x3",2)]:
    s=signature[x]
    assert s[low] <= 2
    assert sum(s)-s[low] >= 5

# Explicit four disjoint directed cycles. This deliberately proves that
# the construction is NOT a BT4 counterexample.
cert=[
    ["a0","b0","c0"],
    ["a1","a2","c4"],
    ["a4","b1","a3"],
    ["b2","c2","x1"],
]
used=set()
for cyc in cert:
    assert not (used & set(cyc))
    used.update(cyc)
    for i,u in enumerate(cyc):
        assert (u,cyc[(i+1)%len(cyc)]) in arcs

print(json.dumps({
    "vertices":len(V),
    "arcs":len(arcs),
    "minimum_outdegree":min(outdeg(v) for v in V),
    "strongly_connected":True,
    "R_is_independent_DAG":True,
    "sink_signatures":signature,
    "heavy_cycle_no_return":True,
    "pair_deletion_five_fan_counts":True,
    "four_disjoint_directed_cycles":cert,
    "scope":"Refutes only the local/count-only implication to the short-return obligation; it is intentionally not a BT4 counterexample."
},indent=2))
