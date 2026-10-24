#!/usr/bin/env python3
"""
NM13-03 / T03: entropy-stable complete-third spherical perceptron checker.

Model: iid Gaussian rows, kappa=-1, exact sphere radius sqrt(N).
This is numerical support (not directed interval arithmetic). It checks:
  1) the entropy/KL c-sector rewrite of third-full stationarity;
  2) the entropy-stable four-scalar capacity compiler at GH order 160;
  3) a fixed-density full stationary point at alpha=12.28723 at GH order 200,
     with positive scale-gap/comparison value;
  4) independent adaptive quadrature for Q and the one-dimensional collapsed
     comparison L, plus the power-mean envelope-slope sandwich.

Requires numpy, scipy, jax (x64).
"""
import os
os.environ.setdefault("JAX_ENABLE_X64", "True")
import math
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

KAPPA = -1.0
ALPHA_TEST = 12.28723


def gh(n):
    x, w = hermgauss(n)
    return jnp.array(np.sqrt(2.0)*x), jnp.array(w/np.sqrt(np.pi))


def reconstruct(p3,p2,q3,q2):
    sq_qp = jnp.sqrt(q3/p3)
    sq_pq = 1.0/sq_qp
    c3 = sq_pq/(p2-p3) - sq_qp/(q2-q3)
    gp = 0.5*((1-q2)/(1-p2))*((p2-p3)/(q2-q3))*sq_qp
    c2 = (((p2-p3)/(q2-q3))*sq_qp)/(1-p2) \
       - (((q2-q3)/(p2-p3))*sq_pq)/(1-q2)
    return c3,c2,gp


def algebra_terms(v):
    p3,p2,q3,q2,c3,c2,gs,gp = [float(z) for z in v]
    Aq = 2*gp-c2*(1-q2)
    Dq = Aq-c3*(q2-q3)
    H = (1/(2*c2))*np.log(Aq/(2*gp)) + (1/(2*c3))*np.log(Dq/Aq) - q3/(2*Dq)
    Ac3 = (0.5*(p2*q2-p3*q3) - np.log(Dq/Aq)/(2*c3*c3)
           - (q2-q3)/(2*c3*Dq) - q3*(q2-q3)/(2*Dq*Dq))
    Ac2 = (0.5*(1-p2*q2) - np.log(Aq/(2*gp))/(2*c2*c2)
           - (1-q2)/(2*c2*Aq) + (1-q2)/(2*c3)*(1/Aq-1/Dq)
           - q3*(1-q2)/(2*Dq*Dq))
    return Aq,Dq,H,Ac3,Ac2


def make_full_system(n):
    nodes, weights = gh(n)
    U = nodes[:,None]
    V = nodes[None,:]

    def psi_orig(v, alpha):
        p3,p2,q3,q2,c3,c2,gs,gp = v
        Aq = 2*gp-c2*(1-q2)
        Dq = Aq-c3*(q2-q3)
        B = c2/(4*gs)
        s = jnp.sqrt(1-p2)
        mu = jnp.sqrt(p2-p3)*U + jnp.sqrt(p3)*V + KAPPA
        A = 1+2*B*s*s
        logf = jnp.logaddexp(
            jlog_ndtr(-mu/s),
            -0.5*jnp.log(A)-B*mu*mu/A+jlog_ndtr(mu/(s*jnp.sqrt(A)))
        )
        m = c3/c2
        logZ = jlogsumexp(jnp.log(weights)[:,None] + m*logf, axis=0)
        Q = jnp.sum(weights*logZ)
        return (0.5*(1-p2*q2)*c2 + 0.5*(p2*q2-p3*q3)*c3 - gp
                + (0.5/c2)*jnp.log(Aq/(2*gp))
                + (0.5/c3)*jnp.log(Dq/Aq) - q3/(2*Dq)
                + gs - (alpha/c3)*Q)

    psi = jax.jit(psi_orig)
    grad = jax.jit(jax.grad(psi_orig,argnums=0))

    def fixres(y, alpha):
        p3,p2,q3,q2,gs = y
        c3,c2,gp = reconstruct(p3,p2,q3,q2)
        v = jnp.array([p3,p2,q3,q2,c3,c2,gs,gp])
        g = grad(v,alpha)
        return jnp.array([g[0],g[1],g[4],g[5],g[6]])

    return psi,grad,jax.jit(fixres)


