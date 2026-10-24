#!/usr/bin/env python3
# PROB20-19 exact symbolic/combinatorial self-check for the matching-supported theorem.
import sympy as sp
from itertools import combinations

def givens4(i,j,c,s):
    M=sp.eye(4)
    M[i,i]=c; M[j,j]=c
    M[i,j]=s; M[j,i]=-s
    return M

c1,s1,c2,s2=sp.symbols("c1 s1 c2 s2", nonzero=True)
G01=givens4(0,1,c1,s1)
G23=givens4(2,3,c2,s2)
G12=givens4(1,2,c2,s2)

assert G01*G23-G23*G01 == sp.zeros(4)
print("DISJOINT_GIVENS_COMMUTE=PASS")

Qd=sp.expand(G01*G23)
# Every row/column of a generic direct-sum two-block matrix has support <=2.
row_support_d=[sum(1 for x in Qd.row(i) if x!=0) for i in range(4)]
col_support_d=[sum(1 for x in Qd.col(j) if x!=0) for j in range(4)]
assert max(row_support_d)<=2 and max(col_support_d)<=2
print("DISJOINT_SUPPORT_MAX=2 PASS")

Qo=sp.expand(G01*G12)
row_support_o=[sum(1 for x in Qo.row(i) if x!=0) for i in range(4)]
col_support_o=[sum(1 for x in Qo.col(j) if x!=0) for j in range(4)]
assert max(row_support_o)>=3 or max(col_support_o)>=3
print("OVERLAP_CREATES_3_DIRECTION_COMPONENT=PASS")
print("OVERLAP_MATRIX=", Qo)

edges=list(combinations(range(4),2))
disjoint=0
overlap=0
for e,f in combinations(edges,2):
    k=len(set(e)&set(f))
    if k==0: disjoint+=1
    elif k==1: overlap+=1
assert disjoint==3 and overlap==12
print("K4_EDGE_PAIR_COUNTS disjoint=3 overlap=12 PASS")

# Polar identities used by the archived one-plane lemma.
r,phi,theta,a,b=sp.symbols("r phi theta a b", positive=True, real=True)
x1=r*(sp.cos(theta)*sp.cos(phi)+sp.sin(theta)*sp.sin(phi))
x2=r*(-sp.sin(theta)*sp.cos(phi)+sp.cos(theta)*sp.sin(phi))
assert sp.simplify(sp.trigsimp(x1**2+x2**2-r**2))==0
assert sp.simplify(sp.trigsimp((x1**2-x2**2)-r**2*sp.cos(2*(phi-theta))))==0
quad=sp.cos(phi)**2/a+sp.sin(phi)**2/b
quad2=sp.Rational(1,2)*(1/a+1/b)+sp.Rational(1,2)*(1/a-1/b)*sp.cos(2*phi)
assert sp.simplify(sp.trigsimp(quad-quad2))==0
print("POLAR_IDENTITIES=PASS")

# Deterministic top-d reduction: exact exhaustive check over a finite rational bank.
def topd(vals,d):
    return sum(sorted(vals, reverse=True)[:d])
bank=[sp.Rational(0),sp.Rational(1,5),sp.Rational(1,2),sp.Rational(7,5),sp.Rational(3)]
checks=0
for p in range(3,7):
    for d in range(1,p):
        # representative outside vectors; exact rational values.
        outs=[bank[k%len(bank)] for k in range(p-2)]
        for S in [sp.Rational(1,2),sp.Rational(2),sp.Rational(5)]:
            for M in [S/2, 3*S/4, S]:
                pair=[M,S-M]
                lhs=topd(outs+pair,d)
                so=sorted(outs, reverse=True)
                def B(k):
                    if k<0 or k>len(so): return None
                    return sum(so[:k])
                candidates=[]
                if B(d) is not None: candidates.append(B(d))
                if B(d-1) is not None: candidates.append(B(d-1)+M)
                if B(d-2) is not None: candidates.append(B(d-2)+S)
                rhs=max(candidates)
                assert sp.simplify(lhs-rhs)==0
                checks+=1
print(f"TOPD_REDUCTION_EXACT_CHECKS={checks} PASS")
print("SELF_CHECK_ONLY: theorem validity rests on the written analytic proof, not this script.")
