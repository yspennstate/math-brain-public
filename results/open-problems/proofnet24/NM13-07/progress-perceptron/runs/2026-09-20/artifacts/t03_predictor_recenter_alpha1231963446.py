#!/usr/bin/env python3
"""
NM13-07 / T03, 2026-09-20.
Exact rational predictor-recenter continuation inside the already certified
complete-second directed rectangle.

Inputs inherited from the archived directed certificate:
  whole-rectangle derivative enclosures for H, alpha, Psi,
  center residual ceilings at alpha0=12.319635,
  and the true-root comparison lower bound at alpha0.

New exact work here:
  * construct a rational midpoint-inverse predictor chart centered at the
    midpoint density alpha0-5e-7;
  * certify the new chart is contained in the old directed rectangle;
  * enumerate all interval-Jacobian vertices for a new weighted contraction
    constant (no inherited q is used);
  * bound the shifted-center residual by the fundamental theorem of calculus;
  * certify one contraction chart uniformly for densities alpha0-[4.6,5.4]e-7;
  * prove global uniqueness of stationary roots in the old rectangle from
    H_p<0, H_B>0 and det D(H,alpha)>0;
  * reuse/recheck the exact 64-vertex branch slope bound dPsi/dalpha<1/25;
  * transport positivity to alpha=12.31963446.
All arithmetic below is fractions.Fraction.
"""
from fractions import Fraction as F
import itertools

Hp  = (F(-3371,100000), F(-2828,100000))
HB  = (F(3284,10_000_000), F(5044,10_000_000))
Ap  = (F(24671,1000), F(25288,1000))
AB  = (F(-60244,100000), F(-6008,10000))
Pp  = (F(8701,10000), F(8955,10000))
PB  = (F(-2137,100000), F(-2115,100000))

rp_old = F(1,10_000_000)
rB_old = F(1,250_000)
EH0 = F(47,10**13)
EA0 = F(37,10**12)
alpha0 = F(12319635,1_000_000)
alpha_old = F(615981727,50_000_000)
alpha1 = F(615981723,50_000_000)
assert alpha0-alpha_old == F(46,100_000_000)
assert alpha0-alpha1 == F(54,100_000_000)

def mid(iv): return (iv[0]+iv[1])/2
def smul(a,iv):
    z=(a*iv[0],a*iv[1]); return min(z),max(z)
def iadd(*ivs): return (sum(x[0] for x in ivs),sum(x[1] for x in ivs))
def absmax(iv): return max(abs(iv[0]),abs(iv[1]))
def matmul(A,J):
    return [[sum(A[i][k]*J[k][j] for k in range(2)) for j in range(2)] for i in range(2)]

a,b=mid(Hp),mid(HB)
c,d=mid(Ap),mid(AB)
detm=a*d-b*c
Ainv=[[d/detm,-b/detm],[-c/detm,a/detm]]

delta_m=F(1,2_000_000)
dp=b*delta_m/detm
dB=-a*delta_m/detm
assert dp>0 and dB>0

ratio=F(85,2)
rB=F(21,10_000_000)
rp=rB/ratio
assert abs(dp)+rp < rp_old
assert abs(dB)+rB < rB_old

q=F(0)
for hp,hb,ap,ab in itertools.product(Hp,HB,Ap,AB):
    J=[[hp,hb],[ap,ab]]
    AJ=matmul(Ainv,J)
    M=[[F(int(i==j))-AJ[i][j] for j in range(2)] for i in range(2)]
    row0=abs(M[0][0])+ratio*abs(M[0][1])
    row1=abs(M[1][0])/ratio+abs(M[1][1])
    q=max(q,row0,row1)
assert q < 1

Hmid=iadd((-EH0,EH0),smul(dp,Hp),smul(dB,HB))
Amid=iadd((-EA0,EA0),(delta_m,delta_m),smul(dp,Ap),smul(dB,AB))
mis=F(4,100_000_000)
Auniform=iadd(Amid,(-mis,mis))

def lin_iv(row,ivs):
    out=(F(0),F(0))
    for aa,iv in zip(row,ivs): out=iadd(out,smul(aa,iv))
    return out
AF=[lin_iv(row,[Hmid,Auniform]) for row in Ainv]
eta=max(absmax(AF[0])/rp,absmax(AF[1])/rB)
assert eta < 1-q
rho=eta/(1-q)
assert rho < 1

det_min=None
for hp,hb,ap,ab in itertools.product(Hp,HB,Ap,AB):
    det=hp*ab-hb*ap
    det_min=det if det_min is None else min(det_min,det)
assert Hp[1]<0 and HB[0]>0 and det_min>0

s=F(1,25)
num_min=None; gap_max=None
for hp,hb,ap,ab,pp,pbv in itertools.product(Hp,HB,Ap,AB,Pp,PB):
    det=hp*ab-hb*ap
    num=-pp*hb+pbv*hp
    num_min=num if num_min is None else min(num_min,num)
    gap=num-s*det
    gap_max=gap if gap_max is None else max(gap_max,gap)
assert num_min>0 and gap_max<0

psi0_lb=F(23584189005311,1090044380000000000000)
delta=alpha0-alpha1
psi1_lb=psi0_lb-s*delta
assert psi1_lb>0

alphaL=F(315148718753,50_000_000_000)
width_before=alpha_old-alphaL
width_after=alpha1-alphaL
gain=alpha_old-alpha1
assert gain>0

print('EXACT_PREDICTOR_RECENTER_CERTIFICATE')
print('A_MID_INV',*[str(z) for row in Ainv for z in row])
print('SHIFT_DP',dp,float(dp))
print('SHIFT_DB',dB,float(dB))
print('NEW_RADII',rp,float(rp),rB,float(rB),'RATIO',ratio,float(ratio))
print('CONTAINMENT_P',abs(dp)+rp,float(abs(dp)+rp),'OLD',float(rp_old))
print('CONTAINMENT_B',abs(dB)+rB,float(abs(dB)+rB),'OLD',float(rB_old))
print('Q_NEW',q,float(q),'ONE_MINUS_Q',float(1-q))
print('H_SHIFTED_CENTER_ABSMAX',absmax(Hmid),float(absmax(Hmid)))
print('ALPHA_SHIFTED_CENTER_ABSMAX_AT_MID',absmax(Amid),float(absmax(Amid)))
print('ALPHA_UNIFORM_ABSMAX',absmax(Auniform),float(absmax(Auniform)))
print('ETA_UNIFORM',eta,float(eta),'RHO',rho,float(rho))
print('DET_MIN',det_min,float(det_min))
print('SLOPE_NUM_MIN',num_min,float(num_min))
print('SLOPE_GAP_MAX_N_MINUS_1_25_DET',gap_max,float(gap_max))
print('PSI0_LOWER',psi0_lb,float(psi0_lb))
print('PSI1_LOWER',psi1_lb,float(psi1_lb))
print('ALPHA_U_BEFORE',float(alpha_old))
print('ALPHA_U_AFTER',float(alpha1))
print('SOURCE_GAIN',gain,float(gain))
print('WIDTH_BEFORE',width_before,float(width_before))
print('WIDTH_AFTER',width_after,float(width_after))
print('ALL_EXACT_PREDICTOR_RECENTER_CHECKS_PASS')
