#!/usr/bin/env python3
"""
NM13-07 / T03, 20 Sep 2026.

Two independent pieces:
(1) EXACT rational continuation of the already certified complete-second
    stationary branch from alpha=12.31963485 to 12.31963484.
(2) EXACT symbolic check of the prescribed-positive-gap third-full compiler,
    plus NUMERICAL_ONLY Gauss-Hermite scouts at gap delta=1/1000.

The numerical third-full section is falsification/conditioning evidence only.
It is NOT used for the rigorous source endpoint in (1).
"""
from fractions import Fraction as F
import itertools, math
import sympy as sp
import numpy as np
from numpy.polynomial.hermite import hermgauss
from scipy.special import log_ndtr, logsumexp
from scipy.optimize import root

# -------------------------------------------------------------------------
# PART A. Exact complete-second microcontinuation.
# These whole-box derivative ranges, rational preconditioner, center
# residual bounds, and anchor objective lower bound are inherited from the
# already archived directed-interval certificate at alpha0=12.319635.
# -------------------------------------------------------------------------
Aq = [[F(-7294853,100000), F(-504965,10000000)],
      [F(-3028867,1000), F(-3758826,1000000)]]
dr = [F(1,10_000_000), F(1,250_000)]
ranges = [
    (F(-34,1000), F(-28,1000)),          # H_p
    (F(32,100000), F(51,100000)),        # H_B
    (F(246,10), F(254,10)),              # alpha_p
    (F(-603,1000), F(-600,1000)),        # alpha_B
]

def mm(X,Y):
    return [[sum(X[i][k]*Y[k][j] for k in range(2))
             for j in range(2)] for i in range(2)]

def qvertex(hp,hb,ap,ab):
    AJ = mm(Aq, [[hp,hb],[ap,ab]])
    M = [[F(int(i==j))-AJ[i][j] for j in range(2)] for i in range(2)]
    return max(sum(abs(F(1,dr[i])*M[i][j]*dr[j]) for j in range(2))
               for i in range(2))

QCON = max(qvertex(*v) for v in itertools.product(*ranges))
assert QCON == F(70497781,125000000)

# Old certified center errors:
# |H_c| < 4.7e-12, |alpha_c-12.319635| < 3.7e-11.
# New target is lower by 1.6e-7; EA=1.601e-7 safely includes center error.
EH = F(47,10**13)
EA = F(1601,10**10)
ETA = max(F(1,dr[i])*(abs(Aq[i][0])*EH + abs(Aq[i][1])*EA)
          for i in range(2))
RHO = ETA/(1-QCON)
assert ETA == F(246409487,1600000000)
assert ETA < 1-QCON
assert RHO < 1

# Inherited exact envelope bound dPsi/dalpha < 2/15 on the same whole box.
slope_ub = F(2,15)
psi_anchor_lb = F(23584189005311,1090044380000000000000)
delta_alpha = F(16,100_000_000)  # 1.6e-7
psi_new_lb = psi_anchor_lb - slope_ub*delta_alpha
assert psi_new_lb == F(989726695933,3270133140000000000000)
assert psi_new_lb > 0

alpha0 = F(12319635,1000000)     # 12.319635
alpha1 = alpha0-delta_alpha      # 12.31963484
alphaL = F(315148718753,50000000000)  # 6.30297437506
assert alpha1 == F(307990871,25000000)
width_before = F(246392697,20000000)-alphaL  # prior 12.31963485 endpoint
width_after = alpha1-alphaL
source_gain = F(246392697,20000000)-alpha1
assert source_gain == F(1,100000000)

