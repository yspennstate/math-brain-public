#!/usr/bin/env python3
from fractions import Fraction
from math import comb, factorial

def B(a,b):
    return Fraction(factorial(a-1)*factorial(b-1), factorial(a+b-1))

print("R10 I0070 / R11 exact checker")
print("run=20260916T2138Z_i0070_progressive_representative")

# R10 critical endpoint algebra:
# s=2 beta-1, criticality s(rho+1)=1.
# The compact-tail coefficient exponent is (1-s)(rho+1)=rho.
for num in range(1,31):
    for den in range(1,31):
        rho=Fraction(num,den)
        s=Fraction(1,1)/(rho+1)
        beta=(1+s)/2
        assert Fraction(1,2) < beta < 1
        assert (2*beta-1)*(rho+1)==1
        assert (1-s)*(rho+1)==rho
print("R10 critical tail exponent identity: PASS (900 exact rational rho values)")

# R11 RRT fringe expectation recurrence E Z_{m,s}=m/[s(s+1)].
for n in range(2,51):
    lhs=Fraction(n+1,2)
    rhs=(1-Fraction(1,n))*Fraction(n,2)+1
    assert lhs==rhs
    for s in range(2,n):
        En_s=Fraction(n,s*(s+1))
        En_sm1=Fraction(n,(s-1)*s)
        rec=(1-Fraction(s,n))*En_s+Fraction(s-1,n)*En_sm1
        target=Fraction(n+1,s*(s+1))
        assert rec==target
print("R11 fringe expectation recurrence: PASS (n<=50)")

# R11 visible one-orientation hazard identity.
def hazard(m,b,i):
    total=Fraction(0)
    for s in range(i, m-(b-i)+1):
        EZ=Fraction(m,s*(s+1))
        w=Fraction(s+1,2*(m-s))
        cond=Fraction(comb(m-b,s-i),comb(m,s))
        total += EZ*w*cond
    return total

checks=0
for m in range(2,31):
    for b in range(2,m+1):
        for i in range(1,b):
            assert hazard(m,b,i)==B(i,b-i)/2
            checks+=1
print(f"R11 one-orientation beta hazard identity: PASS ({checks} exact triples, m<=30)")

# Both orientations sum to B(i,b-i); total unordered split rate is H_{b-1}.
for b in range(2,31):
    total=Fraction(0)
    for i in range(1,b):
        total += Fraction(comb(b,i),2)*B(i,b-i)
    H=sum((Fraction(1,k) for k in range(1,b)), Fraction(0))
    assert total==H
print("R11 CTCS total split-rate identity: PASS (b<=30)")
print("ALL_EXACT_CHECKS_PASS")
