#!/usr/bin/env python3
"""Exact rational self-check for HARD7-05 optimal spectral-majorization run.

This checks the finite algebra around the analytic proof. It does NOT replace:
(1) the Euler-product identities,
(2) the standard inequalities pi < 22/7 and alternating-series bounds for Catalan G,
(3) countable Karamata,
(4) the Feldheim--Feldheim--Mukherjee persistence comparison theorem.

All arithmetic below is exact Fraction arithmetic.
"""
from fractions import Fraction as F


def catalan_lower_even_terms(N):
    assert N % 2 == 0 and N >= 2
    return sum((F(1, (2*n+1)**2) if n % 2 == 0 else -F(1, (2*n+1)**2))
               for n in range(N))


# Analytic rational bounds used on page:
# pi < 22/7, hence pi^2 < 484/49.
pi2U = F(484, 49)

# Alternating Catalan series G = 1 - 1/3^2 + 1/5^2 - ...
# Every even-length partial sum is a strict lower bound.
G4L = catalan_lower_even_terms(4)
G8L = catalan_lower_even_terms(8)

assert G4L == F(10016, 11025)
assert G8L == F(1854623872, 2029052025)

# D = pi^2/2 - 8G + 416/25, q_* = 40/(9D).
# Prove q_* > q0=(279/500)^2 using D < D_U from pi^2<pi2U and G>G8L.
DU8 = pi2U/2 - 8*G8L + F(416,25)
q0 = F(279,500)**2
D_threshold_q0 = F(40,9) / q0
movement_margin = D_threshold_q0 - DU8
assert movement_margin > 0

# Also q_*>9/31 (>1/4), enough to fix the descending order of x.
# The coarser G>8/9 and pi^2<10 gives D<3269/225<1240/81.
DU_coarse = F(5,1) - 8*F(8,9) + F(416,25)
assert DU_coarse == F(3269,225)
assert DU_coarse < F(1240,81)

# D > 9/2 - 8 + 416/25 = 657/50 > 40/9, using pi>3 and G<1,
# so q_*<1.
DL_coarse = F(9,2) - 8 + F(416,25)
assert DL_coarse == F(657,50)
assert DL_coarse > F(40,9)

# First three partial-sum majorization gap at q_*:
# S3 = 8G - pi^2/2 - 20/9.
# G>G4L and pi^2<484/49 give a positive exact margin.
S3_lower = 8*G4L - pi2U/2 - F(20,9)
assert S3_lower == F(1178,11025)
assert S3_lower > 0

# Tail termwise inequality: for k>=4,
# y_k=16/(4k-9)^2 < x_k=16/(4k-10)^2.
for k in range(4, 10000):
    xk = F(16, (4*k-10)**2)
    yk = F(16, (4*k-9)**2)
    assert yk < xk

# Constant bookkeeping for S3 after substituting 40/(9q_*)=D.
Y3_const = F(16,1) + F(16,9) + F(16,25) - F(4,1)
assert Y3_const - F(416,25) == -F(20,9)

# Previous certified scale is strictly below c_*.
assert D_threshold_q0 > DU8

print("G4_LOWER =", G4L)
print("G8_LOWER =", G8L)
print("D_UPPER_FROM_PI22_7_G8 =", DU8)
print("D_THRESHOLD_FOR_C0_279_500 =", D_threshold_q0)
print("MOVEMENT_MARGIN =", movement_margin)
print("COARSE_D_UPPER =", DU_coarse, "< 1240/81 =", F(1240,81))
print("COARSE_D_LOWER =", DL_coarse, "> 40/9 =", F(40,9))
print("S3_MAJORISATION_LOWER_MARGIN =", S3_lower)
print("TAIL_PAIR_CHECK_K4_TO_9999 = PASS")
print("OLD_C0_SQUARED =", q0)
print("ALL_EXACT_CHECKS_PASS = True")
