#!/usr/bin/env python3
from fractions import Fraction
from itertools import combinations, product
import math, random
import numpy as np

random.seed(20260922)
np.random.seed(20260922)


def det2(a,b,c,d):
    return a*d-b*c


def det3(M):
    return (M[0][0]*(M[1][1]*M[2][2]-M[1][2]*M[2][1])
            -M[0][1]*(M[1][0]*M[2][2]-M[1][2]*M[2][0])
            +M[0][2]*(M[1][0]*M[2][1]-M[1][1]*M[2][0]))


def exact_zero_identity(c,r,D):
    m,n=len(c),len(r)
    Z=Fraction(0)
    for j,k in combinations(range(m),2):
        for p,q in combinations(range(n),2):
            M=[[Fraction(0),r[p],r[q]],
               [c[j],D[j][p],D[j][q]],
               [c[k],D[k][p],D[k][q]]]
            Z += det3(M)**2
    cn=sum(x*x for x in c)
    rn=sum(x*x for x in r)
    Df=sum(D[i][j]*D[i][j] for i in range(m) for j in range(n))
    Dt_c=[sum(D[i][j]*c[i] for i in range(m)) for j in range(n)]
    Dr=[sum(D[i][j]*r[j] for j in range(n)) for i in range(m)]
    cDr=sum(c[i]*Dr[i] for i in range(m))
    rhs=cn*rn*Df-rn*sum(x*x for x in Dt_c)-cn*sum(x*x for x in Dr)+cDr*cDr
    assert Z==rhs, (Z,rhs)


def E2(M):
    m,n=M.shape
    z=0.0
    for i,j in combinations(range(m),2):
        for p,q in combinations(range(n),2):
            z += np.linalg.det(M[np.ix_([i,j],[p,q])])**2
    return z


def deshear_check(m,n,trials=2000):
    worst=0.0
    for _ in range(trials):
        D=np.random.randn(m,n)
        c=np.random.randn(m)
        r=np.random.randn(n)
        b=random.choice([-1,1])*(0.1+3*random.random())
        S=D-np.outer(c,r)/b
        lhs=abs(b)*math.sqrt(max(E2(S),0.0))
        phys=abs(b)*math.sqrt(max(E2(D),0.0))
        rr=np.dot(r,r)*np.linalg.norm(D,'fro')**2-np.linalg.norm(D@r)**2
        cc=np.dot(c,c)*np.linalg.norm(D,'fro')**2-np.linalg.norm(D.T@c)**2
        tR=np.linalg.norm(c)*math.sqrt(max(rr,0.0))
        tL=np.linalg.norm(r)*math.sqrt(max(cc,0.0))
        assert lhs <= phys+tR+1e-9*(1+lhs+phys+tR)
        assert lhs <= phys+tL+1e-9*(1+lhs+phys+tL)
        worst=max(worst,lhs/max(phys+tR,1e-300),lhs/max(phys+tL,1e-300))
    return worst


def separated_minor_check(M):
    m,n=M.shape
    total=E2(M)
    if m<2 or n<2:
        return 0.0,0.0
    best=0.0
    # Enumerate nontrivial two-colorings with first element fixed to avoid complements.
    for rb in product([0,1], repeat=m-1):
        R=[0]+list(rb)
        if all(x==R[0] for x in R):
            continue
        for cb in product([0,1], repeat=n-1):
            C=[0]+list(cb)
            if all(x==C[0] for x in C):
                continue
            z=0.0
            for i,j in combinations(range(m),2):
                if R[i]==R[j]:
                    continue
                for p,q in combinations(range(n),2):
                    if C[p]==C[q]:
                        continue
                    z += np.linalg.det(M[np.ix_([i,j],[p,q])])**2
            best=max(best,z)
    assert best+1e-10 >= total/4
    return best,total


# Exact polynomial identity for the b=0 branch.
for _ in range(100):
    m,n=3,4
    c=[Fraction(random.randint(-4,4)) for _ in range(m)]
    r=[Fraction(random.randint(-4,4)) for _ in range(n)]
    D=[[Fraction(random.randint(-4,4)) for _ in range(n)] for _ in range(m)]
    exact_zero_identity(c,r,D)

worst=max(deshear_check(3,4),deshear_check(5,3),deshear_check(4,4))

for _ in range(30):
    M=np.random.randn(3,3)
    separated_minor_check(M)

print('delta=',1/math.sqrt(768))
print('delta/2=',1/(2*math.sqrt(768)))
print('delta/8=',1/(8*math.sqrt(768)))
print('delta^2/8=',1/(768*8))
print('worst_deshear_ratio=',worst)
print('exact_zero_identity_trials=100')
print('separated_minor_partition_trials=30')
print('QFORM_B20_R20_CHECK_PASS')
