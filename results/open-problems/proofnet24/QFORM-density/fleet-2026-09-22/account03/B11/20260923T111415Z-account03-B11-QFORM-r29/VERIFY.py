import math
import sympy as sp

m11,m12,m13,m22,m23,m33=sp.symbols('m11 m12 m13 m22 m23 m33')
M=sp.Matrix([[m11,m12,m13],[m12,m22,m23],[m13,m23,m33]])
N=sp.Matrix([
    [m11-m12**2/m22, m13-m12*m23/m22],
    [m13-m12*m23/m22, m33-m23**2/m22],
])
assert sp.simplify(M.det()-m22*N.det()) == 0

H0=sp.Matrix([[0,0,1],[0,1,0],[1,0,0]])
assert H0.eigenvals() == {-1:1, 1:2}

beta=sp.Rational(1,1024)
C=128*math.e*float((beta*(1-beta))**(-sp.Rational(1,4)))
partner=3*2**(2/3)
assert abs(C-1968.7271088025232) < 1e-10
assert abs(partner-4.762203155904598) < 1e-12

print('schur_identity=PASS')
print('partner_spectrum={-1,1,1}')
print(f'beta_constant={C:.13f}')
print(f'partner_constant={partner:.15f}')
print('QFORM_B11_R29_SHARED_SQUARE_CHECK_PASS')
