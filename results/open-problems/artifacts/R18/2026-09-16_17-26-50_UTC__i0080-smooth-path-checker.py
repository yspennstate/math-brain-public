#!/usr/bin/env python3
"""
R18 I0080 exact self-check for the smooth reparameterization of retained C007.
This is an AUTHOR SELF-CHECK, not an independent closure audit.
"""
import sympy as sp

t = sp.symbols("t", positive=True)
pi = sp.pi
ell = 100 + 95*pi*t
d = sp.Rational(19,20)
kappa = sp.Rational(8,5)
D = d/ell
b2 = pi*D*t
p = kappa/ell

assert sp.simplify(b2 - (sp.Rational(1,100) - 1/ell)) == 0
assert sp.simplify(b2/(pi*D) - t) == 0
# With a=D/b and b=sqrt(b2), source admissibility is a*pi*t=b.
assert sp.simplify((D/sp.sqrt(b2))*pi*t - sp.sqrt(b2)) == 0

# Exact positive gaps for t>0:
p_gap = sp.factor(sp.Rational(2,125) - p)
D_gap = sp.factor(sp.Rational(19,2000) - D)
b2_gap = sp.factor(sp.Rational(1,100) - b2)

print("R18 I0080 smooth C007 self-check")
print("ell(t) =", ell)
print("b^2 =", sp.factor(b2))
print("1/100 - b^2 =", b2_gap)
print("2/125 - p =", p_gap)
print("19/2000 - D =", D_gap)
print("b^2/(pi D)-t =", sp.simplify(b2/(pi*D)-t))
print("(D/sqrt(b^2))*pi*t-sqrt(b^2) =", sp.simplify((D/sp.sqrt(b2))*pi*t-sp.sqrt(b2)))
print("PASS")
