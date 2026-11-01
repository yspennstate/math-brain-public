#!/usr/bin/env python3
"""NM13-07 / T03, 2026-09-20.

Exact part:
  * one final source-bookkeeping microstep inside the already certified
    complete-second continuation band, from 12.319634446193 to
    12.319634446191, using only inherited exact rational data.

Numerical-only part:
  * tests the new scalar-partition / Bregman compiler for the complete-third
    prescribed-positive-gap system at delta=1e-3;
  * verifies that all five moments S1,S2,H1,DU,DH can be recovered/enclosed
    from scalar nested free-energy values Q by secants in outer variance,
    inner variance, b and m;
  * checks the transformed total-Bregman residual crosses robustly at the
    x-branch endpoints of the prior pivoted-Schur scout;
  * demonstrates O(h^2)-type chord/tangent scalar-Q enclosure numerically.

All quadrature/CDF calculations in the numerical section are ordinary double
precision and are NUMERICAL_ONLY, not directed interval proof claims.
"""
from fractions import Fraction as F
import math
import numpy as np
from numpy.polynomial.hermite import hermgauss
from scipy.special import log_ndtr, logsumexp, ndtr
from scipy.optimize import root

# ---------------------------------------------------------------------------
# Exact source bookkeeping microstep inside inherited certified band
# ---------------------------------------------------------------------------
alphaL = F(315148718753, 50_000_000_000)              # 6.30297437506
alpha0 = F(12319635, 1_000_000)                       # 12.319635
alpha_before = F(12319634446193, 1_000_000_000_000)   # 12.319634446193
alpha_after  = F(12319634446191, 1_000_000_000_000)   # 12.319634446191
assert alpha_before-alpha_after == F(1,500_000_000_000)
dec_lo = F(446,1_000_000_000)
dec_hi = F(554,1_000_000_000)
delta_new = alpha0-alpha_after
assert dec_lo <= delta_new <= dec_hi
slope = F(4136629,105883920)
psi0 = F(23584189005311,1090044380000000000000)
psi_new = psi0-slope*delta_new
assert psi_new > 0
print('EXACT_SOURCE_MICROSTEP')
print('ALPHA_BEFORE', float(alpha_before))
print('ALPHA_AFTER', float(alpha_after))
print('SOURCE_GAIN', alpha_before-alpha_after, float(alpha_before-alpha_after))
print('DELTA_FROM_ANCHOR', delta_new, float(delta_new))
print('PSI_AFTER_LOWER', psi_new, float(psi_new))
print('WIDTH_BEFORE', float(alpha_before-alphaL))
print('WIDTH_AFTER', float(alpha_after-alphaL))
print('EXACT_SOURCE_MICROSTEP_PASS')

# ---------------------------------------------------------------------------
# Numerical-only complete-third scalar free energy and direct moments
# ---------------------------------------------------------------------------
DEL=1e-3
GH={}
def gh(n):
    if n not in GH:
        z,w=hermgauss(n)
        GH[n]=(np.sqrt(2)*z,w/np.sqrt(np.pi))
    return GH[n]

def geom(v):
    w0,w1,x,m=map(float,v); w2=1-w0-w1
    y=1+m*(x-1)*w1/(x*w0)
    Z=x*y*y*w0+y*w1+w2
    S=math.sqrt(Z)/(x*y); lam=S/(S+DEL); xi=1+lam*(x-1)
    return w2,y,Z,S,lam,xi

def inner_closed(t,b,s=1.0):
    """P_s exp[-b (z_+)^2](t), plus moments for s=1 direct checks."""
    t=np.asarray(t,float)
    den=1+2*b*s
    l1=log_ndtr(-t/math.sqrt(s))
    l2=-0.5*math.log(den)-b*t*t/den+log_ndtr(t/math.sqrt(s*den))
    U=np.logaddexp(l1,l2)
    return U

def kernel_moments_s1(t,xi):
    """Closed U, U_t and inner positive-part moment for s=1."""
    t=np.asarray(t,float)
    l1=log_ndtr(-t)
    z=t/math.sqrt(xi)
    l2=-.5*math.log(xi)-(xi-1)*t*t/(2*xi)+log_ndtr(z)
    U=np.logaddexp(l1,l2)
    f2=np.exp(l2-U)
    phF=np.exp(-.5*t*t-.5*math.log(2*math.pi)-U)
    mu1=(t*f2+phF)/xi
    mu2=(t*mu1+f2)/xi
    Ut=-(xi-1)*mu1
    K=-(xi-1)*.5*mu2-U
    return U,Ut,mu2,K

