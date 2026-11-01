import itertools
from fk_lib import comps

def canon(n, edges):
    pairs=list(itertools.combinations(range(n),2))
    idx={p:i for i,p in enumerate(pairs)}
    best=None
    for perm in itertools.permutations(range(n)):
        mask=0
        for (u,v) in edges:
            a,b=perm[u],perm[v]
            if a>b: a,b=b,a
            mask |= 1<<idx[(a,b)]
        if best is None or mask<best: best=mask
    return (n,best)

def connected_iso(n, mmax=99, min_edges=1, two_conn=False):
    pairs=list(itertools.combinations(range(n),2))
    M=len(pairs); seen=set(); out=[]
    for s in range(1<<M):
        e=[pairs[i] for i in range(M) if s>>i&1]
        if not (min_edges<=len(e)<=mmax): continue
        if comps(n,e,(1<<len(e))-1)!=1: continue
        if two_conn and not is_two_connected(n,e): continue
        c=canon(n,e)
        if c in seen: continue
        seen.add(c); out.append(e)
    return out

def is_two_connected(n, edges):
    if n<3: return False
    for v in range(n):
        vs=[u for u in range(n) if u!=v]
        rel={u:i for i,u in enumerate(vs)}
        e2=[(rel[a],rel[b]) for (a,b) in edges if a!=v and b!=v]
        if comps(n-1,e2,(1<<len(e2))-1)!=1: return False
    return True
