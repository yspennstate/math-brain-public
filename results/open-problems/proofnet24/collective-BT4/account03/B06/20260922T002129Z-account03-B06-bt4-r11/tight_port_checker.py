#!/usr/bin/env python3
"""Exact sanity checker for account03/B06 BT4 tight-port work.

No external dependencies.  It verifies:
(1) the finite cyclic-block sanity sweep for the tight-port lemma, and
(2) an explicit 18-vertex oriented min-outdegree-7 graph showing that the
    local U1 tight geometry alone does not force a contradiction.
"""
import json
from collections import deque

ADJ = {
    0:[1,5,10,11,12,13,16],
    1:[2,6,7,10,11,12,13],
    2:[3,6,8,9,10,12,13],
    3:[0,4,7,8,9,10,11],
    4:[0,2,5,8,10,15,16],
    5:[2,3,6,8,10,11,12],
    6:[4,9,10,11,12,14,17],
    7:[4,6,8,10,11,12,16],
    8:[0,1,6,9,10,12,13],
    9:[0,4,7,10,14,16,17],
    10:[11,12,13,14,15,16,17],
    11:[2,12,13,14,15,16,17],
    12:[3,4,13,14,15,16,17],
    13:[6,7,9,14,15,16,17],
    14:[2,3,5,8,15,16,17],
    15:[0,1,3,5,9,16,17],
    16:[1,2,3,5,6,8,17],
    17:[1,2,3,4,5,7,8],
}
A = {u:set(vs) for u,vs in ADJ.items()}

def is_cycle(c):
    return len(set(c)) == len(c) and all(c[(i+1)%len(c)] in A[c[i]]
                                          for i in range(len(c)))

def acyclic(vertices):
    vertices=set(vertices)
    indeg={v:0 for v in vertices}
    for u in vertices:
        for v in A[u]:
            if v in vertices:
                indeg[v]+=1
    q=deque(v for v,d in indeg.items() if d==0)
    seen=0
    while q:
        u=q.popleft()
        seen+=1
        for v in A[u]:
            if v in vertices:
                indeg[v]-=1
                if indeg[v]==0:
                    q.append(v)
    return seen==len(vertices)

# Symbolic finite sanity sweep: equality in the path-fan count says the fan
# is exactly the m successors of the port.  For m<r this cyclic block has
# exactly one predecessor/port.
case_count=0
max_ports=0
all_consecutive=True
for r in range(4,13):
    for m in range(3,r):
        case_count += 1
        target=set(range(1,m+1))
        ports=[]
        for b in range(r):
            block={(b+t)%r for t in range(1,m+1)}
            if block==target:
                ports.append(b)
        max_ports=max(max_ports,len(ports))
        all_consecutive &= (ports == [0])

# Full-graph certificate for sharpness of the local geometry.
n=18
outdegrees={u:len(A[u]) for u in range(n)}
no_loops=all(u not in A[u] for u in range(n))
no_digons=all(not (v in A[u] and u in A[v])
              for u in range(n) for v in range(u+1,n))
C1=[0,1,2,3]
C2=[4,5,6]
C3=[7,8,9]
R=set(range(10,18))
sinks=sorted(u for u in R if not (A[u] & R))
tight_path=[0,16,17]
fan=sorted(A[17] & set(C1))
Cstar=[0,16,17,3]
Rprime=(R-{16,17})|{1,2}
remainder_cycle=[1,10,15]
four_pack=[Cstar,C2,C3,remainder_cycle]
four_pack_disjoint=len(set(sum(four_pack,[])))==sum(map(len,four_pack))

result={
  "symbolic_tight_port_sweep":{
    "r_range":[4,12],
    "m_range":"3..r-1",
    "cases":case_count,
    "all_consecutive_block_identity":all_consecutive,
    "max_ports_per_fan":max_ports,
  },
  "explicit_full_graph":{
    "vertices":n,
    "arcs":sum(outdegrees.values()),
    "min_outdegree":min(outdegrees.values()),
    "max_outdegree":max(outdegrees.values()),
    "no_loops":no_loops,
    "no_digons":no_digons,
    "packed_cycles_valid":all(is_cycle(c) for c in [C1,C2,C3]),
    "R_acyclic":acyclic(R),
    "R_sinks":sinks,
    "tight_path_valid":all(tight_path[i+1] in A[tight_path[i]]
                           for i in range(len(tight_path)-1)),
    "x_fan_on_C1":fan,
    "C1_has_no_arc_to_x":all(17 not in A[c] for c in C1),
    "equal_size_exchange_cycle_valid":is_cycle(Cstar) and len(Cstar)==len(C1),
    "new_remainder_cycle":remainder_cycle,
    "new_remainder_cycle_valid":all(v in Rprime for v in remainder_cycle)
                                 and is_cycle(remainder_cycle),
    "four_pack_valid":four_pack_disjoint and all(is_cycle(c) for c in four_pack),
    "four_pack":four_pack,
  }
}
print(json.dumps(result,sort_keys=True,indent=2))
