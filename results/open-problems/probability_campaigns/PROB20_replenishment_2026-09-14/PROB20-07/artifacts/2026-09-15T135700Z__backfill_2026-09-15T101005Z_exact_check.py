"""Recovered exact symbolic checks from PROB20-07 run 2026-09-15T101005Z.

Recovery provenance: authored in the completed run but the artifacts directory was absent on bounded GitHub retrieval during the 2026-09-15 backfill. This file preserves that checker; it is not evidence of an earlier GitHub commit.

Checks:
1. one-parameter two-cycle family and strict 1/12 lower-bound limit;
2. rational s=1/30 certificate;
3. exact two-step Fisher expansion witness at floor a=21/250>1/12.

Requires sympy only.
"""

import sympy as sp

s = sp.symbols("s", positive=True)
t = (1 - 9*s**2) / (12 - 27*s**2)
A = (20 - 99*s**2) / (6*(4 - 9*s**2))
B = (63*s**2 + 2) / (6*(4 - 9*s**2))

assert sp.simplify(A + B + t - 1) == 0
assert sp.simplify((sp.Rational(1,12) - t) - 9*s**2/(4*(4 - 9*s**2))) == 0
assert sp.simplify((A - t) - 3*(2 - 9*s**2)/(2*(4 - 9*s**2))) == 0
assert sp.simplify((B - t) - 27*s**2/(2*(4 - 9*s**2))) == 0
assert sp.simplify((1 - 3*t) - 3/(4 - 9*s**2)) == 0

x = sp.Matrix([
    sp.Rational(1,3) + s,
    sp.Rational(1,3) - s,
    sp.Rational(1,3),
])

rows = {
    (0,0): sp.Matrix([t, 1 - 2*t, t]),
    (0,1): sp.Matrix([t, t, 1 - 2*t]),
    (0,2): sp.Matrix([t, A, B]),
    (1,1): sp.Matrix([1 - 2*t, t, t]),
    (1,2): sp.Matrix([A, t, B]),
    (2,2): sp.Matrix([t, t, 1 - 2*t]),
}

V = sp.zeros(3, 1)
for i in range(3):
    for j in range(3):
        V += x[i]*x[j]*rows[tuple(sorted((i,j)))]

target = sp.Matrix([x[1], x[0], x[2]])
assert all(sp.simplify(V[k] - target[k]) == 0 for k in range(3))

subs = {s: sp.Rational(1,30)}
assert sp.simplify(t.subs(subs)) == sp.Rational(11,133)
assert sp.simplify(A.subs(subs)) == sp.Rational(221,266)
assert sp.simplify(B.subs(subs)) == sp.Rational(23,266)
assert sp.simplify((1 - 2*t).subs(subs)) == sp.Rational(111,133)
assert sp.Rational(11,133) > sp.Rational(1,13)

# Two-step Fisher witness. Residual deterministic rule:
# 11,12,13 -> child 1; 22 -> child 2; 23,33 -> child 3.
a = sp.Rational(21,250)
b = 1 - 3*a
assert a > sp.Rational(1,12)

x1 = sp.Rational(3,20)
x2 = sp.Rational(1,10)
x3 = 1 - x1 - x2
assert min(x1, x2, x3) > a

h1 = sp.Integer(-10)
h2 = sp.Integer(1)
h3 = -h1 - h2

def V2(v1, v2):
    y1 = a + b*(2*v1 - v1**2)
    y2 = a + b*v2**2
    y3 = 1 - y1 - y2
    return sp.factor(y1), sp.factor(y2), sp.factor(y3)

def J2(v1, v2):
    return sp.Matrix([
        [2*b*(1 - v1), 0],
        [0, 2*b*v2],
    ])

y = V2(x1, x2)
z = V2(y[0], y[1])
out12 = J2(y[0], y[1]) * J2(x1, x2) * sp.Matrix([h1, h2])
out3 = -(out12[0] + out12[1])

input_fisher_sq = sp.factor(h1**2/x1 + h2**2/x2 + h3**2/x3)
output_fisher_sq = sp.factor(out12[0]**2/z[0] + out12[1]**2/z[1] + out3**2/z[2])
ratio = sp.factor(output_fisher_sq/input_fisher_sq)

expected_ratio = sp.Rational(
    43032428053871146674182064894745224411789503,
    42348093240878655419656833460688026367187500,
)
assert ratio == expected_ratio
assert ratio > 1

print("ALL EXACT CHECKS PASSED")
print("lower witness min coefficient at s=1/30:", t.subs(subs))
print("two-step Fisher floor a:", a)
print("two-step squared Fisher ratio:", ratio)
print("ratio - 1:", sp.factor(ratio - 1))
