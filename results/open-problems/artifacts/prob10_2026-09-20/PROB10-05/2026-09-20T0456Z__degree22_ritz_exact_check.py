#!/usr/bin/env python3
from fractions import Fraction as F
from math import isqrt, comb, factorial
from functools import lru_cache

# PROB10-05 exact self-check for the degree-22 Ritz trial at the frozen
# softened-edge comparator r=7/8, s=24861/25000.
# All promoted finite claims use exact integer/Fraction arithmetic or
# outward rational fixed-point intervals.
DEG=22
SCALE=10**52
DROOT=10**70
PC=[
-419530588464385600,
1000000000000000000,
-286191401153231584,
-520247871708990784,
50493918782423584,
246784556913484064,
-2493956925053368,
-62950991744397232,
-1040188571730376,
9152894677176570,
231902282235252,
-795552747068942,
-22186633268174,
42334735941753,
1185376565765,
-1377735571842,
-37371612652,
26516146661,
685998231,
-274996352,
-6738704,
1176078,
27223,
]
r=F(7,8)
s=F(24861,25000)
edge=F(1+r,2)
c=s*edge

def floor_frac(x): return x.numerator//x.denominator
def ceil_frac(x): return -((-x.numerator)//x.denominator)
def C(x):
    x=F(x); y=x*SCALE
    return floor_frac(y),ceil_frac(y)
def I_from_bounds(lo,hi): return floor_frac(lo*SCALE),ceil_frac(hi*SCALE)
def iadd(a,b): return a[0]+b[0],a[1]+b[1]
def ineg(a): return -a[1],-a[0]
def isub(a,b): return iadd(a,ineg(b))
def imul(a,b):
    vals=(a[0]*b[0],a[0]*b[1],a[1]*b[0],a[1]*b[1])
    lo,hi=min(vals),max(vals)
    return lo//SCALE,-((-hi)//SCALE)
def iscale(a,q):
    q=F(q)
    if q>=0: lo,hi=F(a[0])*q,F(a[1])*q
    else: lo,hi=F(a[1])*q,F(a[0])*q
    return floor_frac(lo),ceil_frac(hi)
def iinv(a):
    assert a[0]>0
    return floor_frac(F(SCALE*SCALE,a[1])),ceil_frac(F(SCALE*SCALE,a[0]))
def idiv(a,b): return imul(a,iinv(b))
def interval_float(a): return a[0]/SCALE,a[1]/SCALE
def ipow(a,n):
    out=C(1)
    for _ in range(n): out=imul(out,a)
    return out

def atan_series_bounds(x,m):
    x=F(x); assert 0<=x<1
    ss=F(0)
    for k in range(m+1):
        ss += F((-1)**k,2*k+1)*x**(2*k+1)
    nxt=F((-1)**(m+1),2*(m+1)+1)*x**(2*(m+1)+1)
    return min(ss,ss+nxt),max(ss,ss+nxt)

a5=atan_series_bounds(F(1,5),80)
a239=atan_series_bounds(F(1,239),25)
PI=(16*a5[0]-4*a239[1],16*a5[1]-4*a239[0])

def sqrt_bounds(x):
    x=F(x); assert x>=0
    if x==0:return F(0),F(0)
    m=isqrt((DROOT*DROOT*x.numerator)//x.denominator)
    lo,hi=F(m,DROOT),F(m+1,DROOT)
    assert lo*lo<=x<hi*hi
    return lo,hi

def atan_point_bounds(t):
    t=F(t)
    if t<0:
        lo,hi=atan_point_bounds(-t); return -hi,-lo
    if t<=F(1,2): return atan_series_bounds(t,90)
    if t<=2:
        u=(t-1)/(t+1); lo,hi=atan_series_bounds(u,90)
        return PI[0]/4+lo,PI[1]/4+hi
    lo,hi=atan_series_bounds(1/t,90)
    return PI[0]/2-hi,PI[1]/2-lo

sqrt2pi=(sqrt_bounds(2*PI[0])[0],sqrt_bounds(2*PI[1])[1])
tI=I_from_bounds(1/sqrt2pi[1],1/sqrt2pi[0])
piI=I_from_bounds(*PI)

def std_moment(k):
    if k%2:return 0
    out=1
    for j in range(1,k,2): out*=j
    return out

def trunc_negative_moment(k):
    if k%2==0:return C(F(std_moment(k),2))
    m=(k-1)//2
    return iscale(tI,-(2**m)*factorial(m))

@lru_cache(None)
def biv_moment_cached(i,j,vnum,vden,hnum,hden):
    v=F(vnum,vden); h=F(hnum,hden)
    if i<0 or j<0:return F(0)
    if i==0:
        if j%2:return F(0)
        return F(std_moment(j))*v**(j//2)
    return (F(i-1)*v*biv_moment_cached(i-2,j,vnum,vden,hnum,hden)
            +F(j)*h*biv_moment_cached(i-1,j-1,vnum,vden,hnum,hden))
def biv_moment(i,j,v,h):
    return biv_moment_cached(i,j,v.numerator,v.denominator,h.numerator,h.denominator)

# Norm in L^2(phi).
q_exact=0
for i,ci in enumerate(PC):
    for j,cj in enumerate(PC):
        q_exact += ci*cj*std_moment(i+j)
qI=C(q_exact)
assert qI[0]>0

# <f,Kf>: one noisy edge, after conditioning on the edge Gaussian.
sqrtcI=I_from_bounds(*sqrt_bounds(c))
sqrtcP=[ipow(sqrtcI,k) for k in range(2*DEG+1)]
v1=1-c
h1=r-c
mI=(0,0)
for i,ci in enumerate(PC):
  for j,cj in enumerate(PC):
    pair=(0,0)
    for a in range(i+1):
      for b in range(j+1):
        res=biv_moment(i-a,j-b,v1,h1)
        if res==0: continue
        term=imul(sqrtcP[a+b],trunc_negative_moment(a+b))
        term=iscale(term,F(comb(i,a)*comb(j,b))*res)
        pair=iadd(pair,term)
    mI=iadd(mI,iscale(pair,F(ci*cj)))
muI=idiv(mI,qI)

# <Kf,Kf>: two adjacent noisy edges, exact bivariate orthant moment recurrences.
MAX=2*DEG+2
EXT=3*DEG+12
s2=1-c*c
sqrt_s2=sqrt_bounds(s2)
sI=I_from_bounds(*sqrt_s2)
ratioI=I_from_bounds(c/sqrt_s2[1],c/sqrt_s2[0])
asin_c=(atan_point_bounds(c/sqrt_s2[1])[0],atan_point_bounds(c/sqrt_s2[0])[1])
asinI=I_from_bounds(*asin_c)
B=[None]*EXT
B[0]=iscale(imul(sI,tI),F(1,2))
B[1]=iscale(imul(tI,tI),s2)
for k in range(2,EXT):
    B[k]=iscale(B[k-2],F(k-1)*s2)
A=[None]*EXT
A[0]=iadd(C(F(1,4)),iscale(idiv(asinI,piI),F(1,2)))
A[1]=iadd(iscale(tI,F(1,2)),imul(ratioI,B[0]))
for k in range(2,EXT):
    A[k]=iadd(iscale(A[k-2],k-1),imul(ratioI,B[k-1]))
Q=[[None]*EXT for _ in range(MAX+1)]
for n in range(EXT): Q[0][n]=A[n]
for n in range(EXT-1):
    Q[1][n]=iadd(iscale(A[n+1],c),imul(sI,B[n]))
for mm in range(2,MAX+1):
    for n in range(EXT-mm):
        Q[mm][n]=iadd(iscale(Q[mm-1][n+1],c),
                      iscale(Q[mm-2][n],F(mm-1)*s2))
for i in range(2*DEG+1):
    for j in range(2*DEG+1-i):
        qi,qj=Q[i][j],Q[j][i]
        assert max(qi[0],qj[0])<=min(qi[1],qj[1])

def q_negative(a,b):
    z=Q[a][b]
    return ineg(z) if (a+b)%2 else z

den=1-c*c
alpha_coef=(1-r*c)/den
beta_coef=(r-c)/den
alphaI=iscale(sqrtcI,alpha_coef)
betaI=iscale(sqrtcI,beta_coef)
alphaP=[ipow(alphaI,k) for k in range(DEG+1)]
betaP=[ipow(betaI,k) for k in range(DEG+1)]
v2=F(1)-c*(1+r*r-2*r*c)/den
h2=r*r-c*(2*r-c*(1+r*r))/den
assert v2>abs(h2)
meanM=[[None]*(DEG+1) for _ in range(DEG+1)]
for p in range(DEG+1):
  for q in range(DEG+1):
    total=(0,0)
    for ia in range(p+1):
      ib=p-ia
      coeff1=imul(alphaP[ia],betaP[ib])
      for ja in range(q+1):
        jb=q-ja
        coeff=imul(coeff1,imul(betaP[ja],alphaP[jb]))
        term=imul(coeff,q_negative(ia+ja,ib+jb))
        total=iadd(total,iscale(term,F(comb(p,ia)*comb(q,ja))))
    meanM[p][q]=total
condM=[[None]*(DEG+1) for _ in range(DEG+1)]
for p in range(DEG+1):
  for q in range(DEG+1):
    total=(0,0)
    for e in range(p+1):
      for h in range(q+1):
        rm=biv_moment(e,h,v2,h2)
        if rm==0: continue
        total=iadd(total,iscale(meanM[p-e][q-h],
                                F(comb(p,e)*comb(q,h))*rm))
    condM[p][q]=total
nI=(0,0)
for i,ci in enumerate(PC):
    for j,cj in enumerate(PC):
        nI=iadd(nI,iscale(condM[i][j],F(ci*cj)))
nNormI=idiv(nI,qI)
eps2I=isub(nNormI,imul(muI,muI))
assert eps2I[0]>0

# Coarse rational enclosures promoted in the proof.
mu_lo=F(9119014796,10_000_000_000)
mu_hi=F(9119014797,10_000_000_000)
eps2_hi=F(285492169,1_000_000_000_000)
assert muI[0] > floor_frac(mu_lo*SCALE)
assert muI[1] < ceil_frac(mu_hi*SCALE)
assert eps2I[1] < ceil_frac(eps2_hi*SCALE)

# Consume the independently archived sharp-probit endpoint and 256-block
# Plackett decrement; only their exact rational composition is done here.
peq_norm_cap=F(5453881,5_000_000)       # 1.0907762
plackett_dec=F(9289,2_500_000)          # 0.0037156
trace_exact_cap=peq_norm_cap-plackett_dec/(1-r**4)
trace_cap=F(540899,500_000)              # 1.081798
assert trace_exact_cap<trace_cap

# New exponent target.
theta_old=F(330973,2_000_000)            # 0.1654865
theta=F(8399,50_000)                     # 0.16798
x0=F(914184915597,1_000_000_000_000)
beta=F(491787987,625_000_000)

# Exact logarithm enclosure proves x0 < r^(4 theta).
def neglog_bounds(a,N):
    z=(1-a)/(1+a)
    lo=sum(F(2)*z**(2*k+1)/F(2*k+1) for k in range(N+1))
    tail=F(2)*z**(2*N+3)/(F(2*N+3)*(1-z*z))
    return lo,lo+tail
Lx,Ux=neglog_bounds(x0,4)
Lr,Ur=neglog_bounds(r,4)
log_margin=Lx-4*theta*Ur
assert log_margin>0

# If lambda_1 >= r^(4 theta), then lambda_1>x0.
# Trace(K^4)<trace_cap forces each non-Perron eigenvalue into (-beta,beta).
assert x0>mu_hi>mu_lo>beta
tail_margin=beta**4-(trace_cap-x0**4)
assert tail_margin>0

# Spectral-measure/Temple contradiction.
temple_lower=(x0-mu_hi)*(mu_lo-beta)
temple_margin=temple_lower-eps2_hi
assert temple_margin>0

width_old=F(1,4)-theta_old
width_new=F(1,4)-theta
assert width_old==F(169027,2_000_000)
assert width_new==F(4101,50_000)
assert theta>theta_old

print("degree =",DEG)
print("mu interval =",interval_float(muI))
print("eps2 interval =",interval_float(eps2I))
print("mu coarse =",mu_lo,mu_hi)
print("eps2 coarse upper =",eps2_hi,float(eps2_hi))
print("trace exact inherited composition =",float(trace_exact_cap))
print("trace cap =",trace_cap,float(trace_cap))
print("x0 =",x0,float(x0))
print("beta =",beta,float(beta))
print("log margin =",log_margin,float(log_margin))
print("spectral tail margin =",tail_margin,float(tail_margin))
print("Temple lower =",temple_lower,float(temple_lower))
print("Temple contradiction margin =",temple_margin,float(temple_margin))
print("old theta =",theta_old,float(theta_old),"old width =",width_old,float(width_old))
print("new theta =",theta,float(theta),"new width =",width_new,float(width_new))
print("source gain =",theta-theta_old,float(theta-theta_old))
print("ALL_EXACT_CHECKS_PASS = True")
