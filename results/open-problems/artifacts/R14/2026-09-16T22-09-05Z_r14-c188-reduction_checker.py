#!/usr/bin/env python3
import sympy as sp
from fractions import Fraction

print('R14-C188 exact 2-sfl reduction / route-obstruction checker')

# Closed-form r=2 full-stationarity identities from Stojnic (84)-(90).
r,q = sp.symbols('r q', positive=True)
p = q*r**2
gp = sp.Rational(1,2)*(1-q)/(1-p)*r
c = r/(1-p) - 1/(r*(1-q))
D = sp.simplify(2*gp - c*(1-q))
assert sp.simplify(D - 1/r) == 0
assert sp.simplify(q/D**2 - p) == 0
assert sp.simplify((1-q)/(2*gp*D) + q/D**2 - 1) == 0
print('Stojnic (84)-(90) closed relations: PASS')

# c_q at fixed p is strictly negative. Introduce s=sqrt(q/p)>0.
p0,q0,s = sp.symbols('p0 q0 s', positive=True)
# with ds/dq = s/(2q), c=1/(s(1-p))-s/(1-q)
dsdq = s/(2*q0)
cq_formula = -dsdq/(s**2*(1-p0)) - dsdq/(1-q0) - s/(1-q0)**2
cq_target = -1/(2*q0*s*(1-p0)) - s/(2*q0*(1-q0)) - s/(1-q0)**2
assert sp.simplify(cq_formula-cq_target)==0
print('Partial c_q formula: PASS; every term is strictly negative on 0<q<p<1')

# Chain rule reduction: if source relations force F_q=F_gp=0,
# reduced q-stationarity plus c_q != 0 forces F_c=0; then reduced
# p-stationarity forces F_p=0, and reduced gamma derivative equals F_gamma.
Fp,Fq,Fc,Fg,Fgp,cp,cq,gpp,gpq = sp.symbols('Fp Fq Fc Fg Fgp cp cq gpp gpq')
dtp = Fp + Fc*cp + Fgp*gpp
dtq = Fq + Fc*cq + Fgp*gpq
assert sp.simplify(dtq.subs({Fq:0,Fgp:0}) - Fc*cq) == 0
assert sp.simplify(dtp.subs({Fgp:0,Fc:0}) - Fp) == 0
print('Three-variable reduced-gradient chain rule: PASS')

# Retained bracket arithmetic: no metric movement this run.
alphaL=Fraction(630297437506,10**11)
alphaU=Fraction(1278437096216,10**11)
width=alphaU-alphaL
assert width==Fraction(64813965871,10**10)
print('Frozen bracket arithmetic: PASS')
print(' alpha_L =', float(alphaL))
print(' alpha_U =', float(alphaU))
print(' width =', width, '=', float(width))
print('ALL_EXACT_CHECKS_PASS')
