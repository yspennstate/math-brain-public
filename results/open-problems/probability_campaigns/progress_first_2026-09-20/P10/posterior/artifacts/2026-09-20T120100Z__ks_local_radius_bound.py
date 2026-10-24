#!/usr/bin/env python3
"""Outward-rounded constants for a quantitative arbitrary-orbit KS contraction ball in P10/F0119."""
import sympy as sp
import mpmath as mp

s2=sp.sqrt(2)
alpha=-sp.Rational(9,16)+9*s2/sp.Integer(64)
beta=21*s2/sp.Integer(16)
C5=sp.simplify(sp.Rational(4,27)*(-alpha+beta))
assert sp.simplify(C5-(sp.Rational(1,12)+25*s2/sp.Integer(144)))==0

# Sixth-order form positivity.  With |C_x|<=A^(3/2)/sqrt(6),
# after dropping the positive 27/80(C_x^2+C_y^2) term and writing t=sqrt(A/B),
# 320 times the remaining normalized lower bound is
# P(t)=81(t^6+1)+30(t^4+t^2)-180t^3.
# Dividing by t^3 and setting s=t+t^{-1}>=2 gives Q(s)=81s^3-213s-180.
s=sp.symbols('s', real=True)
Q=81*s**3-213*s-180
assert Q.subs(s,2)==42
assert sp.diff(Q,s).subs(s,2)>0

mp.mp.dps=80
iv=mp.iv
rho=iv.mpf(1)/10
Rmax=rho**2
SQ2=iv.sqrt(2)

# Tail of the one-edge entropy series after degrees <=6.
Ce=(iv.mpf(32)/21)/(1-2*rho)+(iv.mpf(64)/21)*(2**(-3.5))/(1-SQ2*rho)

# Tail of the KL fusion interaction after c^2 and c^3, using |c|<=rho^2.
Cjd=rho/(24*(1-rho**2))

# Tail of the polynomial fusion interaction after total degree <=6.
# Exact denominator remainders for (1-c)^-2 and (1-c)^-3 are bounded at c=rho^2.
C21=(3-2*Rmax)/(1-Rmax)**2
C20=(2-Rmax)/(1-Rmax)**2
C31=(6-8*Rmax+3*Rmax**2)/(1-Rmax)**3
C30=(3-3*Rmax+Rmax**2)/(1-Rmax)**3
inv3=1/(1-Rmax)**3
Ccub=(iv.mpf(1)/3)*(C21*(SQ2+iv.mpf('0.15'))+C20*(3*SQ2/8+iv.mpf('0.00625')))
Cquart=(iv.mpf(2)/9)*(C31*iv.mpf('0.2')+C30*(2*SQ2+iv.mpf('0.15'))+inv3*(SQ2/4+iv.mpf('0.003125')))
Cjp=Ccub+Cquart
Ctail=Ce+Cjd+Cjp

C5iv=iv.mpf(1)/12+25*SQ2/144
# H4 >= (r^4+s^4)/18; H6>=0; |H5|<=C5*rho*(r^4+s^4);
# |R_{>=7}|<=Ctail*rho^3*(r^4+s^4).
margin=iv.mpf(1)/18-C5iv*rho-Ctail*rho**3

print('alpha',alpha)
print('beta',beta)
print('C5',C5)
print('H6_reduced_Q_at_2',Q.subs(s,2))
print('Ce',Ce)
print('Cjd',Cjd)
print('Cjp',Cjp)
print('Ctail',Ctail)
print('margin',margin)
assert Ctail.b<mp.mpf('6.551')
assert margin.a>mp.mpf('0.0161')
print('OVERALL_PASS')
