#!/usr/bin/env python3
# NM13-03 / T03 2026-09-20. Numerical support, NOT directed interval arithmetic.
import os, math, numpy as np
os.environ.setdefault('JAX_ENABLE_X64','True')
from numpy.polynomial.hermite import hermgauss
from scipy.optimize import root
from scipy.integrate import quad
from scipy.special import log_ndtr as sp_log_ndtr
import jax, jax.numpy as jnp
from jax.scipy.special import log_ndtr, logsumexp
jax.config.update('jax_enable_x64',True)
K=-1.0; A0=12.28722222161; PREV=12.2872222217; LOWER=6.30297437506

def gh(n):
    x,w=hermgauss(n); return jnp.array(np.sqrt(2)*x),jnp.array(w/np.sqrt(np.pi))
def recon(p3,p2,q3,q2):
    r=jnp.sqrt(q3/p3); ri=1/r
    c3=ri/(p2-p3)-r/(q2-q3)
    gp=.5*((1-q2)/(1-p2))*((p2-p3)/(q2-q3))*r
    c2=(((p2-p3)/(q2-q3))*r)/(1-p2)-(((q2-q3)/(p2-p3))*ri)/(1-q2)
    return c3,c2,gp

def system(n):
    x,w=gh(n); U=x[:,None]; V=x[None,:]
    def P(v,a):
        p3,p2,q3,q2,c3,c2,gs,gp=v
        Aq=2*gp-c2*(1-q2); Dq=Aq-c3*(q2-q3); B=c2/(4*gs); s=jnp.sqrt(1-p2)
        mu=jnp.sqrt(p2-p3)*U+jnp.sqrt(p3)*V+K; C=1+2*B*s*s
        u=jnp.logaddexp(log_ndtr(-mu/s),-.5*jnp.log(C)-B*mu*mu/C+log_ndtr(mu/(s*jnp.sqrt(C))))
        m=c3/c2; Q=jnp.sum(w*logsumexp(jnp.log(w)[:,None]+m*u,axis=0))
        return (.5*(1-p2*q2)*c2+.5*(p2*q2-p3*q3)*c3-gp
                +.5/c2*jnp.log(Aq/(2*gp))+.5/c3*jnp.log(Dq/Aq)-q3/(2*Dq)+gs-a*Q/c3)
    G=jax.jit(jax.grad(P,0)); PJ=jax.jit(P)
    def F(y,a):
        p3,p2,q3,q2,gs=y; c3,c2,gp=recon(p3,p2,q3,q2)
        g=G(jnp.array([p3,p2,q3,q2,c3,c2,gs,gp]),a)
        return jnp.array([g[0],g[1],g[4],g[5],g[6]])
    return PJ,G,jax.jit(F)

def adaptive_Q(v,L=8.0):
    p3,p2,q3,q2,c3,c2,gs,gp=map(float,v)
    B=c2/(4*gs); s=math.sqrt(1-p2); m=c3/c2; rt=math.sqrt(2*math.pi)
    def phi(x): return math.exp(-.5*x*x)/rt
    def logf(u3,u4):
        mu=math.sqrt(p2-p3)*u3+math.sqrt(p3)*u4+K; C=1+2*B*s*s
        return np.logaddexp(sp_log_ndtr(-mu/s),-.5*math.log(C)-B*mu*mu/C+sp_log_ndtr(mu/(s*math.sqrt(C))))
    def inner(u4):
        val,_=quad(lambda u3:phi(u3)*math.exp(m*logf(u3,u4)),-L,L,epsabs=2e-12,epsrel=2e-12,limit=180)
        return val
    val,err=quad(lambda u4:phi(u4)*math.log(inner(u4)),-L,L,epsabs=5e-11,epsrel=5e-11,limit=140)
    return val,err

def algebra_without_Q(v):
    p3,p2,q3,q2,c3,c2,gs,gp=map(float,v)
    Aq=2*gp-c2*(1-q2); Dq=Aq-c3*(q2-q3)
    return (.5*(1-p2*q2)*c2+.5*(p2*q2-p3*q3)*c3-gp
            +.5/c2*math.log(Aq/(2*gp))+.5/c3*math.log(Dq/Aq)-q3/(2*Dq)+gs)

seed=np.array([.59916661553777206,.96911591246056061,.22869805152395933,.63843683126824713,.076564602131018136])
print('STATUS NUMERICAL_SUPPORT_NOT_DIRECTED_INTERVAL')
print('ALPHA',format(A0,'.14f'))
last=None
for n in (120,160,200,240,280):
    P,G,F=system(n); z=root(lambda y:np.asarray(F(jnp.array(y),A0),float),seed,tol=1e-12)
    p3,p2,q3,q2,gs=z.x; c3,c2,gp=map(float,recon(p3,p2,q3,q2)); v=np.array([p3,p2,q3,q2,c3,c2,gs,gp])
    g=np.asarray(G(jnp.array(v),A0),float); val=float(P(jnp.array(v),A0))
    r2=q3/p3; r1=(q2-q3)/(p2-p3); r0=(1-q2)/(1-p2); gap=2*gs-r1/(r0*np.sqrt(r2))
    print('GH',n,'psi',format(val,'.17g'),'gap',format(gap,'.17g'),'grad_inf',format(np.max(abs(g)),'.3e'))
    seed=z.x; last=v

n=240
p3,p2,q3,q2,c3,c2,gs,gp=map(float,last)
x,w=hermgauss(n); x=np.sqrt(2)*x; w=w/np.sqrt(np.pi); ww=jnp.array(w)
U=jnp.array(x[:,None]); V=jnp.array(x[None,:])
B=c2/(4*gs); s=math.sqrt(1-p2); d=math.sqrt(p2-p3); m=c3/c2