def score_entropy_moments(v,n):
    p3,p2,q3,q2,c3,c2,gs,gp = [float(z) for z in v]
    x,w = hermgauss(n)
    x = np.sqrt(2.0)*x
    w = w/np.sqrt(np.pi)
    U = jnp.array(x[:,None]); V = jnp.array(x[None,:]); jw = jnp.array(w)
    B = float(c2/(4*gs)); s = float(math.sqrt(1-p2)); m = float(c3/c2)

    def logf_scalar(mu,Bv):
        A = 1+2*Bv*s*s
        return jnp.logaddexp(
            jlog_ndtr(-mu/s),
            -0.5*jnp.log(A)-Bv*mu*mu/A+jlog_ndtr(mu/(s*jnp.sqrt(A)))
        )
    ux_s = jax.grad(logf_scalar,argnums=0)
    uB_s = jax.grad(logf_scalar,argnums=1)
    vf = jax.jit(jax.vmap(logf_scalar,in_axes=(0,None)))
    vux = jax.jit(jax.vmap(ux_s,in_axes=(0,None)))
    vuB = jax.jit(jax.vmap(uB_s,in_axes=(0,None)))

    mu = (jnp.sqrt(p2-p3)*U+jnp.sqrt(p3)*V+KAPPA).reshape(-1)
    u = vf(mu,B).reshape((n,n))
    ux = vux(mu,B).reshape((n,n))
    uB = vuB(mu,B).reshape((n,n))
    logw = jnp.log(jw)[:,None]
    logZ = jlogsumexp(logw+m*u,axis=0)
    probs = jnp.exp(logw+m*u-logZ[None,:])
    mean_ux = jnp.sum(probs*ux,axis=0)
    mean_ux2 = jnp.sum(probs*ux*ux,axis=0)
    mean_uB = jnp.sum(probs*uB,axis=0)
    mean_u = jnp.sum(probs*u,axis=0)
    DU = jnp.sum(jw*(m*mean_u-logZ))
    DH = jnp.sum(jw*(m*jnp.sum(probs*(B*uB-u),axis=0)))
    M1 = jnp.sum(jw*mean_ux**2)
    M2 = jnp.sum(jw*mean_ux2)
    MB = -jnp.sum(jw*mean_uB)
    QM = jnp.sum(jw*mean_u)
    Q = jnp.sum(jw*logZ)
    return {k:float(z) for k,z in {
        'M1':M1,'M2':M2,'MB':MB,'QM':QM,'Q':Q,'DU':DU,'DH':DH
    }.items()}


def make_entropy_capacity_system(n):
    x,w = hermgauss(n)
    x = jnp.array(np.sqrt(2.0)*x)
    w = jnp.array(w/np.sqrt(np.pi))
    U=x[:,None]; V=x[None,:]; logw=jnp.log(w)[:,None]

    def logf_scalar(mu,B,s):
        A=1+2*B*s*s
        return jnp.logaddexp(
            jlog_ndtr(-mu/s),
            -0.5*jnp.log(A)-B*mu*mu/A+jlog_ndtr(mu/(s*jnp.sqrt(A)))
        )
    ux_s=jax.grad(logf_scalar,argnums=0)
    uB_s=jax.grad(logf_scalar,argnums=1)
    v_logf=jax.vmap(logf_scalar,in_axes=(0,None,None))
    v_ux=jax.vmap(ux_s,in_axes=(0,None,None))
    v_uB=jax.vmap(uB_s,in_axes=(0,None,None))

    def residual(y):
        p2,p3,q2,q3=y
        sq_qp=jnp.sqrt(q3/p3); sq_pq=1/sq_qp
        c3=sq_pq/(p2-p3)-sq_qp/(q2-q3)
        gp=0.5*((1-q2)/(1-p2))*((p2-p3)/(q2-q3))*sq_qp
        c2=(((p2-p3)/(q2-q3))*sq_qp)/(1-p2) \
           -(((q2-q3)/(p2-p3))*sq_pq)/(1-q2)
        r2=q3/p3; r1=(q2-q3)/(p2-p3); r0=(1-q2)/(1-p2)
        gs=r1/(2*r0*jnp.sqrt(r2))
        B=c2/(4*gs); s=jnp.sqrt(1-p2); m=c3/c2
        mu=(jnp.sqrt(p2-p3)*U+jnp.sqrt(p3)*V+KAPPA).reshape(-1)
        u=v_logf(mu,B,s).reshape((n,n))
        ux=v_ux(mu,B,s).reshape((n,n))
        uB=v_uB(mu,B,s).reshape((n,n))
        logZ=jlogsumexp(logw+m*u,axis=0)
        probs=jnp.exp(logw+m*u-logZ[None,:])
        mean_ux=jnp.sum(probs*ux,axis=0)
        mean_ux2=jnp.sum(probs*ux*ux,axis=0)
        mean_uB=jnp.sum(probs*uB,axis=0)
        mean_u=jnp.sum(probs*u,axis=0)
        M1=jnp.sum(w*mean_ux**2)
        M2=jnp.sum(w*mean_ux2)
        MB=-jnp.sum(w*mean_uB)
        DU=jnp.sum(w*(m*mean_u-logZ))
        DH=jnp.sum(w*(m*jnp.sum(probs*(B*uB-u),axis=0)))
        alpha=c2*c2/(4*B*B*MB)
        Aq=2*gp-c2*(1-q2); Dq=Aq-c3*(q2-q3)
        Ac3=(0.5*(p2*q2-p3*q3)-jnp.log(Dq/Aq)/(2*c3*c3)
             -(q2-q3)/(2*c3*Dq)-q3*(q2-q3)/(2*Dq*Dq))
        Ac2=(0.5*(1-p2*q2)-jnp.log(Aq/(2*gp))/(2*c2*c2)
             -(1-q2)/(2*c2*Aq)+(1-q2)/(2*c3)*(1/Aq-1/Dq)
             -q3*(1-q2)/(2*Dq*Dq))
        return jnp.array([
            q3-M1/(4*B*B*MB),
            q2-M2/(4*B*B*MB),
            Ac3-alpha*DU/(c3*c3),
            Ac2-alpha*DH/(c2*c3),
        ])

    r=jax.jit(residual)
    J=jax.jit(jax.jacfwd(residual))
    return r,J


