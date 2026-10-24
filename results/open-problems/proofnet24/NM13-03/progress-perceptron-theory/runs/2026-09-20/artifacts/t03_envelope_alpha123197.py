#!/usr/bin/env python3
"""NM13-03 T03 envelope-theorem scout for alpha=12.3197.

NUMERICAL SUPPORT ONLY, not outward-rounded certification.
Checks the exact-stationary-branch envelope identity dPsi/dalpha=-I/c
numerically, continues the full second-lift branch from 12.75 to 12.3197,
verifies a piecewise rational transport margin, and builds a small
Poincare-Miranda-style endpoint rectangle.
"""
from fractions import Fraction as Q
import math
import numpy as np
import sympy as sp
from numpy.polynomial.hermite import hermgauss
from scipy.optimize import root
from scipy.special import ndtr

ALPHA_ANCHOR=12.75
ALPHA_TARGET=12.3197
ALPHA_L=6.30297437506
ALPHA_OLD_CAND=12.33

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

def gh_factory(n):
    hn,hw=hermgauss(n)
    z=hn*np.sqrt(2.0)
    w=hw/np.sqrt(np.pi)
    def scalar(pp,BB):
        s=np.sqrt(1-pp)
        mu=np.sqrt(pp)*z-1.0
        A=1+2*BB*s*s
        a=mu/s
        v=mu/(s*np.sqrt(A))
        phia=np.exp(-0.5*a*a)/math.sqrt(2*math.pi)
        J0=np.exp(-BB*mu*mu/A)/np.sqrt(A)*ndtr(v)
        f=ndtr(-a)+J0
        Iv=np.sum(w*np.log(f))
        fB=-(J0*(mu*mu+s*s*A)+mu*s*phia)/(A*A)
        IBv=np.sum(w*fB/f)
        fmu=-(2*BB/A)*(mu*J0+s*phia)
        Kv=np.sum(w*pp*(fmu/f)**2)
        D2=Kv/(-4*pp*pp*BB*BB*IBv)
        DD=np.sqrt(D2)
        cc=(1-DD*DD)/(DD*(1-pp)*(1-pp*DD*DD))
        aa=-cc*cc/(4*BB*BB*IBv)
        H=Iv-BB*IBv-4*BB*BB*IBv*(TDf(pp,DD,BB)/cDf(pp,DD))
        Psi=Tsubf(pp,DD,BB)+cc*Iv/(4*BB*BB*IBv)
        env=-Iv/cc
        return np.array([H,aa,Psi,DD,Iv,IBv,Kv,cc,env])
    return scalar

gh200=gh_factory(200)
gh260=gh_factory(260)

def grads(scalar,pp,bb,hp=1e-5,hb=1e-4):
    vp=(scalar(pp+hp,bb)-scalar(pp-hp,bb))/(2*hp)
    vb=(scalar(pp,bb+hb)-scalar(pp,bb-hb))/(2*hb)
    return float(vp),float(vb)

# Dense descending continuation.
x=np.array([0.6457670646889506,4.929229200895245])
grid=np.linspace(ALPHA_ANCHOR,ALPHA_TARGET,862)
rows=[]
for aa in grid:
    rr=root(lambda xx:[gh260(xx[0],xx[1])[0],gh260(xx[0],xx[1])[1]-aa],x,tol=1e-12)
    assert rr.success
    x=rr.x
    v=gh260(*x); v2=gh200(*x)
    rows.append((aa,float(x[0]),float(x[1]),float(v[2]),float(v[4]),float(v[7]),float(v[8]),float(np.max(np.abs(v[:5]-v2[:5])))))
R=np.array(rows,float)
print('BRANCH alpha_min alpha_max',repr(float(R[:,0].min())),repr(float(R[:,0].max())))
print('BRANCH p_range',repr(float(R[:,1].min())),repr(float(R[:,1].max())))
print('BRANCH B_range',repr(float(R[:,2].min())),repr(float(R[:,2].max())))
print('BRANCH Psi_range',repr(float(R[:,3].min())),repr(float(R[:,3].max())))
print('BRANCH envelope_rate_range',repr(float(R[:,6].min())),repr(float(R[:,6].max())))
print('BRANCH GH200_260_max_discrepancy',repr(float(R[:,7].max())))
assert R[:,6].min()>0
assert R[:,6].max()<0.035342
assert R[:,7].max()<1e-11

# Independent numerical check of envelope identity at selected branch points:
# finite-difference Psi along the actual stationary branch vs -I/c.
max_env_fd=0.0
for aa in np.linspace(ALPHA_TARGET+0.01,ALPHA_ANCHOR-0.01,13):
    h=1e-5
    r0=root(lambda xx:[gh260(xx[0],xx[1])[0],gh260(xx[0],xx[1])[1]-aa],[0.655,5.6],tol=1e-12); assert r0.success
    rp=root(lambda xx:[gh260(xx[0],xx[1])[0],gh260(xx[0],xx[1])[1]-(aa+h)],r0.x,tol=1e-12); assert rp.success
    rm=root(lambda xx:[gh260(xx[0],xx[1])[0],gh260(xx[0],xx[1])[1]-(aa-h)],r0.x,tol=1e-12); assert rm.success
    fd=(gh260(*rp.x)[2]-gh260(*rm.x)[2])/(2*h)
    env=gh260(*r0.x)[8]
    max_env_fd=max(max_env_fd,abs(fd-env))
