import sympy as sp

beta, alpha, A, theta, u, h, V, L, Y = sp.symbols(
    'beta alpha A theta u h V L Y', nonzero=True
)

Q = beta*(u+A*Y)**2 + 2*alpha*V*(h+theta*A*Y+L)
d = beta*A**2
m = u/A + alpha*theta*V/(beta*A)
R = sp.expand(Q-d*(Y+m)**2)
R_expected = 2*alpha*V*L + 2*alpha*(h-theta*u)*V - alpha**2*theta**2*V**2/beta
assert sp.simplify(R-R_expected) == 0

N = sp.Matrix([
    [-alpha**2*theta**2/beta, alpha],
    [alpha, 0],
])
assert sp.factor(N.det()) == -alpha**2

# Worst partner balance scale: 1-rho = 2^-10.
constant = sp.sqrt(2) * 2 * 128 * (sp.Integer(2)**10)**sp.Rational(1,4)
assert sp.simplify(constant-2048) == 0

print('QFORM_B11_RANKONE_RESIDUAL_CHECK_PASS')
