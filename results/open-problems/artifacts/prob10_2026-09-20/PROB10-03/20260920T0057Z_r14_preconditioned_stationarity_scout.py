#!/usr/bin/env python3
"""
PROB10-03 / R14 self-check and numerical scout.

EXACT part:
  verifies the rational preconditioned-Newton compiler arithmetic.

NUMERICAL_ONLY parts:
  (1) Gauss-Hermite finite-difference scouting of the proposed Jacobian/Psi
      enclosure on the small alpha=12.75 box;
  (2) squared-polynomial Hermite-canceling SAT-weight scout.

Nothing numerical in this file is a rigorous bracket endpoint.
"""
import math, itertools
from fractions import Fraction as F
import numpy as np
import sympy as sp
from numpy.polynomial.hermite import hermgauss
from scipy.special import ndtr
from scipy.integrate import quad
from scipy.optimize import root, minimize_scalar
from math import comb

# ---------- exact rational preconditioner arithmetic ----------
A11,A12,A21,A22 = F(-1601,20),F(-493,12500),F(-60418,25),F(-5789,2500)
rp,rB = F(1,1000),F(1,25)
Jbounds = [
    [F(-131,5000),F(-63,2500)],
    [F(21,50000),F(23,50000)],
    [F(53,2),F(136,5)],
    [F(-23,25),F(-43,50)],
]
worst = None
for j11,j12,j21,j22 in itertools.product(*Jbounds):
    m11 = 1-(A11*j11+A12*j21)
    m12 = -(A11*j12+A12*j22)
    m21 = -(A21*j11+A22*j21)
    m22 = 1-(A21*j12+A22*j22)
    sm = (m11, m12*rB/rp, m21*rp/rB, m22)
    nrm = max(abs(sm[0])+abs(sm[1]),abs(sm[2])+abs(sm[3]))
    if worst is None or nrm>worst[0]:
        worst=(nrm,(j11,j12,j21,j22),sm)
q=worst[0]
assert q == F(215437,1250000)
epsH,epsAlpha=F(1,200000),F(1,1000)
eta1=(abs(A11)*epsH+abs(A12)*epsAlpha)/rp
eta2=(abs(A21)*epsH+abs(A22)*epsAlpha)/rB
eta=max(eta1,eta2)
assert eta == F(43969,100000)
assert eta < 1-q
print("EXACT_CONTRACTION_COMPILER_ARITHMETIC_PASS")
print("q =", q, float(q))
print("1-q =", 1-q, float(1-q))
print("eta =", eta, float(eta))
print("worst_J_vertex =", worst[1])
print("worst_scaled_matrix =", worst[2])

# ---------- exact source-matched second-full formulas, numerical evaluation ----------
pS,DS,BS,gS=sp.symbols('p D B g', positive=True)
qS=pS*DS**2
gpS=(1-qS)/(2*DS*(1-pS))
cS=(1-DS**2)/(DS*(1-pS)*(1-pS*DS**2))
TS=sp.Rational(1,2)*(1-pS*qS)*cS-gpS+sp.Rational(1,2)/cS*sp.log(DS/(2*gpS))-qS/(2*DS)+gS
TD=sp.diff(TS,DS).subs(gS,cS/(4*BS))
cD=sp.diff(cS,DS)
Tsub=TS.subs(gS,cS/(4*BS))
TDf=sp.lambdify((pS,DS,BS),TD,'numpy')
cDf=sp.lambdify((pS,DS),cD,'numpy')
Tsubf=sp.lambdify((pS,DS,BS),Tsub,'numpy')

def gh_factory(n):
    hn,hw=hermgauss(n)
    z=hn*np.sqrt(2.0); w=hw/np.sqrt(np.pi)
    def scalar(pp,BB):
        s=np.sqrt(1-pp); mu=np.sqrt(pp)*z-1.0
        AA=1+2*BB*s*s
        aa=mu/s; vv=mu/(s*np.sqrt(AA))
        phia=np.exp(-0.5*aa*aa)/math.sqrt(2*math.pi)
        Qv=np.exp(-BB*mu*mu/AA)/np.sqrt(AA)*ndtr(vv)
        f=ndtr(-aa)+Qv
        Iv=np.sum(w*np.log(f))
        fB=-(Qv*(mu*mu+s*s*AA)+mu*s*phia)/(AA*AA)
        IBv=np.sum(w*fB/f)
        fmu=-(2*BB/AA)*(mu*Qv+s*phia)
        Kv=np.sum(w*pp*(fmu/f)**2)
        D2=Kv/(-4*pp*pp*BB*BB*IBv)
        DD=np.sqrt(D2)
        cc=(1-DD*DD)/(DD*(1-pp)*(1-pp*DD*DD))
        alpha=-cc*cc/(4*BB*BB*IBv)
        H=Iv-BB*IBv-4*BB*BB*IBv*(TDf(pp,DD,BB)/cDf(pp,DD))
        Psi=Tsubf(pp,DD,BB)+cc*Iv/(4*BB*BB*IBv)
        return np.array([H,alpha,Psi,DD,Iv,IBv,Kv])
    return scalar

gh=gh_factory(260)
pc=0.645767064689
bc=4.9292292009
center=gh(pc,bc)
print("NUMERICAL_ONLY_CENTER",*(repr(float(x)) for x in center[:4]))

