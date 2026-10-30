from math import sqrt

h0=63/64
star=sqrt(h0)*(247/504)
assert star>31/64
assert 247**2*63>1953**2

cross_bound=9.4*(h0*(2**-12)/16)**(-1/6)
assert cross_bound<60

# If D^2 nu < 2^-12 and det G>=1/16, innovation^2=nu/detG <2^-8 D^-2.
assert 16*(2**-12)==2**-8

print('hub_star_lower=',star)
print('31/64=',31/64)
print('projected_crossing_universal_bound=',cross_bound)
print('innovation_squared_factor=',2**-8)
print('innovation_norm_factor=',1/16)
print('STATUS=PASS')
