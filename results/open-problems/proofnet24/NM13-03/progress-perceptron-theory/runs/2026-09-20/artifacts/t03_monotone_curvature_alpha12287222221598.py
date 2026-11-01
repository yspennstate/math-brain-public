#!/usr/bin/env python3
# NM13-03 / T03 2026-09-20
# Exact theorem is proved in companion report. Numerical sections are falsification/support only.
import os, math
from fractions import Fraction as F
import numpy as np
os.environ.setdefault('JAX_ENABLE_X64','True')
from numpy.polynomial.hermite import hermgauss
from scipy.optimize import root
from scipy.integrate import quad
from scipy.special import log_ndtr as sp_log_ndtr, logsumexp as sp_logsumexp
import jax, jax.numpy as jnp
from jax.scipy.special import log_ndtr, logsumexp
jax.config.update('jax_enable_x64',True)

LOWER=F(315148718753,50_000_000_000)
PREV=F(12287222221600,1_000_000_000_000)
A0=F(6143611110799,500_000_000_000)  # 12.287222221598
assert PREV-A0 == F(1,500_000_000_000)
print('EXACT_SUPPORTED_BOOKKEEPING')
print('SUPPORTED_BEFORE',float(PREV))
print('SUPPORTED_AFTER',float(A0))
print('GAIN_EXACT',PREV-A0,float(PREV-A0))
print('WIDTH_AFTER_EXACT',A0-LOWER,float(A0-LOWER))

# delta=1e-3 positive-gap waypoint from companion
w0=0.0321710159451139; w1=0.370106966023378
xpg=3.54218891058057; mpg=0.226621581517544; DEL=1e-3
w2=1-w0-w1
y=1+mpg*(xpg-1)*w1/(xpg*w0)
Zalg=xpg*y*y*w0+y*w1+w2
S=math.sqrt(Zalg)/(xpg*y); lam=S/(S+DEL); xi=1+lam*(xpg-1)
beta=xi-1; ell=beta/(1+beta); d2=w1/w0; d=math.sqrt(d2); s2=w2/w0; s=math.sqrt(s2)
Lout=mpg*ell/(1+mpg*ell*d2)
Cself=2*ell/(mpg*(1+mpg*ell*d2))

def hinge_kernel_np(t):
    t=np.asarray(t,float)
    l1=sp_log_ndtr(-t)
    l2=-.5*math.log(xi)-beta*t*t/(2*xi)+sp_log_ndtr(t/math.sqrt(xi))
    U=np.logaddexp(l1,l2)
    f2=np.exp(l2-U)
    phF=np.exp(-.5*t*t-.5*math.log(2*math.pi)-U)
    mu1=(t*f2+phF)/xi
    Ut=-beta*mu1
    return U,Ut

zq,wq=hermgauss(240); uq=np.sqrt(2)*zq; wgh=wq/np.sqrt(np.pi)
def q_g_qxx(a):
    U,Ut=hinge_kernel_np(a+d*uq)
    lt=np.log(wgh)+mpg*U
    lz=sp_logsumexp(lt); pr=np.exp(lt-lz)
    g=float(np.dot(pr,Ut))
    T=a+d*uq; mt=float(np.dot(pr,T)); vt=float(np.dot(pr,(T-mt)**2))
    qxx=-1/d2+vt/(d2*d2)
    return float(lz),g,qxx

# finite-difference sign check for q'''<=0 and refined pointwise energy cage
agrid=np.linspace(-15,20,281)
qxs=[]; ratios=[]
for a in agrid:
    q,g,qxx=q_g_qxx(a); qxs.append(qxx)
    den=2*(-q)*(-qxx)
    if den>1e-28: ratios.append((mpg*g)**2/den)
max_increase=max(np.diff(qxs))
assert max_increase < 3e-10
assert max(ratios) <= 1+2e-10

vals=[]
for vv in uq:
    a=s*vv-1/math.sqrt(w0)
    vals.append(q_g_qxx(a))
