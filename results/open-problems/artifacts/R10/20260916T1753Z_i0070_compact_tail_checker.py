#!/usr/bin/env python3
from fractions import Fraction
import math, random

SEED=202609161753
rng=random.Random(SEED)
print('R10 I0070 compact-tail endpoint algebra checker')
print(f'seed={SEED}')
print('All critical exponent identities below use exact rational arithmetic.')

# Critical interpolation identity s(rho+1)=1 and the positive H-tail exponent.
for rho in range(1,31):
    s=Fraction(1,rho+1)
    assert s*(rho+1)==1
    assert 1-s>0
    assert s*rho==1-s
print('C002 critical identities rho=1..30: PASS')

# Representative strict-subcritical exponent checks.
for rho in range(1,21):
    for a in [Fraction(1,2),Fraction(2,3),Fraction(3,4)]:
        s=a/Fraction(rho+1,1)
        assert s*(rho+1)<1
        assert s*rho<1
        assert 1-s>0
print('C002 strict-subcritical exponent checks: PASS')

# Scalar compiler used in the rank-one linearization:
# y <= a*x+C -> y=h+b with h<=a*x and b<=C.
for _ in range(100000):
    x=Fraction(rng.randint(0,1000),17)
    a=Fraction(rng.randint(1,100),101)
    C=Fraction(rng.randint(0,1000),29)
    ub=a*x+C
    y=Fraction(rng.randint(0,1000),1000)*ub
    b=min(y,C)
    h=y-b
    assert h+b==y and b<=C and h<=a*x
print('C002 bounded-remainder/rank-one scalar compiler 100000 cases: PASS')

# Neumann perturbation algebra: M*delta<=1/2 gives inverse bound <=2M.
for _ in range(100000):
    M=Fraction(rng.randint(1,1000),100)
    delta=Fraction(rng.randint(0,1000),1000)/(2*M+1)
    q=M*delta
    if q>Fraction(1,2):
        delta=Fraction(1,2)/M
        q=M*delta
    assert q<=Fraction(1,2)
    assert M/(1-q)<=2*M
print('C003 small-perturbation contraction algebra 100000 cases: PASS')

# Independent R11-C002 audit core: total binary Ewens tangent rate is H_{m-1}.
for m in range(2,31):
    H=sum(Fraction(1,j) for j in range(1,m))
    total=Fraction(0)
    for i in range(1,m):
        beta=Fraction(math.factorial(i-1)*math.factorial(m-i-1),math.factorial(m-1))
        total += Fraction(math.comb(m,i),2)*beta
    assert total==H
print('R11-C002 Ewens binary generator total-rate identity m=2..30: PASS')
print('PASS')