print("EXACT_MICROCONTINUATION")
print("Q_CONTRACTION", QCON, float(QCON))
print("ETA", ETA, float(ETA))
print("RHO", RHO, float(RHO))
print("PSI_ANCHOR_LOWER", psi_anchor_lb, float(psi_anchor_lb))
print("DELTA_ALPHA_FROM_ANCHOR", delta_alpha, float(delta_alpha))
print("PSI_NEW_LOWER", psi_new_lb, float(psi_new_lb))
print("RIGOROUS_ALPHA_U_BEFORE", 12.31963485)
print("RIGOROUS_ALPHA_U_AFTER", float(alpha1))
print("SOURCE_GAIN_FROM_PRIOR_ENDPOINT", source_gain, float(source_gain))
print("BRACKET_WIDTH_BEFORE", float(width_before))
print("BRACKET_WIDTH_AFTER", float(width_after))
print("EXACT_MICROCONTINUATION_PASS")

# -------------------------------------------------------------------------
# PART B. Exact algebra: prescribed positive-gap four-overlap compiler.
# Let S=r1/(r0 sqrt(r2)).  At full stationarity the scale-Euler identity is
# Psi3 = 2 gamma_sq-S.  Prescribe a positive gap DEL and reconstruct
# gamma_sq=(S+DEL)/2, B=c2/(4 gamma_sq).
# The generic residual dependency from the source objective is
# Psi3 + c2*Rc2 + c3*Rc3 = 2 gamma_sq-S
# after gamma_sq stationarity.  Hence if Rc2=Rc3=0, Psi3=DEL exactly.
# -------------------------------------------------------------------------
C2,C3,GS,S,DEL,PSI,RC2,RC3 = sp.symbols(
    "C2 C3 GS S DEL PSI RC2 RC3", nonzero=True)
identity = sp.expand(PSI + C2*RC2 + C3*RC3 - (2*GS-S))
reduced = sp.simplify(identity.subs(GS,(S+DEL)/2).subs({RC2:0,RC3:0,PSI:DEL}))
assert reduced == 0
print("EXACT_POSITIVE_GAP_SCALE_IDENTITY_PASS")

# -------------------------------------------------------------------------
# NUMERICAL_ONLY scout for DEL=1/1000, using the exact score/moment residual
# formulas proved in the preceding NM13-07 report.
# -------------------------------------------------------------------------
DELTA = 1e-3

def gh(n):
    x,w=hermgauss(n)
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
        ux2=-2*B*x/A + mills_b/(s*rtA)
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
    return dict(Q=float(Q),M1=float(M1),M2=float(M2),
                MB=float(MB),QM=float(QM),m=m)

def posgap_geometry(p2,p3,q2,q3,delta):
    c2,c3,gp=reconstruct_q_sector(p2,p3,q2,q3)
    r2=q3/p3
    r1=(q2-q3)/(p2-p3)
    r0=(1-q2)/(1-p2)
    S=r1/(r0*math.sqrt(r2))
    gs=0.5*(S+delta)
    B=c2/(4*gs)
    return c2,c3,gp,r0,r1,r2,S,B,gs

def four_residual_gap(x,delta,n):
    p2,p3,q2,q3=map(float,x)
    if not (0<p3<p2<1 and 0<q3<q2<1):
        return np.ones(4)*1e3
    try:
        c2,c3,gp,r0,r1,r2,S,B,gs=posgap_geometry(p2,p3,q2,q3,delta)
        if not (c2>c3>0 and gp>0 and B>0 and gs>0):
            return np.ones(4)*1e3
        d=kernel_moments(p2,p3,c2,c3,B,n)
        alpha=c2*c2/(4*B*B*d["MB"])
        q3p=d["M1"]/(4*B*B*d["MB"])
        q2p=d["M2"]/(4*B*B*d["MB"])
        Aq0=2*gp-c2*(1-q2)
        Dq=Aq0-c3*(q2-q3)
        if not (Aq0>0 and Dq>0):
            return np.ones(4)*1e3
        Ac3=(0.5*(p2*q2-p3*q3)
             -math.log(Dq/Aq0)/(2*c3*c3)
             -(q2-q3)/(2*c3*Dq)
             -q3*(q2-q3)/(2*Dq*Dq))
        Ac2=(0.5*(1-p2*q2)
             -math.log(Aq0/(2*gp))/(2*c2*c2)
             -(1-q2)/(2*c2*Aq0)
             +(1-q2)/(2*c3)*(1/Aq0-1/Dq)
             -q3*(1-q2)/(2*Dq*Dq))
        QB=-d["m"]*d["MB"]
        Qc2=(B*QB-d["m"]*d["QM"])/c2
        Rc3=Ac3+alpha*d["Q"]/(c3*c3)-alpha*d["QM"]/(c2*c3)
        Rc2=Ac2-alpha*Qc2/c3
        return np.array([q3-q3p,q2-q2p,Rc3,Rc2],float)
    except Exception:
        return np.ones(4)*1e3

