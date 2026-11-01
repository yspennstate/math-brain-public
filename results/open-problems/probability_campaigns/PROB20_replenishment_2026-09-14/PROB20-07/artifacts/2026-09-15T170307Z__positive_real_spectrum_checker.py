"""
Exact algebra checker for PROB20-07 run 2026-09-15T170307Z.

Checks:
1. Case I call differences in the positive-real endpoint proof.
2. Case II u=0 and u=1 contradictions.
3. The unique positive endpoint tensor fixes the barycentre and has tangent multiplier +1
   in score direction (-1,0,1).
"""

import sympy as sp

a = sp.Rational(1,12)
b = sp.Rational(3,4)

v, w = sp.symbols("v w", real=True)

# Case I after p=1/3, rho=1:
# q(w-v)=2w/3-1/3.
source_c1 = (1+w)/9 + sp.Rational(2,3)*(sp.Rational(2,3)*w-sp.Rational(1,3))
target_c1 = sp.Rational(1,9) + w/3
diff_c1 = sp.factor(sp.simplify(source_c1-target_c1))
assert sp.simplify(diff_c1 - 2*(w-1)/9) == 0

source_c2 = (1+v)/9
target_c2 = sp.Rational(1,9) + v/3
diff_c2 = sp.factor(sp.simplify(source_c2-target_c2))
assert sp.simplify(diff_c2 + 2*v/9) == 0

# Case II, u=0 equality subcase.
c = sp.symbols("c", positive=True)
q_expr = sp.Rational(2,3) - 1/(3*c)
source_u0 = 2*q_expr*c/3 + (1+c)/9
target_u0 = sp.Rational(1,9) + c/3
diff_u0 = sp.factor(sp.simplify(source_u0-target_u0))
assert sp.simplify(diff_u0 - 2*(c-1)/9) == 0

# Case II, u=1 equality subcase.
source_u1 = sp.Rational(1,6)
target_u1 = (
    sp.Rational(1,3)
    - sp.Rational(1,2)*(sp.Rational(1,3)-2*a)
) / b
assert sp.simplify(target_u1-sp.Rational(1,3)) == 0
assert sp.simplify(source_u1-target_u1 + sp.Rational(1,6)) == 0

# Positive endpoint tensor.
P = {
    (0,0): sp.Matrix([sp.Rational(5,6), a, a]),
    (0,1): sp.Matrix([sp.Rational(5,6), a, a]),
    (0,2): sp.Matrix([a, sp.Rational(5,6), a]),
    (1,1): sp.Matrix([a, sp.Rational(5,6), a]),
    (1,2): sp.Matrix([a, a, sp.Rational(5,6)]),
    (2,2): sp.Matrix([a, a, sp.Rational(5,6)]),
}

x = sp.Matrix([sp.Rational(1,3)]*3)
Vx = sp.zeros(3,1)
for i in range(3):
    for j in range(3):
        Vx += x[i]*x[j]*P[tuple(sorted((i,j)))]

assert all(sp.simplify(Vx[k]-x[k]) == 0 for k in range(3))

J = sp.zeros(3,3)
for k in range(3):
    for ell in range(3):
        for j in range(3):
            J[k,ell] += 2*x[j]*P[tuple(sorted((ell,j)))][k]

h = sp.Matrix([-sp.Rational(1,3), 0, sp.Rational(1,3)])
assert all(sp.simplify((J*h-h)[k]) == 0 for k in range(3))

print("ALL EXACT ALGEBRA CHECKS PASSED")
print("Case I c=1-w source-target:", diff_c1)
print("Case I c=1-v source-target:", diff_c2)
print("Case II u=0 source-target:", diff_u0)
print("Case II u=1 source,target:", source_u1, target_u1)
print("Endpoint Jacobian:")
sp.pprint(J)
