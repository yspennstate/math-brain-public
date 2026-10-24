#!/usr/bin/env python3
# NM13-03 / T03 2026-09-20.
# Numerical support only; NOT directed interval arithmetic.
import os, math, numpy as np
os.environ.setdefault('JAX_ENABLE_X64','True')
from numpy.polynomial.hermite import hermgauss
from scipy.optimize import root
from scipy.integrate import quad
from scipy.special import log_ndtr as sp_log_ndtr
import jax, jax.numpy as jnp
from jax.scipy.special import log_ndtr, logsumexp
jax.config.update('jax_enable_x64',True)

K=-1.0
A0=12.287222221605
PREV=12.28722222161
LOWER=6.30297437506

def gh(n):
    x,w=hermgauss(n)
    return jnp.array(np.sqrt(2)*x), jnp.array(w/np.sqrt(np.pi))

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
        Aq=2*gp-c2*(1-q2); Dq=Aq-c3*(q2-q3); B=c2/(4*gs); s=jnp.sqrt(1-p2)
        mu=jnp.sqrt(p2-p3)*U+jnp.sqrt(p3)*V+K
        C=1+2*B*s*s
        u=jnp.logaddexp(log_ndtr(-mu/s),-.5*jnp.log(C)-B*mu*mu/C+log_ndtr(mu/(s*jnp.sqrt(C))))
        m=c3/c2
        Q=jnp.sum(w*logsumexp(jnp.log(w)[:,None]+m*u,axis=0))
        return (.5*(1-p2*q2)*c2+.5*(p2*q2-p3*q3)*c3-gp
                +.5/c2*jnp.log(Aq/(2*gp))+.5/c3*jnp.log(Dq/Aq)-q3/(2*Dq)+gs-a*Q/c3)
    G=jax.jit(jax.grad(P,0)); PJ=jax.jit(P)
    def F(y,a):
        p3,p2,q3,q2,gs=y
        c3,c2,gp=recon(p3,p2,q3,q2)
        g=G(jnp.array([p3,p2,q3,q2,c3,c2,gs,gp]),a)
        return jnp.array([g[0],g[1],g[4],g[5],g[6]])
    return x,w,PJ,G,jax.jit(F)

seed=np.array([.59916661553777206,.96911591246056061,.22869805152395933,.63843683126824713,.076564602131018136])
sols={}
for n in (160,200,240,280,320):
    x,w,P,G,F=build(n)
    z=root(lambda y:np.asarray(F(jnp.array(y),A0),float),seed,tol=1e-12)
    p3,p2,q3,q2,gs=z.x
    c3,c2,gp=map(float,recon(p3,p2,q3,q2))
    v=np.array([p3,p2,q3,q2,c3,c2,gs,gp])
    g=np.asarray(G(jnp.array(v),A0),float)
    val=float(P(jnp.array(v),A0))
    r2=q3/p3; r1=(q2-q3)/(p2-p3); r0=(1-q2)/(1-p2)
    gap=2*gs-r1/(r0*np.sqrt(r2))
    sols[n]=(v,val,gap,np.max(abs(g)))
    seed=z.x

# Evaluate the entropy cages at the GH240 stationary point.
n=240
v,val,gap,ginf=sols[n]
p3,p2,q3,q2,c3,c2,gs,gp=map(float,v)
x,wj,_,_,_=build(n)
w=np.array(wj)
U=jnp.array(np.array(x)[:,None]); V=jnp.array(np.array(x)[None,:]); ww=jnp.array(w)
B=c2/(4*gs); s=math.sqrt(1-p2); d=math.sqrt(p2-p3); d2=p2-p3; m=c3/c2; C=1+2*B*s*s

def u(mu,Bv):
    Cv=1+2*Bv*s*s
    return jnp.logaddexp(log_ndtr(-mu/s),-.5*jnp.log(Cv)-Bv*mu*mu/Cv+log_ndtr(mu/(s*jnp.sqrt(Cv))))