def u(mu,Bv):
    C=1+2*Bv*s*s
    return jnp.logaddexp(log_ndtr(-mu/s),-.5*jnp.log(C)-Bv*mu*mu/C+log_ndtr(mu/(s*jnp.sqrt(C))))
ux=jax.grad(u,0); uxx=jax.grad(ux,0); uB=jax.grad(u,1)
vf=jax.jit(jax.vmap(u,in_axes=(0,None))); vx=jax.jit(jax.vmap(ux,in_axes=(0,None))); vxx=jax.jit(jax.vmap(uxx,in_axes=(0,None))); vB=jax.jit(jax.vmap(uB,in_axes=(0,None)))
muf=(d*U+jnp.sqrt(p3)*V+K).reshape(-1)
uu=vf(muf,B).reshape((n,n)); gx=vx(muf,B).reshape((n,n)); gxx=vxx(muf,B).reshape((n,n)); bb=vB(muf,B).reshape((n,n))
lz=logsumexp(jnp.log(ww)[:,None]+m*uu,axis=0); pr=jnp.exp(jnp.log(ww)[:,None]+m*uu-lz[None,:])
mg=jnp.sum(pr*gx,axis=0); m2=jnp.sum(pr*gx*gx,axis=0); tv=m2-mg*mg; cv=-jnp.sum(pr*gxx,axis=0)
du=jnp.maximum(0.0,m*d*d*cv-m*m*d*d*tv); vu=1-du
psi=lambda z:-z-jnp.log1p(-z)
DU=jnp.sum(ww*(m*jnp.sum(pr*uu,axis=0)-lz)); L_U=.5*jnp.sum(ww*((m*d*mg)**2+psi(du)))
R_U=m*m*d*d*tv; Irel_U=jnp.maximum(0.0,R_U-du*du/vu)
oldcorr_U=.5*jnp.log1p(vu*Irel_U)
dsafe=jnp.maximum(du,1e-300)
hsicorr_U=(dsafe/(2*vu))*jnp.log1p(vu*vu*Irel_U/dsafe)
hsicorr_U=jnp.where(du>1e-14,hsicorr_U,0.0)
Old_U=L_U+jnp.sum(ww*oldcorr_U); HSI_U=L_U+jnp.sum(ww*jnp.minimum(oldcorr_U,hsicorr_U))

Cker=1+2*B*s*s; mumat=muf.reshape((n,n))
logJ0=-.5*math.log(Cker)-B*mumat*mumat/Cker+log_ndtr(mumat/(s*math.sqrt(Cker)))
ppos=jnp.exp(logJ0-uu); dh=jnp.maximum(0.0,-s*s*gxx); vh=1-dh
RH=2*B*s*s*ppos-dh; Irel_H=jnp.maximum(0.0,RH-dh*dh/vh)
KLloH=.5*(s*s*gx*gx+psi(dh)); KLactH=B*bb-uu
DH=m*jnp.sum(ww*jnp.sum(pr*KLactH,axis=0)); L_H=m*jnp.sum(ww*jnp.sum(pr*KLloH,axis=0))
oldcorr_H=.5*jnp.log1p(vh*Irel_H)
dhsafe=jnp.maximum(dh,1e-300); hsicorr_H=(dhsafe/(2*vh))*jnp.log1p(vh*vh*Irel_H/dhsafe); hsicorr_H=jnp.where(dh>1e-14,hsicorr_H,0.0)
Old_H=m*jnp.sum(ww*jnp.sum(pr*(KLloH+oldcorr_H),axis=0)); HSI_H=m*jnp.sum(ww*jnp.sum(pr*(KLloH+jnp.minimum(oldcorr_H,hsicorr_H)),axis=0))

print('PARAMS_GH280',*(format(t,'.17g') for t in last))
print('OUTER_DU_LO_ACT_MATCHEDUP_HSIUP',float(L_U),float(DU),float(Old_U),float(HSI_U),'HSI_SLACK',float(HSI_U-DU))
print('INNER_DH_LO_ACT_MATCHEDUP_HSIUP',float(L_H),float(DH),float(Old_H),float(HSI_H),'HSI_SLACK',float(HSI_H-DH))
print('AC3_LO_ACT_MATCHEDUP_HSIUP',float(A0*L_U/c3**2),float(A0*DU/c3**2),float(A0*Old_U/c3**2),float(A0*HSI_U/c3**2))
print('AC2_LO_ACT_MATCHEDUP_HSIUP',float(A0*L_H/(c2*c3)),float(A0*DH/(c2*c3)),float(A0*Old_H/(c2*c3)),float(A0*HSI_H/(c2*c3)))
print('HSI_TIGHTENS_OUTER',float(Old_U-HSI_U),'INNER',float(Old_H-HSI_H))
qad,err=adaptive_Q(last)
psi_ad=algebra_without_Q(last)-A0*qad/c3
print('ADAPTIVE_Q',format(qad,'.17g'),'reported_quad_err',format(err,'.3e'),'PSI_ADAPTIVE',format(psi_ad,'.17g'))
print('SUPPORTED_BOUND_BEFORE',PREV,'AFTER',A0,'GAIN',PREV-A0,'WIDTH_AFTER',A0-LOWER)
assert float(L_U) <= float(DU)+1e-10 <= float(HSI_U)+1e-10 <= float(Old_U)+1e-10
assert float(L_H) <= float(DH)+1e-10 <= float(HSI_H)+1e-10 <= float(Old_H)+1e-10
assert psi_ad>0
print('ALL_STEIN_HSI_CHECKS_PASS')
