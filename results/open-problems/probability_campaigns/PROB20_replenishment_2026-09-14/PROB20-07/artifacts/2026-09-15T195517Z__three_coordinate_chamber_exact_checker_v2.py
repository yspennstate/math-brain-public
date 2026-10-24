"""Corrected exact symbolic checker for PROB20-07 run 2026-09-15T195517Z.

The first archived checker used one direct SymPy structural-equality assertion
for an algebraically identical rational polynomial. That assertion did not fire
because of expression representation, not because the mathematical identity
failed. This v2 uses simplify() for equality tests and was executed locally to
completion before upload.

Requires sympy only.
"""

import sympy as sp

a, S, X, Y, u = sp.symbols("a S X Y u", positive=True)
b = 1 - 3*a

F = sp.factor(S - a - b*(1 + S**2/4))
F_left = sp.factor(F.subs(S, 1/b))
F_right = sp.factor(F.subs(S, 2*(1 - 2*a)))

assert sp.simplify(
    F_left - (24*a**2 - 20*a + 1)/(4*(3*a - 1))
) == 0
assert sp.simplify(
    F_right - a*(2*a - 1)*(6*a - 5)
) == 0

roots = sp.solve(sp.Eq(24*a**2 - 20*a + 1, 0), a)
assert roots == [sp.Rational(5,12) - sp.sqrt(19)/12,
                 sp.sqrt(19)/12 + sp.Rational(5,12)]

a0 = sp.Rational(1,12)
assert sp.factor(F_left.subs(a, a0)) == sp.Rational(1,6)
assert sp.factor(F_right.subs(a, a0)) == sp.Rational(5,16)

Yxu = X - u
r1 = Yxu/X
source_r1 = sp.factor((1 - r1)*(1 + X*Yxu))
target1_r1 = sp.factor(((X - a) - r1*(Yxu - a))/b)
assert sp.simplify(source_r1 - u*(1 + X*Yxu)/X) == 0
assert sp.simplify(target1_r1 - u*(X + Yxu - a)/(b*X)) == 0

source_tv = sp.factor(X**2 - Y**2)
target_tv = sp.factor((X - Y)/b)
assert sp.simplify(source_tv - (X - Y)*(X + Y)) == 0
assert sp.simplify(target_tv - (X - Y)/b) == 0

B_gap = sp.factor(
    S/2 + sp.Rational(1,2)
    - sp.Rational(3,4)*(1 + S**2/4)
)
assert sp.simplify(B_gap + (3*S - 2)*(S - 2)/16) == 0

late_gap = sp.factor(
    S - sp.Rational(1,12)
    - sp.Rational(3,4)*(1 + S**2/4)
)
assert sp.simplify(late_gap + (9*S**2 - 48*S + 40)/48) == 0
late_roots = sp.solve(sp.Eq(9*S**2 - 48*S + 40, 0), S)
assert late_roots == [sp.Rational(8,3) - 2*sp.sqrt(6)/3,
                      2*sp.sqrt(6)/3 + sp.Rational(8,3)]

support_cross = sp.factor(X**2*(Y-a) - Y**2*(X-a))
assert sp.simplify(
    support_cross - (X-Y)*(X*Y - a*(X+Y))
) == 0

print("ALL EXACT SYMBOLIC CHECKS PASSED")
print("F_left =", F_left)
print("F_right =", F_right)
print("B_gap =", B_gap)
print("late_gap =", late_gap)
print("support_cross =", support_cross)
