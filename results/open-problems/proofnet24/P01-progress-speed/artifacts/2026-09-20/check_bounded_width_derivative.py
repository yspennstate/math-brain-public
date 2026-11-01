#!/usr/bin/env python3
import sympy as sp

d,h,lam=sp.symbols("d h lam", positive=True)
D=d+h
qmax=(d-1)/((d-lam)*(d-lam/d))
qmin=1/(D-lam/D)
F=d/lam-h*(qmax-qmin)/4
lam0=d-h/4
F0=sp.factor(F.subs(lam,lam0))
N=32*d**4 + 44*d**3*h - 32*d**3 + 12*d**2*h**2 - 4*d**2*h + 7*d*h**2 - h**3
den=(4*d-h)*(4*d**2-4*d+h)*(4*d**2+8*d*h-4*d+4*h**2+h)
assert sp.simplify(F0-h*N/den)==0

positive_decomp=32*d**3*(d-1)+4*d**2*h*(11*d-1)+h**2*(12*d**2+7*d-h)
assert sp.expand(positive_decomp-N)==0

F24=sp.factor(F.subs({d:2,h:2}))
target=(33*lam**2-208*lam+256)/(lam*(16-lam)*(4-lam)*(2-lam))
assert sp.simplify(F24-target)==0

rho=(sp.Integer(104)-8*sp.sqrt(37))/33
assert sp.simplify((33*lam**2-208*lam+256).subs(lam,rho))==0
assert 1 < float(rho) < 2

F_at=sp.simplify(F24.subs(lam,sp.Rational(3,2)))
assert F_at==sp.Rational(292,435)
delta=sp.simplify(2*F_at/sp.Integer(25))
assert delta==sp.Rational(584,10875)

theta2=sp.simplify(2/(1+sp.sqrt(sp.Rational(1,2))))
assert float(theta2)<1.5<float(rho)

print("general_F0 =", F0)
print("positive_numerator_decomposition =", positive_decomp)
print("F_2_4(lambda) =", F24)
print("rho_2_4 =", rho, "~", float(rho))
print("theta_2 ~", float(theta2))
print("F_2_4(3/2) =", F_at)
print("uniform derivative margin delta_2_4 =", delta, "~", float(delta))
print("ALL EXACT SYMBOLIC CHECKS PASSED")
