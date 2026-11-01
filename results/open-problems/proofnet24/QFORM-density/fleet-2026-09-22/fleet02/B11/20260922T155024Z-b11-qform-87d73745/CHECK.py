import math
import sympy as sp

m = 16
sqrt2 = sp.sqrt(2)
rows = [
    sp.Matrix([[1/sqrt2, 0, 1/sqrt2]]),
    sp.Matrix([[1/sqrt2, 0, -1/sqrt2]]),
]
for _ in range(m):
    rows.append(sp.Matrix([[0, sp.Rational(1, 4), 0]]))
R = sp.Matrix.vstack(*rows)
H = sp.diag(1, 1, -1)
A = sp.simplify(R * H * R.T)
assert sp.simplify(R.T * R) == sp.eye(3)
B = A.extract([0, 1, 2], [0, 1, 2])
assert B == sp.Matrix([[0,1,0],[1,0,0],[0,0,sp.Rational(1,16)]])
assert B.det() == -sp.Rational(1,16)
assert sorted([abs(x) for x in B.eigenvals().keys()], key=float) == [sp.Rational(1,16), 1, 1]
C_bank = 3 * 2**(4/3) * math.e**(1/3)
partner_local = 48 * 3**0.25 * math.sqrt(m)
print('m=', m)
print('RtR=', R.T * R)
print('B=', B)
print('detB=', B.det())
print('bank_bound=', repr(C_bank))
print('partner_local_bound=', repr(partner_local))
print('QFORM_BANKED_NULL_PAIR_CHECK_PASS')
