#!/usr/bin/env python3
from fractions import Fraction as F

# PROB10-05 synthesis self-check.
# Inputs are two already archived exact certificates on current master:
# (i) PROB10-05 corrected circulant/Hermite trace: tr(K^4)<881/800;
# (ii) NM13-09 degree-48 scale-safe Ritz certificate:
#      9121983/1e7 < mu < 91219831/1e8, eps^2 < 25851/1e9.
# This checker verifies only the new exact Temple synthesis and source metric.

r=F(7,8)
trace4_cap=F(881,800)
mu_lo=F(9121983,10_000_000)
mu_hi=F(91219831,100_000_000)
eps2_hi=F(25851,1_000_000_000)

old_theta=F(343,2000)          # 0.1715, newest complementary repository bound
new_theta=F(8579,50000)        # 0.17158
x=F(456214,500000)             # 0.912428
beta=F(799297,1_000_000)       # 0.799297

# x < r^(4 theta), since 4*8579/50000 = 8579/12500.
power_ok = x**12500 < r**8579
assert power_ok

# If lambda_1 >= r^(4 theta) > x, fourth trace forces every non-Perron
# spectral value into (-beta,beta).
tail_margin = beta**4-(trace4_cap-x**4)
assert tail_margin>0
assert mu_lo>beta
assert x>mu_hi

# Temple contradiction with the degree-48 residual certificate.
temple_lower=(x-mu_hi)*(mu_lo-beta)
temple_margin=temple_lower-eps2_hi
assert temple_margin>0

old_width=F(1,4)-old_theta
new_width=F(1,4)-new_theta
assert new_width==F(3921,50000)
assert old_width-new_width==F(1,12500)

print('trace4 cap =',trace4_cap,float(trace4_cap))
print('mu bounds =',mu_lo,mu_hi,float(mu_lo),float(mu_hi))
print('eps2 upper =',eps2_hi,float(eps2_hi))
print('new theta =',new_theta,float(new_theta))
print('x =',x,float(x),'power check =',power_ok)
print('beta =',beta,float(beta))
print('tail margin =',tail_margin,float(tail_margin))
print('Temple lower =',temple_lower,float(temple_lower))
print('Temple margin =',temple_margin,float(temple_margin))
print('old width =',old_width,float(old_width))
print('new width =',new_width,float(new_width))
print('metric gain =',old_width-new_width,float(old_width-new_width))
print('ALL_EXACT_CHECKS_PASS = True')
