#!/usr/bin/env python3
import sympy as sp

lam=sp.symbols("lam", positive=True)

def F(d,D,x):
    h=D-d
    return sp.factor(sp.Rational(d,1)/x-sp.Rational(h,4)*(sp.Rational(d-1,1)/((d-x)*(d-x/sp.Rational(d,1)))-1/(D-x/sp.Rational(D,1))))

x=sp.Rational(6,5)
f210=F(2,10,x)
assert f210==sp.Rational(865,10374)
delta=sp.factor(2*f210/sp.Integer(11**2))
assert delta==sp.Rational(865,627627)

theta2=4-2*sp.sqrt(2)
assert sp.simplify(x-theta2)>0

# D=10 is a genuinely wider-support success at the rational endpoint 6/5;
# the same coarse covariance bound already fails there for D=11.
f211=F(2,11,x)
assert f211==sp.Rational(-27305,201264)

print("F_2_10(6/5) =", f210)
print("uniform derivative margin on [1,6/5] =", delta, "~", float(delta))
print("theta_2 =", theta2, "~", float(theta2))
print("6/5 - theta_2 =", sp.simplify(x-theta2), "~", float(x-theta2))
print("F_2_11(6/5) =", f211)
print("ALL EXACT EXTENSION CHECKS PASSED")
