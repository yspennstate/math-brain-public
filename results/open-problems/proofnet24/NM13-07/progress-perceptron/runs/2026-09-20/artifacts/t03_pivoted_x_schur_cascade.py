#!/usr/bin/env python3
"""NM13-07 / T03, 2026-09-20.

Exact part:
  * preserves the inherited directed complete-second certificate and takes one
    final bookkeeping microstep from 12.319634446194 to 12.319634446193 by
    exact rational transport.  This is source-level rigorous conditional only
    on the already archived directed certificate/source transfer; it is NOT the
    substantive mechanism of this run.

Numerical-only part:
  * tests a new pivoted nested-Schur cascade for the delta=1e-3 complete-third
    positive-gap compiler.  Residual order is
      (Rscale, RU, Rratio, RH)
    and variable order is
      (w0, w1, m, x).
    The first 3x3 branch block is much better conditioned than the companion's
    (w0,w1,x)|m block.  All Gaussian expectations here are ordinary
    Gauss-Hermite and therefore NUMERICAL_ONLY, not a directed source proof.
"""
from fractions import Fraction as F
import math, itertools
import numpy as np
import sympy as sp
from numpy.polynomial.hermite import hermgauss
from scipy.special import log_ndtr, logsumexp
from scipy.optimize import root

# ---------------------------------------------------------------------------
# Exact bookkeeping microstep inside inherited directed complete-second chart
# ---------------------------------------------------------------------------
alphaL=F(315148718753,50_000_000_000)               # 6.30297437506
alpha0=F(12319635,1_000_000)                        # 12.319635
alpha_before=F(6159817223097,500_000_000_000)       # 12.319634446194
alpha_after=F(12319634446193,1_000_000_000_000)     # 12.319634446193
assert alpha_before-alpha_after==F(1,1_000_000_000_000)
# inherited recentered chart decrement range [4.46e-7,5.54e-7]
dec_lo=F(446,1_000_000_000)
dec_hi=F(554,1_000_000_000)
delta_new=alpha0-alpha_after
assert dec_lo <= delta_new <= dec_hi
# inherited exact objective transport data
slope=F(4136629,105883920)
psi0=F(23584189005311,1090044380000000000000)
psi_new=psi0-slope*delta_new
assert psi_new>0
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
# Exact symbolic Schur-pivot identities for a generic 4x4 Jacobian
# ---------------------------------------------------------------------------
a=sp.symbols('a0:16')
J=sp.Matrix(4,4,a)
D1=J[:1,:1].det(); D2=J[:2,:2].det(); D3=J[:3,:3].det(); D4=J.det()
# Schur pivots s_k = det(J_k)/det(J_{k-1}), D0=1.
s1=J[0,0]
s2=sp.simplify(J[1,1]-J[1,0]*J[0,1]/J[0,0])
A2=J[:2,:2]
b2=J[:2,2]
c2=J[2,:2]
s3=sp.simplify(J[2,2]-(c2*A2.inv()*b2)[0])
A3=J[:3,:3]
b3=J[:3,3]
c3=J[3,:3]
s4=sp.simplify(J[3,3]-(c3*A3.inv()*b3)[0])
assert sp.simplify(s1-D1)==0
assert sp.simplify(s2-D2/D1)==0
assert sp.simplify(s3-D3/D2)==0
assert sp.simplify(s4-D4/D3)==0
assert sp.simplify(s1*s2*s3*s4-D4)==0
print('EXACT_NESTED_SCHUR_IDENTITIES_PASS')

# ---------------------------------------------------------------------------
# Numerical-only complete-third dimensionless residuals, delta=1e-3
# ---------------------------------------------------------------------------
DEL=1e-3
GH={}
def gh(n):
    if n not in GH:
        z,w=hermgauss(n); GH[n]=(np.sqrt(2)*z,w/np.sqrt(np.pi))
    return GH[n]

