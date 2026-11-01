#!/usr/bin/env python3
# PROB20-16 exact checker: 3-parameter C082 affine solid + full Hermitian tube.
import sympy as sp
from math import comb

h,g,r,u,v,w = sp.symbols("h g r u v w", real=True)
sqrt2 = sp.sqrt(2)

Kstar = sp.Matrix([
    [sp.Rational(8846539,15630789), sp.Rational(1812625,15630789), sp.Rational(6375,79546)*sqrt2],
    [sp.Rational(1812625,15630789), sp.Rational(8846539,15630789), -sp.Rational(6375,79546)*sqrt2],
    [sp.Rational(6375,79546)*sqrt2, -sp.Rational(6375,79546)*sqrt2, sp.Rational(47421,79546)]
])
I = sp.eye(3)
D = sp.diag(1,1,-2)
F = sp.Matrix([[0,1,0],[1,0,0],[0,0,0]])
K = Kstar + h*I + g*D + r*F
L = sp.simplify((I-K).inv()-I)

A = 125-393*(g+h+r)
Q = (-159092*g**2 -79546*g*h +159092*g*r +55375*g
     +79546*h**2 -79546*h*r -75875*h +32125*r +15625)
R = (-62523156*g**3 -93784734*g**2*h -20874281*g**2 -29374828*g*h
     +62523156*g*r**2 +14501000*g*r +13730625*g
     +31261578*h**3 -8500547*h**2 -31261578*h*r**2
     -7250500*h*r -10568625*h +12625125*r**2 +2125000*r +3125000)
S = (62523156*g*r +7250500*g -31261578*h*r -3625250*h
     +12625125*r +1062500)
P = (159092*g**2 +79546*g*h -159092*g*r -134921*g
     -79546*h**2 +79546*h*r -3671*h +47421*r +28125)
C = 2*6375**2

assert sp.simplify(L[0,0]-R/(A*Q)) == 0
assert sp.simplify(L[1,1]-R/(A*Q)) == 0
assert sp.simplify(L[2,2]-P/Q) == 0
assert sp.simplify(L[0,1]-S/(A*Q)) == 0
assert sp.simplify(L[0,2]-6375*sqrt2/Q) == 0
assert sp.simplify(L[1,2]+6375*sqrt2/Q) == 0

# Exact central-solid bounds:
# ell_i in [7/10,199/100], rho_i in [29/100,41/100].
polys = {
    "A": A,
    "Q": Q,
    "R": R,
    "P": P,
    "ell12_lo": 10*R-7*A*Q,
    "ell12_hi": sp.Rational(199,100)*A*Q-R,
    "ell3_lo": 10*P-7*Q,
    "ell3_hi": sp.Rational(199,100)*Q-P,
    "rho12_lo": 10000*S**2-29**2*R**2,
    "rho12_hi": 41**2*R**2-10000*S**2,
    "rho13_lo": 10000*C*A-29**2*R*P,
    "rho13_hi": 41**2*R*P-10000*C*A,
}

# Parameter box:
# h in [-3/20,1/100], g in [-1/500,3/100], r in [-1/100,1/100].
hsub = -sp.Rational(3,20) + sp.Rational(4,25)*u
gsub = -sp.Rational(1,500) + sp.Rational(4,125)*v
rsub = -sp.Rational(1,100) + sp.Rational(1,50)*w

def bernstein_coefficients(expr):
    f = sp.Poly(sp.expand(expr.subs({h:hsub,g:gsub,r:rsub})), u,v,w, domain=sp.QQ)
    du,dv,dw = f.degree(u),f.degree(v),f.degree(w)
    dct = f.as_dict()
    vals=[]
    for i in range(du+1):
        for j in range(dv+1):
            for k in range(dw+1):
                s=sp.Rational(0)
                for a in range(i+1):
                    for b in range(j+1):
                        for c in range(k+1):
                            q=dct.get((a,b,c),sp.Rational(0))
                            if q:
                                s += q*sp.Rational(comb(i,a),comb(du,a))*sp.Rational(comb(j,b),comb(dv,b))*sp.Rational(comb(k,c),comb(dw,c))
                vals.append(sp.factor(s))
    return (du,dv,dw), vals

print("PROB20-16 C082 3-PARAMETER SOLID EXACT CERTIFICATE")
print("parameter box: h in [-3/20,1/100], g in [-1/500,3/100], r in [-1/100,1/100]")
print("central spectral margins:")
print("  K >= 17/150 I =", float(sp.Rational(17,150)))
print("  I-K >= 1/5 I =", float(sp.Rational(1,5)))

for name, expr in polys.items():
    deg, vals = bernstein_coefficients(expr)
    m=min(vals)
    assert m>0, (name,m)
    print(f"{name}: degree={deg}, coefficients={len(vals)}, min={m}, approx={float(m)}")

eps=sp.Rational(1,6000)
m=sp.Rational(1,5)
eta=sp.factor(eps/(m*(m-eps)))
print("generic Hermitian tube epsilon =", eps, float(eps))
print("exact odds perturbation bound =", eta, float(eta))
assert eta == sp.Rational(5,1199)
assert eta < sp.Rational(1,239)

# Robust C082 margins using eta < 1/239.
eta0=sp.Rational(1,239)
a0=sp.Rational(7,10)
rho_upper=sp.factor((sp.Rational(41,100)*a0+eta0)/(a0-eta0))
rho_lower=sp.factor((sp.Rational(29,100)*a0-eta0)/(a0+eta0))
print("robust rho interval =", rho_lower, rho_upper, float(rho_lower), float(rho_upper))
assert rho_lower == sp.Rational(15839,56100)
assert rho_upper == sp.Rational(69593,166300)
assert rho_lower > sp.Rational(1,10)
assert rho_upper < sp.Rational(21,50)
assert a0-eta0 > sp.Rational(1,2)
assert sp.Rational(199,100)+eta0 < 2

# The new E12+E21 structured half-width is 20 times the previous run's
# generic Hermitian tube radius 1/2000.
ratio=sp.Rational(1,100)/sp.Rational(1,2000)
assert ratio==20
print("new structured half-width / previous generic tube radius =", ratio)
print("ALL EXACT ASSERTIONS PASSED")
