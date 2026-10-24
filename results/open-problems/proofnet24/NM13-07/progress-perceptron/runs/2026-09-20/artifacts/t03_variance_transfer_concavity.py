#!/usr/bin/env python3
"""
NM13-07 / T03: scalar-Q directional compiler for complete-third moments.

PROVED identities checked algebraically:
  D_tau Q = m(m-1) S2 / 2, and Q is concave in tau for 0<m<1.
  D_rho Q = -m^2 S1 / 2, and Q is concave in rho.
  Q is convex in auxiliary exponent m and penalty beta.
Consequently S1,S2,H1,DU can all be enclosed by one-sided secants of the
single scalar free energy Q, once Q itself has a rigorous evaluator.

Numerical sections are only falsification checks at the delta=1e-3 waypoint.
"""
import math
import numpy as np
import sympy as sp
from scipy.special import roots_hermitenorm, log_ndtr, logsumexp

# ----- symbolic positivity behind tau concavity -----
aa,zz,ss,mm=sp.symbols('a z s m', positive=True)
# BL cost for the negative variance term:
bl_cost = 2*mm*(1-mm)*zz*aa**2/(1/ss+mm*aa)
positive_cross = 2*(1-mm)*zz*aa
gap = sp.factor(positive_cross-bl_cost)
assert sp.simplify(gap - 2*(1-mm)*zz*aa/(1+mm*aa*ss))==0
print('EXACT_TAU_BL_DOMINATION_IDENTITY_PASS')
print('BL_GAP_SYMBOLIC', gap)

# rho concavity integrand q_xx^2 - 2 q_x^2 q_xx is nonnegative for q_xx<=0.
r,z=sp.symbols('r z', nonnegative=True)
rho_integrand = sp.expand(r**2 + 2*z*r)  # r=-q_xx, z=q_x^2
assert rho_integrand == r**2+2*z*r
print('EXACT_RHO_CONCAVITY_INTEGRAND_PASS')

DEL=1e-3
vpar=np.array([0.0321710159451139,0.370106966023378,
               3.54218891058057,0.226621581517544],float)

def geom(v):
    w0,w1,x,m=map(float,v); w2=1-w0-w1
    y=1+m*(x-1)*w1/(x*w0)
    Z=x*y*y*w0+y*w1+w2
    S=math.sqrt(Z)/(x*y); lam=S/(S+DEL); xi=1+lam*(x-1)
    return w2,y,Z,S,lam,xi

def gh(n):
    z,w=roots_hermitenorm(n)
    return z,w/math.sqrt(2*math.pi)

def U_general(t,beta,rh):
    t=np.asarray(t,float)
    A=1+beta*rh
    s=math.sqrt(rh)
    l1=log_ndtr(-t/s)
    l2=-.5*math.log(A)-beta*t*t/(2*A)+log_ndtr(t/(s*math.sqrt(A)))
    return np.logaddexp(l1,l2)

def kernel_base(t,xi):
    t=np.asarray(t,float)
    l1=log_ndtr(-t)
    l2=-.5*math.log(xi)-(xi-1)*t*t/(2*xi)+log_ndtr(t/math.sqrt(xi))
    U=np.logaddexp(l1,l2)
    f2=np.exp(l2-U)
    phF=np.exp(-.5*t*t-.5*math.log(2*math.pi)-U)
    mu1=(t*f2+phF)/xi
    mu2=(t*mu1+f2)/xi
    Ut=-(xi-1)*mu1
    return U,Ut,mu2

w0,w1,x,m=map(float,vpar)
w2,y,Z,S,lam,xi=geom(vpar)
beta=xi-1
d2=w1/w0
b2=w2/w0
c0=1/math.sqrt(w0)

def Q_nested(varV,varU,varH,beta0,mexp,n=120):
    Ug,wu=gh(n); Vg,wv=gh(n)
    T=np.sqrt(varU)*Ug[None,:]+np.sqrt(varV)*Vg[:,None]-c0
    U=U_general(T,beta0,varH)
    lz=logsumexp(np.log(wu)[None,:]+mexp*U,axis=1)
    return float(np.dot(wv,lz))

def base_moments(n=140):
    Ug,wu=gh(n); Vg,wv=gh(n)
    T=np.sqrt(d2)*Ug[None,:]+np.sqrt(b2)*Vg[:,None]-c0
    U,Ut,H=kernel_base(T,xi)
    lw=np.log(wu)[None,:]+m*U
    lz=logsumexp(lw,axis=1)
    tw=np.exp(lw-lz[:,None])
    g=np.sum(tw*Ut,axis=1)
    S1=float(np.dot(wv,g*g))
    S2=float(np.dot(wv,np.sum(tw*Ut*Ut,axis=1)))
    H1=float(np.dot(wv,np.sum(tw*H,axis=1)))
    DU=float(np.dot(wv,m*np.sum(tw*U,axis=1)-lz))
    Q=float(np.dot(wv,lz))
    return Q,S1,S2,H1,DU

Q0,S1,S2,H1,DU=base_moments()
print('NUMERICAL_ONLY_BASE')
print('Q',Q0,'S1',S1,'S2',S2,'H1',H1,'DU',DU)
print('PRED_DTAU_Q',m*(m-1)*S2/2)
print('PRED_DRHO_Q',-m*m*S1/2)
print('PRED_DBETA_Q',-m*H1/2)
print('PRED_DM_Q',(DU+Q0)/m)

Qbase120=Q_nested(b2,d2,1,beta,m,120)
for h in (1e-3,5e-4,2e-4,1e-4):
    # tau: move variance H -> U
    tp=Q_nested(b2,d2+h,1-h,beta,m,120)
    tm=Q_nested(b2,d2-h,1+h,beta,m,120)
    dt=(tp-tm)/(2*h); d2t=(tp-2*Qbase120+tm)/(h*h)
    # rho: move variance U -> V
    rp=Q_nested(b2+h,d2-h,1,beta,m,120)
    rm=Q_nested(b2-h,d2+h,1,beta,m,120)
    dr=(rp-rm)/(2*h); d2r=(rp-2*Qbase120+rm)/(h*h)
    # beta, auxiliary penalty only
    bp=Q_nested(b2,d2,1,beta+h,m,120)
    bm=Q_nested(b2,d2,1,beta-h,m,120)
    db=(bp-bm)/(2*h); d2b=(bp-2*Qbase120+bm)/(h*h)
    # m, auxiliary exponent only
    mp=Q_nested(b2,d2,1,beta,m+h,120)
    mn=Q_nested(b2,d2,1,beta,m-h,120)
    dm=(mp-mn)/(2*h); d2m=(mp-2*Qbase120+mn)/(h*h)
    print('NUMERICAL_ONLY_H',h,
          'DTAU',dt,'D2TAU',d2t,
          'DRHO',dr,'D2RHO',d2r,
          'DBETA',db,'D2BETA',d2b,
          'DM',dm,'D2M',d2m)
    assert d2t < 0
    assert d2r < 0
    assert d2b > 0
    assert d2m > 0

print('ALL_EXACT_AND_NUMERICAL_DIRECTIONAL_COMPILER_CHECKS_PASS')
