#!/usr/bin/env python3
"""NM13-07 / T03: exact tilted-moment derivative compiler + numerical scout.

Exact parts: rational contraction arithmetic and algebraic derivative formulas stated in
this run's report. Numerical parts: 260-node Gauss-Hermite evaluation and finite grid
sanity checks. Numerical quadrature is explicitly not a rigorous interval enclosure.
"""
import math, itertools
from fractions import Fraction as F
import numpy as np
import sympy as sp
from numpy.polynomial.hermite import hermgauss
from scipy.special import ndtr

P0=0.6457670646889506
B0=4.929229200895245

p,D,B,g=sp.symbols('p D B g', positive=True)
q=p*D**2
gp=(1-q)/(2*D*(1-p))
c=(1-D**2)/(D*(1-p)*(1-p*D**2))
T=sp.Rational(1,2)*(1-p*q)*c-gp+sp.Rational(1,2)/c*sp.log(D/(2*gp))-q/(2*D)+g
TD_hold=sp.diff(T,D).subs(g,c/(4*B))
cD=sp.diff(c,D)
A0=sp.simplify(TD_hold/cD)
Tsub=sp.simplify(T.subs(g,c/(4*B)))
funcs=sp.lambdify((p,D,B),(c,cD,A0,sp.diff(A0,p),sp.diff(A0,D),Tsub,
    sp.diff(Tsub,p),sp.diff(Tsub,D),sp.diff(Tsub,B),sp.diff(c,p)),'numpy')

hn,hw=hermgauss(260)
z=hn*np.sqrt(2.0); w=hw/np.sqrt(np.pi)

def scalar(pp,BB):
    s=np.sqrt(1-pp); mu=np.sqrt(pp)*z-1.0
    AA=1+2*BB*s*s; a=mu/s; v=mu/(s*np.sqrt(AA))
    phia=np.exp(-0.5*a*a)/math.sqrt(2*math.pi)
    J0=np.exp(-BB*mu*mu/AA)/np.sqrt(AA)*ndtr(v)
    f=ndtr(-a)+J0
    # J_r = E[Y_+^r exp(-B Y_+^2)].
    J1=(mu*J0+s*phia)/AA
    J2=(mu*J1+s*s*J0)/AA
    J3=(mu*J2+2*s*s*J1)/AA
    J4=(mu*J3+3*s*s*J2)/AA
    fB=-J2; fBB=J4
    fmu=-2*BB*J1
    fmuB=-2*J1+2*BB*J3
    fmumu=-2*BB*J0+4*BB*BB*J2
    uB=fB/f; umu=fmu/f
    uBB=fBB/f-uB*uB
    umuB=fmuB/f-umu*uB
    umumu=fmumu/f-umu*umu
    Iv=np.sum(w*np.log(f)); IB=np.sum(w*uB); IBB=np.sum(w*uBB)
    Kv=pp*np.sum(w*umu*umu)
    KB=2*pp*np.sum(w*umu*umuB)
    IBp=-KB/(2*pp)
    Kp=np.sum(w*umu*umu)+pp*np.sum(w*(umumu*umumu-2*umu*umu*umumu))
    Ip=-Kv/(2*pp)
    R=Kv/(-4*pp*pp*BB*BB*IB); DD=np.sqrt(R)
    Dp=.5*DD*(Kp/Kv-2/pp-IBp/IB)
    DB=.5*DD*(KB/Kv-2/BB-IBB/IB)
    cc,ccD,a0,a0p,a0D,ts,tsp,tsD,tsB,ccp=funcs(pp,DD,BB)
    alpha=-cc*cc/(4*BB*BB*IB)
    H=Iv-BB*IB-4*BB*BB*IB*a0
    Hp=Ip-BB*IBp-4*BB*BB*(IBp*a0+IB*(a0p+a0D*Dp))
    HB=-BB*IBB-8*BB*IB*a0-4*BB*BB*IBB*a0-4*BB*BB*IB*a0D*DB
    alphap=alpha*(2*(ccp+ccD*Dp)/cc-IBp/IB)
    alphaB=alpha*(2*ccD*DB/cc-2/BB-IBB/IB)
    S=cc*Iv/(4*BB*BB*IB); Psi=ts+S
    Psip=tsp+tsD*Dp+S*((ccp+ccD*Dp)/cc+Ip/Iv-IBp/IB)
    PsiB=tsB+tsD*DB+S*(ccD*DB/cc+IB/Iv-2/BB-IBB/IB)
    return dict(I=Iv,IB=IB,IBB=IBB,K=Kv,KB=KB,IBp=IBp,Kp=Kp,D=DD,Dp=Dp,DB=DB,
      alpha=alpha,H=H,Hp=Hp,HB=HB,alphap=alphap,alphaB=alphaB,
      Psi=Psi,Psip=Psip,PsiB=PsiB,umumu_max=float(np.max(umumu)))

