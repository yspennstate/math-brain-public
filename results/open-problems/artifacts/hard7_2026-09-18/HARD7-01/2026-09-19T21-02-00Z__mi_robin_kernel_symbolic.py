#!/usr/bin/env python3
import sympy as sp

x,y,z = sp.symbols("x y z")
a11,a22,a12,a13,a23 = sp.symbols("a11 a22 a12 a13 a23")
c11,c22,c12,c13,c23 = sp.symbols("c11 c22 c12 c13 c23")

theta = sp.Matrix([x,y,z])
r2 = sp.expand(theta.dot(theta))

A = sp.Matrix([
    [a11,a12,a13],
    [a12,a22,a23],
    [a13,a23,-a11-a22],
])
C = sp.Matrix([
    [c11,c12,c13],
    [c12,c22,c23],
    [c13,c23,-c11-c22],
])

a = sp.expand((theta.T*A*theta)[0])
q = sp.expand((theta.T*C*theta)[0])
X = A*theta-a*theta

# On S^2, grad_S q = 2(C theta-q theta).
gradS_q = 2*(C*theta-q*theta)
CA = sp.expand((theta.T*C*A*theta)[0])
grad_remainder = sp.factor(
    sp.expand(gradS_q.dot(X) - (2*CA-2*a*q))
)
expected_grad = sp.factor(2*(r2-1)*a*q)
assert sp.simplify(grad_remainder-expected_grad) == 0

# div_S X = tr((I-theta theta^T) DX) on S^2.
J = X.jacobian([x,y,z])
P = sp.eye(3)-theta*theta.T
divS = sp.expand(sp.trace(P*J))
div_remainder = sp.factor(sp.expand(divS+3*a))
expected_div = sp.factor(3*(r2-1)*a)
assert sp.simplify(div_remainder-expected_div) == 0

# Frobenius-orthonormal basis of trace-zero symmetric 3x3 matrices.
sqrt = sp.sqrt
basis = [
    sp.diag(1,-1,0)/sqrt(2),
    sp.diag(1,1,-2)/sqrt(6),
    sp.Matrix([[0,1,0],[1,0,0],[0,0,0]])/sqrt(2),
    sp.Matrix([[0,0,1],[0,0,0],[1,0,0]])/sqrt(2),
    sp.Matrix([[0,0,0],[0,0,1],[0,1,0]])/sqrt(2),
]
for i,E in enumerate(basis):
    assert sp.trace(E) == 0
    for j,F in enumerate(basis):
        target = 1 if i == j else 0
        assert sp.simplify(sp.trace(E.T*F)-target) == 0

sum_q2 = sp.factor(sum(sp.expand((theta.T*E*theta)[0])**2 for E in basis))
assert sp.simplify(sum_q2 - sp.Rational(2,3)*r2**2) == 0

print("HARD7-01 exact symbolic Robin-kernel identities")
print("CHECK_1 grad identity modulo sphere:", grad_remainder)
print("CHECK_2 div identity modulo sphere:", div_remainder)
print("CHECK_3 H2 evaluation-frame norm:", sum_q2)
print("ALL_EXACT_CHECKS_PASS = True")
