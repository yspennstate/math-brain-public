import sympy as sp

lam = sp.symbols('lam')
A = sp.Matrix([
    [1,1,0,1,0],
    [1,0,0,2,0],
    [0,0,0,0,1],
    [1,2,0,0,0],
    [0,0,1,0,0],
])
print('charpoly =', sp.factor(A.charpoly(lam).as_expr()))
C0 = 3 * 2**sp.Rational(1,3) * sp.sqrt(6)
print('C0_exact =', C0)
print('C0_decimal =', sp.N(C0, 16))

# Endpoint Fourier-integrability arithmetic used in the proof.
K = sp.symbols('K', positive=True)
q = sp.Rational(4,3)
# Integral over R of min(1,(K/|t|)^q): 2K + 2*K/(q-1).
expr = sp.simplify(2*K + 2*K/(q-1))
print('L4over3_integral =', expr)

M = sp.symbols('M', positive=True)
Acoef = 6**sp.Rational(3,4) * M
y = (2/Acoef)**sp.Rational(1,3)
minval = sp.simplify(Acoef*y + y**(-2))
print('riesz_minimum =', minval)
