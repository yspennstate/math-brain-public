#!/usr/bin/env python3
"""PROB10-03 R14: numerical-only scout for piecewise Schur continuation
plus exact-form inner KL sign-mixture/path identities.

No numerical value produced by this file is a rigorous source endpoint.
"""
import math
import numpy as np
from numpy.polynomial.hermite import hermgauss
from scipy.special import log_ndtr, logsumexp
from scipy.optimize import root
from scipy.integrate import quad

GH={}
def gh(n):
    if n not in GH:
        z,w=hermgauss(n); GH[n]=(np.sqrt(2)*z,w/np.sqrt(np.pi))
    return GH[n]

def valid(v):
    w0,w1,x,m=map(float,v); w2=1-w0-w1
    return w0>0 and w1>0 and w2>0 and x>1 and 0<m<1

def geom(v,delta):
    w0,w1,x,m=map(float,v); w2=1-w0-w1
    if not valid(v): raise ValueError('outside strict chart')
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
    a=xi-1
    Ut=-a*mu1
    Utt=-a*f2+a*a*(mu2-mu1*mu1)
    K=-a*0.5*mu2-U
    return U,Ut,Utt,mu1,mu2,K,f2

def moments(vpar,delta,n):
    w0,w1,x,m=map(float,vpar); w2,y,Z,S,lam,xi=geom(vpar,delta)
    Uq,wu=gh(n); V,wv=gh(n); lwu=np.log(wu)
    aa=math.sqrt(w1/w0); bb=math.sqrt(w2/w0); cc=1/math.sqrt(w0)
    out=np.zeros(5)
    for vv,ov in zip(V,wv):
        T=aa*Uq+bb*vv-cc
        U,Ut,Utt,mu1,H,K,pplus=kernel(T,xi)
        lt=lwu+m*U; lz=logsumexp(lt); tw=np.exp(lt-lz)
        g=float(np.dot(tw,Ut))
        out += ov*np.array([g*g,np.dot(tw,Ut*Ut),np.dot(tw,H),
                            m*np.dot(tw,U)-lz,m*np.dot(tw,K)])
    return out

def kfun(y): return y*(y*math.log(y)-y+1)/(y-1)**2
def hfun(x): return x*(x-1-math.log(x))/(x-1)**2

def residual(vpar,delta,n):
    if not valid(vpar): return np.ones(4)*1e6
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
    sol=root(fun,guess[:3],method='hybr',options={'xtol':1e-11,'maxfev':500})
    vv=np.array([*sol.x,mval]); rr=residual(vv,delta,n)
    if not (sol.success and valid(vv) and np.linalg.norm(rr[:3],np.inf)<5e-9):
        raise RuntimeError('3D branch solve failed')
    return vv,rr

def fd_jac(fun,x,rel=5e-7):
    x=np.array(x,float); y=np.asarray(fun(x),float); J=np.zeros((len(y),len(x)))
    for j in range(len(x)):
        h=rel*max(1.,abs(x[j])); xp=x.copy(); xm=x.copy(); xp[j]+=h; xm[j]-=h
        J[:,j]=(fun(xp)-fun(xm))/(2*h)
    return J

# Positive-path inner conditional KL.
def trunc_pos_moments(t,s):
    r=1+s; mu=t/r; sig2=1/r; z=t/math.sqrt(r)
    mills=math.exp(-0.5*z*z-0.5*math.log(2*math.pi)-float(log_ndtr(z)))
    M1=mu+math.sqrt(sig2)*mills
    M2=mu*M1+sig2
    M3=mu*M2+2*sig2*M1
    M4=mu*M3+3*sig2*M2
    return M1,M2,M3,M4

def kplus_direct(t,a):
    r=1+a
    logp=float(log_ndtr(t))
    logB=-0.5*math.log(r)-a*t*t/(2*r)+float(log_ndtr(t/math.sqrt(r)))
    M2=trunc_pos_moments(t,a)[1]
    return logp-logB-a*M2/2

def kplus_path(t,a):
    def f(s):
        M1,M2,M3,M4=trunc_pos_moments(t,s)
        return s*(M4-M2*M2)/4
    return quad(f,0,a,epsabs=1e-12,epsrel=1e-12,limit=120)[0]

def inner_kl_decomp(t,xi):
    a=xi-1
    logA=float(log_ndtr(-t))
    logp=float(log_ndtr(t))
    logB=-0.5*math.log(xi)-a*t*t/(2*xi)+float(log_ndtr(t/math.sqrt(xi)))
    logF=float(np.logaddexp(logA,logB))
    q=math.exp(logB-logF)
    bern=(1-q)*(-logF)+q*(logB-logF-logp)
    kp=kplus_direct(t,a)
    direct=kernel(np.array([t]),xi)[5][0]
    return direct,bern,q*kp,q,kp

