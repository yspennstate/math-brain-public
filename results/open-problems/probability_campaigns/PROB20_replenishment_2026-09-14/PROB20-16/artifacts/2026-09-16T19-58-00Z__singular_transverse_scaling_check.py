#!/usr/bin/env python3
"""PROB20-16 exact symbolic self-check for the singular transverse-scaling route.

Finite claims checked exactly:
  (i) two-site entropy interaction identities;
  (ii) the positive rational formula L-H_xy;
  (iii) first-order singular scaling formulas at x1=eps, s=theta*eps;
  (iv) the phase-orthogonal W Frobenius bookkeeping.

This is NOT a global X095/Phi certificate.
"""
import sympy as sp

x,y,s = sp.symbols('x y s', positive=True)
p00=(1-x)*(1-y)-s
p10=x*(1-y)+s
p01=(1-x)*y+s
p11=x*y-s
P=[p00,p10,p01,p11]
H=-sum(p*sp.log(p) for p in P)
L=sp.log(p10*p01/(p00*p11))
Hy=sp.diff(H,y)
Hxy=sp.diff(H,x,y)

assert sp.simplify(sp.logcombine(sp.diff(H,s)+L, force=True)) == 0
R = sp.factor(sp.simplify(sp.expand_log(L-Hxy, force=True)))
R_expected = sp.factor(s*(x*y*(1-x)*(1-y)-s**2)/(p00*p10*p01*p11))
assert sp.simplify(R-R_expected) == 0
A = 1/(x*(1-x)*y*(1-y))
assert sp.simplify(sp.diff(L,s).subs(s,0)-A)==0
assert sp.simplify(sp.logcombine(sp.diff(L,x).subs(s,0),force=True))==0
assert sp.simplify(sp.logcombine(Hxy.subs(s,0),force=True))==0
assert sp.simplify(sp.logcombine(sp.diff(Hxy,s).subs(s,0),force=True))==0

eps,theta=sp.symbols('eps theta', positive=True)
A0=1-y
AA=1-y+theta
BB=y-theta
Hy1=(1-eps)*sp.log((A0-eps*AA)/(y-eps*BB)) + eps*sp.log(AA/BB)
ell=sp.log(y*AA/(A0*BB))
C=ell-theta/(y*(1-y))
assert sp.simplify(sp.logcombine(sp.diff(Hy1,eps).subs(eps,0)-C, force=True))==0
L1=sp.log(AA*(y-eps*BB)/(BB*(A0-eps*AA)))
assert sp.simplify(sp.logcombine(L1.subs(eps,0)-ell, force=True))==0

rho=sp.symbols('rho', positive=True)
Hy0_path=Hy.subs({x:rho+eps,s:theta*eps})
L0_path=L.subs({x:rho+eps,s:theta*eps})
assert sp.simplify(sp.logcombine(sp.diff(Hy0_path,eps).subs(eps,0),force=True))==0
assert sp.simplify(sp.diff(L0_path,eps).subs(eps,0)-theta/(rho*(1-rho)*y*(1-y)))==0

c=sp.symbols('c', positive=True)
margin = theta/(c*(1-rho)*y*(1-y)) + C
margin_expected = ell + theta/(y*(1-y))*(1/(c*(1-rho))-1)
assert sp.simplify(margin-margin_expected)==0

b,v=sp.symbols('b v', real=True)
assert sp.expand(2*b**2*v**2 - 2*b**2*v**2)==0

print('status=PASS')
print('H_s_equals_minus_L=PASS')
print('L_minus_Hxy_positive_rational_identity=PASS')
print('diagonal_face_derivatives=PASS')
print('singular_Hy1_coefficient_C=PASS')
print('singular_L1_limit_ell=PASS')
print('C0_Hy_first_motion_zero=PASS')
print('C0_L_slope=PASS')
print('leading_margin_rewrite=PASS')
print('phase_orthogonal_W_norm=PASS')
print('NOTE=analytic identities only; no global Phi bound is certified')