def geom(v):
    w0,w1,x,m=map(float,v); w2=1-w0-w1
    y=1+m*(x-1)*w1/(x*w0)
    Z=x*y*y*w0+y*w1+w2
    S=math.sqrt(Z)/(x*y); lam=S/(S+DEL); xi=1+lam*(x-1)
    return w2,y,Z,S,lam,xi

def kernel(t,xi):
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

def moments(v,n):
    w0,w1,x,m=map(float,v); w2,y,Z,S,lam,xi=geom(v)
    Uq,wu=gh(n); Vq,wv=gh(n)
    T=np.sqrt(w1/w0)*Uq[None,:]+np.sqrt(w2/w0)*Vq[:,None]-1/np.sqrt(w0)
    U,Ut,H,K=kernel(T,xi)
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

def residual(v,n):
    w0,w1,x,m=map(float,v); w2,y,Z,S,lam,xi=geom(v)
    if min(w0,w1,w2)<=0 or x<=1 or not(0<m<1): return np.ones(4)*1e3
    S1,S2,H1,DU,DH=moments(v,n)
    return np.array([
      S2/S1-(1+y*w1/w2),
      Z*S1-w2*lam*lam*(x-1)**2*H1,
      x*x*w0*(y-1)**2*S1*(w2+w1*kfun(y))-2*w1*w2*(x-1)**2*DU,
      x*(y-1)*w0*S1*(Z-x*y*y*w0*hfun(x))-2*w1*w2*(x-1)*DH])

def alpha_of(v,n):
    w0,w1,x,m=map(float,v); w2,y,Z,S,lam,xi=geom(v)
    S1=moments(v,n)[0]
    return w2*(x-1)**2/(x*x*y*y*w0*S1)

def jac_fd(fun,z,h=5e-6):
    y=np.asarray(fun(z)); A=np.zeros((len(y),len(z)))
    for j in range(len(z)):
        hh=h*max(1.,abs(z[j])); zp=z.copy(); zm=z.copy(); zp[j]+=hh; zm[j]-=hh
        A[:,j]=(np.asarray(fun(zp))-np.asarray(fun(zm)))/(2*hh)
    return A

# archived positive-gap waypoint
vseed=np.array([0.0321710159451139,0.370106966023378,3.54218891058057,0.226621581517544])

def solve_x(xval,guess,n):
    z0=np.array([guess[0],guess[1],guess[3]])
    def fun(z):
        vv=np.array([z[0],z[1],xval,z[2]])
        return residual(vv,n)[[1,2,0]]
    sol=root(fun,z0,method='hybr',options={'xtol':1e-12,'maxfev':1000})
    vv=np.array([sol.x[0],sol.x[1],xval,sol.x[2]])
    rr=residual(vv,n)
    assert np.linalg.norm(rr[[1,2,0]],np.inf)<2e-10
    return vv,rr

# Refine center at GH160.
vc,_=solve_x(vseed[2],vseed,160)
Jc=jac_fd(lambda z:residual(z,160),vc)
old3=Jc[np.ix_([0,1,2],[0,1,2])]
new3=Jc[np.ix_([1,2,0],[0,1,3])]
sv_old=np.linalg.svd(old3,compute_uv=False); sv_new=np.linalg.svd(new3,compute_uv=False)
print('NUMERICAL_ONLY_CENTER_CONDITIONING')
print('OLD_M_BRANCH_SIGMA3_MIN',sv_old[-1],'COND3',sv_old[0]/sv_old[-1])
print('NEW_X_BRANCH_SIGMA3_MIN',sv_new[-1],'COND3',sv_new[0]/sv_new[-1])
print('SIGMA_MIN_GAIN',sv_new[-1]/sv_old[-1])
print('COND_IMPROVEMENT', (sv_old[0]/sv_old[-1])/(sv_new[0]/sv_new[-1]))

