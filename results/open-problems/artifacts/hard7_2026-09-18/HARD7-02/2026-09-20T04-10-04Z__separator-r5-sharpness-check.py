#!/usr/bin/env python3
"""Exact symbolic self-check for HARD7-02 separator-recursion sharpness.

This checks the 2x2 Schur-complement family used in the corresponding run report:

    M_R = [[R^{-1}, 1], [1, R + R^{-3}]].

With A=R^{-1}, B=C=1, the Schur complement is S=R^{-3}.  Thus the
child inverse scale is R and the Schur inverse scale is R^3, while the
full inverse has an entry R^5+R.  Consequently the R^5 exponent in the
bare deterministic block-inverse bookkeeping cannot be improved from
only these norm hypotheses.

All identities are symbolic over Q(R); no floating-point arithmetic is used.
"""
import sympy as sp

R = sp.symbols("R", positive=True)
A = R**-1
B = C = sp.Integer(1)
D = R + R**-3
M = sp.Matrix([[A, B], [C, D]])
S = sp.simplify(D - C * A**-1 * B)
Minv = sp.simplify(M.inv())

checks = [
    sp.simplify(S - R**-3) == 0,
    sp.simplify(M.det() - R**-4) == 0,
    sp.simplify(Minv[0, 0] - (R**5 + R)) == 0,
    sp.simplify(Minv[0, 1] + R**4) == 0,
    sp.simplify(Minv[1, 0] + R**4) == 0,
    sp.simplify(Minv[1, 1] - R**3) == 0,
]

print("HARD7-02 exact Schur-sharpness self-check")
print("Schur complement =", S)
print("det(M) =", sp.factor(M.det()))
print("M^{-1} =")
print(Minv)
print("entry_11_minus_(R^5+R) =", sp.simplify(Minv[0, 0] - (R**5 + R)))
print("entry_12_plus_R^4 =", sp.simplify(Minv[0, 1] + R**4))
print("entry_22_minus_R^3 =", sp.simplify(Minv[1, 1] - R**3))
print("R=2 det =", sp.factor(M.det().subs(R, 2)), " inverse =", Minv.subs(R, 2))
print("ALL_EXACT_CHECKS_PASS =", all(checks))
