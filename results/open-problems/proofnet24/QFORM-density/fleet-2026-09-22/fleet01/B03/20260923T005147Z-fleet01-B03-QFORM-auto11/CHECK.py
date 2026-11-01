import math

# Constants in REPORT.md
M0 = 4*math.sqrt(3)
I0 = 8*math.sqrt(2*math.pi)*3**0.25
c0 = math.sqrt(math.pi/3)/I0

assert abs(M0 - 6.928203230275509) < 1e-12
assert abs(I0 - 26.39126665899042) < 1e-12
assert abs(c0 - 0.03877520246258749) < 1e-14

# Scaling check for the star + rank-one-square family.
# Generic packet: 4 sqrt(3) c^(-2/3) lambda^(-1/3)
#                 * (M_Z M_U M_V)^(2/3)
# c=2, M_Z=1, M_U=sqrt(2)/|a|, M_V=sqrt(2), lambda=|b|.
def packet_density(a,b):
    generic = (4*math.sqrt(3)*(2**(-2/3))*abs(b)**(-1/3)
               *((math.sqrt(2)/abs(a))*math.sqrt(2))**(2/3))
    simplified = 4*math.sqrt(3)*abs(a)**(-2/3)*abs(b)**(-1/3)
    assert abs(generic-simplified) <= 1e-12*max(1,abs(simplified))
    return simplified

for a,b in [(1,1),(2,3),(0.7,4.0),(5.0,0.8)]:
    packet_density(a,b)

print('QFORM_B03_MIXED_HUB_BANK_PASS')
print('density_constant_a1_b1=', repr(M0))
print('collision_constant_a1_b1=', repr(I0))
print('local_global_ratio_constant=', repr(c0))
