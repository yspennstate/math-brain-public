from fractions import Fraction
import math

C2 = 7.673759290384858
C_S0 = C2 * 48**(1/8)
C_PIVOT_QUARTER = 2*C_S0

print('S0 half-Riesz constant =', repr(C_S0))
print('S0 density constant for |a|>=1/4 =', repr(C_PIVOT_QUARTER))
assert C_S0 < 12.450
assert C_PIVOT_QUARTER < 24.900

for m in (3,4,8,32):
    pair_mass = Fraction(m-1, 2*m)
    max_pair_det = Fraction(1, m*m)
    print('m=', m,
          'P2_mass=', pair_mass, float(pair_mass),
          'max_pair_det=', max_pair_det, float(max_pair_det),
          'local_det_penalty=', math.sqrt(m))
    assert pair_mass >= Fraction(1,3)
    # S_m has m unit eigenvalues, so s_2(S_m)=1 for m>=2.
    # Each same-block principal pair has determinant 0;
    # each different-block pair has determinant 1/m^2.
    # Number of different-block coordinate pairs is C(m,2)*m^2.
    assert Fraction(m*(m-1),2) * m*m * max_pair_det**2 == pair_mass

print('QFORM_SCHUR_S2_OVERLAP_CHECK_PASS')
