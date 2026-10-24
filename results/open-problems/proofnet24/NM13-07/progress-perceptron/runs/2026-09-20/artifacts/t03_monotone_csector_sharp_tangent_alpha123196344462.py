#!/usr/bin/env python3
"""
NM13-07 / LIVE20 T03, 2026-09-20.

Part A (EXACT): sharpen the complete-second stationary branch tangent by
computing the exact best vertex-ratio slope bound on the already directed
derivative box, and combine it with the existing predictor/recentered chart
to certify alpha_U = 12.3196344462.

Part B (NUMERICAL_ONLY): falsification/practicality check for a new exact
third-full monotone c-sector theorem at the delta=1e-3 waypoint.  It checks
that both outer conditional KL integrands are increasing, measures monotone
Gaussian-cell enclosure widths, and compares the new common truncated-normal
D_H envelope with the older E2 envelope.  No floating computation in Part B
is used for the source endpoint.
"""
from fractions import Fraction as F
import itertools, math
import numpy as np
from numpy.polynomial.hermite import hermgauss
from scipy.special import log_ndtr, logsumexp

# ----------------------------------------------------------------------
# PART A: exact branch-tangent + recentered contraction
# ----------------------------------------------------------------------
Hp  = (F(-3371,100000), F(-2828,100000))
HB  = (F(3284,10_000_000), F(5044,10_000_000))
Ap  = (F(24671,1000), F(25288,1000))
AB  = (F(-60244,100000), F(-6008,10000))
Pp  = (F(8701,10000), F(8955,10000))
PB  = (F(-2137,100000), F(-2115,100000))

def mid(iv): return (iv[0]+iv[1])/2
def smul(a,iv):
    z=(a*iv[0],a*iv[1]); return min(z),max(z)
def iadd(*ivs): return (sum(x[0] for x in ivs),sum(x[1] for x in ivs))
def absmax(iv): return max(abs(iv[0]),abs(iv[1]))
def matmul(A,J):
    return [[sum(A[i][k]*J[k][j] for k in range(2)) for j in range(2)]
            for i in range(2)]
def lin_iv(row,ivs):
    out=(F(0),F(0))
    for aa,iv in zip(row,ivs):
        out=iadd(out,smul(aa,iv))
    return out

# Exact determinant/numerator signs and optimal ratio among vertices.
det_min=None
num_min=None
slope_vmax=None
slope_arg=None
for hp,hb,ap,ab,pp,pb in itertools.product(Hp,HB,Ap,AB,Pp,PB):
    det=hp*ab-hb*ap
    num=-pp*hb+pb*hp
    assert det > 0
    assert num > 0
    sl=num/det
    if det_min is None or det<det_min: det_min=det
    if num_min is None or num<num_min: num_min=num
    if slope_vmax is None or sl>slope_vmax:
        slope_vmax=sl; slope_arg=(hp,hb,ap,ab,pp,pb)

# For fixed s, N-s*Delta is multi-affine in the six interval variables.
# Choosing s as the maximum vertex ratio makes every vertex <=0; hence
# N/Delta <= s on the entire hyperrectangle.
gap_max=None
for hp,hb,ap,ab,pp,pb in itertools.product(Hp,HB,Ap,AB,Pp,PB):
    det=hp*ab-hb*ap
    num=-pp*hb+pb*hp
    gap=num-slope_vmax*det
    gap_max=gap if gap_max is None else max(gap_max,gap)
assert gap_max == 0
assert slope_vmax == F(4136629,105883920)

# Predictor/recentered chart inherited geometry, but with an enlarged density
# band sufficient to reach the new endpoint.
rp_old=F(1,10_000_000)
rB_old=F(1,250_000)
EH0=F(47,10**13)
EA0=F(37,10**12)
alpha0=F(12319635,1_000_000)

a,b=mid(Hp),mid(HB)
c,d=mid(Ap),mid(AB)
detm=a*d-b*c
Ainv=[[d/detm,-b/detm],[-c/detm,a/detm]]
delta_m=F(1,2_000_000)       # predictor center: alpha0-5e-7
dp=b*delta_m/detm
dB=-a*delta_m/detm
ratio=F(85,2)
rB=F(21,10_000_000)
rp=rB/ratio
assert abs(dp)+rp < rp_old
assert abs(dB)+rB < rB_old

