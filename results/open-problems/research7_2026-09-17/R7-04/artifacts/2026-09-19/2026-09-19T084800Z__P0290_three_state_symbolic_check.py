"""Exact symbolic self-check for the R7-04 P0290 three-state obstruction theorem.

This checks only algebraic identities used in the proof. It is not an independent
mathematical audit and does not establish source closure.
"""
import sympy as sp

# 1. Three-state monotone-generator discriminant.
a, b, e, f, u, v = sp.symbols("a b e f u v", nonnegative=True, real=True)
c = e + v
d = b + u
S = a + b + c + d + e + f
P = (c*e + c*f + d*e) + (a*e + a*f + b*f) + (a*d + b*c + b*d)
D = sp.expand(S**2 - 4*P)
target_D = sp.expand((a - f - u + v)**2 + 4*u*v)
assert sp.expand(D - target_D) == 0

# 2. Derivative identities for phi and g_0=-phi'.
x = sp.symbols("x", positive=True, real=True)
phi = (sp.exp(-x) - 1 + x) / x**2
g0 = sp.simplify(-sp.diff(phi, x))
expected_g0 = (x - 2 + (x + 2)*sp.exp(-x)) / x**3
assert sp.simplify(g0 - expected_g0) == 0

id_gprime = 6 - 2*x - (x**2 + 4*x + 6)*sp.exp(-x)
assert sp.simplify(x**4 * sp.diff(g0, x) - id_gprime) == 0

id_x2gprime = 2 - (x**2 + 2*x + 2)*sp.exp(-x)
assert sp.simplify(x**2 * sp.diff(x**2*g0, x) - id_x2gprime) == 0

# 3. Spectral-density numerator for a two-real-exponential covariance.
A, B, alpha, beta, omega = sp.symbols("A B alpha beta omega", real=True)
spectral = A*alpha/(alpha**2 + omega**2) + B*beta/(beta**2 + omega**2)
num = sp.factor(sp.together(spectral).as_numer_denom()[0])
expected_num = sp.expand(
    alpha*beta*(A*beta + B*alpha)
    + (A*alpha + B*beta)*omega**2
)
assert sp.expand(num - expected_num) == 0

print("P0290 exact symbolic certificate")
print("three_state_discriminant = (a-f-u+v)^2 + 4*u*v")
print("g0(x) = (x-2+(x+2)*exp(-x))/x^3")
print("x^4*g0'(x) = 6-2*x-(x^2+4*x+6)*exp(-x)")
print("x^2*(x^2*g0(x))' = 2-(x^2+2*x+2)*exp(-x)")
print("spectral_numerator = alpha*beta*(A*beta+B*alpha)+(A*alpha+B*beta)*omega^2")
print("ALL_SYMBOLIC_CHECKS_PASS")
