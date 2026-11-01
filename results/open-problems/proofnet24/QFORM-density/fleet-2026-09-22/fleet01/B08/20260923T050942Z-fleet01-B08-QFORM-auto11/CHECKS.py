import math

sqrt=math.sqrt
mu=1/3
kappa=sqrt(3/2)
alpha=0.5-kappa*mu
rho=sqrt(alpha/(1-alpha))
c0=0.5*rho
b0=0.5*rho*rho

assert abs(alpha-(3-sqrt(6))/6) < 1e-15
assert abs(rho*rho-(5-2*sqrt(6))) < 1e-15
assert abs(b0-(5-2*sqrt(6))/2) < 1e-15
assert alpha>0 and rho>0 and b0>0

CD=24*sqrt(math.e)/sqrt(5)
K5=5*sqrt(2*math.e)*(225/37)**0.1
K4=16.0626626053
theta=1/8
k0=CD/b0
k1d5=K5/(theta**(3/5))/b0
k1d3=CD*(15**(1/3))/(theta**(1/3))/b0
k2first=K4/(theta**(4/5))/b0
k2d5=120*K5/b0
k2d3=120*CD*(15**(1/3))/b0
assert k0 < 351
assert max(k1d5,k1d3) < 1729
assert k2first < 1679
assert max(k2d5,k2d3) < 103683
assert b0/8 > 0.00631
assert b0/120 > 0.000420

anchor3=b0**6/4
nested3=b0**6/8
assert anchor3 > 4.15e-9
assert nested3 > 2.07e-9
Cstar=10*sqrt(math.e)*(2**(1/5))*b0**(-6/5)
assert Cstar < 682

# Old alpha-factor transfer at the same floating cut would give alpha*(L*rho/2).
b_old=0.5*alpha*rho
assert b0 > b_old
assert abs(b0/b_old-rho/alpha) < 1e-12

print('alpha=',alpha)
print('rho=',rho)
print('child_scale=',c0)
print('cross_scale=',b0)
print('k0_paid=',k0)
print('k1_paid=',max(k1d5,k1d3))
print('k2_first_paid=',k2first)
print('k2_second_paid=',max(k2d5,k2d3))
print('rank1_tube=',b0/8)
print('rank2_tube=',b0/120)
print('k0_anchor3=',anchor3)
print('k0_nested3=',nested3)
print('k0_selfmatched_paid=',Cstar)
print('sharp/old_cross_scale_ratio=',b0/b_old)
print('QFORM_B08_FLOATING_SHARP_TRANSFER_CHECK_PASS')