def scalar_Q_params(tau,rho,s,m,b,c,n=160):
    Uq,wu=gh(n); Vq,wv=gh(n)
    T=c+math.sqrt(tau)*Uq[None,:]+math.sqrt(rho)*Vq[:,None]
    U=inner_closed(T,b,s)
    l=np.log(wu)[None,:]+m*U
    qv=logsumexp(l,axis=1)
    return float(np.dot(wv,qv))

def scalar_Q(v,n=160, *, tau=None,rho=None,s=1.0,m=None,b=None):
    w0,w1,x,m0=map(float,v); w2,y,Z,S,lam,xi=geom(v)
    if tau is None: tau=w1/w0
    if rho is None: rho=w2/w0
    if m is None: m=m0
    if b is None: b=(xi-1)/2
    c=-1/math.sqrt(w0)
    return scalar_Q_params(tau,rho,s,m,b,c,n)

def direct_moments(v,n=160):
    w0,w1,x,m=map(float,v); w2,y,Z,S,lam,xi=geom(v)
    Uq,wu=gh(n); Vq,wv=gh(n)
    T=np.sqrt(w1/w0)*Uq[None,:]+np.sqrt(w2/w0)*Vq[:,None]-1/np.sqrt(w0)
    U,Ut,H,K=kernel_moments_s1(T,xi)
    lt=np.log(wu)[None,:]+m*U
    lz=logsumexp(lt,axis=1)
    tw=np.exp(lt-lz[:,None])
    g=np.sum(tw*Ut,axis=1)
    vals=np.column_stack((
        g*g,
        np.sum(tw*Ut*Ut,axis=1),
        np.sum(tw*H,axis=1),
        m*np.sum(tw*U,axis=1)-lz,
        m*np.sum(tw*K,axis=1)))
    return np.dot(wv,vals)

def kfun(y): return y*(y*math.log(y)-y+1)/(y-1)**2
def hfun(x): return x*(x-1-math.log(x))/(x-1)**2

def targets(v,n=160):
    w0,w1,x,m=map(float,v); w2,y,Z,S,lam,xi=geom(v)
    S1,S2,H1,DU,DH=direct_moments(v,n)
    CU=x*x*w0*(y-1)**2*S1*(w2+w1*kfun(y))/(2*w1*w2*(x-1)**2)
    CH=x*(y-1)*w0*S1*(Z-x*y*y*w0*hfun(x))/(2*w1*w2*(x-1))
    return CU,CH

def residual(v,n=160):
    w0,w1,x,m=map(float,v); w2,y,Z,S,lam,xi=geom(v)
    if min(w0,w1,w2)<=0 or x<=1 or not(0<m<1): return np.ones(4)*1e3
    S1,S2,H1,DU,DH=direct_moments(v,n)
    return np.array([
      S2/S1-(1+y*w1/w2),
      Z*S1-w2*lam*lam*(x-1)**2*H1,
      x*x*w0*(y-1)**2*S1*(w2+w1*kfun(y))-2*w1*w2*(x-1)**2*DU,
      x*(y-1)*w0*S1*(Z-x*y*y*w0*hfun(x))-2*w1*w2*(x-1)*DH])

def solve_x(xval,guess,n=160):
    z0=np.array([guess[0],guess[1],guess[3]])
    def fun(z):
        vv=np.array([z[0],z[1],xval,z[2]])
        return residual(vv,n)[[1,2,0]]
    sol=root(fun,z0,method='hybr',options={'xtol':1e-12,'maxfev':1000})
    vv=np.array([sol.x[0],sol.x[1],xval,sol.x[2]])
    rr=residual(vv,n)
    assert np.linalg.norm(rr[[1,2,0]],np.inf)<3e-10
    return vv,rr

vseed=np.array([0.0321710159451139,0.370106966023378,3.54218891058057,0.226621581517544])
vc,_=solve_x(vseed[2],vseed,120)
print('NUMERICAL_ONLY_CENTER')
print('VC',*[format(z,'.15g') for z in vc])
for n in (80,100,120):
    mm=direct_moments(vc,n)
    print('GH',n,'S1_S2_H1_DU_DH',*[format(z,'.15g') for z in mm], 'TOTAL',format(mm[3]+mm[4],'.15g'))