def derived_gap(x,delta,n):
    p2,p3,q2,q3=map(float,x)
    c2,c3,gp,r0,r1,r2,S,B,gs=posgap_geometry(p2,p3,q2,q3,delta)
    d=kernel_moments(p2,p3,c2,c3,B,n)
    alpha=c2*c2/(4*B*B*d["MB"])
    Aq0=2*gp-c2*(1-q2); Dq=Aq0-c3*(q2-q3)
    A0=(0.5*(1-p2*q2)*c2+0.5*(p2*q2-p3*q3)*c3-gp
        +math.log(Aq0/(2*gp))/(2*c2)
        +math.log(Dq/Aq0)/(2*c3)-q3/(2*Dq))
    psi=A0+gs-alpha*d["Q"]/c3
    return dict(alpha=alpha,psi=psi,B=B,gs=gs,c2=c2,c3=c3,gp=gp,
                Q=d["Q"],MB=d["MB"],S=S)

def num_jac(f,x,h=1e-6):
    x=np.array(x,float); n=len(x); J=np.zeros((n,n))
    for j in range(n):
        hh=h*max(1.0,abs(x[j]))
        xp=x.copy(); xm=x.copy(); xp[j]+=hh; xm[j]-=hh
        J[:,j]=(f(xp)-f(xm))/(2*hh)
    return J

seed=np.array([0.96783,0.59772,0.63866,0.22992],float)
last=None
for n in (60,80,100,120,160,200):
    sol=root(lambda z:four_residual_gap(z,DELTA,n),seed,
             method="hybr",tol=1e-11,options={"maxfev":1000})
    assert sol.success
    d=derived_gap(sol.x,DELTA,n)
    J=num_jac(lambda z:four_residual_gap(z,DELTA,n),sol.x)
    sv=np.linalg.svd(J,compute_uv=False)
    print("NUMERICAL_ONLY_POSGAP", n,
          "alpha", format(d["alpha"],".15g"),
          "psi", format(d["psi"],".15g"),
          "maxres", format(np.max(np.abs(sol.fun)),".3e"),
          "sigma_min", format(sv[-1],".12g"),
          "cond", format(sv[0]/sv[-1],".12g"),
          "p2", format(sol.x[0],".15g"),
          "p3", format(sol.x[1],".15g"),
          "q2", format(sol.x[2],".15g"),
          "q3", format(sol.x[3],".15g"))
    seed=sol.x
    last=(sol.x.copy(),d)

x,d=last
print("NUMERICAL_ONLY_DELTA", DELTA)
print("NUMERICAL_ONLY_ALPHA_IF_CERTIFIED", format(d["alpha"],".17g"))
print("NUMERICAL_ONLY_IMPROVEMENT_VS_NEW_RIGOROUS",
      format(float(alpha1)-d["alpha"],".17g"))
print("NUMERICAL_ONLY_B", format(d["B"],".17g"))
print("NUMERICAL_ONLY_GAMMA_SQ", format(d["gs"],".17g"))
print("NUMERICAL_ONLY_C2", format(d["c2"],".17g"))
print("NUMERICAL_ONLY_C3", format(d["c3"],".17g"))
print("NUMERICAL_ONLY_GAMMA_P", format(d["gp"],".17g"))
print("ALL_EXACT_CHECKS_PASS")
print("ALL_NUMERICAL_SCOUTS_PASS")
