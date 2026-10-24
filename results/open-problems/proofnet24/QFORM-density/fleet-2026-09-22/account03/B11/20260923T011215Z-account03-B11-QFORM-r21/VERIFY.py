import math
import sympy as sp

B = sp.Matrix([[0,0,1],[0,1,0],[1,0,0]])
v = sp.Matrix([1,1,sp.Rational(-1,2)])
a = B*v

A = sp.zeros(4)
for j in range(3):
    A[0,j+1] = a[j]
    A[j+1,0] = a[j]
for i in range(3):
    for j in range(3):
        A[i+1,j+1] = B[i,j]

lam = sp.symbols('lam')
assert a == sp.Matrix([sp.Rational(-1,2),1,1])
assert (v.T*B*v)[0] == 0
assert B.det() == -1
assert sp.factor(A.charpoly(lam).as_expr()) == lam*(lam-1)*(4*lam**2-13)/4

print('a =', list(a))
print('vTBv =', (v.T*B*v)[0])
print('charpoly =', sp.factor(A.charpoly(lam).as_expr()))
print('detB =', B.det())
print('partner_LM1 =', 3*2**(2/3))
print('partner_Me =', 3*(2*math.e)**(2/3))
print('QFORM_B11_NULL_SCHUR_LIFT_CHECK_PASS')
