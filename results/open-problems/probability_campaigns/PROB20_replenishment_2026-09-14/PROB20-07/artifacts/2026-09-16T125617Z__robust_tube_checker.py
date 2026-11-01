#!/usr/bin/env python3
"""Exact symbolic/rational checker for PROB20-07 run 2026-09-16T125617Z.

Checks the quantitative robust-tube theorem around the trimmed neutral triangle:
- scalar contraction-factor expansions;
- exact neutral-triangle Jacobian;
- Lyapunov perturbation constant 227/32;
- local base-bound algebra;
- global-entry radius simplification;
- exact eta=1/4 numerical certificate.

The universal theorem is analytic; this script checks its algebraic constants.
"""
from fractions import Fraction
import sympy as sp

eta = sp.symbols('eta', positive=True)
t = sp.symbols('t', nonnegative=True)
u, v, lam, kap = sp.symbols('u v lam kap', real=True)

qrad = t**2 * (8 - 3*t) / 5
qedge = (81 + 175*t**2) / 256

assert sp.simplify(
    sp.expand(qrad.subs(t, 1-eta))
    - (1 - sp.Rational(7,5)*eta - sp.Rational(1,5)*eta**2
       + sp.Rational(3,5)*eta**3)
) == 0

assert sp.simplify(
    sp.expand(qedge.subs(t, 1-eta))
    - (1 - sp.Rational(175,128)*eta + sp.Rational(175,256)*eta**2)
) == 0

alpha = u * (4 + 3*v) / 4
beta = -sp.Rational(3,8) * (u**2 - 3*v**2)
G = sp.Matrix([lam*kap*alpha, lam*beta])
J = sp.simplify(G.jacobian([u, v]))
J_expected = sp.Matrix([
    [lam*kap*(1 + sp.Rational(3,4)*v), sp.Rational(3,4)*lam*kap*u],
    [-sp.Rational(3,4)*lam*u, sp.Rational(9,4)*lam*v],
])
assert all(sp.simplify(z) == 0 for z in list(J - J_expected))

C = 2*sp.Rational(21,8) + sp.Rational(59,32)
assert C == sp.Rational(227,32)

R, q = sp.symbols('R q', positive=True)
r = sp.Rational(5,8) * R**2
global_radius = sp.simplify((1-q)*r / (2*C))
assert sp.simplify(
    global_radius - sp.Rational(10,227)*(1-q)*R**2
) == 0

# Local first-row margin identity:
# (1-eta)(1+eta/2) <= 1-eta/2.
assert sp.simplify(
    sp.expand((1-eta)*(1+eta/2) - (1-eta/2)) + eta**2/2
) == 0

# Exact eta = 1/4 example.
E = Fraction(1,4)
Rf = min(Fraction(1,8), E/Fraction(3,1))

def qr(z):
    return z*z*(8-3*z)/5

def qe(z):
    return (81 + 175*z*z)/256

qrf = qr(1-E)
qef = qe(1-E)
qf = max(qrf, qef)
e1 = E/Fraction(48,1)
e2 = E*Rf/Fraction(8,1)
e3 = Fraction(10,227)*(1-qf)*Rf*Rf

assert Rf == Fraction(1,12)
assert qrf == Fraction(207,320)
assert qef == Fraction(2871,4096)
assert qf == Fraction(2871,4096)
assert 1-qf == Fraction(1225,4096)
assert e1 == Fraction(1,192)
assert e2 == Fraction(1,384)
assert e3 == Fraction(6125,66945024)
assert e3 < e2 < e1

print('ALL EXACT ROBUST-TUBE CHECKS PASSED')
print('qrad(1-eta) =', sp.expand(qrad.subs(t, 1-eta)))
print('qedge(1-eta) =', sp.expand(qedge.subs(t, 1-eta)))
print('Jacobian =', J)
print('global Lyapunov perturbation constant =', C)
print('eta=1/4: R =', Rf)
print('eta=1/4: qrad =', qrf)
print('eta=1/4: qedge =', qef)
print('eta=1/4: q =', qf)
print('eta=1/4: epsilon =', e3, float(e3))