ux=jax.grad(u,0); uxx=jax.grad(ux,0); uB=jax.grad(u,1)
vf=jax.jit(jax.vmap(u,in_axes=(0,None))); vx=jax.jit(jax.vmap(ux,in_axes=(0,None)))
vxx=jax.jit(jax.vmap(uxx,in_axes=(0,None))); vB=jax.jit(jax.vmap(uB,in_axes=(0,None)))
muf=(d*U+jnp.sqrt(p3)*V+K).reshape(-1)
uu=vf(muf,B).reshape((n,n)); gx=vx(muf,B).reshape((n,n)); gxx=vxx(muf,B).reshape((n,n)); bb=vB(muf,B).reshape((n,n))
lz=logsumexp(jnp.log(ww)[:,None]+m*uu,axis=0)
pr=jnp.exp(jnp.log(ww)[:,None]+m*uu-lz[None,:])
mg=jnp.sum(pr*gx,axis=0); m2=jnp.sum(pr*gx*gx,axis=0); tv=m2-mg*mg; cv=-jnp.sum(pr*gxx,axis=0)
psi=lambda z:-z-jnp.log1p(-z)

du=jnp.maximum(0.0,m*d2*cv-m*m*d2*tv); vu=1-du
DU=jnp.sum(ww*(m*jnp.sum(pr*uu,axis=0)-lz))
LU=.5*jnp.sum(ww*((m*d*mg)**2+psi(du)))
RU=m*m*d2*tv; Iu=jnp.maximum(0.0,RU-du*du/vu)
stamU=.5*jnp.log1p(vu*Iu)
SoldU=du/vu
hsiU=.5*SoldU*jnp.log1p((vu*Iu)/jnp.maximum(SoldU,1e-300)); hsiU=jnp.where(SoldU>1e-15,hsiU,0.0)
prevU=LU+jnp.sum(ww*jnp.minimum(stamU,hsiU))
ellU=1/(1+2*m*d2*B/C)
SnewU=du*jnp.maximum(vu-ellU,0)/(vu*vu)
curvU=.5*SnewU*jnp.log1p((vu*Iu)/jnp.maximum(SnewU,1e-300)); curvU=jnp.where(SnewU>1e-15,curvU,0.0)
newU=LU+jnp.sum(ww*jnp.minimum(jnp.minimum(stamU,hsiU),curvU))

logJ0=-.5*math.log(C)-B*muf*muf/C+log_ndtr(muf/(s*math.sqrt(C)))
ppos=jnp.exp(logJ0.reshape((n,n))-uu)
dh=jnp.maximum(0.0,-s*s*gxx); vh=1-dh
RH=2*B*s*s*ppos-dh; Ih=jnp.maximum(0.0,RH-dh*dh/vh)
KLlo=.5*(s*s*gx*gx+psi(dh)); KLact=B*bb-uu
DH=m*jnp.sum(ww*jnp.sum(pr*KLact,axis=0)); LH=m*jnp.sum(ww*jnp.sum(pr*KLlo,axis=0))
stamH=.5*jnp.log1p(vh*Ih); SoldH=dh/vh
hsiH=.5*SoldH*jnp.log1p((vh*Ih)/jnp.maximum(SoldH,1e-300)); hsiH=jnp.where(SoldH>1e-15,hsiH,0.0)
prevH=m*jnp.sum(ww*jnp.sum(pr*(KLlo+jnp.minimum(stamH,hsiH)),axis=0))
ellH=1/C
SnewH=dh*jnp.maximum(vh-ellH,0)/(vh*vh)
curvH=.5*SnewH*jnp.log1p((vh*Ih)/jnp.maximum(SnewH,1e-300)); curvH=jnp.where(SnewH>1e-15,curvH,0.0)
newH=m*jnp.sum(ww*jnp.sum(pr*(KLlo+jnp.minimum(jnp.minimum(stamH,hsiH),curvH)),axis=0))

