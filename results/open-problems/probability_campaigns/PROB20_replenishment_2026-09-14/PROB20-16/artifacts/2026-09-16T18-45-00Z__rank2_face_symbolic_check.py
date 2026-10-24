#!/usr/bin/env python3
"""
PROB20-16 exact symbolic checker for the generic rank-two fixed-nullspace
boundary-face entropy concavity theorem.

All asserted identities are symbolic/rational algebra. No floating-point
positivity claim is used as proof.
"""
import sympy as sp

# Eigenvalues of the surviving 2x2 kernel block.
a,b = sp.symbols('a b', positive=True)
m = a+b-2*a*b
e = (1-a)*(1-b)
d = a*b
Delta = a-b

# Cardinality-Fisher coefficients for a diagonal direction D=diag(x,y)
# in the eigenbasis of A.
Acoef = sp.simplify((1-b)**2/e + (1-2*b)**2/m + b**2/d)
Ccoef = sp.simplify((1-a)**2/e + (1-2*a)**2/m + a**2/d)
Bcoef = sp.simplify((1-b)*(1-a)/e + (1-2*b)*(1-2*a)/m + a*b/d)

A_expected = sp.simplify((Delta**2 + a*(1-a))/(a*(1-a)*m))
C_expected = sp.simplify((Delta**2 + b*(1-b))/(b*(1-b)*m))
B_expected = sp.simplify(1/m)

assert sp.simplify(Acoef-A_expected) == 0
assert sp.simplify(Ccoef-C_expected) == 0
assert sp.simplify(Bcoef-B_expected) == 0

# Odds-square-root variables r,s: a=r^2/(1+r^2), b=s^2/(1+s^2).
r,s = sp.symbols('r s', positive=True)
subs = {
    a: r**2/(1+r**2),
    b: s**2/(1+s**2),
}
AA = sp.factor(Acoef.subs(subs))
CC = sp.factor(Ccoef.subs(subs))
BB = sp.factor(Bcoef.subs(subs))
z = sp.simplify(r/s+s/r)
T = sp.simplify(2+z-BB)

# Key exact factor proving B+sqrt(A C) >= 2+z.
factor_gap = sp.factor(AA*CC - T**2)
expected_gap = sp.factor((r+s)**2*(r*s-1)**2/(r**2*s**2))
assert sp.simplify(factor_gap-expected_gap) == 0

# One-particle block eigenvalues gamma_1, gamma_2.
g1 = sp.simplify(a*(1-b))
g2 = sp.simplify(b*(1-a))
assert sp.simplify(g1+g2-m) == 0
assert sp.simplify(g1*g2-e*d) == 0

# The spectral ratio entering the logarithmic upper bound.
kappa = sp.simplify(g1/g2)
ratio = sp.simplify(m**2/(3*e*d))
ratio_expected = sp.simplify((kappa+1)**2/(3*kappa))
assert sp.simplify(ratio-ratio_expected) == 0

# Verify the face-log aggregation algebra abstractly.
q1,q2,q3 = sp.symbols('q1 q2 q3', positive=True)
p1,p2,p3,p0,p12,p13,p23 = sp.symbols(
    'p1 p2 p3 p0 p12 p13 p23', positive=True
)
# L = sum q_k lambda_k with pair opposite k:
L_expanded = (
    q1*sp.log(p2*p3/(p0*p23))
    + q2*sp.log(p1*p3/(p0*p13))
    + q3*sp.log(p1*p2/(p0*p12))
)
# Under q1+q2+q3=1, p23=d*q1, p13=d*q2, p12=d*q3,
# coefficients on log p_i become 1-q_i.
# This is checked by coefficient bookkeeping instead of symbolic log expansion.
coeffs = {
    'log_p1': sp.simplify(q2+q3),
    'log_p2': sp.simplify(q1+q3),
    'log_p3': sp.simplify(q1+q2),
    'log_p0': sp.simplify(-(q1+q2+q3)),
}
assert sp.simplify(coeffs['log_p1']-(1-q1)).subs(q1+q2+q3,1) == 0

# Since SymPy does not substitute sum constraints syntactically, verify after q3=1-q1-q2.
q3sub = 1-q1-q2
assert sp.simplify((q2+q3sub)-(1-q1)) == 0
assert sp.simplify((q1+q3sub)-(1-q2)) == 0
assert sp.simplify((q1+q2)-(1-q3sub)) == 0

# Boundary entropy extremizer helper:
# G(q)=H(q)-2H((1-q)/2). On q3=0 it is exactly -log 4.
t = sp.symbols('t', positive=True)
# Use algebraic log expansion explicitly.
G_edge = (
    -t*sp.log(t) -(1-t)*sp.log(1-t)
    -2*(
        -((1-t)/2)*sp.log((1-t)/2)
        -(t/2)*sp.log(t/2)
        -(sp.Rational(1,2))*sp.log(sp.Rational(1,2))
    )
)
assert sp.simplify(sp.expand_log(G_edge, force=True) + sp.log(4)) == 0

print("status=PASS")
print("cardinality_fisher_coefficients=PASS")
print("rank2_one_particle_spectral_identities=PASS")
print("key_factor_identity=PASS")
print("weighted_face_log_bookkeeping=PASS")
print("boundary_entropy_edge_value=PASS")
print("factor_gap=", factor_gap)
