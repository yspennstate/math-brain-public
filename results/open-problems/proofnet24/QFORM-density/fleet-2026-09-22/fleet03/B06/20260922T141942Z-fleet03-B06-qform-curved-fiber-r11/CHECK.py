import sympy as sp

B, r, s, tau = sp.symbols('B r s tau', nonzero=True, real=True)
L = sp.Matrix([[0, B, 0], [B, r, s], [0, s, tau]])
expected_inv = sp.Matrix([
    [(-r*tau+s**2)/(B**2*tau), 1/B, -s/(B*tau)],
    [1/B, 0, 0],
    [-s/(B*tau), 0, 1/tau],
])
assert sp.simplify(L.det() + B**2*tau) == 0
assert sp.simplify(L.inv() - expected_inv) == sp.zeros(3)

M4 = 2**(sp.Rational(11,4))
Criesz = 3*sp.sqrt(3)*2**(sp.Rational(5,3))
print('det(L)=', sp.factor(L.det()))
print('inverse_verified=', True)
print('M4_exact=', M4)
print('M4_numeric=', sp.N(M4, 16))
print('Criesz_exact=', Criesz)
print('Criesz_numeric=', sp.N(Criesz, 16))
