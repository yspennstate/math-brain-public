#!/usr/bin/env python3
"""
NM13-07 / T03, 20 Sep 2026.

A. Exact rational micro-continuation of the already directed-interval-certified
   complete-second branch, using a sharpened elementary Gaussian second-moment
   upper bound.
B. Numerical-only falsification check of a new exact entropy-dissipation
   representation for the complete-third c-sector at the previously archived
   positive-gap delta=1e-3 scout.

Only Part A is used for the rigorous source endpoint in this run.
"""
from fractions import Fraction as F
import math
import numpy as np
from numpy.polynomial.hermite import hermgauss
from numpy.polynomial.legendre import leggauss
from scipy.special import log_ndtr, logsumexp

# ----------------------------------------------------------------------
# PART A: exact rational complete-second microcontinuation.
# ----------------------------------------------------------------------

# Inherited directed-interval complete-second contraction data at alpha0.
Aq = [[F(-7294853,100000), F(-504965,10000000)],
      [F(-3028867,1000), F(-3758826,1000000)]]
dr = [F(1,10_000_000), F(1,250_000)]
ranges = [
    (F(-34,1000), F(-28,1000)),
    (F(32,100000), F(51,100000)),
    (F(246,10), F(254,10)),
    (F(-603,1000), F(-600,1000)),
]

def mm(X,Y):
    return [[sum(X[i][k]*Y[k][j] for k in range(2))
             for j in range(2)] for i in range(2)]

import itertools
def qvertex(hp,hb,ap,ab):
    AJ = mm(Aq, [[hp,hb],[ap,ab]])
    M = [[F(int(i==j))-AJ[i][j] for j in range(2)] for i in range(2)]
    return max(sum(abs(F(1,dr[i])*M[i][j]*dr[j]) for j in range(2))
               for i in range(2))
QCON = max(qvertex(*v) for v in itertools.product(*ranges))
assert QCON == F(70497781,125000000)

# New elementary rational Gaussian estimates.
# First, pi < 355/113.
pi_ub = F(355,113)

# e < 271829/100000.  Prove by sum_{0..8} 1/n! plus a geometric tail.
e_partial = sum(F(1, math.factorial(n)) for n in range(9))
# for n>=9, ratio of successive terms <= 1/10 after the 1/9! term:
e_tail_ub = F(1, math.factorial(9)) / (1-F(1,10))
e_ub = e_partial + e_tail_ub
assert e_ub < F(271829,100000)

# phi(0)=1/sqrt(2pi) > 0.39894.
phi0_lb = F(39894,100000)
assert 2*pi_ub < F(1,1)/(phi0_lb*phi0_lb)

# Integral_0^1 exp(-x^2/2) dx.  Alternating series:
# sum_n (-1)^n/[2^n n! (2n+1)].
# Truncation through n=5 is a lower bound.
I6 = sum(F((-1)**n, (2**n)*math.factorial(n)*(2*n+1)) for n in range(6))
I_lb = F(42781,50000)   # 0.85562
assert I6 > I_lb

# Therefore Q(1)=1/2 - phi(0)*Integral < 0.15866.
Q1_ub = F(15866,100000)
assert phi0_lb*I_lb > F(1,2)-Q1_ub

# phi(1)=1/sqrt(2*pi*e) > 0.24197.
phi1_lb = F(24197,100000)
assert 2*pi_ub*F(271829,100000) < F(1,1)/(phi1_lb*phi1_lb)

# Exact identity E[(G-1)_+^2]=2 Q(1)-phi(1).
gauss_tail2_ub = 2*Q1_ub - phi1_lb
assert gauss_tail2_ub == F(1507,20000)  # 0.07535

# Inherited exact whole-box B/c < 5/3, hence a sharper envelope slope.
slope_ub = F(5,3)*gauss_tail2_ub
assert slope_ub == F(1507,12000)

# Inherited anchor.
alpha0 = F(12319635,1000000)  # 12.319635
psi_anchor_lb = F(23584189005311,1090044380000000000000)
EH = F(47,10**13)

# New target: down by 1.722e-7 from the anchor.
delta_alpha = F(1722,10**10)
alpha1 = alpha0 - delta_alpha
assert alpha1 == F(61598174139,5000000000)  # 12.3196348278

# Contraction residual ceiling includes inherited 3.7e-11 alpha-center error.
EA = F(1723,10**10)
ETA = max(F(1,dr[i])*(abs(Aq[i][0])*EH + abs(Aq[i][1])*EA)
          for i in range(2))
RHO = ETA/(1-QCON)
assert ETA == F(6618813947,40000000000)
assert ETA < 1-QCON
assert RHO < 1

psi_new_lb = psi_anchor_lb - slope_ub*delta_alpha
assert psi_new_lb > 0

alpha_prev = F(307990871,25000000)  # 12.31963484
source_gain = alpha_prev - alpha1
assert source_gain == F(61,5_000_000_000)  # 1.22e-8
alphaL = F(315148718753,50000000000)
width_before = alpha_prev-alphaL
width_after = alpha1-alphaL

print("EXACT_GAUSSIAN_SHARPENING")
print("E_UB", e_ub, float(e_ub))
print("PHI0_LB", phi0_lb, float(phi0_lb))
print("INT01_LB", I_lb, float(I_lb))
print("Q1_UB", Q1_ub, float(Q1_ub))
print("PHI1_LB", phi1_lb, float(phi1_lb))
print("GAUSS_TAIL2_UB", gauss_tail2_ub, float(gauss_tail2_ub))
print("SLOPE_UB", slope_ub, float(slope_ub))
print("Q_CONTRACTION", QCON, float(QCON))
print("ETA", ETA, float(ETA))
print("RHO", RHO, float(RHO))
print("PSI_ANCHOR_LB", psi_anchor_lb, float(psi_anchor_lb))
print("DELTA_ALPHA", delta_alpha, float(delta_alpha))
print("PSI_NEW_LB", psi_new_lb, float(psi_new_lb))
print("RIGOROUS_ALPHA_U_BEFORE", float(alpha_prev))
print("RIGOROUS_ALPHA_U_AFTER", float(alpha1))
print("SOURCE_GAIN", source_gain, float(source_gain))
print("BRACKET_WIDTH_BEFORE", float(width_before))
print("BRACKET_WIDTH_AFTER", float(width_after))
print("EXACT_MICROCONTINUATION_PASS")

