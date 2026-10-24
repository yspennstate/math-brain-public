#!/usr/bin/env python3
"""
Exact symbolic self-check for HARD7-02 final-recovery run.

This checker verifies only finite-dimensional algebra used in the report:
(1) the one-child positive joint-resolvent overlap recursion;
(2) the corresponding same-sign (physical Schur-susceptibility) recursion;
(3) the quadratic block-determinant coefficient
    d/d(t^2) log det([[H_+,tI],[tI,H_-]]-i eta I)|_{t=0}
    = -Tr(R_- R_+);
(4) the endpoint H_+=H_- Ward identity Z=q/eta.

It is a self-check, not an independent proof of the PWIT limit, the
infinite-tree strict-coherence theorem, or eta->0 Hermitization.
"""
import sympy as sp

a, b, eta, t = sp.symbols("a b eta t", positive=True, real=True)
I = sp.I
I2 = sp.eye(2)

Hp = sp.Matrix([[0, a], [a, 0]])
Hm = sp.Matrix([[0, b], [b, 0]])
Rp = (Hp - I*eta*I2).inv()
Rm = (Hm - I*eta*I2).inv()
e0 = sp.Matrix([1, 0])

up = Rp*e0
um = Rm*e0
qp = sp.simplify(Rp[0, 0]/I)
qm = sp.simplify(Rm[0, 0]/I)

Z = sp.simplify((sp.conjugate(up).T*um)[0])
Z_rhs = sp.simplify(qp*qm*(1 + a*b/eta**2))

X = sp.simplify((e0.T*Rm*Rp*e0)[0])
X_rhs = sp.simplify(-qp*qm*(1 - a*b/eta**2))

B = Hp.row_join(t*I2).col_join((t*I2).row_join(Hm))
det_poly = sp.Poly(sp.expand((B - I*eta*sp.eye(4)).det()), t)
det0 = det_poly.coeff_monomial(t**0)
coeff_t2 = det_poly.coeff_monomial(t**2)
schur_coeff = sp.simplify(coeff_t2/det0)
schur_rhs = sp.simplify(-sp.trace(Rm*Rp))

Z_endpoint = sp.simplify(Z.subs(b, a))
q_endpoint = sp.simplify(qp)
ward_rhs = sp.simplify(q_endpoint/eta)

checks = {
    "positive_overlap_recursion": sp.simplify(Z - Z_rhs) == 0,
    "same_sign_overlap_recursion": sp.simplify(X - X_rhs) == 0,
    "schur_quadratic_coefficient": sp.simplify(schur_coeff - schur_rhs) == 0,
    "endpoint_Ward_identity": sp.simplify(Z_endpoint - ward_rhs) == 0,
}

print("HARD7-02 joint-channel exact algebra self-check")
print("q_plus =", sp.factor(qp))
print("q_minus =", sp.factor(qm))
print("Z =", sp.factor(Z))
print("X =", sp.factor(X))
print("quadratic_logdet_coefficient =", sp.factor(schur_coeff))
print("endpoint_Z =", sp.factor(Z_endpoint))
for name, ok in checks.items():
    print(f"{name} = {ok}")
print("ALL_EXACT_CHECKS_PASS =", all(checks.values()))

if not all(checks.values()):
    raise SystemExit(1)
