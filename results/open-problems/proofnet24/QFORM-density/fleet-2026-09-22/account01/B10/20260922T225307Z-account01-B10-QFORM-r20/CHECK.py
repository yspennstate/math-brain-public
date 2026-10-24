"""Exact/numeric checks for account01/B10 QFORM r20.
No probabilistic claim depends on this script; the report contains analytic proofs.
"""
import math
import sympy as sp

# Centered graph-plane determinant identity.
s = sp.symbols('s', nonzero=True, real=True)
a,b,c = sp.symbols('a b c', real=True)
d1,d2 = sp.symbols('d1 d2', real=True)
# m=(s,0), D_c symmetric.
Dc = sp.Matrix([[a,b],[b,c]])
d = sp.Matrix([d1,d2])
m = sp.Matrix([s,0])
K = Dc + (d*m.T-m*d.T)/2
assert sp.simplify(K.det() - (Dc.det() + (d1*0-d2*s)**2/4)) == 0

# Cofactor identity in symbolic coordinates for a symmetric 3x3 matrix.
m00,m01,m02,m11,m12,m22 = sp.symbols('m00 m01 m02 m11 m12 m22')
M = sp.Matrix([[m00,m01,m02],[m01,m11,m12],[m02,m12,m22]])
p1,p2,q1,q2 = sp.symbols('p1 p2 q1 q2')
Rp = sp.Matrix([[p1,1,0],[p2,0,1]])
Rq = sp.Matrix([[q1,1,0],[q2,0,1]])
npv = sp.Matrix([1,-p1,-p2])
nqv = sp.Matrix([1,-q1,-q2])
assert sp.simplify((Rp*M*Rq.T).det() - (npv.T*M.adjugate()*nqv)[0]) == 0

# Numerical constant in (4.5).
C = (3*2**(5/6)*(1/2)**(-1/3)*(7/9)**(-1/6)
     *((1/640)*(1/64))**(-1/6))
assert C < 41.233

# Angular constant in (6.3).
angle_const = 24*math.sqrt(5)/329
assert angle_const > 0.163

print('QFORM_B10_R20_CHECK_PASS')
print('one_large_defect_constant=', C)
print('angle_constant=', angle_const)
