#!/usr/bin/env python3
"""Exact symbolic checks for the finite algebraic core of P04 Target 1.

No floating-point arithmetic is used.  This verifies the rank-two Woodbury
completion identities in the 2x2 leverage variables and the exact N=2n
normalization used by the full Lindeberg telescope.
"""
import sympy as sp

q11, q12, q22, e1, e2, n = sp.symbols(
    "q11 q12 q22 e1 e2 n", nonzero=True
)
Q = sp.Matrix([[q11, q12], [q12, q22]])
I = sp.eye(2)
A = (I + Q).inv()
e = sp.Matrix([e1, e2])

checks = {
    "I_minus_QA_minus_A": sp.simplify(I - Q * A - A),
    "AQA_plus_A2_minus_A": sp.simplify(A * Q * A + A * A - A),
    "scalar_completion_residual": sp.simplify(
        (e.T * (A * Q * A + A * A - A) * e)[0]
    ),
    "n_over_2N_when_N_eq_2n": sp.simplify(n / (2 * (2 * n))),
}

assert checks["I_minus_QA_minus_A"] == sp.zeros(2)
assert checks["AQA_plus_A2_minus_A"] == sp.zeros(2)
assert checks["scalar_completion_residual"] == 0
assert checks["n_over_2N_when_N_eq_2n"] == sp.Rational(1, 4)

print("EXACT_SYMBOLIC_CHECK=PASS")
for key, value in checks.items():
    print(f"{key}={value}")
print("Interpretation: the minimized restored-block increment is (1/(2N))*e^T*A*e,")
print("and n=N/2 blocks convert an unscaled K/sqrt(d) bracket discrepancy to K/(4*sqrt(d)).")
