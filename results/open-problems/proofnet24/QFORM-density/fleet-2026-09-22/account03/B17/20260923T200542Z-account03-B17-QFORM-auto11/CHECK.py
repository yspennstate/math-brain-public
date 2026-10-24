from fractions import Fraction
import sympy as sp

lam = sp.symbols('lam')
s2 = sp.sqrt(2)
T = sp.Matrix([
    [1/s2, 1/s2, 0, 0, 0, 0],
    [0, 0, 1/s2, 1/s2, 0, 0],
    [0, 0, 0, 0, 1/s2, 1/s2],
])
B = sp.eye(3) - sp.Rational(2, 3) * sp.ones(3)
A = sp.simplify(T.T * B * T)

assert T*T.T == sp.eye(3)
assert B*B == sp.eye(3)
assert sp.simplify(A**2 - T.T*T) == sp.zeros(6)
assert sp.simplify(A**3 - A) == sp.zeros(6)
charpoly = sp.factor(A.charpoly(lam).as_expr())
assert charpoly == lam**3 * (lam-1)**2 * (lam+1)

# Rational certificate used for R >= 120.
assert Fraction(7, 10)**2 < Fraction(1, 2)          # 7/10 < 1/sqrt(2)
assert Fraction(49, 20)**2 > 6                      # sqrt(6) < 49/20
M_lower = Fraction(120*7, 10) - Fraction(49, 40)
assert M_lower == Fraction(3311, 40)
remote_upper = Fraction(147, 10) / M_lower
assert remote_upper == Fraction(588, 3311)
whole_upper = Fraction(508, 125) + remote_upper
benchmark = Fraction(140, 33)
gap = benchmark - whole_upper
assert gap == Fraction(148, 177375) and gap > 0
assert Fraction(140, 99)**2 < 2                     # 140/33 < 3 sqrt(2)

print('PASS QFORM_FRAGMENT_KERNEL_AGGREGATE')
print('charpoly =', charpoly)
print('M_lower_R120 =', M_lower)
print('remote_upper =', remote_upper, float(remote_upper))
print('whole_rational_upper =', whole_upper, float(whole_upper))
print('benchmark_140_over_33 =', benchmark, float(benchmark))
print('exact_gap =', gap, float(gap))
