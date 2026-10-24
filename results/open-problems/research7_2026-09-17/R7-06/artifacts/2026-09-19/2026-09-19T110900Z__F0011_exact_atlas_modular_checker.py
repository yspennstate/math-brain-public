#!/usr/bin/env python3
"""Exact finite certificate for R7-06 / F0011 through n=8.

Quotients twice:
  (i) diagonal sign switching fixes first-row off-diagonal signs to +1;
  (ii) permutations of the remaining n-1 coordinates identify the residual
       off-diagonal sign pattern with an unlabeled simple graph on n-1 vertices.
NetworkX's graph_atlas_g() is the standard atlas of all unlabeled graphs through
7 vertices. For each atlas graph G, orbit-stabilizer gives exactly
(n-1)!/|Aut(G)| labeled residual sign patterns. We enumerate all 2^n diagonal
sign patterns and use integer traces only. The weighted total is asserted equal
to 2^{n + C(n-1,2)}, independently checking the orbit accounting.

For n<=7 we additionally certify splitting of the characteristic polynomial
mod p=3,5,7 using the exact criterion (M^p-M)^n=0 over F_p. At n=8 we examine
all intersections of p in {3,5,7,11,13}.
"""
from itertools import combinations_with_replacement
from collections import Counter, defaultdict
from fractions import Fraction
import itertools
import math
import numpy as np
import networkx as nx

ATLAS = nx.graph_atlas_g()
EXPECTED_I = {1:2,2:2,3:10,4:10,5:154,6:274,7:15446,8:111290}
EXPECTED_SPLIT = {
  1:(2,2,2,2,2,2),
  2:(4,2,2,4,2,2),
  3:(16,10,10,10,10,10),
  4:(128,50,34,24,10,10),
  5:(2048,274,308,314,154,154),
  6:(65536,6226,4126,5346,1666,274),
  7:(4194304,166198,69192,115642,16566,15446),
}

def candidates(n):
    out=[]
    for lam in combinations_with_replacement(range(-n,n+1),n):
        if sum(x*x for x in lam)!=n*n: continue
        if n%2==0:
            if any(x&1 for x in lam): continue
        else:
            if sum(abs(x)&1 for x in lam)!=1: continue
        tr=sum(lam)
        if abs(tr)>n or ((tr-n)&1): continue
        p=tuple(sum(x**k for x in lam) for k in range(1,n+1))
        out.append((lam,p))
    return out

def atlas_graphs(m):
    if m==0:
        return [nx.empty_graph(0)]
    return [g for g in ATLAS if g.number_of_nodes()==m]

def aut_size(g):
    if g.number_of_nodes()<=1: return 1
    return sum(1 for _ in nx.algorithms.isomorphism.GraphMatcher(g,g).isomorphisms_iter())

def build_normalized_A(n,g):
    A=np.zeros((n,n),dtype=np.int64)
    if n>1:
        A[0,1:]=1; A[1:,0]=1
    for i in range(n-1):
        for j in range(i+1,n-1):
            v=1 if g.has_edge(i,j) else -1
            A[i+1,j+1]=A[j+1,i+1]=v
    return A

def diag_patterns(n):
    ids=np.arange(1<<n,dtype=np.uint16)
    D=np.empty((1<<n,n),dtype=np.int64)
    for i in range(n): D[:,i]=2*((ids>>i)&1).astype(np.int64)-1
    return D

def matpow_mod(A,e,p):
    B,n,_=A.shape
    R=np.zeros_like(A,dtype=np.int64); idx=np.arange(n); R[:,idx,idx]=1
    X=A%p
    while e:
        if e&1: R=(R@X)%p
        e//=2
        if e: X=(X@X)%p
    return R

def split_mask(A,p):
    n=A.shape[1]
    B=(matpow_mod(A,p,p)-A)%p
    return np.all(matpow_mod(B,n,p)==0,axis=(1,2))

