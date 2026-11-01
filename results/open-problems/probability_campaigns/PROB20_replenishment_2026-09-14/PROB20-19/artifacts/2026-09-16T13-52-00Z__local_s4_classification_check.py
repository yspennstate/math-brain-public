#!/usr/bin/env python3
"""
PROB20-19 local S4 normal-form classification checker.

This is a symbolic consistency checker for the analytic proof in the
2026-09-16 local critical-set classification checkpoint. It does not prove
analyticity or the neighborhood estimates; those are proved in the report.
"""

import sympy as sp

# Generic invariant-gradient coefficients:
# grad_i = A z_i + B z_i^2 + C z_i^3
x, y, r, s, t = sp.symbols("x y r s t")
A, B, C = sp.symbols("A B C")

diff = sp.factor(
    (A*x + B*x**2 + C*x**3) -
    (A*y + B*y**2 + C*y**3)
)
expected_diff = (x-y)*(A + B*(x+y) + C*(x**2+x*y+y**2))
assert sp.expand(diff - expected_diff) == 0

Qrs = A + B*(r+s) + C*(r**2+r*s+s**2)
Qrt = A + B*(r+t) + C*(r**2+r*t+t**2)
triple = sp.factor(Qrs - Qrt)
expected_triple = (s-t)*(B + C*(r+s+t))
assert sp.expand(triple - expected_triple) == 0

# Basic invariants on E={sum z_i=0}: q2,q3,q4.
# Newton identities: e2=-q2/2, e3=q3/3, e4=q2^2/8-q4/4.
q2, q3, q4 = sp.symbols("q2 q3 q4")
e2 = -q2/2
e3 = q3/3
e4 = q2**2/8 - q4/4
assert sp.simplify(q2 + 2*e2) == 0
assert sp.simplify(q3 - 3*e3) == 0
assert sp.simplify(q4 + e2*q2 + 4*e4) == 0

sqrt3 = sp.sqrt(3)
h31 = [sp.Rational(3,1)/(2*sqrt3),
       -sp.Rational(1,1)/(2*sqrt3),
       -sp.Rational(1,1)/(2*sqrt3),
       -sp.Rational(1,1)/(2*sqrt3)]
h22 = [sp.Rational(1,2), sp.Rational(1,2),
       -sp.Rational(1,2), -sp.Rational(1,2)]

def pk(v, k):
    return sp.simplify(sum(a**k for a in v))

assert pk(h31, 2) == 1
assert pk(h22, 2) == 1
assert pk(h31, 3) == sqrt3/3
assert pk(h22, 3) == 0
assert pk(h31, 4) == sp.Rational(7,12)
assert pk(h22, 4) == sp.Rational(1,4)

a = sp.symbols("a")
c3_from_invariant = sp.simplify(6*a*pk(h31,3))
assert c3_from_invariant == 2*sqrt3*a

print("PASS invariant-gradient pair factorization:")
print("  grad_i-grad_j =", diff)
print("PASS three-distinct-level subtraction:")
print("  Q(r,s)-Q(r,t) =", triple)
print("  Therefore distinct r,s,t require B + C(r+s+t)=0.")
print("PASS Newton generator identities on sum-zero hyperplane.")
print("PASS axis invariants:")
print("  q2(h31) =", pk(h31,2))
print("  q3(h31) =", pk(h31,3))
print("  q4(h31) =", pk(h31,4))
print("  q2(h22) =", pk(h22,2))
print("  q3(h22) =", pk(h22,3))
print("  q4(h22) =", pk(h22,4))
print("PASS cubic coefficient relation:")
print("  c3 = 6*a*q3(h31) =", c3_from_invariant)
print("ALL SYMBOLIC CHECKS PASSED")
