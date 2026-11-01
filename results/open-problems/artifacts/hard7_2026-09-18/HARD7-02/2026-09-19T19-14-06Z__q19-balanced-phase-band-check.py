import sympy as sp

# Exact finite-algebra self-check for HARD7-02, Q1.9 balanced-phase
# amplitude-band theorem. This verifies only the elementary constants and
# algebraic identities used in the written proof; it is not an independent audit.

h = sp.symbols("h", positive=True)
delta = sp.Rational(1, 4)
density = sp.simplify(1 / (1 - 2*delta))

# alpha = 1 worked slice, beta = alpha/2 = 1/2.
m = sp.simplify(density * sp.integrate(sp.sqrt(h), (h, delta, 1-delta)))
m_expected = -sp.Rational(1, 6) + sp.sqrt(3)/2

ell = sp.simplify(
    density * sp.integrate(sp.Rational(1,2)*(sp.log(h)+sp.log(1-h)),
                           (h, delta, 1-delta))
)
ell_expected = -1 + sp.log(3*sp.sqrt(3)/4)

# For alpha=1 the proof chooses c = exp(ell/2)/(2 e).
c = sp.simplify(sp.exp(ell/2)/(2*sp.E))
c_expected = 3**sp.Rational(3,4) * sp.exp(-sp.Rational(3,2)) / 4

# The peeled-edge circular-log-potential bracket must be exactly 1+log 2.
bracket = sp.simplify(ell - (1 + sp.log(2)) - 2*sp.log(c))

# Moment-row constant at beta=1/2.
beta = sp.Rational(1,2)
C_row = sp.simplify(2 + m * 2**beta * (2-beta)/(1-beta))

checks = [
    sp.simplify(m - m_expected) == 0,
    sp.simplify(ell - ell_expected) == 0,
    sp.simplify(c - c_expected) == 0,
    sp.simplify(bracket - (1 + sp.log(2))) == 0,
    sp.simplify(C_row - (2 - sp.sqrt(2)/2 + sp.Rational(3,2)*sp.sqrt(6))) == 0,
]

print("HARD7-02 balanced-phase amplitude-band exact algebra self-check")
print("delta =", delta)
print("m = E[sqrt(H)] =", m)
print("ell = E[log sqrt(H(1-H))] =", ell)
print("c(alpha=1,delta=1/4) =", c)
print("peeled bracket =", bracket)
print("C_row(beta=1/2) =", C_row)
print("m numeric =", sp.N(m, 18))
print("ell numeric =", sp.N(ell, 18))
print("c numeric =", sp.N(c, 18))
print("checks =", checks)
print("ALL_EXACT_CHECKS_PASS =", all(checks))
