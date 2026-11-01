#!/usr/bin/env python3
"""NM13-03 / T03 2026-09-20.

Exact proof checks:
  * final exact complete-second transport microstep on the inherited directed chart;
  * algebraic recurrence behind the hinge entropy/log-partition comparison.

Numerical-only checks:
  * verify the sharp pointwise derivative ratio for the inner Gaussian hinge tilt;
  * evaluate the new coupled entropy cage on NM13-07's delta=1e-3 pivoted x-branch;
  * verify the new coupled-m monotonicity at fixed geometry by finite differences.

Ordinary Gauss-Hermite values are NUMERICAL_ONLY and are not a directed source proof.
"""
from fractions import Fraction as F
import math
import numpy as np
import sympy as sp
from numpy.polynomial.hermite import hermgauss
from scipy.special import log_ndtr, logsumexp
from scipy.optimize import root

# ---------------------------------------------------------------------------
# Exact inherited complete-second transport microstep
# ---------------------------------------------------------------------------
alphaL=F(315148718753,50_000_000_000)               # 6.30297437506
alpha0=F(12319635,1_000_000)                        # 12.319635
alpha_before=F(12319634446193,1_000_000_000_000)   # 12.319634446193
alpha_after=F(30799086115477,2_500_000_000_000)    # 12.3196344461908
slope=F(4136629,105883920)
psi0=F(23584189005311,1090044380000000000000)
dec_lo=F(446,1_000_000_000)
dec_hi=F(554,1_000_000_000)
dec=alpha0-alpha_after
psi_after=psi0-slope*dec
assert alpha_before-alpha_after == F(11,5_000_000_000_000)
assert dec_lo <= dec <= dec_hi
assert psi_after > 0
print('EXACT_SOURCE_TRANSPORT')
print('ALPHA_BEFORE', float(alpha_before))
print('ALPHA_AFTER', float(alpha_after))
print('GAIN_EXACT', alpha_before-alpha_after, float(alpha_before-alpha_after))
print('DEC_FROM_ANCHOR', dec, float(dec))
print('PSI_LOWER_EXACT', psi_after, float(psi_after))
print('WIDTH_AFTER', float(alpha_after-alphaL))
print('EXACT_SOURCE_TRANSPORT_PASS')

# ---------------------------------------------------------------------------
# Exact symbolic algebra for the new hinge entropy lemma
# ---------------------------------------------------------------------------
r,t,m1,m2,m3,neg = sp.symbols('r t m1 m2 m3 neg', positive=True, finite=True)
c=1+r
# Positive-half-line integration by parts recurrence: c*m3=t*m2+2*m1.
rec=(t*m2+2*m1)/c
cov=sp.simplify(rec-m2*m1)
identity=sp.simplify(c*cov-(2*m1+m2*(t-c*m1)))
assert identity==0
# Full score identity says t-c*m1 = E[Y 1_{Y<0}] =: neg <=0.
# Hence cov <= 2*m1/c and K_t=(r^2/2)cov <= r^2*m1/c=(r/c)(-U_t).
upper=sp.simplify(r**2*m1/c-(r/c)*(r*m1))
assert upper==0
print('EXACT_HINGE_RECURRENCE_IDENTITY_PASS')
print('THEOREM_CONSTANT_c_r = r/(1+r)')

# Exact residual-row elimination for the positive-gap system.
w0,w1,w2,x,y,Z,lam,mr,S1,Q,DU,DH,H1,ku,hx=sp.symbols(
    'w0 w1 w2 x y Z lam mr S1 Q DU DH H1 ku hx', nonzero=True)
# Here mr=m*r and positive-gap geometry gives r=lam*(x-1).
AU=x**2*w0*(y-1)**2*S1*(w2+w1*ku)
BU=2*w1*w2*(x-1)**2
RU=AU-BU*DU
RS=Z*S1-w2*lam**2*(x-1)**2*H1
A0=x*(y-1)*w0*S1*(Z-x*y**2*w0*hx)
RH=A0-2*w1*w2*(x-1)*DH
# Entropy closure DH=-Q-DU-(m*r/2)H1 and mr=m*lam*(x-1).
RHclosed=sp.expand(RH.subs(DH,-Q-DU-mr*H1/2))
RHhat=(2*w1*w2*(x-1)*Q + A0
       + x**2*w0*(y-1)**2*S1*(w2+w1*ku)/(x-1)
       + (mr/(lam*(x-1)))*w1*Z*S1/lam)
