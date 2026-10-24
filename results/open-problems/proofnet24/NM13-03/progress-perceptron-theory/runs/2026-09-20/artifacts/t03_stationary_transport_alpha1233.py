#!/usr/bin/env python3
"""NM13-03 T03 stationary-branch transport scout for alpha=12.33.

Mathematical theorem in the companion report:
on a C^1 stationary branch H=0 with alpha as coordinate and nonzero
Jacobian determinant Delta=H_p alpha_B-H_B alpha_p,
  dp/dalpha=-H_B/Delta,
  dB/dalpha=H_p/Delta,
  dPsi/dalpha=(H_p Psi_B-H_B Psi_p)/Delta.
Hence an upper bound on dPsi/dalpha transports positive comparison value
from one certified stationary point to a lower density.

This executable is NUMERICAL SUPPORT, not an outward-rounded proof.
It:
  * continues the complete-second-lift stationary root from alpha=12.75 to 12.33;
  * cross-checks Gauss-Hermite orders 200 and 260;
  * finite-difference checks Delta and dPsi/dalpha on 43 branch points;
  * exhibits a small Poincare-Miranda rectangle at alpha=12.33;
  * cross-checks endpoint center/corners by adaptive quadrature;
  * verifies an exact rational transport margin from the proposed hypotheses
      Psi(12.75)>=0.01519, dPsi/dalpha<=0.0354.
"""
from fractions import Fraction as Q
import math
import numpy as np
import sympy as sp
from numpy.polynomial.hermite import hermgauss
from scipy.integrate import quad
from scipy.optimize import root
from scipy.special import ndtr

ALPHA_ANCHOR=12.75
ALPHA_TARGET=12.33
ALPHA_L=6.30297437506
ALPHA_OLD=12.78437096216

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

def grads(scalar,pp,bb,hp=1e-5,hb=1e-4):
    vp=(scalar(pp+hp,bb)-scalar(pp-hp,bb))/(2*hp)
    vb=(scalar(pp,bb+hb)-scalar(pp,bb-hb))/(2*hb)
    return float(vp),float(vb)

x=np.array([0.6457670646889506,4.929229200895245])
rows=[]
for aa in np.linspace(ALPHA_ANCHOR,ALPHA_TARGET,43):
    rr=root(lambda xx:[gh260(xx[0],xx[1])[0],gh260(xx[0],xx[1])[1]-aa],x,tol=1e-12)
    assert rr.success
    x=rr.x
    v=gh260(*x)
    v2=gh200(*x)
    Hp,Hb=grads(lambda pp,bb:gh260(pp,bb)[0],*x)
    ap,ab=grads(lambda pp,bb:gh260(pp,bb)[1],*x)
    Pp,Pb=grads(lambda pp,bb:gh260(pp,bb)[2],*x)
    det=Hp*ab-Hb*ap
    dP=(Hp*Pb-Hb*Pp)/det
    disc=float(np.max(np.abs(v[:3]-v2[:3])))
    rows.append((aa,float(x[0]),float(x[1]),float(v[2]),Hp,Hb,ap,ab,Pp,Pb,det,dP,disc))

R=np.array(rows,float)
print("BRANCH alpha_range",repr(float(R[:,0].min())),repr(float(R[:,0].max())))
labels=["p","B","Psi","H_p","H_B","alpha_p","alpha_B","Psi_p","Psi_B","Delta","dPsi_dalpha","GHdisc"]
for j,lab in enumerate(labels,1):
    print("BRANCH_RANGE",lab,repr(float(R[:,j].min())),repr(float(R[:,j].max())))
assert R[:,10].min()>0.008
assert R[:,11].min()>0.0352 and R[:,11].max()<0.0354
assert R[:,12].max()<1e-11
assert rows[0][3]>0.01519

psi_anchor_lb=Q(1519,100000)
slope_ub=Q(177,5000)
delta_alpha=Q(42,100)
transport_lb=psi_anchor_lb-slope_ub*delta_alpha
print("EXACT_TRANSPORT psi_anchor_lb",psi_anchor_lb,float(psi_anchor_lb))
print("EXACT_TRANSPORT slope_ub",slope_ub,float(slope_ub))
print("EXACT_TRANSPORT delta_alpha",delta_alpha,float(delta_alpha))
print("EXACT_TRANSPORT target_Psi_lb",transport_lb,float(transport_lb))
assert transport_lb==Q(161,500000) and transport_lb>0

pt=np.array([rows[-1][1],rows[-1][2]])
v0=gh260(*pt)
print("TARGET_ROOT",repr(float(pt[0])),repr(float(pt[1])))
print("TARGET_DATA H alpha Psi D",*(repr(float(t)) for t in v0[:4]))
assert abs(v0[0])<1e-11 and abs(v0[1]-ALPHA_TARGET)<1e-10 and v0[2]>3.6e-4

