from fractions import Fraction as F

# R13 exact arithmetic delta-import constant tightening.
# Imported theorem/certificate from the immediately preceding immutable R13 run:
#   runs/R13/20260919T1001Z_p165-tilted-4f2d.md
#   artifacts/R13/20260919T1001Z_p165-tilted-4f2d_checker.py
#   artifacts/R13/20260919T1001Z_p165-tilted-4f2d.out
# That run rigorously certifies, for p=33/20 and D=139,
#   delta := 1-E sqrt(X_139) > 0.05374576758247757...
# We deliberately import only the weaker rational consequence below.
delta_floor = F(53745767, 10**9)

# For p=33/20 the square of the deterministic prefactor is
#   9801*pi/520.
# Reuse the classical rational upper bound pi < 355/113 already used in R13,
# but replace the coarse prefactor upper bound 7.695 by a sharper rational one.
pi_up = F(355, 113)
base_sq_up = F(9801, 520) * pi_up
base_up = F(7694998, 10**6)  # 7.694998
assert base_up * base_up > base_sq_up

# Since actual delta > delta_floor and actual base < base_up,
# C_{33/20,139} < base_up*(1-delta_floor).
C_upper = base_up * (1 - delta_floor)
old_h = F(45509, 6250)       # 7.28144
h = F(728143, 100000)        # 7.28143
assert C_upper < h
assert old_h - h == F(1, 100000)

# Active-row pruning at n=86: 139 < 86^2/h^2 < 140, so there are at most
# 139 active rows; the D=139 Boolean theorem handles those rows.
row_ratio = F(86**2, 1) / (h*h)
assert F(139) < row_ratio < F(140)

print('R13_CONSTANT_TIGHTENING_EXACT_PASS')
print('delta_floor =', float(delta_floor))
print('base_up =', float(base_up))
print('C_upper =', float(C_upper))
print('h =', float(h))
print('row_ratio =', float(row_ratio))
print('improvement =', float(old_h-h))
