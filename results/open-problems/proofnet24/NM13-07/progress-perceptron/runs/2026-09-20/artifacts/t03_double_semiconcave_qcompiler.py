#!/usr/bin/env python3
"""
NM13-07 / T03, 2026-09-20.
Exact source microstep + exact outer semiconcavity algebra + numerical-only
falsification/conditioning checks for the double-semiconcave scalar-Q compiler.

Exact theorem proved in the accompanying report:
If U'' in [-ell,0] and
  q(a)=log E exp(m U(a+dG)),
then
  -m*ell/(1+m*ell*d^2) <= q''(a) <= 0.
For a(v)=b v-c this becomes q_vv in [-C,0],
  C=b^2*m*ell/(1+m*ell*d^2).
Hence on every V-cell [r,s], with L the chord of q,
  L(v) <= q(v) <= L(v)+C/2*(v-r)*(s-v).
This yields a derivative-free O(h^2) Gaussian-cell enclosure for Q=E q(V).
"""
from fractions import Fraction as F
import math
import numpy as np
import sympy as sp
from scipy.special import roots_hermitenorm, log_ndtr, logsumexp, ndtr
from scipy.integrate import quad

alphaL = F("6.30297437506")
alpha0 = F("12.319635")
alpha_before = F("12.31963444619075")
alpha_after  = F("12.3196344461907498")
gain = alpha_before-alpha_after
assert gain == F(1, 5_000_000_000_000_000)
dec = alpha0-alpha_after
assert F(446,1_000_000_000) <= dec <= F(554,1_000_000_000)
slope = F(4136629,105883920)
psi0 = F(23584189005311,1090044380000000000000)
psi_after = psi0-slope*dec
assert psi_after > 0
print("EXACT_SOURCE_MICROSTEP")
print("ALPHA_BEFORE", format(float(alpha_before), ".17g"))
print("ALPHA_AFTER", format(float(alpha_after), ".17g"))
print("GAIN_EXACT", gain, float(gain))
print("DEC_FROM_ANCHOR", dec, float(dec))
print("PSI_AFTER_LOWER_EXACT", psi_after, float(psi_after))
print("WIDTH_AFTER", format(float(alpha_after-alphaL), ".17g"))
print("EXACT_SOURCE_MICROSTEP_PASS")

m,ell,d,b = sp.symbols("m ell d b", positive=True)
L = 1/d**2 + m*ell
qaa_lower = sp.simplify(1/(L*d**4)-1/d**2)
target = -m*ell/(1+m*ell*d**2)
assert sp.simplify(qaa_lower-target)==0
Cv = sp.simplify(b**2*(-target))
assert sp.simplify(Cv-b**2*m*ell/(1+m*ell*d**2))==0
print("EXACT_OUTER_CURVATURE_ALGEBRA_PASS")

DEL=1e-3
vpar=np.array([0.0321710159451139,0.370106966023378,
               3.54218891058057,0.226621581517544],float)

def geom(v):
    w0,w1,x,m=map(float,v); w2=1-w0-w1
    y=1+m*(x-1)*w1/(x*w0)
    Z=x*y*y*w0+y*w1+w2
    S=math.sqrt(Z)/(x*y)
    lam=S/(S+DEL)
    xi=1+lam*(x-1)
    return w2,y,Z,S,lam,xi

def kernel(t,xi):
    t=np.asarray(t,float)
    l1=log_ndtr(-t)
    z=t/math.sqrt(xi)
    l2=-.5*math.log(xi)-(xi-1)*t*t/(2*xi)+log_ndtr(z)
    U=np.logaddexp(l1,l2)
    f2=np.exp(l2-U)
    phF=np.exp(-.5*t*t-.5*math.log(2*math.pi)-U)
    mu1=(t*f2+phF)/xi
    Ut=-(xi-1)*mu1
    return U,Ut