def secant_bounds(v,h,n=200):
    w0,w1,x,m=map(float,v); w2,y,Z,S,lam,xi=geom(v)
    tau=w1/w0; rho=w2/w0; b=(xi-1)/2; c=-1/math.sqrt(w0)
    def Frr(r): return scalar_Q_params(tau+rho-r,r,1.0,m,b,c,n)
    q0=Frr(rho); ql=Frr(rho-h); qr=Frr(rho+h)
    L=(q0-ql)/h; R=(qr-q0)/h
    S1lo=-2*L/(m*m); S1hi=-2*R/(m*m)
    def Gtt(t): return scalar_Q_params(t,rho,tau+1.0-t,m,b,c,n)
    q0g=Gtt(tau); qlg=Gtt(tau-h); qrg=Gtt(tau+h)
    Lg=(q0g-qlg)/h; Rg=(qrg-q0g)/h
    cm=m*(m-1)/2
    S2lo=Lg/cm; S2hi=Rg/cm
    if S2lo>S2hi: S2lo,S2hi=S2hi,S2lo
    qm=scalar_Q_params(tau,rho,1,m,b-h,c,n); q0b=scalar_Q_params(tau,rho,1,m,b,c,n); qp=scalar_Q_params(tau,rho,1,m,b+h,c,n)
    dblo=(q0b-qm)/h; dbhi=(qp-q0b)/h
    H1lo=-dbhi/m; H1hi=-dblo/m
    BTlo=b*dblo-q0b; BThi=b*dbhi-q0b
    qmM=scalar_Q_params(tau,rho,1,m-h,b,c,n); q0M=q0b; qpM=scalar_Q_params(tau,rho,1,m+h,b,c,n)
    dmlo=(q0M-qmM)/h; dmhi=(qpM-q0M)/h
    DUlo=m*dmlo-q0M; DUhi=m*dmhi-q0M
    return (S1lo,S1hi),(S2lo,S2hi),(H1lo,H1hi),(DUlo,DUhi),(BTlo,BThi)

print('NUMERICAL_ONLY_SCALAR_SECANT_CENTER')
truth=direct_moments(vc,120)
for h in (0.002,0.001,0.0005):
    bs=secant_bounds(vc,h,120)
    vals=[truth[0],truth[1],truth[2],truth[3],truth[3]+truth[4]]
    names=['S1','S2','H1','DU','DU_PLUS_DH']
    print('H',h)
    for name,(lo,hi),tv in zip(names,bs,vals):
        assert lo <= tv <= hi
        print(name,'LO',format(lo,'.15g'),'TRUE',format(tv,'.15g'),'HI',format(hi,'.15g'),'WIDTH',format(hi-lo,'.8g'))

vl,_=solve_x(vc[2]-0.2,vc,120)
vr,_=solve_x(vc[2]+0.2,vc,120)
print('NUMERICAL_ONLY_TOTAL_BREGMAN_X_CROSSING')
for lab,vv in [('LEFT',vl),('RIGHT',vr)]:
    S1,S2,H1,DU,DH=direct_moments(vv,120)
    CU,CH=targets(vv,120)
    direct=(DU+DH)-(CU+CH)
    print(lab,'DIRECT_TOTAL_RESID',format(direct,'.16e'))
    for h in (0.001,0.0005):
        sb=secant_bounds(vv,h,120)
        s1lo,s1hi=sb[0]; btlo,bthi=sb[4]
        w0,w1,x,m=map(float,vv); w2,y,Z,S,lam,xi=geom(vv)
        coeff=(x*x*w0*(y-1)**2*(w2+w1*kfun(y))/(2*w1*w2*(x-1)**2)
               +x*(y-1)*w0*(Z-x*y*y*w0*hfun(x))/(2*w1*w2*(x-1)))
        assert coeff>0
        rlo=btlo-coeff*s1hi; rhi=bthi-coeff*s1lo
        assert rlo <= direct <= rhi
        print(lab,'H',h,'RESID_LO',format(rlo,'.16e'),'RESID_HI',format(rhi,'.16e'))
        if lab=='LEFT': assert rhi<0
        else: assert rlo>0

# ---------------------------------------------------------------------------
# Numerical chord/tangent/Jensen scalar-Q enclosure demonstration
# ---------------------------------------------------------------------------
def U_scalar(t,b,s=1.0):
    t=np.asarray(t,float)
    return inner_closed(t,b,s)

