#!/usr/bin/env python3
"""Exact/interval certificate for the P10 arbitrary-orbit KS radius improvement."""
import sympy as sp
import mpmath as mp

# ---------- exact fifth-order harmonic bound ----------
s2 = sp.sqrt(2)
a = -sp.Rational(9,16) + 9*s2/sp.Integer(64)
b = 21*s2/sp.Integer(16)
C5 = sp.simplify(sp.Rational(4,27)*(a+b))
assert sp.simplify(C5 - (-sp.Rational(1,12)+31*s2/sp.Integer(144))) == 0
assert a < 0 and b > 0 and a+b > 0 and b+3*a > 0

t = sp.symbols('t', nonnegative=True)
# If a+b*t^2 >= 0, the desired numerator comparison factors as follows.
D_hi = sp.expand((a+b)*(1+t**4) - (a+b*t**2 + t**3*(b+a*t**2)))
assert sp.simplify(D_hi - (1-t)*(a*t**4 - b*t**3 + b*t + b)) == 0
# The factor in parentheses is >= a+b > 0 on 0<=t<=1 because
# b(1+t-t^3)>=b and a*t^4>=a.

# If a+b*t^2 < 0, after removing the absolute value:
D_lo = sp.expand((a+b)*(1+t**4) - (-a-b*t**2 + t**3*(b+a*t**2)))
assert sp.simplify(D_lo - (a*(2+t**4-t**5)+b*(1+t**2-t**3+t**4))) == 0
# Here 1+t^2-t^3+t^4>=1 and 2+t^4-t^5<=3, so D_lo>=b+3a>0.

# ---------- exact sixth-order coercivity ----------
# With r>=s, t=s/r and angular cosines c,d, 360 H6/r^6 equals
# 27(1+t^6)+10(t^2+t^4)+6c^2+6t^6 d^2-60 t^3 c d.
# We prove H6 >= 13/360*(r^6+s^6).
D_boundary = 20*(1+t**6) + 10*(t**2+t**4) - 60*t**3
assert sp.factor(D_boundary) == 10*(t-1)**2*(2*t**4+4*t**3+7*t**2+4*t+2)
# For t^3<=1/5, completing the square gives angular part >= -144 t^6,
# hence the residual after subtracting 13(1+t^6) is
D_small = 14 + 10*t**2 + 10*t**4 - 130*t**6
# Since t^6<=1/25, D_small >= 14-130/25 = 44/5 >0.
assert sp.Rational(14) - sp.Rational(130,25) == sp.Rational(44,5)
# For t^3>=1/5, minimizing the convex quadratic over |c|,|d|<=1
# gives c=d=sign, yielding D_boundary>=0 above.

# Convert r^6+s^6 into rho^2(r^4+s^4): for x=t^2 in [0,1],
# (1+t^6)/(1+t^4) >= 8/9.
x = sp.symbols('x', nonnegative=True)
radial_poly = 1 - 8*x**2 + 9*x**3
crit = sp.Rational(16,27)
assert sp.diff(radial_poly,x).subs(x,crit) == 0
assert sp.simplify(radial_poly.subs(x,crit)) == sp.Rational(139,2187)
C6 = sp.Rational(13,360)*sp.Rational(8,9)
assert C6 == sp.Rational(13,405)

# ---------- self-contained analytic tail bound at rho=33/250 ----------
mp.mp.dps = 80
iv = mp.iv
rho = iv.mpf(33)/250
R = rho**2
SQ2 = iv.sqrt(2)
C5iv = -iv.mpf(1)/12 + 31*SQ2/144
C6iv = iv.mpf(13)/405

# Endpoint entropy tails: 1/2 D(p)+1/2 D(q) and -D(T_*p)-D(T_*q).
Ce = (iv.mpf(32)/21)/(1-2*rho) + (iv.mpf(64)/21)*(iv.mpf(2)**(-iv.mpf(7)/2))/(1-SQ2*rho)

# KL fusion interaction tail after c^2,c^3.
Cjd = rho/(24*(1-rho**2))

# Denominator tail constants for (1+c)^-2 and (1+c)^-3, |c|<=R.
C21 = (3-2*R)/(1-R)**2
C20 = (2-R)/(1-R)**2
C31 = (6-8*R+3*R**2)/(1-R)**3
C30 = (3-3*R+R**2)/(1-R)**3
inv3 = 1/(1-R)**3

# Coarse per-orbit polynomial tail, independent of any previous rho=0.1 optimization.
# L=(m+gn)/sqrt(2), Q=conj(m)conj(gn)/2, so |L|<=sqrt(2)rho,
# |Q|<=rho^2/2 and |c|<=rho^2. Expanding numerator degree and denominator
# series gives the following coefficients after division by rho^3(r^4+s^4),
# using r^4+s^4>=rho^4.
Ccub = (iv.mpf(1)/3)*(C21*(2*SQ2+3*rho) + C20*(3*SQ2/4+rho/8))
Cquart = (iv.mpf(2)/9)*(C31*(4*rho) + C30*(4*SQ2+3*rho) + inv3*(SQ2/2+rho/16))
Cjp = Ccub + Cquart
Ctail = Ce + Cjd + Cjp

# H4 >= S4/18; |H5|<=C5*rho*S4; H6>=C6*rho^2*S4;
# |R_{>=7}|<=Ctail*rho^3*S4.
margin = iv.mpf(1)/18 - C5iv*rho + C6iv*rho**2 - Ctail*rho**3

print('alpha', a)
print('beta', b)
print('C5_sharp', C5)
print('beta_plus_3alpha', sp.simplify(b+3*a))
print('C6_rho2', C6)
print('rho', rho)
print('Ce', Ce)
print('Cjd', Cjd)
print('Cjp_coarse', Cjp)
print('Ctail_coarse', Ctail)
print('margin', margin)
assert margin.a > mp.mpf('0.00043')
print('OVERALL_PASS')
