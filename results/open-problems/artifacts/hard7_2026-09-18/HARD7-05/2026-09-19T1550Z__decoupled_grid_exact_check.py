#!/usr/bin/env python3
from fractions import Fraction as F
from math import isqrt

# HARD7-05 exact self-check:
# (i) decoupled grid/correlation Slepian comparison at q=661/1000,
#     rho=683387/10^6, using the inherited covariance envelope below r0;
# (ii) degree-5 Kato-Temple upper bound for the killed AR(1) operator K_rho;
# (iii) exact conversion to theta_{2,1/4} >= 146611/10^6.
# Every theorem-deciding comparison uses integer/rational arithmetic.
DROOT = 10**20
NATAN = 28
DEG = 5
MAXM = 2 * DEG

def C(x): return F(x), F(x)
def iadd(x,y): return x[0]+y[0], x[1]+y[1]
def iscale(c,x): return (c*x[0],c*x[1]) if c >= 0 else (c*x[1],c*x[0])
def imul(x,y):
    v=(x[0]*y[0],x[0]*y[1],x[1]*y[0],x[1]*y[1]); return min(v),max(v)
def idiv(x,y):
    assert y[0] > 0
    return imul(x,(1/y[1],1/y[0]))

def sqrt_point_bounds(x):
    assert x > 0
    m=isqrt((DROOT*DROOT*x.numerator)//x.denominator)
    lo,hi=F(m,DROOT),F(m+1,DROOT)
    assert lo*lo <= x < hi*hi
    return lo,hi

def sqrt_interval(I): return sqrt_point_bounds(I[0])[0],sqrt_point_bounds(I[1])[1]

def atan_series_bounds(x,m=NATAN):
    if x < 0:
        lo,hi=atan_series_bounds(-x,m); return -hi,-lo
    assert 0 <= x <= F(1,2)
    s=F(0)
    for k in range(m+1): s += F((-1)**k,2*k+1)*x**(2*k+1)
    nxt=F((-1)**(m+1),2*(m+1)+1)*x**(2*(m+1)+1)
    return min(s,s+nxt),max(s,s+nxt)

a5=atan_series_bounds(F(1,5),36)
a239=atan_series_bounds(F(1,239),10)
PI=(16*a5[0]-4*a239[1],16*a5[1]-4*a239[0])

def atan_point(t):
    if isinstance(t,tuple):
        lo,_=atan_point(t[0]); _,hi=atan_point(t[1]); return lo,hi
    if t < 0:
        lo,hi=atan_point(-t); return -hi,-lo
    if t <= F(1,2): return atan_series_bounds(t)
    if t <= 2:
        u=(t-1)/(t+1); lo,hi=atan_series_bounds(u)
        return PI[0]/4+lo,PI[1]/4+hi
    lo,hi=atan_series_bounds(1/t); return PI[0]/2-hi,PI[1]/2-lo

def asin_point(x):
    s=sqrt_point_bounds(1-x*x)
    return atan_point((x/s[1],x/s[0]))

def neglog_bounds(x,N=50):
    assert 0 < x < 1
    z=(1-x)/(1+x); partial=F(0)
    for k in range(N+1): partial += z**(2*k+1)/F(2*k+1)
    lo=2*partial; m=2*N+3
    tail=2*z**m/F(m)/(1-z*z)
    return lo,lo+tail

# 1. New source-side comparison: decouple grid q from AR correlation rho.
q=F(661,1000)
rho=F(683387,10**6)
r0=F(287831,500000)  # inherited exact envelope R(u)<=u for 0<u<=r0
assert rho > q
assert q*q < r0

# Exact source covariance formula inherited in HARD7-05:
# R(q)-q=(1-q^2)/(6q^5)*[-P(z)+2(1+z)(1-z^2)^(3/2)], z=q^2.
# Prove R(q)<rho by moving the rational terms to the right and squaring.
z=q*q
Pz=2+2*z-3*z*z-2*z**3-2*z**4
D=6*q**5*(rho-q)/(1-q*q)
T=Pz+D
lhs_sq=4*(1+z)**2*(1-z*z)**3
assert T > 0
assert lhs_sq < T*T

# 2. Exact degree-5 moments for K_rho and K_rho^2.
r=rho; R=r*r; s2=1-R
sI=sqrt_point_bounds(s2); gI=sqrt_point_bounds(1+R)
sqrt2piI=sqrt_interval((2*PI[0],2*PI[1]))
tI=(1/sqrt2piI[1],1/sqrt2piI[0]); t2I=imul(tI,tI); t3I=imul(t2I,tI)
aI=idiv(C(r),sI)
asinr=asin_point(r); asinR=asin_point(R); atanr=atan_point(r)
Porth=iadd(C(F(1,4)),iscale(F(1,2),idiv(asinr,PI)))

sPow=[C(1)]
for _ in range(1,MAXM+2): sPow.append(imul(sPow[-1],sI))
Gmom=[None]*(MAXM+1); Gmom[0]=C(F(1,2)); Gmom[1]=tI
for m in range(2,MAXM+1): Gmom[m]=iscale(m-1,Gmom[m-2])
G=[[Gmom[i+j] for j in range(DEG+1)] for i in range(DEG+1)]

B=[None]*(MAXM+1); B[0]=iscale(F(1,2),imul(sI,tI)); B[1]=iscale(s2,t2I)
for m in range(2,MAXM+1): B[m]=iscale((m-1)*s2,B[m-2])
A=[None]*(MAXM+1); A[0]=Porth; A[1]=iadd(iscale(F(1,2),tI),imul(aI,B[0]))
for m in range(2,MAXM+1): A[m]=iadd(iscale(m-1,A[m-2]),imul(aI,B[m-1]))

def poly_add(P1,P2):
    out=dict(P1)
    for k,v in P2.items(): out[k]=iadd(out.get(k,C(0)),v)
    return out
def poly_scale(P1,c): return {k:iscale(c,v) for k,v in P1.items()}
def poly_y_scale(P1,c): return {k+1:iscale(c,v) for k,v in P1.items()}

Jq=[{0:C(1)},{1:C(r)}]; Jp=[{},{0:sI}]
for n in range(2,DEG+1):
    Jq.append(poly_add(poly_y_scale(Jq[n-1],r),poly_scale(Jq[n-2],(n-1)*s2)))
    Jp.append(poly_add(poly_y_scale(Jp[n-1],r),poly_scale(Jp[n-2],(n-1)*s2)))

def int_poly(poly,shift,seq):
    out=C(0)
    for p,coeff in poly.items(): out=iadd(out,imul(coeff,seq[p+shift]))
    return out

M=[[iadd(int_poly(Jq[j],i,A),int_poly(Jp[j],i,B)) for j in range(DEG+1)] for i in range(DEG+1)]
for i in range(DEG+1):
    for j in range(DEG+1): assert max(M[i][j][0],M[j][i][0]) <= min(M[i][j][1],M[j][i][1])

H=[None]*MAXM; H[0]=iscale(F(1,2),idiv(tI,gI)); H[1]=idiv(t2I,C(1+R))
for m in range(2,MAXM): H[m]=iscale(m-1,idiv(H[m-2],C(1+R)))
Qm=[None]*MAXM; Qm[0]=iadd(C(F(1,4)),iscale(F(1,2),idiv(atanr,PI)))
Qm[1]=iadd(iscale(F(1,2),tI),iscale(r,H[0]))
for m in range(2,MAXM): Qm[m]=iadd(iscale(m-1,Qm[m-2]),iscale(r,H[m-1]))
V=[imul(imul(sPow[m+1],tI),Qm[m]) for m in range(MAXM)]
tau=idiv(sI,gI); tau2=imul(tau,tau)
W=[None]*(MAXM-1); W[0]=iscale(F(1,2),imul(tau,t2I)); W[1]=imul(tau2,t3I)
for m in range(2,MAXM-1): W[m]=iscale(m-1,imul(tau2,W[m-2]))
U=[None]*(MAXM+1)
U[0]=iadd(C(F(1,8)),iscale(F(1,4),idiv(iadd(iscale(2,asinr),asinR),PI)))
U[1]=iadd(iscale(F(1,4),tI),iscale(2,imul(aI,V[0])))
for m in range(2,MAXM+1): U[m]=iadd(iscale(m-1,U[m-2]),iscale(2,imul(aI,V[m-1])))

def Nij(i,j):
    out=C(0)
    for p,c1 in Jq[i].items():
        for q0,c2 in Jq[j].items(): out=iadd(out,imul(imul(c1,c2),U[p+q0]))
    for p,c1 in Jq[i].items():
        for q0,c2 in Jp[j].items(): out=iadd(out,imul(imul(c1,c2),V[p+q0]))
    for p,c1 in Jp[i].items():
        for q0,c2 in Jq[j].items(): out=iadd(out,imul(imul(c1,c2),V[p+q0]))
    for p,c1 in Jp[i].items():
        for q0,c2 in Jp[j].items(): out=iadd(out,imul(imul(c1,c2),W[p+q0]))
    return out
N=[[Nij(i,j) for j in range(DEG+1)] for i in range(DEG+1)]
for i in range(DEG+1):
    for j in range(DEG+1): assert max(N[i][j][0],N[j][i][0]) <= min(N[i][j][1],N[j][i][1])

# Rational degree-5 trial vector fixed before checker construction.
c=[F(x) for x in (100000000,89568199,19343854,-12359986,2685150,-209252)]
def quad_interval(Mat):
    out=C(0)
    for i in range(DEG+1):
        for j in range(DEG+1): out=iadd(out,iscale(c[i]*c[j],Mat[i][j]))
    return out
qI=quad_interval(G); mI=quad_interval(M); nrawI=quad_interval(N)
assert qI[0] > 0 and mI[0] > 0 and nrawI[0] > 0
muI=idiv(mI,qI); nI=idiv(nrawI,qI)
eps2_lo=nI[0]-muI[1]**2; eps2_hi=nI[1]-muI[0]**2
assert 0 < eps2_lo <= eps2_hi < F(9,10**9)

# Exact Hilbert-Schmidt trace:
# tr K^2=[1/4+asin(2r/(1+r^2))/(2pi)]/(1-r^2).
corr2=F(2)*r/(1+R); asin_corr2=asin_point(corr2)
p2I=iadd(C(F(1,4)),iscale(F(1,2),idiv(asin_corr2,PI)))
trace2I=idiv(p2I,C(1-R))

# lambda2^2 <= tr K^2-lambda1^2 <= tr K^2-mu^2.
beta=F(461,1000)
spectral_remainder_upper=trace2I[1]-muI[0]**2
assert spectral_remainder_upper < beta**2
assert muI[0] > beta

# Kato-Temple top-eigenvalue enclosure.
lambda1_upper=muI[1]+eps2_hi/(muI[0]-beta)
LAMBDA_CAP=F(784437,10**6)
assert lambda1_upper < LAMBDA_CAP

# Delta=4(-log q), theta >= -log(lambda1)/Delta.
target=F(146611,10**6)
neglog_cap=neglog_bounds(LAMBDA_CAP,52); neglog_q=neglog_bounds(q,52)
log_margin=neglog_cap[0]-4*target*neglog_q[1]
assert log_margin > 0

old_lower=F(14344477,10**8); old_width=F(10655523,10**8)
new_width=F(1,4)-target; improvement=target-old_lower
assert new_width == F(103389,10**6)
assert old_width-new_width == improvement

print('q_grid =',float(q))
print('rho_AR =',float(rho))
print('q^2 =',float(q*q),'< inherited r0 =',float(r0))
print('source_covariance_one_step_margin_squared =',float(T*T-lhs_sq))
print('degree =',DEG)
print('mu interval =',float(muI[0]),float(muI[1]))
print('normalized K2 interval =',float(nI[0]),float(nI[1]))
print('residual^2 interval =',float(eps2_lo),float(eps2_hi))
print('trace K^2 interval =',float(trace2I[0]),float(trace2I[1]))
print('spectral remainder upper =',float(spectral_remainder_upper))
print('beta^2 =',float(beta**2))
print('Kato lambda1 upper =',float(lambda1_upper))
print('rational lambda1 cap =',float(LAMBDA_CAP))
print('log comparison margin =',float(log_margin))
print('old theta lower =',float(old_lower))
print('certified theta lower =',float(target))
print('new bracket width =',float(new_width))
print('width improvement =',float(improvement))
print('ALL_EXACT_CHECKS_PASS = True')
