#!/usr/bin/env python3
"""Exact falsification/checker for B16 common-order first-hit Ward covariance.

All arithmetic in the combinatorial tests is fractions.Fraction.
The universal statements are proved algebraically in REPORT.md; this script
checks finite instances and the two explicit admissible one-point Boolean
examples used there.
"""
from fractions import Fraction
from itertools import combinations, permutations
from math import factorial
import json

def first(R, perm):
    pos = {v:i for i,v in enumerate(perm)}
    return min(R, key=pos.__getitem__)

def cov_formula(R,S):
    R=set(R); S=set(S)
    h=len(R&S)
    if h==0:
        return Fraction(0)
    return Fraction(h, len(R|S)) - Fraction(h, len(R)*len(S))

def cov_syndrome_formula(R,S):
    R=set(R); S=set(S)
    qR,qS,qX=len(R),len(S),len(R^S)
    num=qR+qS-qX
    J=Fraction(num, qR+qS+qX)
    G=Fraction(num, 2*qR*qS)
    return J-G

def cov_bruteforce(R,S,m):
    R=set(R); S=set(S)
    uR=[Fraction(int(i in R),len(R)) for i in range(m)]
    uS=[Fraction(int(i in S),len(S)) for i in range(m)]
    tot=Fraction(0)
    for p in permutations(range(m)):
        jr,js=first(R,p),first(S,p)
        xr=[Fraction(int(i==jr))-uR[i] for i in range(m)]
        xs=[Fraction(int(i==js))-uS[i] for i in range(m)]
        tot += sum(a*b for a,b in zip(xr,xs))
    return tot/Fraction(factorial(m))

def aggregate_formula(relations, coeffs):
    out=Fraction(0)
    for i,(R,c) in enumerate(zip(relations,coeffs)):
        out += Fraction(c*c)*(1-Fraction(1,len(R)))
        for j in range(i):
            out += 2*c*coeffs[j]*cov_formula(R,relations[j])
    return out

def aggregate_bruteforce(relations, coeffs, m):
    means=[]
    for R,c in zip(relations,coeffs):
        u=[Fraction(c*int(i in R),len(R)) for i in range(m)]
        means.append(u)
    tot=Fraction(0)
    for p in permutations(range(m)):
        z=[Fraction(0) for _ in range(m)]
        for R,c,u in zip(relations,coeffs,means):
            j=first(R,p)
            for i in range(m):
                z[i] += c*int(i==j)-u[i]
        tot += sum(x*x for x in z)
    return tot/Fraction(factorial(m))

def qflip_basis(n):
    vs=[v for v in range(1,1<<n) if v.bit_count()>=2]
    B={}
    for v in vs:
        pivot=v & -v
        B[v]={0,pivot,v,v^pivot}
    return vs,B

def relation_from_coords(coords,B):
    A=set()
    for v in coords:
        A ^= B[v]
    return A

def r32_sign(A):
    assert len(A)%2==0
    return 1 if (len(A)//2)%2==0 else -1

pair_checks=0
for m in range(1,6):
    odds=[set(c) for k in range(1,m+1,2) for c in combinations(range(m),k)]
    for R in odds:
        for S in odds:
            brute=cov_bruteforce(R,S,m)
            f1=cov_formula(R,S)
            f2=cov_syndrome_formula(R,S)
            assert brute==f1==f2, (m,R,S,brute,f1,f2)
            h=len(R&S)
            if h:
                qR,qS,qX=len(R),len(S),len(R^S)
                J=Fraction(2*h, qR+qS+qX)
                assert J == Fraction(h,len(R|S))
            pair_checks += 1

R1={0,1,2}; R2={0,1,3}
same=aggregate_formula([R1,R2],[1,1])
opp=aggregate_formula([R1,R2],[1,-1])
assert same==Fraction(17,9)
assert opp==Fraction(7,9)
assert aggregate_bruteforce([R1,R2],[1,1],4)==same
assert aggregate_bruteforce([R1,R2],[1,-1],4)==opp
diag=Fraction(4,3)

# Genuine one-point Boolean phases: f(0)=-1 and f(x)=+1 otherwise.
# Every anchored q-flip basis word contains 0, hence every z_v=-1.
vs3,B3=qflip_basis(3)
assert vs3 == [3,5,6,7]
for v in vs3:
    assert 0 in B3[v]
A3=relation_from_coords((3,5,6),B3)
B3rel=relation_from_coords((3,5,7),B3)
assert len(A3)==4 and len(B3rel)==8
assert r32_sign(A3)==r32_sign(B3rel)==1
assert len({3,5,6}&{3,5,7})==2
assert same==Fraction(17,9) and diag==Fraction(4,3)

vs4,B4=qflip_basis(4)
for v in vs4:
    assert 0 in B4[v]
A4=relation_from_coords((3,5,6),B4)
B4rel=relation_from_coords((3,5,10),B4)
assert len(A4)==4 and len(B4rel)==6
assert r32_sign(A4)==1 and r32_sign(B4rel)==-1
assert len({3,5,6}&{3,5,10})==2
scale=Fraction(1,8)
q4=opp*scale*scale
diag4=diag*scale*scale
assert q4==Fraction(7,576)
assert diag4==Fraction(1,48)

out={
    "status":"PASS",
    "exact_pair_covariance_cases":pair_checks,
    "max_ground_set_exhaustive":5,
    "common_order_same_sign_overlap_example":{
        "supports":["012","013"],
        "kernel":"5/18",
        "aggregate_fluctuation_energy":"17/9",
        "relationwise_diagonal_only":"4/3",
        "ratio":"17/12"
    },
    "common_order_opposite_sign_overlap_example":{
        "supports":["012","013"],
        "aggregate_fluctuation_energy":"7/9",
        "relationwise_diagonal_only":"4/3",
        "refund":"5/9"
    },
    "admissible_n3_one_point":{
        "qflip_coordinates":[3,5,6,7],
        "relations":{
            "R1_coords":[3,5,6],"R1_vertices":sorted(A3),"R1_weight":len(A3),"R1_r32_sign":"+",
            "R2_coords":[3,5,7],"R2_vertices":sorted(B3rel),"R2_weight":len(B3rel),"R2_r32_sign":"+"
        },
        "theta_pi_over_4_borel_coeff_each":"1",
        "aggregate_energy":"17/9",
        "diagonal_only":"4/3"
    },
    "admissible_n4_one_point_negative_credit":{
        "relations":{
            "Rplus_coords":[3,5,6],"Rplus_vertices":sorted(A4),"Rplus_weight":len(A4),"Rplus_r32_sign":"+",
            "Rminus_coords":[3,5,10],"Rminus_vertices":sorted(B4rel),"Rminus_weight":len(B4rel),"Rminus_r32_sign":"-"
        },
        "theta_pi_over_4_borel_coefficients":["1/8","-1/8"],
        "aggregate_energy":"7/576",
        "diagonal_only":"1/48",
        "signed_refund":"5/576"
    }
}
print(json.dumps(out,indent=2,sort_keys=True))