def ghn(n):
    z,w=roots_hermitenorm(n)
    mask=w>0
    return z[mask],w[mask]/math.sqrt(2*math.pi)

Uq,wu=ghn(400)
lwu=np.log(wu)
w0,w1,x,m0=map(float,vpar)
w2,y,Z,S,lam,xi=geom(vpar)
beta=xi-1
ell0=beta/xi
d2=w1/w0
b2=w2/w0
b0=math.sqrt(b2)
C=b2*m0*ell0/(1+m0*ell0*d2)
M3=math.sqrt(5)*(b0/math.sqrt(d2))**3

def q_and_qv(vv):
    T=math.sqrt(d2)*Uq+b0*vv-1/math.sqrt(w0)
    U,Ut=kernel(T,xi)
    lt=lwu+m0*U
    lz=logsumexp(lt)
    tw=np.exp(lt-lz)
    g=float(np.dot(tw,Ut))
    qv=b0*m0*g
    return float(lz),qv

print("WAYPOINT")
print("XI",xi,"ELL",ell0,"D2",d2,"B2",b2)
print("OUTER_CURVATURE_C",C)
print("OUTER_THIRD_DERIVATIVE_CAP_BL4",M3)

print("NUMERICAL_ONLY_QVV_CHECK")
for vv in (-5.,-3.,-1.,0.,1.,3.,5.):
    h=2e-4
    qm=q_and_qv(vv-h)[0]; q0=q_and_qv(vv)[0]; qp=q_and_qv(vv+h)[0]
    qvv=(qp-2*q0+qm)/(h*h)
    print("V",vv,"Q",q0,"QV",q_and_qv(vv)[1],"QVV_FD",qvv)
    assert qvv < 5e-6 and qvv > -C-5e-4

def phi(z):
    return math.exp(-z*z/2)/math.sqrt(2*math.pi)

def q_cell_bounds(N,R=6.):
    xs=np.linspace(-R,R,N+1)
    lower=upper=0.0
    for r,s in zip(xs[:-1],xs[1:]):
        qr=q_and_qv(float(r))[0]
        qs=q_and_qv(float(s))[0]
        h=s-r
        P=ndtr(s)-ndtr(r)
        Iv=phi(r)-phi(s)
        sec=(qs-qr)/h
        chord_int=qr*P+sec*(Iv-r*P)
        Iv2=r*phi(r)-s*phi(s)+P
        quad = -Iv2 + (r+s)*Iv - r*s*P
        lower += chord_int
        upper += chord_int + .5*C*quad
    return lower,upper

qref,err=quad(lambda z:q_and_qv(z)[0]*phi(z),-6,6,
              epsabs=2e-13,epsrel=2e-13,limit=400)
print("NUMERICAL_ONLY_TRUNCATED_Q_REFERENCE",qref,"QUADERR",err)
for N in (50,100,200,400,800,1600):
    lo,up=q_cell_bounds(N)
    print("NUMERICAL_ONLY_Q_SECANT_CELL",
          N,"LOWER",lo,"UPPER",up,"WIDTH",up-lo,
          "CONTAINS_REF",lo<=qref<=up)
    assert lo <= qref+2e-11 and qref <= up+2e-11

print("NUMERICAL_ONLY_CENTRAL_SECANT_QV")
for hh in (0.1,0.05,0.02):
    cap=M3*hh*hh/6
    worst=0.0
    for vv in np.linspace(-4,4,17):
        sec=(q_and_qv(vv+hh)[0]-q_and_qv(vv-hh)[0])/(2*hh)
        true=q_and_qv(vv)[1]
        errv=abs(sec-true)
        worst=max(worst,errv)
        assert errv <= cap+2e-8
    print("H",hh,"THEORETICAL_CAP",cap,"WORST_OBSERVED",worst)

print("ALL_EXACT_AND_NUMERICAL_DOUBLE_SEMICONCAVITY_CHECKS_PASS")