def U_Ut_scalar(t,b,s=1.0):
    """Closed U and stable spatial derivative U_t for general inner variance s."""
    t=np.asarray(t,float)
    den=1+2*b*s
    rt=math.sqrt(s); rd=math.sqrt(s*den)
    z1=-t/rt; z2=t/rd
    l1=log_ndtr(z1)
    l2=-0.5*math.log(den)-b*t*t/den+log_ndtr(z2)
    U=np.logaddexp(l1,l2)
    logphi1=-0.5*(t/rt)**2-0.5*math.log(2*math.pi)
    logphi2=-0.5*z2*z2-0.5*math.log(2*math.pi)
    dl1=-np.exp(logphi1-l1)/rt
    dl2=-2*b*t/den + np.exp(logphi2-log_ndtr(z2))/rd
    w1=np.exp(l1-U); w2=np.exp(l2-U)
    Ut=w1*dl1+w2*dl2
    return U,Ut

def affine_gauss_int(a0,a1,l,r,m=1.0):
    sh=m*a1
    return math.exp(m*a0+0.5*sh*sh)*(ndtr(r-sh)-ndtr(l-sh))

def cond_partition_bounds(a,d,m,b,s,Nu=256,L=8.0):
    edges=np.linspace(-L,L,Nu+1)
    l=edges[:-1]; r=edges[1:]; mid=(l+r)/2
    tl=a+d*l; tr=a+d*r; tm=a+d*mid
    Ul=U_scalar(tl,b,s); Ur=U_scalar(tr,b,s); Um=U_scalar(tm,b,s)
    a1=(Ur-Ul)/(r-l); a0=Ul-a1*l
    sh=m*a1
    low_terms=np.exp(m*a0+0.5*sh*sh)*(ndtr(r-sh)-ndtr(l-sh))
    lo=float(np.sum(low_terms))
    _,Utmid=U_Ut_scalar(a+d*mid,b,s)
    slope=d*Utmid
    a0u=Um-slope*mid
    shu=m*slope
    high_terms=np.exp(m*a0u+0.5*shu*shu)*(ndtr(r-shu)-ndtr(l-shu))
    hi=float(np.sum(high_terms))+2*ndtr(-L)
    return math.log(max(lo,1e-300)), math.log(hi)

def scalar_Q_cell_bounds(v,Nu=128,Nv=256,L=7.0):
    w0,w1,x,m=map(float,v); w2,y,Z,S,lam,xi=geom(v)
    tau=w1/w0; rho=w2/w0; b=(xi-1)/2; c=-1/math.sqrt(w0)
    d=math.sqrt(tau)
    edges=np.linspace(-L,L,Nv+1)
    qlo=np.empty(Nv+1); qhi=np.empty(Nv+1)
    for j,z in enumerate(edges):
        qlo[j],qhi[j]=cond_partition_bounds(c+math.sqrt(rho)*z,d,m,b,1.0,Nu,L=8.0)
    l=edges[:-1]; r=edges[1:]
    mass=ndtr(r)-ndtr(l)
    mean_num=(np.exp(-0.5*l*l)-np.exp(-0.5*r*r))/math.sqrt(2*math.pi)
    slope=(qlo[1:]-qlo[:-1])/(r-l); intercept=qlo[:-1]-slope*l
    lower=float(np.sum(intercept*mass+slope*mean_num))
    zbar=mean_num/mass
    qu=np.empty(Nv)
    for j,z in enumerate(zbar):
        _,qu[j]=cond_partition_bounds(c+math.sqrt(rho)*z,d,m,b,1.0,Nu,L=8.0)
    upper=float(np.sum(mass*qu))
    Qtail=2*ndtr(-L)
    phiL=math.exp(-0.5*L*L)/math.sqrt(2*math.pi)
    Ez2_tail=2*(L*phiL+ndtr(-L))
    lower += -m*b*((c*c+tau+1)*Qtail + rho*Ez2_tail)
    return lower,upper

qtrue=scalar_Q(vc,120)
print('NUMERICAL_ONLY_SCALAR_Q_CELL_ENCLOSURE')
prev=None
for Nu,Nv in [(32,64),(64,128),(128,256),(256,512)]:
    lo,hi=scalar_Q_cell_bounds(vc,Nu,Nv)
    width=hi-lo
    assert lo <= qtrue <= hi
    ratio=(prev/width if prev is not None else float('nan'))
    print('NU_NV',Nu,Nv,'LO',format(lo,'.12g'),'TRUE',format(qtrue,'.12g'),'HI',format(hi,'.12g'),'WIDTH',format(width,'.8g'),'PREV_OVER_WIDTH',format(ratio,'.6g'))
    prev=width

print('ALL_EXACT_AND_NUMERICAL_SCALAR_COMPILER_CHECKS_PASS')
