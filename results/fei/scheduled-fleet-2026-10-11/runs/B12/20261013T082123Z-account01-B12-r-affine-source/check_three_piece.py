#!/usr/bin/env python3
"""Exact Walsh audit for the three-affine-piece composition theorem."""
from fractions import Fraction
import math

def fwht(vals):
    a=list(map(Fraction,vals)); h=1
    while h<len(a):
        for s in range(0,len(a),2*h):
            for j in range(s,s+h):
                x,y=a[j],a[j+h]; a[j],a[j+h]=x+y,x-y
        h*=2
    return tuple(x/len(a) for x in a)

def entropy(h): return sum(float(c*c)*math.log(1/float(c*c)) for c in h if c)
def influence(h): return sum(i.bit_count()*c*c for i,c in enumerate(h))

def subspaces(n):
    spaces={1}
    for x in range(1,1<<n):
        for mask in list(spaces):
            if not(mask>>x&1):
                elems=[i for i in range(1<<n) if mask>>i&1]; new=mask
                for v in elems: new|=1<<(v^x)
                spaces.add(new)
    return spaces

def cosets(n):
    ans=set(); full=(1<<(1<<n))-1
    for V in subspaces(n):
        unseen=full
        while unseen:
            x=(unseen&-unseen).bit_length()-1; C=0
            for v in range(1<<n):
                if V>>v&1: C|=1<<(x^v)
            ans.add(C); unseen&=~C
    return sorted(ans,key=lambda C:(C.bit_count(),C))

def compose(mask,n):
    N=1<<n; s=tuple((mask>>i)&1 for i in range(N)); a=[];d=[];F=[]
    for selector in (0,1):
        chi=1 if selector==0 else -1
        for z in s:
            defect=selector*z
            d.append(defect); a.append(chi*(1-defect)); F.append(a[-1]+defect)
    return fwht(s),fwht(a),fwht(d),fwht(F)

C3=24*math.log(3)+4/math.e
total=0; unique_total=0; best=(-1,None); sharp8_viol=0
for n in range(2,5):
    N=1<<n; cs=cosets(n); unions={}; row=0
    for i,A in enumerate(cs):
        for j in range(i+1,len(cs)):
            B=cs[j]
            if A&B: continue
            for C in cs[j+1:]:
                if (A|B)&C: continue
                total+=1; row+=1; U=A|B|C
                ps=[Fraction(X.bit_count(),N) for X in (A,B,C)]
                K=sum(p*int(math.log2(1/float(p))) for p in ps)
                old=unions.get(U)
                if old is None or K>old: unions[U]=K
    unique_total+=len(unions)
    for U,K in unions.items():
        hs,ha,hd,hF=compose(U,n); p=Fraction(U.bit_count(),N)
        Is=influence(hs); Id=influence(hd)
        assert Id==Is/2+p/4
        assert float(K)<=2*float(Is)+float(p)*math.log2(3)+1e-12
        omega=entropy(hF)-entropy(ha)-entropy(hd)
        assert omega<=C3*float(Id)+1e-11
        if omega>8*math.log(2)*float(Id)+1e-11: sharp8_viol+=1
        ratio=omega/float(Id) if Id else -1e100
        if ratio>best[0]: best=(ratio,(n,U,omega,float(Id),float(Is),float(p),float(K)))
    print(f"m={n} triple_decompositions={row} unique_unions={len(unions)} PASS")

def phi(t): return 0.0 if t==0 else t*math.log(1/t)
grid=0
for j in range(1,1000000):
    u=Fraction(j,1000000); cap=min(3*float(u),1.0)
    z=1/math.e if cap>=1/math.e else cap
    assert phi(z)<=3*phi(float(u))+float(u)/math.e+1e-12
    grid+=1

print(f"total_triple_decompositions={total}")
print(f"total_unique_unions_by_dimension={unique_total}")
print(f"best_ratio={best[0]:.15f}")
print(f"best_instance={best[1]}")
print(f"proved_constant_C3={C3:.15f}")
print(f"stronger_8ln2_finite_violations={sharp8_viol}")
print(f"scalar_grid_points={grid}")
print("RESULT=PASS")
