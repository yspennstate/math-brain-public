#!/usr/bin/env python3
import json
from collections import deque
from itertools import combinations

ADJ = {
0:[1,4,7,9,10,11,13],
1:[2,6,7,9,10,11,13],
2:[3,4,5,7,10,11,18],
3:[0,6,7,8,12,16,18],
4:[1,3,5,11,12,13,19],
5:[0,1,3,6,8,11,13],
6:[0,2,7,8,9,10,12],
7:[4,10,12,13,14,16,17],
8:[0,1,2,4,7,9,17],
9:[2,3,4,5,7,10,15],
10:[3,4,5,11,13,14,15],
11:[6,7,8,14,16,17,18],
12:[0,1,5,8,11,16,19],
13:[6,9,14,15,16,17,19],
14:[3,4,6,8,9,16,19],
15:[2,3,5,11,16,17,19],
16:[1,6,8,9,10,18,19],
17:[0,2,3,5,10,18,19],
18:[0,1,5,6,8,9,19],
19:[0,1,2,5,6,9,10],
}
A={u:set(vs) for u,vs in ADJ.items()}
V=set(A)
H=[0,1,2,3]; B=[4,5,6,7]; C=[8,9,10,11]; R=list(range(12,20)); x=19; b=4
PACK=[H,B,C]

def is_cycle(c):
    return len(c)>=2 and len(set(c))==len(c) and all(c[(i+1)%len(c)] in A[c[i]] for i in range(len(c)))

def chordless(c):
    S=set(c)
    allowed={(c[i],c[(i+1)%len(c)]) for i in range(len(c))}
    return all(((u,v) in allowed) == (v in A[u]) for u in c for v in c if u!=v)

def acyclic(vertices):
    S=set(vertices); indeg={v:0 for v in S}
    for u in S:
        for v in A[u]&S: indeg[v]+=1
    q=deque(v for v,d in indeg.items() if d==0); seen=0
    while q:
        u=q.popleft(); seen+=1
        for v in A[u]&S:
            indeg[v]-=1
            if indeg[v]==0:q.append(v)
    return seen==len(S)

def reachable(start, allowed):
    allowed=set(allowed)
    if start not in allowed: return set()
    q=[start]; seen={start}
    while q:
        u=q.pop()
        for v in A[u]:
            if v in allowed and v not in seen:
                seen.add(v); q.append(v)
    return seen

def strongly_connected_after_delete(deleted):
    S=V-set(deleted)
    if not S: return True
    s=next(iter(S))
    if reachable(s,S)!=S: return False
    rev={u:set() for u in S}
    for u in S:
        for v in A[u]&S: rev[v].add(u)
    q=[s]; seen={s}
    while q:
        u=q.pop()
        for v in rev[u]:
            if v not in seen:
                seen.add(v); q.append(v)
    return seen==S

def three_vertex_strong():
    return all(strongly_connected_after_delete(S) for k in (0,1,2) for S in combinations(V,k))

def dominated_arc(u,v):
    return any(w not in (u,v) and u in A[w] and v in A[w] for w in V)

def pair_fans(P,Q):
    T=set(P)|set(Q)
    return {u:len(A[u]&T) for u in V-T}

pair_data={}
for name,(P,Q) in {"HB":(H,B),"HC":(H,C),"BC":(B,C)}.items():
    vals=pair_fans(P,Q)
    pair_data[name]={"max":max(vals.values()),"five":sorted(u for u,z in vals.items() if z==5)}

four_pack=[[0,1,6],[2,3,8],[4,11,7],[5,13,9]]
result={
 "vertices":len(V),
 "arcs":sum(len(A[u]) for u in V),
 "outdegrees":sorted(set(len(A[u]) for u in V)),
 "no_loops":all(u not in A[u] for u in V),
 "no_digons":all(not(v in A[u] and u in A[v]) for u,v in combinations(sorted(V),2)),
 "packed_cycles_valid":all(is_cycle(c) for c in PACK),
 "packed_cycles_chordless":all(chordless(c) for c in PACK),
 "R_acyclic":acyclic(R),
 "R_sinks":sorted(u for u in R if not(A[u]&set(R))),
 "x_fans":{"H":sorted(A[x]&set(H)),"B":sorted(A[x]&set(B)),"C":sorted(A[x]&set(C))},
 "ports_to_x":{"H":sorted(u for u in H if x in A[u]),"B":sorted(u for u in B if x in A[u]),"C":sorted(u for u in C if x in A[u])},
 "all_arcs_dominated":all(dominated_arc(u,v) for u in V for v in A[u]),
 "three_vertex_strong":three_vertex_strong(),
 "pair_fans":pair_data,
 "port_cross_fan_HC":sorted(A[b]&(set(H)|set(C))),
 "port_R_outneighbors":sorted(A[b]&set(R)),
 "expected_exact_five_sets":{"HB":[8,9,19],"HC":[5,6,19],"BC":[0,1,2]},
 "exact_five_sets_match":pair_data["HB"]["five"]==[8,9,19] and pair_data["HC"]["five"]==[5,6,19] and pair_data["BC"]["five"]==[0,1,2],
 "four_pack":four_pack,
 "four_pack_valid":len(set(sum(four_pack,[])))==sum(map(len,four_pack)) and all(is_cycle(c) for c in four_pack),
}
print(json.dumps(result,sort_keys=True,indent=2))
