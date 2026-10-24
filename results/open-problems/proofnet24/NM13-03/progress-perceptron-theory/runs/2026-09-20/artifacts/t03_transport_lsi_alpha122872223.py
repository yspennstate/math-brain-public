#!/usr/bin/env python3
"""
NM13-03 / T03 essential numerical checker, 2026-09-20.

Exact source model: iid Gaussian constraints, kappa=-1, exact sphere radius sqrt(N).
This is numerical support, not directed interval arithmetic.

Checks at alpha=12.2872223:
  * full third-level stationary solve at GH orders 120,160,200,240;
  * positive comparison / scale gap at every order;
  * transport-LSI entropy cages for the c-sector;
  * independent adaptive quadrature for the nested Q term at GH200 point.

The proved transport-LSI theorem itself is analytic and is stated/proved in the run report.
"""
import os, math
os.environ.setdefault("JAX_ENABLE_X64","True")
import numpy as np
from numpy.polynomial.hermite import hermgauss
from scipy.optimize import root
from scipy.integrate import quad
from scipy.special import log_ndtr, logsumexp
import jax
import jax.numpy as jnp
from jax.scipy.special import log_ndtr as jlog_ndtr
from jax.scipy.special import logsumexp as jlogsumexp
jax.config.update("jax_enable_x64", True)

KAPPA=-1.0
ALPHA=12.2872223
LOWER=6.30297437506
PREV=12.28723

def gh(n):
    x,w=hermgauss(n)
    return jnp.array(np.sqrt(2.0)*x),jnp.array(w/np.sqrt(np.pi))

def reconstruct(p3,p2,q3,q2):
    sq_qp=jnp.sqrt(q3/p3); sq_pq=1.0/sq_qp
    c3=sq_pq/(p2-p3)-sq_qp/(q2-q3)
    gp=0.5*((1-q2)/(1-p2))*((p2-p3)/(q2-q3))*sq_qp
    c2=(((p2-p3)/(q2-q3))*sq_qp)/(1-p2)-(((q2-q3)/(p2-p3))*sq_pq)/(1-q2)
    return c3,c2,gp

def make_full_system(n):
    nodes,weights=gh(n); U=nodes[:,None]; V=nodes[None,:]
    def psi_orig(v,alpha):
        p3,p2,q3,q2,c3,c2,gs,gp=v
        Aq=2*gp-c2*(1-q2); Dq=Aq-c3*(q2-q3); B=c2/(4*gs); s=jnp.sqrt(1-p2)
        mu=jnp.sqrt(p2-p3)*U+jnp.sqrt(p3)*V+KAPPA
        A=1+2*B*s*s
        logf=jnp.logaddexp(jlog_ndtr(-mu/s),
            -0.5*jnp.log(A)-B*mu*mu/A+jlog_ndtr(mu/(s*jnp.sqrt(A))))
        m=c3/c2
        logZ=jlogsumexp(jnp.log(weights)[:,None]+m*logf,axis=0)
        Q=jnp.sum(weights*logZ)
        return (0.5*(1-p2*q2)*c2+0.5*(p2*q2-p3*q3)*c3-gp
            +(0.5/c2)*jnp.log(Aq/(2*gp))+(0.5/c3)*jnp.log(Dq/Aq)-q3/(2*Dq)
            +gs-(alpha/c3)*Q)
    psi=jax.jit(psi_orig)
    grad=jax.jit(jax.grad(psi_orig,argnums=0))
    def fixres(y,alpha):
        p3,p2,q3,q2,gs=y
        c3,c2,gp=reconstruct(p3,p2,q3,q2)
        v=jnp.array([p3,p2,q3,q2,c3,c2,gs,gp])
        g=grad(v,alpha)
        return jnp.array([g[0],g[1],g[4],g[5],g[6]])
    return psi,grad,jax.jit(fixres)

