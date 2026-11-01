#!/usr/bin/env python3
from fractions import Fraction as F
import math, numpy as np
from numpy.polynomial.hermite import hermgauss
from scipy.special import log_ndtr, logsumexp
from scipy.optimize import root

# Exact inherited complete-second microstep. This is source-level bookkeeping;
# the substantive new mechanism below is third-full Schur continuation.
alphaL=F(315148718753,50_000_000_000)
alpha0=F(12319635,1_000_000)
alpha_before=F(2463926889239,200_000_000_000)  # 12.319634446195
alpha_after=F(6159817223097,500_000_000_000)   # 12.319634446194
q=F(229179741,467259059)
eta=F(18671401519768819,40795417037192166)
slope=F(4136629,105883920)
psi0=F(23584189005311,1090044380000000000000)
dec_lo=F(1,2_000_000)-F(27,500_000_000)
dec_hi=F(1,2_000_000)+F(27,500_000_000)
dec=alpha0-alpha_after
psi=psi0-slope*dec
assert alpha_before-alpha_after==F(1,1_000_000_000_000)
assert eta < 1-q and dec_lo <= dec <= dec_hi and psi>0
print('EXACT_SOURCE_MICROSTEP')
print('ALPHA_BEFORE', float(alpha_before))
print('ALPHA_AFTER', float(alpha_after))
print('SOURCE_GAIN', alpha_before-alpha_after, float(alpha_before-alpha_after))
print('PSI_AFTER_LOWER', psi, float(psi))
print('WIDTH_AFTER', float(alpha_after-alphaL))
print('EXACT_SOURCE_MICROSTEP_PASS')

GH={}
def gh(n):
    if n not in GH:
        z,w=hermgauss(n); GH[n]=(np.sqrt(2)*z,w/np.sqrt(np.pi))
    return GH[n]

def geom(v,delta):
    w0,w1,x,m=map(float,v); w2=1-w0-w1
    y=1+m*(x-1)*w1/(x*w0)
    Z=x*y*y*w0+y*w1+w2
    S=math.sqrt(Z)/(x*y); lam=S/(S+delta); xi=1+lam*(x-1)
    return w2,y,Z,S,lam,xi

def kernel(t,xi):
    t=np.asarray(t,float)
    l1=log_ndtr(-t); z=t/math.sqrt(xi)
    l2=-0.5*math.log(xi)-(xi-1)*t*t/(2*xi)+log_ndtr(z)
    U=np.logaddexp(l1,l2); f2=np.exp(l2-U)
    phF=np.exp(-0.5*t*t-0.5*math.log(2*math.pi)-U)
    mu1=(t*f2+phF)/xi; mu2=(t*mu1+f2)/xi
    Ut=-(xi-1)*mu1; K=-(xi-1)*0.5*mu2-U
    return U,Ut,mu2,K

def moments(vpar,delta,n):
    w0,w1,x,m=map(float,vpar); w2,y,Z,S,lam,xi=geom(vpar,delta)
    Uq,wu=gh(n); V,wv=gh(n); lwu=np.log(wu)
    a=math.sqrt(w1/w0); b=math.sqrt(w2/w0); c=1/math.sqrt(w0)
    out=np.zeros(5)
    for vv,ov in zip(V,wv):
        T=a*Uq+b*vv-c
        U,Ut,H,K=kernel(T,xi)
        lt=lwu+m*U; lz=logsumexp(lt); tw=np.exp(lt-lz)
        g=float(np.dot(tw,Ut))
        out += ov*np.array([g*g,np.dot(tw,Ut*Ut),np.dot(tw,H),
                            m*np.dot(tw,U)-lz,m*np.dot(tw,K)])
    return out

def kfun(y): return y*(y*math.log(y)-y+1)/(y-1)**2
def hfun(x): return x*(x-1-math.log(x))/(x-1)**2

def residual(vpar,delta,n):
    w0,w1,x,m=map(float,vpar); w2,y,Z,S,lam,xi=geom(vpar,delta)
    S1,S2,H1,DU,DH=moments(vpar,delta,n)
    return np.array([
      S2/S1-(1+y*w1/w2),
      Z*S1-w2*lam*lam*(x-1)**2*H1,
      x*x*w0*(y-1)**2*S1*(w2+w1*kfun(y))-2*w1*w2*(x-1)**2*DU,
      x*(y-1)*w0*S1*(Z-x*y*y*w0*hfun(x))-2*w1*w2*(x-1)*DH])

