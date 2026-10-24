#!/usr/bin/env python3
import json
from itertools import combinations, permutations

ADJ={
"A0":["A1","B2","R1","R2","R4","R6","Z0"],
"A1":["A2","B1","B2","R1","R2","R4","Z1"],
"A2":["A0","B0","R1","R2","R3","R4","Z2"],
"B0":["A1","B1","R0","R1","R3","R5","R6"],
"B1":["A0","A2","B2","R0","R1","R2","R3"],
"B2":["A2","B0","R1","R2","R3","R4","R5"],
"Z0":["A1","A2","B0","B1","B2","R0","Z1"],
"Z1":["A0","A2","B0","B1","B2","R0","Z2"],
"Z2":["A0","A1","B0","B1","B2","R0","Z0"],
"R0":["A0","A1","A2","B2","R2","R5","R6"],
"R1":["R0","R2","R3","R4","R5","Z1","Z2"],
"R2":["B0","R3","R4","R6","Z0","Z1","Z2"],
"R3":["A0","A1","R4","R5","Z0","Z1","Z2"],
"R4":["B0","B1","R5","R6","Z0","Z1","Z2"],
"R5":["A0","A1","A2","B1","R6","Z0","Z1"],
"R6":["A1","A2","B1","B2","Z0","Z1","Z2"]
}
V=tuple(ADJ)
C1=("A0","A1","A2")
C2=("B0","B1","B2")
X=("Z0","Z1","Z2")
R=tuple("R%d"%i for i in range(7))

def arc(u,v):
    return v in ADJ[u]

def cycle_order(vertices):
    S=tuple(vertices)
    for p in permutations(S):
        if all(arc(p[i],p[(i+1)%len(p)]) for i in range(len(p))):
            return p
    return None

def dag(S):
    S=set(S)
    indeg={v:0 for v in S}
    for u in S:
        for v in ADJ[u]:
            if v in S:
                indeg[v]+=1
    q=[v for v in S if indeg[v]==0]
    seen=0
    while q:
        u=q.pop()
        seen+=1
        for v in ADJ[u]:
            if v in S:
                indeg[v]-=1
                if indeg[v]==0:
                    q.append(v)
    return seen==len(S)

def strong(delset=()):
    dead=set(delset)
    live=[v for v in V if v not in dead]
    if not live:
        return True
    root=live[0]
    def reach(rev=False):
        seen={root}
        stack=[root]
        while stack:
            u=stack.pop()
            if rev:
                ns=[w for w in live if arc(w,u)]
            else:
                ns=[w for w in ADJ[u] if w in live]
            for w in ns:
                if w not in seen:
                    seen.add(w)
                    stack.append(w)
        return seen
    return len(reach(False))==len(live)==len(reach(True))

def all_directed_cycles(S):
    S=set(S)
    ans=set()
    for s in sorted(S):
        stack=[(s,[s],{s})]
        while stack:
            u,path,used=stack.pop()
            for v in ADJ[u]:
                if v not in S:
                    continue
                if v==s and len(path)>=2:
                    rots=[tuple(path[i:]+path[:i]) for i in range(len(path))]
                    ans.add(min(rots))
                elif v not in used:
                    stack.append((v,path+[v],used|{v}))
    return sorted(ans,key=lambda c:(len(c),c))

def disjoint_cycle_pair(S):
    cs=all_directed_cycles(S)
    for i,c in enumerate(cs):
        sc=set(c)
        for d in cs[i+1:]:
            if sc.isdisjoint(d):
                return [list(c),list(d)]
    return None

# Revalidate the high-level local normal-form properties of the reused exact graph.
assert all(len(ADJ[u])==7 and len(set(ADJ[u]))==7 and u not in ADJ[u] for u in V)
for u,v in combinations(V,2):
    assert not (arc(u,v) and arc(v,u))
for k in (0,1,2):
    for S in combinations(V,k):
        assert strong(S)
for u in V:
    for v in ADJ[u]:
        assert any(w not in (u,v) and arc(w,u) and arc(w,v) for w in V)

# Fixed-pair residual Gamma = D - (C1 union C2).
Gamma=set(V)-set(C1)-set(C2)
gamma_deg={v:sum(arc(v,w) for w in Gamma if w!=v) for v in Gamma}
W=sorted(v for v,d in gamma_deg.items() if d==2)
assert W==["Z0","Z1","Z2"]

