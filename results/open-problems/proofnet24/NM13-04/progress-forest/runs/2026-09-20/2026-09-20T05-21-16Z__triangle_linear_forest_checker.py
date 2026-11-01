#!/usr/bin/env python3
from fractions import Fraction
from itertools import combinations
from math import comb

STATES=[
    ((0,),(1,),(2,)),
    ((0,),(1,2)),
    ((0,1),(2,)),
    ((0,2),(1,)),
    ((0,1,2),),
]
def canon(p):
    return tuple(sorted((tuple(sorted(b)) for b in p), key=lambda z:z[0]))
SID={canon(s):i for i,s in enumerate(STATES)}

class DSU:
    def __init__(self,n): self.p=list(range(n))
    def find(self,x):
        while self.p[x]!=x:
            self.p[x]=self.p[self.p[x]]
            x=self.p[x]
        return x
    def union(self,a,b):
        a,b=self.find(a),self.find(b)
        if a==b: return False
        self.p[b]=a
        return True

def layer_edges(kind):
    if kind=="K1":
        nr,internal=1,[]
    elif kind=="K2":
        nr,internal=2,[(3,4)]
    elif kind=="P3":
        nr,internal=3,[(3,4),(4,5)]
    else:
        raise ValueError(kind)
    return nr, internal+[(t,v) for v in range(3,3+nr) for t in range(3)]

def all_marked_transfers(kind):
    nr,E=layer_edges(kind)
    m=len(E)
    pairs=list(combinations(range(m),2))
    pidx={p:i for i,p in enumerate(pairs)}
    stores=[[[0]*5 for _ in range(5)] for __ in range(1+m+len(pairs))]
    for si,s in enumerate(STATES):
        for mask in range(1<<m):
            d=DSU(3+nr)
            for block in s:
                for x in block[1:]:
                    d.union(block[0],x)
            inc=[]
            ok=True
            for i,(a,b) in enumerate(E):
                if (mask>>i)&1:
                    if not d.union(a,b):
                        ok=False
                        break
                    inc.append(i)
            if not ok:
                continue
            groups={}
            for t in range(3):
                groups.setdefault(d.find(t),[]).append(t)
            sj=SID[canon(groups.values())]
            stores[0][si][sj]+=1
            for i in inc:
                stores[1+i][si][sj]+=1
            for a,b in combinations(inc,2):
                stores[1+m+pidx[(a,b)]][si][sj]+=1
    M0=stores[0]
    M1=stores[1:1+m]
    M2={p:stores[1+m+i] for p,i in pidx.items()}
    return M0,M1,M2,E

def triangle_vector(required=()):
    E=[(0,1),(0,2),(1,2)]
    v=[0]*5
    required=set(required)
    for mask in range(8):
        if any(((mask>>i)&1)==0 for i in required):
            continue
        d=DSU(3)
        ok=True
        for i,(a,b) in enumerate(E):
            if (mask>>i)&1 and not d.union(a,b):
                ok=False
                break
        if not ok:
            continue
        groups={}
        for t in range(3):
            groups.setdefault(d.find(t),[]).append(t)
        v[SID[canon(groups.values())]]+=1
    return v

def mm(A,B):
    return [[sum(Fraction(A[i][k])*Fraction(B[k][j]) for k in range(5))
             for j in range(5)] for i in range(5)]
def vm(v,M):
    return [sum(Fraction(v[k])*Fraction(M[k][j]) for k in range(5))
            for j in range(5)]
def mpow(M,n):
    R=[[Fraction(i==j) for j in range(5)] for i in range(5)]
    B=[[Fraction(x) for x in row] for row in M]
    while n:
        if n&1: R=mm(R,B)
        B=mm(B,B)
        n//=2
    return R

SPECIES=["P3","K2","K1"]
LEAD={"P3":130,"K2":23,"K1":4}
M={}; M1={}; M2={}; E={}
for s in SPECIES:
    M[s],M1[s],M2[s],E[s]=all_marked_transfers(s)

assert M["P3"]==[
 [130,103,103,103,273],
 [0,130,0,0,206],
 [0,0,130,0,206],
 [0,0,0,130,206],
 [0,0,0,0,130]]
assert M["K2"]==[
 [23,12,12,12,22],
 [0,23,0,0,24],
 [0,0,23,0,24],
 [0,0,0,23,24],
 [0,0,0,0,23]]
assert M["K1"]==[
 [4,1,1,1,1],
 [0,4,0,0,2],
 [0,0,4,0,2],
 [0,0,0,4,2],
 [0,0,0,0,4]]

NORM={s:[[Fraction(x,LEAD[s]) for x in row] for row in M[s]]
      for s in SPECIES}
POW={s:[mpow(NORM[s],i) for i in range(5)] for s in SPECIES}
H={}
for x in range(5):
    for y in range(5):
        for z in range(5):
            U=mm(mm(POW["P3"][x],POW["K2"][y]),POW["K1"][z])
            H[(x,y,z)]=[sum(U[i][j] for j in range(5)) for i in range(5)]

TV={}
for req in [(),(0,),(1,),(2,),(0,1),(0,2),(1,2)]:
    TV[tuple(sorted(req))]=[Fraction(x) for x in triangle_vector(req)]
