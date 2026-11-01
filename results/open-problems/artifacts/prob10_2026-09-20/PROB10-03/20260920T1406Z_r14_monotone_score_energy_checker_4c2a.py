#!/usr/bin/env python3
"""
PROB10-03 R14 monotone score/energy outer-compiler checker.

Exact theorem is proved in the accompanying report/idea note.
This script provides:
  * an exact algebra check for the right-tail polynomial;
  * broad numerical falsification of monotonicity/envelopes;
  * a numerical check of the exact lambda-sensitivity identity;
  * a numerical candidate outer-mesh bracket.
No numerical output is a directed source endpoint.
"""
import math
import numpy as np
import sympy as sp
from numpy.polynomial.hermite import hermgauss
from scipy.special import log_ndtr, logsumexp, ndtr

LOGPHI0=-0.5*math.log(2*math.pi)

def phi(x):
    return math.exp(-0.5*x*x)/math.sqrt(2*math.pi)

# --- exact algebraic tail identity from Gaussian moment formulas ---
b,g,s,R,ph,Q=sp.symbols("b g s R ph Q", positive=True)
expr = b*b*(R*ph+Q)-2*b*g*ph+(g*g+s*s)*Q
expanded = sp.expand(
    b*b*(R*ph+Q) - 2*b*g*ph + (g*g+s*s)*Q
)
assert sp.simplify(expr-expanded)==0
print("EXACT_RIGHT_TAIL_POLYNOMIAL_PASS")

def gh(n):
    z,w=hermgauss(n)
    return np.sqrt(2.0)*z, w/np.sqrt(np.pi)

def closed_vals(t,r):
    """u(t), u_t(t), h(t)=E_rho (t+H)_+^2 for r=1+lambda."""
    t=np.asarray(t,float)
    b=t/np.sqrt(r)
    logB=log_ndtr(-t)
    logA=-0.5*np.log(r)-(r-1)*t*t/(2*r)+log_ndtr(b)
    logF=np.logaddexp(logB,logA)
    fracB=np.exp(logB-logF)
    fracA=np.exp(logA-logF)

    mills_minus=np.exp(LOGPHI0-0.5*t*t-log_ndtr(-t))
    dlogB=-mills_minus
    mills_b=np.exp(LOGPHI0-0.5*b*b-log_ndtr(b))
    dlogA=-(r-1)*t/r+mills_b/np.sqrt(r)
    ut=fracB*dlogB+fracA*dlogA

    h=fracA*(1/r+t*t/r**2+t*mills_b/(r**1.5))
    return logF,ut,h

def cond(a,d,m,r,n=140):
    U,wu=gh(n)
    T=a+d*U
    u,ut,h=closed_vals(T,r)
    lw=np.log(wu)+m*u
    z=logsumexp(lw)
    tw=np.exp(lw-z)
    mu=float(np.dot(tw,ut))
    return np.array([mu*mu,
                     float(np.dot(tw,ut*ut)),
                     float(np.dot(tw,h))])

def Tplus2(a,s):
    z=a/s
    return (a*a+s*s)*ndtr(z)+a*s*phi(z)

# broad numerical falsification over strict-domain tuples
rng=np.random.default_rng(20260920)
worst=np.full(3,np.inf)
max_ratio=np.zeros(3)
for _ in range(16):
    d=10**rng.uniform(-0.45,0.65)
    m=rng.uniform(0.07,0.9)
    r=1+10**rng.uniform(-0.5,0.8)
    lam=r-1
    aa=np.linspace(-5.5,5.5,67)
    vals=np.array([cond(a,d,m,r,120) for a in aa])
    worst=np.minimum(worst,np.min(np.diff(vals,axis=0),axis=0))
    env=np.array([Tplus2(a,math.sqrt(1+d*d)) for a in aa])
    den=np.column_stack([lam*lam*env,lam*lam*env,env])
    max_ratio=np.maximum(max_ratio,np.max(vals/(den+1e-300),axis=0))
print("NUMERICAL_ONLY_BROAD_MONOTONE_MIN_INCREMENTS",
      *(format(float(x),".12g") for x in worst))
print("NUMERICAL_ONLY_BROAD_ENVELOPE_MAX_RATIOS",
      *(format(float(x),".12g") for x in max_ratio))
assert np.min(worst) > -2e-8
assert np.max(max_ratio) < 1+2e-8
print("NUMERICAL_ONLY_BROAD_FALSIFICATION_PASS")

# inherited third-full numerical point
w0=0.030884087534487
w1=0.369949296921514
w2=0.599166615543999
r=3.64279338727087
lam=r-1
m=0.218827592829088
d=math.sqrt(w1/w0)
beta=math.sqrt(w2/w0)
gamma=1/math.sqrt(w0)