# Three globally minimum triangle packings linked by one-slot neutral pivots.
states=[]
for i,z in enumerate(X):
    znext=X[(i+1)%3]
    Q=("R0","R2",z)
    assert cycle_order(Q)==Q  # R0 -> R2 -> Zi -> R0
    used=set(C1+C2+Q)
    rem=set(V)-used
    assert len(used)==9 and dag(rem)
    # Neutral one-slot pivot Q_i -> Q_{i+1}: R2 -> Znext -> R0 replaces Zi.
    assert znext in rem
    assert arc("R2",znext) and arc(znext,"R0")
    Qnext=("R0","R2",znext)
    assert cycle_order(Qnext)==Qnext

    # The fixed-pair witness set W is invariant and there are two fresh off-pivot witnesses.
    off=sorted(set(W)&rem)
    assert len(off)==2 and znext in off

    cross={}
    for fixed_name,fixed_cycle in (("C1",C1),("C2",C2)):
        live=set(V)-set(fixed_cycle)-set(Q)
        deg={v:sum(arc(v,w) for w in live if w!=v) for v in live}
        low=sorted((v,d) for v,d in deg.items() if d<=2)
        pair=disjoint_cycle_pair(live)
        assert pair is not None  # this local adversary is not a BT4 counterexample
        cross[fixed_name]={
            "minimum_residual_outdegree":min(deg.values()),
            "degree_two_count":sum(d==2 for d in deg.values()),
            "low_vertices":low,
            "two_disjoint_cycle_certificate":pair,
        }

    states.append({
        "state":i,
        "support_triangle":list(Q),
        "remainder":sorted(rem),
        "fresh_off_pivot_W":off,
        "neutral_pivot_to_state":(i+1)%3,
        "pivot_insert":znext,
        "pivot_remove":z,
        "anchor_arc":["R0","R2"],
        "cross_pair_data":cross,
    })

# The orbit closes only after three fresh-witness pivots.
assert states[0]["support_triangle"] != states[1]["support_triangle"] != states[2]["support_triangle"]
assert states[2]["neutral_pivot_to_state"]==0

# An explicit four-pack, proving this is a local obstruction only.
four=(("A0","R1","R5"),("B0","R3","Z2"),("A1","R4","R6"),("R0","R2","Z1"))
assert all(cycle_order(c) is not None for c in four)
assert len(set().union(*(set(c) for c in four)))==12

# New digon boundary: contraction does not preserve the threshold seven.
# K_8 with both ordered arcs on each unordered pair has delta^+=7.
DV=tuple("d%d"%i for i in range(8))
def darc(u,v):
    return u!=v
before={u:sum(darc(u,v) for v in DV) for u in DV}
assert min(before.values())==7
digon=("d0","d1")
assert darc(*digon) and darc(digon[1],digon[0])
# Contract d0,d1 to q and suppress duplicate ordered arcs: the result is bidirected K_7.
CV=("q",)+tuple(v for v in DV if v not in digon)
after={u:len(CV)-1 for u in CV}
assert min(after.values())==6

obj={
  "status":"PASS",
  "candidate_refuted":"fresh same-pair off-pivot witnesses force neutral-orbit termination",
  "graph":{
    "vertices":len(V),
    "arcs":sum(len(ADJ[u]) for u in V),
    "exact_outdegree":7,
    "oriented":True,
    "strong_after_any_at_most_two_vertex_deletions":True,
    "every_arc_dominated":True,
    "fixed_cycles":[list(C1),list(C2)],
    "fixed_pair_residual_W":W,
    "fixed_pair_residual_degrees":dict(sorted(gamma_deg.items())),
    "three_state_neutral_orbit":states,
    "explicit_four_pack":[list(c) for c in four]
  },
  "repair_lemma_checked_scope":{
    "statement":"The local 3-state orbit survives same-pair W-regeneration; in a genuine counterexample the known k=2 pair-deletion theorem must be applied to each cross pair. For a 3-slot state, persistent no-six forces at least one degree-two witness outside the three slot vertices for each cross pair.",
    "why_local_adversary_is_excluded":"Every cross-pair residual in the three states already contains two vertex-disjoint directed cycles; the recorded certificates exhibit them."
  },
  "digon_contraction_boundary":{
    "example":"complete bidirected K8",
    "minimum_outdegree_before":min(before.values()),
    "digon":list(digon),
    "contract_and_suppress_duplicates_minimum_outdegree":min(after.values()),
    "repair":"Use digon deletion plus the proved k=3 threshold-five theorem; do not contract and continue at threshold seven."
  }
}
print(json.dumps(obj,indent=2,sort_keys=True))
