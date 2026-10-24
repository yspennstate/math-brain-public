#!/usr/bin/env python3
"""Independent R18 exact/symbolic audit of R19-I0084-C001.

This is not a copy of R19's checker. It independently differentiates the
positive half-stable kernel, verifies all rational margins used by the proof,
and checks the sparse-weight moment/tail algebra. Infinite-series uniform
convergence and the unimodality contradiction are re-derived in the R18 report.
"""
from fractions import Fraction
import sympy as sp

r,s,u=sp.symbols('r s u', positive=True)
K=r**sp.Rational(-3,2)*sp.exp(-s/(2*r))
Kprime=sp.diff(K,r)
claimed=(s-3*r)/(2*r**sp.Rational(7,2))*sp.exp(-s/(2*r))
assert sp.simplify(Kprime-claimed)==0
H=(1-3*u)/(2*u**sp.Rational(7,2))*sp.exp(-1/(2*u))
assert sp.simplify((s**sp.Rational(5,2)*Kprime).subs(r,s*u)-H)==0

assert Fraction(3151,32)<99

tail=Fraction(1,128)/(1-Fraction(1,128))
assert tail==Fraction(1,127)
margin=Fraction(4)-99*tail
assert margin==Fraction(409,127) and margin>0

n=sp.symbols('n', integer=True, nonnegative=True)
expr=sp.factor((-n**2+sp.Rational(5,2)*n)-(-sp.Rational(1,2)*n**2))
assert expr==-n*(n-5)/2
for N in range(5,1000):
    assert -N*N+Fraction(5,2)*N<=Fraction(-N*N,2)

for p in [Fraction(1,3),Fraction(5,2),Fraction(17,4),Fraction(31,7),Fraction(25)]:
    N=(2*p.numerator+p.denominator-1)//p.denominator
    for k in range(N,N+50):
        assert -k*k+p*k<=Fraction(-k*k,2)

for N in range(3,30):
    bound=Fraction(2**(N-1),1)
    for den in [2,3,5,7,11]:
        sval=bound-Fraction(1,den)
        assert sval>0
        assert 2**N>2*sval>sval/3
        an=-2**N; anm1=-2**(N-1)
        assert an+sval<anm1

print('PASS independent R18 audit of R19-I0084-C001 finite/symbolic core')
print('kernel derivative identity: exact symbolic PASS')
print('tail ratio =',tail)
print('positive slope margin =',margin)
print('critical and general moment exponents: PASS')
print('one-sided shielding geometry: exact rational grid PASS; general algebra in report')
