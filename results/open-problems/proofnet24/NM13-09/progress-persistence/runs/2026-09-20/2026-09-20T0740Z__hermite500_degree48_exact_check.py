#!/usr/bin/env python3
from fractions import Fraction as F
from math import isqrt, factorial

# NM13-09 / T05 exact self-check.
# New finite core: extend the corrected circulant/Hermite trace expansion to M=500,
# then combine it with the already certified degree-48 Ritz/residual bounds.
# All promoted inequalities below use exact Fraction/integer arithmetic plus
# outward rational enclosures for sqrt, pi and arctangent.

r=F(7,8)
s=F(24861,25000)
c=s*F(1+r,2)

# Correctly scaled four-cycle correlations.
a=(r+r**3)/(1+r**4)
b=2*r*r/(1+r**4)
G0=(1+r**4)/(1-r**4)
v_unit=(1+a)/(1+r)
g_unit=(1+b+2*a)/(2*(1+r))
h_unit=(a+b)/(1+r)
v_true=G0*v_unit
g_true=G0*g_unit
h_true=G0*h_unit
varV=s*v_true+(1-s)
u=s*g_true/varV
v=s*h_true/varV
assert u==F(11237172,11352323)
assert v==F(11137728,11352323)
q=2*u/(1+v)
A=(1+v)/(1-v)
assert q==F(198888,199027)
assert A==F(22490051,214595)
assert 0<v<u<1 and 0<q<1 and A>1