print('ENVELOPE_IDENTITY max_abs_fd_minus_minusI_over_c',repr(max_env_fd))
assert max_env_fd<5e-9

# Piecewise envelope caps. These are deliberately rounded upward relative to
# the dense numerical scout; the theorem says that *if outward certified* on
# each interval, they imply the displayed exact rational positivity margin.
pieces=[
(Q(123197,10000),Q(123697,10000),Q(353414,10000000)),
(Q(123697,10000),Q(124197,10000),Q(353414,10000000)),
(Q(124197,10000),Q(124697,10000),Q(353402,10000000)),
(Q(124697,10000),Q(125197,10000),Q(353364,10000000)),
(Q(125197,10000),Q(125697,10000),Q(353302,10000000)),
(Q(125697,10000),Q(126197,10000),Q(353218,10000000)),
(Q(126197,10000),Q(126697,10000),Q(353113,10000000)),
(Q(126697,10000),Q(127197,10000),Q(352989,10000000)),
(Q(127197,10000),Q(51,4),Q(352846,10000000)),
]
for lo,hi,cap in pieces:
    lof=float(lo); hif=float(hi)
    mask=(R[:,0]>=lof-1e-13)&(R[:,0]<=hif+1e-13)
    obs=float(R[mask,6].max())
    print('PIECE',str(lo),str(hi),'observed_max',repr(obs),'rational_cap',str(cap),float(cap))
    assert obs < float(cap)
anchor_lb=Q(152009,10000000)
loss=sum((hi-lo)*cap for lo,hi,cap in pieces)
transport_lb=anchor_lb-loss
print('EXACT_PIECEWISE_TRANSPORT anchor_lb',str(anchor_lb),float(anchor_lb))
print('EXACT_PIECEWISE_TRANSPORT loss_ub',str(loss),float(loss))
print('EXACT_PIECEWISE_TRANSPORT target_Psi_lb',str(transport_lb),float(transport_lb))
assert transport_lb==Q(34831,50000000000) and transport_lb>0
assert rows[0][3]>float(anchor_lb)

# Direct endpoint reconstruction.
rr=root(lambda xx:[gh260(xx[0],xx[1])[0],gh260(xx[0],xx[1])[1]-ALPHA_TARGET],x,tol=1e-12); assert rr.success
pt=rr.x; v0=gh260(*pt); v02=gh200(*pt)
print('TARGET_ROOT p B',repr(float(pt[0])),repr(float(pt[1])))
print('TARGET_DATA H alpha Psi D I c envelope',*(repr(float(t)) for t in [v0[0],v0[1],v0[2],v0[3],v0[4],v0[7],v0[8]]))
print('TARGET_GH200_260_MAXDIFF',repr(float(np.max(np.abs(v0[:5]-v02[:5])))))
assert abs(v0[0])<1e-11 and abs(v0[1]-ALPHA_TARGET)<1e-10 and v0[2]>2.3e-6

# Small endpoint root rectangle. Positivity of Psi is transported from the
# anchor, so Psi need not have one sign on the entire rectangle.
DP=1e-5; DB=0.00055
pm,pM=pt[0]-DP,pt[0]+DP; bm,bM=pt[1]-DB,pt[1]+DB
corner={
 'LB':gh260(pm,bm),'LT':gh260(pm,bM),'RB':gh260(pM,bm),'RT':gh260(pM,bM)
}
for k,v in corner.items():
    print('CORNER',k,'H',repr(float(v[0])),'alpha_minus_target',repr(float(v[1]-ALPHA_TARGET)),'Psi',repr(float(v[2])))
assert corner['LB'][0]>7e-8 and corner['RT'][0]<-7e-8
assert corner['LB'][1]-ALPHA_TARGET>7e-5 and corner['RT'][1]-ALPHA_TARGET<-7e-5
Hb_min=1e9; ap_min=1e9; deriv_disc=0.0
for pp in np.linspace(pm,pM,9):
  for bb in np.linspace(bm,bM,9):
    Hb260=grads(lambda xx,yy:gh260(xx,yy)[0],pp,bb)[1]
    ap260=grads(lambda xx,yy:gh260(xx,yy)[1],pp,bb)[0]
    Hb200=grads(lambda xx,yy:gh200(xx,yy)[0],pp,bb)[1]
    ap200=grads(lambda xx,yy:gh200(xx,yy)[1],pp,bb)[0]
    Hb_min=min(Hb_min,Hb260); ap_min=min(ap_min,ap260)
    deriv_disc=max(deriv_disc,abs(Hb260-Hb200),abs(ap260-ap200))
print('BOX_SCOUT H_B_min alpha_p_min derivative_cross_order_discrepancy',repr(Hb_min),repr(ap_min),repr(deriv_disc))
assert Hb_min>4e-4 and ap_min>24.0 and deriv_disc<1e-8

print('SUPPORTED_CANDIDATE_ALPHA_U',ALPHA_TARGET)
print('SUPPORTED_CANDIDATE_WIDTH',repr(ALPHA_TARGET-ALPHA_L))
print('IMPROVEMENT_VS_12P33_CANDIDATE',repr(ALPHA_OLD_CAND-ALPHA_TARGET))
print('ALL_NUMERICAL_SUPPORT_CHECKS_PASS')
