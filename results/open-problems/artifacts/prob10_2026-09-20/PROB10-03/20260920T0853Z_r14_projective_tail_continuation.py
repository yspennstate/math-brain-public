#!/usr/bin/env python3
"""
R14 / PROB10-03, 20 Sep 2026.

Exact symbolic checks for:
  (i) projective slope-simplex normal form of the complete-third q-sector;
  (ii) simplified algebraic c-sector terms A_c2,A_c3;
  (iii) prescribed-gap B reconstruction.

A small numerical-only falsification block checks the sharp kernel curvature
bound and the coordinate reconstruction at the previously archived delta=1e-3
third-full scout. Numerical values are NOT source endpoints.
"""
import math
import sympy as sp
import numpy as np
from scipy.special import ndtr

w0,w1,w2,x,y,Z,delta = sp.symbols('w0 w1 w2 x y Z delta', positive=True)
Zdef = x*y**2*w0 + y*w1 + w2
r2 = 1/Z
r1 = y/Z
r0 = x*y**2/Z

p2 = 1-w0
p3 = w2
q3 = r2*w2
q2 = r1*w1+r2*w2

assert sp.simplify((w0+w1+w2-1).subs(w1,1-w0-w2)) == 0
assert sp.simplify((r0*w0+r1*w1+r2*w2-1).subs(Z,Zdef)) == 0
assert sp.simplify((r1/r2)-y) == 0
assert sp.simplify((r0*r2/r1**2)-x) == 0

c3_orig = sp.sqrt(p3/q3)/(p2-p3) - sp.sqrt(q3/p3)/(q2-q3)
gp_orig = sp.Rational(1,2)*(1-q2)/(1-p2)*(p2-p3)/(q2-q3)*sp.sqrt(q3/p3)
c2_orig = ((p2-p3)/(q2-q3)*sp.sqrt(q3/p3))/(1-p2) \
        - ((q2-q3)/(p2-p3)*sp.sqrt(p3/q3))/(1-q2)

c3_new = (y-1)*sp.sqrt(Z)/(y*w1)
gp_new = x*y/(2*sp.sqrt(Z))
c2_new = (x-1)*sp.sqrt(Z)/(x*y*w0)

def simp_geom(e):
    return sp.simplify(e.subs(Z,Zdef).subs(w1,1-w0-w2))

assert simp_geom(c3_orig-c3_new) == 0
assert simp_geom(gp_orig-gp_new) == 0
assert simp_geom(c2_orig-c2_new) == 0

Aq_orig = 2*gp_new - c2_new*(1-q2)
Dq_orig = Aq_orig - c3_new*(q2-q3)
Aq_new = y/sp.sqrt(Z)
Dq_new = 1/sp.sqrt(Z)
assert simp_geom(Aq_orig-Aq_new) == 0
assert simp_geom(Dq_orig-Dq_new) == 0
assert simp_geom(Aq_new/(2*gp_new)-1/x) == 0
assert simp_geom(Dq_new/Aq_new-1/y) == 0

S_orig = r1/(r0*sp.sqrt(r2))
S_new = sp.sqrt(Z)/(x*y)
assert sp.simplify(S_orig-S_new) == 0

B_orig = c2_new/(2*(S_new+delta))
B_new = (x-1)*sp.sqrt(Z)/(2*w0*(sp.sqrt(Z)+delta*x*y))
assert sp.simplify(B_orig-B_new) == 0
assert sp.simplify(B_new.subs(delta,0)-(x-1)/(2*w0)) == 0

m_new = sp.simplify(c3_new/c2_new)
m_target = x*(y-1)*w0/((x-1)*w1)
assert sp.simplify(m_new-m_target) == 0

Ac3_orig = (sp.Rational(1,2)*(p2*q2-p3*q3)
            - sp.log(Dq_new/Aq_new)/(2*c3_new**2)
            - (q2-q3)/(2*c3_new*Dq_new)
            - q3*(q2-q3)/(2*Dq_new**2))
Ac2_orig = (sp.Rational(1,2)*(1-p2*q2)
            - sp.log(Aq_new/(2*gp_new))/(2*c2_new**2)
            - (1-q2)/(2*c2_new*Aq_new)
            + (1-q2)/(2*c3_new)*(1/Aq_new-1/Dq_new)
            - q3*(1-q2)/(2*Dq_new**2))

k_y = y*(y*sp.log(y)-y+1)/(y-1)**2
h_x = x*(x-1-sp.log(x))/(x-1)**2
Ac3_new = w1/(2*Z)*(w2+w1*k_y)
Ac2_new = w0/sp.Integer(2)*(1-(x*y**2*w0/Z)*h_x)

assert simp_geom(Ac3_orig-Ac3_new) == 0
assert simp_geom(Ac2_orig-Ac2_new) == 0

p2n=0.967828984055228
p3n=0.597722018031788
q2n=0.638663550092673
q3n=0.229918637629570
B=39.26289564113617
w0n=1-p2n; w1n=p2n-p3n; w2n=p3n
r2n=q3n/w2n
r1n=(q2n-q3n)/w1n
r0n=(1-q2n)/w0n
xn=r0n*r2n/(r1n*r1n)
yn=r1n/r2n
Zn=xn*yn*yn*w0n+yn*w1n+w2n

q3_rec=w2n/Zn
q2_rec=(yn*w1n+w2n)/Zn
assert abs(q3_rec-q3n) < 5e-15
assert abs(q2_rec-q2n) < 5e-15

c2rec=(xn-1)*math.sqrt(Zn)/(xn*yn*w0n)
c3rec=(yn-1)*math.sqrt(Zn)/(yn*w1n)
gprec=xn*yn/(2*math.sqrt(Zn))
assert abs(c2rec-12.52805599281815) < 2e-6
assert abs(c3rec-2.839127862412615) < 2e-6
assert abs(gprec-3.153765242988234) < 2e-6

s=math.sqrt(1-p2n)
A=1+2*B*s*s

def phi(t):
    return math.exp(-0.5*t*t)/math.sqrt(2*math.pi)

def uxx(mu):
    J0=A**(-0.5)*math.exp(-B*mu*mu/A)*ndtr(mu/(s*math.sqrt(A)))
    J1=(mu*J0+s*phi(mu/s))/A
    J2=(mu/A)*J1+(s*s/A)*J0
    f=ndtr(-mu/s)+J0
    fm=-2*B*J1
    fmm=-2*B*J0+4*B*B*J2
    return fmm/f-(fm/f)**2

lower=-2*B/A
vals=[]
for mu in np.linspace(-1.5,4.0,111):
    v=uxx(float(mu))
    vals.append(v)
    assert v >= lower-5e-10
    assert v <= 5e-10

print("EXACT_PROJECTIVE_QSECTOR_PASS")
print("EXACT_AQ_DQ_LOGRATIOS_PASS")
print("EXACT_CSECTOR_NORMALFORM_PASS")
print("EXACT_POSGAP_B_RECONSTRUCTION_PASS")
print("NUMERICAL_ONLY x y Z", xn, yn, Zn)
print("NUMERICAL_ONLY curvature_lower", lower, "grid_min", min(vals), "grid_max", max(vals))
print("ALL_EXACT_SYMBOLIC_CHECKS_PASS")
print("ALL_NUMERICAL_FALSIFICATION_CHECKS_PASS")