def adaptive_Q(v,L=8.0):
    p3,p2,q3,q2,c3,c2,gs,gp=map(float,v)
    B=c2/(4*gs); s=math.sqrt(1-p2); m=c3/c2; rt=math.sqrt(2*math.pi)
    def phi(z): return math.exp(-.5*z*z)/rt
    def logf(u3,u4):
        mu=math.sqrt(p2-p3)*u3+math.sqrt(p3)*u4+K; C=1+2*B*s*s
        return np.logaddexp(sp_log_ndtr(-mu/s),-.5*math.log(C)-B*mu*mu/C+sp_log_ndtr(mu/(s*math.sqrt(C))))
    def inner(u4):
        q,_=quad(lambda u3:phi(u3)*math.exp(m*logf(u3,u4)),-L,L,epsabs=2e-12,epsrel=2e-12,limit=180)
        return q
    q,err=quad(lambda u4:phi(u4)*math.log(inner(u4)),-L,L,epsabs=5e-11,epsrel=5e-11,limit=140)
    return q,err

def algebra_without_Q(v):
    p3,p2,q3,q2,c3,c2,gs,gp=map(float,v)
    Aq=2*gp-c2*(1-q2); Dq=Aq-c3*(q2-q3)
    return (.5*(1-p2*q2)*c2+.5*(p2*q2-p3*q3)*c3-gp
            +.5/c2*math.log(Aq/(2*gp))+.5/c3*math.log(Dq/Aq)-q3/(2*Dq)+gs)

qad,qerr=adaptive_Q(v)
psi_ad=algebra_without_Q(v)-A0*qad/c3

print('STATUS NUMERICAL_SUPPORT_NOT_DIRECTED_INTERVAL')
print('ALPHA',format(A0,'.15f'))
for n in (160,200,240,280,320):
    vv,pv,gg,gi=sols[n]
    print('GH',n,'PSI',format(pv,'.17g'),'GAP',format(gg,'.17g'),'GRAD_INF',format(gi,'.3e'))
print('PARAMS_GH240',*(format(t,'.17g') for t in v))
print('CURVATURE_CONSTANTS ellU',format(float(ellU),'.17g'),'ellH',format(float(ellH),'.17g'))
print('OUTER DU lower actual prevHSI newCurv',format(float(LU),'.17g'),format(float(DU),'.17g'),format(float(prevU),'.17g'),format(float(newU),'.17g'))
print('OUTER slack_prev slack_new',format(float(prevU-DU),'.17g'),format(float(newU-DU),'.17g'))
print('INNER DH lower actual prevHSI newCurv',format(float(LH),'.17g'),format(float(DH),'.17g'),format(float(prevH),'.17g'),format(float(newH),'.17g'))
print('INNER slack_prev slack_new',format(float(prevH-DH),'.17g'),format(float(newH-DH),'.17g'))
print('AC3_upper_prev_new',format(float(A0*prevU/c3**2),'.17g'),format(float(A0*newU/c3**2),'.17g'))
print('AC2_upper_prev_new',format(float(A0*prevH/(c2*c3)),'.17g'),format(float(A0*newH/(c2*c3)),'.17g'))
print('ADAPTIVE_Q',format(qad,'.17g'),'QUAD_ERR',format(qerr,'.3e'),'PSI_ADAPTIVE',format(psi_ad,'.17g'))
print('SUPPORTED_BOUND_BEFORE',format(PREV,'.14f'),'AFTER',format(A0,'.15f'),'GAIN',format(PREV-A0,'.3e'),'WIDTH_AFTER',format(A0-LOWER,'.14f'))

assert float(LU) <= float(DU)+1e-10 <= float(newU)+1e-10 <= float(prevU)+1e-10
assert float(LH) <= float(DH)+1e-10 <= float(newH)+1e-10 <= float(prevH)+1e-10
assert all(sols[n][1] > 0 for n in sols)
assert psi_ad > 0
print('ALL_CURVATURE_LOCKED_HSI_CHECKS_PASS')