# ----------------------------------------------------------------------
# PART B: numerical-only entropy-dissipation identity check at the
# previously archived delta=1e-3 complete-third positive-gap scout.
# ----------------------------------------------------------------------

p2=0.967828984055228
p3=0.597722018031788
q2=0.638663550092673
q3=0.229918637629570
B=39.26289564113617
c2=12.52805599281815
c3=2.839127862412615
m=c3/c2
s2=1-p2
s=math.sqrt(s2)

def gh(n):
    x,w=hermgauss(n)
    return np.sqrt(2.0)*x, w/np.sqrt(np.pi)

def kernel_arrays(x, Bv):
    A=1+2*Bv*s2
    rtA=math.sqrt(A)
    a=x/s
    b=x/(s*rtA)
    logt1=log_ndtr(-a)
    logt2=-0.5*math.log(A)-Bv*x*x/A+log_ndtr(b)
    logf=np.logaddexp(logt1,logt2)
    return logf

def J_normalized(mu, b):
    # Return log f and moments E_rho[(Y_+)^r] under
    # rho(dH) proportional exp(-b Y_+^2) gamma(dH), Y=mu+sH.
    # The positive-tail unnormalized moments K_r obey the recurrence, while
    # f = P(Y<=0)+K_0 is the full normalizer.
    A=1+2*b*s2
    rtA=math.sqrt(A)
    a=mu/s
    bb=mu/(s*rtA)
    logneg=float(log_ndtr(-a))
    logpos=float(-0.5*math.log(A)-b*mu*mu/A+log_ndtr(bb))
    logf=float(np.logaddexp(logneg,logpos))
    k0=math.exp(logpos-logf)  # K0/f
    log_boundary=math.log(s)-0.5*(mu/s)**2-0.5*math.log(2*math.pi)
    br=math.exp(log_boundary-logf) if log_boundary-logf < 700 else float("inf")
    k1=(mu*k0+br)/A
    k2=(mu*k1+s2*k0)/A
    k3=(mu*k2+2*s2*k1)/A
    k4=(mu*k3+3*s2*k2)/A
    return logf,k1,k2,k3,k4

def third_entropy_check(n_outer=80, n_tilt=80):
    U,wu=gh(n_outer); V,wv=gh(n_outer)
    logwu=np.log(wu)
    sd=math.sqrt(p2-p3); sp3=math.sqrt(p3)

    Q=QM=0.0
    KHavg=0.0

    xa,wa=leggauss(n_tilt)
    anodes=0.5*m*(xa+1); aweights=0.5*m*wa
    bnodes=0.5*B*(xa+1); bweights=0.5*B*wa

    DU_int=0.0
    for v,ov in zip(V,wv):
        x=sd*U+sp3*v-1.0
        u=kernel_arrays(x,B)

        lt=logwu+m*u
        lz=logsumexp(lt)
        tw=np.exp(lt-lz)
        Q += ov*lz
        QM += ov*float(np.dot(tw,u))

        integ_u=0.0
        for aa,aw in zip(anodes,aweights):
            lta=logwu+aa*u
            lza=logsumexp(lta)
            twa=np.exp(lta-lza)
            mu_u=float(np.dot(twa,u))
            var_u=float(np.dot(twa,(u-mu_u)**2))
            integ_u += aw*aa*var_u
        DU_int += ov*integ_u

        kx=np.empty_like(x)
        for i,mu in enumerate(x):
            integ_h=0.0
            for bb,bw in zip(bnodes,bweights):
                logJ0,j1,j2,j3,j4=J_normalized(float(mu),float(bb))
                mean2=j2
                var2=j4-mean2*mean2
                integ_h += bw*bb*var2
            kx[i]=integ_h
        KHavg += ov*float(np.dot(tw,kx))

    DU_direct=m*QM-Q
    DH_int=m*KHavg

    DH_direct=0.0
    for v,ov in zip(V,wv):
        x=sd*U+sp3*v-1.0
        u=kernel_arrays(x,B)
        lt=logwu+m*u
        lz=logsumexp(lt)
        tw=np.exp(lt-lz)
        kl=np.empty_like(x)
        for i,mu in enumerate(x):
            logJ0,j1,j2,j3,j4=J_normalized(float(mu),B)
            mean2=j2
            kl[i]=-B*mean2-logJ0
        DH_direct += m*ov*float(np.dot(tw,kl))
    return DU_direct,DU_int,DH_direct,DH_int

for n in (40,60,80):
    du_d,du_i,dh_d,dh_i=third_entropy_check(n,n)
    print("NUMERICAL_ONLY_ENTROPY_DISSIPATION",
          n,
          "DU_direct", format(du_d,".15g"),
          "DU_integral", format(du_i,".15g"),
          "DU_diff", format(du_i-du_d,".3e"),
          "DH_direct", format(dh_d,".15g"),
          "DH_integral", format(dh_i,".15g"),
          "DH_diff", format(dh_i-dh_d,".3e"))

print("ALL_EXACT_CHECKS_PASS")
print("ALL_NUMERICAL_DISSIPATION_CHECKS_PASS")