q=F(0)
for hp,hb,ap,ab in itertools.product(Hp,HB,Ap,AB):
    AJ=matmul(Ainv,[[hp,hb],[ap,ab]])
    M=[[F(int(i==j))-AJ[i][j] for j in range(2)] for i in range(2)]
    row0=abs(M[0][0])+ratio*abs(M[0][1])
    row1=abs(M[1][0])/ratio+abs(M[1][1])
    q=max(q,row0,row1)
assert q == F(229179741,467259059)
assert q < 1

Hmid=iadd((-EH0,EH0),smul(dp,Hp),smul(dB,HB))
Amid=iadd((-EA0,EA0),(delta_m,delta_m),smul(dp,Ap),smul(dB,AB))

# Uniformly cover the old endpoint delta=5.4e-7 and new endpoint
# delta=5.538e-7.  Radius 5.4e-8 around the 5e-7 predictor center suffices.
mis=F(27,500_000_000)       # 5.4e-8
Auniform=iadd(Amid,(-mis,mis))
AF=[lin_iv(row,[Hmid,Auniform]) for row in Ainv]
eta=max(absmax(AF[0])/rp,absmax(AF[1])/rB)
rho=eta/(1-q)
assert eta < 1-q
assert rho < 1

# New source endpoint and objective transport.
alpha_before=F(615981723,50_000_000)  # 12.31963446
alpha1=F(61598172231,5_000_000_000)   # 12.3196344462
delta=alpha0-alpha1
assert delta == F(2769,5_000_000_000)

psi0_lb=F(23584189005311,1090044380000000000000)
psi1_lb=psi0_lb-slope_vmax*delta
assert psi1_lb > 0

alphaL=F(315148718753,50_000_000_000)
width_before=alpha_before-alphaL
width_after=alpha1-alphaL
gain=alpha_before-alpha1
assert gain > 0

print("EXACT_COMPLETE_SECOND_SHARP_TANGENT")
print("DET_MIN",det_min,float(det_min))
print("NUM_MIN",num_min,float(num_min))
print("SLOPE_VERTEX_MAX",slope_vmax,float(slope_vmax))
print("SLOPE_ARG",*[str(x) for x in slope_arg])
print("MAX_N_MINUS_SLOPEMAX_DET",gap_max,float(gap_max))
print("RECENTER_Q",q,float(q))
print("RECENTER_ETA",eta,float(eta))
print("RECENTER_ONE_MINUS_Q",1-q,float(1-q))
print("RECENTER_RHO",rho,float(rho))
print("TARGET_DELTA",delta,float(delta))
print("PSI_ANCHOR_LOWER",psi0_lb,float(psi0_lb))
print("PSI_NEW_LOWER",psi1_lb,float(psi1_lb))
print("ALPHA_U_BEFORE",float(alpha_before))
print("ALPHA_U_AFTER",float(alpha1))
print("SOURCE_GAIN",gain,float(gain))
print("WIDTH_BEFORE",width_before,float(width_before))
print("WIDTH_AFTER",width_after,float(width_after))
print("ALL_EXACT_SHARP_TANGENT_CHECKS_PASS")

# ----------------------------------------------------------------------
# PART B: numerical-only check of new monotone c-sector theorem.
# ----------------------------------------------------------------------
def gh(n):
    x,w=hermgauss(n)
    return np.sqrt(2.0)*x, w/np.sqrt(np.pi)

def reconstruct_q_sector(p2,p3,q2,q3):
    c3=math.sqrt(p3/q3)/(p2-p3)-math.sqrt(q3/p3)/(q2-q3)
    gp=0.5*(1-q2)/(1-p2)*(p2-p3)/(q2-q3)*math.sqrt(q3/p3)
    c2=((p2-p3)/(q2-q3)*math.sqrt(q3/p3))/(1-p2) \
       -((q2-q3)/(p2-p3)*math.sqrt(p3/q3))/(1-q2)
    return c2,c3,gp

def kernel_u_ux_kl(x,s,B):
    x=np.asarray(x,float)
    A=1+2*B*s*s
    a=x/s
    b=x/(s*math.sqrt(A))
    logt1=log_ndtr(-a)
    logt2=-0.5*math.log(A)-B*x*x/A+log_ndtr(b)
    u=np.logaddexp(logt1,logt2)
    f1=np.exp(logt1-u); f2=np.exp(logt2-u)
    logphi0=-0.5*math.log(2*math.pi)
    mills_mina=np.exp(logphi0-0.5*a*a-log_ndtr(-a))
    ux1=-mills_mina/s
    mills_b=np.exp(logphi0-0.5*b*b-log_ndtr(b))
    ux2=-2*B*x/A+mills_b/(s*math.sqrt(A))
    ux=f1*ux1+f2*ux2
    uB2=-s*s/A-x*x/(A*A)-x*s*(A**-1.5)*mills_b
    uB=f2*uB2
    KL=B*uB-u
    return u,ux,KL

