"""Exact symbolic checker for PROB20-07 run 2026-09-15T185528Z.

Verifies the two stop-loss identities used to exclude every nontrivial
three-type QSO 2-cycle with one unchanged coordinate when the coefficient
floor is at least 1/12.

Requires sympy only.  This file performs algebraic checks; it is not a
formal proof assistant certificate.
"""

import sympy as sp

# Symbols and midpoint/amplitude parametrization.
a, p, q, d = sp.symbols("a p q d", positive=True)
b = 1 - 3*a
r = 1 - p - q

x1, x2, x3 = p + d, q - d, r
y1, y2, y3 = p - d, q + d, r

Ux = [
    x1**2,
    2*x1*x2,
    2*x1*x3,
    x2**2,
    2*x2*x3,
    x3**2,
]
Uy = [
    y1**2,
    2*y1*y2,
    2*y1*y3,
    y2**2,
    2*y2*y3,
    y3**2,
]

A = [(y1-a)/b, (y2-a)/b, (y3-a)/b]
B = [(x1-a)/b, (x2-a)/b, (x3-a)/b]

# ------------------------------------------------------------------
# lambda = 1
# Under p>=q, positive source coordinates are 12,22,23.
# ------------------------------------------------------------------
source_lam1 = sp.factor(
    (Uy[1]-Ux[1]) + (Uy[3]-Ux[3]) + (Uy[4]-Ux[4])
)
target_lam1 = sp.factor(B[0]-A[0])

assert sp.simplify(source_lam1 - 4*d*(1-q)) == 0
assert sp.simplify(target_lam1 - 2*d/b) == 0

# The resulting midpoint cap is q <= c(a).
c = sp.factor(1 - 1/(2*b))
assert sp.simplify(c - (1-6*a)/(2*(1-3*a))) == 0

# ------------------------------------------------------------------
# lambda = u = y1/x1
# Source signs: 11 negative; 13 zero; 12,22,23,33 positive.
# Target signs under p>=q and r>=a: state 1 positive, state 2
# negative, state 3 nonnegative.
# ------------------------------------------------------------------
u = sp.factor(y1/x1)

source_terms = [sp.factor(Uy[i] - u*Ux[i]) for i in range(6)]
target_terms = [sp.factor(B[i] - u*A[i]) for i in range(3)]

assert sp.simplify(source_terms[0] + 2*d*(p-d)) == 0
assert sp.simplify(source_terms[2]) == 0
assert sp.simplify(target_terms[1] + 2*d*(a+p-q)/(b*(p+d))) == 0
assert sp.simplify(target_terms[2] - 2*d*(r-a)/(p+d)) == 0

source_u = sp.factor(sum(source_terms[i] for i in [1,3,4,5]))
target_u = sp.factor(target_terms[0] + target_terms[2])
slack_u = sp.factor(source_u - target_u)

expected_source_u = sp.factor(2*d*(1+p**2-d**2)/(p+d))
expected_target_u = sp.factor(2*d*(1+p-q-2*a)/(b*(p+d)))
expected_slack_u = sp.factor(
    2*d*(b*(p**2-d**2) - (p-q+a))/(b*(p+d))
)

assert sp.simplify(source_u - expected_source_u) == 0
assert sp.simplify(target_u - expected_target_u) == 0
assert sp.simplify(slack_u - expected_slack_u) == 0

# ------------------------------------------------------------------
# Endpoint scalar factorizations.
# ------------------------------------------------------------------
fac_left = sp.factor(b*c**2 - a)
fac_right = sp.factor(c - 4*a)

expected_left = -(4*a-1)*(12*a-1)/(4*(3*a-1))
expected_right = -(2*a-1)*(12*a-1)/(2*(3*a-1))

assert sp.simplify(fac_left - expected_left) == 0
assert sp.simplify(fac_right - expected_right) == 0

# Exact endpoint a=1/12: c=1/3 and both endpoint scalar bounds are zero.
a0 = sp.Rational(1,12)
assert sp.simplify(c.subs(a,a0) - sp.Rational(1,3)) == 0
assert sp.simpl(fac_left.subs(a,a0)) == 0
assert sp.simpl(fac_right.subs(a,a0)) == 0

# A concrete interior sanity point at the endpoint that passes the lambda=1
# midpoint cap still fails the lambda=u condition strictly.
vals = {
    a: a0,
    p: sp.Rational(2,5),
    q: sp.Rational(3,10),
    d: sp.Rational(1,50),
}
assert q.subs(vals) <= c.subs(vals)
assert sp.factor(
    (b*(p**2-d**2) - (p-q+a)).subs(vals)
) < 0

print("ALL EXACT CHECKS PASSED")
print("lambda=1 source positive mass:", source_lam1)
print("lambda=1 target positive mass:", target_lam1)
print("lambda=u stop-loss slack:", slack_u)
print("b*c(a)^2-a factor:", fac_left)
print("c(a)-4a factor:", fac_right)
