from fractions import Fraction as F

# Exact rational interval arithmetic. No floating point is used in any assertion.

def iadd(a,b): return (a[0]+b[0], a[1]+b[1])
def ineg(a): return (-a[1], -a[0])
def isub(a,b): return iadd(a, ineg(b))
def imul(a,b):
    xs = [a[0]*b[0], a[0]*b[1], a[1]*b[0], a[1]*b[1]]
    return (min(xs), max(xs))
def iscale(c,a): return imul((F(c),F(c)),a)
def ipow(a,n):
    r=(F(1),F(1))
    for _ in range(n):
        r=imul(r,a)
    return r

# For x>1 rational, log x = 2 sum_{k>=0} y^(2k+1)/(2k+1),
# y=(x-1)/(x+1). The tail is bounded above by
# 2*y^(2N+3)/((2N+3)*(1-y^2)).
def log_interval(x,N=20):
    assert x>0
    if x==1: return (F(0),F(0))
    if x<1:
        lo,hi=log_interval(1/x,N)
        return (-hi,-lo)
    y=(x-1)/(x+1)
    s=F(0)
    for k in range(N+1):
        s += y**(2*k+1)/F(2*k+1)
    lo=2*s
    rem=2*y**(2*N+3)/(F(2*N+3)*(1-y*y))
    return (lo,lo+rem)

eu=F(6909,6820)
ev=F(12267,10540)
S=2*eu+2*ev-3
assert S==F(7848,5797)
ru=eu/S
rv=ev/S
u=log_interval(eu)
v=log_interval(ev)
logS=log_interval(S)

# Exact earlier n=4 candidate:
# q=(u,u,v,v), h=(9/5,9/5,-1/5,-1/5).
hu=F(9,5); hv=F(-1,5)

Mh=2*ru*hu+2*rv*hv
Mh2=2*ru*hu**2+2*rv*hv**2
Mh3=2*ru*hu**3+2*rv*hv**3
Mh4=2*ru*hu**4+2*rv*hv**4
L4=Mh4-4*Mh*Mh3-3*Mh2**2+12*Mh**2*Mh2-6*Mh**4
assert L4==F(3950752179,950480000)

def lin2(cu,cv):
    return iadd(iscale(cu,u),iscale(cv,v))

Mq=lin2(2*ru,2*rv)
Mqh=lin2(2*ru*hu,2*rv*hv)
Mqh2=lin2(2*ru*hu**2,2*rv*hv**2)
Mq2=iadd(iscale(2*ru,ipow(u,2)),iscale(2*rv,ipow(v,2)))

# b = D^3 log S(q)[q,h,h].
b=isub(isub(iadd(Mqh2,iscale(2*Mh**2,Mq)),
                imul(Mq,(Mh2,Mh2))),
         iscale(2*Mh,Mqh))

# K(q)=2 log S -2 Mq + Mq2 - Mq^2 = -g_q''(1)>0.
K=iadd(iscale(2,logS),ineg(iscale(2,Mq)))
K=iadd(K,Mq2)
K=isub(K,ipow(Mq,2))

# Necessary projective fourth-order margin:
# Delta = D_h^4 log S * K - 3 (D^3 log S[q,h,h])^2.
Delta=isub(iscale(L4,K),iscale(3,ipow(b,2)))

# Exact rational comparisons.
assert K[0] > F(6,1000)
assert K[1] < F(7,1000)
assert b[0] > F(1871,1000)
assert b[1] < F(1873,1000)
assert L4 > F(4)
assert Delta[1] < F(-10)

print("EXACT_RATIONAL_INTERVAL_CHECK")
print("S=7848/5797")
print("D4_logS_hhhh=3950752179/950480000 > 4")
print("0.006 < K(q) < 0.007")
print("1.871 < D3_logS[q,h,h] < 1.873")
print("Delta = D4*K - 3*D3^2 < -10")
print("PROJECTIVE_FOURTH_ORDER_NECESSARY_CONDITION_VIOLATED")
print("ALL_EXACT_CHECKS_PASS")
