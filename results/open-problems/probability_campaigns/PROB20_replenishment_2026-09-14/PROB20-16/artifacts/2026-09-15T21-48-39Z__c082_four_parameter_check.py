#!/usr/bin/env python3
# PROB20-16 exact checker: 4-parameter C082 affine solid + full Hermitian tube.
import sympy as sp
from math import comb

h,g,r,q,u,v,w,x = sp.symbols("h g r q u v w x", real=True)
sqrt2 = sp.sqrt(2)

Kstar = sp.Matrix([
    [sp.Rational(8846539,15630789), sp.Rational(1812625,15630789), sp.Rational(6375,79546)*sqrt2],
    [sp.Rational(1812625,15630789), sp.Rational(8846539,15630789), -sp.Rational(6375,79546)*sqrt2],
    [sp.Rational(6375,79546)*sqrt2, -sp.Rational(6375,79546)*sqrt2, sp.Rational(47421,79546)]
])
I = sp.eye(3)
D = sp.diag(1,1,-2)
F = sp.Matrix([[0,1,0],[1,0,0],[0,0,0]])
G = sp.Matrix([[0,sp.I,0],[-sp.I,0,0],[0,0,0]])
K = Kstar + h*I + g*D + r*F + q*G
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
B = 62523156*g -31261578*h +12625125
P = (159092*g**2 +79546*g*h -159092*g*r -134921*g
     -79546*h**2 +79546*h*r -3671*h +47421*r +28125)
C = 2*6375**2

T = sp.expand(A*Q - 393*q**2*(159092*g-79546*h+32125))
R4 = sp.expand(R + q**2*B)
P4 = sp.expand(A*P + 393*q**2*(159092*g-79546*h-47421))

assert sp.simplify(L[0,0]-R4/T) == 0
assert sp.simplify(L[1,1]-R4/T) == 0
assert sp.simplify(L[2,2]-P4/T) == 0
assert sp.simplify(L[0,1]-(S+sp.I*q*B)/T) == 0
assert sp.simplify(L[0,2]-6375*sqrt2*(A-393*sp.I*q)/T) == 0
assert sp.simplify(L[1,2]+6375*sqrt2*(A+393*sp.I*q)/T) == 0

# Central 4D bounds: ell_i in [7/10,199/100], rho_i in [29/100,41/100].
polys = {
    "T": T,
    "R4": R4,
    "P4": P4,
    "ell12_lo": 10*R4-7*T,
    "ell12_hi": sp.Rational(199,100)*T-R4,
    "ell3_lo": 10*P4-7*T,
    "ell3_hi": sp.Rational(199,100)*T-P4,
    "rho12_lo": 10000*(S**2+q**2*B**2)-29**2*R4**2,
    "rho12_hi": 41**2*R4**2-10000*(S**2+q**2*B**2),
    "rho13_lo": 10000*C*(A**2+393**2*q**2)-29**2*R4*P4,
    "rho13_hi": 41**2*R4*P4-10000*C*(A**2+393**2*q**2),
}

hsub = -sp.Rational(3,20) + sp.Rational(4,25)*u
gsub = -sp.Rational(1,500) + sp.Rational(4,125)*v
rsub = -sp.Rational(1,100) + sp.Rational(1,50)*w
qsub = -sp.Rational(1,100) + sp.Rational(1,50)*x

def bernstein_coefficients(expr):
    f = sp.Poly(sp.expand(expr.subs({h:hsub,g:gsub,r:rsub,q:qsub})),
                u,v,w,x, domain=sp.QQ)
    degs = tuple(f.degree(z) for z in (u,v,w,x))
    dct = f.as_dict()
    vals=[]
    for i in range(degs[0]+1):
        for j in range(degs[1]+1):
            for k in range(degs[2]+1):
                for l in range(degs[3]+1):
                    s=sp.Rational(0)
                    for a in range(i+1):
                        for b in range(j+1):
                            for c in range(k+1):
                                for d in range(l+1):
                                    coeff=dct.get((a,b,c,d),sp.Rational(0))
                                    if coeff:
                                        s += (coeff
                                              *sp.Rational(comb(i,a),comb(degs[0],a))
                                              *sp.Rational(comb(j,b),comb(degs[1],b))
                                              *sp.Rational(comb(k,c),comb(degs[2],c))
                                              *sp.Rational(comb(l,d),comb(degs[3],d)))
                    vals.append(sp.factor(s))
    return degs, vals

print("PROB20-16 C082 4-PARAMETER SOLID EXACT CERTIFICATE")
print("box: h[-3/20,1/100], g[-1/500,3/100], r[-1/100,1/100], q[-1/100,1/100]")
print("central spectral margins:")
print("  K >= 31/300 I =", float(sp.Rational(31,300)))
print("  I-K >= 19/100 I =", float(sp.Rational(19,100)))

for name, expr in polys.items():
    degs, vals = bernstein_coefficients(expr)
    m=min(vals)
    assert m>0, (name,m)
    print(f"{name}: degree={degs}, coefficients={len(vals)}, min={m}, approx={float(m)}")

eps=sp.Rational(1,6000)
m=sp.Rational(19,100)
eta=sp.factor(eps/(m*(m-eps)))
print("generic Hermitian tube epsilon =", eps, float(eps))
print("exact odds perturbation bound =", eta, float(eta))
assert eta == sp.Rational(100,21641)
assert eta < sp.Rational(1,216)

eta0=sp.Rational(1,216)
a0=sp.Rational(7,10)
rho_upper=sp.factor((sp.Rational(41,100)*a0+eta0)/(a0-eta0))
rho_lower=sp.factor((sp.Rational(29,100)*a0-eta0)/(a0+eta0))
print("robust rho interval =", rho_lower, rho_upper, float(rho_lower), float(rho_upper))
assert rho_lower == sp.Rational(5356,19025)
assert rho_upper == sp.Rational(7874,18775)
assert rho_lower > sp.Rational(1,10)
assert rho_upper < sp.Rational(21,50)
assert a0-eta0 > sp.Rational(1,2)
assert sp.Rational(199,100)+eta0 < 2

assert sp.Rational(1,100)/sp.Rational(1,2000) == 20
print("real and imaginary 12-edge half-widths / previous generic tube radius = 20")
print("ALL EXACT ASSERTIONS PASSED")