Q=float(np.dot(wgh,[z[0] for z in vals]))
S1=float(np.dot(wgh,[z[1]**2 for z in vals]))
S1_old=Cself*(-Q)
S1_new=float(np.dot(wgh,[2*(-z[0])*(-z[2])/(mpg*mpg) for z in vals]))
slack_old=S1_old-S1; slack_new=S1_new-S1
shrink=1-slack_new/slack_old
assert S1 <= S1_new+2e-12 <= S1_old+2e-12
print('NUMERICAL_ONLY_MONOTONE_CURVATURE_WAYPOINT')
print('ELL',format(ell,'.17g'),'LOUT',format(Lout,'.17g'))
print('QXX_MONOTONE_MAX_FORWARD_INCREMENT',format(max_increase,'.17g'))
print('LOCAL_ENERGY_MAX_UTILIZATION',format(max(ratios),'.17g'))
print('Q',format(Q,'.17g'),'S1',format(S1,'.17g'))
print('S1_OLD_GLOBAL_UPPER',format(S1_old,'.17g'))
print('S1_NEW_LOCAL_CURVATURE_UPPER',format(S1_new,'.17g'))
print('S1_UPPER_SLACK_SHRINK_FRACTION',format(shrink,'.17g'))
# Scalar-q-only spatial secant compiler for S1 on the outer V mesh.
# This numerically demonstrates the exact cell inequalities proved in the report.
from scipy.special import ndtr
def qv(v): return q_g_qxx(s*v-1/math.sqrt(w0))[0]
def gv(v): return q_g_qxx(s*v-1/math.sqrt(w0))[1]
S1_central_ref,_=quad(lambda v: math.exp(-.5*v*v)/math.sqrt(2*math.pi)*gv(v)**2,-6,6,epsabs=1e-11,epsrel=1e-11,limit=200)
for ncell in (100,200,400,800):
    R=6.0; h=2*R/ncell
    xs=np.linspace(-R-h,R+h,ncell+3); qs=np.array([qv(v) for v in xs])
    lo=0.0; up=0.0
    for i in range(ncell):
        l=xs[i+1]; r=xs[i+2]; mass=ndtr(r)-ndtr(l)
        back=(qs[i+1]-qs[i])/h
        fwd=(qs[i+3]-qs[i+2])/h
        lo += back*back/(s2*mpg*mpg)*mass
        up += fwd*fwd/(s2*mpg*mpg)*mass
    assert lo <= S1_central_ref+2e-10 <= up+2e-10
    print('SPATIAL_SECANT_S1_N',ncell,'LOW',format(lo,'.17g'),'UP',format(up,'.17g'),'WIDTH',format(up-lo,'.17g'))
print('S1_CENTRAL_REFERENCE',format(S1_central_ref,'.17g'),'FULL_MINUS_CENTRAL',format(S1-S1_central_ref,'.17g'))
print('MONOTONE_CURVATURE_CHECKS_PASS')

# complete-third fixed-density numerical support at improved alpha
K=-1.0; A0f=float(A0)
def gh(n):
    x,w=hermgauss(n); return jnp.array(np.sqrt(2)*x),jnp.array(w/np.sqrt(np.pi))
def recon(p3,p2,q3,q2):
    r=jnp.sqrt(q3/p3); ri=1/r
    c3=ri/(p2-p3)-r/(q2-q3)
    gp=.5*((1-q2)/(1-p2))*((p2-p3)/(q2-q3))*r
    c2=(((p2-p3)/(q2-q3))*r)/(1-p2)-(((q2-q3)/(p2-p3))*ri)/(1-q2)
    return c3,c2,gp

def build(n):
    x,w=gh(n); U=x[:,None]; V=x[None,:]
    def P(v,a):
        p3,p2,q3,q2,c3,c2,gs,gp=v
        Aq=2*gp-c2*(1-q2); Dq=Aq-c3*(q2-q3); B=c2/(4*gs); ss=jnp.sqrt(1-p2)
        mu=jnp.sqrt(p2-p3)*U+jnp.sqrt(p3)*V+K; C=1+2*B*ss*ss
        uu=jnp.logaddexp(log_ndtr(-mu/ss),-.5*jnp.log(C)-B*mu*mu/C+log_ndtr(mu/(ss*jnp.sqrt(C))))
        mm=c3/c2; QQ=jnp.sum(w*logsumexp(jnp.log(w)[:,None]+mm*uu,axis=0))
        return (.5*(1-p2*q2)*c2+.5*(p2*q2-p3*q3)*c3-gp+.5/c2*jnp.log(Aq/(2*gp))
                +.5/c3*jnp.log(Dq/Aq)-q3/(2*Dq)+gs-a*QQ/c3)
    G=jax.jit(jax.grad(P,0)); PJ=jax.jit(P)
    def FF(yy,a):
        p3,p2,q3,q2,gs=yy; c3,c2,gp=recon(p3,p2,q3,q2)
        gg=G(jnp.array([p3,p2,q3,q2,c3,c2,gs,gp]),a)
        return jnp.array([gg[0],gg[1],gg[4],gg[5],gg[6]])
    return PJ,G,jax.jit(FF)

