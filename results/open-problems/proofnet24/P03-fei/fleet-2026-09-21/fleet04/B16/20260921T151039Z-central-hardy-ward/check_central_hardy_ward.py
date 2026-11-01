#!/usr/bin/env python3
"""Exact checks for P03-B16 central-band Hardy/Ward resolvent."""
from fractions import Fraction
from itertools import combinations
from math import factorial

def subsets(items):
    items=list(items)
    for r in range(len(items)+1):
        for s in combinations(items,r):
            yield frozenset(s)

def parity_game(relations,S):
    return sum((c for R,c in relations if len(R&S)%2), Fraction(0))

def delta(game,F,S):
    F=list(F)
    out=Fraction(0)
    for T in subsets(F):
        out += (-1)**(len(F)-len(T))*game(S|T)
    return out

def bern_expect_delta(relations,F,p):
    M=set().union(*(R for R,c in relations))
    rest=M-set(F)
    game=lambda S: parity_game(relations,S)
    out=Fraction(0)
    for S in subsets(rest):
        out += p**len(S)*(1-p)**(len(rest)-len(S))*delta(game,set(F),S)
    return out

def build_m(relations,v):
    p={}
    for R,c in relations:
        if v in R:
            d=len(R)-1
            p[d]=p.get(d,Fraction(0))+c
    return {d:a for d,a in p.items() if a}

def deriv(p):
    return {d-1:Fraction(d)*a for d,a in p.items() if d>0 and a}

def hardy(p):
    return {d:Fraction(d,d+1)*a for d,a in p.items() if d>0 and a}

def int_square(p,T=Fraction(1,2)):
    return sum((a*b*T**(d+e+1)/Fraction(d+e+1)
                for d,a in p.items() for e,b in p.items()), Fraction(0))

def int_weight_square(p,T=Fraction(1,2)):
    out=Fraction(0)
    for d,a in p.items():
        for e,b in p.items():
            k=d+e
            out += a*b*(T*T**(k+2)/Fraction(k+2)-T**(k+3)/Fraction(k+3))
    return out

def internal_face_bank(relations):
    M=sorted(set().union(*(R for R,c in relations)))
    total=Fraction(0); layers={}
    for k in range(2,len(M)+1):
        val=Fraction(0)
        for Ft in combinations(M,k):
            F=set(Ft); p={}
            for R,c in relations:
                if F<=R:
                    d=len(R)-k
                    p[d]=p.get(d,Fraction(0))+c
            p={d:a for d,a in p.items() if a}
            for d,a in p.items():
                for e,b in p.items():
                    A=d+e+k; B=k
                    beta=Fraction(factorial(A-1)*factorial(B-1),factorial(A+B-1))
                    val += Fraction(k)*a*b*beta
        if val:
            layers[k]=val; total += val
    return total,layers

families=[
 [(frozenset([0,1,2]),Fraction(2)),
  (frozenset([0,2,3]),Fraction(-1)),
  (frozenset([0,1,2,3,4]),Fraction(3,2))],
 [(frozenset([0]),Fraction(7,3)),
  (frozenset([0,1,2]),Fraction(-2)),
  (frozenset([1,2,3]),Fraction(5,4)),
  (frozenset([0,1,2,3,4]),Fraction(-3,5))],
 [(frozenset([0,1,2]),Fraction(1,8)),
  (frozenset([0,1,3]),Fraction(-1,8))],
]
plus=[(1,2,3),(1,4,5),(2,4,6),(3,5,6)]
minus=[(1,2,4),(1,3,5),(2,3,6),(4,5,6)]
pasch=[(frozenset(x),Fraction(1)) for x in plus]+[
      (frozenset(x),Fraction(-1)) for x in minus]
families.append(pasch)

cesaro=ward1=ward2=hardy_bounds=0
for rels in families:
    M=sorted(set().union(*(R for R,c in rels)))
    for v in M:
        m=build_m(rels,v); h=hardy(m); A=deriv(m)
        c={}
        for d,a in A.items():
            c[d+1]=c.get(d+1,Fraction(0))+a/Fraction(d+2)
        assert c==h
        cesaro += 1
        assert int_square(h) <= Fraction(1,2)*int_weight_square(A)
        hardy_bounds += 1
        for t in [Fraction(0),Fraction(1,4),Fraction(1,2),
                  Fraction(3,4),Fraction(1)]:
            p=(1-t)/2
            ep=bern_expect_delta(rels,{v},p)
            es=bern_expect_delta(rels,{v},1-p)
            mv=sum((a*t**d for d,a in m.items()),Fraction(0))
            assert mv == Fraction(1,2)*(ep+es)
            ward1 += 1
    for u,v in combinations(M,2):
        p2={}
        for R,c0 in rels:
            if {u,v}<=R:
                d=len(R)-2
                p2[d]=p2.get(d,Fraction(0))+c0
        p2={d:a for d,a in p2.items() if a}
        game=lambda S: Fraction(1,4)*parity_game(rels,S)
        rest=set(M)-{u,v}
        def expd(prob):
            out=Fraction(0)
            for S in subsets(rest):
                out += prob**len(S)*(1-prob)**(len(rest)-len(S))*delta(game,{u,v},S)
            return out
        for t in [Fraction(0),Fraction(1,4),Fraction(1,2),
                  Fraction(3,4),Fraction(1)]:
            p=(1-t)/2
            lhs=sum((a*t**d for d,a in p2.items()),Fraction(0))
            rhs=(-expd(p))-(-expd(1-p))
            assert lhs==rhs
            ward2 += 1

assert all(build_m(pasch,v)=={} for v in set().union(*(R for R,c in pasch)))
pasch_int,layers=internal_face_bank(pasch)
scaled,_=internal_face_bank([(R,c/Fraction(8)) for R,c in pasch])
assert pasch_int==Fraction(4,5) and layers=={3:Fraction(4,5)}
assert scaled==Fraction(1,80)

print({
 "status":"PASS",
 "cesaro_hardy_identities":cesaro,
 "ward_k1_checks":ward1,
 "ward_k2_checks":ward2,
 "hardy_weighted_bounds":hardy_bounds,
 "pasch_radial_bank":"0",
 "pasch_internal_bank":"4/5",
 "pasch_scaled_internal_bank":"1/80"
})
