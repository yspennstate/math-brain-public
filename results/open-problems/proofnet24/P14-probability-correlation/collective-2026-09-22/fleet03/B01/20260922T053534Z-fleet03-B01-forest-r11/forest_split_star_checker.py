#!/usr/bin/env python3
"""Exact finite checks for fleet03/B01 FOREST split-star representation.

No floating point is used.  This script:
1. Exhaustively verifies the split/contraction multiplicity identity for every
   simple graph on at most five vertices and every nonedge u-v.
2. Exhaustively checks (finite evidence only) all {1,2}-star weighted simple
   graphs on at most five vertices for pairwise Rayleigh nonnegativity.
3. Verifies an exact six-vertex counterexample to coordinatewise monotonicity
   of the Rayleigh gap when one star edge is doubled.
"""
from itertools import combinations
from collections import Counter

def forest_mask(n, edges, mask):
    parent=list(range(n))
    def find(a):
        while parent[a]!=a:
            parent[a]=parent[parent[a]]
            a=parent[a]
        return a
    for i,(u,v) in enumerate(edges):
        if mask>>i & 1:
            a,b=find(u),find(v)
            if a==b:
                return False
            parent[a]=b
    return True

def connected_in_mask(n, edges, mask, s, t):
    parent=list(range(n))
    def find(a):
        while parent[a]!=a:
            parent[a]=parent[parent[a]]
            a=parent[a]
        return a
    for i,(u,v) in enumerate(edges):
        if mask>>i & 1:
            a,b=find(u),find(v)
            if a!=b:
                parent[a]=b
    return find(s)==find(t)

def contraction_classes(n, edges, u, v):
    survivors=[a for a in range(n) if a!=v]
    new_index={a:i for i,a in enumerate(survivors)}
    def rep(a):
        return u if a==v else a
    key_to_class={}
    preimages=[]
    edge_to_class={}
    for i,(a,b) in enumerate(edges):
        aa,bb=rep(a),rep(b)
        assert aa!=bb
        key=tuple(sorted((new_index[aa],new_index[bb])))
        if key not in key_to_class:
            key_to_class[key]=len(preimages)
            preimages.append([])
        c=key_to_class[key]
        preimages[c].append(i)
        edge_to_class[i]=c
    h_edges=[None]*len(preimages)
    for key,c in key_to_class.items():
        h_edges[c]=key
    multiplicity=[len(x) for x in preimages]
    assert all(m in (1,2) for m in multiplicity)
    return n-1,h_edges,multiplicity,edge_to_class

def verify_split_identity(max_n=5):
    instances=0
    conditional_forests=0
    for n in range(2,max_n+1):
        all_edges=list(combinations(range(n),2))
        M=len(all_edges)
        for graph_mask in range(1<<M):
            J=[all_edges[i] for i in range(M) if graph_mask>>i & 1]
            edge_set=set(J)
            for u,v in combinations(range(n),2):
                if (u,v) in edge_set:
                    continue
                hn,h_edges,mult,e2c=contraction_classes(n,J,u,v)
                actual=Counter()
                for mask in range(1<<len(J)):
                    if not forest_mask(n,J,mask):
                        continue
                    if connected_in_mask(n,J,mask,u,v):
                        continue
                    projected=0
                    for i in range(len(J)):
                        if mask>>i & 1:
                            c=e2c[i]
                            assert not (projected>>c & 1)
                            projected |= 1<<c
                    actual[projected]+=1
                expected=Counter()
                for mask in range(1<<len(h_edges)):
                    if not forest_mask(hn,h_edges,mask):
                        continue
                    w=1
                    for c,m in enumerate(mult):
                        if mask>>c & 1:
                            w*=m
                    expected[mask]=w
                assert actual==expected
                instances+=1
                conditional_forests+=sum(actual.values())
    return instances,conditional_forests

def weighted_counts(n, edges, doubled):
    forests=[mask for mask in range(1<<len(edges)) if forest_mask(n,edges,mask)]
    m=len(edges)
    Z=0
    z1=[0]*m
    z2=[[0]*m for _ in range(m)]
    for mask in forests:
        w=1 << sum((mask>>i)&1 for i in doubled)
        Z+=w
        chosen=[i for i in range(m) if mask>>i&1]
        for i in chosen:
            z1[i]+=w
        for a in range(len(chosen)):
            for b in range(a+1,len(chosen)):
                i,j=chosen[a],chosen[b]
                z2[i][j]+=w
                z2[j][i]+=w
    return Z,z1,z2

def verify_star2_small(max_n=5):
    instances=0
    pair_checks=0
    min_gap=None
    for n in range(2,max_n+1):
        all_edges=list(combinations(range(n),2))
        M=len(all_edges)
        for graph_mask in range(1<<M):
            edges=[all_edges[i] for i in range(M) if graph_mask>>i&1]
            if len(edges)<2:
                continue
            for x in range(n):
                star=[i for i,(u,v) in enumerate(edges) if u==x or v==x]
                for sm in range(1,1<<len(star)):
                    doubled={star[j] for j in range(len(star)) if sm>>j&1}
                    instances+=1
                    Z,z1,z2=weighted_counts(n,edges,doubled)
                    for e in range(len(edges)):
                        for f in range(e+1,len(edges)):
                            gap=z1[e]*z1[f]-Z*z2[e][f]
                            assert gap>=0
                            pair_checks+=1
                            min_gap=gap if min_gap is None else min(min_gap,gap)
    return instances,pair_checks,min_gap

def verify_monotonicity_counterexample():
    n=6
    edges=[
        (0,5),(0,1),(1,4),(0,4),(2,4),(4,5),
        (1,3),(0,3),(1,2),(1,5),(3,5),(2,5)
    ]
    e=0
    f=8
    h=9
    vals=[]
    for t in (0,1,2):
        Z,z1,z2=weighted_counts(n,edges,{h} if t==2 else set())
        if t==0:
            sub_edges=[ed for i,ed in enumerate(edges) if i!=h]
            old_to_new={}
            k=0
            for i in range(len(edges)):
                if i!=h:
                    old_to_new[i]=k
                    k+=1
            Z0,a1,a2=weighted_counts(n,sub_edges,set())
            Z=Z0
            ze=a1[old_to_new[e]]
            zf=a1[old_to_new[f]]
            zef=a2[old_to_new[e]][old_to_new[f]]
        else:
            ze=z1[e]
            zf=z1[f]
            zef=z2[e][f]
        vals.append((Z,ze,zf,zef,ze*zf-Z*zef))
    assert vals[0]==(722,244,268,86,3300)
    assert vals[1]==(1014,316,350,106,3116)
    assert vals[2]==(1306,388,432,126,3060)
    assert 3300-248+64==3116
    assert 3300-2*248+4*64==3060
    assert 3060 < 3116
    return vals

if __name__=="__main__":
    split=verify_split_identity(5)
    star=verify_star2_small(5)
    mono=verify_monotonicity_counterexample()
    print("SPLIT_IDENTITY_PASS instances=%d conditional_forests=%d" % split)
    print("STAR2_FINITE_PASS weighted_instances=%d marked_pair_checks=%d min_gap=%d" % star)
    print("MONOTONICITY_COUNTEREXAMPLE_PASS")
    print("t=0,1,2 rows (Z,Ze,Zf,Zef,Delta):", mono)
    print("Delta(t)=3300-248*t+64*t^2; Delta(2)=3060 < Delta(1)=3116")
    print("ALL_EXACT_ASSERTIONS_PASSED")
