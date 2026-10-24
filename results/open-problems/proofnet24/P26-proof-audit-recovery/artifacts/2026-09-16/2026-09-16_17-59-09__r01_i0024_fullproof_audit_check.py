#!/usr/bin/env python3
"""P26 independent exact checks for R01/I0024 (Aldous-Fill Open Problem 3.44).

This checks the finite examples and the Gram/right-inverse normalization used in
P26-AUDIT-R01-I0024-FLOW-01.  It is a finite certificate only; the universal
proof is written in the P26 run report.
"""
import sympy as sp
Q = sp.Rational


def data(weights):
    n = max(max(e) for e in weights) + 1
    deg = [sum(w for (i,j),w in weights.items() if i == v or j == v) for v in range(n)]
    W = sum(deg)
    pi = [sp.simplify(d/W) for d in deg]
    edges = sorted(weights)
    B = sp.zeros(n, len(edges))
    for k,(i,j) in enumerate(edges):
        B[i,k] = 1; B[j,k] = -1
    C = sp.diag(*[sp.simplify(weights[e]/W) for e in edges])
    Pi = sp.diag(*pi)
    P = sp.zeros(n)
    for (i,j),w in weights.items():
        P[i,j] = sp.simplify(w/deg[i]); P[j,i] = sp.simplify(w/deg[j])
    L = sp.simplify(B*C*B.T)
    assert L == sp.simplify(Pi*(sp.eye(n)-P))
    J = sp.ones(n,n)
    Lp = sp.simplify((L + J/Q(n)).inv() - J/Q(n))
    return n,pi,edges,B,C,Pi,P,Lp


def tau(P):
    ev=[]
    for z,m in P.eigenvals().items(): ev += [sp.simplify(z)]*m
    ev=sorted(ev,key=lambda z:float(sp.N(z)),reverse=True)
    return sp.simplify(1/(1-ev[1]))


def check_gram(name, weights):
    n,pi,edges,B,C,Pi,P,Lp = data(weights)
    p = sp.Matrix(pi)
    Psi = sp.zeros(len(edges),n)
    R = sp.simplify(C*B.T*Lp)
    for x in range(n):
        b=sp.zeros(n,1); b[x]=1; b-=p
        Psi[:,x]=sp.simplify(R*b)
        assert sp.simplify(B*Psi[:,x]-b)==sp.zeros(n,1)
    assert sp.simplify(Psi*p)==sp.zeros(len(edges),1)
    G=sp.simplify(Psi.T*C.inv()*Psi)
    H=sp.zeros(n,n-1)
    for i in range(n-1):
        H[i,i]=1; H[n-1,i]=-pi[i]/pi[n-1]
    lam=sp.symbols('lam')
    poly=sp.factor((H.T*Pi*G*Pi*H-lam*(H.T*Pi*H)).det())
    vals=[sp.simplify(x) for x in sp.solve(sp.Eq(poly,0),lam)]
    t=tau(P)
    assert max(vals,key=lambda z:float(sp.N(z)))==t
    print(name, 'tau=',t,'gram_eigs=',vals)

P4={(0,1):Q(1),(1,2):Q(1),(2,3):Q(1)}
K3={(0,1):Q(1),(0,2):Q(1),(1,2):Q(1)}
WT={(0,1):Q(1),(0,2):Q(2),(1,2):Q(3)}
check_gram('P4',P4)
check_gram('K3',K3)
check_gram('weighted_triangle_1_2_3',WT)

# Exact antisymmetric-projection test on a nontrivial rational kernel.
pi=[Q(1,6),Q(1,3),Q(1,2)]
D=sp.Matrix([[0,Q(2,3),Q(-5,4)],[-Q(2,3),0,Q(7,5)],[Q(5,4),-Q(7,5),0]])
g=D*sp.Matrix(pi)
var=sp.simplify(sum(pi[i]*g[i]**2 for i in range(3)))
ed2=sp.simplify(sum(pi[i]*pi[j]*D[i,j]**2 for i in range(3) for j in range(3)))
assert sp.simplify(ed2-2*var)>=0
print('projection_ed2_minus_2var=',sp.simplify(ed2-2*var))
print('ALL_EXACT_CHECKS_PASS')
