from fractions import Fraction
from math import pi, sqrt

C3 = 2*pi + 3*sqrt(3)

# Exact orientation-free cover.
theta = Fraction(983, 1000)
pair_margin = 1 - theta
triple_margin = Fraction(3, 2)*theta - 1
assert pair_margin == Fraction(17, 1000)
assert triple_margin == Fraction(949, 2000)
C_pair = pi / sqrt(float(pair_margin))
C_triple = C3 / float(triple_margin)
C_orient = max(C_pair, C_triple)
assert C_orient < 24.193

# One-percent perturbative stability cover.
theta_stab = Fraction(24, 25)
delta = Fraction(1, 100)
pair_det = (1-delta) * (1-theta_stab-delta)
triple_stab = Fraction(3, 2)*theta_stab - 1 - delta
assert pair_det == Fraction(297, 10000)
assert triple_stab == Fraction(43, 100)
C_pair_stab = pi / sqrt(float(pair_det))
C_triple_stab = C3 / float(triple_stab)
C_stab = max(C_pair_stab, C_triple_stab)
assert C_stab < 26.697

print('PASS')
print('pair_margin_exact =', pair_margin)
print('triple_margin_exact =', triple_margin)
print('C_pair = %.15f' % C_pair)
print('C_triple = %.15f' % C_triple)
print('C_orient = %.15f' % C_orient)
print('pair_det_stability =', pair_det)
print('triple_margin_stability =', triple_stab)
print('C_pair_stability = %.15f' % C_pair_stab)
print('C_triple_stability = %.15f' % C_triple_stab)
print('C_stability = %.15f' % C_stab)
