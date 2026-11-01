#!/usr/bin/env python3
"""
R20 / I0100 exact finite self-check for the determinant-variational/simplex-pivot route.

This is NOT a proof of Randomstrasse Conjecture 26. It verifies, for p=17,
the exact basis variational identity used in the accompanying written theorem:

    T^2/n = min_{A positive basis, 0 in A} D1(A)/D0(A),

where
    D1(A)=|det U[{0} union S,A]|^2,
    D0(A)=|det U[S,A\\{0}]|^2.

It also verifies one adjacent-basis path along which the distinguished atom
mu_A(0) strictly increases and the determinant ratio strictly decreases,
ending at the exact theta optimum T=8-4*sqrt(2).

All calculations are exact in Q(sqrt(2), i).
"""
import itertools
import sympy as sp

p=17
n=(p-1)//2
m=n//2
I=sp.I
rt2=sp.sqrt(2)
zeta=(1+I)/rt2
U=sp.Matrix([[sp.simplify(zeta**(r*c)/sp.sqrt(n)) for c in range(n)] for r in range(n)])

# Exact one-localized Paley connection set in exponent coordinates.
S=[1,4,7]
R=[0]+S
b=sp.Matrix([1/sp.sqrt(n)]+[0]*(m-1))

def abs2(z):
    return sp.simplify(sp.expand_complex(z*sp.conjugate(z)))

def real_exact(z):
    z=sp.simplify(sp.expand_complex(z))
    assert sp.simplify(sp.im(z))==0
    return sp.simplify(sp.re(z))

def nonnegative_exact(x):
    x=sp.simplify(x)
    if x==0:
        return True
    q=sp.ask(sp.Q.nonnegative(x))
    if q is not None:
        return bool(q)
    # All values in this checker lie in Q(sqrt(2)); this branch is only a
    # robust exact-sign fallback using the minimal polynomial embedding.
    poly=sp.Poly(sp.minpoly(x), sp.Symbol('x'))
    return float(sp.N(x,80)) > 0 and sp.count_roots(poly, -sp.oo, 0)==0

positive={}
for A in itertools.combinations(range(n),m):
    if 0 not in A:
        continue
    MA=U.extract(R,A)
    det=sp.simplify(MA.det())
    if det==0:
        continue
    mu=[real_exact(v) for v in (MA.inv()*b)]
    if not all(nonnegative_exact(v) for v in mu):
        continue
    pos0=A.index(0)
    mu0=sp.simplify(mu[pos0])
    Ap=tuple(j for j in A if j!=0)
    D1=abs2(det)
    D0=abs2(U.extract(S,Ap).det())
    assert D0!=0
    ratio=sp.simplify(D1/D0)
    assert sp.simplify(mu0**2-D0/(n*D1))==0
    assert sp.simplify(ratio-1/(n*mu0**2))==0
    positive[A]=(mu,mu0,sp.simplify(ratio))

assert len(positive)==10

T=8-4*rt2
target=sp.simplify(T**2/n)
bestA=min(positive, key=lambda A: float(sp.N(positive[A][2],80)))
assert bestA==(0,3,4,5)
assert sp.simplify(positive[bestA][1]-1/T)==0
assert sp.simplify(positive[bestA][2]-target)==0

# A concrete exact improving simplex/basis-exchange path.
path=[
    (0,1,4,7),
    (0,1,4,5),
    (0,3,4,5),
]
assert all(A in positive for A in path)
assert all(len(set(path[i])^set(path[i+1]))==2 for i in range(len(path)-1))

atoms=[sp.simplify(positive[A][1]) for A in path]
ratios=[sp.simplify(positive[A][2]) for A in path]
expected_atoms=[
    sp.Rational(1,4)-rt2/8,
    sp.Rational(1,4),
    sp.Rational(1,4)+rt2/8,
]
assert all(sp.simplify(a-b)==0 for a,b in zip(atoms,expected_atoms))
assert all(float(sp.N(atoms[i+1]-atoms[i],80))>0 for i in range(2))
assert all(float(sp.N(ratios[i]-ratios[i+1],80))>0 for i in range(2))

# Complementary basis at the optimum is positive and realizes the exact
# complementary max-atom value T/n.
N=sorted(set(range(1,n))-set(S))
C=[0]+N
Aopt=bestA
B=tuple([0]+sorted(set(range(1,n))-set(Aopt[1:])))
assert len(B)==m+1
rhsB=sp.Matrix([1/sp.sqrt(n)]+[0]*(len(C)-1))
MB=U.extract(C,B)
assert sp.simplify(MB.det())!=0
nu=[real_exact(v) for v in (MB.inv()*rhsB)]
assert all(nonnegative_exact(v) for v in nu)
assert sp.simplify(nu[0]-T/n)==0
assert sp.simplify(positive[Aopt][1]*nu[0]-sp.Rational(1,n))==0

print("R20 I0100 p=17 exact determinant-variational / pivot self-check")
print("p =",p,"n =",n,"m =",m,"S =",S,"N =",N)
print("positive_bases_containing_0 =",len(positive))
print("best_basis =",bestA)
print("theta_exact =",T)
print("min_D1_over_D0 =",sp.simplify(positive[bestA][2]))
print("theta_squared_over_n =",sp.simplify(T**2/n))
print("pivot_path =",path)
print("pivot_atoms =",atoms)
print("pivot_ratios =",ratios)
print("complement_basis =",B)
print("complement_atom =",nu[0])
print("atom_product =",sp.simplify(positive[Aopt][1]*nu[0]))
print("PASS")
