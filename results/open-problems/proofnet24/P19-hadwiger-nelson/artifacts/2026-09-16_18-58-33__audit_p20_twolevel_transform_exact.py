#!/usr/bin/env python3
"""Independent exact algebra audit for P20-I0081-TWOLEVEL-TRANSFORM-04.

Audited report:
proofnet24/P20-closure-log-unimodality/runs/2026-09-16/2026-09-16_18-40-47__run-report.md
Creation commit 9fa714dbddadb44c6fb837688d1ce69d525fb7fe
Blob f138c86333ee2b3d70bb49402bac54ab5b469bb8

Scope: exact normalization/decomposition of the two-level log-density, the antiderivative
leading to F_X(z), and the algebraic eta identity. This does NOT audit P20's physical-branch,
interval-root, regularity, or four-mode conclusions.
"""
from fractions import Fraction
import sympy as sp

# Exact two-level density decomposition.
# h = 1/24 on |y|<=8 and 1/36 on 8<|y|<=14.
# Equivalent: h = 1/72 * 1[-8,8] + 1/36 * 1[-14,14].
assert Fraction(1,72) + Fraction(1,36) == Fraction(1,24)
assert Fraction(1,36) == Fraction(1,36)
assert 16*Fraction(1,24) + 12*Fraction(1,36) == 1

# Direct symbolic differentiation of the t-antiderivative after t=e^u:
# integral du/(1-z e^u) = integral dt/[t(1-z t)].
t, z = sp.symbols('t z', nonzero=True)
A = sp.log(t) - sp.log(1-z*t)
assert sp.simplify(sp.diff(A,t) - 1/(t*(1-z*t))) == 0

# Endpoint evaluation gives F_X = 2X - log(1-z e^X)+log(1-z e^-X).
# Verify algebraically with E standing for e^X (so e^-X=1/E).
E = sp.symbols('E', positive=True, nonzero=True)
X = sp.symbols('X', real=True)
endpoint = (X - sp.log(1-z*E)) - (-X - sp.log(1-z/E))
claimed = 2*X - sp.log(1-z*E) + sp.log(1-z/E)
assert sp.simplify(endpoint - claimed) == 0

# Weighting of F_8 and F_14 from the indicator decomposition.
# integral h(u)/(1-ze^u) du = (1/72)F_8 +(1/36)F_14 = (F_8+2F_14)/72.
F8, F14 = sp.symbols('F8 F14')
weighted = sp.Rational(1,72)*F8 + sp.Rational(1,36)*F14
assert sp.simplify(weighted - (F8+2*F14)/72) == 0

# eta = psi/(1+psi), psi=M-1, hence eta=1-1/M.
M = sp.symbols('M', nonzero=True)
psi = M-1
eta = sp.simplify(psi/(1+psi))
assert sp.simplify(eta - (1-1/M)) == 0

print('normalization', 16*Fraction(1,24) + 12*Fraction(1,36))
print('indicator_inner_height', Fraction(1,72)+Fraction(1,36))
print('indicator_outer_height', Fraction(1,36))
print('antiderivative_derivative_check PASS')
print('endpoint_FX_formula_check PASS')
print('M_weighting_check PASS')
print('eta_identity_check PASS')
print('CLAIM P19-AUDIT-P20-TWOLEVEL-TRANSFORM-15 PASS')
print('AUDIT_SCOPE exact transform/algebra only; physical branch and four-mode theorem NOT audited')
print('ALL_EXACT_CHECKS_PASSED')
