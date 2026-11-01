#!/usr/bin/env python3
import sympy as sp

print("R15 F0111 all-ray exact algebra self-check")

z,M1,M2 = sp.symbols("z M1 M2")
expr = 2 - 2*(z+1-M1) + (z**2+2*z-M2) - 2*M1*(z+1-M1)
Q = z**2 - 2*M1*z + 2*M1**2 - M2
assert sp.expand(expr-Q) == 0
print("partial-K quadratic identity: PASS")

R,a = sp.symbols("R a")
Qeq = a**2 - 2*(R*a)*a + 2*(R*a)**2 - R*a**2
assert sp.factor(Qeq - a**2*(R-1)*(2*R-1)) == 0
print("all-equal critical obstruction factor: PASS")

aa,bb,x,y = sp.symbols("aa bb x y")
sol = sp.solve([
    sp.Eq(x*aa+y*bb,(aa+bb)/2),
    sp.Eq(x*aa**2+y*bb**2,(aa**2+bb**2)/2)
],[x,y], dict=True)
assert len(sol)==1
assert sp.simplify(sol[0][x]-sp.Rational(1,2)) == 0
assert sp.simplify(sol[0][y]-sp.Rational(1,2)) == 0
print("two-root aggregate weights: PASS")

f,fp = sp.symbols("f fp")
B = fp-f
A = 2*f-fp
assert sp.expand(A+B-f) == 0
assert sp.expand(A+2*B-fp) == 0
print("radial value-gradient tangent identity: PASS")

eps,mu,var,H = sp.symbols("eps mu var H")
RR=1/(1-eps)
nu=var+mu**2
K_raw = 2*(mu+H+sp.log(1-eps))-2*RR*mu+RR*nu-RR**2*mu**2
K_dec = RR*var + 2*H + 2*sp.log(1-eps) - 2*(RR-1)*mu - RR*(RR-1)*mu**2
assert sp.simplify(K_raw-K_dec) == 0
print("infinity entropy-variance decomposition: PASS")

print("ALL_EXACT_SYMBOLIC_CHECKS_PASS")
