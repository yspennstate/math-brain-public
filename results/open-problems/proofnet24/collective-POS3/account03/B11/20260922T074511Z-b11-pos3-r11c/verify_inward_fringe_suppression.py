#!/usr/bin/env python3
"""
POS3 exact-two positive crossed-distinguisher inward-fringe verifier.

The symbolic theorem in REPORT.md is arbitrary-size. This program is only a
finite regression:
  (1) exact interval-fiber word inequalities;
  (2) all naturally labelled posets through n=6.
No external packages or network access.
"""
from itertools import permutations, product

def closure_from_edges(n, mask):
    pairs=[(i,j) for i in range(n) for j in range(i+1,n)]
    reach=[0]*n
    for k,(i,j) in enumerate(pairs):
        if (mask>>k)&1:
            reach[i] |= 1<<j
    for k in range(n-1,-1,-1):
        for i in range(k):
            if (reach[i]>>k)&1:
                reach[i] |= reach[k]
    return tuple(reach)

def all_posets(n):
    seen=set()
    m=n*(n-1)//2
    for mask in range(1<<m):
        r=closure_from_edges(n,mask)
        if r not in seen:
            seen.add(r)
            yield r

def incomparable(r,u,v):
    return not ((r[u]>>v)&1) and not ((r[v]>>u)&1)

def rel(r,u,v):
    if (r[u]>>v)&1:
        return -1
    if (r[v]>>u)&1:
        return 1
    return 0

def linear_extensions(n,r):
    pred=[0]*n
    for u in range(n):
        for v in range(n):
            if (r[u]>>v)&1:
                pred[v] |= 1<<u
    out=[]
    def rec(mask,seq):
        if len(seq)==n:
            out.append(tuple(seq)); return
        for v in range(n):
            if not (mask>>v)&1 and pred[v]&~mask==0:
                rec(mask|(1<<v),seq+(v,))
    rec(0,())
    return out

def distinguishers(n,r,p,q):
    return [z for z in range(n) if z not in (p,q) and rel(r,z,p)!=rel(r,z,q)]

def count_word(word, intervals):
    ranges=[range(intervals[c][0],intervals[c][1]+1) for c in word]
    ans=0
    for gaps in product(*ranges):
        if all(gaps[i]<=gaps[i+1] for i in range(len(gaps)-1)):
            ans+=1
    return ans

words_inc=[
    ('p','d','q','u'),
    ('p','d','u','q'),
    ('p','u','d','q'),
    ('d','p','q','u'),
    ('d','p','u','q'),
    ('d','q','p','u'),
]
words_comp=[w for w in words_inc if w.index('d')<w.index('u')]

fiber_instances=0
for m in range(0,7):
    for lo in range(m+1):
        for hi in range(lo,m+1):
            I=(lo,hi)
            for ld in range(lo+1):
                for ud in range(ld,hi+1):
                    Id=(ld,ud)
                    for lu in range(lo,m+1):
                        for uu in range(max(lu,hi),m+1):
                            Iu=(lu,uu)
                            intervals={'p':I,'q':I,'d':Id,'u':Iu}
                            for words in (words_inc,words_comp):
                                counts={w:count_word(w,intervals) for w in words}
                                T=sum(counts.values())
                                if not T:
                                    continue
                                fiber_instances+=1
                                pd=sum(c for w,c in counts.items() if w.index('p')<w.index('d'))
                                uq=sum(c for w,c in counts.items() if w.index('u')<w.index('q'))
                                assert 2*pd <= T, (m,I,Id,Iu,words,pd,T)
                                assert 2*uq <= T, (m,I,Id,Iu,words,uq,T)

posets=0
ordered_incomparable_pairs=0
crossed_exact_two_cases=0
cases_by_n={}
for n in range(2,7):
    c_n=0
    for r in all_posets(n):
        posets += 1
        le=linear_extensions(n,r)
        E=len(le)
        pair=[[0]*n for _ in range(n)]
        for L in le:
            pos=[0]*n
            for i,v in enumerate(L):
                pos[v]=i
            for a in range(n):
                for b in range(n):
                    if a!=b and pos[a]<pos[b]:
                        pair[a][b]+=1
        for p in range(n):
            for q in range(n):
                if p==q or not incomparable(r,p,q):
                    continue
                ordered_incomparable_pairs+=1
                D=distinguishers(n,r,p,q)
                if len(D)!=2:
                    continue
                lowers=[d for d in D if rel(r,d,q)==-1 and incomparable(r,d,p)]
                uppers=[u for u in D if rel(r,p,u)==-1 and incomparable(r,u,q)]
                if len(lowers)==1 and len(uppers)==1 and set(lowers+uppers)==set(D):
                    d,u=lowers[0],uppers[0]
                    crossed_exact_two_cases+=1
                    c_n+=1
                    assert 2*pair[p][d] <= E, (n,r,p,q,d,u,E,pair[p][d])
                    assert 2*pair[u][q] <= E, (n,r,p,q,d,u,E,pair[u][q])
    cases_by_n[n]=c_n

print("fiber_instances", fiber_instances)
print("posets", posets)
print("ordered_incomparable_pairs", ordered_incomparable_pairs)
print("crossed_exact_two_cases", crossed_exact_two_cases)
print("cases_by_n", cases_by_n)
print("POS3_INWARD_FRINGE_SUPPRESSION_CHECK_PASS")
