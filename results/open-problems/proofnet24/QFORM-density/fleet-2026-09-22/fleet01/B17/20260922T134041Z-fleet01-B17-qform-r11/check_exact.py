import sympy as sp
A = sp.Matrix([
    [-1, 3,-1,-1],
    [ 3,-1,-1,-1],
    [-1,-1, 3,-1],
    [-1,-1,-1, 3],
]) / 4
assert A.eigenvals() == {-1:1, 0:1, 1:2}

u = sp.symbols('u', nonnegative=True)
expr_u = 4 / ((1+sp.sqrt(2))+2*u+(1-sp.sqrt(2))*u**2)
quad = sp.integrate(expr_u, (u, 0, 1))
quad_expected = sp.sqrt(2)*sp.log(1+sp.sqrt(2))
assert sp.simplify((3+2*sp.sqrt(2))-(1+sp.sqrt(2))**2) == 0
assert abs(complex(sp.N(quad-quad_expected,50))) < 1e-40
p0 = sp.simplify((4/sp.sqrt(2))*quad_expected)
expected = 4*sp.log(1+sp.sqrt(2))
assert sp.simplify(p0-expected) == 0

a = sp.symbols('a', nonnegative=True)
x = sp.symbols('x', real=True)
outside = 2*sp.integrate(x**2, (x, sp.Rational(1,2), sp.Rational(1,2)+a/2))
missing = 2*sp.integrate(x**2, (x, sp.Rational(1,2)-a/2, sp.Rational(1,2)))
assert sp.expand(outside-missing) == a**2/2

print('PASS')
print('eigenvalues=', A.eigenvals())
print('p0_exact=', expected)
print('p0_decimal=', sp.N(expected, 30))
print('pi_decimal=', sp.N(sp.pi, 30))
print('3sqrt2=', sp.N(3*sp.sqrt(2), 30))
print('stability_shell_excess=', sp.expand(outside-missing))
