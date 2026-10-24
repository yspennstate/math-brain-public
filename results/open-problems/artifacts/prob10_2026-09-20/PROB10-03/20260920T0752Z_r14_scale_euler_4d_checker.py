#!/usr/bin/env python3
"""
R14 PROB10-03 scale-Euler / four-scalar third-full checker.

EXACT sections use SymPy algebra only.
NUMERICAL_ONLY sections use Gauss-Hermite quadrature and scipy.root as a
falsification/sanity test. They are not rigorous bracket endpoints.
"""
import math
import sympy as sp
import numpy as np
from numpy.polynomial.hermite import hermgauss
from scipy.special import log_ndtr, logsumexp
from scipy.optimize import root

# ---------- EXACT CHECK 1: q-sector slope simplification ----------
p2,p3,r0,r1,r2 = sp.symbols("p2 p3 r0 r1 r2", positive=True)
sr = sp.sqrt(r2)
q3 = p3*r2
q2 = q3 + (p2-p3)*r1
c3 = (r1-r2)/((p2-p3)*r1*sr)
c2 = (r0*r2-r1**2)/((1-p2)*r0*r1*sr)
gp = sp.Rational(1,2)*r0*sr/r1
L2 = sp.simplify(c2*(1-p2*q2) + c3*(p2*q2-p3*q3) - 2*gp)
p3_on_constraint = (1-r0*(1-p2)-p2*r1)/(r2-r1)
identity1 = sp.factor(sp.simplify((L2 + r1/(r0*sr)).subs(p3,p3_on_constraint)))
assert identity1 == 0
print("EXACT_SLOPE_EULER_CONSTRAINT_PASS")

# ---------- EXACT CHECK 2: generic residual dependency ----------
# Abstract pattern values Q,QB,Qm; m=c3/c2. Use gamma stationarity:
# alpha*B*QB/c3 = -gs.
A0,E2,E3,gs,alpha,B,Q,QB,Qm,C2,C3 = sp.symbols(
    "A0 E2 E3 gs alpha B Q QB Qm C2 C3", nonzero=True)
m = C3/C2
Rcap = A0 + gs - alpha*Q/C3
Rc3 = E3/C3 + alpha*Q/C3**2 - alpha*Qm/(C2*C3)
Rc2 = E2/C2 - alpha*(B*QB-m*Qm)/(C3*C2)
dep = sp.expand(Rcap + C2*Rc2 + C3*Rc3)
dep_sub = sp.simplify(dep.subs(QB, -gs*C3/(alpha*B)))
assert sp.simplify(dep_sub - (A0+E2+E3+2*gs)) == 0
print("EXACT_RESIDUAL_DEPENDENCY_PASS")

# ---------- NUMERICAL_ONLY third-full implementation ----------
def gh(n):
    x,w = hermgauss(n)
    return np.sqrt(2.0)*x, w/np.sqrt(np.pi)

def reconstruct_q_sector(p2,p3,q2,q3):
    c3 = math.sqrt(p3/q3)/(p2-p3) - math.sqrt(q3/p3)/(q2-q3)
    gp = 0.5*(1-q2)/(1-p2)*(p2-p3)/(q2-q3)*math.sqrt(q3/p3)
    c2 = ((p2-p3)/(q2-q3)*math.sqrt(q3/p3))/(1-p2) \
         - ((q2-q3)/(p2-p3)*math.sqrt(p3/q3))/(1-q2)
    return c2,c3,gp

def kernel_moments(p2,p3,c2,c3,B,n):
    m=c3/c2
    U,wu=gh(n); V,wv=gh(n)
    logwu=np.log(wu)
    s2=1-p2; s=math.sqrt(s2)
    A=1+2*B*s2; rtA=math.sqrt(A)
    sd=math.sqrt(p2-p3); sp3=math.sqrt(p3)
    logphi0=-0.5*math.log(2*math.pi)
    Q=M1=M2=MB=QM=0.0
    for v,ov in zip(V,wv):
        x=sd*U+sp3*v-1.0
        a=x/s; b=x/(s*rtA)
        logt1=log_ndtr(-a)
        logt2=-0.5*math.log(A)-B*x*x/A+log_ndtr(b)
        logf=np.logaddexp(logt1,logt2)
        frac1=np.exp(logt1-logf); frac2=np.exp(logt2-logf)
        mills_mina=np.exp(logphi0-0.5*a*a-log_ndtr(-a))
        ux1=-mills_mina/s
        mills_b=np.exp(logphi0-0.5*b*b-log_ndtr(b))
        ux2=-2*B*x/A+mills_b/(s*rtA)
        ux=frac1*ux1+frac2*ux2
        uB2=-s2/A-x*x/(A*A)-x*s*(A**-1.5)*mills_b
        uB=frac2*uB2
        lt=logwu+m*logf
        lz=logsumexp(lt)
        tw=np.exp(lt-lz)
        mean_ux=float(np.dot(tw,ux))
        Q += ov*lz
        M1 += ov*mean_ux*mean_ux
        M2 += ov*float(np.dot(tw,ux*ux))
        MB += ov*(-float(np.dot(tw,uB)))
        QM += ov*float(np.dot(tw,logf))
    return dict(Q=float(Q),M1=float(M1),M2=float(M2),MB=float(MB),QM=float(QM),m=m)

