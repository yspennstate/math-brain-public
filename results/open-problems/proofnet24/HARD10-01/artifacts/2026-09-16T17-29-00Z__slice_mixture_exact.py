#!/usr/bin/env python3
"""Exact self-check for HARD10-01 single-edge interpolation identities.

Finite validation artifact only; not a general proof of Grimmett-Winkler.
It recomputes the B1 one-edge-field example, checks the exact two-slice
interpolation algebra with Fractions, and checks every third-edge direction
of the archived ten-vertex B15 near-miss for the fixed distinguished pair.
"""
from fractions import Fraction
from collections import Counter

class DSU:
    __slots__=("p","r")
    def __init__(self,n):
        self.p=list(range(n)); self.r=[0]*n
    def find(self,x):
        p=self.p
        while p[x]!=x:
            p[x]=p[p[x]]
            x=p[x]
        return x
    def union(self,a,b):
        a=self.find(a); b=self.find(b)
        if a==b: return False
        r=self.r
        if r[a]<r[b]: a,b=b,a
        self.p[b]=a
        if r[a]==r[b]: r[a]+=1
        return True

def forest_masks(n, edges):
    out=[]
    for mask in range(1<<len(edges)):
        d=DSU(n); ok=True
        mm=mask; i=0
        while mm:
            if mm&1:
                if not d.union(*edges[i]):
                    ok=False; break
            mm >>= 1; i += 1
        if ok: out.append(mask)
    return out

def split_counts(masks, ie, jf, ig):
    # g-slice -> Z, Ze, Zf, Zef
    c=[[0,0,0,0] for _ in range(2)]
    for mask in masks:
        s=(mask>>ig)&1
        be=(mask>>ie)&1
        bf=(mask>>jf)&1
        c[s][0]+=1
        c[s][1]+=be
        c[s][2]+=bf
        c[s][3]+=int(be and bf)
    return c

def quadratic(c):
    A,Ae,Af,Aef=c[0]
    B,Be,Bf,Bef=c[1]
    q0=Ae*Af-A*Aef
    q1=Ae*Bf+Be*Af-A*Bef-B*Aef
    q2=Be*Bf-B*Bef
    return q0,q1,q2

def slice_parameters(c):
    A,Ae,Af,Aef=c[0]
    B,Be,Bf,Bef=c[1]
    assert A>0 and B>0
    a=Fraction(Ae*Af-A*Aef, A*A)
    b=Fraction(Be*Bf-B*Bef, B*B)
    u=Fraction(Ae,A)-Fraction(Be,B)
    v=Fraction(Af,A)-Fraction(Bf,B)
    q=quadratic(c)
    assert q[0] == A*A*a
    assert q[1] == A*B*(a+b-u*v)
    assert q[2] == B*B*b
    return a,b,u,v

def all_positive_axis(q):
    q0,q1,q2=q
    if q0 < 0 or q2 < 0: return False
    if q2 == 0: return q1 >= 0
    if q1 >= 0: return True
    return q1*q1 <= 4*q0*q2

# B1 example from the preceding method run.
E1=[(0,1),(0,3),(0,4),(1,2),(1,4),(2,3),(2,4),(3,4)]
E1=[tuple(sorted(x)) for x in E1]
ie=E1.index((0,1)); jf=E1.index((3,4)); ig=E1.index((0,4))
M1=forest_masks(5,E1)
c1=split_counts(M1,ie,jf,ig)
q1=quadratic(c1)
assert c1 == [[86,38,34,14],[48,14,14,4]]
assert q1 == (88,-8,4)
a,b,u,v=slice_parameters(c1)
assert u*v-a-b == Fraction(1,516)
assert (u*v-a-b)**2 <= 4*a*b
assert all_positive_axis(q1)
print("B1_EXACT PASS")
print("B1 slices absent/present =",c1)
print("B1 q(t)=88-8t+4t^2; minimum at t=1 equals 84")
print("B1 mixture a,b,u,v =",a,b,u,v)
print("B1 uv-a-b =",u*v-a-b," 4ab =",4*a*b)

# B15 archived ten-vertex near-miss.
H=[(0,5),(0,8),(1,5),(1,8),(2,5),(2,6),(2,7),(3,6),
   (4,5),(4,7),(4,9),(5,6),(5,7),(5,8),(5,9),(6,7),(8,9)]
e=(0,1); f=(2,3)
E2=[tuple(sorted(x)) for x in H+[e,f]]
ie=E2.index(e); jf=E2.index(f)
M2=forest_masks(10,E2)
assert len(M2)==90880
polys=[]
for ig,g in enumerate(E2):
    if ig in (ie,jf): continue
    c=split_counts(M2,ie,jf,ig)
    q=quadratic(c)
    slice_parameters(c)
    assert sum(q)==576
    assert all_positive_axis(q)
    polys.append((g,q))
hist=Counter(q for _,q in polys)
assert hist==Counter({(384,0,192):8,(576,0,0):5,(0,288,288):4})
print("B15_EXACT PASS")
print("B15 forests =",len(M2)," third_edges =",len(polys))
print("B15 one-field polynomial histogram =",sorted(hist.items()))
print("B15 every third-edge q(1)=576 and every q(t)>=0 for all t>0")
print("B15 no q1<0 third-edge direction; this near-miss is not an external-field near-miss")
print("ALL_EXACT_SELF_CHECKS_PASS")