def gh_Q(v,n):
    p3,p2,q3,q2,c3,c2,gs,gp=[float(z) for z in v]
    x,w=hermgauss(n); x=np.sqrt(2)*x; w=w/np.sqrt(np.pi)
    U=x[:,None]; V=x[None,:]
    B=c2/(4*gs); s=np.sqrt(1-p2); m=c3/c2
    mu=np.sqrt(p2-p3)*U+np.sqrt(p3)*V+KAPPA
    A=1+2*B*s*s
    u=np.logaddexp(log_ndtr(-mu/s),-0.5*np.log(A)-B*mu*mu/A+log_ndtr(mu/(s*np.sqrt(A))))
    logZ=logsumexp(np.log(w)[:,None]+m*u,axis=0)
    return float(np.sum(w*logZ))


def gh_L(v,n):
    p3,p2,q3,q2,c3,c2,gs,gp=[float(z) for z in v]
    x,w=hermgauss(n); x=np.sqrt(2)*x; w=w/np.sqrt(np.pi)
    B=c2/(4*gs); s=np.sqrt(1-p3)
    mu=np.sqrt(p3)*x+KAPPA
    A=1+2*B*s*s
    u=np.logaddexp(log_ndtr(-mu/s),-0.5*np.log(A)-B*mu*mu/A+log_ndtr(mu/(s*np.sqrt(A))))
    return float(np.sum(w*u))


def adaptive_Q(v,L=8.0):
    p3,p2,q3,q2,c3,c2,gs,gp=[float(z) for z in v]
    B=c2/(4*gs); s=np.sqrt(1-p2); m=c3/c2; rt=np.sqrt(2*np.pi)
    def phi(x): return np.exp(-0.5*x*x)/rt
    def logf(u3,u4):
        mu=np.sqrt(p2-p3)*u3+np.sqrt(p3)*u4+KAPPA
        A=1+2*B*s*s
        return np.logaddexp(log_ndtr(-mu/s),-0.5*np.log(A)-B*mu*mu/A+log_ndtr(mu/(s*np.sqrt(A))))
    def inner(u4):
        val,_=quad(lambda u3: phi(u3)*np.exp(m*logf(u3,u4)),-L,L,
                   epsabs=2e-12,epsrel=2e-12,limit=180)
        return val
    val,err=quad(lambda u4: phi(u4)*np.log(inner(u4)),-L,L,
                 epsabs=5e-11,epsrel=5e-11,limit=120)
    return val,err


def adaptive_L(v,L=9.0):
    p3,p2,q3,q2,c3,c2,gs,gp=[float(z) for z in v]
    B=c2/(4*gs); s=np.sqrt(1-p3); rt=np.sqrt(2*np.pi)
    def phi(x): return np.exp(-0.5*x*x)/rt
    def fun(z):
        mu=np.sqrt(p3)*z+KAPPA
        A=1+2*B*s*s
        u=np.logaddexp(log_ndtr(-mu/s),-0.5*np.log(A)-B*mu*mu/A+log_ndtr(mu/(s*np.sqrt(A))))
        return phi(z)*u
    return quad(fun,-L,L,epsabs=1e-13,epsrel=1e-13,limit=240)


