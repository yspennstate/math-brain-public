#!/usr/bin/env python3
from fractions import Fraction as F
from math import isqrt, comb, factorial
from functools import lru_cache

# HARD7-05 exact self-check for the near-frontier independently softened
# edge comparator at r=7/8, s=24861/25000.
# All theorem-deciding finite comparisons use exact integer/Fraction
# arithmetic or outward-rounded rational fixed-point intervals.
# The only inherited analytic inputs are the proved source tail envelope
# R(u)<=u for u<=287831/500000 and the previous on-page theorem
# tr(K_{r,s}^4)<=tr(K_{r,1}^4), together with the already certified
# hard-edge cap tr(K_{7/8,1}^4)<553151/500000.

DEG=18
SCALE=10**52
DROOT=10**70
PC=[
-483977989012241664,
1115118951175956224,
-321598937420313152,
-488951718181460672,
63134926720828960,
184558584009882528,
-8135483950085454,
-35774376518893592,
523343654913742,
3746547459919287,
-9784307088286,
-218347978364829,
-605761245592,
7000765956317,
36905362702,
-114278008349,
-730339541,
734962998,
5006652,
]
r=F(7,8)
s=F(24861,25000)
edge=F(1+r,2)
c=s*edge
r0=F(287831,500000)

def P(z): return 2+2*z-3*z*z-2*z**3-2*z**4
cov_margins=[]
for k in range(1,5):
    u=r**k; cap=c*r**(k-1); assert cap>u
    z=u*u; D=6*u**5*(cap-u)/(1-u*u); T=P(z)+D
    margin=T*T-4*(1+z)**2*(1-z*z)**3
    assert T>0 and margin>0
    cov_margins.append(margin)
assert r**5<r0 and c/r>1

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
    vals=(a[0]*b[0],a[0]*b[1],a[1]*b[0],a[1]*b[1]); lo,hi=min(vals),max(vals)
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
    for k in range(m+1): ss += F((-1)**k,2*k+1)*x**(2*k+1)
    nxt=F((-1)**(m+1),2*(m+1)+1)*x**(2*(m+1)+1)
    return min(ss,ss+nxt),max(ss,ss+nxt)
