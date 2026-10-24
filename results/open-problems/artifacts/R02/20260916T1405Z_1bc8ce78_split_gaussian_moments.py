#!/usr/bin/env python3
# Exact moment certificate for the uniformly strongly log-concave skew product
# used in R02 X002/X003.
import sympy as sp
pi=sp.pi
c=sp.Rational(2,3)*sp.sqrt(2/pi)
# Base density proportional to exp(-x^2/2) on x<0 and exp(-2x^2) on x>=0.
# Half-line Gaussian moments give the following raw moments exactly.
m1=sp.simplify(c*(-1+sp.Rational(1,4)))
m2=sp.simplify(c*sp.sqrt(pi/2)*(1+sp.Rational(1,8)))
m3=sp.simplify(c*(-2+sp.Rational(1,8)))
var=sp.simplify(m2-m1**2)
mu3=sp.simplify(m3-3*m1*m2+2*m1**3)
tau=sp.simplify(mu3/var**sp.Rational(3,2))
assert sp.simplify(m1+sp.sqrt(2/pi)/2)==0
assert m2==sp.Rational(3,4)
assert sp.simplify(m3+sp.Rational(5,4)*sp.sqrt(2/pi))==0
assert sp.simplify(var-(3*pi-2)/(4*pi))==0
assert sp.simplify(mu3+sp.sqrt(2)*(pi+4)/(8*pi**sp.Rational(3,2)))==0
assert sp.simplify(tau+sp.sqrt(2)*(pi+4)/(3*pi-2)**sp.Rational(3,2))==0
assert tau!=0
print('split-Gaussian exact moments PASS')
print('mean =',m1)
print('variance =',var)
print('central third moment =',mu3)
print('standardized third moment tau =',tau)
print('tau^2 =',sp.simplify(tau**2))
print('ALL CHECKS PASS')
