#!/usr/bin/env python3
import json
from itertools import combinations, permutations

ADJ = {'h0': ['h1', 'r0', 'r1', 's0', 'u0', 'u1', 'u2'],
 'h1': ['h2', 'r1', 's2', 'u0', 'u1', 'u3', 'u4'],
 'h2': ['h0', 'r2', 's1', 's3', 'u2', 'u3', 'u4'],
 'r0': ['h1', 'h2', 'r1', 'r2', 's0', 's3', 'x'],
 'r1': ['h2', 'r2', 'u0', 'u1', 'u2', 'u4', 'x'],
 'r2': ['h0', 's0', 's1', 's2', 's3', 'u3', 'x'],
 's0': ['h1', 'h2', 'r1', 's1', 'u2', 'u3', 'x'],
 's1': ['h0', 'h1', 'r0', 'r1', 's2', 'u1', 'x'],
 's2': ['h0', 'h2', 'r0', 'r1', 's3', 'u0', 'x'],
 's3': ['h0', 'h1', 'r1', 's0', 'u1', 'u2', 'u4'],
 'u0': ['h2', 'r0', 'r2', 's0', 's1', 's3', 'u1'],
 'u1': ['h2', 'r0', 'r2', 's0', 's2', 'u2', 'x'],
 'u2': ['h1', 'r0', 'r2', 's1', 's2', 'u3', 'x'],
 'u3': ['h0', 'r0', 'r1', 's1', 's2', 's3', 'u4'],
 'u4': ['h0', 'r0', 'r2', 's0', 's1', 's2', 'u0'],
 'x': ['h0', 'h1', 'h2', 's3', 'u0', 'u3', 'u4']}
V = tuple(ADJ)
H = ("h0","h1","h2")
S = ("s0","s1","s2","s3")
U = ("u0","u1","u2","u3","u4")
R = ("r0","r1","r2","x")
T2 = ("h2","r2","x")
R2 = ("h0","r0","h1","r1")

def arc(u,v):
    return v in ADJ[u]

def dag(S0):
    S0=set(S0)
    indeg={v:0 for v in S0}
    for u in S0:
        for v in ADJ[u]:
            if v in S0: indeg[v]+=1
    stack=[v for v in S0 if indeg[v]==0]
    seen=0
    while stack:
        u=stack.pop(); seen+=1
        for v in ADJ[u]:
            if v in S0:
                indeg[v]-=1
                if indeg[v]==0: stack.append(v)
    return seen==len(S0)

def strong(dead=()):
    dead=set(dead)
    live=[v for v in V if v not in dead]
    if not live: return True
    root=live[0]
    def reach(rev=False):
        seen={root}; stack=[root]
        while stack:
            u=stack.pop()
            ns=([w for w in live if arc(w,u)] if rev else [w for w in ADJ[u] if w in live])
            for w in ns:
                if w not in seen:
                    seen.add(w); stack.append(w)
        return len(seen)==len(live)
    return reach(False) and reach(True)

def directed_cycle(c):
    return all(arc(c[i],c[(i+1)%len(c)]) for i in range(len(c)))

def induced_cycle(c):
    if not directed_cycle(c): return False
    n=len(c)
    for i in range(n):
        for j in range(i+1,n):
            if (j-i)%n in (1,n-1): continue
            if arc(c[i],c[j]) or arc(c[j],c[i]): return False
    return True

# High-level exact local adversary.
assert len(V)==16
assert all(len(ADJ[u])==7 and len(set(ADJ[u]))==7 and u not in ADJ[u] for u in V)
nonedges=[]
for i,u in enumerate(V):
    for v in V[i+1:]:
        assert not (arc(u,v) and arc(v,u))
        if not arc(u,v) and not arc(v,u): nonedges.append((u,v))
assert len(nonedges)==8
for k in (0,1,2):
    for dead in combinations(V,k):
        assert strong(dead)
for u in V:
    for v in ADJ[u]:
        assert any(w not in (u,v) and arc(w,u) and arc(w,v) for w in V)

assert induced_cycle(H)
assert induced_cycle(S)
assert induced_cycle(U)
assert set(H).isdisjoint(S) and set(H).isdisjoint(U) and set(S).isdisjoint(U)
assert set(V)-set(H)-set(S)-set(U)==set(R)

# Lead's exact-two-predecessor aligned cage, in the potential-equality branch.
for i in range(3):
    assert arc(H[i],f"r{i}") and arc(f"r{i}","x") and arc("x",H[i])
