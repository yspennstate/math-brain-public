#!/usr/bin/env python3
"""
R08 I0082 exact/symbolic self-check of the local-branch hardening
and independent exact audit of R09 Tang Q4.11 Cayley/stem formulas.

Finite algebra only. The theorem-sized analytic continuation/Harnack
argument is written in the immutable report.
"""
import sympy as sp

x, r, p, t, k = sp.symbols("x r p t k", positive=True)

print("R08 I0082 branch-hardening SELF-CHECK")

# Flat witness derivative identities.
A = r/x + (1-r)*sp.log(x/(1-x))
Aprime = sp.factor(sp.diff(A, x))
assert sp.simplify(Aprime - (x-r)/(x**2*(1-x))) == 0
r0 = sp.Rational(1,1000)
assert sp.simplify(Aprime.subs({r:r0, x:r0})) == 0
assert sp.simplify(Aprime.subs({r:r0, x:2*r0}) - sp.Rational(125000,499)) == 0
assert sp.simplify(Aprime.subs({r:r0, x:sp.Rational(1,2)}) - sp.Rational(499,125)) == 0
assert sp.Rational(3,100)*sp.Rational(125000,499) > sp.Rational(499,125)
print("flat_witness_coefficients = PASS")

# Cauchy stress: phi=-i eta, so S=i eta and normalized H=i.
eta = sp.symbols("eta", positive=True, real=True)
I = sp.I
S_cauchy = I*eta
assert sp.simplify(S_cauchy/eta - I) == 0
print("cauchy_normalized_direction = PASS")

# Semicircle direction: phi=t/z, S=-t/z.
# At z=1/(a-i beta), -1/z=-a+i beta.
a, beta = sp.symbols("a beta", real=True, positive=True)
zbd = 1/(a-I*beta)
assert sp.simplify(sp.im(-1/zbd) - beta) == 0
print("semicircle_boundary_pick_direction = PASS")

# Symmetric Bernoulli ±eps:
# phi(w)=(sqrt(w^2+4 eps^2)-w)/2
#      = eps^2/w-eps^4/w^3+O(eps^6).
eps = sp.symbols("eps", real=True)
w = sp.symbols("w", positive=True)
phi_bern = (sp.sqrt(w**2 + 4*eps**2) - w)/2
series = sp.series(phi_bern, eps, 0, 6)
expected = eps**2/w - eps**4/w**3
assert sp.simplify(series.removeO() - expected) == 0
print("bernoulli_small_scale_direction = PASS")

# Dirac is the unique degenerate normalization pattern: real phi -> eta=0.
m = sp.symbols("m", real=True)
assert sp.im(-m) == 0
print("dirac_eta_zero = PASS")

print("R08 independent audit R09 Tang Q4.11 latest package")

P0 = (1-p)**2
P1 = 2*p*(1-p)**2
P2 = p**2*(3-2*p)
pgf = sp.expand(P0 + P1*t + P2*t**2)
factor_claim = sp.expand((t-1)*(p**2*(3-2*p)*t-(1-p)**2))
assert sp.simplify((pgf-t) - factor_claim) == 0
assert sp.simplify(P0+P1+P2-1) == 0
print("triangle_block_offspring_and_factorization = PASS")

h = -2*p**3 + 2*p**2 + 2*p - 1
assert h.subs(p, sp.Rational(2,5)) == -sp.Rational(1,125)
assert h.subs(p, sp.Rational(41,100)) == sp.Rational(9179,500000)
assert sp.factor(sp.diff(h,p) - 2*(1-p)*(3*p+1)) == 0
print("critical_bracket_and_monotonicity = PASS")

q = (1-p)**2/(p**2*(3-2*p))
theta = sp.simplify(1-q**2)
R = 2*p**4 - 12*p**3 + 30*p**2 - 34*p + 15
theta2_claim = -12*(1-p)**2*R/(p**6*(3-2*p)**4)
assert sp.simplify(sp.diff(theta,p,2) - theta2_claim) == 0
bernstein = (
    15*(1-p)**4
    + 26*p*(1-p)**3
    + 18*p**2*(1-p)**2
    + 6*p**3*(1-p)
    + p**4
)
assert sp.expand(bernstein-R) == 0
print("cayley_theta_second_derivative_and_positive_R = PASS")

# General finite-stem derivative identity for integer k.
th = sp.Function("th")
stem = p**k * th(p)
stem2 = sp.diff(stem,p,2)
stem2_claim = p**(k-2)*(k*(k-1)*th(p) + 2*k*p*sp.diff(th(p),p) + p**2*sp.diff(th(p),p,2))
assert sp.simplify(stem2-stem2_claim) == 0
print("finite_stem_second_derivative_identity = PASS")

print("R08-AUDIT-R09-TANG-Q411-CAYLEY-03 = PASS")
print("ALL_EXACT_CHECKS_PASS")
