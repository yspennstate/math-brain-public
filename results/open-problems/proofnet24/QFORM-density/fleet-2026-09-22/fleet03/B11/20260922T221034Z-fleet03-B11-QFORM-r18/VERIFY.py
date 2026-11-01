import sympy as sp
from math import sqrt

s,t,u=sp.symbols('s t u', real=True)
H=sp.Matrix([[0,0,1],[0,1,0],[1,0,0]])
def r(x):
    return sp.Matrix([1,x,-x**2/sp.Integer(2)])

pair=sp.factor((r(s).T*H*r(t))[0])
det=sp.factor(sp.Matrix.hstack(r(s),r(t),r(u)).det())
assert sp.simplify(pair + (s-t)**2/sp.Integer(2)) == 0
assert sp.simplify(det - (s-t)*(s-u)*(t-u)/sp.Integer(2)) == 0

C3=16*sqrt(30)*2**0.25
bound=2*C3*10**(1/3)
trace=2*bound
print('pair =', pair)
print('triple_det =', det)
print('C3 =', repr(C3))
print('five_ray_density_bound =', repr(bound))
print('partner_trace_bound =', repr(trace))
print('QFORM_B11_NULL_D0_FIVERAY_CHECK_PASS')