assert arc("r0","r1") and arc("r1","r2") and arc("r0","r2")
assert arc("r0","h1") and arc("r1","h2") and arc("r2","h0")
assert arc("h0","r1")
G=set(H)|set(R)
assert {v for v in ADJ["h1"] if v in G}=={"h2","r1"}
assert {v for v in ADJ["h2"] if v in G}=={"h0","r2"}
assert {v for v in ADJ["r2"] if v in G}=={"h0","x"}
assert {v for v in ADJ["h0"] if v in G}=={"h1","r0","r1"}

# Both old and neutral-pivot remainders are complete transitive tournaments.
def induced_arc_count(S0):
    S0=set(S0)
    return sum(1 for u in S0 for v in ADJ[u] if v in S0)

assert dag(R) and induced_arc_count(R)==6
assert directed_cycle(T2)
assert dag(R2) and induced_arc_count(R2)==6
assert set(T2).isdisjoint(S) and set(T2).isdisjoint(U)
assert set(V)-set(T2)-set(S)-set(U)==set(R2)

# The terminal remainder witness is exact-five into the light supports and has no heavy-target inport.
r2_light=[v for v in ADJ["r2"] if v in set(S)|set(U)]
assert len(r2_light)==5
r2_S=[v for v in r2_light if v in S]
r2_U=[v for v in r2_light if v in U]
assert len(r2_S)>=3
assert all(not arc(s,"r2") for s in S)

# The graph is only a LOCAL adversary, never a BT4 counterexample.
four=(("h0","h1","h2"),("r0","r1","u0"),("r2","s0","u2"),("s1","x","u3"))
assert all(directed_cycle(c) for c in four)
assert len(set().union(*(set(c) for c in four)))==12

# Symbolic potential case split from the theorem.
cases=[]
for eps in (0,1):  # eps=1 means r0->r2, so old Phi=6 rather than 5.
    old_phi=5+eps
    for pair in ("nonedge","h0_to_r1","r1_to_h0"):
        new_phi=5+(pair!="nonedge")
        cyclic=(pair=="r1_to_h0")
        arcmax_ok=(new_phi<=old_phi)
        survives=arcmax_ok and not cyclic
        if survives:
            assert (eps,pair) in ((0,"nonedge"),(1,"nonedge"),(1,"h0_to_r1"))
        cases.append({"r0_to_r2":bool(eps),"h0_r1_state":pair,
                      "old_phi":old_phi,"new_phi":new_phi,
                      "exchanged_remainder_cyclic":cyclic,
                      "arcmax_ok":arcmax_ok,"survives_local_filters":survives})

# Highly asymmetric digon boundary: only one vertex is at degree 7, others at 9.
DV=("a","b")+tuple(f"d{i}" for i in range(8))
w="d0"
def darc(u,v):
    if u==v: return False
    if u==w and v in ("d6","d7"): return False
    return True
before={u:sum(darc(u,v) for v in DV) for u in DV}
assert sorted(before.values())==[7]+[9]*9
assert darc("a","b") and darc("b","a")
surv=[v for v in DV if v not in ("a","b")]
after={u:sum(darc(u,v) for v in surv) for u in surv}
assert min(after.values())==5 and after[w]==5

obj={
  "status":"PASS",
  "candidate_refuted":"potential equality alone forbids an aligned heavy-triangle neutral slide",
  "local_adversary":{
    "vertices":len(V),
    "arcs":sum(len(ADJ[u]) for u in V),
    "outdegree_vector":sorted(len(ADJ[u]) for u in V),
    "oriented":True,
    "nonedges":nonedges,
    "strong_after_any_at_most_two_vertex_deletions":True,
    "every_arc_dominated":True,
    "chosen_chordless_cycles":[list(H),list(S),list(U)],
    "old_remainder":list(R),
    "old_remainder_arc_count":induced_arc_count(R),
    "pivot_triangle":list(T2),
    "new_remainder":list(R2),
    "new_remainder_arc_count":induced_arc_count(R2),
    "r2_light_fans":{"S":r2_S,"U":r2_U},
    "no_S_inport_to_r2":True,
    "explicit_four_pack":[list(c) for c in four]
  },
  "symbolic_arcmax_cases":cases,
  "digon_asymmetric_boundary":{
    "vertices":len(DV),
    "outdegree_before":before,
    "chosen_digon":["a","b"],
    "outdegree_after_deleting_digon":after,
    "minimum_before":min(before.values()),
    "minimum_after":min(after.values())
  }
}
print(json.dumps(obj,sort_keys=True,indent=2))
