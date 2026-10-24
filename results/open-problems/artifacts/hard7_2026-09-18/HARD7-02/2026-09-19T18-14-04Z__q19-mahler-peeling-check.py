import sympy as sp

# Exact symbolic self-check for the finite algebra in the HARD7-02 Q1.9
# phase-Mahler peeling argument.  This is a self-check, not an independent audit.

u, a, b = sp.symbols('u a b', nonzero=True)
d1, d2, d3, d4 = sp.symbols('d1 d2 d3 d4')
m13, m14, m23, m24, m31, m32, m34, m41, m42, m43 = sp.symbols(
    'm13 m14 m23 m24 m31 m32 m34 m41 m42 m43'
)

# Generic 4x4 characteristic-type matrix.  The distinguished reciprocal edge
# occupies entries (1,2) and (2,1), with opposite phase powers.
M = sp.Matrix([
    [d1, -a*u, m13, m14],
    [-b/u, d2, m23, m24],
    [m31, m32, d3, m34],
    [m41, m42, m43, d4],
])

h = sp.expand(u * M.det())
poly = sp.Poly(h, u)
c0 = sp.expand(poly.coeff_monomial(u))

M0 = M.copy()
M0[0, 1] = 0
M0[1, 0] = 0
A0 = sp.expand(M0.det())
B = sp.expand(sp.Matrix([[d3, m34], [m43, d4]]).det())

middle_identity = sp.simplify(c0 - (A0 - a*b*B))
assert middle_identity == 0

# Exact negative-log integral used in the Pareto overshoot anti-concentration
# bound: integral_{-1}^1 log|t| dt = -2.
t = sp.symbols('t', positive=True)
int_log_abs = 2 * sp.integrate(sp.log(t), (t, 0, 1))
assert sp.simplify(int_log_abs + 2) == 0

# Exact constants after choosing r = (kappa/(2e)) s.
kappa, s = sp.symbols('kappa s', positive=True)
C0 = 1 + sp.log(2)
c = kappa / (2 * sp.E)
delta = sp.simplify(sp.log(kappa**2 * s**2 / (c**2 * s**2)) - C0)
assert sp.simplify(delta - (1 + sp.log(2))) == 0

potential_constant = sp.simplify((1 + sp.log(2)) * kappa / (4 * sp.E**3))

print('HARD7-02 exact symbolic self-check: determinant peeling and constants')
print('middle_coefficient_identity =', middle_identity)
print('integral_-1^1_log_abs =', int_log_abs)
print('C0 = 1 + log(2)')
print('chosen_c = kappa/(2*e)')
print('delta =', delta)
print('radial_potential_constant =', potential_constant)
print('ALL_EXACT_CHECKS_PASS = True')