def deriv(pp,bb,hp=2e-6,hb=2e-5):
    vp=(gh(pp+hp,bb)-gh(pp-hp,bb))/(2*hp)
    vb=(gh(pp,bb+hb)-gh(pp,bb-hb))/(2*hb)
    return vp,vb

ranges={k:[float('inf'),-float('inf')] for k in ("Hp","HB","ap","aB","Pp","PB")}
max_scaled=0.0
A=np.array([[float(A11),float(A12)],[float(A21),float(A22)]])
Dmat=np.diag([float(rp),float(rB)])
Di=np.linalg.inv(Dmat)
for pp in np.linspace(pc-.001,pc+.001,9):
    for bb in np.linspace(bc-.04,bc+.04,9):
        vp,vb=deriv(pp,bb)
        cur={"Hp":vp[0],"HB":vb[0],"ap":vp[1],"aB":vb[1],"Pp":vp[2],"PB":vb[2]}
        for k,v in cur.items():
            ranges[k][0]=min(ranges[k][0],float(v))
            ranges[k][1]=max(ranges[k][1],float(v))
        J=np.array([[vp[0],vb[0]],[vp[1],vb[1]]],float)
        max_scaled=max(max_scaled,np.linalg.norm(Di@(np.eye(2)-A@J)@Dmat,np.inf))
print("NUMERICAL_ONLY_JACOBIAN_RANGES",ranges)
print("NUMERICAL_ONLY_SAMPLED_SCALED_CONTRACTION_MAX",repr(max_scaled))
assert ranges["Hp"][0]>-0.0262 and ranges["Hp"][1]<-0.0252
assert ranges["HB"][0]>0.00042 and ranges["HB"][1]<0.00046
assert ranges["ap"][0]>26.5 and ranges["ap"][1]<27.2
assert ranges["aB"][0]>-0.92 and ranges["aB"][1]<-0.86
assert abs(center[0])<5e-6 and abs(center[1]-12.75)<1e-3
assert center[2]>0.014
assert max(abs(ranges["Pp"][0]),abs(ranges["Pp"][1]))<2
assert max(abs(ranges["PB"][0]),abs(ranges["PB"][1]))<0.1
print("NUMERICAL_ONLY_BOX_SCOUT_PASS")

# ---------- distinct lower-side attack: squared polynomial weight ----------
SQRT2PI=math.sqrt(2*math.pi)
def phi(x): return math.exp(-0.5*x*x)/SQRT2PI

def wmom(a,b):
    def w(x): return (1+a*x+b*x*x)**2
    m0=quad(lambda x:w(x)*phi(x),-1,np.inf,epsabs=1e-11,epsrel=1e-11)[0]
    m1=quad(lambda x:w(x)*x*phi(x),-1,np.inf,epsabs=1e-11,epsrel=1e-11)[0]
    m2=quad(lambda x:w(x)*(x*x-1)*phi(x),-1,np.inf,epsabs=1e-11,epsrel=1e-11)[0]
    return m0,m1,m2

branches=[]
for guess in [(-.7,.4),(-.65,-.2)]:
    rr=root(lambda z:wmom(*z)[1:],guess,tol=1e-11)
    assert rr.success
    branches.append(tuple(float(t) for t in rr.x))

def coeff_w(a,b): return [1,2*a,a*a+2*b,2*a*b,b*b]
def Rstd(t):
    R=[ndtr(-t),phi(t),0,0,0]
    for j in range(2,5):
        R[j]=t**(j-1)*phi(t)+(j-1)*R[j-2]
    return R
def Ymoms(mu,s):
    t=(-1-mu)/s; R=Rstd(t); M=[]
    for k in range(5):
        M.append(sum(comb(k,j)*mu**(k-j)*s**j*R[j] for j in range(k+1)))
    return M
def eq(a,b,q):
    co=coeff_w(a,b); s=math.sqrt(1-q*q)
    def integrand(x):
        wx=(1+a*x+b*x*x)**2
        M=Ymoms(q*x,s)
        cond=sum(co[k]*M[k] for k in range(5))
        return wx*cond*phi(x)
    return quad(integrand,-1,np.inf,epsabs=3e-10,epsrel=3e-10,limit=200)[0]
def overlap_cap(a,b):
    m0=wmom(a,b)[0]
    def cap(q):
        lr=math.log(eq(a,b,q)/(m0*m0))
        return -0.5*math.log(1-q*q)/lr
    rr=minimize_scalar(cap,bounds=(1e-3,.995),method='bounded',options={'xatol':1e-8})
    return float(rr.x),float(rr.fun)

for a,b in branches:
    m0,m1,m2=wmom(a,b)
    qc,ac=overlap_cap(a,b)
    print("NUMERICAL_ONLY_OVERLAP_BRANCH",
          "a=",repr(a),"b=",repr(b),"m0=",repr(m0),
          "m1=",repr(m1),"m2=",repr(m2),
          "q_obstruction=",repr(qc),"alpha_obstruction=",repr(ac))
    assert abs(m1)<1e-8 and abs(m2)<1e-8
    assert ac < 6.30297437506
print("NUMERICAL_ONLY_OVERLAP_SCOUT_PASS")
print("ALL_SELF_CHECKS_PASS")
