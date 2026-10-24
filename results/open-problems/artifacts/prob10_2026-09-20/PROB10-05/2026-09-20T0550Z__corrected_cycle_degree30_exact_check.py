#!/usr/bin/env python3
from fractions import Fraction as F
from math import isqrt, comb, factorial
from functools import lru_cache

# PROB10-05 exact self-check: corrected cycle normalization + degree-30 quasimode.
# All promoted finite inequalities use exact Fraction/integer arithmetic or
# outward rational fixed-point intervals.
DEG=30
SCALE=10**90
DROOT=10**120
PC=[
-403538617160325835501027,
1000000000000000000000000,
-237241954579029112959138,
-689157957755810506429109,
-19153851269648221180401,
455599874185879192752026,
48180060817640846262342,
-170698180749844123684386,
-20107899528441048743256,
38479331910270764041425,
4379885522368056353577,
-5522811764774798872508,
-585303627334720184566,
525456460191960377114,
51334400246640131740,
-34026947894303258728,
-3061600955126932760,
1521999895849587648,
126428497780439077,
-47202475057519965,
-3633028527321064,
1006715742695658,
72076250316713,
-14411711126658,
-963536311987,
131654879931,
8250012772,
-690410213,
-40688894,
1574956,
87570,
]
r=F(7,8)
s=F(24861,25000)
edge=F(1+r,2)
c=s*edge

a=(r+r**3)/(1+r**4)
b=2*r*r/(1+r**4)
G0=(1+r**4)/(1-r**4)
v_unit=(1+a)/(1+r)
g_unit=(1+b+2*a)/(2*(1+r))
h_unit=(a+b)/(1+r)
v_true=G0*v_unit
g_true=G0*g_unit
h_true=G0*h_unit
varV_true=s*v_true+(1-s)
rho_adj_true=s*g_true/varV_true
rho_opp_true=s*h_true/varV_true
varV_wrong=s*v_unit+(1-s)
rho_adj_wrong=s*g_unit/varV_wrong
rho_opp_wrong=s*h_unit/varV_wrong
assert G0>1
assert rho_adj_true>rho_adj_wrong
assert rho_opp_true>rho_opp_wrong
assert rho_adj_wrong==F(168557580,170952323)
assert rho_opp_wrong==F(167065920,170952323)

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
a5=atan_series_bounds(F(1,5),80); a239=atan_series_bounds(F(1,239),25)
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
    if t<=F(1,2): return atan_series_bounds(t,100)
    if t<=2:
        u=(t-1)/(t+1); lo,hi=atan_series_bounds(u,100)
        return PI[0]/4+lo,PI[1]/4+hi
    lo,hi=atan_series_bounds(1/t,100)
    return PI[0]/2-hi,PI[1]/2-lo
sqrt2pi=(sqrt_bounds(2*PI[0])[0],sqrt_bounds(2*PI[1])[1])
tI=I_from_bounds(1/sqrt2pi[1],1/sqrt2pi[0]); piI=I_from_bounds(*PI)

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

