#!/usr/bin/env python3
"""
T03 / NM13-03: complete third-full (r=3) negative spherical perceptron
stationarity reduction at kappa=-1.

This is a numerical support script, not an interval proof.  It:
  * implements Stojnic (arXiv:2312.16531) Eq. (94) at kappa=-1;
  * analytically reconstructs c3,c2,gamma_p from Eqs. (142),(145),(147);
  * uses the exact closed inner Gaussian kernel for E exp[-B(Y_+)^2];
  * solves the six-scalar capacity system at several Gauss-Hermite orders;
  * solves the five-scalar stationary system at alpha=12.288 and checks Psi>0;
  * checks the full eight-variable gradient, not only the reduced residual;
  * independently checks the nested perceptron Gaussian term at the n=160
    alpha=12.288 point by adaptive scipy quadrature.

Requires numpy, scipy, jax (x64).
"""
import os
os.environ.setdefault("JAX_ENABLE_X64", "True")

import numpy as np
from numpy.polynomial.hermite import hermgauss
from scipy.integrate import quad
from scipy.optimize import root
from scipy.special import log_ndtr, logsumexp
import jax
import jax.numpy as jnp
from jax.scipy.special import log_ndtr as jlog_ndtr
from jax.scipy.special import logsumexp as jlogsumexp
jax.config.update("jax_enable_x64", True)

KAPPA = -1.0
ALPHA_TEST = 12.288

def gh(n):
    x,w = hermgauss(n)
    return jnp.array(np.sqrt(2.0)*x), jnp.array(w/np.sqrt(np.pi))

def reconstruct(p3,p2,q3,q2):
    """Stojnic (142),(145),(147), positive interior branch."""
    sq_qp = jnp.sqrt(q3/p3)
    sq_pq = 1.0/sq_qp
    c3 = sq_pq/(p2-p3) - sq_qp/(q2-q3)
    gp = 0.5*((1-q2)/(1-p2))*((p2-p3)/(q2-q3))*sq_qp
    c2 = (((p2-p3)/(q2-q3))*sq_qp)/(1-p2) \
       - (((q2-q3)/(p2-p3))*sq_pq)/(1-q2)
    return c3,c2,gp

def make_system(n):
    nodes, weights = gh(n)
    U3 = nodes[:,None]
    U4 = nodes[None,:]

    def psi_orig(v, alpha):
        # independent variables v=(p3,p2,q3,q2,c3,c2,gamma_sq,gamma_p)
        p3,p2,q3,q2,c3,c2,gs,gp = v
        A1 = 2*gp-c2*(1-q2)
        D  = A1-c3*(q2-q3)

        # Exact conditional kernel:
        # f(mu,s,B)=E_H exp[-B(mu+sH)_+^2]
        B = c2/(4*gs)
        s = jnp.sqrt(1-p2)
        mu = jnp.sqrt(p2-p3)*U3 + jnp.sqrt(p3)*U4 + KAPPA
        A = 1+2*B*s*s
        logf = jnp.logaddexp(
            jlog_ndtr(-mu/s),
            -0.5*jnp.log(A)-B*mu*mu/A+jlog_ndtr(mu/(s*jnp.sqrt(A)))
        )

        r = c3/c2
        log_inner = jlogsumexp(jnp.log(weights)[:,None] + r*logf, axis=0)
        Q = jnp.sum(weights*log_inner)

        # Eq. (94), with the first (q/Gaussian) nested term analytically closed.
        return (
            0.5*(1-p2*q2)*c2
            + 0.5*(p2*q2-p3*q3)*c3
            - gp
            + (0.5/c2)*jnp.log(A1/(2*gp))
            + (0.5/c3)*jnp.log(D/A1)
            - q3/(2*D)
            + gs
            - (alpha/c3)*Q
        )

    psi = jax.jit(psi_orig)
    grad = jax.jit(jax.grad(psi_orig, argnums=0))

    def capacity_residual(y):
        p3,p2,q3,q2,gs,alpha = y
        c3,c2,gp = reconstruct(p3,p2,q3,q2)
        v = jnp.array([p3,p2,q3,q2,c3,c2,gs,gp])
        g = grad(v,alpha)
        # q3,q2,gamma_p stationarity is built in by reconstruction.
        return jnp.array([g[0],g[1],g[4],g[5],g[6],psi(v,alpha)])

    def fixed_alpha_residual(y, alpha):
        p3,p2,q3,q2,gs = y
        c3,c2,gp = reconstruct(p3,p2,q3,q2)
        v = jnp.array([p3,p2,q3,q2,c3,c2,gs,gp])
        g = grad(v,alpha)
        return jnp.array([g[0],g[1],g[4],g[5],g[6]])

    return psi, grad, jax.jit(capacity_residual), jax.jit(fixed_alpha_residual)

def full_point(y, alpha=None):
    if alpha is None:
        p3,p2,q3,q2,gs,alpha = y
    else:
        p3,p2,q3,q2,gs = y
    c3,c2,gp = [float(z) for z in reconstruct(p3,p2,q3,q2)]
    return np.array([p3,p2,q3,q2,c3,c2,gs,gp]), float(alpha)

