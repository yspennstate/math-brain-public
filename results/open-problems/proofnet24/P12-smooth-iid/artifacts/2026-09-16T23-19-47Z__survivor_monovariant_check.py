#!/usr/bin/env python3
"""Exact symbolic check for the P12 survivor-state audit normal form.

This is an audit checker, not a new theorem generator.  It verifies only the
algebraic recurrence normalization and the source-scale powers recorded in the
2026-09-16T23-19-47Z P12 run report.
"""
import sympy as sp

c, C, p, m = sp.symbols("c C p m", positive=True)
a = sp.symbols("a", real=True)
E, B, M = sp.symbols("E B M", positive=True)
j = sp.symbols("j", integer=True, nonnegative=True)

# Worst-case equalities corresponding to the one-step inequalities
# M' >= c p M, E' <= C m^a p^2 E, B' <= C p B.
Mp = c*p*M
Ep = C*m**a*p**2*E
Bp = C*p*B

medium_multiplier = sp.simplify((Ep/Mp**2)/(E/M**2))
bad_multiplier = sp.simplify((Bp/Mp**2)/(B/M**2))
assert medium_multiplier == C*m**a/c**2
assert bad_multiplier == C/(c**2*p)

Rj = (c**2/(C*m**a))**j * E/M**2
Rj1 = sp.simplify((c**2/(C*m**a))**(j+1) * Ep/Mp**2)
Sj = (c**2*p/C)**j * B/M**2
Sj1 = sp.simplify((c**2*p/C)**(j+1) * Bp/Mp**2)
assert sp.simplify(Rj1/Rj) == 1
assert sp.simplify(Sj1/Sj) == 1

k, lam, mm = sp.symbols("k lam mm", positive=True)
s_complex = k**sp.Rational(-1, 2) * sp.exp(-lam*mm/(2*k))
p_complex = sp.simplify(s_complex**2)
s_real = k**sp.Rational(-1, 2) * sp.exp(-lam*mm/k)
p_real = s_real

assert sp.simplify(p_complex**k - sp.exp(-lam*mm)/k**k) == 0
assert sp.simplify(p_real**k - sp.exp(-lam*mm)/k**(k/2)) == 0

print("medium_multiplier = C*m**a/c**2")
print("bad_multiplier = C/(c**2*p)")
print("adjusted_medium_next/current = 1")
print("adjusted_bad_next/current = 1")
print("complex p^k = exp(-lambda*m)/k^k")
print("real p^k = exp(-lambda*m)/k^(k/2)")
print("complex log(p^{-k}) = lambda*m + k*log(k)")
print("real log(p^{-k}) = lambda*m + (k/2)*log(k)")
print("P12-SURVIVOR-MONOVARIANT-EXACT-CHECK: PASS")