CD=11
Mmono=[[mono_M(i,j) for j in range(CD+1)] for i in range(CD+1)]
def He_coeff(n):
    out=[0]*(n+1); nf=factorial(n)
    for m in range(n//2+1):
        k=n-2*m
        out[k]=((-1)**m)*nf//(factorial(m)*factorial(k)*2**m)
    return out
Aherm=[[(0,0) for _ in range(CD+1)] for __ in range(CD+1)]
for i in range(CD+1):
    ci=He_coeff(i)
    for j in range(CD+1):
        cj=He_coeff(j); z=(0,0)
        for p,cp in enumerate(ci):
            if cp==0: continue
            for q,cq in enumerate(cj):
                if cq==0: continue
                z=iadd(z,iscale(Mmono[p][q],F(cp*cq)))
        Aherm[i][j]=z
Bmat=[[iscale(Aherm[i][j],F(1,factorial(i))) for j in range(CD+1)] for i in range(CD+1)]
def matmul(X,Y):
    n=len(X); Z=[[(0,0) for _ in range(n)] for __ in range(n)]
    for i in range(n):
      for k in range(n):
        xik=X[i][k]
        for j in range(n): Z[i][j]=iadd(Z[i][j],imul(xik,Y[k][j]))
    return Z
B2=matmul(Bmat,Bmat); B4=matmul(B2,B2)
trcomp=(0,0)
for i in range(CD+1): trcomp=iadd(trcomp,B4[i][i])
old_bad_cap=F(540899,500000)
assert trcomp[0] > floor_frac(old_bad_cap*SCALE)

q_exact=0
for i,ci in enumerate(PC):
    for j,cj in enumerate(PC): q_exact += ci*cj*std_moment(i+j)
qI=C(q_exact); assert qI[0]>0
mI=(0,0)
for i,ci in enumerate(PC):
    for j,cj in enumerate(PC): mI=iadd(mI,iscale(mono_M(i,j),F(ci*cj)))
muI=idiv(mI,qI)

MAX=2*DEG+2; EXT=3*DEG+12
s2=1-c*c; sqrt_s2=sqrt_bounds(s2); sI=I_from_bounds(*sqrt_s2)
ratioI=I_from_bounds(c/sqrt_s2[1],c/sqrt_s2[0])
asin_c=(atan_point_bounds(c/sqrt_s2[1])[0],atan_point_bounds(c/sqrt_s2[0])[1]); asinI=I_from_bounds(*asin_c)
B=[None]*EXT
B[0]=iscale(imul(sI,tI),F(1,2)); B[1]=iscale(imul(tI,tI),s2)
for k in range(2,EXT): B[k]=iscale(B[k-2],F(k-1)*s2)
AA=[None]*EXT
AA[0]=iadd(C(F(1,4)),iscale(idiv(asinI,piI),F(1,2)))
AA[1]=iadd(iscale(tI,F(1,2)),imul(ratioI,B[0]))
for k in range(2,EXT): AA[k]=iadd(iscale(AA[k-2],k-1),imul(ratioI,B[k-1]))
Q=[[None]*EXT for _ in range(MAX+1)]
for n in range(EXT): Q[0][n]=AA[n]
for n in range(EXT-1): Q[1][n]=iadd(iscale(AA[n+1],c),imul(sI,B[n]))
for mm in range(2,MAX+1):
    for n in range(EXT-mm): Q[mm][n]=iadd(iscale(Q[mm-1][n+1],c),iscale(Q[mm-2][n],F(mm-1)*s2))
for i in range(2*DEG+1):
    for j in range(2*DEG+1-i):
        qi,qj=Q[i][j],Q[j][i]
        assert max(qi[0],qj[0])<=min(qi[1],qj[1])
def q_negative(a,b):
    z=Q[a][b]
    return ineg(z) if (a+b)%2 else z

den=1-c*c
alpha_coef=(1-r*c)/den; beta_coef=(r-c)/den
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
        total=iadd(total,iscale(meanM[p-e][q-h],F(comb(p,e)*comb(q,h))*rm))
    condM[p][q]=total
nI=(0,0)
for i,ci in enumerate(PC):
    for j,cj in enumerate(PC): nI=iadd(nI,iscale(condM[i][j],F(ci*cj)))
nNormI=idiv(nI,qI)
eps2I=isub(nNormI,imul(muI,muI)); assert eps2I[0]>0

mu_lo=F(91208413,100000000)
mu_hi=F(91208414,100000000)
eps2_hi=F(126929,1000000000)
assert muI[0] > floor_frac(mu_lo*SCALE)
assert muI[1] < ceil_frac(mu_hi*SCALE)
assert eps2I[1] < ceil_frac(eps2_hi*SCALE)

trace4_upper=F(553151,500000)
theta=F(8497,50000)
xL=F(913227,1000000)
assert xL**12500 < r**8497
assert xL>mu_hi
beta=F(1601145,2000000)
assert beta**4 > trace4_upper-xL**4
assert mu_lo>beta
temple_lower=(xL-mu_hi)*(mu_lo-beta)
temple_margin=temple_lower-eps2_hi
assert temple_margin>0

old_valid=F(1647,10000)
source_upper=F(1,4)
old_valid_width=source_upper-old_valid
new_width=source_upper-theta

print('wrong rho_adj =',rho_adj_wrong,float(rho_adj_wrong))
print('true rho_adj =',rho_adj_true,float(rho_adj_true))
print('wrong rho_opp =',rho_opp_wrong,float(rho_opp_wrong))
print('true rho_opp =',rho_opp_true,float(rho_opp_true))
print('degree-11 compression trace4 interval =',interval_float(trcomp))
print('invalid old trace cap =',old_bad_cap,float(old_bad_cap))
print('mu interval =',interval_float(muI))
print('eps2 interval =',interval_float(eps2I))
print('mu coarse =',mu_lo,mu_hi)
print('eps2 coarse upper =',eps2_hi,float(eps2_hi))
print('valid hard-edge trace cap =',trace4_upper,float(trace4_upper))
print('xL =',xL,float(xL))
print('beta =',beta,float(beta))
print('Temple lower =',temple_lower,float(temple_lower))
print('Temple margin =',temple_margin,float(temple_margin))
print('old last unaffected lower =',old_valid,float(old_valid),'width =',old_valid_width,float(old_valid_width))
print('new lower =',theta,float(theta),'width =',new_width,float(new_width))
print('net gain over unaffected baseline =',theta-old_valid,float(theta-old_valid))
print('ALL_EXACT_CHECKS_PASS = True')