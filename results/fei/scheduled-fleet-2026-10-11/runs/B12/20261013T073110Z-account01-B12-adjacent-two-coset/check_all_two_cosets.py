#!/usr/bin/env python3
"""Exact Walsh/rank audit for the unrestricted two-affine-coset theorem."""
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

def entropy(h):
    return sum(float(c*c)*math.log(1/float(c*c)) for c in h if c)

def influence(h):
    return sum(i.bit_count()*c*c for i,c in enumerate(h))

def subspaces(n):
    spaces={frozenset({0})}
    for x in range(1,1<<n):
        for V in list(spaces):
            if x not in V: spaces.add(frozenset(V|{v^x for v in V}))
    return spaces

def cosets(n):
    ans=set()
    for V in subspaces(n):
        unseen=set(range(1<<n))
        while unseen:
            x=min(unseen); C=frozenset(x^v for v in V)
            unseen-=C; ans.add(C)
    return sorted(ans,key=lambda C:(len(C),tuple(C)))

def compose(s):
    a=[];d=[];F=[]
    for selector in (0,1):
        chi=1 if selector==0 else -1
        for z in s:
            defect=selector*z
            d.append(defect); a.append(chi*(1-defect)); F.append(a[-1]+defect)
    return fwht(a),fwht(d),fwht(F)

total=adjacent=nonaffine=positive=0
best=(-1,None)
for n in range(1,5):
    cs=cosets(n); cset=set(cs); N=1<<n
    row=[0,0,0,0]
    for i,A in enumerate(cs):
        for B in cs[i+1:]:
            if not A.isdisjoint(B): continue
            total+=1; row[0]+=1
            edge=sum(1 for x in A for j in range(n) if (x^(1<<j)) in B)
            adjacent += edge>0; row[1]+=edge>0
            U=A|B
            nonaffine += U not in cset; row[2]+=U not in cset
            s=tuple(int(x in U) for x in range(N))
            hs=fwht(s); p=Fraction(len(U),N)
            ha,hd,hF=compose(s)
            assert influence(hd)==influence(hs)/2+p/4
            omega=entropy(hF)-entropy(ha)-entropy(hd)
            assert omega <= 8*math.log(2)*float(influence(hd))+1e-11
            positive += omega>1e-12; row[3]+=omega>1e-12
            ratio=omega/float(influence(hd)) if influence(hd) else -1e100
            if U not in cset and ratio>best[0]:
                best=(ratio,(n,tuple(sorted(A)),tuple(sorted(B)),omega,float(influence(hd)),edge))
    print(f"m={n} disjoint_pairs={row[0]} adjacent={row[1]} nonaffine={row[2]} positive={row[3]} PASS")

scalar=0
for a in range(80):
  for b in range(a,80):
    for q in range(1,161):
      lhs=2*q
      rhs=(2**b)*(1+max(0,q-1-a))+(2**a)*(1+max(0,q-1-b))
      assert lhs<=rhs
      scalar+=1

print(f"total_disjoint_pairs={total}")
print(f"adjacent_pairs={adjacent}")
print(f"nonaffine_pairs={nonaffine}")
print(f"positive_associator_pairs={positive}")
print(f"best_nonaffine_ratio={best[0]:.15f}")
print(f"best_nonaffine_instance={best[1]}")
print(f"theorem_constant_8ln2={8*math.log(2):.15f}")
print(f"scalar_rank_tuples={scalar}")
print("RESULT=PASS")
