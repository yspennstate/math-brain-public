#!/usr/bin/env python3
"""Exact rooted-isomorphism completeness check for R20/KNSV transfer signatures.

For connected simple two-terminal networks with r=1,2,3,4 internal vertices
and no direct terminal-terminal edge, verify that every ordinary two-boundary
transfer signature is a single terminal-fixed isomorphism class, and every
pointed three-boundary transfer signature is a single terminal-and-mark-fixed
isomorphism class.  This justifies replacing raw networks by transfer-signature
representatives in the n=12 one-cross-edge search without losing loopy data:
for these sizes, quotienting by transfer signature is no coarser than rooted
isomorphism.
"""
from itertools import combinations, permutations
from collections import Counter, defaultdict

def dsu_state(n,allowed,mask,bounds):
    p=list(range(n)); sz=[1]*n
    def f(x):
        while p[x]!=x:
            p[x]=p[p[x]]; x=p[x]
        return x
    for i,(a,b) in enumerate(allowed):
        if (mask>>i)&1:
            a,b=f(a),f(b)
            if a!=b:
                if sz[a]<sz[b]: a,b=b,a
                p[b]=a; sz[a]+=sz[b]
    roots=[f(i) for i in range(n)]
    bpos={b:i for i,b in enumerate(bounds)}; comp={}
    for b,i in bpos.items():
        r=roots[b]; comp.setdefault(r,[0,0])[0] |= 1<<i
    for v in range(n):
        if v not in bpos and roots[v] in comp: comp[roots[v]][1]+=1
    blocks=tuple(sorted((a,b) for a,b in comp.values())); seen=set(comp); closed=[]
    for v in range(n):
        if v in bpos: continue
        r=roots[v]
        if r not in comp and r not in seen:
            seen.add(r); closed.append(sum(x==r for x in roots))
    return (blocks,tuple(sorted(closed)),mask.bit_count()), len(set(roots))==1

def submasks(mask):
    s=mask
    while True:
        yield s
        if s==0: return
        s=(s-1)&mask

def check_r(r):
    n=r+2
    allowed=[e for e in combinations(range(n),2) if e!=(0,1)]
    idx={e:i for i,e in enumerate(allowed)}
    T=1<<len(allowed)
    st2=[None]*T; st3=[[None]*T for _ in range(r)]; conn=[False]*T
    for m in range(T):
        st2[m],conn[m]=dsu_state(n,allowed,m,(0,1))
        for j in range(r): st3[j][m]=dsu_state(n,allowed,m,(0,1,2+j))[0]
    def transform(m,pmap):
        out=0; x=m
        while x:
            lb=x&-x; i=lb.bit_length()-1; x-=lb
            a,b=allowed[i]; A,B=pmap[a],pmap[b]
            if A>B: A,B=B,A
            out |= 1<<idx[(A,B)]
        return out
    iperms=[[0,1]+list(q) for q in permutations(range(2,n))]
    def canon_un(m):
        return min(transform(m,p) for p in iperms)
    def canon_pt(m,j):
        mark=2+j; rest=[v for v in range(2,n) if v!=mark]
        vals=[]
        for dests in permutations(range(3,n)):
            p=[None]*n; p[0]=0; p[1]=1; p[mark]=2
            for old,new in zip(rest,dests): p[old]=new
            vals.append(transform(m,p))
        return min(vals)
    gu=defaultdict(set); gp=defaultdict(set); connected=0
    for m in range(T):
        if not conn[m]: continue
        connected+=1; ss=list(submasks(m))
        su=tuple(sorted(Counter(st2[s] for s in ss).items()))
        gu[su].add(canon_un(m))
        for j in range(r):
            sp=tuple(sorted(Counter(st3[j][s] for s in ss).items()))
            gp[sp].add(canon_pt(m,j))
    au=sum(len(v)>1 for v in gu.values()); ap=sum(len(v)>1 for v in gp.values())
    maxu=max(map(len,gu.values())); maxp=max(map(len,gp.values()))
    return connected,len(gu),len(gp),au,ap,maxu,maxp

print('R20 KNSV exact transfer-signature rooted-isomorphism completeness check')
expected={1:(1,1,1),2:(14,8,14),3:(314,67,171),4:(12424,701,2394)}
for r in range(1,5):
    connected,u,p,au,ap,maxu,maxp=check_r(r)
    print(f'r={r} connected={connected} unpointed_types={u} pointed_types={p} unpointed_ambiguous={au} pointed_ambiguous={ap} max_rooted_classes_per_unpointed_signature={maxu} max_rooted_classes_per_pointed_signature={maxp}')
    assert (connected,u,p)==expected[r]
    assert au==0 and ap==0 and maxu==1 and maxp==1
print('VERDICT=PASS: for r<=4 every transfer signature used by the n=12 search is exactly one rooted/pointed isomorphism class.')
