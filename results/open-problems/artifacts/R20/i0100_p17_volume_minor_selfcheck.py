#!/usr/bin/env python3
"""
R20/I0100 exact self-check for the volume-minor / positive-basis reformulation.

This is NOT a proof of Randomstrasse Conjecture 26.  It exactly verifies at p=17:
  (i) the two Cauchy--Binet aggregate minor identities;
  (ii) one complementary positive physical-support pair;
  (iii) the Cramer determinant formula for the two zero atoms;
  (iv) Jacobi complementary-minor equality in squared modulus;
  (v) the known exact theta value T_17=8-4*sqrt(2).

All arithmetic is symbolic in Q(sqrt(2), i).
"""
import sympy as sp
import itertools

p=17
n=(p-1)//2
m=n//2
I=sp.I
rt2=sp.sqrt(2)
zeta=(1+I)/rt2
U=sp.Matrix([[sp.simplify(zeta**(r*c)/sp.sqrt(n)) for c in range(n)] for r in range(n)])

alpha=9
Q={x*x % p for x in range(1,p)}
vals=[pow(alpha,j,p) for j in range(n)]
S=sorted(d for d in range(1,n) if (vals[d]-1)%p in Q)
N=sorted(set(range(1,n))-set(S))
assert S==[1,4,7]
assert N==[2,3,5,6]
assert len(S)==m-1 and len(N)==m

R=[0]+S
C=[0]+N

def abs2(z):
    return sp.simplify(sp.expand_complex(z*sp.conjugate(z)))

sum_D1=sp.Integer(0)
sum_D0=sp.Integer(0)
for Ap in itertools.combinations(range(1,n),m-1):
    A=(0,)+Ap
    d1=U.extract(R,A).det()
    d0=U.extract(S,Ap).det()
    sum_D1=sp.simplify(sum_D1+abs2(d1))
    sum_D0=sp.simplify(sum_D0+abs2(d0))

assert sp.simplify(sum_D1-sp.Rational(m,n))==0
assert sp.simplify(sum_D1-sp.Rational(1,2))==0
assert sp.simplify(sum_D0-(1-sp.Rational(m-1,n)))==0
assert sp.simplify(sum_D0-sp.Rational(m+1,2*m))==0
assert sp.simplify(sum_D1/sum_D0-sp.Rational(m,m+1))==0

A=[0,3,4,5]
Ap=[3,4,5]
B=[0,1,2,6,7]
Bp=[1,2,6,7]
assert sorted(set(Ap)|set(Bp))==list(range(1,n))
assert set(Ap).isdisjoint(Bp)

rhsA=sp.Matrix([1/sp.sqrt(n)]+[0]*(len(R)-1))
rhsB=sp.Matrix([1/sp.sqrt(n)]+[0]*(len(C)-1))
mu=U.extract(R,A).inv()*rhsA
nu=U.extract(C,B).inv()*rhsB
mu=[sp.simplify(sp.expand_complex(x)) for x in mu]
nu=[sp.simplify(sp.expand_complex(x)) for x in nu]

mu_expected=[
    sp.Rational(1,4)+rt2/8,
    sp.Rational(1,4),
    sp.Rational(1,4)-rt2/8,
    sp.Rational(1,4),
]
nu_expected=[
    1-rt2/2,
    -sp.Rational(1,2)+rt2/2,
    sp.Rational(1,2)-rt2/4,
    sp.Rational(1,2)-rt2/4,
    -sp.Rational(1,2)+rt2/2,
]
assert all(sp.simplify(a-b)==0 for a,b in zip(mu,mu_expected))
assert all(sp.simplify(a-b)==0 for a,b in zip(nu,nu_expected))
assert all(float(sp.N(x,30))>0 for x in mu+nu)
assert sp.simplify(sum(mu)-1)==0
assert sp.simplify(sum(nu)-1)==0

det_RA=U.extract(R,A).det()
det_SAp=U.extract(S,Ap).det()
det_CB=U.extract(C,B).det()
det_NBp=U.extract(N,Bp).det()

a2_from_det=sp.simplify(abs2(det_SAp)/(n*abs2(det_RA)))
b2_from_det=sp.simplify(abs2(det_NBp)/(n*abs2(det_CB)))
assert sp.simplify(a2_from_det-mu[0]**2)==0
assert sp.simplify(b2_from_det-nu[0]**2)==0
assert sp.simplify(abs2(det_SAp)-abs2(det_CB))==0
assert sp.simplify(abs2(det_RA)-abs2(det_NBp))==0

a=mu[0]
b=nu[0]
assert sp.simplify(a*b-sp.Rational(1,n))==0
T=sp.simplify(1/a)
assert sp.simplify(T-(8-4*rt2))==0
ratio2=sp.simplify(abs2(det_RA)/abs2(det_SAp))
assert sp.simplify(T**2/n-ratio2)==0

print("R20 I0100 p=17 exact volume-minor self-check")
print("p =",p,"n =",n,"m =",m)
print("S =",S,"N =",N)
print("sum_D1 =",sum_D1)
print("sum_D0 =",sum_D0)
print("aggregate_ratio =",sp.simplify(sum_D1/sum_D0))
print("positive_A =",A)
print("positive_B =",B)
print("mu =",mu)
print("nu =",nu)
print("mu0*nu0 =",sp.simplify(a*b))
print("Jacobi_minor_equalities = PASS")
print("Cramer_atom_formulas = PASS")
print("theta_exact =",T)
print("theta_numeric =",sp.N(T,30))
print("theta_over_sqrt_n =",sp.N(T/sp.sqrt(n),30))
print("PASS")