assert TV[()]==[Fraction(1),Fraction(1),Fraction(1),Fraction(1),Fraction(3)]

# Two copies of each layer species form a universal local witness:
# any edge pair uses at most two right components.
RECS=[("T",None,0,i) for i in range(3)]
for s in SPECIES:
    for copy in (0,1):
        RECS += [("B",s,copy,i) for i in range(len(E[s]))]

def getM(s,req):
    req=tuple(sorted(req))
    X=M[s] if not req else M1[s][req[0]] if len(req)==1 else M2[s][req]
    return [[Fraction(x) for x in row] for row in X]

def distinguished_vector(e,f,mask):
    tr=[]
    for rec,on in ((e,mask[0]),(f,mask[1])):
        if on and rec[0]=="T":
            tr.append(rec[3])
    v=TV[tuple(sorted(tr))]
    blocks={(rec[1],rec[2]) for rec in (e,f) if rec[0]=="B"}
    for block in sorted(blocks,key=lambda q:(SPECIES.index(q[0]),q[1])):
        req=[]
        for rec,on in ((e,mask[0]),(f,mask[1])):
            if on and rec[0]=="B" and (rec[1],rec[2])==block:
                req.append(rec[3])
        v=vm(v,getM(block[0],req))
    return v

def forward_difference(vals,i,j,k):
    ans=Fraction(0)
    for a in range(i+1):
        for b in range(j+1):
            for c in range(k+1):
                ans += ((-1)**((i-a)+(j-b)+(k-c))
                        *comb(i,a)*comb(j,b)*comb(k,c)*vals[(a,b,c)])
    return ans

neg=0
nonzero=0
zero=0
min_positive=None
min_constant=None
for e,f in combinations(RECS,2):
    B=[distinguished_vector(e,f,m) for m in ((0,0),(1,0),(0,1),(1,1))]
    vals={}
    for xyz,h in H.items():
        Z=[sum(v[i]*h[i] for i in range(5)) for v in B]
        vals[xyz]=Z[1]*Z[2]-Z[0]*Z[3]
    c0=vals[(0,0,0)]
    assert c0>0
    min_constant=c0 if min_constant is None else min(min_constant,c0)
    for i in range(5):
        for j in range(5-i):
            for k in range(5-i-j):
                c=forward_difference(vals,i,j,k)
                if c<0:
                    neg+=1
                elif c==0:
                    zero+=1
                else:
                    nonzero+=1
                    min_positive=c if min_positive is None else min(min_positive,c)

assert neg==0
assert min_constant==2
assert min_positive==Fraction(1,8)
assert len(RECS)==45
assert len(list(combinations(RECS,2)))==990
assert nonzero+zero==990*35

def build_graph(p,m,r):
    edges=[(0,1),(0,2),(1,2)]
    v=3
    for _ in range(p):
        q=[v,v+1,v+2]; v+=3
        edges += [(q[0],q[1]),(q[1],q[2])]
        edges += [(t,u) for u in q for t in range(3)]
    for _ in range(m):
        q=[v,v+1]; v+=2
        edges += [(q[0],q[1])]
        edges += [(t,u) for u in q for t in range(3)]
    for _ in range(r):
        u=v; v+=1
        edges += [(t,u) for t in range(3)]
    return v,edges

def brute(p,m,r):
    n,edges=build_graph(p,m,r)
    mE=len(edges)
    Z=0
    one=[0]*mE
    two=[[0]*mE for _ in range(mE)]
    for mask in range(1<<mE):
        d=DSU(n)
        inc=[]
        ok=True
        for i,(a,b) in enumerate(edges):
            if (mask>>i)&1:
                if not d.union(a,b):
                    ok=False
                    break
                inc.append(i)
        if not ok:
            continue
        Z+=1
        for i in inc:
            one[i]+=1
        for i,j in combinations(inc,2):
            two[i][j]+=1
    mind=None
    for i,j in combinations(range(mE),2):
        gap=one[i]*one[j]-Z*two[i][j]
        mind=gap if mind is None else min(mind,gap)
    assert mind>0
    return n,mE,Z,mind

small=[(prm,brute(*prm)) for prm in [(1,0,0),(0,1,1),(1,0,1)]]

print("T07 TRIANGLE + RIGHT LINEAR FOREST (components K1/K2/P3)")
print("unmarked P3 =",M["P3"])
print("unmarked K2 =",M["K2"])
print("unmarked K1 =",M["K1"])
print("triangle vector =",[int(x) for x in TV[()]])
print("universal witness edges =",len(RECS))
print("witness edge pairs =",len(list(combinations(RECS,2))))
print("Newton coefficients checked =",nonzero+zero)
print("positive coefficients =",nonzero)
print("zero coefficients =",zero)
print("negative coefficients =",neg)
print("minimum positive Newton coefficient =",min_positive)
print("minimum constant Rayleigh coefficient =",min_constant)
for prm,res in small:
    print("bruteforce",prm,"-> n,m,Z,minDelta =",res)
print("ALL_EXACT_CHECKS_PASS")