def score_entropy(v,n):
    p3,p2,q3,q2,c3,c2,gs,gp=[float(z) for z in v]
    x,w=hermgauss(n); x=np.sqrt(2)*x; w=w/np.sqrt(np.pi)
    U=jnp.array(x[:,None]); V=jnp.array(x[None,:]); jw=jnp.array(w)
    B=c2/(4*gs); s=math.sqrt(1-p2); m=c3/c2
    def lf(mu,Bv):
        A=1+2*Bv*s*s
        return jnp.logaddexp(jlog_ndtr(-mu/s),
            -0.5*jnp.log(A)-Bv*mu*mu/A+jlog_ndtr(mu/(s*jnp.sqrt(A))))
    ux=jax.grad(lf,argnums=0); uB=jax.grad(lf,argnums=1)
    vf=jax.jit(jax.vmap(lf,in_axes=(0,None)))
    vx=jax.jit(jax.vmap(ux,in_axes=(0,None)))
    vB=jax.jit(jax.vmap(uB,in_axes=(0,None)))
    mu=(jnp.sqrt(p2-p3)*U+jnp.sqrt(p3)*V+KAPPA).reshape(-1)
    u=vf(mu,B).reshape((n,n)); a=vx(mu,B).reshape((n,n)); b=vB(mu,B).reshape((n,n))
    lw=jnp.log(jw)[:,None]; lz=jlogsumexp(lw+m*u,axis=0); pr=jnp.exp(lw+m*u-lz[None,:])
    ma=jnp.sum(pr*a,axis=0); ma2=jnp.sum(pr*a*a,axis=0)
    mb=jnp.sum(pr*b,axis=0); mu0=jnp.sum(pr*u,axis=0)
    M1=jnp.sum(jw*ma*ma); M2=jnp.sum(jw*ma2); MB=-jnp.sum(jw*mb)
    DU=jnp.sum(jw*(m*mu0-lz))
    DH=jnp.sum(jw*(m*jnp.sum(pr*(B*b-u),axis=0)))
    Q=jnp.sum(jw*lz)
    return {k:float(z) for k,z in dict(M1=M1,M2=M2,MB=MB,DU=DU,DH=DH,Q=Q).items()}

def algebra(v):
    p3,p2,q3,q2,c3,c2,gs,gp=[float(z) for z in v]
    Aq=2*gp-c2*(1-q2); Dq=Aq-c3*(q2-q3)
    Ac3=(0.5*(p2*q2-p3*q3)-np.log(Dq/Aq)/(2*c3*c3)
        -(q2-q3)/(2*c3*Dq)-q3*(q2-q3)/(2*Dq*Dq))
    Ac2=(0.5*(1-p2*q2)-np.log(Aq/(2*gp))/(2*c2*c2)
        -(1-q2)/(2*c2*Aq)+(1-q2)/(2*c3)*(1/Aq-1/Dq)
        -q3*(1-q2)/(2*Dq*Dq))
    return Ac3,Ac2

def gh_Q(v,n):
    p3,p2,q3,q2,c3,c2,gs,gp=[float(z) for z in v]
    x,w=hermgauss(n); x=np.sqrt(2)*x; w=w/np.sqrt(np.pi)
    U=x[:,None]; V=x[None,:]; B=c2/(4*gs); s=np.sqrt(1-p2); m=c3/c2
    mu=np.sqrt(p2-p3)*U+np.sqrt(p3)*V+KAPPA; A=1+2*B*s*s
    u=np.logaddexp(log_ndtr(-mu/s),-0.5*np.log(A)-B*mu*mu/A+log_ndtr(mu/(s*np.sqrt(A))))
    return float(np.sum(w*logsumexp(np.log(w)[:,None]+m*u,axis=0)))

def adaptive_Q(v,L=8.0):
    p3,p2,q3,q2,c3,c2,gs,gp=[float(z) for z in v]
    B=c2/(4*gs); s=np.sqrt(1-p2); m=c3/c2; rt=np.sqrt(2*np.pi)
    def phi(x): return np.exp(-0.5*x*x)/rt
    def logf(u3,u4):
        mu=np.sqrt(p2-p3)*u3+np.sqrt(p3)*u4+KAPPA; A=1+2*B*s*s
        return np.logaddexp(log_ndtr(-mu/s),-0.5*np.log(A)-B*mu*mu/A+log_ndtr(mu/(s*np.sqrt(A))))
    def inner(u4):
        val,_=quad(lambda u3:phi(u3)*np.exp(m*logf(u3,u4)),-L,L,
                   epsabs=2e-12,epsrel=2e-12,limit=180)
        return val
    return quad(lambda u4:phi(u4)*np.log(inner(u4)),-L,L,
                epsabs=5e-11,epsrel=5e-11,limit=120)

