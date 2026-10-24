import math
import sympy as sp

x,z,w,y=sp.symbols('x z w y', nonzero=True)
M=sp.Matrix([[0,x,0],[x,z,w],[0,w,y]])
assert sp.factor(M.det()) == -x**2*y
Minv=sp.simplify(M.inv())
assert sp.simplify(Minv[0,1]-1/x)==0
assert sp.simplify(Minv[2,2]-1/y)==0

print('QFORM_B05_TRIBANK_CHECK')
print('det(M)=-x^2*y')
print('Minv_12=1/x')
print('Minv_33=1/y')
print('aggregate_constant_bound=',8.0)
print('general_diffuse_star_pairlog_bound=',8*2**0.75)
print('partner_nearzero_uniform=',8*2**0.25)
for m in [3,10,100,10000]:
    a=1/m
    beta2=2*(1+a)
    b2=beta2/m
    disc=math.sqrt(a*a+4*beta2)
    lp=(a+disc)/2
    lm=(a-disc)/2
    kappa=(math.sqrt(a*a+4*b2)-a)/2
    partner=8*2**0.25*(1+a)**-0.25
    print(m, f's3=1 star=({lp:.12g},{lm:.12g}) b_j^2={b2:.12g} kappa_j={kappa:.12g} partner={partner:.12g}')
print('PASS')
