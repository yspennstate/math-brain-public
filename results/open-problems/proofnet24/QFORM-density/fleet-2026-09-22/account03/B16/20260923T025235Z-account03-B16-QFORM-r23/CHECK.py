from fractions import Fraction
from math import sqrt

m_lower=Fraction(31,128)
intersect=1-Fraction(256,961)
hll_heavy=intersect-Fraction(4,31)
hll_packet=m_lower*hll_heavy
hhl_heavy=intersect-Fraction(2,31)
hhl_packet=m_lower*(hhl_heavy/2)
cstar=Fraction(643,7936)
astar=Fraction(31,10288)
gstar=cstar/2
mstar=cstar/4
delta=Fraction(1,4096)
kstar=mstar-2*delta
pair=8*sqrt(5)*(float(gstar*kstar))**(-0.25)
beta=sqrt(1-float(astar)**2)

print('mixed_mass_lower', float(Fraction(31,64)))
print('dominant_class_lower', float(m_lower))
print('conditional_intersection_lower', float(intersect))
print('HLL_heavy_collision_lower', float(hll_heavy))
print('HLL_packet_lower', hll_packet, float(hll_packet))
print('HHL_heavy_collision_lower', float(hhl_heavy))
print('HHL_packet_lower', hhl_packet, float(hhl_packet))
print('cstar', cstar, float(cstar))
print('astar', astar, float(astar))
print('beta_lower', beta)
print('gstar', float(gstar), 'mstar', float(mstar), 'kstar', float(kstar))
print('pair_bound', pair)
assert hll_packet == Fraction(581,3968)
assert hhl_packet == cstar
assert astar == Fraction(31,10288)
assert kstar > 0 and pair < 107 and beta > 0.999995
print('QFORM_B16_R23_CHECK_PASS')
