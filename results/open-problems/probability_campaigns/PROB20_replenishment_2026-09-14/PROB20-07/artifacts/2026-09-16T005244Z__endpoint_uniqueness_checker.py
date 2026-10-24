#!/usr/bin/env python3
"""
Exact symbolic checker for PROB20-07 run 2026-09-16T005244Z.

Checks the exceptional weak-endpoint tensor from the archived positive-real
spectral rigidity theorem:
  * the barycentre is a fixed point;
  * its tangent derivative has eigenvalues 1 and 0;
  * the simplex fixed-point equations eliminate to
        (3*x-1)^3 (9*x+1) = 0,
    hence the only simplex fixed point is the barycentre.

This checks algebra only; the Brouwer-degree argument in the report is
topological and is not reduced to symbolic computation.
"""
import sympy as sp

x, y = sp.symbols("x y", real=True)
z = 1 - x - y
a = sp.Rational(1, 12)
b = sp.Rational(3, 4)

# Exceptional tensor residual Q:
# Q11=Q12=e1, Q13=Q22=e2, Q23=Q33=e3.
V1 = a + b*(x**2 + 2*x*y)
V2 = a + b*(2*x*z + y**2)
V3 = a + b*(2*y*z + z**2)

# Simplex preservation in affine coordinates.
assert sp.simplify(V1 + V2 + V3 - 1) == 0

# Barycentre fixed.
subs_bar = {x: sp.Rational(1,3), y: sp.Rational(1,3)}
assert sp.simplify(V1.subs(subs_bar) - sp.Rational(1,3)) == 0
assert sp.simplify(V2.subs(subs_bar) - sp.Rational(1,3)) == 0
assert sp.simplify(V3.subs(subs_bar) - sp.Rational(1,3)) == 0

# Tangent derivative in affine coordinates (x1,x2), x3=1-x1-x2.
M = sp.Matrix([V1, V2]).jacobian([x,y]).subs(subs_bar)
lam = sp.symbols("lam")
char = sp.factor(M.charpoly(lam).as_expr())
assert sp.simplify(char - lam*(lam-1)) == 0

# Exact elimination of the first two fixed-point equations.
f1 = sp.expand(V1 - x)
f2 = sp.expand(V2 - y)
G = sp.groebner([f1, f2], y, x, order="lex")
basis = [sp.factor(p.as_expr()) for p in G.polys]
assert len(basis) == 2

g_y = sp.expand(basis[0])
g_x = sp.factor(basis[1])

expected_gx = sp.factor((3*x-1)**3*(9*x+1)/sp.Integer(243))
assert sp.simplify(g_x - expected_gx) == 0

expected_gy = sp.expand(y + sp.Rational(27,2)*x**3 - 12*x**2 + sp.Rational(7,2)*x - sp.Rational(2,3))
assert sp.simplify(g_y - expected_gy) == 0

# The only affine algebraic candidates and their simplex status.
y_from_x = sp.Rational(2,3) - sp.Rational(27,2)*x**3 + 12*x**2 - sp.Rational(7,2)*x
candidates = []
for xv in [sp.Rational(1,3), sp.Rational(-1,9)]:
    yv = sp.simplify(y_from_x.subs(x, xv))
    zv = sp.simplify(1-xv-yv)
    candidates.append((xv,yv,zv))
    assert sp.simplify(V1.subs({x:xv,y:yv})-xv) == 0
    assert sp.simplify(V2.subs({x:xv,y:yv})-yv) == 0
    assert sp.simplify(V3.subs({x:xv,y:yv})-zv) == 0

assert candidates[0] == (sp.Rational(1,3),)*3
assert candidates[1] == (sp.Rational(-1,9), sp.Rational(11,9), sp.Rational(-1,9))
assert all(v >= 0 for v in candidates[0])
assert not all(v >= 0 for v in candidates[1])

print("Exceptional tensor tangent matrix:", M)
print("Affine algebraic fixed-point candidates:", candidates)
print("ALL EXACT ENDPOINT UNIQUENESS CHECKS PASSED")