def reconstruct_capacity_geometry(p2,p3,q2,q3):
    c2,c3,gp=reconstruct_q_sector(p2,p3,q2,q3)
    r2=q3/p3
    r1=(q2-q3)/(p2-p3)
    r0=(1-q2)/(1-p2)
    gap=r0*r2-r1*r1
    B=gap/(2*(1-p2)*r1*r1)
    gs=r1/(2*r0*math.sqrt(r2))
    return c2,c3,gp,r0,r1,r2,B,gs

def four_residual(x,n):
    p2,p3,q2,q3 = map(float,x)
    if not (0<p3<p2<1 and 0<q3<q2<1):
        return np.ones(4)*1e3
    try:
        c2,c3,gp,r0,r1,r2,B,gs=reconstruct_capacity_geometry(p2,p3,q2,q3)
        if not (c2>c3>0 and gp>0 and B>0 and gs>0):
            return np.ones(4)*1e3
        d=kernel_moments(p2,p3,c2,c3,B,n)
        alpha=c2*c2/(4*B*B*d["MB"])
        q3p=d["M1"]/(4*B*B*d["MB"])
        q2p=d["M2"]/(4*B*B*d["MB"])
        Aq=2*gp-c2*(1-q2)
        Dq=Aq-c3*(q2-q3)
        if not (Aq>0 and Dq>0):
            return np.ones(4)*1e3
        Ac3=(0.5*(p2*q2-p3*q3)
             -math.log(Dq/Aq)/(2*c3*c3)
             -(q2-q3)/(2*c3*Dq)
             -q3*(q2-q3)/(2*Dq*Dq))
        Ac2=(0.5*(1-p2*q2)
             -math.log(Aq/(2*gp))/(2*c2*c2)
             -(1-q2)/(2*c2*Aq)
             +(1-q2)/(2*c3)*(1/Aq-1/Dq)
             -q3*(1-q2)/(2*Dq*Dq))
        QB=-d["m"]*d["MB"]
        Qc2=(B*QB-d["m"]*d["QM"])/c2
        Rc3=Ac3+alpha*d["Q"]/(c3*c3)-alpha*d["QM"]/(c2*c3)
        Rc2=Ac2-alpha*Qc2/c3
        return np.array([q3-q3p,q2-q2p,Rc3,Rc2],float)
    except Exception:
        return np.ones(4)*1e3

def derived(x,n):
    p2,p3,q2,q3=map(float,x)
    c2,c3,gp,r0,r1,r2,B,gs=reconstruct_capacity_geometry(p2,p3,q2,q3)
    d=kernel_moments(p2,p3,c2,c3,B,n)
    alpha=c2*c2/(4*B*B*d["MB"])
    Aq=2*gp-c2*(1-q2); Dq=Aq-c3*(q2-q3)
    A0=(0.5*(1-p2*q2)*c2+0.5*(p2*q2-p3*q3)*c3-gp
        +math.log(Aq/(2*gp))/(2*c2)+math.log(Dq/Aq)/(2*c3)-q3/(2*Dq))
    psi=A0+gs-alpha*d["Q"]/c3
    return alpha,psi,B,gs

# Independent fixed-density point from NM13-03.
P3=0.599126773053267; P2=0.969080522852930
Q3=0.228731793616387; Q2=0.638442418504189
GS=0.0766524281089569
r2v=Q3/P3; r1v=(Q2-Q3)/(P2-P3); r0v=(1-Q2)/(1-P2)
rhs=2*GS-r1v/(r0v*math.sqrt(r2v))
print("NUMERICAL_ONLY_ALPHA12_288_SCALE_OBJECTIVE", format(rhs,".17g"))

x0=np.array([0.96908,0.5991,0.6384,0.2287],float)
last=None
for n in (60,80,100,120,160,200):
    sol=root(lambda x: four_residual(x,n),x0,method="hybr",
             options={"xtol":1e-12,"maxfev":1000})
    assert sol.success
    x0=sol.x
    alpha0,psi0,B0,gs0=derived(sol.x,n)
    mr=float(np.linalg.norm(four_residual(sol.x,n),np.inf))
    print("NUMERICAL_ONLY_GH",n,
          "p2",format(sol.x[0],".15g"),
          "p3",format(sol.x[1],".15g"),
          "q2",format(sol.x[2],".15g"),
          "q3",format(sol.x[3],".15g"),
          "alpha",format(alpha0,".15g"),
          "psi",format(psi0,".3e"),
          "maxres",format(mr,".3e"))
    last=sol.x.copy()

def num_jac(f,x,h=2e-6):
    n=len(x); J=np.zeros((n,n))
    for j in range(n):
        hh=h*max(1.0,abs(x[j]))
        xp=x.copy(); xm=x.copy()
        xp[j]+=hh; xm[j]-=hh
        J[:,j]=(f(xp)-f(xm))/(2*hh)
    return J

J=num_jac(lambda x: four_residual(x,160),last)
sv=np.linalg.svd(J,compute_uv=False)
print("NUMERICAL_ONLY_4D_JAC_SINGULAR_VALUES",*(format(v,".12g") for v in sv))
print("NUMERICAL_ONLY_4D_JAC_CONDITION",format(sv[0]/sv[-1],".12g"))
print("ALL_EXACT_CHECKS_PASS")
print("ALL_NUMERICAL_SANITY_CHECKS_PASS")