v=scalar(P0,B0)
print('CENTER')
for k in ['H','alpha','Psi','D','Hp','HB','alphap','alphaB','Psip','PsiB','IBB','IBp','Kp','KB','umumu_max']:
    print(k,repr(float(v[k])))
assert v['umumu_max'] < 2e-13

for h in [1e-4,1e-5,1e-6]:
    vp=scalar(P0+h,B0); vm=scalar(P0-h,B0)
    vb=scalar(P0,B0+h); va=scalar(P0,B0-h)
    fdp=np.array([(vp[k]-vm[k])/(2*h) for k in ['H','alpha','Psi']])
    fdb=np.array([(vb[k]-va[k])/(2*h) for k in ['H','alpha','Psi']])
    ana_p=np.array([v[k] for k in ['Hp','alphap','Psip']])
    ana_b=np.array([v[k] for k in ['HB','alphaB','PsiB']])
    print('FD_CHECK',h,'p_err',float(np.max(abs(fdp-ana_p))),'B_err',float(np.max(abs(fdb-ana_b))))

pc=645767064689/1e12; bc=49292292009/1e10
keys=['Hp','HB','alphap','alphaB','Psip','PsiB','IBB','IBp','Kp','KB','D']
mins={k:1e100 for k in keys}; maxs={k:-1e100 for k in keys}
for pp in np.linspace(pc-.001,pc+.001,41):
    for bb in np.linspace(bc-.04,bc+.04,41):
        x=scalar(pp,bb)
        for k in keys:
            mins[k]=min(mins[k],float(x[k])); maxs[k]=max(maxs[k],float(x[k]))
print('ANALYTIC_DERIVATIVE_GRID_RANGES')
for k in keys: print(k,repr(mins[k]),repr(maxs[k]))

# Exact broad derivative-box contraction compiler from the R14 preconditioner.
A=[[F(-1601,20),F(-493,12500)],[F(-60418,25),F(-5789,2500)]]
d=[F(1,1000),F(1,25)]; di=[1/d[0],1/d[1]]
ranges=[(F(-7,250),F(-3,125)),(F(3,10000),F(3,5000)),
        (F(24),F(30)),(F(-1),F(-4,5))]
def mm(X,Y): return [[sum(X[i][k]*Y[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
def qvertex(hp,hb,ap,ab):
    AJ=mm(A,[[hp,hb],[ap,ab]])
    M=[[F(int(i==j))-AJ[i][j] for j in range(2)] for i in range(2)]
    S=[[di[i]*M[i][j]*d[j] for j in range(2)] for i in range(2)]
    return max(sum(abs(S[i][j]) for j in range(2)) for i in range(2))
qmax=max(qvertex(*x) for x in itertools.product(*ranges))
def eta(eh,ea): return max(di[i]*(abs(A[i][0])*eh+abs(A[i][1])*ea) for i in range(2))
e1=eta(F(1,10**8),F(1,10**6)); e2=eta(F(1,10**7),F(1,10**5))
print('EXACT_BROAD_CONTRACTION q',qmax,'=',float(qmax),'one_minus_q',1-qmax,'=',float(1-qmax))
print('EXACT_ETA_FINE',e1,'=',float(e1),'PASS',e1<1-qmax)
print('EXACT_ETA_COARSER',e2,'=',float(e2),'PASS',e2<1-qmax)
assert qmax==F(23849,25000) and e2 < 1-qmax

# Exact identity D^2 = E[m1^2]/(p E[m2]) checked numerically at the scout point.
def moment_ratio(pp,BB):
    s=np.sqrt(1-pp); mu=np.sqrt(pp)*z-1; AA=1+2*BB*s*s; a=mu/s; vv=mu/(s*np.sqrt(AA))
    phia=np.exp(-.5*a*a)/math.sqrt(2*math.pi)
    J0=np.exp(-BB*mu*mu/AA)/np.sqrt(AA)*ndtr(vv); f=ndtr(-a)+J0
    J1=(mu*J0+s*phia)/AA; J2=(mu*J1+s*s*J0)/AA
    m1=J1/f; m2=J2/f
    return np.sum(w*m1*m1)/(pp*np.sum(w*m2))
mr=moment_ratio(P0,B0)
print('D2_MOMENT_RATIO_CHECK',repr(float(mr)),repr(float(v['D']**2)),repr(float(abs(mr-v['D']**2))))
assert abs(mr-v['D']**2)<2e-14
print('ALL_CHECKS_PASS')