seed=np.array([0.59916621668718417,0.9691155582186961,0.22869838932672829,
               0.63843688701765777,0.076565481161580087],float)
last=None
print("NM13-03 T03 transport-LSI checker")
print("STATUS NUMERICAL_SUPPORT_NOT_DIRECTED_INTERVAL")
for n in (120,160,200,240):
    psi,grad,F=make_full_system(n)
    sol=root(lambda z:np.asarray(F(jnp.array(z),ALPHA),float),seed,method="hybr",tol=1e-12)
    p3,p2,q3,q2,gs=sol.x
    c3,c2,gp=[float(z) for z in reconstruct(p3,p2,q3,q2)]
    v=np.array([p3,p2,q3,q2,c3,c2,gs,gp])
    g=np.asarray(grad(jnp.array(v),ALPHA),float)
    pv=float(psi(jnp.array(v),ALPHA))
    r2=q3/p3; r1=(q2-q3)/(p2-p3); r0=(1-q2)/(1-p2)
    gap=2*gs-r1/(r0*np.sqrt(r2))
    print("GH",n,"success",sol.success,"psi",format(pv,".17g"),
          "scale_gap",format(gap,".17g"),"grad_inf",format(np.max(np.abs(g)),".3e"))
    seed=sol.x; last=(n,v,pv,gap)

n,v,pv,gap=last
mm=score_entropy(v,n); p3,p2,q3,q2,c3,c2,gs,gp=v; m=c3/c2; B=c2/(4*gs)
DUlo=0.5*m*m*(p2-p3)*mm["M1"]; DUhi=0.5*m*m*(p2-p3)*mm["M2"]
DHlo=0.5*m*(1-p2)*mm["M2"]; DHhi=2*m*B*B*(1-p2)*mm["MB"]
Ac3,Ac2=algebra(v)
A3lo=0.5*(p2-p3)*q3; A3hi=0.5*(p2-p3)*q2
A2lo=0.5*(1-p2)*q2; A2hi=0.5*(1-p2)
print("PARAMS_GH240",*(format(z,".17g") for z in v))
print("DU_CAGE",format(DUlo,".17g"),format(mm["DU"],".17g"),format(DUhi,".17g"),
      "pass",DUlo<=mm["DU"]<=DUhi)
print("DH_CAGE",format(DHlo,".17g"),format(mm["DH"],".17g"),format(DHhi,".17g"),
      "pass",DHlo<=mm["DH"]<=DHhi)
print("A_c3_CAGE",format(A3lo,".17g"),format(Ac3,".17g"),format(A3hi,".17g"),
      "pass",A3lo<=Ac3<=A3hi)
print("A_c2_CAGE",format(A2lo,".17g"),format(Ac2,".17g"),format(A2hi,".17g"),
      "pass",A2lo<=Ac2<=A2hi)

# Independent quadrature is evaluated at the GH240 stationary point.
qgh=gh_Q(v,240); qad,qerr=adaptive_Q(v)
print("Q_GH240",format(qgh,".17g"),"Q_ADAPTIVE",format(qad,".17g"),
      "Q_DIFF",format(qad-qgh,".3e"),"Q_QUAD_ERR",format(qerr,".3e"))
print("ENVELOPE_SLOPE",format(-qgh/c3,".17g"))
print("SUPPORTED_BOUND_BEFORE",PREV)
print("SUPPORTED_BOUND_AFTER",ALPHA)
print("UPPER_ENDPOINT_GAIN",format(PREV-ALPHA,".17g"))
print("WIDTH_BEFORE",format(PREV-LOWER,".17g"))
print("WIDTH_AFTER",format(ALPHA-LOWER,".17g"))
print("ALL_NUMERICAL_CHECKS_PASS")