vv=np.linspace(-6,6,121)
vals=np.array([cond(beta*v-gamma,d,m,r,160) for v in vv])
mind=np.min(np.diff(vals,axis=0),axis=0)
env=np.array([Tplus2(beta*v-gamma,math.sqrt(1+d*d)) for v in vv])
rat=np.max(vals/(
    np.column_stack([lam*lam*env,lam*lam*env,env])+1e-300),axis=0)
print("NUMERICAL_ONLY_CANDIDATE_MONOTONE_MIN_INCREMENTS",
      *(format(float(x),".12g") for x in mind))
print("NUMERICAL_ONLY_CANDIDATE_ENVELOPE_MAX_RATIOS",
      *(format(float(x),".12g") for x in rat))
assert np.min(mind) >= -2e-10
assert np.max(rat) < 1+2e-10

# direct inner variance for lambda-sensitivity identity
def inner_varY2(t,lam,n=140):
    H,wh=gh(n)
    lwh=np.log(wh)
    t=np.atleast_1d(t)
    hs=[]; vs=[]
    for tt in t:
        P=np.maximum(tt+H,0)
        lw=lwh-0.5*lam*P*P
        z=logsumexp(lw)
        tw=np.exp(lw-z)
        Y2=P*P
        hh=float(np.dot(tw,Y2))
        hs.append(hh)
        vs.append(float(np.dot(tw,(Y2-hh)**2)))
    return np.array(hs),np.array(vs)

def lambda_rhs(a,d,m,r,nU=90,nH=140):
    U,wu=gh(nU)
    T=a+d*U
    u,ut,h=closed_vals(T,r)
    lw=np.log(wu)+m*u
    z=logsumexp(lw)
    tw=np.exp(lw-z)
    _,varY2=inner_varY2(T,r-1,nH)
    Eh=float(np.dot(tw,h))
    return (-0.5*float(np.dot(tw,varY2))
            -0.5*m*float(np.dot(tw,(h-Eh)**2)))

errs=[]
rhsvals=[]
for a in (-8.0,-5.0,-2.0,0.0,2.0):
    eps=1e-4
    fd=(cond(a,d,m,r+eps,160)[2]-cond(a,d,m,r-eps,160)[2])/(2*eps)
    rhs=lambda_rhs(a,d,m,r)
    errs.append(abs(fd-rhs))
    rhsvals.append(rhs)
print("NUMERICAL_ONLY_LAMBDA_AH_RHS",
      *(format(float(x),".12g") for x in rhsvals))
print("NUMERICAL_ONLY_LAMBDA_IDENTITY_MAX_ABS_ERROR",
      format(float(max(errs)),".12g"))
assert max(rhsvals) < 0
assert max(errs) < 2e-5
print("NUMERICAL_ONLY_LAMBDA_SENSITIVITY_PASS")

# candidate outer Gaussian integral and monotone endpoint bracket
def direct_outer(nV=180):
    V,wv=gh(nV)
    arr=np.array([cond(beta*v-gamma,d,m,r,160) for v in V])
    return np.dot(wv,arr)

def tail_poly(R):
    Q=ndtr(-R)
    ph=phi(R)
    ss=math.sqrt(1+d*d)
    return (beta*beta*(R*ph+Q)-2*beta*gamma*ph
            +(gamma*gamma+ss*ss)*Q)

def bracket(L=-6.0,R=6.0,step=0.10):
    grid=np.arange(L,R+0.5*step,step)
    A=np.array([cond(beta*v-gamma,d,m,r,140) for v in grid])
    prob=ndtr(grid[1:])-ndtr(grid[:-1])
    lower=np.sum(prob[:,None]*A[:-1],axis=0)
    upper=np.sum(prob[:,None]*A[1:],axis=0)
    # monotonicity gives a right-tail lower contribution
    lower=lower+ndtr(-R)*A[-1]
    left=ndtr(L)*A[0]
    mult=np.array([lam*lam,lam*lam,1.0])
    upper=upper+left+mult*tail_poly(R)
    return lower,upper

direct=direct_outer()
lo,up=bracket()
print("NUMERICAL_ONLY_CANDIDATE_DIRECT_S1_S2_H1",
      *(format(float(x),".12g") for x in direct))
print("NUMERICAL_ONLY_MONOTONE_MESH_LOWER",
      *(format(float(x),".12g") for x in lo))
print("NUMERICAL_ONLY_MONOTONE_MESH_UPPER",
      *(format(float(x),".12g") for x in up))
print("NUMERICAL_ONLY_MONOTONE_MESH_WIDTH",
      *(format(float(x),".12g") for x in (up-lo)))
assert np.all(direct >= lo-2e-7)
assert np.all(direct <= up+2e-7)
print("NUMERICAL_ONLY_MONOTONE_MESH_BRACKET_PASS")
print("ALL_SELF_CHECKS_PASS")