DP=5e-5
DB=0.00275
pm,pM=pt[0]-DP,pt[0]+DP
bm,bM=pt[1]-DB,pt[1]+DB
corner={
    "LB":gh260(pm,bm),
    "LT":gh260(pm,bM),
    "RB":gh260(pM,bm),
    "RT":gh260(pM,bM),
}
for k,v in corner.items():
    print("CORNER",k,"H",repr(float(v[0])),"alpha_minus_target",repr(float(v[1]-ALPHA_TARGET)),"Psi",repr(float(v[2])))
assert corner["LB"][0]>3.8e-7
assert corner["RT"][0]<-3.8e-7
assert corner["LB"][1]-ALPHA_TARGET>4.0e-4
assert corner["RT"][1]-ALPHA_TARGET<-4.0e-4

Hb_min=1e9
ap_min=1e9
psi_min=1e9
deriv_cross_disc=0.0
for pp in np.linspace(pm,pM,11):
    for bb in np.linspace(bm,bM,11):
        Hb260=grads(lambda x,y:gh260(x,y)[0],pp,bb)[1]
        ap260=grads(lambda x,y:gh260(x,y)[1],pp,bb)[0]
        Hb200=grads(lambda x,y:gh200(x,y)[0],pp,bb)[1]
        ap200=grads(lambda x,y:gh200(x,y)[1],pp,bb)[0]
        Hb_min=min(Hb_min,Hb260)
        ap_min=min(ap_min,ap260)
        psi_min=min(psi_min,float(gh260(pp,bb)[2]))
        deriv_cross_disc=max(deriv_cross_disc,abs(Hb260-Hb200),abs(ap260-ap200))
print("BOX_SCOUT H_B_min alpha_p_min Psi_min derivative_cross_order_discrepancy",
      repr(Hb_min),repr(ap_min),repr(psi_min),repr(deriv_cross_disc))
assert Hb_min>4.0e-4 and ap_min>24.0 and psi_min>2.5e-4
assert deriv_cross_disc<1e-8

def quad_scalar(pp,BB):
    s=math.sqrt(1-pp); rp=math.sqrt(pp)
    def terms(z):
        mu=rp*z-1
        A=1+2*BB*s*s
        a=mu/s
        vv=mu/(s*math.sqrt(A))
        phia=math.exp(-.5*a*a)/math.sqrt(2*math.pi)
        Qv=math.exp(-BB*mu*mu/A)/math.sqrt(A)*ndtr(vv)
        f=ndtr(-a)+Qv
        fB=-(Qv*(mu*mu+s*s*A)+mu*s*phia)/(A*A)
        fmu=-(2*BB/A)*(mu*Qv+s*phia)
        den=math.exp(-z*z/2)/math.sqrt(2*math.pi)
        return math.log(f)*den,(fB/f)*den,pp*(fmu/f)**2*den
    vv=[]; ee=[]
    for k in range(3):
        val,err=quad(lambda zz:terms(zz)[k],-9,9,epsabs=2e-13,epsrel=2e-13,limit=500)
        vv.append(val); ee.append(err)
    Iv,IBv,Kv=vv
    DD=math.sqrt(Kv/(-4*pp*pp*BB*BB*IBv))
    cc=(1-DD*DD)/(DD*(1-pp)*(1-pp*DD*DD))
    aa=-cc*cc/(4*BB*BB*IBv)
    H=Iv-BB*IBv-4*BB*BB*IBv*(TDf(pp,DD,BB)/cDf(pp,DD))
    Psi=Tsubf(pp,DD,BB)+cc*Iv/(4*BB*BB*IBv)
    return np.array([H,aa,Psi,DD]),max(ee)

maxdiff=0.0
maxerr=0.0
for pp,bb in [tuple(pt),(pm,bm),(pm,bM),(pM,bm),(pM,bM)]:
    qv,qe=quad_scalar(pp,bb)
    gv=gh260(pp,bb)[:4]
    maxdiff=max(maxdiff,float(np.max(np.abs(qv-gv))))
    maxerr=max(maxerr,float(qe))
print("ADAPTIVE_CROSSCHECK max_abs_diff max_reported_error",repr(maxdiff),repr(maxerr))
assert maxdiff<3e-12 and maxerr<3e-12

print("SUPPORTED_CANDIDATE_ALPHA_U",ALPHA_TARGET)
print("SUPPORTED_CANDIDATE_WIDTH",repr(ALPHA_TARGET-ALPHA_L))
print("IMPROVEMENT_VS_RIGOROUS_OLD_UPPER",repr(ALPHA_OLD-ALPHA_TARGET))
print("IMPROVEMENT_VS_PREVIOUS_12P75_CANDIDATE",repr(ALPHA_ANCHOR-ALPHA_TARGET))
print("ALL_NUMERICAL_SUPPORT_CHECKS_PASS")
