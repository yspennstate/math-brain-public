#!/usr/bin/env python3
from fractions import Fraction as F
from math import comb

# Rigorous rational bounds for ln(q) from the atanh series.
def ln_bounds(q: F, n=1200):
    if q <= 0:
        raise ValueError(q)
    if q == 1:
        return F(0), F(0)
    if q < 1:
        lo, hi = ln_bounds(1/q, n)
        return -hi, -lo
    y = (q-1)/(q+1)
    y2 = y*y
    term = y
    s = F(0)
    for k in range(n):
        s += term/F(2*k+1)
        term *= y2
    lo = 2*s
    # tail starts with y^(2n+1)/(2n+1), bound denominators by first denominator
    tail = 2*term/(F(2*n+1)*(1-y2))
    return lo, lo+tail

LN2_LO,LN2_HI=ln_bounds(F(2))
LN10_LO,LN10_HI=ln_bounds(F(10))
assert LN2_LO > F(69,100)
assert LN2_HI < F(7,10)
assert LN10_LO > F(1151,500)   # 2.302
assert LN10_HI < F(2303,1000)  # 2.303

# Binary entropy interval in bits, exact input q.
def h2_bounds(q: F):
    if q == 0 or q == 1:
        return F(0),F(0)
    a_lo,a_hi=ln_bounds(1/q)
    b_lo,b_hi=ln_bounds(1/(1-q))
    num_lo=q*a_lo+(1-q)*b_lo
    num_hi=q*a_hi+(1-q)*b_hi
    return num_lo/LN2_HI, num_hi/LN2_LO

# Boolean-realizable dyadic adversary: residual x in Q_10, g=-1 on 235 points.
d=F(235,1024)
b=1-2*d
m=(1+b*b)/2
x=b*b/(1+b*b)
theta=d*d/m
hx_lo,hx_hi=h2_bounds(x)
ht_lo,ht_hi=h2_bounds(theta)
# Exact local center threshold Q(d) = [2-m-m*h2(x)+m*h2(theta)]/d.
Q_lo=(2-m-m*hx_hi+m*ht_lo)/d
Q_hi=(2-m-m*hx_lo+m*ht_hi)/d
assert Q_lo > F(48723,10000)
assert Q_hi < F(48724,10000)

# Actual Boolean realization on pivot t, character y, and 10 residual bits.
# f_0=(-1)^y, f_1=(-1)^y g(x), with g=-1 on x=0,...,234.
N=1<<12
vals=[]
diff=0
for z in range(N):
    xval=z & ((1<<10)-1)
    y=(z>>10)&1
    t=(z>>11)&1
    g=-1 if xval < 235 else 1
    f0=-1 if y else 1
    f1=f0*g
    if f0 != f1:
        diff += 1
    vals.append(f0 if t==0 else f1)
assert sum(vals)==0
# diff counts each x,y,t; disagreement independent of t, so fraction diff/N=d.
assert F(diff,N)==d

# Analytic 5.1 upper certificate.
# Lower-bound branch entropy by h2(u)>=4u(1-u), and upper-bound
# h2(theta)<=theta*log2(e/theta). This reduces the required center to
# U(d)=A(d)+d log2(e*m/d^2), where
# A(d)=4(1-d)(d^2-d+1)/m, m=2d^2-2d+1.
# Its second derivative satisfies U''<=-16 on (0,1/2].
# We certify the polynomial positivity used in that proof in Bernstein form.
bern=[F(5),F(11,6),F(7,5),F(39,20),F(13,4),F(41,8),F(31,4)]
assert all(v>0 for v in bern)
# These are the degree-6 Bernstein coefficients on t=2d of
# 112 d^6-280 d^5+364 d^4-280 d^3+164 d^2-38 d+5.

# At d0=1/4, coarse rigorous log bounds give U(d0)<U0_bound.
U0_bound=F(39,10)+F(1,4)*F(3303,1000)/F(69,100)
# U'(1/4)=-34/25+(ln 10-7/5)/ln 2 lies in [p_lo,p_hi].
p_lo=-F(34,25)+(F(2302,1000)-F(7,5))/F(7,10)
p_hi=-F(34,25)+(F(2303,1000)-F(7,5))/F(69,100)
assert p_lo < p_hi < 0
pabs=max(abs(p_lo),abs(p_hi))
# Strong concavity U''<=-16 yields sup U <= U0+p^2/32.
U_sup_bound=U0_bound+pabs*pabs/F(32)
assert U_sup_bound < F(51,10)

print('PASS')
print('ln2_bounds', float(LN2_LO), float(LN2_HI))
print('ln10_bounds', float(LN10_LO), float(LN10_HI))
print('dyadic_d', f'{d.numerator}/{d.denominator}', float(d))
print('Q_d_lower', float(Q_lo))
print('Q_d_upper', float(Q_hi))
print('U0_upper', float(U0_bound))
print('Uprime_quarter_interval', float(p_lo), float(p_hi))
print('U_global_upper', float(U_sup_bound))
