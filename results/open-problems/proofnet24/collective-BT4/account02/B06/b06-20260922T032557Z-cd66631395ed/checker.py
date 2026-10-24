#!/usr/bin/env python3
import itertools, json
from collections import deque
OUT = {
0:{1,4,5,7,8,10,11}, 1:{2,3,4,10,11,12,13}, 2:{0,3,9,11,12,14,15},
3:{0,4,7,9,11,12,14}, 4:{2,5,7,8,9,10,12}, 5:{1,2,3,8,9,13,15},
6:{0,1,2,3,4,5,7}, 7:{1,2,5,8,10,12,14}, 8:{1,2,3,6,9,11,13},
9:{0,1,6,10,11,12,15}, 10:{2,3,6,8,12,13,14}, 11:{4,5,6,7,12,13,14},
12:{0,5,6,8,13,14,15}, 13:{0,2,3,4,7,14,15}, 14:{0,1,4,5,6,8,15},
15:{0,1,3,4,6,7,8}}
V=set(OUT); A=(0,1,2); B=(3,4,5); C=(6,7,8); R=set(range(9,16))
def arc(u,v): return v in OUT[u]
def cyc(c): return all(arc(c[i],c[(i+1)%len(c)]) for i in range(len(c)))
def acyclic(S):
    S=set(S); indeg={v:0 for v in S}
    for u in S:
        for v in OUT[u]&S: indeg[v]+=1
    q=deque(v for v in S if indeg[v]==0); seen=0
    while q:
        u=q.popleft(); seen+=1
        for v in OUT[u]&S:
            indeg[v]-=1
            if indeg[v]==0:q.append(v)
    return seen==len(S)
def sc(S):
    S=set(S)
    if len(S)<=1:return True
    s=next(iter(S))
    def reach(rev=False):
        seen={s}; stack=[s]
        while stack:
            u=stack.pop()
            nbr=({v for v in S if u in OUT[v]} if rev else OUT[u]&S)
            for v in nbr:
                if v not in seen: seen.add(v); stack.append(v)
        return seen
    return len(reach())==len(S) and len(reach(True))==len(S)
def three_strong():
    for k in range(3):
        for rem in itertools.combinations(V,k):
            if not sc(V-set(rem)): return False,rem
    return True,None
def dominated():
    for x in V:
        for y in OUT[x]:
            if not any(x in OUT[z] and y in OUT[z] for z in V-{x,y}):
                return False,(x,y)
    return True,None
assert all(len(OUT[v])==7 for v in V)
assert all(v not in OUT[v] for v in V)
assert all(not (v in OUT[u] and u in OUT[v]) for u in V for v in V if u!=v)
assert cyc(A) and cyc(B) and cyc(C)
assert acyclic(R)
dom_ok,dom_bad=dominated(); assert dom_ok,dom_bad
k3_ok,k3_bad=three_strong(); assert k3_ok,k3_bad
u=6
residual=OUT[u]-(set(A)|set(B)); fanA=OUT[u]&set(A); fanB=OUT[u]&set(B)
assert residual=={7}
assert fanA==set(A) and fanB==set(B) and OUT[u].isdisjoint(R)
assert all(u not in OUT[a] for a in A) and all(u not in OUT[b] for b in B)
Q1=(8,11,7); Q2=(8,13,7)
for Q in (Q1,Q2):
    assert all(arc(Q[i],Q[i+1]) for i in range(len(Q)-1))
    assert set(Q[1:-1])<=R
assert set(Q1[1:-1]).isdisjoint(Q2[1:-1])
assert len(Q1)-1==2 < len(fanA)==3
four=[(0,1,2),(3,4,5),(6,7,10),(8,9,12)]
assert all(cyc(c) for c in four)
assert len(set().union(*(set(c) for c in four)))==12
n=10; x=0; y=1; z=2
D={i:{j for j in range(n) if j!=i} for i in range(n)}
D[z]-={8,9}
surv=set(range(n))-{x,y}
before=min(len(D[v]) for v in D)
after=min(len(D[v]&surv) for v in surv)
assert x in D[y] and y in D[x] and before==7 and after==5 and len(D[z]&surv)==5
result={"status":"PASS","base_graph":{"vertices":16,"outdegree_set":[7],"oriented":True,
"arc_dominated":dom_ok,"three_vertex_strong":k3_ok,"packed_cycles":[list(A),list(B),list(C)],
"packed_total":9,"globally_minimum_three_pack_by_absolute_lower_bound":True,
"remainder":sorted(R),"remainder_acyclic":True,"six_witness":{"u":u,"residual_outneighbors":sorted(residual),
"fan_split":[len(fanA),len(fanB)],"remainder_exits":sorted(OUT[u]&R),
"heavy_target_inport_from_A":any(u in OUT[a] for a in A),
"heavy_target_inport_from_B":any(u in OUT[b] for b in B),
"pure_R_bypasses":[list(Q1),list(Q2)],"bypass_lengths":[2,2],"naive_length_tax_m":3,
"naive_length_tax_violated":True},"explicit_four_pack":[list(c) for c in four]},
"digon_boundary":{"vertices":10,"digon":[x,y],"minimum_outdegree_before":before,
"minimum_outdegree_after_deleting_digon":after,"sharp_vertex":z,
"sharp_vertex_surviving_outdegree":len(D[z]&surv)}}
print(json.dumps(result,sort_keys=True,separators=(",",":")))