# Last coefficient mr/[lam(x-1)] is m; retain mr to avoid a new symbol.
combo=sp.simplify(RHhat - (RHclosed + RU/(x-1) + (mr*w1/(lam**2*(x-1)))*RS))
assert combo==0
print('EXACT_KL_FREE_RESIDUAL_ROW_IDENTITY_PASS')

# ---------------------------------------------------------------------------
# Numerical-only complete-third positive-gap branch, copied independently
# from the published-in-repo compiler formulas.
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
    S=math.sqrt(Z)/(x*y)
    lam=S/(S+DEL)
    xi=1+lam*(x-1)
    return w2,y,Z,S,lam,xi

def kernel(tarr,xi):
    tarr=np.asarray(tarr,float)
    l1=log_ndtr(-tarr)
    z=tarr/math.sqrt(xi)
    l2=-.5*math.log(xi)-(xi-1)*tarr*tarr/(2*xi)+log_ndtr(z)
    U=np.logaddexp(l1,l2)
    f2=np.exp(l2-U)  # positive-half tilted probability
    phF=np.exp(-.5*tarr*tarr-.5*math.log(2*math.pi)-U)
    mu1=(tarr*f2+phF)/xi
    mu2=(tarr*mu1+f2)/xi
    Ut=-(xi-1)*mu1
    K=-(xi-1)*.5*mu2-U
    return U,Ut,mu1,mu2,K

def bundle(v,n,m_override=None):
    w0,w1,x,m0=map(float,v); w2,y,Z,S,lam,xi=geom(v)
    m=m0 if m_override is None else float(m_override)
    Uq,wu=gh(n); Vq,wv=gh(n)
    T=np.sqrt(w1/w0)*Uq[None,:]+np.sqrt(w2/w0)*Vq[:,None]-1/np.sqrt(w0)
    U,Ut,mu1,mu2,K=kernel(T,xi)
    lt=np.log(wu)[None,:]+m*U
    lz=logsumexp(lt,axis=1)
    tw=np.exp(lt-lz[:,None])
    g=np.sum(tw*Ut,axis=1)
    S1=float(np.dot(wv,g*g))
    S2=float(np.dot(wv,np.sum(tw*Ut*Ut,axis=1)))
    H1=float(np.dot(wv,np.sum(tw*mu2,axis=1)))
    EU=np.sum(tw*U,axis=1)
    DUv=m*EU-lz
    DU=float(np.dot(wv,DUv))
    DH=float(np.dot(wv,m*np.sum(tw*K,axis=1)))
    Q=float(np.dot(wv,lz))
    return dict(S1=S1,S2=S2,H1=H1,DU=DU,DH=DH,Q=Q,xi=xi,r=xi-1,y=y,Z=Z,S=S,lam=lam)

def kfun(y): return y*(y*math.log(y)-y+1)/(y-1)**2
def hfun(x): return x*(x-1-math.log(x))/(x-1)**2

def residual(v,n):
    w0,w1,x,m=map(float,v); w2,y,Z,S,lam,xi=geom(v)
    if min(w0,w1,w2)<=0 or x<=1 or not(0<m<1): return np.ones(4)*1e3
    b=bundle(v,n)
    S1,S2,H1,DU,DH=b['S1'],b['S2'],b['H1'],b['DU'],b['DH']
    return np.array([
      S2/S1-(1+y*w1/w2),
      Z*S1-w2*lam*lam*(x-1)**2*H1,
      x*x*w0*(y-1)**2*S1*(w2+w1*kfun(y))-2*w1*w2*(x-1)**2*DU,
      x*(y-1)*w0*S1*(Z-x*y*y*w0*hfun(x))-2*w1*w2*(x-1)*DH])

def alpha_of(v,n):
    w0,w1,x,m=map(float,v); w2,y,Z,S,lam,xi=geom(v)
    S1=bundle(v,n)['S1']
    return w2*(x-1)**2/(x*x*y*y*w0*S1)

def reduced_rh(v,n):
    w0,w1,x,m=map(float,v); w2,y,Z,S,lam,xi=geom(v)
    b=bundle(v,n); S1,Q=b['S1'],b['Q']
    term = x*(y-1)*w0*(Z-x*y*y*w0*hfun(x))
    term += x*x*w0*(y-1)**2*(w2+w1*kfun(y))/(x-1)
    term += m*w1*Z/lam
    return 2*w1*w2*(x-1)*Q + S1*term

def solve_x(xval,guess,n):
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
vc,_=solve_x(vseed[2],vseed,160)

