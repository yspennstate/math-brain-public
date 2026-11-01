import sympy as sp

# Exact symbolic self-check for the finite algebra used in the HARD7-02
# Campbell--O'Rourke Q1.9 logarithmic reciprocal-product criterion.
# This is a self-check, not an independent audit.

y, s, w1, w2, alpha, ell = sp.symbols(
    'y s w1 w2 alpha ell', positive=True
)

# Generic 4x4 matrix with the selected directed edge in positions (0,1),(1,0).
a = sp.symbols(
    'a00 a01 a02 a03 a10 a11 a12 a13 '
    'a20 a21 a22 a23 a30 a31 a32 a33'
)
M = sp.Matrix(4, 4, a)
M[0, 1] = -s * y * w1
M[1, 0] = -s * y * w2

D = sp.expand(M.det())
P = sp.Poly(D, y)
minor = M.extract([2, 3], [2, 3]).det()

check_degree = (P.degree() == 2)
check_quad = sp.simplify(P.coeff_monomial(y**2) + s**2*w1*w2*minor) == 0

# Analytic constant in the one-root Pareto logarithmic bound:
# integral_{-1}^1 log|t| dt = 2 integral_0^1 log t dt = -2.
t = sp.symbols('t', positive=True)
log_interval = sp.simplify(2 * sp.integrate(sp.log(t), (t, 0, 1)))
check_log = (log_interval == -2)

# If K_s = 2 log s + ell - 4 alpha and
# c_theta = exp((ell - 4 alpha - 1)/2), then K_s - 2 log(c_theta s)=1.
c_theta = sp.exp((ell - 4*alpha - 1)/2)
bracket = sp.simplify((2*sp.log(s) + ell - 4*alpha) - 2*sp.log(c_theta*s))
check_bracket = (bracket == 1)

print('HARD7-02 Q1.9 log-product exact algebra self-check')
print('determinant_degree_in_overshoot =', P.degree())
print('quadratic_coefficient =', sp.factor(P.coeff_monomial(y**2)))
print('minus_s2w1w2_minor =', sp.factor(-s**2*w1*w2*minor))
print('quadratic_coeff_identity =', check_quad)
print('integral_-1_1_log_abs_t =', log_interval)
print('c_theta =', c_theta)
print('potential_bracket =', bracket)
print('ALL_EXACT_CHECKS_PASS =', all([check_degree, check_quad, check_log, check_bracket]))