def classify(n, do_mod=False):
    C=candidates(n); by_ps={p:lam for lam,p in C}; assert len(by_ps)==len(C)
    D=diag_patterns(n); idx=np.arange(n)
    spec=Counter(); total=0
    split={3:0,5:0,7:0}; joint35=0; joint357=0
    gs=atlas_graphs(n-1)
    for g in gs:
        aut=aut_size(g); w=math.factorial(n-1)//aut
        A=build_normalized_A(n,g)
        M=np.broadcast_to(A,(1<<n,n,n)).copy(); M[:,idx,idx]=D
        total += w*(1<<n)
        P=M.copy(); traces=[np.trace(P,axis1=1,axis2=2)]
        for k in range(2,n+1):
            P=P@M; traces.append(np.trace(P,axis1=1,axis2=2))
        for d in range(1<<n):
            powers=tuple(int(traces[k][d]) for k in range(n))
            lam=by_ps.get(powers)
            if lam is not None: spec[lam]+=w
        if do_mod:
            m3=split_mask(M,3); m5=split_mask(M,5); m7=split_mask(M,7)
            split[3]+=w*int(m3.sum()); split[5]+=w*int(m5.sum()); split[7]+=w*int(m7.sum())
            joint35+=w*int((m3&m5).sum()); joint357+=w*int((m3&m5&m7).sum())
    expected_total=1 << (n + (n-1)*(n-2)//2)
    assert total==expected_total,(n,total,expected_total)
    I=sum(spec.values()); assert I==EXPECTED_I[n],(n,I)
    if do_mod:
        got=(total,split[3],split[5],split[7],joint35,joint357)
        assert got==EXPECTED_SPLIT[n],(n,got,EXPECTED_SPLIT[n])
        assert joint357==I
    return C,spec,total,(split,joint35,joint357) if do_mod else None,len(gs)

def modular_subsets_n8():
    n=8; primes=[3,5,7,11,13]
    D=diag_patterns(n); idx=np.arange(n)
    subs=[s for r in range(1,len(primes)+1) for s in itertools.combinations(primes,r)]
    counts={s:0 for s in subs}
    for g in atlas_graphs(7):
        aut=aut_size(g); w=math.factorial(7)//aut
        A=build_normalized_A(n,g)
        M=np.broadcast_to(A,(1<<n,n,n)).copy(); M[:,idx,idx]=D
        masks={p:split_mask(M,p) for p in primes}
        for sub in subs:
            keep=np.ones(1<<n,dtype=bool)
            for p in sub: keep &= masks[p]
            counts[sub]+=w*int(keep.sum())
    I8=111290
    assert all(counts[sub]!=I8 for sub in itertools.combinations(primes,2))
    assert counts[(3,5,13)]==I8
    assert counts[(3,7,13)]==I8
    assert counts[(5,7,13)]==I8
    assert counts[(5,11,13)]==I8
    assert counts[(7,11,13)]==111306
    return primes,counts

def main():
    print('F0011 exact switching/permutation quotient certificate')
    print('n atlas_graphs candidates total integral spectra probability')
    results={}
    for n in range(1,9):
        C,spec,total,mod,ng=classify(n,do_mod=(n<=7))
        f=Fraction(sum(spec.values()),total)
        print(n,ng,len(C),total,sum(spec.values()),len(spec),f'{f.numerator}/{f.denominator}')
        results[n]=(C,spec,total,mod)
    print('\nmodular splitting census through n=7')
    print('n total split3 split5 split7 split3and5 split3and5and7')
    for n in range(1,8):
        split,j35,j357=results[n][3]
        total=results[n][2]
        print(n,total,split[3],split[5],split[7],j35,j357)
    C,spec,total,_=results[8]
    print('\nn=8 exact details')
    print('integral normalized I_8:',sum(spec.values()))
    print('all-matrix integral count:',sum(spec.values())*(1<<7),'of',1<<36)
    print('max normalized cospectral fiber:',max(spec.values()))
    profile=defaultdict(lambda:[0,0,0])
    for lam,c in spec.items():
        r=len(set(lam)); profile[r][0]+=c; profile[r][1]+=1; profile[r][2]=max(profile[r][2],c)
    print('r integral_matrices spectra max_fiber')
    for r in sorted(profile): print(r,*profile[r])
    print('realized spectra and normalized counts:')
    for lam,c in sorted(spec.items()): print(f'{c:6d}  {lam}')
    assert len(C)==39 and len(spec)==33 and max(spec.values())==24360
    primes,counts=modular_subsets_n8()
    print('\nn=8 modular splitting over',primes)
    print('single-prime counts:')
    for p in primes: print(p,counts[(p,)])
    print('all two-prime intersections:')
    for sub in itertools.combinations(primes,2): print(sub,counts[sub])
    print('all three-prime intersections:')
    for sub in itertools.combinations(primes,3): print(sub,counts[sub])
    exact=[sub for sub,c in counts.items() if c==111290]
    print('subsets with count exactly I_8=111290:')
    for sub in sorted(exact,key=lambda x:(len(x),x)): print(sub)
    print('MINIMUM CERTIFYING SUBSET SIZE WITHIN {3,5,7,11,13}: 3')
    print('ALL_EXACT_ASSERTIONS_PASS')
if __name__=='__main__': main()
