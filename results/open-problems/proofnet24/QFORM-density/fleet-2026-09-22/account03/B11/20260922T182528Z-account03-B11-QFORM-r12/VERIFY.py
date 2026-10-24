#!/usr/bin/env python3
"""Exact symbolic regression checks for account03/B11 QFORM r12."""
import sympy as sp

kappa,d,e,c,M,K,a,b = sp.symbols('kappa d e c M K a b', positive=True)
Q = sp.Matrix([[0,kappa,0],[kappa,d,e],[0,e,c]])
assert sp.factor(Q.det()) == -c*kappa**2

A = M/(2*a)
B = 4*sp.sqrt(2)*K*sp.sqrt(M)/sp.sqrt(a*b)
rstar = (2*A/B)**(sp.Rational(2,3))
minimum = sp.simplify(A/rstar+B*sp.sqrt(rstar))
target = 3*2**(sp.Rational(2,3))*(M*K)**(sp.Rational(2,3))*a**(-sp.Rational(2,3))*b**(-sp.Rational(1,3))
assert sp.simplify(minimum-target) == 0

# The h>1/2 reduction multiplies the base constant by at most 2^(1/3).
assert sp.simplify(3*2**(sp.Rational(2,3))*2**(sp.Rational(1,3))-6) == 0
print('QFORM_HEAVY_NULL_SEPARATED_CHECK_PASS')
print('6*e^(2/3)=', float(6*sp.E**(sp.Rational(2,3))))