def alpha_of(vpar,delta,n):
    w0,w1,x,m=map(float,vpar); w2,y,Z,S,lam,xi=geom(vpar,delta)
    S1=moments(vpar,delta,n)[0]
    return w2*(x-1)**2/(x*x*y*y*w0*S1)

def solve3(mval,guess,delta,n):
    fun=lambda z:residual(np.array([z[0],z[1],z[2],mval]),delta,n)[:3]
    sol=root(fun,guess[:3],method='hybr',options={'xtol':1e-11,'maxfev':300})
    vv=np.array([*sol.x,mval])
    rr=residual(vv,delta,n)
    assert sol.success and np.linalg.norm(rr[:3],np.inf)<3e-11
    return vv,rr

def fd_jac(fun,x,rel=1e-6):
    x=np.array(x,float); y=np.array(fun(x),float); J=np.zeros((len(y),len(x)))
    for j in range(len(x)):
        h=rel*max(1.,abs(x[j])); xp=x.copy(); xm=x.copy(); xp[j]+=h; xm[j]-=h
        J[:,j]=(fun(xp)-fun(xm))/(2*h)
    return J

DEL=1e-3
vcenter=np.array([0.0321710159451139,0.370106966023378,3.54218891058057,0.226621581517544])
m0=vcenter[3]
print('NUMERICAL_ONLY_SCHUR_BRANCH_SWEEP_GH100')
guess=vcenter.copy()
for dm in np.linspace(-0.002,0.002,9):
    vv,rr=solve3(m0+dm,guess,DEL,100); guess=vv
    J=fd_jac(lambda z:residual(z,DEL,100),vv)
    A=J[:3,:3]
    sch=J[3,3]-J[3,:3]@np.linalg.solve(A,J[:3,3])
    sv=np.linalg.svd(A,compute_uv=False)
    print('DM',format(float(dm),'.7f'),
          'RH',format(float(rr[3]),'.16e'),
          'SCHUR',format(float(sch),'.16e'),
          'SIGMA3_MIN',format(float(sv[-1]),'.16e'),
          'COND3',format(float(sv[0]/sv[-1]),'.10g'),
          'ALPHA',format(float(alpha_of(vv,DEL,100)),'.15f'))

print('NUMERICAL_ONLY_ENDPOINT_ORDER_STABILITY')
for dm in (-0.001,0.001):
    print('SIDE',dm)
    guess=vcenter.copy()
    for n in (80,100,120,160,200):
        vv,rr=solve3(m0+dm,guess,DEL,n); guess=vv
        print('N',n,'RH',format(float(rr[3]),'.16e'),
              'ALPHA',format(float(alpha_of(vv,DEL,n)),'.15f'))

sol=root(lambda z:residual(z,DEL,120),vcenter,method='hybr',options={'xtol':1e-12,'maxfev':300})
v=sol.x; rr=residual(v,DEL,120)
J=fd_jac(lambda z:residual(z,DEL,120),v,rel=5e-7)
A=J[:3,:3]
sch=J[3,3]-J[3,:3]@np.linalg.solve(A,J[:3,3])
ratio=np.linalg.det(J)/np.linalg.det(A)
svJ=np.linalg.svd(J,compute_uv=False); svA=np.linalg.svd(A,compute_uv=False)
print('NUMERICAL_ONLY_CENTER_GH120')
print('V',*[format(float(t),'.16g') for t in v])
print('MAXRES',format(float(np.linalg.norm(rr,np.inf)),'.3e'))
print('SCHUR',format(float(sch),'.16e'))
print('DET_RATIO',format(float(ratio),'.16e'))
print('FULL_SIGMA_MIN',format(float(svJ[-1]),'.16e'))
print('THREE_SIGMA_MIN',format(float(svA[-1]),'.16e'))
print('SIGMA_GAIN',format(float(svA[-1]/svJ[-1]),'.10g'))
print('FULL_COND',format(float(svJ[0]/svJ[-1]),'.10g'))
print('THREE_COND',format(float(svA[0]/svA[-1]),'.10g'))
print('ALPHA_CENTER',format(float(alpha_of(v,DEL,120)),'.15f'))
print('ALL_CHECKS_PASS')
