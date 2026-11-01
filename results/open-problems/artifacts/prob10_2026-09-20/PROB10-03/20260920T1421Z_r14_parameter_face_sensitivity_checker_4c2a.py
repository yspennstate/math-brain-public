#!/usr/bin/env python3
"""Numerical falsification/checker for the exact parameter-face identities
proved in the matching PROB10-03 report. Numerical outputs are NOT source
endpoints or directed interval certificates."""
import math
import numpy as np
from numpy.polynomial.hermite import hermgauss
from scipy.special import log_ndtr, logsumexp

LOGPHI0=-0.5*math.log(2*math.pi)
def gh(n):
    z,w=hermgauss(n); return np.sqrt(2.0)*z,w/np.sqrt(np.pi)

def closed(t,r):
    # lambda=r-1, exponent -lambda (t+H)_+^2/2
    t=np.asarray(t,float); b=t/np.sqrt(r)
    logB=log_ndtr(-t)
    logA=-0.5*np.log(r)-(r-1)*t*t/(2*r)+log_ndtr(b)
    logF=np.logaddexp(logB,logA)
    fracA=np.exp(logA-logF); fracB=np.exp(logB-logF)
    mm=np.exp(LOGPHI0-0.5*t*t-log_ndtr(-t))
    mb=np.exp(LOGPHI0-0.5*b*b-log_ndtr(b))
    ut=fracB*(-mm)+fracA*(-(r-1)*t/r+mb/np.sqrt(r))
    h=fracA*(1/r+t*t/r**2+t*mb/(r**1.5))
    K=-(r-1)*h/2-logF
    return logF,ut,h,K

def vals(a,d,m,r,n=180):
    U,w=gh(n); T=a+d*U
    u,ut,h,K=closed(T,r)
    lw=np.log(w)+m*u; z=logsumexp(lw); tw=np.exp(lw-z)
    g=float(tw@ut)
    DU=m*float(tw@u)-z
    DH=m*float(tw@K)
    return np.array([g*g,float(tw@(ut*ut)),float(tw@h),DU,DH])

def fd(fun,x,h): return (fun(x+h)-fun(x-h))/(2*h)

# Candidate-region sign table: a derivatives should be >=0 for all five;
# m derivatives A1,A2,AH <=0 and DU >=0; lambda derivative AH<=0, DU>=0.
w0=0.030884087534487; w1=0.369949296921514; w2=0.599166615543999
r=3.64279338727087; m=0.218827592829088; d=math.sqrt(w1/w0)
beta=math.sqrt(w2/w0); gamma=1/math.sqrt(w0)
for a in (-5.0,-2.0,0.0,2.0):
    da=fd(lambda z: vals(z,d,m,r,180),a,1e-5)
    dm=fd(lambda z: vals(a,d,z,r,180),m,1e-5)
    dr=fd(lambda z: vals(a,d,m,z,180),r,1e-5)
    print("CANDIDATE_DERIV",a,
          "DA",*(f"{q:.12g}" for q in da),
          "DM",*(f"{q:.12g}" for q in dm),
          "DLAMBDA",*(f"{q:.12g}" for q in dr))
    assert np.min(da) > -2e-7
    assert np.max(dm[:3]) < 2e-7 and dm[3] > -2e-7
    assert dr[2] < 2e-7 and dr[3] > -2e-7
print("NUMERICAL_ONLY_CANDIDATE_SIGN_TABLE_PASS")

# Negation test: D_H is NOT globally monotone in m. Two stable tuples give
# opposite finite-difference signs, so no universal m-corner rule may be used.
examples=[
 ("POS",5.661023429588642,0.41346355478050834,0.30649045981821843,2.0653736378264775),
 ("NEG",5.874676075747857,2.0492681702431534,0.7471944978935743,5.409842344742469),
]
for label,a,d0,m0,r0 in examples:
    signs=[]
    for n in (100,140,180,220):
        deriv=fd(lambda z: vals(a,d0,z,r0,n)[4],m0,2e-5)
        signs.append(deriv)
    print("NUMERICAL_ONLY_DH_M_SIGN",label,*(f"{q:.12g}" for q in signs))
    if label=="POS": assert min(signs)>3.9
    else: assert max(signs)<-0.19
print("NUMERICAL_ONLY_DH_M_NONMONOTONE_OBSTRUCTION_PASS")

# Exact AH_lambda identity is checked by finite differences against
# -1/2 E Var_rho(Y_+^2) - m/2 Var_nu(h).
def inner_h_var(t,lam,n=160):
    H,w=gh(n); lw0=np.log(w); hs=[]; vs=[]
    for tt in np.atleast_1d(t):
        Y=np.maximum(tt+H,0.0); Y2=Y*Y
        lw=lw0-0.5*lam*Y2; z=logsumexp(lw); tw=np.exp(lw-z)
        h=float(tw@Y2); hs.append(h); vs.append(float(tw@(Y2-h)**2))
    return np.array(hs),np.array(vs)

def AH_lambda_rhs(a,d,m,r,nU=100,nH=160):
    U,w=gh(nU); T=a+d*U
    u,ut,h,K=closed(T,r)
    lw=np.log(w)+m*u; z=logsumexp(lw); tw=np.exp(lw-z)
    _,vY=inner_h_var(T,r-1,nH)
    Eh=float(tw@h)
    return -0.5*float(tw@vY)-0.5*m*float(tw@((h-Eh)**2))
errs=[]
for a in (-5.0,-2.0,0.0,2.0):
    num=fd(lambda rr: vals(a,d,m,rr,180)[2],r,1e-4)
    rhs=AH_lambda_rhs(a,d,m,r)
    errs.append(abs(num-rhs))
    print("NUMERICAL_ONLY_AH_LAMBDA",a,f"FD {num:.12g}",f"RHS {rhs:.12g}")
    assert rhs < 0
print("NUMERICAL_ONLY_AH_LAMBDA_MAX_ERROR",f"{max(errs):.12g}")
assert max(errs)<2e-5
print("NUMERICAL_ONLY_AH_LAMBDA_IDENTITY_PASS")
print("ALL_PARAMETER_FACE_SELF_CHECKS_PASS")
