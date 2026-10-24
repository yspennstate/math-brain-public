#!/usr/bin/env python3
from fractions import Fraction as F
from math import isqrt, factorial

# PROB10-05 exact self-check: corrected circulant/Hermite fourth-trace bound.
# The finite inequalities deciding the promoted claim use exact Fraction arithmetic
# plus outward rational enclosures for pi, square roots and arctangent.

r=F(7,8)
s=F(24861,25000)
edge=F(1+r,2)
c0=s*edge

# Re-derive the corrected cyclic loop scale and correlations; do NOT use the
# withdrawn unit-variance loop substitution from the superseded trace chain.
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
assert 0<v<u<1

# Circulant covariance eigenvalues: 1+2u+v, 1-v (double), 1-2u+v.
assert 1+2*u+v>0
assert 1-v>0
assert 1-2*u+v>0
q=2*u/(1+v)
A=(1+v)/(1-v)  # a_cone^2
assert 0<q<1 and A>1

# Exact rational interval helpers.
DROOT=10**90
def floor_frac(x): return x.numerator//x.denominator
def ceil_frac(x): return -((-x.numerator)//x.denominator)
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
    if lo>1:
        alo=atan_series_bounds(1/hi)[0]
        ahi=atan_series_bounds(1/lo)[1]
        return PI[0]/2-ahi,PI[1]/2-alo
    raise AssertionError('interval straddles 1')

def iadd(x,y): return x[0]+y[0],x[1]+y[1]
def imul(x,y):
    z=(x[0]*y[0],x[0]*y[1],x[1]*y[0],x[1]*y[1])
    return min(z),max(z)
def iscale(x,c):
    c=F(c)
    return (x[0]*c,x[1]*c) if c>=0 else (x[1]*c,x[0]*c)
def idivpos(x,y):
    assert y[0]>0
    return imul(x,(1/y[1],1/y[0]))
def isquare(x):
    if x[0]<=0<=x[1]: return F(0),max(x[0]*x[0],x[1]*x[1])
    return min(x[0]*x[0],x[1]*x[1]),max(x[0]*x[0],x[1]*x[1])

# Cone mean m=atan(sqrt(A))/pi.
sqrtA=sqrt_bounds(A)
atanA=atan_pos_interval(*sqrtA)
mI=(atanA[0]/PI[1],atanA[1]/PI[0])

# Cone second moment E g^2 = atan(A/sqrt(1+2A))/pi.
sqrtB=sqrt_bounds(1+2*A)
arg2=(A/sqrtB[1],A/sqrtB[0])
atan2=atan_pos_interval(*arg2)
e2I=(atan2[0]/PI[1],atan2[1]/PI[0])
assert 0<mI[0]<=mI[1]<F(1,2)
assert 0<e2I[0]<=e2I[1]<F(1,2)

# d_n = (sqrt(A)/pi) int_0^inf He_{n-1}(x) exp(-(1+A)x^2/2) dx.
h=1+A
base_lo=sqrt_bounds(PI[0]/(2*h))[0]
base_hi=sqrt_bounds(PI[1]/(2*h))[1]
base=(base_lo,base_hi)
def half_moment(k):
    # integral_0^inf x^k exp(-h x^2/2) dx
    if k%2:
        j=(k-1)//2
        z=F((2**j)*factorial(j),1)/h**(j+1)
        return z,z
    j=k//2
    df=1
    for t in range(1,2*j,2): df*=t
    return iscale(base,F(df,1)/h**j)
def he_coeff(n):
    out=[0]*(n+1); nf=factorial(n)
    for j in range(n//2+1):
        k=n-2*j
        out[k]=((-1)**j)*nf//(factorial(j)*factorial(k)*2**j)
    return out
def d_interval(n):
    total=(F(0),F(0))
    for k,ck in enumerate(he_coeff(n-1)):
        if ck: total=iadd(total,iscale(half_moment(k),ck))
    return idivpos(imul(sqrtA,total),PI)

M=10
m2_hi=isquare(mI)[1]
e2_hi=e2I[1]
qt=q**(M+1)
p_upper=(1-qt)*m2_hi+qt*e2_hi
w_hi=[]
for n in range(1,M+1):
    dI=d_interval(n)
    wi=isquare(dI)[1]/factorial(n)
    w_hi.append(wi)
    p_upper += (q**n-qt)*wi

# Exact trace normalization from the AR four-cycle loop.
trace_upper=p_upper/(1-r**4)
trace_cap=F(4405,4000)  # 1.10125
trace_margin=trace_cap-trace_upper
assert trace_margin>0

# Inherited exact degree-30 quasimode coarsenings from the immediately previous
# corrected checker; here they are inputs to an independent new trace refinement.
mu_lo=F(91208413,100000000)
mu_hi=F(91208414,100000000)
eps2_hi=F(126929,1000000000)
assert mu_lo<mu_hi

# Clean source milestone theta*=17/100. xL^25 < r^17 proves
# xL < r^(17/25)=r^(4 theta*).
theta=F(17,100)
xL=F(913199,1000000)
assert xL**25<r**17
assert xL>mu_hi

# If lambda_1 >= r^(4 theta), then every non-Perron spectral value has
# |lambda_j|^4 < trace_cap-xL^4. beta is an exact safe separator.
beta=F(79815,100000)
tail_margin=beta**4-(trace_cap-xL**4)
assert tail_margin>0
assert mu_lo>beta

# Temple residual contradiction.
temple_lower=(xL-mu_hi)*(mu_lo-beta)
temple_margin=temple_lower-eps2_hi
assert temple_margin>0

old_lower=F(8497,50000)
old_width=F(1,4)-old_lower
new_width=F(1,4)-theta
assert old_width==F(4003,50000)
assert new_width==F(2,25)
assert old_width-new_width==F(3,50000)

print('corrected rho_adj =',u,float(u))
print('corrected rho_opp =',v,float(v))
print('q =',q,float(q))
print('cone A =',A,float(A))
print('m interval =',float(mI[0]),float(mI[1]))
print('Eg2 interval =',float(e2I[0]),float(e2I[1]))
for n,wi in enumerate(w_hi,1): print('w%d upper ='%n,float(wi))
print('Hermite p4 upper <',float(p_upper))
print('trace4 upper <',float(trace_upper))
print('trace cap =',trace_cap,float(trace_cap))
print('trace margin >',float(trace_margin))
print('xL =',xL,float(xL),'power check =',xL**25<r**17)
print('beta =',beta,float(beta))
print('tail margin >',float(tail_margin))
print('Temple lower >',float(temple_lower))
print('Temple contradiction margin >',float(temple_margin))
print('old lower =',old_lower,float(old_lower),'old width =',float(old_width))
print('new lower =',theta,float(theta),'new width =',float(new_width))
print('metric improvement =',float(old_width-new_width))
print('ALL_EXACT_CHECKS_PASS = True')
