#!/usr/bin/env python3
# NM13-03 / T03, 2026-09-20. Numerical support, NOT directed interval arithmetic.
import os, math, numpy as np
os.environ.setdefault("JAX_ENABLE_X64","True")
from numpy.polynomial.hermite import hermgauss
from scipy.optimize import root
import jax, jax.numpy as jnp
from jax.scipy.special import log_ndtr, logsumexp
jax.config.update("jax_enable_x64",True)
K=-1.0; A0=12.2872222217; PREV=12.28722223; LOWER=6.30297437506

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

def cage(v,n=240):
    p3,p2,q3,q2,c3,c2,gs,gp=map(float,v)
    x,w=hermgauss(n); x=np.sqrt(2)*x; w=w/np.sqrt(np.pi)
    U=jnp.array(x[:,None]); V=jnp.array(x[None,:]); w=jnp.array(w)
    B=c2/(4*gs); s=math.sqrt(1-p2); d=math.sqrt(p2-p3); m=c3/c2
    def u(mu,Bv):
        C=1+2*Bv*s*s
        return jnp.logaddexp(log_ndtr(-mu/s),-.5*jnp.log(C)-Bv*mu*mu/C+log_ndtr(mu/(s*jnp.sqrt(C))))
    ux=jax.grad(u,0); uxx=jax.grad(ux,0); uB=jax.grad(u,1)
    vf=jax.jit(jax.vmap(u,in_axes=(0,None))); vx=jax.jit(jax.vmap(ux,in_axes=(0,None)))
    vxx=jax.jit(jax.vmap(uxx,in_axes=(0,None))); vB=jax.jit(jax.vmap(uB,in_axes=(0,None)))
    mu=(d*U+jnp.sqrt(p3)*V+K).reshape(-1)
    uu=vf(mu,B).reshape((n,n)); gx=vx(mu,B).reshape((n,n))
    gxx=vxx(mu,B).reshape((n,n)); bb=vB(mu,B).reshape((n,n))
    lz=logsumexp(jnp.log(w)[:,None]+m*uu,axis=0); pr=jnp.exp(jnp.log(w)[:,None]+m*uu-lz[None,:])
    mg=jnp.sum(pr*gx,0); m2=jnp.sum(pr*gx*gx,0); tv=m2-mg*mg; cv=-jnp.sum(pr*gxx,0)
    meanU=jnp.sum(pr*U,0); varU=jnp.sum(pr*U*U,0)-meanU*meanU
    du=m*d*d*cv-m*m*d*d*tv; ident=jnp.max(jnp.abs(1-varU-du))
    ps=lambda z:-z-jnp.log1p(-z)
    DU=jnp.sum(w*(m*jnp.sum(pr*uu,0)-lz))
    DUnew=.5*jnp.sum(w*((m*d*mg)**2+ps(du)))
    M1=jnp.sum(w*mg*mg); M2=jnp.sum(w*m2); MB=-jnp.sum(w*jnp.sum(pr*bb,0))
    C=4*B*B*MB; L=2*B/(1+2*B*s*s); oldtu=m*(M2-M1)/L
    DUold=.5*m*m*d*d*M1+.5*ps(oldtu)
    DUj=.5*m*m*d*d*M1+.5*ps(jnp.sum(w*du))
    dh=-s*s*gxx
    DH=m*jnp.sum(w*jnp.sum(pr*(B*bb-uu),0))
    DHnew=.5*m*jnp.sum(w*jnp.sum(pr*(s*s*gx*gx+ps(dh)),0))
    oldth=C*(1-q2)/(2*B); DHold=.5*m*s*s*M2+.5*m*ps(oldth)
    return dict(ident=float(ident),dumin=float(jnp.min(du)),dumax=float(jnp.max(du)),
                dhmin=float(jnp.min(dh)),dhmax=float(jnp.max(dh)),
                Ac3=float(A0*DU/c3**2),Ac3old=float(A0*DUold/c3**2),
                Ac3j=float(A0*DUj/c3**2),Ac3new=float(A0*DUnew/c3**2),
                Ac2=float(A0*DH/(c2*c3)),Ac2old=float(A0*DHold/(c2*c3)),
                Ac2new=float(A0*DHnew/(c2*c3)))

seed=np.array([.59916661511317781,.96911591208288950,.22869805188482245,.63843683132877171,.076564603068658491])
last=None
print("STATUS NUMERICAL_SUPPORT_NOT_DIRECTED_INTERVAL")
print("ALPHA",format(A0,".13f"))
for n in (120,160,200,240):
    P,G,F=system(n); z=root(lambda y:np.asarray(F(jnp.array(y),A0),float),seed,tol=1e-12)
    p3,p2,q3,q2,gs=z.x; c3,c2,gp=map(float,recon(p3,p2,q3,q2))
    v=np.array([p3,p2,q3,q2,c3,c2,gs,gp]); g=np.asarray(G(jnp.array(v),A0),float)
    val=float(P(jnp.array(v),A0))
    r2=q3/p3; r1=(q2-q3)/(p2-p3); r0=(1-q2)/(1-p2); gap=2*gs-r1/(r0*np.sqrt(r2))
    print("GH",n,"psi",format(val,".17g"),"gap",format(gap,".17g"),"grad_inf",format(np.max(abs(g)),".3e"))
    seed=z.x; last=v
c=cage(last)
print("PARAMS_GH240",*(format(x,".17g") for x in last))
print("DEFICIT_IDENTITY_INF",format(c["ident"],".3e"))
print("DELTA_U_RANGE",c["dumin"],c["dumax"],"DELTA_H_RANGE",c["dhmin"],c["dhmax"])
print("C3_CAGE",c["Ac3old"],c["Ac3j"],c["Ac3new"],c["Ac3"])
print("C2_CAGE",c["Ac2old"],c["Ac2new"],c["Ac2"])
print("SUPPORTED_BOUND_BEFORE",PREV,"AFTER",A0,"GAIN",PREV-A0)
print("WIDTH_AFTER",A0-LOWER)
assert c["Ac3old"]<=c["Ac3j"]<=c["Ac3new"]<=c["Ac3"]+1e-10
assert c["Ac2old"]<=c["Ac2new"]<=c["Ac2"]+1e-10
print("ALL_NUMERICAL_CHECKS_PASS")
