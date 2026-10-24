#!/usr/bin/env python3
"""Exact symbolic certificate for the full-dimensional KS Taylor expansion in P10/F0119."""
import itertools
import sympy as sp

N=6
a,b,c,d=sp.symbols('a b c d', real=True)
s2=sp.sqrt(2)
x=[a,b,-a-b]
y=[c,d,-c-d]

def pmul(P,Q):
    R=[sp.Integer(0)]*(N+1)
    for i,pi in enumerate(P):
        if pi==0: continue
        for j,qj in enumerate(Q):
            if i+j<=N and qj!=0:
                R[i+j]+=pi*qj
    return [sp.expand(v) for v in R]

def ppow(P,n):
    R=[sp.Integer(1)]+[sp.Integer(0)]*N
    for _ in range(n):
        R=pmul(R,P)
    return R

def psi_dev(zps):
    out=[sp.Integer(0)]*(N+1)
    # Psi(u+z)=3/2 S2+5/4 S4-27/20 S5+27/10 S6+O(7)
    for n,coef in [(2,sp.Rational(3,2)),(4,sp.Rational(5,4)),(5,-sp.Rational(27,20)),(6,sp.Rational(27,10))]:
        S=[sp.Integer(0)]*(N+1)
        for zp in zps:
            P=ppow(zp,n)
            S=[S[k]+P[k] for k in range(N+1)]
        out=[sp.expand(out[k]+coef*S[k]) for k in range(N+1)]
    return out

def invden(D):
    R=[sp.Integer(0)]*(N+1)
    alpha=sp.Rational(3,2)*D
    for k in range(N//2+1):
        R[2*k]=(-alpha)**k
    return R

zpx=[[0,xi]+[0]*(N-1) for xi in x]
zpy=[[0,yi]+[0]*(N-1) for yi in y]
Px=psi_dev(zpx); Py=psi_dev(zpy)
K=[sp.Integer(0)]*(N+1)
for perm in itertools.permutations(range(3)):
    yp=[y[i] for i in perm]
    D=sum(x[i]*yp[i] for i in range(3))
    inv=invden(D)
    zps=[]
    for i in range(3):
        num=[sp.Rational(1,3),(x[i]+yp[i])/s2,sp.Rational(3,2)*x[i]*yp[i]]+[0]*(N-2)
        pi=pmul(num,inv)
        pi[0]-=sp.Rational(1,3)
        zps.append(pi)
    P=psi_dev(zps)
    weight=[1,0,sp.Rational(3,2)*D]+[0]*(N-2)
    WP=pmul(weight,P)
    K=[sp.expand(K[k]+WP[k]/6) for k in range(N+1)]

H=[sp.factor(sp.expand((Px[k]+Py[k])/2-K[k])) for k in range(N+1)]
A=sp.expand(sum(v**2 for v in x)); B=sp.expand(sum(v**2 for v in y))
Cx=sp.expand(sum(v**3 for v in x)); Cy=sp.expand(sum(v**3 for v in y))
H4_target=sp.Rational(1,32)*(5*A**2-2*A*B+5*B**2)
alpha=-sp.Rational(9,16)+9*s2/sp.Integer(64)
beta=21*s2/sp.Integer(16)
H5_target=alpha*(A*Cx+B*Cy)+beta*(A*Cy+B*Cx)
H6_target=(sp.Rational(81,320)*(A**3+B**3)
           +sp.Rational(27,80)*(Cx**2+Cy**2)
           +sp.Rational(3,32)*(A**2*B+A*B**2)
           -sp.Rational(27,8)*Cx*Cy)
assert sp.expand(H[2])==0 and sp.expand(H[3])==0
assert sp.expand(H[4]-H4_target)==0
assert sp.expand(H[5]-H5_target)==0
assert sp.expand(H[6]-H6_target)==0
print('H4_EXACT_PASS')
print('H5_EXACT_PASS')
print('H6_EXACT_PASS')
print('alpha =',alpha)
print('beta =',beta)
print('OVERALL_PASS')
