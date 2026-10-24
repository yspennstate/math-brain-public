"""Exact symbolic checks for PROB20-07 run 2026-09-15T151042Z.

Checks the algebra used in the theorem that a fixed-point tangent eigenvalue
mu <= -1 with one zero tangent coordinate cannot occur above floor 1/12.
Requires sympy only.
"""

import sympy as sp

a = sp.symbols("a", positive=True)
b = 1 - 3*a
c = 1 - 1/(2*b)
r0 = sp.sqrt(a/b)
r = sp.symbols("r", positive=True)
L = r + a - b*r**2

assert sp.simplify(c - (1-6*a)/(2*(1-3*a))) == 0
assert sp.simplify((a/b) - c**2 + (4*a-1)*(12*a-1)/(4*(3*a-1)**2)) == 0
assert sp.simplify(L.subs(r, r0) - r0) == 0

rend = 1 - 2*a
Dend = sp.factor(L.subs(r, rend) - c)
expected = (72*a**4 - 120*a**3 + 68*a**2 - 18*a + 1)/(2*(3*a - 1))
assert sp.simplify(Dend - expected) == 0

N = 72*a**4 - 120*a**3 + 68*a**2 - 18*a + 1
H = 144*a**3 - 180*a**2 + 68*a - 9
assert sp.simplify(sp.diff(N,a) - 2*H) == 0
assert sp.factor(N.subs(a, sp.Rational(1,12))) == -sp.Rational(3,32)
assert sp.factor(H.subs(a, sp.Rational(1,6))) == -2
assert sp.simplify(sp.diff(H,a) - 4*(108*a**2 - 90*a + 17)) == 0

ae = sp.Rational(1,12)
assert sp.factor(c.subs(a,ae)) == sp.Rational(1,3)
assert sp.factor((a/b).subs(a,ae)) == sp.Rational(1,9)
assert sp.simplify(L.subs(a,ae)-sp.Rational(1,3) - (3*r-1)*(1-r)/4) == 0

print("ALL EDGE-DIRECTION SYMBOLIC CHECKS PASSED")
print("c(a) =", sp.factor(c))
print("r0^2-c^2 =", sp.factor(a/b-c**2))
print("L(1-2a)-c =", Dend)
print("endpoint L(r)-1/3 =", sp.factor(L.subs(a,ae)-sp.Rational(1,3)))
