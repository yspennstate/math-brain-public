#!/usr/bin/env python3
"""
R14 recovery-1 artifact.
Part A is an exact-rational checker for C189 (objective-tail compactification).
Part B is explicitly NUMERICAL_ONLY: it scouts a preconditioned Poincare-Miranda/Krawczyk box
for the complete r=2 sfl stationary equations at kappa=-1, alpha=12.5.
"""
from fractions import Fraction as Q
import math
import numpy as np

print("R14 recovery-1: exact C189 + NUMERICAL_ONLY preconditioned-root scout")

# ---------- PART A: EXACT C189 ----------
pL,pU=Q(3281,5000),Q(1641,2500)       # [0.6562,0.6564]
DL,DU=Q(261,400),Q(408,625)            # [0.6525,0.6528]
gL,gU=Q(1587,10000),Q(1591,10000)      # [0.1587,0.1591]

# c = 1/(D(1-p)) - D/(1-p D^2)
# coarse interval bounds sufficient for tail compactification
cL=1/(DU*(1-pL))-DU/(1-pU*DU*DU)
cU=1/(DL*(1-pU))
assert cL>0

# B=c/(4 gamma), A=1+2B(1-p)
BU=cU/(4*gL)
AU=1+2*BU*(1-pL)
assert AU < 6

# B/A < 1/[2(1-p)] <= 1/[2(1-pU)] < 3/2.
assert 1/(2*(1-pU)) < Q(3,2)

# For z>=9, sqrt(p)>=0.81 and sqrt(p)<=0.811 are certified by squaring.
assert Q(81,100)**2 < pL
assert Q(811,1000)**2 > pU
assert Q(81,100)*9-1 > 0

# Hence mu^2 <= (0.811 z)^2 and (B/A)mu^2 <= z^2.
coef=Q(3,2)*Q(811,1000)**2
assert coef < 1

# log(2 sqrt(6)) < 2: e > 1+1+1/2+1/6+1/24 = 65/24 > 27/10,
# and (27/10)^4 > 24 = (2 sqrt 6)^2.
elow=Q(65,24)
assert elow > Q(27,10)
assert Q(27,10)**4 > 24

# Gaussian tail:
# Qbar(9) < phi(9)/9 and phi(9)<e^-40<(10/27)^40.
# Therefore E[-log f(Z); |Z|>9] < 4 Qbar(9)+9 phi(9)
# < (85/9) phi(9) < (85/9)(10/27)^40 < 1e-16.
tail_bound=Q(85,9)*Q(10,27)**40
assert tail_bound < Q(1,10**16)

print("EXACT_C189_PASS")
print("  p-box =", float(pL), float(pU))
print("  D-box =", float(DL), float(DU))
print("  gamma-box =", float(gL), float(gU))
print("  c coarse lower/upper =", float(cL), float(cU))
print("  B upper =", float(BU), "A upper =", float(AU))
print("  quadratic coefficient upper =", float(coef))
print("  certified objective Gaussian-tail bound <", float(tail_bound), "< 1e-16")

# ---------- PART B: NUMERICAL ONLY ----------
print("NUMERICAL_ONLY_BEGIN")
try:
    import jax
    import jax.numpy as jnp
    from numpy.polynomial.hermite import hermgauss
    from scipy.optimize import root
    jax.config.update("jax_enable_x64", True)

    def make_obj(nh):
        hn,hw=hermgauss(nh)
        zn=jnp.array(hn*math.sqrt(2.0))
        ww=jnp.array(hw/math.sqrt(math.pi))
        def Phi(x):
            return 0.5*(1+jax.scipy.special.erf(x/jnp.sqrt(2.0)))
        def F(x,alpha=12.5):
            p,D,g=x
            q=p*D**2
            gp=(1-q)/(2*D*(1-p))
            c=1/(D*(1-p))-D/(1-q)
            mu=jnp.sqrt(p)*zn-1
            sig=jnp.sqrt(1-p)
            B=c/(4*g)
            A=1+2*B*sig**2
            ff=Phi(-mu/sig)+jnp.exp(-B*mu**2/A)/jnp.sqrt(A)*Phi(mu/(sig*jnp.sqrt(A)))
            E=jnp.sum(ww*jnp.log(ff))
            return .5*(1-p*q)*c-gp+(1/(2*c))*jnp.log(D/(2*gp))-q/(2*D)+g-(alpha/c)*E
        return jax.jit(F),jax.jit(jax.grad(F)),jax.jit(jax.hessian(F))

    xinit=np.array([0.6563131896141976,
                    math.sqrt(0.2795610890313501/0.6563131896141976),
                    0.15886185238049177])
    records=[]
    for nh in (64,80,96,120):
        F,G,H=make_obj(nh)
        rr=root(lambda x:np.asarray(G(jnp.array(x))),xinit,tol=1e-12)
        assert rr.success
        x=rr.x
        h=np.asarray(H(jnp.array(x)))
        assert np.all(np.isfinite(h))
        records.append((nh,x.copy(),float(F(jnp.array(x))),
                        float(np.linalg.norm(np.asarray(G(jnp.array(x))),np.inf))))
        xinit=x
    for nh,x,v,res in records:
        print("  GH",nh,"x=",repr(x),"F=",repr(v),"grad_inf=",repr(res))

    F,G,H=make_obj(120)
    x0=records[-1][1]
    H0=np.asarray(H(jnp.array(x0)))
    M=np.linalg.inv(H0)
    print("  H0=",repr(H0))
    print("  eig(H0)=",repr(np.linalg.eigvalsh(H0)))
    print("  det(H0)=",repr(float(np.linalg.det(H0))),"cond2=",repr(float(np.linalg.cond(H0))))
    print("  M=H0^-1=",repr(M))

    r=1e-4
    theta=0.0
    for da in np.linspace(-r,r,7):
        for db in np.linspace(-r,r,7):
            for dg in np.linspace(-r,r,7):
                x=x0+np.array([da,db,dg])
                E=np.eye(3)-M@np.asarray(H(jnp.array(x)))
                theta=max(theta,float(np.linalg.norm(E,np.inf)))
    print("  sampled_7cube_sup_norm_I_minus_MH =",repr(theta))

    for i in range(3):
        inds=[j for j in range(3) if j!=i]
        for sign in (-1,1):
            vals=[]
            for a in np.linspace(-r,r,21):
                for b in np.linspace(-r,r,21):
                    d=np.zeros(3); d[i]=sign*r; d[inds[0]]=a; d[inds[1]]=b
                    vals.append(float((M@np.asarray(G(jnp.array(x0+d))))[i]))
            print("  preconditioned_face",i,sign,min(vals),max(vals))
except Exception as e:
    print("  NUMERICAL_SCOUT_FAILED:",repr(e))
    raise
print("NUMERICAL_ONLY_END")