# Pointwise derivative comparison K_t <= c_r(-U_t) over broad t grids.
print('NUMERICAL_ONLY_POINTWISE_SHARPNESS')
for xi in (1.5,2.0,3.5,6.0):
    tt=np.linspace(-8,8,4001)
    U,Ut,mu1,mu2,K=kernel(tt,xi)
    rr=xi-1; cc=rr/xi
    mu3=(tt*mu2+2*mu1)/xi
    Kt=.5*rr*rr*(mu3-mu2*mu1)
    mask=(-Ut)>1e-12
    ratio=np.max(Kt[mask]/(-Ut[mask]))
    pointgap=np.min(cc*(-U)-K)
    assert np.min(Kt)>-2e-12
    assert ratio <= cc+3e-11
    assert pointgap > -2e-12
    print('XI',xi,'C',cc,'MAX_KT_OVER_MINUSUT',ratio,'MIN_POINTWISE_GAP',pointgap)

# Evaluate the new static cage on left/center/right of NM07 pivoted x branch.
print('NUMERICAL_ONLY_X_BRANCH_COUPLED_CAGE')
guess=vc.copy()
branch={}
for dx in (-.2,0,.2):
    vv,rrv=solve_x(vc[2]+dx,guess,160); guess=vv; branch[dx]=vv
    b=bundle(vv,160)
    cr=b['r']/(1+b['r'])
    upper=cr*(-b['Q']-b['DU'])
    w0,w1,x,m=vv; w2=1-w0-w1
    # Exact closure: DH = -Q-DU-(m*r/2)H1.
    dh_id=-b['Q']-b['DU']-.5*m*b['r']*b['H1']
    rhhat=reduced_rh(vv,160)
    assert abs(dh_id-b['DH']) < 2e-13
    assert abs(rhhat-rrv[3]) < 3e-13
    assert b['DH'] <= upper+2e-12
    print('DX',dx,'M',m,'R',b['r'],'C',cr,'Q',b['Q'],'DU',b['DU'],'H1',b['H1'],'DH',b['DH'],
          'DH_IDENTITY_ERR',dh_id-b['DH'],'HINGE_UPPER',upper,'HINGE_SLACK',upper-b['DH'],
          'RH_ORIG',rrv[3],'RH_KLFREE',rhhat,'RH_IDENTITY_ERR',rhhat-rrv[3],
          'ALPHA',alpha_of(vv,160))

# Coupled m monotonicity at fixed center geometry: C(m)=DH+c*DU should increase.
print('NUMERICAL_ONLY_FIXED_GEOMETRY_M_MONOTONICITY')
b0=bundle(vc,200)
cr=b0['r']/(1+b0['r'])
ms=np.linspace(vc[3]-.06,vc[3]+.06,13)
Cs=[]
for mm in ms:
    bb=bundle(vc,200,m_override=mm)
    C=bb['DH']+cr*bb['DU']
    Cs.append(C)
    print('M',mm,'DU',bb['DU'],'DH',bb['DH'],'COUPLED',C)
Cs=np.array(Cs)
assert np.min(np.diff(Cs))>0
# centered numerical derivative and theorem lower EK=DH/m at center
h=1e-4
bp=bundle(vc,240,m_override=vc[3]+h); bm=bundle(vc,240,m_override=vc[3]-h); bc=bundle(vc,240)
der=(bp['DH']+cr*bp['DU']-(bm['DH']+cr*bm['DU']))/(2*h)
lower=bc['DH']/vc[3]
print('CENTER_COUPLED_DERIVATIVE_FD',der,'THEOREM_LOWER_DH_OVER_M',lower,'MARGIN',der-lower)
assert der+2e-8 >= lower

print('NUMERICAL_ONLY_KLFREE_ENDPOINT_ORDER_STABILITY')
for n in (80,100,120,160,200):
    vl,rl=solve_x(vc[2]-.2,vc.copy(),n); vr,rr=solve_x(vc[2]+.2,vc.copy(),n)
    hl=reduced_rh(vl,n); hr=reduced_rh(vr,n)
    assert hl>2e-5 and hr<-1e-5
    assert abs(hl-rl[3])<2e-11 and abs(hr-rr[3])<2e-11
    print('GH',n,'KLFREE_LEFT',format(hl,'.16e'),'KLFREE_RIGHT',format(hr,'.16e'),
          'ORIG_DIFF_LEFT',format(hl-rl[3],'.3e'),'ORIG_DIFF_RIGHT',format(hr-rr[3],'.3e'))

print('ALL_HINGE_ENTROPY_COUPLING_CHECKS_PASS')
