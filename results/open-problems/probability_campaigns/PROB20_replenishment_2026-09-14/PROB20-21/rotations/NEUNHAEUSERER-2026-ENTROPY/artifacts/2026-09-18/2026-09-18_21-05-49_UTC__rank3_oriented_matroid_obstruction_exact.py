#!/usr/bin/env python3
from itertools import product, combinations
from fractions import Fraction as F
M=6
RELS=[]
for v in product((-1,0,1), repeat=M):
    if 1 not in v or -1 not in v:
        continue
    if next(x for x in v if x)<0:
        v=tuple(-x for x in v)
    if v not in RELS:
        RELS.append(v)
assert len(RELS)==301
def active(w):
    return [r for r in RELS if sum(a*b for a,b in zip(r,w))==0]
def rank(rows):
    if not rows: return 0
    A=[[F(x) for x in row] for row in rows]
    m=len(A); r=0
    for c in range(M):
        piv=next((i for i in range(r,m) if A[i][c]),None)
        if piv is None: continue
        A[r],A[piv]=A[piv],A[r]
        q=A[r][c]; A[r]=[x/q for x in A[r]]
        for i in range(m):
            if i!=r and A[i][c]:
                q=A[i][c]
                A[i]=[A[i][j]-q*A[r][j] for j in range(M)]
        r+=1
        if r==m: break
    return r
def basis3(rows):
    B=[]
    for x in rows:
        if rank(B+[x])>len(B):
            B.append(x)
            if len(B)==3: return B
    raise AssertionError('rank < 3')
def det3(B,I):
    m=[[B[r][j] for j in I] for r in range(3)]
    return (m[0][0]*(m[1][1]*m[2][2]-m[1][2]*m[2][1])
            -m[0][1]*(m[1][0]*m[2][2]-m[1][2]*m[2][0])
            +m[0][2]*(m[1][0]*m[2][1]-m[1][1]*m[2][0]))
def chirotope(B):
    z=[]
    for I in combinations(range(M),3):
        d=det3(B,I)
        z.append(0 if d==0 else (1 if d>0 else -1))
    first=next(x for x in z if x)
    if first<0: z=[-x for x in z]
    return tuple(z)
def collision_signature(w):
    cls={}
    for mask in range(1<<M):
        s=sum(w[i] for i in range(M) if (mask>>i)&1)
        c=cls.setdefault(s,[0]*(M+1))
        c[mask.bit_count()]+=1
    return tuple(sorted(tuple(c) for c in cls.values()))
A=(1,1,2,53,66,67)
B=(1,1,1,18,81,84)
actA,actB=active(A),active(B)
assert rank(actA)==rank(actB)==3
assert len(actA)==6 and len(actB)==4
chiA=chirotope(basis3(actA)); chiB=chirotope(basis3(actB))
assert chiA==chiB
sigA=collision_signature(A); sigB=collision_signature(B)
assert sigA!=sigB
assert len(sigA)==32 and len(sigB)==30
print('PASS')
print('weights_A',A,'active_relations',len(actA),'rank',rank(actA),'support',len(sigA))
print('weights_B',B,'active_relations',len(actB),'rank',rank(actB),'support',len(sigB))
print('same_labeled_rank3_chirotope',chiA==chiB)
print('different_entropy_signatures',sigA!=sigB)
print('chirotope',chiA)
