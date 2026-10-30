from fractions import Fraction as F
from math import factorial

def exp_partial(x,n):
    return sum(x**k / F(factorial(k)) for k in range(n+1))

def log_ratio_lower(x, terms):
    return 2*sum(x**(2*k+1)/F(2*k+1) for k in range(terms))

def atan_partial(x,n):
    return sum(((-1)**k)*x**(2*k+1)/F(2*k+1) for k in range(n))

eta=F(9337,100000)
zeta=F(869,250000)
target=F(1178,5)

sqrt2_up=F(70711,50000)
assert sqrt2_up**2 > 2
e_up=F(271829,100000)
assert exp_partial(F(1),10)+F(12,11*factorial(11)) < e_up
root_up=F(12849,10000)
assert root_up**6 > F(9,2)

atan5_up=atan_partial(F(1,5),5)
atan239_low=atan_partial(F(1,239),2)
pi_up=4*(4*atan5_up-atan239_low)
assert pi_up < F(355,113)

log2_up=F(173287,250000)
assert exp_partial(log2_up,7)>2
log19_up=F(73611,25000)
assert exp_partial(log19_up,14)>19

J_up=F(355,113)+4*log2_up+4+4*log19_up
c_up=8+2*log19_up

g3=F(62897,10**6)
rhs=1-eta-2*g3
assert rhs*rhs > 50*(eta*eta+zeta)
C3_up=3*sqrt2_up*e_up*root_up
assert C3_up < F(29637,2000)
assert target*g3 > F(29637,2000)

g2=F(219,1000)
rhs2=1-eta-2*g2
assert rhs2*rhs2 > 18*(eta*eta+zeta)
assert 2**23 * e_up**4 < F(121,10)**8
assert g2 > F(121,260)**2

assert zeta > F(8,33)**4
q=F(327263,100000)
assert q*q*eta>1
assert q+J_up/eta < target
assert q*26 < target
assert q*66 < target
assert 1+J_up*q < 72

assert zeta < F(1,256)
assert zeta > (c_up/target)**2
assert F(355,113) < c_up

# Lower barrier for this exact two-threshold proof architecture.
eta0=F(117,1250)
zeta0=F(349,100000)
pi_low=4*(4*atan_partial(F(1,5),4)-atan_partial(F(1,239),1))
assert pi_low > F(333,106)
assert log_ratio_lower(F(1,3),4) > F(6931,10000)
log19_low=4*log_ratio_lower(F(1,3),5)+log_ratio_lower(F(3,35),2)
assert log19_low > F(36805,12500)
J_low=F(333,106)+4*F(6931,10000)+4+4*F(36805,12500)
assert J_low > F(43383,2000)
assert F(163,50)**2*eta0 < 1
assert F(163,50)+F(43383,2000)/eta0 > 235

c_low=8+2*F(36805,12500)
assert c_low*c_low > F(235)**2*zeta0

sqrt2_low=F(7071,5000)
assert sqrt2_low**2 < 2
gamma_rhs=1-eta0-F(62,500)
assert (5*sqrt2_low)**2*(eta0*eta0+zeta0) > gamma_rhs*gamma_rhs

e_low=F(1359,500)
assert exp_partial(F(1),6) > e_low
root_low=F(321,250)
assert root_low**6 < F(9,2)
C3_low=3*sqrt2_low*e_low*root_low
assert C3_low > F(74,5)
assert F(74,5)/F(31,500)>235

print("ALL EXACT CERTIFICATES PASS")
print("C3 upper", float(C3_up))
print("J upper", float(J_up))
print("main scalar upper", float(q+J_up/eta))
print("half-moment diagonal upper", float(1+J_up*q))
print("architecture contradiction", float(F(74,5)/F(31,500)))
