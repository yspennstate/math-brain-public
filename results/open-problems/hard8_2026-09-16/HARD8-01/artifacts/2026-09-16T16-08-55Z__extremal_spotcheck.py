#!/usr/bin/env python3
from collections import deque

def canonical_perm(parts):
    n=sum(parts); p=list(range(n)); b=0
    for L in parts:
        for i in range(L): p[b+i]=b+(i+1)%L
        b+=L
    return p

def power(p,e):
    out=[]
    for i in range(len(p)):
        x=i
        for _ in range(e): x=p[x]
        out.append(x)
    return out

def idem(n,s,t):
    a=list(range(n)); a[s]=t; return a

def exact_bfs(letters):
    n=len(letters[0]); full=(1<<n)-1
    def image(mask,t):
        out=0
        while mask:
            low=mask & -mask
            b=low.bit_length()-1
            mask-=low
            out |= 1<<t[b]
        return out
    q=deque([full]); dist={full:0}; prev={}
    while q:
        s=q.popleft()
        if s and s&(s-1)==0:
            word=[]; cur=s
            while cur!=full:
                ps,li=prev[cur]; word.append(li); cur=ps
            word.reverse()
            cur=full
            for li in word: cur=image(cur,letters[li])
            assert cur and cur&(cur-1)==0
            return dist[s],word,len(dist)
        for li,t in enumerate(letters):
            u=image(s,t)
            if u not in dist:
                dist[u]=dist[s]+1; prev[u]=(s,li); q.append(u)
    return -1,[],len(dist)

cases=[
 ("n10_k2",10,[9,1],7,[(0,7),(9,0)],65),
 ("n11_k2",11,[11],5,[(0,10),(5,4)],90),
]
print("HARD8_01_EXTREMAL_INDEPENDENT_PYTHON")
for name,n,parts,e,idems,expect in cases:
    g=canonical_perm(parts)
    letters=[power(g,0),power(g,e)]+[idem(n,s,t) for s,t in idems]
    rt,w,seen=exact_bfs(letters)
    print(name,"rt",rt,"states_seen",seen,"word","".join("ABCD"[x] for x in w))
    assert rt==expect
print("ALL_EXTREMAL_SPOTCHECKS_PASSED")