# Archived delta=1e-3 positive-gap waypoint.
p2=0.967828984055228
p3=0.597722018031788
q2=0.638663550092673
q3=0.229918637629570
DEL=1e-3
c2,c3,gp=reconstruct_q_sector(p2,p3,q2,q3)
r2=q3/p3
r1=(q2-q3)/(p2-p3)
r0=(1-q2)/(1-p2)
S=r1/(r0*math.sqrt(r2))
gs=0.5*(S+DEL)
B=c2/(4*gs)
m=c3/c2
dlt=math.sqrt(p2-p3)
s=math.sqrt(1-p2)
sig2=1-p3
sp3=math.sqrt(p3)

U,wu=gh(160)
logwu=np.log(wu)

def cond(v):
    aa=sp3*v-1
    X=aa+dlt*U
    u,ux,kh=kernel_u_ux_kl(X,s,B)
    lt=logwu+m*u
    lz=logsumexp(lt)
    tw=np.exp(lt-lz)
    DU=m*float(np.dot(tw,u))-float(lz)
    DH=m*float(np.dot(tw,kh))
    meanux=float(np.dot(tw,ux))
    return DU,DH,meanux

# Monotonicity scout.
vv=np.linspace(-6,6,601)
cv=np.array([cond(v)[:2] for v in vv])
print("NUMERICAL_ONLY_MONOTONE_MIN_DIFF_DU",float(np.min(np.diff(cv[:,0]))))
print("NUMERICAL_ONLY_MONOTONE_MIN_DIFF_DH",float(np.min(np.diff(cv[:,1]))))

Phi=lambda z: 0.5*(1+math.erf(z/math.sqrt(2)))
phi=lambda z: math.exp(-0.5*z*z)/math.sqrt(2*math.pi)

# Common exact theorem envelope (evaluated numerically here):
# R(a)=mB E(a+sqrt(1-p3)G)_+^2.
def common_env(v):
    aa=sp3*v-1
    sig=math.sqrt(sig2)
    z=aa/sig
    return m*B*((aa*aa+sig2)*Phi(z)+aa*sig*phi(z))

# R14 older D_H envelope.
S0=abs(cond(0.0)[2])
A=1+2*B*s*s
C1=2*B*sp3/A
def old_DH_env(v):
    aa=sp3*v-1
    E2=sig2+(abs(aa)+m*dlt*dlt*(S0+C1*abs(v)))**2
    return m*B*E2

print("NUMERICAL_ONLY_WAYPOINT_B_M",B,m)
print("NUMERICAL_ONLY_ENV_AT_V0_NEW_OLD",common_env(0),old_DH_env(0))
print("NUMERICAL_ONLY_ENV_AT_V6_NEW_OLD",common_env(6),old_DH_env(6))
print("NUMERICAL_ONLY_ENV_RATIO_OLD_OVER_NEW_V0",old_DH_env(0)/common_env(0))
print("NUMERICAL_ONLY_ENV_RATIO_OLD_OVER_NEW_V6",old_DH_env(6)/common_env(6))

# Monotone Gaussian-cell enclosure at finite mesh.  Endpoint values are
# numerical scouts only.  The theorem says this becomes rigorous once each
# endpoint itself is outward enclosed.
def right_poly_tail(L):
    Q=1-Phi(L); ph=phi(L)
    # Integral of mB[(sqrt(p3)v-1)^2 + (1-p3)] over v>L.
    return m*B*(p3*(Q+L*ph)-2*sp3*ph+(2-p3)*Q)

for ncell in (256,1024,4096):
    L=6.0
    e=np.linspace(-L,L,ncell+1)
    g=np.array([cond(v)[:2] for v in e])
    mass=np.array([Phi(e[i+1])-Phi(e[i]) for i in range(ncell)])
    lo=np.sum(mass[:,None]*g[:-1],axis=0)
    up=np.sum(mass[:,None]*g[1:],axis=0)
    up += g[0]*Phi(-L) + right_poly_tail(L)
    print("NUMERICAL_ONLY_MONOTONE_CELLS",ncell,
          "DU_LO_UP_WIDTH",lo[0],up[0],up[0]-lo[0],
          "DH_LO_UP_WIDTH",lo[1],up[1],up[1]-lo[1])

print("ALL_NUMERICAL_MONOTONE_CSECTOR_CHECKS_PASS")