# Pivot ordering: residuals (Rscale,RU,Rratio,RH), vars (w0,w1,m,x).
roword=[1,2,0,3]; colord=[0,1,3,2]
def pivots(J0):
    A=J0[np.ix_(roword,colord)]
    out=[]; prev=1.0
    for k in range(1,5):
        d=float(np.linalg.det(A[:k,:k])); out.append(d/prev); prev=d
    return np.array(out),A

# Sweep broad x interval.  This is a falsification/conditioning scout only.
print('NUMERICAL_ONLY_PIVOTED_X_BRANCH_GH160')
guess=vc.copy(); table=[]
for dx in np.linspace(-.2,.2,9):
    xx=vc[2]+dx
    vv,rr=solve_x(xx,guess,160); guess=vv
    JJ=jac_fd(lambda z:residual(z,160),vv)
    pv,A=pivots(JJ)
    sv=np.linalg.svd(A[:3,:3],compute_uv=False)
    # finite-difference derivative of reconstructed alpha along the solved x branch
    hh=2e-4
    vp,_=solve_x(xx+hh,vv,120); vm,_=solve_x(xx-hh,vv,120)
    dalpha=(alpha_of(vp,120)-alpha_of(vm,120))/(2*hh)
    aa=alpha_of(vv,160)
    table.append((dx,*pv,sv[-1],sv[0]/sv[-1],rr[3],aa,dalpha,*vv[[0,1,3]]))
    print('DX',format(dx,'.6f'),
          'PIVOTS',*[format(t,'.12e') for t in pv],
          'SIGMA3',format(sv[-1],'.12e'),'COND3',format(sv[0]/sv[-1],'.6f'),
          'RH',format(rr[3],'.12e'),'ALPHA',format(aa,'.15f'),
          'DALPHA_DX',format(dalpha,'.12e'),
          'W0_W1_M',*[format(t,'.12f') for t in vv[[0,1,3]]])

T=np.array(table,float)
# Columns after dx: p1..p4,sigma,cond,RH,alpha,dalpha,w0,w1,m
assert np.max(T[:,1]) < 0             # p1<0
assert np.min(T[:,2]) > 0             # p2>0
assert np.min(T[:,3]) > 0             # p3>0
assert np.max(T[:,4]) < 0             # p4<0
assert T[0,7] > 0 and T[-1,7] < 0     # RH crossing across x interval
assert np.min(T[:,9]) > 0             # alpha increases with x in scout
print('NUMERICAL_ONLY_PIVOT_RANGES')
for j,name in enumerate(['S1','S2','S3','S4'],start=1):
    print(name,'MIN',T[:,j].min(),'MAX',T[:,j].max())
print('SIGMA3_MIN_OVER_SWEEP',T[:,5].min())
print('COND3_MAX_OVER_SWEEP',T[:,6].max())
print('RH_LEFT_RIGHT',T[0,7],T[-1,7])
print('ALPHA_LEFT_RIGHT',T[0,8],T[-1,8])
print('DALPHA_DX_MIN',T[:,9].min())
print('PROSPECTIVE_CONSERVATIVE_ALPHA_BAR_IF_DIRECTED', '12.31950')
print('PROSPECTIVE_GAIN_VS_CURRENT', float(alpha_after)-12.31950)

# Quadrature-order stability at the two x endpoints, solving each order afresh.
print('NUMERICAL_ONLY_ENDPOINT_ORDER_STABILITY')
for n in (80,100,120,160,200):
    gl=vc.copy(); gr=vc.copy()
    vl,rl=solve_x(vc[2]-.2,gl,n); vr,rr=solve_x(vc[2]+.2,gr,n)
    print('GH',n,
          'RH_LEFT',format(rl[3],'.16e'),'RH_RIGHT',format(rr[3],'.16e'),
          'ALPHA_LEFT',format(alpha_of(vl,n),'.15f'),'ALPHA_RIGHT',format(alpha_of(vr,n),'.15f'))
    assert rl[3]>2e-5 and rr[3]<-1e-5
    assert alpha_of(vr,n)<12.31950
print('ALL_EXACT_AND_NUMERICAL_CASCADE_CHECKS_PASS')
