import sympy as sp
from math import sqrt

a,s,t=sp.symbols('a s t', real=True)
B=4*sp.Matrix([[a,1,0],[1,0,0],[0,0,1]])
carrier=4*sp.Matrix([[a*s**2,s,0,0],[s,0,0,0],[0,0,t**2,0],[0,0,0,1]])
assert sp.factor(B.det()) == -64
assert sp.factor(B[2,2]*B.det()) == -256
cp=sp.factor(carrier.charpoly().as_expr())
expected=(-sp.Symbol('lambda')+4*t**2)*(sp.Symbol('lambda')-4)*(4*a*sp.Symbol('lambda')*s**2-sp.Symbol('lambda')**2+16*s**2)
assert sp.expand(cp-expected)==0
print('PASS')
print('det_Ba =', sp.factor(B.det()))
print('b_times_det_Ba =', sp.factor(B[2,2]*B.det()))
print('carrier_charpoly =', cp)
print('new_bound_exact = 2*sqrt(2) = %.12f' % (2*sqrt(2)))
print('partner_zero_bound_exact = 3/2 = %.12f' % 1.5)