def psi_def(d):
    return -d-np.log1p(-d)

def dh_cage(vpar,delta,n):
    w0,w1,x,m=map(float,vpar); w2,y,Z,S,lam,xi=geom(vpar,delta)
    Uq,wu=gh(n); V,wv=gh(n); lwu=np.log(wu)
    aa=math.sqrt(w1/w0); bb=math.sqrt(w2/w0); cc=1/math.sqrt(w0); a=xi-1
    vals=np.zeros(3)
    for vv,ov in zip(V,wv):
        T=aa*Uq+bb*vv-cc
        U,Ut,Utt,mu1,mu2,K,pplus=kernel(T,xi)
        lt=lwu+m*U; lz=logsumexp(lt); tw=np.exp(lt-lz)
        d=-Utt; var=1-d; R=a*a*(mu2-mu1*mu1)
        L=0.5*(Ut*Ut+psi_def(d))
        Up=L+0.5*np.log(np.maximum(1e-300,1+var*R-d*d))
        vals += ov*np.array([m*np.dot(tw,K),m*np.dot(tw,L),m*np.dot(tw,Up)])
    return vals

DEL=1e-3
VC=np.array([0.0321710159451139,0.370106966023378,3.54218891058057,0.226621581517544])
M0=VC[3]
CURRENT_UPPER=12.319634446193
print('NUMERICAL_ONLY_PIECEWISE_SCHUR_SCOUT')
for d in (0.01,0.02,0.04):
    print('WINDOW',d)
    for side in (-1,1):
        m=M0+side*d; guess=VC.copy()
        for n in (80,100,120,160,200):
            vv,rr=solve3(m,guess,DEL,n); guess=vv
            A=fd_jac(lambda z:residual(np.array([z[0],z[1],z[2],m]),DEL,n)[:3],vv[:3])
            sv=np.linalg.svd(A,compute_uv=False)
            if n in (80,200):
                print('SIDE',side,'N',n,'RH',format(float(rr[3]),'.16e'),
                      'ALPHA',format(float(alpha_of(vv,DEL,n)),'.15f'),
                      'SIGMA3_MIN',format(float(sv[-1]),'.12e'),
                      'COND3',format(float(sv[0]/sv[-1]),'.8g'))
        cage=dh_cage(vv,DEL,160)
        coeff=2*vv[1]*(1-vv[0]-vv[1])*(vv[2]-1)
        rw=coeff*(cage[2]-cage[1])
        print('CAGE_RH_WIDTH',format(float(rw),'.16e'),
              'CAGE_TO_SIGN_RATIO',format(float(rw/abs(rr[3])),'.8g'))

left,_=solve3(M0-0.01,VC,DEL,200)
right,_=solve3(M0+0.01,VC,DEL,200)
print('SELECTED_WINDOW_MINUS_PLUS',M0-0.01,M0+0.01)
print('SELECTED_LEFT_ALPHA',format(alpha_of(left,DEL,200),'.15f'))
print('CURRENT_UPPER',format(CURRENT_UPPER,'.15f'))
print('CONDITIONAL_POTENTIAL_GAIN_IF_CERTIFIED',format(CURRENT_UPPER-alpha_of(left,DEL,200),'.15e'))

_,_,_,_,_,xi=geom(VC,DEL)
a=xi-1
print('INNER_KL_POSITIVE_DECOMPOSITION_TEST', 'XI',format(xi,'.16g'))
max_chain=0.0; max_path=0.0
for t in (-8.,-4.,-2.,-1.,0.,1.,2.,4.,8.):
    direct,bern,qkp,q,kp=inner_kl_decomp(t,xi)
    path=kplus_path(t,a)
    chain_err=abs(direct-(bern+qkp)); path_err=abs(kp-path)
    max_chain=max(max_chain,chain_err); max_path=max(max_path,path_err)
    print('T',t,'K',format(direct,'.16e'),'BERN',format(bern,'.16e'),
          'QKPLUS',format(qkp,'.16e'),'CHAIN_ERR',format(chain_err,'.3e'),
          'KPLUS_PATH_ERR',format(path_err,'.3e'))
print('MAX_CHAIN_ERR',format(max_chain,'.3e'))
print('MAX_KPLUS_PATH_ERR',format(max_path,'.3e'))
assert max_chain < 5e-13 and max_path < 5e-12
print('ALL_NUMERICAL_SELF_CHECKS_PASS')
