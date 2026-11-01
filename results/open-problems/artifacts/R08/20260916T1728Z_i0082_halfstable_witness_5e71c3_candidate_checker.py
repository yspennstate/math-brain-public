#!/usr/bin/env python3
# R08 I0082 candidate checker: positive free 1/2-stable law.
# Symbolic algebra + validated interval Krawczyk boxes for one explicit unimodal witness.

import sympy as sp
import mpmath as mp
from mpmath import iv

mp.mp.dps = 50

# --- Obligation 1/2 symbolic checks ---
x=sp.symbols('x', positive=True)
f=sp.sqrt(4*x-1)/(2*sp.pi*x**2)
logder=sp.simplify(sp.diff(sp.log(f),x))
assert sp.factor(logder - 2*(1-3*x)/(x*(4*x-1))) == 0
print("candidate_density_logderivative =", sp.factor(logder))
print("candidate_mode = 1/3; support [1/4, infinity); non-Dirac probability law (normalization proven on page)")

# --- Cauchy / semicircle stress-family exact algebra ---
b,t=sp.symbols('b t', positive=True)
theta = b*(b+1)/2 * sp.sqrt((4*b+1)/(4*b+3))
dlog = sp.simplify(sp.diff(sp.log(theta),b))
expected = 1/b + 1/(b+1) + 2/(4*b+1) - 2/(4*b+3)
assert sp.simplify(dlog-expected)==0
# Positive derivative after common denominator.
num=sp.factor(sp.together(dlog).as_numer_denom()[0])
den=sp.factor(sp.together(dlog).as_numer_denom()[1])
print("Theta(b) =", theta)
print("dlogTheta numerator =", num)
print("dlogTheta denominator =", den)
assert all(c >= 0 for c in sp.Poly(num,b).all_coeffs())
print("Cauchy_stress_exact_monotonicity = PASS")

# --- Explicit unimodal witness nu = .03 delta_0 + .0194 1_(0,50) dx ---
p = mp.mpf(3)/100
B = mp.mpf(50)
c = (1-p)/B  # 97/5000

def Gnu(z):
    return p/z + c*mp.log(z/(z-B))

def Gnu_iv(z):
    return iv.mpf([3,3])/100/z + iv.mpf([97,97])/5000*iv.log(z/(z-50))

def H(q, xx):
    z=xx+1j*q
    return q*q*Gnu(z)-1

def Hp(q, xx):
    z=xx+1j*q
    gp = -p/(z*z) + c*(1/z - 1/(z-B))
    return 2*q*Gnu(z) + 1j*q*q*gp

def H_iv(q, xx):
    z=iv.mpc([xx,xx],[0,0]) + iv.mpc([0,0],[1,1])*q
    return q*q*Gnu_iv(z)-1

def Hp_iv(q, xx):
    z=iv.mpc([xx,xx],[0,0]) + iv.mpc([0,0],[1,1])*q
    pp=iv.mpf([3,3])/100
    cc=iv.mpf([97,97])/5000
    gp=-pp/(z*z)+cc*(1/z-1/(z-50))
    return 2*q*Gnu_iv(z)+iv.mpc(0,1)*q*q*gp

cases=[
    (mp.mpf(16)/5, mp.mpc("1.110053865109794","3.098668028111616")),
    (mp.mpf(61)/10, mp.mpc("1.619686910133982","3.401326945393118")),
    (mp.mpf(43)/2, mp.mpc("2.714477792390544","3.172448118363714")),
]
rad=mp.mpf("1e-5")

density_boxes=[]
for xx,q0 in cases:
    qr=iv.mpf([mp.re(q0)-rad, mp.re(q0)+rad])
    qi=iv.mpf([mp.im(q0)-rad, mp.im(q0)+rad])
    X=iv.mpc(qr,qi)
    h0=H(q0,xx)
    hp0=Hp(q0,xx)
    K = iv.mpc([mp.re(q0-h0/hp0),mp.re(q0-h0/hp0)],[mp.im(q0-h0/hp0),mp.im(q0-h0/hp0)]) + (1 - Hp_iv(X,xx)/iv.mpc([mp.re(hp0),mp.re(hp0)],[mp.im(hp0),mp.im(hp0)]))*(X-iv.mpc([mp.re(q0),mp.re(q0)],[mp.im(q0),mp.im(q0)]))
    xr=(mp.re(q0)-rad,mp.re(q0)+rad); xi=(mp.im(q0)-rad,mp.im(q0)+rad)
    kr=(mp.mpf(K.real.a),mp.mpf(K.real.b))
    ki=(mp.mpf(K.imag.a),mp.mpf(K.imag.b))
    assert xr[0] < kr[0] and kr[1] < xr[1]
    assert xi[0] < ki[0] and ki[1] < xi[1]
    dens = -(iv.mpf([1,1])/iv.pi) * (1/(X*X)).imag
    db=(mp.mpf(dens.a),mp.mpf(dens.b))
    density_boxes.append(db)
    print("x =", mp.nstr(xx,20))
    print("X real =", mp.nstr(xr[0],20), mp.nstr(xr[1],20))
    print("X imag =", mp.nstr(xi[0],20), mp.nstr(xi[1],20))
    print("K real =", mp.nstr(kr[0],20), mp.nstr(kr[1],20))
    print("K imag =", mp.nstr(ki[0],20), mp.nstr(ki[1],20))
    print("density =", mp.nstr(db[0],20), mp.nstr(db[1],20))
    print("residual_center =", mp.nstr(abs(h0),12))

assert density_boxes[0][0] > density_boxes[1][1]
assert density_boxes[2][0] > density_boxes[1][1]
print("strict_valley = PASS")
print("candidate_not_FSU_for_this_explicit_unimodal_witness = PASS")
print("ALL_CANDIDATE_CHECKS_PASS")
