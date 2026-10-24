#!/usr/bin/env python3
"""B17 FEI stress tests for point-process, sensitivity, and antichain-spectrum lemmas."""
from fractions import Fraction
from collections import Counter
from math import log2
import itertools

def fwht_int(vals):
    y=list(map(int,vals))
    h=1
    while h<len(y):
        for i in range(0,len(y),2*h):
            for j in range(i,i+h):
                u,v=y[j],y[j+h]
                y[j],y[j+h]=u+v,u-v
        h*=2
    return y

def vals_from_mask(n,mask):
    return [1 if (mask>>x)&1 else -1 for x in range(1<<n)]

def spectral(n,vals):
    N=1<<n
    w=fwht_int(vals)
    return {S:Fraction(w[S]*w[S],N*N) for S in range(N) if w[S]}

def sensitivity_law(n,vals):
    N=1<<n
    c=Counter()
    for x in range(N):
        sm=0
        for i in range(n):
            if vals[x] != vals[x^(1<<i)]:
                sm |= 1<<i
        c[sm]+=1
    return {S:Fraction(v,N) for S,v in c.items()}

def entropy(law):
    return -sum(float(p)*log2(float(p)) for p in law.values())

def influence(law):
    return sum(S.bit_count()*float(p) for S,p in law.items())

def inclusion(law,T):
    return sum(p for S,p in law.items() if S&T==T)

def antichain(supp):
    L=list(supp)
    for a,b in itertools.combinations(L,2):
        if (a & b)==a or (a & b)==b:
            return False
    return True

def fmt(S,n):
    return format(S,f"0{n}b")

# A. The 3-bit one-point defect is an actual Boolean spectral process
# with positive pair covariance, so universal negative association is false.
n=3
vals=vals_from_mask(n,1)
p=spectral(n,vals)
assert p[0]==Fraction(9,16)
assert all(p[S]==Fraction(1,16) for S in range(1,8))
pi=inclusion(p,1<<0); pj=inclusion(p,1<<1); pij=inclusion(p,(1<<0)|(1<<1))
cov=pij-pi*pj
assert (pi,pj,pij,cov)==(Fraction(1,4),Fraction(1,4),Fraction(1,8),Fraction(1,16))
print("ONE_POINT_3", "p_i",pi,"p_j",pj,"p_ij",pij,"cov",cov)

# B. Exact 6-bit homogeneous degree-3 Boolean example.
n=6
mask=int("e22755acca551bb8",16)
vals=vals_from_mask(n,mask)
p=spectral(n,vals)
q=sensitivity_law(n,vals)
assert sum(p.values())==1 and sum(q.values())==1
assert {S.bit_count() for S in p}=={3}
assert {S.bit_count() for S in q}=={3}
for r in (1,2):
    for Tt in itertools.combinations(range(n),r):
        T=sum(1<<i for i in Tt)
        assert inclusion(p,T)==inclusion(q,T)
tv=sum(abs(p.get(S,0)-q.get(S,0)) for S in set(p)|set(q))/2
assert tv==Fraction(1,4)
assert len(p)==13 and len(q)==14
assert p[int("011001",2)]==Fraction(1,4)
assert q[int("011001",2)]==Fraction(3,16)
assert int("100110",2) not in p and q[int("100110",2)]==Fraction(1,16)
print("HOMOGENEOUS_6_3", "mask",hex(mask),"support_spec",len(p),"support_sens",len(q),
      "TV",tv,"Hspec",f"{entropy(p):.12f}","Hsens",f"{entropy(q):.12f}")
for i,j in ((0,5),(1,4),(2,3)):
    pi=inclusion(p,1<<i); pj=inclusion(p,1<<j); pij=inclusion(p,(1<<i)|(1<<j))
    print("PAIR",i,j,"p_i",pi,"p_j",pj,"p_ij",pij,"cov",pij-pi*pj)

# C. Homogeneous degree 3 granularity in the exact example.
w=fwht_int(vals); N=1<<n
nonzero=[Fraction(abs(w[S]),N) for S in range(N) if w[S]]
mesh=Fraction(1,4) # 2^(1-k), k=3
assert all(c/mesh == int(c/mesh) for c in nonzero)
assert entropy(p) <= 2*(3-1)+1e-12
print("GRANULARITY", "min_abs_coeff",min(nonzero),"homogeneous_entropy_bound",4,
      "actual_H",f"{entropy(p):.12f}","I",f"{influence(p):.12f}")

# D. Exhaustive n<=4 stress test for the antichain-spectrum theorem.
# This is not a FEI audit; it checks only the new exact lemma on its natural class.
for n in range(1,5):
    N=1<<n
    count=0
    maxratio=0.0
    maximizer=0
    for mask in range(1<<N):
        vals=vals_from_mask(n,mask)
        p=spectral(n,vals)
        if not antichain(p.keys()):
            continue
        count+=1
        H=entropy(p); I=influence(p)
        ratio=H/I if I else 0.0
        assert H <= 2*I + 1e-12
        if ratio>maxratio+1e-12:
            maxratio=ratio; maximizer=mask
    print("ANTICHAIN_ENUM", "n",n,"count",count,"max_H_over_I",f"{maxratio:.12f}",
          "maximizer",hex(maximizer))

print("SPECTRAL_6_3")
for S in sorted(p): # note p currently overwritten by last enumeration; recompute
    pass
p=spectral(6,vals_from_mask(6,int("e22755acca551bb8",16)))
q=sensitivity_law(6,vals_from_mask(6,int("e22755acca551bb8",16)))
for S in sorted(p):
    print(fmt(S,6),p[S])
print("SENSITIVITY_6_3")
for S in sorted(q):
    print(fmt(S,6),q[S])