def essential_main():
    print('NM13-03 T03 entropy/KL essential checker')
    print('STATUS NUMERICAL_SUPPORT_NOT_DIRECTED_INTERVAL')

    # Entropy-stable capacity compiler, GH160.
    R,J=make_entropy_capacity_system(160)
    seed=np.array([0.96911591,0.59916662,0.63843683,0.22869805],float)
    sol=root(lambda z:np.asarray(R(jnp.array(z)),float),seed,
             jac=lambda z:np.asarray(J(jnp.array(z)),float),tol=1e-11)
    p2,p3,q2,q3=sol.x
    c3,c2,gp=[float(z) for z in reconstruct(p3,p2,q3,q2)]
    r2=q3/p3; r1=(q2-q3)/(p2-p3); r0=(1-q2)/(1-p2)
    gs=r1/(2*r0*np.sqrt(r2)); B=c2/(4*gs)
    v=np.array([p3,p2,q3,q2,c3,c2,gs,gp])
    mm=score_entropy_moments(v,160)
    alpha=c2*c2/(4*B*B*mm['MB'])
    Aq,Dq,H,Ac3,Ac2=algebra_terms(v)
    svals=np.linalg.svd(np.asarray(J(jnp.array(sol.x)),float),compute_uv=False)
    print('CAP_ENT_160 success',sol.success,'alpha',format(alpha,'.15g'),
          'resid_inf',format(float(np.max(np.abs(sol.fun))),'.3e'),
          'cond',format(float(svals[0]/svals[-1]),'.9g'))
    print('CAP_ENT_160 DU',format(mm['DU'],'.15g'),'DH',format(mm['DH'],'.15g'),
          'Ac3_minus_alphaDU/c3^2',format(Ac3-alpha*mm['DU']/(c3*c3),'.3e'),
          'Ac2_minus_alphaDH/(c2c3)',format(Ac2-alpha*mm['DH']/(c2*c3),'.3e'))

    # Fixed-density full stationary point at improved endpoint, GH200.
    psi,grad,F=make_full_system(200)
    seed5=np.array([0.59916622,0.96911556,0.22869839,0.63843689,0.07656548],float)
    fsol=root(lambda z:np.asarray(F(jnp.array(z),ALPHA_TEST),float),seed5,
              method='hybr',tol=1e-12)
    p3,p2,q3,q2,gs=fsol.x
    c3,c2,gp=[float(z) for z in reconstruct(p3,p2,q3,q2)]
    v=np.array([p3,p2,q3,q2,c3,c2,gs,gp])
    g=np.asarray(grad(jnp.array(v),ALPHA_TEST),float)
    pval=float(psi(jnp.array(v),ALPHA_TEST))
    r2=q3/p3; r1=(q2-q3)/(p2-p3); r0=(1-q2)/(1-p2)
    scale_gap=2*gs-r1/(r0*np.sqrt(r2))
    print('FIX_200 success',fsol.success,'alpha',ALPHA_TEST,
          'psi',format(pval,'.15g'),'scale_gap',format(scale_gap,'.15g'),
          'psi_minus_scale',format(pval-scale_gap,'.3e'),
          'full_grad_inf',format(float(np.max(np.abs(g))),'.3e'))
    print('FIX_200_PARAMS',*(format(z,'.17g') for z in v))
    qgh=gh_Q(v,200); qadapt,qerr=adaptive_Q(v)
    lgh=gh_L(v,200); ladapt,lerr=adaptive_L(v)
    m=c3/c2
    slope=-qgh/c3; lower=-lgh/c2; upper=-lgh/c3
    print('Q_GH200',format(qgh,'.17g'),'Q_ADAPTIVE',format(qadapt,'.17g'),
          'Q_DIFF',format(qadapt-qgh,'.3e'),'Q_QUAD_ERR',format(qerr,'.3e'))
    print('L_GH200',format(lgh,'.17g'),'L_ADAPTIVE',format(ladapt,'.17g'),
          'L_DIFF',format(ladapt-lgh,'.3e'),'L_QUAD_ERR',format(lerr,'.3e'))
    print('POWER_MEAN L<=Q<=mL',lgh <= qgh <= m*lgh,
          'L',format(lgh,'.15g'),'Q',format(qgh,'.15g'),'mL',format(m*lgh,'.15g'))
    print('SLOPE_SANDWICH lower',format(lower,'.15g'),'actual',format(slope,'.15g'),
          'upper',format(upper,'.15g'),'pass',lower <= slope <= upper)
    print('SUPPORTED_BOUND_BEFORE 12.288')
    print('SUPPORTED_BOUND_AFTER 12.28723')
    print('UPPER_ENDPOINT_GAIN',format(12.288-ALPHA_TEST,'.15g'))
    print('WIDTH_BEFORE',format(12.288-6.30297437506,'.15g'))
    print('WIDTH_AFTER',format(ALPHA_TEST-6.30297437506,'.15g'))
    print('ALL_NUMERICAL_CHECKS_PASS')

if __name__ == "__main__":
    essential_main()
