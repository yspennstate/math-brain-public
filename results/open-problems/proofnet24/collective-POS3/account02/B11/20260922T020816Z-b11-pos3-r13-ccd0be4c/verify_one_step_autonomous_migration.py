#!/usr/bin/env python3
"""Exact finite stress-test for the POS3 one-step autonomous-chain migration lemma.

No finite census is treated as arbitrary-size closure.  This verifier enumerates
all naturally labelled transitive posets R through |R|<=6, substitutes one
chosen point by a chain of length m-1 and m (m=2,3), retains width<=3, and asks:

If P_{m-1} has a 1/3--2/3 balanced pair, then in P_m either
  (i) some pair already balanced in P_{m-1} remains balanced, or
  (ii) the newly added top chain element has a balanced incomparable pair.

All counts use exact integers and the uniform law on all linear extensions.
"""
from functools import lru_cache
from itertools import combinations
from collections import defaultdict

def natural_relation(n, mask):
    pairs=[(i,j) for i in range(n) for j in range(i+1,n)]
    rel=[[False]*n for _ in range(n)]
    for bit,(i,j) in enumerate(pairs):
        if (mask>>bit)&1:
            rel[i][j]=True
    for i in range(n):
        for j in range(i+1,n):
            if rel[i][j]:
                for k in range(j+1,n):
                    if rel[j][k] and not rel[i][k]:
                        return None
    return rel

def width(rel):
    n=len(rel); best=0
    for mask in range(1<<n):
        k=mask.bit_count()
        if k<=best: continue
        xs=[i for i in range(n) if (mask>>i)&1]
        if all(not rel[a][b] and not rel[b][a] for a,b in combinations(xs,2)):
            best=k
    return best

def key(rel):
    return tuple(tuple(row) for row in rel)

@lru_cache(maxsize=None)
def extension_data(k):
    rel=[list(row) for row in k]
    n=len(rel)
    pred=[]
    for y in range(n):
        mask=0
        for x in range(n):
            if rel[x][y]: mask |= 1<<x
        pred.append(mask)
    dp=[0]*(1<<n); dp[0]=1
    for S in range(1<<n):
        if not dp[S]: continue
        for x in range(n):
            if not ((S>>x)&1) and not (pred[x]&~S):
                dp[S|1<<x]+=dp[S]
    E=dp[-1]
    counts={}
    for a,b in combinations(range(n),2):
        if rel[a][b]:
            counts[(a,b)]=E
        elif rel[b][a]:
            counts[(a,b)]=0
        else:
            d=[0]*(1<<n); d[0]=1
            for S in range(1<<n):
                if not d[S]: continue
                for x in range(n):
                    if (S>>x)&1: continue
                    req=pred[x] | ((1<<a) if x==b else 0)
                    if not (req&~S):
                        d[S|1<<x]+=d[S]
            counts[(a,b)]=d[-1]
    return E,counts

def balanced(E,c):
    return 3*min(c,E-c) >= E

def balanced_pairs(rel):
    E,c=extension_data(key(rel))
    out=[]
    for a,b in combinations(range(len(rel)),2):
        if rel[a][b] or rel[b][a]: continue
        if balanced(E,c[(a,b)]):
            out.append((a,b))
    return E,c,out

def substitute_chain(R, mu, m):
    outside=[i for i in range(len(R)) if i!=mu]
    idx={old:i for i,old in enumerate(outside)}
    base=len(outside); N=base+m
    P=[[False]*N for _ in range(N)]
    for a in outside:
        for b in outside:
            if R[a][b]: P[idx[a]][idx[b]]=True
    for i in range(m):
        for j in range(i+1,m):
            P[base+i][base+j]=True
    for a in outside:
        if R[a][mu]:
            for j in range(m): P[idx[a]][base+j]=True
        if R[mu][a]:
            for j in range(m): P[base+j][idx[a]]=True
    return P, list(range(base,base+m))

stats=defaultdict(int)
for n in range(2,7):
    pair_count=n*(n-1)//2
    natural_count=0
    for mask in range(1<<pair_count):
        R=natural_relation(n,mask)
        if R is None: continue
        natural_count += 1
        for mu in range(n):
            for m in (2,3):
                stats["substitutions"] += 1
                P0,M0=substitute_chain(R,mu,m-1)
                P1,M1=substitute_chain(R,mu,m)
                if width(P1)>3:
                    stats["width_skip"] += 1
                    continue
                stats["width_retained"] += 1
                E0,c0,b0=balanced_pairs(P0)
                if not b0:
                    stats["antecedent_no_balance"] += 1
                    continue
                stats["antecedent_balance"] += 1
                E1,c1,b1=balanced_pairs(P1)
                old_surv=[ab for ab in b0 if balanced(E1,c1[ab])]
                x=M1[-1]
                new_top=[]
                for z in range(len(P1)):
                    if z==x or P1[x][z] or P1[z][x]: continue
                    a,b=sorted((x,z))
                    if balanced(E1,c1[(a,b)]):
                        new_top.append((x,z))
                if old_surv: stats["old_survival"] += 1
                if new_top: stats["new_top_balance"] += 1
                if old_surv and new_top:
                    stats["both"] += 1
                elif old_surv:
                    stats["old_only"] += 1
                elif new_top:
                    stats["new_only"] += 1
                else:
                    stats["failure"] += 1
                    raise AssertionError((n,mu,m))
    stats[f"natural_posets_n{n}"]=natural_count

expected={
    "natural_posets_n2":2,
    "natural_posets_n3":7,
    "natural_posets_n4":40,
    "natural_posets_n5":357,
    "natural_posets_n6":4824,
    "substitutions":61828,
    "width_retained":43570,
    "width_skip":18258,
    "antecedent_balance":43530,
    "antecedent_no_balance":40,
    "old_survival":43413,
    "new_top_balance":31324,
    "both":31207,
    "old_only":12206,
    "new_only":117,
    "failure":0,
}
for k,v in expected.items():
    assert stats[k]==v,(k,stats[k],v)

for k in sorted(expected):
    print(f"{k}={stats[k]}")
print("POS3_ONE_STEP_AUTONOMOUS_MIGRATION_STRESS_PASS")
