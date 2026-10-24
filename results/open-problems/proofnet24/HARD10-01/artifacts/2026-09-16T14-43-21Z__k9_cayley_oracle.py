#!/usr/bin/env python3
"""Independent exact K9 oracle via set partitions and Cayley forest-extension counts."""
from math import prod
N=9

def partitions(n):
    """All set partitions as restricted-growth strings."""
    a=[0]*n
    a[0]=0
    def rec(i,maxb):
        if i==n:
            blocks=[[] for _ in range(maxb+1)]
            for v,b in enumerate(a): blocks[b].append(v)
            yield tuple(tuple(x) for x in blocks)
            return
        for b in range(maxb+2):
            a[i]=b
            yield from rec(i+1,max(maxb,b))
    yield from rec(1,0)

def tau_complete(s):
    return 1 if s==1 else s**(s-2)

def forced_tree_count(s, nontrivial_component_sizes):
    """Trees of K_s containing a fixed forest with these nontrivial component sizes.

    Cayley's forest-extension formula: if the fixed forest has k components after
    including isolated vertices, the count is s^(k-2) times the product of the
    component sizes. The k=1 case is already a spanning tree and has count 1.
    """
    used=sum(nontrivial_component_sizes)
    k=len(nontrivial_component_sizes)+(s-used)
    if k==1:
        return 1
    return s**(k-2)*prod(nontrivial_component_sizes)

def block_of(P,v):
    for i,B in enumerate(P):
        if v in B: return i
    raise AssertionError

Z=Ze=Zef_adj=Zef_dis=0
npart=0
for P in partitions(N):
    npart+=1
    base=prod(tau_complete(len(B)) for B in P)
    Z+=base
    b0=block_of(P,0); b1=block_of(P,1)
    if b0==b1:  # e=(0,1)
        s=len(P[b0])
        other=prod(tau_complete(len(B)) for j,B in enumerate(P) if j!=b0)
        Ze += forced_tree_count(s,[2])*other
    b2=block_of(P,2)
    if b0==b1==b2:  # f=(0,2), adjacent to e
        s=len(P[b0])
        other=prod(tau_complete(len(B)) for j,B in enumerate(P) if j!=b0)
        Zef_adj += forced_tree_count(s,[3])*other
    b3=block_of(P,3)
    if b0==b1 and b2==b3:  # f=(2,3), disjoint from e
        if b0==b2:
            s=len(P[b0])
            other=prod(tau_complete(len(B)) for j,B in enumerate(P) if j!=b0)
            Zef_dis += forced_tree_count(s,[2,2])*other
        else:
            s=len(P[b0]); t=len(P[b2])
            other=prod(tau_complete(len(B)) for j,B in enumerate(P) if j not in (b0,b2))
            Zef_dis += forced_tree_count(s,[2])*forced_tree_count(t,[2])*other

print('partitions',npart)
print('Z',Z)
print('Ze',Ze)
print('Zef_adj',Zef_adj)
print('Zef_dis',Zef_dis)
print('delta_adj',Ze*Ze-Z*Zef_adj)
print('delta_dis',Ze*Ze-Z*Zef_dis)
