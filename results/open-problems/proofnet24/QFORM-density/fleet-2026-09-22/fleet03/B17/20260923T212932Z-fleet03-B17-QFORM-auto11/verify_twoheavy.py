import sympy as sp

sqrt2 = sp.sqrt(2)
c = 1 / sqrt2
A = sp.Matrix([
    [sp.Rational(1, 2), -sp.Rational(1, 2), -1 / sqrt2],
    [-sp.Rational(1, 2), sp.Rational(1, 2), -1 / sqrt2],
    [-1 / sqrt2, -1 / sqrt2, 0],
])

assert sp.simplify(A * A - sp.eye(3)) == sp.zeros(3)
lam = sp.symbols('lam')
charpoly = sp.factor(A.charpoly(lam).as_expr())
assert charpoly == (lam - 1) ** 2 * (lam + 1)
assert A[2, 2] == 0

r = (sp.sqrt(1 + 4 * c) - 1) / 2
assert sp.simplify(r**2 + r - c) == 0
p0 = sp.simplify(2 * r + 2 * c * sp.log(c / r**2))
global_bound = 2 ** sp.Rational(9, 4) - 1
partner_obstruction = 3 * sqrt2
u = 2 ** sp.Rational(1, 4)
gap = sp.simplify(partner_obstruction - global_bound)
assert sp.simplify(gap - (3 * u - 1) * (u - 1)) == 0
assert float(sp.N(gap, 40)) > 0

print('A^2=I: PASS')
print('charpoly:', charpoly)
print('A_33:', A[2, 2])
print('c:', sp.N(c, 30))
print('r:', sp.N(r, 30))
print('cone_tip_uniform:', sp.N(p0, 30))
print('global_bound:', sp.N(global_bound, 30))
print('3sqrt2:', sp.N(partner_obstruction, 30))
print('gap:', sp.N(gap, 30))
print('gap_factorization:', (3 * u - 1) * (u - 1))
print('PASS QFORM_TWOHEAVY_ZEROPIVOT_GLOBAL')
