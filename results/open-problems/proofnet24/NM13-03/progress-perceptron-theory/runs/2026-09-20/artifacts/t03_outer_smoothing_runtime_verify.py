#!/usr/bin/env python3
# Independent runtime verification for the immutable T03 outer-smoothing report.
# NUMERICAL_ONLY except the theorem formulas proved in the report.
import math, numpy as np
from numpy.polynomial.hermite import hermgauss
from scipy.special import log_ndtr, logsumexp

# Positive-gap waypoint theorem check.
w0=0.0321710159451139; w1=0.370106966023378
xpg=3.54218891058057; mpg=0.226621581517544; DEL=1e-3
w2=1-w0-w1
y=1+mpg*(xpg-1)*w1/(xpg*w0)
Zalg=xpg*y*y*w0+y*w1+w2
S=math.sqrt(Zalg)/(xpg*y); lam=S/(S+DEL); xi=1+lam*(xpg-1)
beta=xi-1; ell=beta/(1+beta); d2=w1/w0; d=math.sqrt(d2)
s2=w2/w0; s=math.sqrt(s2)
L=mpg*ell/(1+mpg*ell*d2); LV=L*s2
CQ=2*ell/(mpg*(1+mpg*ell*d2))
z,w=hermgauss(240); u=np.sqrt(2)*z; wg=w/np.sqrt(np.pi)
def hinge(t):
    t=np.asarray(t,float)
    l1=log_ndtr(-t); l2=-.5*math.log(xi)-beta*t*t/(2*xi)+log_ndtr(t/math.sqrt(xi))
    U=np.logaddexp(l1,l2); f2=np.exp(l2-U)
    phF=np.exp(-.5*t*t-.5*math.log(2*math.pi)-U)
    mu1=(t*f2+phF)/xi
    return U,-beta*mu1
def qgxx(a):
    U,Ut=hinge(a+d*u); lt=np.log(wg)+mpg*U; q=logsumexp(lt); pr=np.exp(lt-q)
    g=float(np.dot(pr,Ut)); T=a+d*u; mt=float(np.dot(pr,T)); var=float(np.dot(pr,(T-mt)**2))
    return float(q),g,-1/d2+var/d2**2
qxx=[]; ratios=[]
for vv in np.linspace(-6,6,121):
    q,g,h=qgxx(s*vv-1/math.sqrt(w0)); qxx.append(h)
    rhs=2*L*(-q)
    if rhs>1e-30: ratios.append((mpg*g)**2/rhs)
vals=[qgxx(s*vv-1/math.sqrt(w0))[:2] for vv in u]
Q=float(np.dot(wg,[a for a,b in vals])); S1=float(np.dot(wg,[b*b for a,b in vals]))
print('WAYPOINT ell',repr(ell),'d2',repr(d2),'s2',repr(s2),'L',repr(L),'LV',repr(LV))
print('WAYPOINT qxx_min',repr(min(qxx)),'qxx_max',repr(max(qxx)),'selfbound_maxratio',repr(max(ratios)))
print('WAYPOINT Q',repr(Q),'S1',repr(S1),'S1_cage',repr(CQ*(-Q)),'utilization',repr(S1/(CQ*(-Q))))
assert min(qxx)>=-L-2e-12 and max(qxx)<=2e-12 and max(ratios)<=1+2e-12

# Independent objective evaluation at the new supported conditional alpha.
alpha=12.287222221600
v=np.array([0.59916661554407757,0.96911591246567508,0.22869805152002043,0.63843683126931883,
            2.8674017463469124,13.103474334644494,0.076564602119094452,3.2652164718563506])
K=-1.0
def objective(v,a,n):
    p3,p2,q3,q2,c3,c2,gs,gp=map(float,v)
    z,w=hermgauss(n); x=np.sqrt(2)*z; ww=w/np.sqrt(np.pi); U=x[:,None]; V=x[None,:]
    Aq=2*gp-c2*(1-q2); Dq=Aq-c3*(q2-q3); B=c2/(4*gs); ss=math.sqrt(1-p2)
    mu=math.sqrt(p2-p3)*U+math.sqrt(p3)*V+K; C=1+2*B*ss*ss
    uu=np.logaddexp(log_ndtr(-mu/ss),-.5*math.log(C)-B*mu*mu/C+log_ndtr(mu/(ss*math.sqrt(C))))
    mm=c3/c2; QQ=float(np.dot(ww,logsumexp(np.log(ww)[:,None]+mm*uu,axis=0)))
    P=(.5*(1-p2*q2)*c2+.5*(p2*q2-p3*q3)*c3-gp+.5/c2*math.log(Aq/(2*gp))
       +.5/c3*math.log(Dq/Aq)-q3/(2*Dq)+gs-a*QQ/c3)
    return P,QQ
for n in (160,200,240,280,320):
    P,Qn=objective(v,alpha,n); print('ALPHA',repr(alpha),'GH',n,'Psi3',repr(P),'Q',repr(Qn)); assert P>0
print('RUNTIME_VERIFY_PASS')