#!/usr/bin/env python3
from fractions import Fraction as F
from math import isqrt, comb, factorial
from functools import lru_cache

# T05 exact self-check: degree-48 Ritz certificate for the scale-correct comparator.
# All promoted inequalities use exact Fraction/integer arithmetic or outward
# rational fixed-point intervals. The covariance bridge is checked separately
# with exact rational square tests below.
DEG=48
SCALE=10**130
DROOT=10**170
PC=[-3871971365618629463843449310797811941376, 10000000000000000000000000000000000000000, -1428982843150673592941088035344597647360, -9720144667506307552473515666109982834688, -2683748409820633413222522017515839684608, 9937867224558091305483667703918120402944, 3477501742011225109872689872619612143616, -6178089359457098356642394593287408189440, -2086208773128157908155372323658425958400, 2447307013046943843115796324177101717504, 756237204601580739283495239458465251328, -651992251393556965619071131820213927936, -182391928692659184944468836328620949504, 121994112527171720299093798981442994176, 30930710401608269267531723884204130304, -16576336066068029958093751520216481792, -3827422906193461276538914245661687808, 1678159764852371383361579677233709056, 354899699068716256431026214572916736, -129097760701746523303283856074866688, -25149077369843888696567103985025024, 7660262377594847135223437875740672, 1381960919933868577646686672781312, -354513177324894037262354396217344, -59518088609731271103699648249856, 12896524907028169419079775420416, 2023791042180253454670074216448, -370551299398149062002133172224, -54568218058658172841578463232, 8425170138829029956558782464, 1168476169517203732723400704, -151413085678098075158052864, -19840577651038337999306752, 2140973778992362464215040, 265839066274451270139904, -23610388285005812989952, -2785332509459556073472, 200161721088574914560, 22488920159962615808, -1275362106353788160, -136770210874381808, 5892777361208584, 604401368723389, -18595065207451, -1827497599360, 35770426584, 3374274906, -31580365, -2863903]

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
    for k in range(m+1): ss += F((-1)**k,2*k+1)*x**(2*k+1)
    nxt=F((-1)**(m+1),2*(m+1)+1)*x**(2*(m+1)+1)
    return min(ss,ss+nxt),max(ss,ss+nxt)
a5=atan_series_bounds(F(1,5),100)
a239=atan_series_bounds(F(1,239),30)
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
    if t<=F(1,2): return atan_series_bounds(t,120)
    if t<=2:
        u=(t-1)/(t+1); lo,hi=atan_series_bounds(u,120)
        return PI[0]/4+lo,PI[1]/4+hi
    lo,hi=atan_series_bounds(1/t,120)
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

# One-step killed moment matrix.
sqrtcI=I_from_bounds(*sqrt_bounds(c))
sqrtcP=[ipow(sqrtcI,k) for k in range(2*DEG+1)]
v1=1-c; h1=r-c
def mono_M(i,j):
    pair=(0,0)
    for aa in range(i+1):
      for bb in range(j+1):
        res=biv_moment(i-aa,j-bb,v1,h1)
        if res==0: continue
        term=imul(sqrtcP[aa+bb],trunc_negative_moment(aa+bb))
        term=iscale(term,F(comb(i,aa)*comb(j,bb))*res)
        pair=iadd(pair,term)
    return pair

q_exact=0
for i,ci in enumerate(PC):
    for j,cj in enumerate(PC):
        q_exact += ci*cj*std_moment(i+j)
qI=C(q_exact); assert qI[0]>0
mI=(0,0)
for i,ci in enumerate(PC):
    for j,cj in enumerate(PC):
        mI=iadd(mI,iscale(mono_M(i,j),F(ci*cj)))
muI=idiv(mI,qI)

# Two-step killed moment matrix for <Kf,Kf>.
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
for k in range(2,EXT): B[k]=iscale(B[k-2],F(k-1)*s2)
AA=[None]*EXT
AA[0]=iadd(C(F(1,4)),iscale(idiv(asinI,piI),F(1,2)))
AA[1]=iadd(iscale(tI,F(1,2)),imul(ratioI,B[0]))
for k in range(2,EXT):
    AA[k]=iadd(iscale(AA[k-2],k-1),imul(ratioI,B[k-1]))
Q=[[None]*EXT for _ in range(MAX+1)]
for n in range(EXT): Q[0][n]=AA[n]
for n in range(EXT-1):
    Q[1][n]=iadd(iscale(AA[n+1],c),imul(sI,B[n]))
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

# Coarse outward spectral data.
mu_lo=F(91219830,100000000)
mu_hi=F(91219831,100000000)
eps2_hi=F(25851,1000000000)
assert muI[0] > floor_frac(mu_lo*SCALE)
assert muI[1] < ceil_frac(mu_hi*SCALE)
assert eps2I[1] < ceil_frac(eps2_hi*SCALE)

# Safe hard-edge fourth-trace cap; this does not use the withdrawn
# scale-incorrect softened four-cycle normalization.
trace4_upper=F(553151,500000)
theta=F(343,2000)
xL=F(456233,500000)       # 0.912466
beta=F(80171,100000)       # 0.80171
# xL < r^(4 theta) iff xL^500 < r^343.
assert xL**500 < r**343
assert xL>mu_hi
assert beta**4 > trace4_upper-xL**4
assert mu_lo>beta
temple_lower=(xL-mu_hi)*(mu_lo-beta)
temple_margin=temple_lower-eps2_hi
assert temple_margin>0

# Exact covariance bridge at finite lags 1..5.
# R(u)=(-2u^10+5u^6+5u^4+2(1-u^4)^(5/2)-2)/(6u^5)
# and target t_k=c*r^(k-1). Rearranging gives 2(1-u^4)^(5/2)<A.
cov_margins=[]
for k in range(1,6):
    u=r**k
    tk=c*r**(k-1)
    A=6*u**5*tk+2*u**10-5*u**6-5*u**4+2
    margin=A*A-4*(1-u**4)**5
    assert A>0 and margin>0
    cov_margins.append(margin)

source_upper=F(1,4)
old=F(8497,50000)
new_width=source_upper-theta
old_width=source_upper-old

print('mu interval =',interval_float(muI))
print('eps2 interval =',interval_float(eps2I))
print('mu coarse =',mu_lo,mu_hi)
print('eps2 coarse upper =',eps2_hi,float(eps2_hi))
print('covariance finite margins =',[float(x) for x in cov_margins])
print('valid hard-edge trace cap =',trace4_upper,float(trace4_upper))
print('theta =',theta,float(theta))
print('xL =',xL,float(xL))
print('beta =',beta,float(beta))
print('Temple lower =',temple_lower,float(temple_lower))
print('Temple margin =',temple_margin,float(temple_margin))
print('old lower =',old,float(old),'old width =',old_width,float(old_width))
print('new lower =',theta,float(theta),'new width =',new_width,float(new_width))
print('source-level gain =',theta-old,float(theta-old))
print('ALL_EXACT_CHECKS_PASS = True')
