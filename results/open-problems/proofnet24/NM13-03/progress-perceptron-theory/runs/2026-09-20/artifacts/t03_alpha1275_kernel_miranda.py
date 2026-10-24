#!/usr/bin/env python3
"""NM13-03 / T03: closed Gaussian kernel + second-full alpha=12.75 certificate scout.

The exact theorem part is the closed form for f, d_B f and d_mu f, combined with
NM13-07's exact two-scalar complete-second-lift reconstruction.  The numerical
part independently evaluates the resulting scalar integrals by two Gauss-Hermite
orders and adaptive quadrature, scans a Poincare-Miranda rectangle, and records
large strict sign/objective margins.  The finite face scan is a review-pending
computer-assisted certificate, not a substitute for independent verification.
"""
import math
from fractions import Fraction as Q
import numpy as np
import sympy as sp
from numpy.polynomial.hermite import hermgauss
from scipy.integrate import quad
from scipy.optimize import root
from scipy.special import ndtr

ALPHA0=12.75
ALPHA_L=6.30297437506
ALPHA_OLD=12.78437096216
P0=0.6457670646889506
B0=4.929229200895245
DP=0.004
DB=0.15

# Deterministic second-full terms.  T_D is the partial derivative with gamma held fixed,
# followed by the stationary substitution gamma=c/(4B).
p,D,B,g=sp.symbols('p D B g', positive=True)
q=p*D**2
gp=(1-q)/(2*D*(1-p))
c=(1-D**2)/(D*(1-p)*(1-p*D**2))
T=sp.Rational(1,2)*(1-p*q)*c-gp+sp.Rational(1,2)/c*sp.log(D/(2*gp))-q/(2*D)+g
TD=sp.diff(T,D).subs(g,c/(4*B))
cD=sp.diff(c,D)
Tsub=T.subs(g,c/(4*B))
TDf=sp.lambdify((p,D,B),TD,'numpy')
cDf=sp.lambdify((p,D),cD,'numpy')
Tsubf=sp.lambdify((p,D,B),Tsub,'numpy')

# New closed conditional kernel lemma.  Here Y=mu+sH, A=1+2Bs^2,
# Q=A^{-1/2} exp(-B mu^2/A) Phi(mu/(s sqrt A)),
# f=E exp[-B(Y_+)^2]=Phi(-mu/s)+Q.
def closed_f(mu,s,BB):
    A=1+2*BB*s*s
    a=mu/s
    v=mu/(s*math.sqrt(A))
    phia=math.exp(-0.5*a*a)/math.sqrt(2*math.pi)
    Qv=math.exp(-BB*mu*mu/A)/math.sqrt(A)*ndtr(v)
    f=ndtr(-a)+Qv
    fB=-(Qv*(mu*mu+s*s*A)+mu*s*phia)/(A*A)
    fmu=-(2*BB/A)*(mu*Qv+s*phia)
    return f,fB,fmu

# Finite-difference falsification check of the exact differentiated closed forms.
max_kernel_fd_error=0.0
for mu in np.linspace(-6,6,31):
    s=.59; BB=4.9; h=1e-5
    f,fB,fmu=closed_f(mu,s,BB)
    fdB=(closed_f(mu,s,BB+h)[0]-closed_f(mu,s,BB-h)[0])/(2*h)
    fdm=(closed_f(mu+h,s,BB)[0]-closed_f(mu-h,s,BB)[0])/(2*h)
    max_kernel_fd_error=max(max_kernel_fd_error,abs(fB-fdB),abs(fmu-fdm))
assert max_kernel_fd_error < 2e-9
print('CLOSED_KERNEL_DERIVATIVE_SELF_CHECK_PASS',repr(max_kernel_fd_error))

# Exact rational tails inherited in form but rechecked here on the coarser box B<8,p<2/3.
phi9_major=Q(10,27)**40
I_tail=Q(85,9)*phi9_major
IB_tail=Q(19,1)*phi9_major
K_tail=Q(19000,1)*phi9_major
assert I_tail < Q(1,10**16)
assert IB_tail < Q(1,10**15)
assert K_tail < Q(1,10**12)
print('EXACT_TAIL_RECHECK_PASS',float(I_tail),float(IB_tail),float(K_tail))

def gh_factory(n):
    hn,hw=hermgauss(n)
    z=hn*np.sqrt(2.0); w=hw/np.sqrt(np.pi)
    def scalar(pp,BB):
        s=np.sqrt(1-pp); mu=np.sqrt(pp)*z-1.0; A=1+2*BB*s*s
        a=mu/s; v=mu/(s*np.sqrt(A))
        phia=np.exp(-0.5*a*a)/math.sqrt(2*math.pi)
        Qv=np.exp(-BB*mu*mu/A)/np.sqrt(A)*ndtr(v)
        f=ndtr(-a)+Qv
        Iv=np.sum(w*np.log(f))
        fB=-(Qv*(mu*mu+s*s*A)+mu*s*phia)/(A*A)
        IBv=np.sum(w*fB/f)
        fmu=-(2*BB/A)*(mu*Qv+s*phia)
        Kv=np.sum(w*pp*(fmu/f)**2)
        D2=Kv/(-4*pp*pp*BB*BB*IBv)
        DD=np.sqrt(D2)
        cc=(1-DD*DD)/(DD*(1-pp)*(1-pp*DD*DD))
        aa=-cc*cc/(4*BB*BB*IBv)
        H=Iv-BB*IBv-4*BB*BB*IBv*(TDf(pp,DD,BB)/cDf(pp,DD))
        Psi=Tsubf(pp,DD,BB)+cc*Iv/(4*BB*BB*IBv)
        return np.array([H,aa,Psi,DD,Iv,IBv,Kv])
    return scalar

