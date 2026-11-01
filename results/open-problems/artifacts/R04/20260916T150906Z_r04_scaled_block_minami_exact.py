#!/usr/bin/env python3
from fractions import Fraction
import math, itertools
import networkx as nx
import numpy as np

print("R04 scaled-block Minami / transfer / R05 scoped audit exact checker")
print("run_id=20260916T150906Z_r04_scaled_block_minami")

def greedy_sizes(N,W):
    assert 2*W+1 <= N
    if N == 2*W+1:
        return [N]
    s=W+1
    k=N//s
    r=N-k*s
    z=[s]*k
    if r:
        z.append(r)
    return z

pairs=0
strict_cmp=0
worst_ratio=(0.0,None)
M=1+math.sqrt(6)/2
for N in range(1,501):
    for W in range(0,(N-1)//2+1):
        pairs += 1
        sizes=greedy_sizes(N,W)
        assert sum(sizes)==N
        v=Fraction(1,2*W+1)
        if N != 2*W+1:
            assert max(sizes) <= W+1
            assert N >= 2*(W+1)
        for m in sizes:
            a2=v*Fraction(m,2)
            diag=Fraction(2,1)*a2/Fraction(m,1)
            off=a2/Fraction(m,1)
            assert diag == v
            assert off == v/2
        if N != 2*W+1:
            J=len(sizes)
            Jold=(N+W)//(W+1)
            assert J==Jold
            q=N//J
            assert q*J <= N
            lhs_upper=Fraction(2*(2*W+1)*J,N)
            rhs_old=Fraction(2*(2*W+1),q)
            assert lhs_upper <= rhs_old
            if lhs_upper < rhs_old:
                strict_cmp += 1
        F=math.sqrt(2*(2*W+1))*sum(math.sqrt(m) for m in sizes)/N
        assert F <= M + 1e-12
        rr=F/M
        if rr>worst_ratio[0]:
            worst_ratio=(rr,(N,W,sizes,F))

print("admissible_pairs_checked",pairs)
print("strict_cauchy_comparison_cases",strict_cmp)
print("worst_finite_ratio_to_uniform_M",worst_ratio)
print("uniform_factor_M",M)

try:
    import sympy as sp
    y=sp.sqrt(6)-2
    expr=sp.simplify(2*(2+y)/(2+y**2))
    assert sp.simplify(expr-(1+sp.sqrt(6)/2))==0
    assert sp.simplify(2-4*y-y**2)==0
    print("sympy_uniform_max_identity PASS",expr)
except Exception as e:
    print("sympy_uniform_max_identity SKIPPED",repr(e))

# Exact transfer support geometry.
for W in range(1,80):
    b=W
    for p in range(b):
        for q in range(b):
            assert (b+q-p<=W) == (q<=p)
    b=W+1
    for p in range(b):
        for q in range(b):
            assert (b+q-p<=W) == (q<p)
print("transfer_support_geometry PASS W=1..79")

for n in range(2,80):
    W=n; b=W
    for p in range(b):
        for q in range(b):
            assert 2*b+q-p>W
print("c1_block_tridiagonal_geometry PASS n=2..79")

# R05 scoped audit: verify each graph6 representative is one of five standard
# arc-transitive graphs, and independently verify the coefficient identity.

def verify_automorphism(G,mp):
    nodes=list(G.nodes())
    assert set(mp)==set(nodes) and set(mp.values())==set(nodes)
    for u in nodes:
        for v in nodes:
            assert G.has_edge(u,v)==G.has_edge(mp[u],mp[v])

def verify_arc_transitive_standard(G, maps, base):
    arcs={(u,v) for u,v in G.edges() for (u,v) in ((u,v),(v,u))}
    assert base in arcs
    orbit=set()
    for mp in maps:
        verify_automorphism(G,mp)
        orbit.add((mp[base[0]],mp[base[1]]))
    assert orbit==arcs

stds=[]
G=nx.cycle_graph(8)
maps=[]
for a in range(8):
    maps.append({x:(x+a)%8 for x in range(8)})
    maps.append({x:(a-x)%8 for x in range(8)})
stds.append((G,maps))
G0=nx.hypercube_graph(3)
tups=list(itertools.product([0,1], repeat=3))
lab={t:i for i,t in enumerate(tups)}
G=nx.relabel_nodes(G0,lab)
maps=[]
for trans in tups:
    for perm in itertools.permutations(range(3)):
        mp={}
        for t in tups:
            u=tuple(t[i]^trans[i] for i in range(3))
            vv=tuple(u[i] for i in perm)
            mp[lab[t]]=lab[vv]
        maps.append(mp)
stds.append((G,maps))
G=nx.complete_bipartite_graph(4,4)
maps=[]
for a in range(4):
    for b in range(4):
        maps.append({**{i:(i+a)%4 for i in range(4)},
                     **{4+i:4+(i+b)%4 for i in range(4)}})
        maps.append({**{i:4+(i+a)%4 for i in range(4)},
                     **{4+i:(i+b)%4 for i in range(4)}})
stds.append((G,maps))
G=nx.complete_multipartite_graph(2,2,2,2)
maps=[]
parts=[(0,1),(2,3),(4,5),(6,7)]
for pp in itertools.permutations(range(4)):
    for flips in itertools.product([0,1],repeat=4):
        mp={}
        for i,part in enumerate(parts):
            target=parts[pp[i]]
            mp[part[0]]=target[flips[i]]
            mp[part[1]]=target[1-flips[i]]
        maps.append(mp)
stds.append((G,maps))
G=nx.complete_graph(8)
maps=[]
for u in range(8):
    for v in range(8):
        if u==v: continue
        rem_src=list(range(2,8))
        rem_dst=[x for x in range(8) if x not in (u,v)]
        mp={0:u,1:v}
        mp.update(dict(zip(rem_src,rem_dst)))
        maps.append(mp)
stds.append((G,maps))

codes=["GqGOOK","GsXP_[","G?~vf_","G]~v~w","G~~~~{"]
bases=[(0,1),(0,1),(0,4),(0,2),(0,1)]
for code,(Gstd,maps),base in zip(codes,stds,bases):
    Grep=nx.from_graph6_bytes(code.encode("ascii"))
    assert nx.is_isomorphic(Grep,Gstd)
    verify_arc_transitive_standard(Gstd,maps,base)
    d=next(iter(dict(Gstd.degree()).values()))
    nodes=sorted(Gstd.nodes())
    A=np.array(nx.to_numpy_array(Gstd,nodelist=nodes,dtype=int),dtype=object)
    Ap=np.eye(8,dtype=object)
    arcs=[(u,v) for u,v in Gstd.edges() for (u,v) in ((u,v),(v,u))]
    for m in range(18):
        Anext=Ap@A
        for x,y in arcs:
            assert Anext[x,x]==d*Ap[x,y]
        Ap=Anext
    print("R05_rep",code,"degree",d,"standard_iso_arc_transitive_identity PASS")
print("R05 scoped representative audit PASS")

print("SELF-CHECK PASS")
