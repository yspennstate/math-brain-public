#!/usr/bin/env python3
"""Exact finite regression for the FOREST 3-terminal defect.

For fixed terminals 0,1,2 and a simple graph H, let
(d,a,b,c,t) count forests of H with terminal partitions
0|1|2, 01|2, 02|1, 12|0, 012.  The defect is
E = d*t - a*b - a*c - b*c.

The script exhausts every labelled simple graph on n<=6 by zeta-transforming
forest-state indicators.  For every present edge g it also checks the mixed
deletion/contraction coefficient B obtained from E(U+yV).

It independently expands E for K_n as a multivariate polynomial in edge
weights.  A product monomial is encoded by (union_mask, intersection_mask),
which exactly records exponents 1 and 2.  Coefficientwise nonnegativity for K_n
implies E>=0 for every nonnegative weighting of every simple subgraph on n
vertices (by setting missing weights to zero).
"""
from collections import defaultdict
from itertools import combinations

def forest_state(n, edges, mask):
    p=list(range(n))
    def find(x):
        while p[x]!=x:
            p[x]=p[p[x]]
            x=p[x]
        return x
    for i,(u,v) in enumerate(edges):
        if (mask>>i)&1:
            ru,rv=find(u),find(v)
            if ru==rv:
                return None
            p[rv]=ru
    r=[find(i) for i in range(3)]
    if r[0]==r[1]==r[2]: return 4
    if r[0]==r[1]: return 1
    if r[0]==r[2]: return 2
    if r[1]==r[2]: return 3
    return 0

def zeta_messages(n):
    edges=list(combinations(range(n),2))
    m=len(edges); N=1<<m
    arr=[[0]*N for _ in range(5)]
    for F in range(N):
        s=forest_state(n,edges,F)
        if s is not None: arr[s][F]=1
    for s in range(5):
        q=arr[s]
        for i in range(m):
            bit=1<<i
            for H in range(N):
                if H&bit: q[H]+=q[H^bit]
    return edges,arr

def defect(w):
    d,a,b,c,t=w
    return d*t-a*b-a*c-b*c

def mixed(U,V):
    d,a,b,c,t=U
    D,A,B,C,T=V
    return d*T+D*t-(a*B+A*b+a*C+A*c+b*C+B*c)

def graph_stats(n):
    edges,arr=zeta_messages(n)
    N=1<<len(edges)
    negE=posE=negB=posB=0
    minE=minB=None; checks=0
    for H in range(N):
        w=tuple(arr[s][H] for s in range(5))
        E=defect(w)
        minE=E if minE is None or E<minE else minE
        negE+=E<0; posE+=E>0
        for j in range(len(edges)):
            if (H>>j)&1:
                H0=H^(1<<j)
                U=tuple(arr[s][H0] for s in range(5))
                V=tuple(w[s]-U[s] for s in range(5))
                B=mixed(U,V)
                minB=B if minB is None or B<minB else minB
                negB+=B<0; posB+=B>0; checks+=1
    return len(edges),N,minE,negE,posE,checks,minB,negB,posB

def state_terms_kn(n):
    edges=list(combinations(range(n),2))
    terms=[[] for _ in range(5)]
    for F in range(1<<len(edges)):
        s=forest_state(n,edges,F)
        if s is not None: terms[s].append(F)
    return edges,terms

def product_masks(A,B):
    out=defaultdict(int)
    for x in A:
        for y in B:
            out[(x|y,x&y)]+=1
    return out

def coefficient_stats(n):
    edges,terms=state_terms_kn(n)
    d,a,b,c,t=terms
    E=defaultdict(int)
    for sign,A,B in ((1,d,t),(-1,a,b),(-1,a,c),(-1,b,c)):
        for k,v in product_masks(A,B).items():
            E[k]+=sign*v
    vals=list(E.values())
    return len(E), min(vals), sum(v<0 for v in vals), sum(v>0 for v in vals), max(vals), sum(v for v in vals if v>0)

def main():
    print("UNIT_GRAPH_AND_MIXED_CHECKS")
    for n in range(3,7):
        m,N,minE,negE,posE,checks,minB,negB,posB=graph_stats(n)
        print(f"n={n} edges={m} graphs={N} E_min={minE} E_neg={negE} E_pos={posE} "
              f"mixed_checks={checks} B_min={minB} B_neg={negB} B_pos={posB}")
        assert negE==0 and negB==0
    print("COEFFICIENTWISE_WEIGHTED_CHECKS_ON_K_n")
    for n in range(3,7):
        keys,mn,neg,pos,mx,psum=coefficient_stats(n)
        print(f"n={n} monomial_keys={keys} coeff_min={mn} coeff_neg={neg} "
              f"coeff_pos={pos} coeff_max={mx} positive_coeff_sum={psum}")
        assert neg==0
    print("ALL_EXACT_CHECKS_PASSED")

if __name__=="__main__":
    main()
