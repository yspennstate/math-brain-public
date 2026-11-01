#!/usr/bin/env python3
"""Exact symbolic self-check for HARD7-02 final-recovery run 2.

This checker verifies only the finite algebra used in the endpoint-deformation
and transverse-susceptibility reductions.  It is a self-check, not an
independent proof of the PWIT limit, the alpha=1 cavity compactness argument,
or the eta -> 0 theorem in the accompanying report.
"""

import sympy as sp

# B5: exact endpoint parameterization x = 1/2 - e.
e, q = sp.symbols("e q", real=True)
h = (sp.sqrt(1 + 2*e) + sp.sqrt(1 - 2*e)) / 2
d = (sp.sqrt(1 + 2*e) - sp.sqrt(1 - 2*e)) / 2
assert sp.simplify(h**2 + d**2 - 1) == 0
assert sp.simplify(h*d - e) == 0
# With q=d^2 this polynomial identity selects q=e^2+O(e^4) near e=0.
assert sp.simplify(d**2 * (1 - d**2) - e**2) == 0

# B15: bipartite parity converts imaginary-shift susceptibility into
# a positive channel overlap.  Use two possibly different one-edge channels.
eta, p, m, b = sp.symbols("eta p m b", positive=True, real=True)
I = sp.I
J = sp.diag(1, -1)
Hp = sp.Matrix([[0, p], [p, 0]])
Hm = sp.Matrix([[0, m], [m, 0]])
Rp = (Hp - I*eta*sp.eye(2)).inv()
Rm = (Hm - I*eta*sp.eye(2)).inv()
Rp_star = (Hp + I*eta*sp.eye(2)).inv()

# J H J = -H implies J R(i eta) J = -R(i eta)^*.
assert sp.simplify(J*Rp*J + Rp_star) == sp.zeros(2)

M4 = sp.BlockMatrix([
    [Hp - I*eta*sp.eye(2), -I*b*J],
    [I*b*J, Hm - I*eta*sp.eye(2)],
]).as_explicit()
detM = sp.expand(M4.det())
det0 = sp.expand(
    (Hp - I*eta*sp.eye(2)).det() * (Hm - I*eta*sp.eye(2)).det()
)
# d/d(b^2) log det at b=0 is the b^2 determinant coefficient / det(0).
coeff_b2 = detM.coeff(b, 2)
imag_direct = sp.simplify(coeff_b2 / det0)
imag_schur = sp.simplify(-sp.trace(Rm * J * Rp * J))
imag_positive = sp.simplify(sp.trace(Rm * Rp_star))
assert sp.simplify(imag_direct - imag_schur) == 0
assert sp.simplify(imag_schur - imag_positive) == 0

root = sp.Matrix([1, 0])
local = sp.simplify((root.T * Rm * Rp_star * root)[0])
overlap = sp.simplify(((Rp * root).conjugate().T * (Rm * root))[0])
assert sp.simplify(local - overlap) == 0

# B5: exact q=d^2 derivative of the endpoint real-shift block determinant.
a, t = sp.symbols("a t", nonzero=True, real=True)
H = sp.Matrix([[0, a], [a, 0]])
V = H  # one-edge signed perturbation; sign is immaterial in the quadratic term
hq = sp.sqrt(1 - q)
dq = sp.sqrt(q)
Aq = hq*H - t*sp.eye(2) - I*eta*sp.eye(2)
Dq = hq*H + t*sp.eye(2) - I*eta*sp.eye(2)
Mq = sp.BlockMatrix([[Aq, dq*V], [dq*V, Dq]]).as_explicit()
detq = sp.simplify(Mq.det())
dlog_direct = sp.simplify(sp.diff(detq, q).subs(q, 0) / detq.subs(q, 0))
Rminus = (H - t*sp.eye(2) - I*eta*sp.eye(2)).inv()
Rplus = (H + t*sp.eye(2) - I*eta*sp.eye(2)).inv()
dlog_formula = sp.simplify(
    -sp.Rational(1, 2) * sp.trace(Rminus*H + Rplus*H)
    - sp.trace(Rplus*V*Rminus*V)
)
assert sp.simplify(dlog_direct - dlog_formula) == 0

# B29: algebraic Hellinger-affinity identity.
A, B, C, D = sp.symbols("A B C D", real=True)
hell_expr = sp.expand(
    1 - (A*C + B*D)
    - sp.Rational(1, 2) * ((A-C)**2 + (B-D)**2)
)
hell_target = 1 - sp.Rational(1, 2) * (A**2 + B**2 + C**2 + D**2)
assert sp.simplify(hell_expr - hell_target) == 0

print("h2_plus_d2 =", sp.simplify(h**2 + d**2))
print("h_times_d =", sp.simplify(h*d))
print("q_identity_residual =", sp.simplify(d**2 * (1-d**2) - e**2))
print("imaginary_shift_susceptibility =", sp.factor(imag_positive))
print("root_overlap =", sp.factor(local))
print("endpoint_q_derivative_match =", sp.simplify(dlog_direct - dlog_formula))
print("hellinger_affinity_identity_residual =", sp.simplify(hell_expr - hell_target))
print("ALL_EXACT_CHECKS_PASS = True")
