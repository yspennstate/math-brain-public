#!/usr/bin/env python3
"""Exact self-check for P15-I0066-BLOCK-LYAPUNOV-05.

Uses exact SymPy rationals only. Verifies the concrete p=4, d=2, m=2
matrix block has noncommuting drift/noise and the claimed coercive
p-homogeneous Lyapunov identity.
"""
import sympy as sp

x, y = sp.symbols("x y", real=True)
z = sp.Matrix([x, y])
M = sp.Matrix([[2, 0], [0, 3]])
C1 = sp.Matrix([[0, -1], [1, 0]])
C2 = sp.Rational(1, 2) * sp.Matrix([[1, 0], [0, -1]])

V = (x*x + y*y)**2
grad = sp.Matrix([sp.diff(V, x), sp.diff(V, y)])
H = sp.hessian(V, (x, y))

def hess_term(C):
    w = C*z
    return sp.expand((w.T * H * w)[0])

drift = sp.expand((grad.T * M * z)[0])
noise_hess = sp.expand(sp.Rational(1, 2) * (hess_term(C1) + hess_term(C2)))
lyap = sp.expand(drift - noise_hess)
target = sp.expand(
    sp.Rational(9, 2) * (x*x + y*y)**2
    + 4*y*y*(2*x*x + y*y)
)

comm_M_C1 = M*C1 - C1*M
comm_C1_C2 = C1*C2 - C2*C1

assert comm_M_C1 != sp.zeros(2)
assert comm_C1_C2 != sp.zeros(2)
assert sp.expand(lyap - target) == 0
assert sp.factor(lyap - sp.Rational(9, 2)*(x*x+y*y)**2) == 4*y*y*(2*x*x+y*y)

print("M =", M.tolist())
print("C1 =", C1.tolist())
print("C2 =", C2.tolist())
print("[M,C1] =", comm_M_C1.tolist())
print("[C1,C2] =", comm_C1C2.tolist())
print("DV[Mz] =", drift)
print("(1/2) sum D2V[C_j z,C_j z] =", noise_hess)
print("LYAPUNOV_POLYNOMIAL =", lyap)
print("COERCIVITY_RESIDUAL =", sp.factor(lyap - sp.Rational(9, 2)*(x*x+y*y)**2))
print("COERCIVITY_CONSTANT = 9/2")
print("ALL_EXACT_CHECKS_PASSED")
