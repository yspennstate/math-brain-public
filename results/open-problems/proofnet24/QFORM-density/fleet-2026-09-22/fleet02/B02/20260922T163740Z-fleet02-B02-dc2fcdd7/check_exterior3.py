#!/usr/bin/env python3
from itertools import combinations, product
from random import Random
from math import sqrt, e
from mpmath import beta

def det3(M):
    return (M[0][0]*(M[1][1]*M[2][2]-M[1][2]*M[2][1])
           -M[0][1]*(M[1][0]*M[2][2]-M[1][2]*M[2][0])
           +M[0][2]*(M[1][0]*M[2][1]-M[1][1]*M[2][0]))

def minor3(A,S,T):
    return det3([[A[i][j] for j in T] for i in S])

def matmul(A,B):
    n=len(A); m=len(B[0]); k=len(B)
    return [[sum(A[i][r]*B[r][j] for r in range(k)) for j in range(m)] for i in range(n)]

def masses(A):
    n=len(A); tri=list(combinations(range(n),3))
    M=[0,0,0,0]
    for S in tri:
        s=set(S)
        for T in tri:
            d=minor3(A,S,T)
            M[len(s.intersection(T))] += d*d
    return M

def e3_A2(A):
    A2=matmul(A,A); n=len(A)
    return sum(minor3(A2,S,S) for S in combinations(range(n),3))

def max_R0(A):
    n=len(A); ans=0
    for mask in range(1<<n):
        I=[i for i in range(n) if (mask>>i)&1]
        J=[i for i in range(n) if not ((mask>>i)&1)]
        val=0
        for S in combinations(I,3):
            for T in combinations(J,3):
                d=minor3(A,S,T); val += d*d
        ans=max(ans,val)
    return ans

def max_Rj(A,j):
    n=len(A); ans=0
    for colors in product(range(3), repeat=n):
        P=[i for i,c in enumerate(colors) if c==0]
        I=[i for i,c in enumerate(colors) if c==1]
        J=[i for i,c in enumerate(colors) if c==2]
        val=0
        if j==1:
            for k in P:
                for R in combinations(I,2):
                    for T in combinations(J,2):
                        d=minor3(A,(k,)+R,(k,)+T); val += d*d
        else:
            for K in combinations(P,2):
                for i in I:
                    for t in J:
                        d=minor3(A,K+(i,),K+(t,)); val += d*d
        ans=max(ans,val)
    return ans

rng=Random(20260922)
for rep in range(3):
    n=6
    X=[[rng.randint(-2,2) for _ in range(n)] for __ in range(n)]
    A=[[X[i][j]+X[j][i] for j in range(n)] for i in range(n)]
    M=masses(A); e3=e3_A2(A)
    assert sum(M)==e3
    r0=max_R0(A); r1=max_Rj(A,1); r2=max_Rj(A,2)
    assert 64*r0 >= M[0]
    assert 3**5*r1 >= M[1]
    assert 3**4*r2 >= M[2]
    print("rep",rep,"M",M,"e3",e3,
          "slacks",(64*r0-M[0],3**5*r1-M[1],3**4*r2-M[2]))

# Explicit application of fleet03/B02 balanced rank-two theorem at mu<=9/50.
mu=9/50
tau=121/200
q=183/100
r=48/25
assert tau*tau > 2*mu
assert 2*mu/(1-tau) <= q/2
assert q < r < 2
C = (4*(2-r)**((r-3)/2)*r**(-r/2)*sqrt(e)*2**(-3/4)*q**(-1/4)
     *sqrt(0.5*float(beta(1/4,r/(4*q)-1/4)))
     *sqrt(2)*(1-tau*tau)**(-1/4))
print("partner_mu",mu,"tau",tau,"q",q,"r",r,
      "leverage",2*mu/(1-tau),"C_bal",C,
      "exact_rank3_bound",sqrt(2)*C)
print("STATUS=ALL_EXACT_COMBINATORIAL_CHECKS_PASS")