gh200=gh_factory(200)
gh260=gh_factory(260)
r=root(lambda x:[gh260(x[0],x[1])[0],gh260(x[0],x[1])[1]-ALPHA0],[P0,B0],tol=1e-12)
assert r.success
v0=gh260(*r.x)
print('CENTER_ROOT',repr(float(r.x[0])),repr(float(r.x[1])))
print('CENTER_DATA H alpha Psi D',*(repr(float(t)) for t in v0[:4]))

# Poincare-Miranda rectangle.  Required orientation:
# H>0 on p=P0-DP; H<0 on p=P0+DP;
# alpha-ALPHA0>0 on B=B0-DB; alpha-ALPHA0<0 on B=B0+DB.
nface=161
Bs=np.linspace(B0-DB,B0+DB,nface)
ps=np.linspace(P0-DP,P0+DP,nface)
HL200=np.array([gh200(P0-DP,b)[0] for b in Bs]); HL260=np.array([gh260(P0-DP,b)[0] for b in Bs])
HR200=np.array([gh200(P0+DP,b)[0] for b in Bs]); HR260=np.array([gh260(P0+DP,b)[0] for b in Bs])
AB200=np.array([gh200(x,B0-DB)[1]-ALPHA0 for x in ps]); AB260=np.array([gh260(x,B0-DB)[1]-ALPHA0 for x in ps])
AT200=np.array([gh200(x,B0+DB)[1]-ALPHA0 for x in ps]); AT260=np.array([gh260(x,B0+DB)[1]-ALPHA0 for x in ps])
quad_order_discrepancy=max(np.max(abs(HL200-HL260)),np.max(abs(HR200-HR260)),np.max(abs(AB200-AB260)),np.max(abs(AT200-AT260)))
print('MIRANDA_FACE_MARGINS H_left_min H_right_max alpha_bottom_min alpha_top_max',repr(float(HL260.min())),repr(float(HR260.max())),repr(float(AB260.min())),repr(float(AT260.max())))
print('FACE_GH200_GH260_MAX_DISCREPANCY',repr(float(quad_order_discrepancy)))
assert HL260.min()>3.5e-5 and HR260.max()<-3.8e-5
assert AB260.min()>0.028 and AT260.max()<-0.023
assert quad_order_discrepancy<1e-11

# Dense objective scan on the entire rectangle.
psi_min=1e9; psi_loc=None; psi_disc=0.0
for pp in np.linspace(P0-DP,P0+DP,61):
    for bb in np.linspace(B0-DB,B0+DB,61):
        a=gh260(pp,bb); b=gh200(pp,bb)
        if a[2]<psi_min: psi_min=float(a[2]); psi_loc=(float(pp),float(bb))
        psi_disc=max(psi_disc,abs(float(a[2]-b[2])))
print('PSI_GRID_MIN',repr(psi_min),repr(psi_loc),'GH_DISCREPANCY',repr(psi_disc))
assert psi_min>0.0068 and psi_disc<1e-11

# Independent adaptive-quadrature cross-check at the center and four rectangle corners.
def quad_scalar(pp,BB):
    s=math.sqrt(1-pp); rp=math.sqrt(pp)
    def tr(z):
        mu=rp*z-1; A=1+2*BB*s*s; a=mu/s; vv=mu/(s*math.sqrt(A))
        phia=math.exp(-.5*a*a)/math.sqrt(2*math.pi)
        Qv=math.exp(-BB*mu*mu/A)/math.sqrt(A)*ndtr(vv)
        f=ndtr(-a)+Qv
        fB=-(Qv*(mu*mu+s*s*A)+mu*s*phia)/(A*A)
        fmu=-(2*BB/A)*(mu*Qv+s*phia)
        den=math.exp(-z*z/2)/math.sqrt(2*math.pi)
        return math.log(f)*den,(fB/f)*den,pp*(fmu/f)**2*den
    vv=[]; ee=[]
    for k in range(3):
        x,e=quad(lambda zz:tr(zz)[k],-9,9,epsabs=2e-13,epsrel=2e-13,limit=500)
        vv.append(x); ee.append(e)
    Iv,IBv,Kv=vv
    DD=math.sqrt(Kv/(-4*pp*pp*BB*BB*IBv))
    cc=(1-DD*DD)/(DD*(1-pp)*(1-pp*DD*DD))
    aa=-cc*cc/(4*BB*BB*IBv)
    H=Iv-BB*IBv-4*BB*BB*IBv*(TDf(pp,DD,BB)/cDf(pp,DD))
    Psi=Tsubf(pp,DD,BB)+cc*Iv/(4*BB*BB*IBv)
    return np.array([H,aa,Psi,DD,Iv,IBv,Kv]),max(ee)

max_qdiff=0.0; max_qerr=0.0
pts=[tuple(r.x),(P0-DP,B0-DB),(P0-DP,B0+DB),(P0+DP,B0-DB),(P0+DP,B0+DB)]
for pt in pts:
    qv,qe=quad_scalar(*pt); gv=gh260(*pt)
    max_qdiff=max(max_qdiff,float(np.max(abs(qv-gv)))); max_qerr=max(max_qerr,float(qe))
print('ADAPTIVE_QUAD_CROSSCHECK max_quad_minus_GH260 max_reported_quad_error',repr(max_qdiff),repr(max_qerr))
assert max_qdiff<2e-12 and max_qerr<2e-12

print('CANDIDATE_ALPHA_U',ALPHA0)
print('CANDIDATE_WIDTH',repr(ALPHA0-ALPHA_L))
print('STRICT_IMPROVEMENT',repr(ALPHA_OLD-ALPHA0))
print('ALL_CHECKS_PASS')
