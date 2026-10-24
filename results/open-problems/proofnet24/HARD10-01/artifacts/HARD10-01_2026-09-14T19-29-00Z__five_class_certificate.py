#!/usr/bin/env python3
"""Exact certificate for HARD10-01 (uniform random forests).

Verifies the five-class decomposition and a near-saturating 10-vertex example.
Standard library only. This is a finite certificate, not a universal proof.
"""
from collections import Counter

V = tuple(range(10))
e = (0,1)
f = (2,3)
H = [
    (1,4),(5,8),(2,6),(6,7),(1,5),(4,7),(4,9),(4,5),
    (3,6),(2,4),(0,8),(2,7),(8,9),(2,5),(1,8)
]
E = H + [e,f]


def is_forest(edges):
    parent={v:v for v in V}
    rank={v:0 for v in V}
    def find(x):
        while parent[x]!=x:
            parent[x]=parent[parent[x]]
            x=parent[x]
        return x
    def union(a,b):
        a,b=find(a),find(b)
        if a==b:
            return False
        if rank[a]<rank[b]:
            a,b=b,a
        parent[b]=a
        if rank[a]==rank[b]:rank[a]+=1
        return True
    return all(union(a,b) for a,b in edges)


def classify(A):
    eok=is_forest(A+[e])
    fok=is_forest(A+[f])
    efok=is_forest(A+[e,f])
    if not eok and not fok:return 'N0'
    if eok and not fok:return 'Ne'
    if fok and not eok:return 'Nf'
    if efok:return 'B'
    return 'R'

counts=Counter()
Rsets=[]
T=0
for mask in range(1<<len(H)):
    A=[H[i] for i in range(len(H)) if (mask>>i)&1]
    if not is_forest(A):
        continue
    T+=1
    c=classify(A)
    counts[c]+=1
    if c=='R':Rsets.append(tuple(A))

expected={'N0':1212,'Ne':2772,'Nf':2912,'B':6700,'R':4}
assert {k:counts[k] for k in expected}==expected
assert T==13600

N0,Ne,Nf,B,R=(counts[k] for k in ('N0','Ne','Nf','B','R'))
Z=N0+2*Ne+2*Nf+4*B+3*R
Ze=Ne+2*B+R
Zf=Nf+2*B+R
Zef=B
delta=Ze*Zf-Z*Zef
assert delta==1216
assert delta==Ne*Nf + R*(Ne+Nf+B+R) - B*N0

cov_num=N0*(B+R)-Ne*Nf
assert cov_num==T*R-delta==53184

# Direct full-graph enumeration, independent cross-check of Z,Ze,Zf,Zef.
Z2=Ze2=Zf2=Zef2=0
for mask in range(1<<len(E)):
    A=[E[i] for i in range(len(E)) if (mask>>i)&1]
    if not is_forest(A):continue
    Z2+=1
    se=(mask>>(len(E)-2))&1
    sf=(mask>>(len(E)-1))&1
    Ze2+=se; Zf2+=sf; Zef2+=se*sf
assert (Z2,Ze2,Zf2,Zef2)==(Z,Ze,Zf,Zef)
assert Ze2*Zf2-Z2*Zef2==1216

print('five-class counts',dict(counts))
print('T(H)=',T)
print('full counts Z,Ze,Zf,Zef=',Z,Ze,Zf,Zef)
print('Rayleigh gap Delta=',delta)
print('T^2 Cov(U,V)=',cov_num)
print('T*R=',T*R)
print('R probability=',f'{R}/{T}')
print('slack Delta/T^2=',f'{delta}/{T*T}')
print('number of R forests=',len(Rsets))
print('ALL EXACT CHECKS PASSED')