seed=np.array([.59916661554336237,.96911591246488993,.22869805152020112,.63843683126748652,.076564602120304762])
sols={}
for n in (160,200,240,280,320):
    P,G,FF=build(n)
    sol=root(lambda yy:np.asarray(FF(jnp.array(yy),A0f),float),seed,tol=1e-12)
    p3,p2,q3,q2,gs=sol.x; c3,c2,gp=map(float,recon(p3,p2,q3,q2))
    vv=np.array([p3,p2,q3,q2,c3,c2,gs,gp]); gg=np.asarray(G(jnp.array(vv),A0f),float)
    psi=float(P(jnp.array(vv),A0f)); r2=q3/p3; r1=(q2-q3)/(p2-p3); r0=(1-q2)/(1-p2)
    gap=2*gs-r1/(r0*np.sqrt(r2)); sols[n]=(vv,psi,gap,float(np.max(abs(gg)))); seed=sol.x
vv,psi320,gap320,ginf320=sols[320]

def adaptive_Q(v,L=8.0):
    p3,p2,q3,q2,c3,c2,gs,gp=map(float,v); B=c2/(4*gs); ss=math.sqrt(1-p2); mm=c3/c2; rt=math.sqrt(2*math.pi)
    def phi(z): return math.exp(-.5*z*z)/rt
    def logf(u3,u4):
        mu=math.sqrt(p2-p3)*u3+math.sqrt(p3)*u4+K; C=1+2*B*ss*ss
        return np.logaddexp(sp_log_ndtr(-mu/ss),-.5*math.log(C)-B*mu*mu/C+sp_log_ndtr(mu/(ss*math.sqrt(C))))
    def inner(u4):
        q,_=quad(lambda u3:phi(u3)*math.exp(mm*logf(u3,u4)),-L,L,epsabs=2e-12,epsrel=2e-12,limit=180); return q
    return quad(lambda u4:phi(u4)*math.log(inner(u4)),-L,L,epsabs=3e-12,epsrel=3e-12,limit=180)

def algebra_without_Q(v):
    p3,p2,q3,q2,c3,c2,gs,gp=map(float,v); Aq=2*gp-c2*(1-q2); Dq=Aq-c3*(q2-q3)
    return (.5*(1-p2*q2)*c2+.5*(p2*q2-p3*q3)*c3-gp+.5/c2*math.log(Aq/(2*gp))
            +.5/c3*math.log(Dq/Aq)-q3/(2*Dq)+gs)
qad,qerr=adaptive_Q(vv); c3=float(vv[4]); psi_ad=algebra_without_Q(vv)-A0f*qad/c3
print('NUMERICAL_ONLY_SUPPORTED_THIRD_FULL')
print('ALPHA',format(A0f,'.12f'))
for n in (160,200,240,280,320):
    v,pp,gg,gi=sols[n]; print('GH',n,'PSI',format(pp,'.17g'),'SCALE_GAP',format(gg,'.17g'),'GRAD_INF',format(gi,'.3e'))
print('PARAMS_GH320',*(format(t,'.17g') for t in vv))
print('ADAPTIVE_Q',format(qad,'.17g'),'REPORTED_QUAD_ERR',format(qerr,'.3e'),'PSI_ADAPTIVE',format(psi_ad,'.17g'))
assert all(sols[n][1] > 0 for n in sols); assert psi_ad > 0
print('SUPPORTED_BOUND_CHECKS_PASS')
print('ALL_MONOTONE_CURVATURE_AND_SUPPORTED_BOUND_CHECKS_PASS')
