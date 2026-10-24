#!/usr/bin/env python3
"""
R01 / I0024 auto run checker.
Exact SymPy verification for:
(1) the right-inverse flow formula on exact rational reversible chains;
(2) equivalence between electrical all-pairs flows and the routing operator;
(3) an independent algebraic audit of R02-KLS-C001/C002 finite core.

Finite checks do not replace the theorem proofs in the reports.
"""
import sympy as sp
from fractions import Fraction

Q=sp.Rational

def laplacian_data(P, pi):
    n=P.rows
    Pi=sp.diag(*pi)
    edges=[]; cs=[]
    for i in range(n):
        for j in range(i+1,n):
            c=sp.simplify(pi[i]*P[i,j])
            if c != 0:
                assert c>0
                assert sp.simplify(c-pi[j]*P[j,i])==0
                edges.append((i,j)); cs.append(c)
    B=sp.zeros(n,len(edges))
    for k,(i,j) in enumerate(edges):
        B[i,k]=1; B[j,k]=-1
    C=sp.diag(*cs)
    L=sp.simplify(B*C*B.T)
    assert L==sp.simplify(Pi*(sp.eye(n)-P))
    J=sp.ones(n,n)
    Lp=sp.simplify((L+J/Q(n)).inv()-J/Q(n))
    return Pi,edges,B,C,L,Lp

def H0_basis(n):
    K=sp.zeros(n,n-1)
    for i in range(n-1):
        K[i,i]=1
        K[n-1,i]=-1
    assert sp.ones(1,n)*K==sp.zeros(1,n-1)
    return K

def right_inverse_check(P,pi, expected_tau):
    n=P.rows
    Pi,edges,B,C,L,Lp=laplacian_data(P,pi)
    K=H0_basis(n)
    Rstar=sp.simplify(C*B.T*Lp*K)
    assert sp.simplify(B*Rstar-K)==sp.zeros(n,n-1)

    E=sp.simplify(Rstar.T*C.inv()*Rstar)
    G=sp.simplify(K.T*Pi.inv()*K)
    A=sp.simplify(G.inv()*E)
    vals=[]
    for z,m in A.eigenvals().items():
        vals += [sp.simplify(z)]*m
    maxcost=max(vals,key=lambda z:float(z))
    assert sp.simplify(maxcost-expected_tau)==0

    Rfull=sp.simplify(C*B.T*Lp)
    pair={}
    for x in range(n):
        for y in range(n):
            d=sp.zeros(n,1)
            d[x]=1; d[y]-=1
            f=sp.simplify(Rfull*d)
            assert sp.simplify(B*f-d)==sp.zeros(n,1)
            pair[(x,y)]=f
    Psi=sp.zeros(len(edges),n)
    for x in range(n):
        col=sp.zeros(len(edges),1)
        for y in range(n):
            col += pi[y]*pair[(x,y)]
        Psi[:,x]=sp.simplify(col)
    assert sp.simplify(Psi*K-Rfull*K)==sp.zeros(len(edges),n-1)

    H=sp.zeros(n,n-1)
    for i in range(n-1):
        H[i,i]=1
        H[n-1,i]=-pi[i]/pi[n-1]
    assert sp.Matrix([pi])*H==sp.zeros(1,n-1)
    Theta=sp.zeros(len(edges),n-1)
    for x in range(n):
        for y in range(n):
            coeff=H[x,:]-H[y,:]
            Theta += Q(1,2)*pi[x]*pi[y]*pair[(x,y)]*coeff
    assert sp.simplify(Theta-Rfull*Pi*H)==sp.zeros(len(edges),n-1)

    ev=[]
    for z,m in P.eigenvals().items():
        ev += [sp.simplify(z)]*m
    ev=sorted(ev,key=lambda z:float(z),reverse=True)
    tau=sp.simplify(1/(1-ev[1]))
    assert tau==expected_tau
    return vals

P4=sp.Matrix([[0,1,0,0],[Q(1,2),0,Q(1,2),0],[0,Q(1,2),0,Q(1,2)],[0,0,1,0]])
pi4=[Q(1,6),Q(1,3),Q(1,3),Q(1,6)]
vals4=right_inverse_check(P4,pi4,Q(2))
print("I0024 RIGHT-INVERSE PASS P4:", sorted(vals4,key=float), "tau=2")

K3=sp.Matrix([[0,Q(1,2),Q(1,2)],[Q(1,2),0,Q(1,2)],[Q(1,2),Q(1,2),0]])
pi3=[Q(1,3)]*3
vals3=right_inverse_check(K3,pi3,Q(2,3))
print("I0024 RIGHT-INVERSE PASS K3:", sorted(vals3,key=float), "tau=2/3")

Pnu=sp.Matrix([[Q(1,4),Q(1,4),Q(1,2)],
               [Q(1,6),Q(1,3),Q(1,2)],
               [Q(1,5),Q(3,10),Q(1,2)]])
pinu=[Q(1,5),Q(3,10),Q(1,2)]
assert sp.Matrix([pinu])*Pnu==sp.Matrix([pinu])
valsnu=right_inverse_check(Pnu,pinu,Q(12,11))
print("I0024 RIGHT-INVERSE PASS nonuniform:", sorted(valsnu,key=float), "tau=12/11")

# Independent R02 audit finite core.
a,b,c=sp.symbols('a b c', positive=True)
Omega=sp.simplify(a*b*c/6*((1+a)/(1+b)+(1+a)/(1+c)+(1+b)/(1+a)+(1+b)/(1+c)+(1+c)/(1+a)+(1+c)/(1+b)))
U=sp.expand(a*b*c+(c*(a-b)**2+a*(b-c)**2+b*(c-a)**2)/6)
avg=sp.expand((a**3+b**3+c**3)/3)
Schur=sp.expand(a**3+b**3+c**3+3*a*b*c-(a*a*b+a*a*c+b*b*a+b*b*c+c*c*a+c*c*b))
AMGM=sp.expand(a**3+b**3+c**3-3*a*b*c)
assert sp.simplify(6*(avg-U)-(Schur+AMGM))==0
samples=[(Q(1,7),Q(2,5),Q(9,4)),(Q(2),Q(3),Q(5)),(Q(1,2),Q(1,2),Q(8))]
for aa,bb,cc in samples:
    oo=sp.simplify(Omega.subs({a:aa,b:bb,c:cc}))
    uu=sp.simplify(U.subs({a:aa,b:bb,c:cc}))
    av=sp.simplify(avg.subs({a:aa,b:bb,c:cc}))
    assert oo<=uu<=av
print("R02 C001 coefficient symmetrization independent audit: PASS")

def r02_family(m):
    N=8*(m**3-m)//3
    assert 3*N==8*(m**3-m)
    hsum=Q(m**3-m)+N*(Q(1,8)-Q(1,2))
    s1=Q(m)+N*Q(1,2)
    s3=Q(m**3)+N*Q(1,8)
    assert hsum==0 and s1==s3
    n=1+N
    assert s3<=n
    Iz=4*s3
    return n,s3,Iz
for m in [2,3,7,25,100]:
    n,s3,Iz=r02_family(m)
    assert Iz<=4*n
print("R02 C002/X001 exact balanced-root family audit: PASS")
print("ALL CHECKS PASS")
