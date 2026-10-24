#!/usr/bin/env python3
from fractions import Fraction as F
import math, numpy as np
from numpy.polynomial.hermite import hermgauss
from scipy.special import log_ndtr, logsumexp, ndtr

# Exact inherited complete-second transport microstep.
alphaL=F(315148718753,50_000_000_000)
alpha0=F(12319635,1_000_000)
alpha_before=F(30799086115477,2_500_000_000_000) # 12.3196344461908
alpha_after=F(49278537784763,4_000_000_000_000)  # 12.31963444619075
slope=F(4136629,105883920)
psi0=F(23584189005311,1090044380000000000000)
assert alpha_before-alpha_after == F(1,20_000_000_000_000)
dec=alpha0-alpha_after
assert F(446,1_000_000_000) <= dec <= F(554,1_000_000_000)
psi=psi0-slope*dec
assert psi>0
print('EXACT_SOURCE_MICROSTEP')
print('ALPHA_BEFORE', float(alpha_before))
print('ALPHA_AFTER', float(alpha_after))
print('GAIN_EXACT', alpha_before-alpha_after, float(alpha_before-alpha_after))
print('DEC_FROM_ANCHOR', dec, float(dec))
print('PSI_LOWER_EXACT', psi, float(psi))
print('WIDTH_AFTER', float(alpha_after-alphaL))

# Archived positive-gap waypoint, numerical-only.
w0=0.0321710159451139; w1=0.370106966023378
x=3.54218891058057; m=0.226621581517544
DEL=1e-3
w2=1-w0-w1
y=1+m*(x-1)*w1/(x*w0)
Z=x*y*y*w0+y*w1+w2
S=math.sqrt(Z)/(x*y); lam=S/(S+DEL); xi=1+lam*(x-1)
beta=xi-1; ell=beta/(1+beta); d=math.sqrt(w1/w0)

# Closed hinge kernel.
def kernel(t):
    t=np.asarray(t,float)
    l1=log_ndtr(-t)
    z=t/math.sqrt(xi)
    l2=-.5*math.log(xi)-(xi-1)*t*t/(2*xi)+log_ndtr(z)
    U=np.logaddexp(l1,l2)
    f2=np.exp(l2-U)
    phF=np.exp(-.5*t*t-.5*math.log(2*math.pi)-U)
    mu1=(t*f2+phF)/xi
    mu2=(t*mu1+f2)/xi
    Ut=-(xi-1)*mu1
    return U,Ut,mu2

def exp_quad_cell(A,b,c,r,s,u0):
    aa=1+c
    lin=b+c*u0
    const=A-b*u0-0.5*c*u0*u0 + lin*lin/(2*aa)
    h=lin/aa
    return math.exp(const)/math.sqrt(aa)*(ndtr(math.sqrt(aa)*(s-h))-ndtr(math.sqrt(aa)*(r-h)))

def q_bounds(v,ncell,R=8.0):
    a=math.sqrt(w2/w0)*v-1/math.sqrt(w0)
    edges=np.linspace(-R,R,ncell+1)
    zl=0.0; zu=0.0
    c=m*ell*d*d
    for r,s in zip(edges[:-1],edges[1:]):
        u0=(r+s)/2
        t0=a+d*u0
        U0,Ut0,_=kernel(np.array([t0]))
        A=m*float(U0[0]); b=m*d*float(Ut0[0])
        zl += exp_quad_cell(A,b,c,r,s,u0)
        zu += exp_quad_cell(A,b,0.0,r,s,u0)
    # e^{mU} <= 1 on the omitted two tails.
    zu += 2*(1-ndtr(R))
    return math.log(zl), math.log(zu)

def q_gh(v,n=240):
    z,w=hermgauss(n); u=np.sqrt(2)*z; ww=w/np.sqrt(np.pi)
    a=math.sqrt(w2/w0)*v-1/math.sqrt(w0)
    U,_,_=kernel(a+d*u)
    return float(logsumexp(np.log(ww)+m*U))

# Numerical falsification of semiconcavity via second finite differences.
ts=np.linspace(-10,10,401); h=1e-4
Um=kernel(ts-h)[0]; U0=kernel(ts)[0]; Up=kernel(ts+h)[0]
sec=(Up-2*U0+Um)/h**2
print('NUMERICAL_ONLY_SEMICONCAVITY')
print('ELL',ell)
print('UXX_MIN',float(sec.min()),'UXX_MAX',float(sec.max()))
assert sec.min() > -ell-2e-5 and sec.max() < 2e-5

print('NUMERICAL_ONLY_CELL_COMPILER')
for v in (0.0,4.0):
    qref=q_gh(v)
    print('V',v,'Q_GH240',qref)
    prev=None
    for n in (100,200,400,800,1600):
        lo,up=q_bounds(v,n)
        width=up-lo
        print('NCELL',n,'LOW',lo,'UP',up,'WIDTH',width,'CONTAINS_GH',lo<=qref<=up)
        assert lo <= qref+2e-12 and qref <= up+2e-12
        if prev is not None:
            # widths should decay close to second order for the partition function enclosure.
            print('WIDTH_RATIO_PREV_OVER_CURR',prev/width)
        prev=width
print('ALL_EXACT_AND_NUMERICAL_CELL_COMPILER_CHECKS_PASS')
