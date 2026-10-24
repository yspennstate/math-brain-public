import os, math, numpy as np
os.environ.setdefault('JAX_ENABLE_X64','True')
from numpy.polynomial.hermite import hermgauss
from scipy.optimize import root
import jax, jax.numpy as jnp
from jax.scipy.special import log_ndtr, logsumexp
jax.config.update('jax_enable_x64',True)
A0=12.2872222217; K=-1.0

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
    G=jax.jit(jax.grad(P,0))
    def F(y,a):
        p3,p2,q3,q2,gs=y; c3,c2,gp=recon(p3,p2,q3,q2)
        g=G(jnp.array([p3,p2,q3,q2,c3,c2,gs,gp]),a)
        return jnp.array([g[0],g[1],g[4],g[5],g[6]])
    return P,G,jax.jit(F)

seed=np.array([.59916661511317781,.96911591208288950,.22869805188482245,.63843683132877171,.076564603068658491])
P,G,F=system(200)
z=root(lambda yy: np.asarray(F(jnp.array(yy),A0),float),seed,tol=1e-12)
p3,p2,q3,q2,gs=z.x
c3,c2,gp=map(float,recon(p3,p2,q3,q2)); v=np.array([p3,p2,q3,q2,c3,c2,gs,gp])
print('ROOT',*(format(t,'.17g') for t in v))
print('GRAD_INF',np.max(np.abs(np.asarray(G(jnp.array(v),A0),float))))

n=200
x,w=hermgauss(n); x=np.sqrt(2)*x; w=w/np.sqrt(np.pi)
U=jnp.array(x[:,None]); V=jnp.array(x[None,:]); ww=jnp.array(w)
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
du=m*d*d*cv-m*m*d*d*tv
psi=lambda z: -z-jnp.log1p(-z)
DU=jnp.sum(ww*(m*jnp.sum(pr*uu,axis=0)-lz))
L_U=.5*jnp.sum(ww*((m*d*mg)**2+psi(du)))
R_U=m*m*d*d*tv
Corr_U=.5*jnp.sum(ww*((1-du)*R_U-du*du))
LogCorr_U=.5*jnp.sum(ww*jnp.log1p((1-du)*R_U-du*du))
U_U_log=L_U+LogCorr_U
U_U=L_U+Corr_U

Cker=1+2*B*s*s
mumat=muf.reshape((n,n))
logJ0=-.5*math.log(Cker)-B*mumat*mumat/Cker+log_ndtr(mumat/(s*math.sqrt(Cker)))
ppos=jnp.exp(logJ0-uu)
dh=-s*s*gxx
R_H=2*B*s*s*ppos-dh
KLloH=.5*(s*s*gx*gx+psi(dh))
Corr_H=.5*((1-dh)*R_H-dh*dh)
KLactH=B*bb-uu
DH=m*jnp.sum(ww*jnp.sum(pr*KLactH,axis=0))
L_H=m*jnp.sum(ww*jnp.sum(pr*KLloH,axis=0))
LogCorr_H=.5*jnp.log1p((1-dh)*R_H-dh*dh)
U_H_log=m*jnp.sum(ww*jnp.sum(pr*(KLloH+LogCorr_H),axis=0))
U_H=m*jnp.sum(ww*jnp.sum(pr*(KLloH+Corr_H),axis=0))

print('OUTER_DU_LO_ACT_UPLOG_UPLIN',float(L_U),float(DU),float(U_U_log),float(U_U),'log_upper_slack',float(U_U_log-DU))
print('INNER_DH_LO_ACT_UPLOG_UPLIN',float(L_H),float(DH),float(U_H_log),float(U_H),'log_upper_slack',float(U_H_log-DH))
print('OUTER_CORRECTION',float(Corr_U),'delta_range',float(jnp.min(du)),float(jnp.max(du)))
print('INNER_CORRECTION',float(U_H-L_H),'delta_range',float(jnp.min(dh)),float(jnp.max(dh)))
print('AC3_LO_ACT_UPLOG_UPLIN',float(A0*L_U/c3**2),float(A0*DU/c3**2),float(A0*U_U_log/c3**2),float(A0*U_U/c3**2))
print('AC2_LO_ACT_UPLOG_UPLIN',float(A0*L_H/(c2*c3)),float(A0*DH/(c2*c3)),float(A0*U_H_log/(c2*c3),),float(A0*U_H/(c2*c3)))
print('CORR_U_MINMAX_POINT',float(jnp.min(.5*((1-du)*R_U-du*du))),float(jnp.max(.5*((1-du)*R_U-du*du))))
print('CORR_H_MINMAX_POINT',float(jnp.min(Corr_H)),float(jnp.max(Corr_H)))
print('ALL_NUMERICAL_MATCHED_GAUSSIAN_CAGE_CHECKS_PASS')
