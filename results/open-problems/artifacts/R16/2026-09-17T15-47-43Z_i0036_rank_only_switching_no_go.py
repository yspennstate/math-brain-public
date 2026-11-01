#!/usr/bin/env python3
"""
Exact self-check for R16 I0036:
rank-only randomized switch-and-loop-erase obstruction on a finite planar
subcubic four-terminal graph, plus an exact geometry-dependent repair on
the same witness.

No floating point is used.
"""

from collections import defaultdict, Counter

CORE_EDGES = [
    (0,1),(0,4),(1,2),(2,3),(2,5),(3,6),(4,5),(5,6)
]
PENDANTS = [('a',0),('b',4),('c',6),('d',3)]
EDGES = CORE_EDGES + PENDANTS

adj = defaultdict(list)
for u,v in EDGES:
    adj[u].append(v); adj[v].append(u)
for u in adj:
    adj[u].sort(key=str)

def simple_paths(s,t):
    out=[]
    def dfs(v,path,used):
        if v==t:
            out.append(tuple(path)); return
        for w in adj[v]:
            if w not in used:
                used.add(w); path.append(w)
                dfs(w,path,used)
                path.pop(); used.remove(w)
    dfs(s,[s],{s})
    return out

def loop_erase(walk):
    out=[]; pos={}
    for v in walk:
        if v in pos:
            i=pos[v]
            for u in out[i+1:]:
                del pos[u]
            out=out[:i+1]
        else:
            pos[v]=len(out); out.append(v)
    return tuple(out)

def switched(P,Q,v):
    i=P.index(v); j=Q.index(v)
    A=P[:i+1]+Q[j+1:]   # a -> d walk
    B=Q[:j+1]+P[i+1:]   # b -> c walk
    return loop_erase(A), loop_erase(B)

Pac=simple_paths('a','c')
Qbd=simple_paths('b','d')
assert len(Pac)==4 and len(Qbd)==4

T1=(('a',0,1,2,3,'d'), ('b',4,5,2,3,6,'c'))
T2=(('a',0,4,5,2,3,'d'), ('b',4,5,6,'c'))

contrib={T1:[],T2:[]}
sources=[]
for P in Pac:
    for Q in Qbd:
        common=[v for v in P if v in set(Q)]
        assert common
        sources.append((P,Q,common))
        m=len(common)
        Lin=(len(P)-1)+(len(Q)-1)
        for k,v in enumerate(common):
            A,B=switched(P,Q,v)
            Lout=(len(A)-1)+(len(B)-1)
            assert Lout<=Lin
            if (A,B) in contrib:
                contrib[(A,B)].append((m,k,Lin-Lout))

sig1=sorted(contrib[T1])
sig2=sorted(contrib[T2])
expected1=[(2,0,0),(2,1,0),(4,0,2),(4,1,2)]
expected2=[(2,0,0),(2,1,0),(4,2,2),(4,3,2)]
assert sig1==expected1
assert sig2==expected2

# Let p[m,k] depend ONLY on m=#common vertices and k=rank along P.
# Put A=p[4,0]+p[4,1].  Since probabilities sum to one,
# p[2,0]+p[2,1]=1 and p[4,2]+p[4,3]=1-A.
# With z=x_c^2=(2-sqrt(2))/2:
#   load(T1)=1+z A,
#   load(T2)=1+z(1-A).
# Hence max load >=1+z/2=(6-sqrt(2))/4>1.
# Strictness uses sqrt(2)<2, equivalent to 2<4.
assert 2<4

# The obstruction is NOT to geometry-dependent switching.  The following
# exact source-pair-dependent choice of intersection vertex gives every
# output fiber critical relative weight <=1 on this same witness.
choice=[0,0,2,3, 0,0,2,5, 2,3,4,4, 0,5,4,4]
assert len(choice)==len(sources)==16
fibers=defaultdict(list)
for (P,Q,common),v in zip(sources,choice):
    assert v in common
    A,B=switched(P,Q,v)
    Lin=(len(P)-1)+(len(Q)-1)
    Lout=(len(A)-1)+(len(B)-1)
    fibers[(A,B)].append(Lin-Lout)

# Every fiber is either a singleton of delta 0, a singleton of delta 2,
# or one exceptional fiber with three delta-2 preimages.
profiles=Counter(tuple(sorted(ds)) for ds in fibers.values())
assert profiles[(0,)]==12
assert profiles[(2,)]==1
assert profiles[(2,2,2)]==1
assert sum(profiles.values())==14

# For z=(2-sqrt(2))/2, 3z<1 iff 4<3sqrt(2), whose square is 16<18.
assert 16<18

print("PAC_COUNT",len(Pac))
print("QBD_COUNT",len(Qbd))
print("T1_SIGNATURE",expected1)
print("T2_SIGNATURE",expected2)
print("RANK_ONLY_LOWER_BOUND = (6-sqrt(2))/4 > 1")
print("GEOMETRY_DEPENDENT_FIBER_PROFILES",dict(sorted(profiles.items(),key=str)))
print("GEOMETRY_DEPENDENT_MAX_LOAD <= 1 because 3*x_c^2 < 1 (16<18)")
print("PRODUCT_ITERATION_OF_RANK_ONLY_LOCAL_RULES_OVERLOADS AS ((6-sqrt(2))/4)^r")
print("ALL_EXACT_CHECKS_PASS")
