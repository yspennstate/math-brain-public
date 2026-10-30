#!/usr/bin/env python3
"""Exact regression for the autonomous-chain corridor-weight formula.

For every naturally labelled finite poset through n=6, and every proper
autonomous subset M that is a chain, verify that after deleting M the number
of lifts of each linear extension tau of Q=P\M is

    binom(k + g(tau) - 1, k),

where k=|M| and g(tau) is the number of admissible gaps after the last
outside element lying below all of M and before the first outside element
lying above all of M.

Also verify an exact five-element counterexample showing that a balanced pair
in the one-point contraction need not lift to a balanced pair with the same
outside endpoint after expanding the contracted point to a two-chain.
"""
from itertools import combinations
from functools import lru_cache
from collections import Counter
from fractions import Fraction
from math import comb

def closure_from_mask(n, mask):
    lt=[0]*n
    pairs=list(combinations(range(n),2))
    for k,(i,j) in enumerate(pairs):
        if mask>>k & 1:
            lt[i] |= 1<<j
    for k in range(n):
        bk=1<<k
        for i in range(n):
            if lt[i]&bk:
                lt[i] |= lt[k]
    return tuple(lt)

def unique_natural_posets(n):
    pairs=n*(n-1)//2
    return {closure_from_mask(n,mask) for mask in range(1<<pairs)}

def linear_extensions(lt):
    n=len(lt)
    preds=[0]*n
    for i,row in enumerate(lt):
        for j in range(n):
            if row>>j & 1:
                preds[j] |= 1<<i
    @lru_cache(None)
    def rec(S):
        if S==(1<<n)-1:
            return ((),)
        out=[]
        for x in range(n):
            if not (S>>x)&1 and preds[x]&~S==0:
                for tail in rec(S|1<<x):
                    out.append((x,)+tail)
        return tuple(out)
    return rec(0)

def relation(lt,a,b):
    if lt[a]>>b & 1:
        return -1
    if lt[b]>>a & 1:
        return 1
    return 0

def autonomous_subsets(lt):
    n=len(lt)
    out=[]
    for r in range(2,n):
        for M in combinations(range(n),r):
            S=set(M)
            if all(len({relation(lt,z,m) for m in M})==1
                   for z in range(n) if z not in S):
                out.append(M)
    return out

def is_chain(lt,M):
    return all(relation(lt,a,b)!=0 for a,b in combinations(M,2))

def check_chain_module(lt,M):
    n=len(lt); S=set(M); k=len(M)
    outside=tuple(x for x in range(n) if x not in S)
    m0=M[0]
    D={z for z in outside if lt[z]>>m0 & 1}
    U={z for z in outside if lt[m0]>>z & 1}
    fibres=Counter(tuple(x for x in L if x not in S)
                   for L in linear_extensions(lt))
    for tau,count in fibres.items():
        pos={x:i+1 for i,x in enumerate(tau)}
        d=max((pos[z] for z in D), default=0)
        u=min((pos[z] for z in U), default=len(outside)+1)
        g=u-d
        predicted=comb(k+g-1,k)
        assert count==predicted, (lt,M,tau,count,predicted,d,u,g)
    return len(fibres)

def pair_prob(lt,x,y):
    L=linear_extensions(lt)
    num=sum(seq.index(x)<seq.index(y) for seq in L)
    return Fraction(num,len(L))

counts=[]
posets=chain_modules=fibres=0
for n in range(1,7):
    ps=unique_natural_posets(n)
    counts.append(len(ps))
    for lt in ps:
        posets += 1
        for M in autonomous_subsets(lt):
            if is_chain(lt,M):
                chain_modules += 1
                fibres += check_chain_module(lt,M)

# Q: chain 0<2<3 plus point 1 incomparable with that chain.
Q=(12,0,8,0)
assert len(linear_extensions(Q))==4
assert pair_prob(Q,1,2)==Fraction(1,2)

# P: expand point 1 to a two-chain 3<4; outside chain is 0<1<2.
# Thus P is the disjoint union of chains (0<1<2) and (3<4).
P=(6,4,0,16,0)
assert len(linear_extensions(P))==10
assert pair_prob(P,3,1)==Fraction(7,10)
assert pair_prob(P,4,1)==Fraction(3,10)
assert pair_prob(P,0,3)==Fraction(3,5)
assert pair_prob(P,2,4)==Fraction(2,5)

print("naturally_labelled_transitive_closures_by_n", counts)
print("posets_checked", posets)
print("proper_autonomous_chain_modules_checked", chain_modules)
print("deleted_order_fibres_checked", fibres)
print("corridor_weight_failures", 0)
print("contraction_example_Q_extensions", len(linear_extensions(Q)))
print("contraction_example_balanced_prob", pair_prob(Q,1,2))
print("expanded_example_P_extensions", len(linear_extensions(P)))
print("same_endpoint_module_probs", pair_prob(P,3,1), pair_prob(P,4,1))
print("expanded_example_other_balanced_probs", pair_prob(P,0,3), pair_prob(P,2,4))
print("POS3_AUTONOMOUS_CHAIN_CORRIDOR_CERTIFICATE_PASS")