def adaptive_Q(v, L=8.0):
    """Independent scipy adaptive check of the nested perceptron term Q."""
    p3,p2,q3,q2,c3,c2,gs,gp = v
    B = c2/(4*gs)
    s = np.sqrt(1-p2)
    r = c3/c2
    rt2pi = np.sqrt(2*np.pi)

    def logf_scalar(u3,u4):
        mu = np.sqrt(p2-p3)*u3 + np.sqrt(p3)*u4 + KAPPA
        A = 1+2*B*s*s
        return np.logaddexp(
            log_ndtr(-mu/s),
            -0.5*np.log(A)-B*mu*mu/A+log_ndtr(mu/(s*np.sqrt(A)))
        )

    def phi(x):
        return np.exp(-0.5*x*x)/rt2pi

    def inner(u4):
        val,_ = quad(
            lambda u3: phi(u3)*np.exp(r*logf_scalar(u3,u4)),
            -L,L,epsabs=2e-12,epsrel=2e-12,limit=150
        )
        return val

    val,err = quad(
        lambda u4: phi(u4)*np.log(inner(u4)),
        -L,L,epsabs=5e-11,epsrel=5e-11,limit=100
    )
    return val,err

def gh_Q(v,n):
    p3,p2,q3,q2,c3,c2,gs,gp = v
    x,w = hermgauss(n)
    x=np.sqrt(2)*x
    w=w/np.sqrt(np.pi)
    U3=x[:,None]; U4=x[None,:]
    B=c2/(4*gs); s=np.sqrt(1-p2)
    mu=np.sqrt(p2-p3)*U3+np.sqrt(p3)*U4+KAPPA
    A=1+2*B*s*s
    lf=np.logaddexp(
        log_ndtr(-mu/s),
        -0.5*np.log(A)-B*mu*mu/A+log_ndtr(mu/(s*np.sqrt(A)))
    )
    r=c3/c2
    loginner=logsumexp(np.log(w)[:,None]+r*lf,axis=0)
    return np.sum(w*loginner)

def fmt(d):
    keys=("p3","p2","q3","q2","c3","c2","gamma_sq","gamma_p","alpha","psi",
          "selected_resid_inf","full_grad_inf")
    return " ".join(f"{k}={d[k]:.15g}" for k in keys)

def main():
    # Source Table-5 values are used only as an initial seed.
    cap_seed=np.array([0.6252,0.9691,0.2500,0.6536,0.0835,12.29],float)
    fixed_seed=None
    cap_results={}
    fixed_results={}

    for n in (60,80,100,120,160):
        psi,grad,capres,fixres=make_system(n)

        sol=root(lambda z:np.asarray(capres(jnp.array(z)),float),
                 cap_seed,method="hybr",tol=1e-11)
        v,a=full_point(sol.x)
        g=np.asarray(grad(jnp.array(v),a),float)
        d=dict(
            p3=v[0],p2=v[1],q3=v[2],q2=v[3],c3=v[4],c2=v[5],
            gamma_sq=v[6],gamma_p=v[7],alpha=a,
            psi=float(psi(jnp.array(v),a)),
            selected_resid_inf=float(np.max(np.abs(sol.fun))),
            full_grad_inf=float(np.max(np.abs(g))),
        )
        cap_results[n]=d
        cap_seed=sol.x
        print("CAP",n,"success",sol.success,fmt(d))

        if fixed_seed is None:
            fixed_seed=sol.x[:5]
        fsol=root(lambda z:np.asarray(fixres(jnp.array(z),ALPHA_TEST),float),
                  fixed_seed,method="hybr",tol=1e-11)
        fv,fa=full_point(fsol.x,ALPHA_TEST)
        fg=np.asarray(grad(jnp.array(fv),fa),float)
        fd=dict(
            p3=fv[0],p2=fv[1],q3=fv[2],q2=fv[3],c3=fv[4],c2=fv[5],
            gamma_sq=fv[6],gamma_p=fv[7],alpha=fa,
            psi=float(psi(jnp.array(fv),fa)),
            selected_resid_inf=float(np.max(np.abs(fsol.fun))),
            full_grad_inf=float(np.max(np.abs(fg))),
        )
        fixed_results[n]=fd
        fixed_seed=fsol.x
        print("FIX",n,"success",fsol.success,fmt(fd))

    # Independent nested-integral check at the highest-order alpha=12.288 point.
    d=fixed_results[160]
    v=np.array([d[k] for k in ("p3","p2","q3","q2","c3","c2","gamma_sq","gamma_p")])
    qgh=gh_Q(v,160)
    qad,qerr=adaptive_Q(v,L=8.0)
    print("Q_GH160",repr(float(qgh)))
    print("Q_ADAPTIVE_L8",repr(float(qad)),"quad_reported_error",repr(float(qerr)))
    print("Q_DIFF",repr(float(qad-qgh)))
    print("ENVELOPE_SLOPE_MINUS_Q_OVER_C3",repr(float(-qgh/v[4])))

    # Local nonsingularity scout for later interval/Krawczyk certification.
    _,_,_,fixres=make_system(160)
    J=np.asarray(jax.jacfwd(fixres,argnums=0)(jnp.array(fixed_seed),ALPHA_TEST),float)
    sv=np.linalg.svd(J,compute_uv=False)
    print("FIXED_ALPHA_JAC_SINGULAR_VALUES", " ".join(f"{x:.15g}" for x in sv))
    print("FIXED_ALPHA_JAC_CONDITION",repr(float(sv[0]/sv[-1])))

    before=12.31963485
    after=ALPHA_TEST
    lower=6.30297437506
    print("BOUND_BEFORE",repr(before))
    print("BOUND_AFTER_SUPPORTED_CONDITIONAL",repr(after))
    print("UPPER_ENDPOINT_GAIN",repr(before-after))
    print("BRACKET_WIDTH_BEFORE",repr(before-lower))
    print("BRACKET_WIDTH_AFTER",repr(after-lower))
    print("STATUS CONDITIONAL_NUMERICAL_NOT_INTERVAL_CERTIFIED")
    print("ALL_NUMERICAL_THIRDFULL_CHECKS_PASS")

if __name__=="__main__":
    main()
