#!/usr/bin/env python3
import json
from itertools import combinations

ADJ={
'A0':['A1','B1','R1','R2','R4','R6','Z0'],
'A1':['A2','B2','R0','R1','R2','R4','Z1'],
'A2':['A0','B0','R1','R2','R3','R4','Z2'],
'B0':['A1','B1','R0','R1','R3','R5','R6'],
'B1':['A1','A2','B2','R0','R1','R2','R3'],
'B2':['A0','A2','B0','R2','R3','R4','R5'],
'Z0':['A1','A2','B0','B1','B2','R0','Z1'],
'Z1':['A0','A2','B0','B1','B2','R0','Z2'],
'Z2':['A0','A1','B0','B1','B2','R0','Z0'],
'R0':['A0','A2','B2','R1','R2','R5','R6'],
'R1':['B2','R2','R3','R4','R5','Z1','Z2'],
'R2':['B0','R3','R4','R6','Z0','Z1','Z2'],
'R3':['A0','A1','R4','R5','Z0','Z1','Z2'],
'R4':['B0','B1','R5','R6','Z0','Z1','Z2'],
'R5':['A0','A1','A2','B1','R6','Z0','Z1'],
'R6':['A1','A2','B1','B2','Z0','Z1','Z2']}
C1=('A0','A1','A2'); C2=('B0','B1','B2'); C3=('Z0','Z1','Z2')
R=tuple(f'R{i}' for i in range(7)); V=tuple(ADJ)
def arc(u,v): return v in ADJ[u]
def is_cycle(c): return all(arc(c[i],c[(i+1)%len(c)]) for i in range(len(c)))
def acyclic(S):
    S=set(S); indeg={v:0 for v in S}
    for u in S:
        for v in ADJ[u]:
            if v in S: indeg[v]+=1
    q=[v for v in S if indeg[v]==0]; seen=0
    while q:
        u=q.pop(); seen+=1
        for v in ADJ[u]:
            if v in S:
                indeg[v]-=1
                if indeg[v]==0:q.append(v)
    return seen==len(S)
def strong_after(delete=()):
    live=[v for v in V if v not in set(delete)]
    def reach(root,rev=False):
        seen={root}; st=[root]
        while st:
            u=st.pop()
            nxt=([w for w in live if arc(w,u)] if rev else [w for w in ADJ[u] if w in live])
            for w in nxt:
                if w not in seen: seen.add(w); st.append(w)
        return seen
    if not live:return True
    return len(reach(live[0]))==len(live) and len(reach(live[0],True))==len(live)

assert all(v not in ADJ[v] and len(ADJ[v])==7 and len(set(ADJ[v]))==7 for v in V)
for u,v in combinations(V,2): assert not (arc(u,v) and arc(v,u))
missing=[(u,v) for u,v in combinations(V,2) if not arc(u,v) and not arc(v,u)]
assert len(missing)==8 and all(is_cycle(c) for c in (C1,C2,C3)) and acyclic(R)
for k in (0,1,2):
    for S in combinations(V,k): assert strong_after(S)
undominated=[]
for u in V:
    for v in ADJ[u]:
        if not any(w not in (u,v) and arc(w,u) and arc(w,v) for w in V): undominated.append((u,v))
assert not undominated
H=set(C3+R); residual={v:sum(arc(v,w) for w in H if w!=v) for v in H}
assert min(residual.values())==2 and all(residual[z]==2 for z in C3)
witness={}
for i,z in enumerate(C3):
    cross=sum(arc(z,w) for w in C1+C2); rout=[w for w in R if arc(z,w)]
    resid=[w for w in H if w!=z and arc(z,w)]
    assert cross==5 and rout==['R0'] and set(resid)=={'R0',C3[(i+1)%3]}
    witness[z]={'cross_fan':cross,'R_out':rout,'residual_out':sorted(resid)}
heads=sorted({h for z in C3 for h in witness[z]['R_out']}); assert heads==['R0']
R_out={v:[w for w in R if arc(v,w)] for v in R}; sinks=[v for v in R if not R_out[v]]; assert sinks==['R6']
fan_R6=[sum(arc('R6',w) for w in C) for C in (C1,C2,C3)]; assert fan_R6==[2,2,3]
assert arc('A0','R6') and arc('B0','R6')
head={'R_out':R_out['R0'],'fan_counts':[sum(arc('R0',w) for w in C) for C in (C1,C2,C3)],'incoming_from_C3':[z for z in C3 if arc(z,'R0')]}
assert head['fan_counts']==[2,1,0] and len(head['incoming_from_C3'])==3
four=(('A0','A1','A2'),('B0','B1','R2'),('B2','R3','Z0'),('R0','R1','Z1'))
assert all(is_cycle(c) for c in four) and len(set().union(*(set(c) for c in four)))==12

# Digon adversary: all ordered arcs on ten vertices except d4->d2,d4->d3.
DV=tuple(f'd{i}' for i in range(10)); DX='d4'; DC=('d0','d1','d2','d3')
def darc(u,v): return u!=v and not (u==DX and v in {'d2','d3'})
dout={u:sum(darc(u,v) for v in DV) for u in DV}; assert min(dout.values())==7
assert all(darc(DC[i],DC[(i+1)%4]) for i in range(4)) and darc('d0',DX) and darc(DX,'d0')
dfan=[v for v in DC if darc(DX,v)]; L=1; m=len(dfan); claimed=['d1','d2']
assert dfan==['d0','d1'] and m==L+1 and m<len(DC) and set(dfan)!=set(claimed)

print(json.dumps({'status':'PASS','oriented_exact7_adversary':{'vertices':len(V),'arcs':sum(map(len,ADJ.values())),'missing_unordered_pairs':missing,'all_outdegree_7':True,'strong_after_any_two_vertex_deletions':True,'every_arc_dominated':True,'packing':[C1,C2,C3],'packing_total':9,'R_acyclic':True,'R_unique_sink':'R6','pair_C1_C2_residual_outdegrees':residual,'five_fan_cycle_witnesses':witness,'distinct_exit_heads':heads,'common_head_R0':head,'sink_R6_fans_C1_C2_C3':fan_R6,'explicit_four_pack':four},'digon_adversary':{'vertices':10,'minimum_outdegree':min(dout.values()),'outdegrees':dout,'cycle':DC,'b':'d0','x':DX,'b_to_x':True,'x_to_b':True,'L':L,'m':m,'actual_fan':dfan,'claimed_successor_window':claimed,'claim_fails':True}},indent=2,sort_keys=True))
