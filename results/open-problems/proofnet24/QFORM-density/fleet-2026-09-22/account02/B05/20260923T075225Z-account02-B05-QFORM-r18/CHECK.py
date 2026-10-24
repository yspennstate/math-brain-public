import sympy as sp
s,th,t=sp.symbols('s th t', positive=True, real=True)
e=sp.Matrix([sp.cos(th),sp.sin(th),0])
ep=sp.Matrix([-sp.sin(th),sp.cos(th),0])
F=sp.sqrt(s)*e+t*(ep+sp.Matrix([0,0,1]))
J=sp.Matrix.hstack(F.diff(s),F.diff(th),F.diff(t))
print('one_sheet_det=',sp.simplify(J.det()))
a,u=sp.symbols('a u', positive=True, real=True)
r=(u-a/u)/2
z=(u+a/u)/2
G=sp.Matrix([r*sp.cos(th),r*sp.sin(th),z])
J2=sp.Matrix.hstack(G.diff(a),G.diff(th),G.diff(u))
print('two_sheet_det=',sp.simplify(J2.det()))
import math
C=8*(2**0.75)*math.sqrt(5)
print('partner_pairlog_prefactor=',C)
print('partner_branch_kappa_quarter=',C*(3/80)**(-0.25))
print('partner_doublezero_eta_quarter=',14.7240*((3/20)*(1/16))**(-1/3))
