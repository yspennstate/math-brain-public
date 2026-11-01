#!/usr/bin/env python3
"""Independent exact oracle for one n=9 graph/pair via set partitions and integer Kirchhoff after contraction."""
from functools import lru_cache
from math import prod
G6='HJ~~~~~'
N=9
# decode exactly in graph6 order used by C checker
bits=[]
for ch in G6[1:]:
    x=ord(ch)-63
    bits += [(x>>b)&1 for b in range(5,-1,-1)]
edges=[]; p=0
for j in range(1,N):
    for i in range(j):
        if bits[p]: edges.append((i,j))
        p+=1
E0=edges[0]; E1=edges[3]
print('g6',G6,'m',len(edges),'e0',E0,'e3',E1)

def bareiss_det(A):
    n=len(A)
    if n==0:return 1
    M=[row[:] for row in A]
    sign=1; prev=1
    for k in range(n-1):
        if M[k][k]==0:
            r=next((r for r in range(k+1,n) if M[r][k]),None)
            if r is None:return 0
            M[k],M[r]=M[r],M[k]; sign=-sign
        piv=M[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                M[i][j]=(M[i][j]*piv-M[i][k]*M[k][j])//prev
        prev=piv
        for i in range(k+1,n): M[i][k]=0
        for j in range(k+1,n): M[k][j]=0
    return sign*M[n-1][n-1]

@lru_cache(None)
def tau(block_tuple, forced_tuple):
    V=list(block_tuple); forced=list(forced_tuple)
    if not V:return 1
    parent={v:v for v in V}
    def find(a):
        while parent[a]!=a:
            parent[a]=parent[parent[a]]; a=parent[a]
        return a
    def union(a,b):
        a,b=find(a),find(b)
        if a==b:return False
        parent[b]=a; return True
    for ei in forced:
        a,b=edges[ei]
        if a not in parent or b not in parent:return 0
        if not union(a,b):return 0
    roots={v:find(v) for v in V}
    uniq=sorted(set(roots.values()))
    idx={r:i for i,r in enumerate(uniq)}
    k=len(uniq)
    if k==1:return 1
    L=[[0]*k for _ in range(k)]
    forced_set=set(forced)
    for ei,(a,b) in enumerate(edges):
        if a not in parent or b not in parent or ei in forced_set: continue
        ia,ib=idx[find(a)],idx[find(b)]
        if ia==ib:continue
        L[ia][ia]+=1; L[ib][ib]+=1; L[ia][ib]-=1; L[ib][ia]-=1
    M=[row[:-1] for row in L[:-1]]
    return bareiss_det(M)

def partitions(n):
    a=[0]*n
    def rec(i,m):
        if i==n:
            B=[[] for _ in range(m+1)]
            for v,b in enumerate(a):B[b].append(v)
            yield tuple(tuple(x) for x in B);return
        for b in range(m+2):
            a[i]=b; yield from rec(i+1,max(m,b))
    yield from rec(1,0)

def which(P,v):
    for i,B in enumerate(P):
        if v in B:return i
    raise RuntimeError
Z=Ze=Zf=Zef=0
for P in partitions(N):
    ts=[tau(tuple(B),tuple()) for B in P]
    base=prod(ts); Z+=base
    a,b=E0; c,d=E1
    ie=which(P,a); je=which(P,b); jf=which(P,c); kf=which(P,d)
    if ie==je:
        oe=prod(ts[j] for j in range(len(P)) if j!=ie)
        te=tau(tuple(P[ie]),(0,)); Ze+=te*oe
    if jf==kf:
        of=prod(ts[j] for j in range(len(P)) if j!=jf)
        tf=tau(tuple(P[jf]),(3,)); Zf+=tf*of
    if ie==je and jf==kf:
        if ie==jf:
            oth=prod(ts[j] for j in range(len(P)) if j!=ie)
            Zef += tau(tuple(P[ie]),(0,3))*oth
        else:
            oth=prod(ts[j] for j in range(len(P)) if j not in (ie,jf))
            Zef += tau(tuple(P[ie]),(0,))*tau(tuple(P[jf]),(3,))*oth
print('Z',Z,'Ze',Ze,'Zf',Zf,'Zef',Zef,'delta',Ze*Zf-Z*Zef)