# Outward rational interval helpers.
DROOT=10**90
def sqrt_bounds(x):
    x=F(x); assert x>=0
    if x==0: return F(0),F(0)
    m=isqrt((DROOT*DROOT*x.numerator)//x.denominator)
    lo,hi=F(m,DROOT),F(m+1,DROOT)
    assert lo*lo<=x<hi*hi
    return lo,hi

def atan_series_bounds(x,m=120):
    x=F(x); assert 0<=x<1
    z=F(0)
    for k in range(m+1):
        z += F((-1)**k,2*k+1)*x**(2*k+1)
    nxt=F((-1)**(m+1),2*(m+1)+1)*x**(2*(m+1)+1)
    return min(z,z+nxt),max(z,z+nxt)

a5=atan_series_bounds(F(1,5),80)
a239=atan_series_bounds(F(1,239),25)
PI=(16*a5[0]-4*a239[1],16*a5[1]-4*a239[0])
assert PI[0]>3 and PI[1]<4

def atan_pos_interval(lo,hi):
    lo,hi=F(lo),F(hi); assert 0<=lo<=hi
    if hi<1:
        return atan_series_bounds(lo)[0],atan_series_bounds(hi)[1]
    assert lo>1
    alo=atan_series_bounds(1/hi)[0]
    ahi=atan_series_bounds(1/lo)[1]
    return PI[0]/2-ahi,PI[1]/2-alo

def iadd(x,y): return x[0]+y[0],x[1]+y[1]
def imul(x,y):
    z=(x[0]*y[0],x[0]*y[1],x[1]*y[0],x[1]*y[1])
    return min(z),max(z)
def iscale(x,c0):
    c0=F(c0)
    return (x[0]*c0,x[1]*c0) if c0>=0 else (x[1]*c0,x[0]*c0)
def idivpos(x,y):
    assert y[0]>0
    return imul(x,(1/y[1],1/y[0]))
def isquare(x):
    if x[0]<=0<=x[1]:
        return F(0),max(x[0]*x[0],x[1]*x[1])
    return min(x[0]*x[0],x[1]*x[1]),max(x[0]*x[0],x[1]*x[1])

# For g_a(z)=1_{z>0}(2 Phi(sqrt(A) z)-1):
# m=E g_a(Z)=atan(sqrt(A))/pi
# e2=E g_a(Z)^2=atan(A/sqrt(1+2A))/pi.
sqrtA=sqrt_bounds(A)
atanA=atan_pos_interval(*sqrtA)
mI=(atanA[0]/PI[1],atanA[1]/PI[0])
sqrtB=sqrt_bounds(1+2*A)
arg2=(A/sqrtB[1],A/sqrtB[0])
atan2=atan_pos_interval(*arg2)
e2I=(atan2[0]/PI[1],atan2[1]/PI[0])

# Hermite coefficients d_n = E[g_a(Z) He_n(Z)].
h=1+A
base=(sqrt_bounds(PI[0]/(2*h))[0],sqrt_bounds(PI[1]/(2*h))[1])
def half_moment(k):
    if k%2:
        j=(k-1)//2
        z=F((2**j)*factorial(j),1)/h**(j+1)
        return z,z
    j=k//2
    df=1
    for t in range(1,2*j,2):
        df*=t
    return iscale(base,F(df,1)/h**j)

def he_coeff(n):
    out=[0]*(n+1)
    nf=factorial(n)
    for j in range(n//2+1):
        k=n-2*j
        out[k]=((-1)**j)*nf//(factorial(j)*factorial(k)*2**j)
    return out

def d_interval(n):
    total=(F(0),F(0))
    for k,ck in enumerate(he_coeff(n-1)):
        if ck:
            total=iadd(total,iscale(half_moment(k),ck))
    return idivpos(imul(sqrtA,total),PI)

# Positive Hermite/Mehler expansion:
# p4 = m^2 + sum_{n>=1} q^n w_n, w_n=d_n^2/n! >=0.
# Parseval gives sum_{n>=1} w_n=e2-m^2.
# Hence for M>=1,
# p4 <= (1-q^(M+1))m^2 + q^(M+1)e2
#        + sum_{n=1}^M (q^n-q^(M+1))w_n.
M=500
qt=q**(M+1)
p_upper=(1-qt)*isquare(mI)[1]+qt*e2I[1]
for n in range(1,M+1):
    wi=isquare(d_interval(n))[1]/factorial(n)
    p_upper += (q**n-qt)*wi

trace_upper=p_upper/(1-r**4)
trace_cap=F(54959,50000)   # 1.09918
trace_margin=trace_cap-trace_upper
assert trace_margin>0

# Certified degree-48 spectral data from the preceding NM13-09 exact checker.
mu_lo=F(91219830,100000000)
mu_hi=F(91219831,100000000)
eps2_hi=F(25851,1000000000)
assert mu_lo<mu_hi

# New source endpoint theta*=0.171587.
theta=F(171587,1000000)
xL=F(45621267,50000000)   # 0.91242534
beta=F(798281,1000000)    # 0.798281

# xL < r^(4 theta): 4 theta = 171587/250000.
assert xL**250000 < r**171587
assert xL>mu_hi

# Fourth-trace tail separation and Temple contradiction.
tail_margin=beta**4-(trace_cap-xL**4)
assert tail_margin>0
assert mu_lo>beta
temple_lower=(xL-mu_hi)*(mu_lo-beta)
temple_margin=temple_lower-eps2_hi
assert temple_margin>0

# Re-execute the exact finite-lag covariance comparison for k=1,...,5.
cov_margins=[]
for k in range(1,6):
    uu=r**k
    tk=c*r**(k-1)
    AA=6*uu**5*tk+2*uu**10-5*uu**6-5*uu**4+2
    margin=AA*AA-4*(1-uu**4)**5
    assert AA>0 and margin>0
    cov_margins.append(margin)

old=F(343,2000)
source_upper=F(1,4)
old_width=source_upper-old
new_width=source_upper-theta
assert theta>old
assert new_width<old_width

print("M =",M)
print("corrected rho_adj =",u,float(u))
print("corrected rho_opp =",v,float(v))
print("q =",q,float(q))
print("A =",A,float(A))
print("Hermite p4 upper <",float(p_upper))
print("trace4 upper <",float(trace_upper))
print("trace cap =",trace_cap,float(trace_cap))
print("trace margin >",float(trace_margin))
print("covariance finite margins =",[float(z) for z in cov_margins])
print("mu coarse =",mu_lo,mu_hi)
print("eps2 coarse upper =",eps2_hi,float(eps2_hi))
print("theta =",theta,float(theta))
print("xL =",xL,float(xL),"power check =",xL**250000 < r**171587)
print("beta =",beta,float(beta))
print("tail margin >",float(tail_margin))
print("Temple lower >",float(temple_lower))
print("Temple contradiction margin >",float(temple_margin))
print("old lower =",old,float(old),"old width =",float(old_width))
print("new lower =",theta,float(theta),"new width =",float(new_width))
print("source-level gain =",float(theta-old))
print("ALL_EXACT_CHECKS_PASS = True")
