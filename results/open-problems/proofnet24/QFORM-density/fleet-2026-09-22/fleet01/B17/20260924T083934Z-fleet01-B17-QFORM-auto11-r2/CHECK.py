import sympy as sp
import mpmath as mp

q = sp.symbols('q', positive=True)
n = sp.Matrix([1, 2, 4]) / sp.sqrt(21)
P = n * n.T
B = sp.eye(3) - 2 * P
V = sp.Matrix([
    [1, 1, 1],
    [1, -1, 1],
    [1, 1, -1],
    [1, -1, -1],
]) / 2

assert sp.simplify(V.T * V - sp.eye(3)) == sp.zeros(3)
assert sp.simplify(B * B - sp.eye(3)) == sp.zeros(3)
assert B.eigenvals() == {sp.Integer(-1): 1, sp.Integer(1): 2}

q0 = sp.Rational(1, 2)
Cmat = sp.eye(3) - (1 - 1 / sp.sqrt(2)) * P
assert sp.simplify(Cmat * Cmat - (sp.eye(3) - q0 * P)) == sp.zeros(3)

K = sp.simplify(V * (sp.eye(3) - (2 - q0) * P) * V.T)
K_expected = sp.Matrix([
    [-sp.Rational(1,8), -sp.Rational(1,8), sp.Rational(3,8), sp.Rational(3,8)],
    [-sp.Rational(1,8), sp.Rational(33,56), -sp.Rational(11,56), sp.Rational(29,56)],
    [sp.Rational(3,8), -sp.Rational(11,56), sp.Rational(41,56), sp.Rational(9,56)],
    [sp.Rational(3,8), sp.Rational(29,56), sp.Rational(9,56), sp.Rational(17,56)],
])
assert K == K_expected
assert all(x != 0 for x in K)

dots = [sp.simplify((V.row(i) * n)[0]) for i in range(4)]
assert [sp.simplify(x * 2 * sp.sqrt(21)) for x in dots] == [7, 3, -1, -5]

u = sp.symbols('u', real=True)
a = 6*q/(2-q)
truncated_I = sum(
    (-a)**j / sp.factorial(j) * (2 * sp.Rational(1,2)**(2*j+1) / (2*j+1))
    for j in range(7)
)
ratio = sp.series((6/sp.sqrt(2-q) * truncated_I) / (3*sp.sqrt(2)), q, 0, 6)
expected = 1 - sp.Rational(3,80)*q**2 - sp.Rational(1,56)*q**3 - sp.Rational(3,512)*q**4 - sp.Rational(9,7040)*q**5
assert sp.expand(ratio.removeO() - expected) == 0

mp.mp.dps = 50
C_half = 2 * mp.sqrt(3*mp.pi) * mp.erf(1/mp.sqrt(2))
C0 = 3 * mp.sqrt(2)
C1 = 12 * mp.e**(-mp.mpf('0.5')) / mp.sqrt(2*mp.pi)
J = mp.sqrt(mp.pi/3) * mp.erf(mp.sqrt(3)/2)
partner_bound = C1 + (C0-C1)*J

assert C_half < C0
assert partner_bound < mp.mpf('3.98')

print('PASS_QFORM_B17_ONE_MACRO_ALIGNED_BARRIER')
print('C_half =', mp.nstr(C_half, 45))
print('gap_to_3sqrt2 =', mp.nstr(C0-C_half, 45))
print('partner_target_family_bound =', mp.nstr(partner_bound, 45))