a5=atan_series_bounds(F(1,5),80); a239=atan_series_bounds(F(1,239),25)
PI=(16*a5[0]-4*a239[1],16*a5[1]-4*a239[0])
def sqrt_bounds(x):
    x=F(x); assert x>=0
    if x==0:return F(0),F(0)
    m=isqrt((DROOT*DROOT*x.numerator)//x.denominator)
    lo,hi=F(m,DROOT),F(m+1,DROOT); assert lo*lo<=x<hi*hi
    return lo,hi
def atan_point_bounds(t):
    t=F(t)
    if t<0:
        lo,hi=atan_point_bounds(-t); return -hi,-lo
    if t<=F(1,2): return atan_series_bounds(t,90)
    if t<=2:
        u=(t-1)/(t+1); lo,hi=atan_series_bounds(u,90)
        return PI[0]/4+lo,PI[1]/4+hi
    lo,hi=atan_series_bounds(1/t,90); return PI[0]/2-hi,PI[1]/2-lo
sqrt2pi=(sqrt_bounds(2*PI[0])[0],sqrt_bounds(2*PI[1])[1])
tI=I_from_bounds(1/sqrt2pi[1],1/sqrt2pi[0]); piI=I_from_bounds(*PI)
def std_moment(k):
    if k%2:return 0
    out=1
    for j in range(1,k,2): out*=j
    return out
def trunc_negative_moment(k):
    if k%2==0:return C(F(std_moment(k),2))
    m=(k-1)//2; return iscale(tI,-(2**m)*factorial(m))
@lru_cache(None)
def biv_moment_cached(i,j,vnum,vden,hnum,hden):
    v=F(vnum,vden); h=F(hnum,hden)
    if i<0 or j<0:return F(0)
    if i==0:
        if j%2:return F(0)
        return F(std_moment(j))*v**(j//2)
    return F(i-1)*v*biv_moment_cached(i-2,j,vnum,vden,hnum,hden)+F(j)*h*biv_moment_cached(i-1,j-1,vnum,vden,hnum,hden)
def biv_moment(i,j,v,h): return biv_moment_cached(i,j,v.numerator,v.denominator,h.numerator,h.denominator)
q_exact=0
for i,ci in enumerate(PC):
    for j,cj in enumerate(PC): q_exact += ci*cj*std_moment(i+j)
qI=C(q_exact); assert qI[0]>0
sqrtcI=I_from_bounds(*sqrt_bounds(c)); sqrtcP=[ipow(sqrtcI,k) for k in range(2*DEG+1)]
v1=1-c; h1=r-c
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
MAX=2*DEG+2; EXT=3*DEG+12
s2=1-c*c; sqrt_s2=sqrt_bounds(s2); sI=I_from_bounds(*sqrt_s2)
ratioI=I_from_bounds(c/sqrt_s2[1],c/sqrt_s2[0])
asin_c=(atan_point_bounds(c/sqrt_s2[1])[0],atan_point_bounds(c/sqrt_s2[0])[1]); asinI=I_from_bounds(*asin_c)
B=[None]*EXT; B[0]=iscale(imul(sI,tI),F(1,2)); B[1]=iscale(imul(tI,tI),s2)
for k in range(2,EXT): B[k]=iscale(B[k-2],F(k-1)*s2)
A=[None]*EXT; A[0]=iadd(C(F(1,4)),iscale(idiv(asinI,piI),F(1,2))); A[1]=iadd(iscale(tI,F(1,2)),imul(ratioI,B[0]))
for k in range(2,EXT): A[k]=iadd(iscale(A[k-2],k-1),imul(ratioI,B[k-1]))
Q=[[None]*EXT for _ in range(MAX+1)]
for n in range(EXT): Q[0][n]=A[n]
for n in range(EXT-1): Q[1][n]=iadd(iscale(A[n+1],c),imul(sI,B[n]))
for mm in range(2,MAX+1):
    for n in range(EXT-mm): Q[mm][n]=iadd(iscale(Q[mm-1][n+1],c),iscale(Q[mm-2][n],F(mm-1)*s2))
for i in range(2*DEG+1):
    for j in range(2*DEG+1-i):
        qi,qj=Q[i][j],Q[j][i]; assert max(qi[0],qj[0])<=min(qi[1],qj[1])
def q_negative(a,b):
    z=Q[a][b]; return ineg(z) if (a+b)%2 else z

den=1-c*c; alpha_coef=(1-r*c)/den; beta_coef=(r-c)/den
alphaI=iscale(sqrtcI,alpha_coef); betaI=iscale(sqrtcI,beta_coef)
alphaP=[ipow(alphaI,k) for k in range(DEG+1)]; betaP=[ipow(betaI,k) for k in range(DEG+1)]
v2=F(1)-c*(1+r*r-2*r*c)/den
h2=r*r-c*(2*r-c*(1+r*r))/den
assert v2>abs(h2)
meanM=[[None]*(DEG+1) for _ in range(DEG+1)]
for p in range(DEG+1):
  for q in range(DEG+1):
    total=(0,0)
    for ia in range(p+1):
      ib=p-ia; coeff1=imul(alphaP[ia],betaP[ib])
      for ja in range(q+1):
        jb=q-ja; coeff=imul(coeff1,imul(betaP[ja],alphaP[jb])); term=imul(coeff,q_negative(ia+ja,ib+jb))
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
        total=iadd(total,iscale(meanM[p-e][q-h],F(comb(p,e)*comb(q,h))*rm))
    condM[p][q]=total
nI=(0,0)
for i,ci in enumerate(PC):
    for j,cj in enumerate(PC): nI=iadd(nI,iscale(condM[i][j],F(ci*cj)))
nNormI=idiv(nI,qI); eps2I=isub(nNormI,imul(muI,muI)); assert eps2I[0]>0

mu_lo=F(9116948312,10_000_000_000)
mu_hi=F(9116948313,10_000_000_000)
eps2_hi=F(47004495,100_000_000_000)
assert muI[0]>floor_frac(mu_lo*SCALE)
assert muI[1]<ceil_frac(mu_hi*SCALE)
assert eps2I[1]<ceil_frac(eps2_hi*SCALE)
trace4_upper=F(553151,500000)
theta_target=F(1647,10000)
xL=F(4578939,5000000)
assert xL**2500 < r**1647
assert xL>mu_hi
beta=F(7967277,10000000)
trace_tail_margin=beta**4-(trace4_upper-xL**4)
assert trace_tail_margin>0
assert mu_lo>beta
temple_lower=(xL-mu_hi)*(mu_lo-beta)
temple_margin=temple_lower-eps2_hi
assert temple_margin>0
old_lower=F(41,250)
new_lower=theta_target
source_upper=F(1,4)
old_width=source_upper-old_lower
new_width=source_upper-new_lower
assert old_width==F(43,500)
assert new_width==F(853,10000)
assert old_width-new_width==F(7,10000)

print('r =',r,float(r))
print('s =',s,float(s),'c =',c,float(c),'c/r =',float(c/r))
print('covariance squared margins =',[float(x) for x in cov_margins])
print('v2,h2 =',v2,float(v2),h2,float(h2))
print('mu interval =',interval_float(muI))
print('eps2 interval =',interval_float(eps2I))
print('mu coarse =',mu_lo,mu_hi)
print('eps2 coarse upper =',eps2_hi,float(eps2_hi))
print('xL =',xL,float(xL),'power check =',xL**2500<r**1647)
print('beta =',beta,float(beta))
print('trace tail margin =',trace_tail_margin,float(trace_tail_margin))
print('Temple lower =',temple_lower,float(temple_lower))
print('Temple contradiction margin =',temple_margin,float(temple_margin))
print('new lower =',new_lower,float(new_lower),'new width =',new_width,float(new_width),'improvement =',old_width-new_width,float(old_width-new_width))
print('ALL_EXACT_CHECKS_PASS = True')