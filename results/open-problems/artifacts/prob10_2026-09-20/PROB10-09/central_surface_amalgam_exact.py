#!/usr/bin/env python3
from fractions import Fraction
import math

# Exact algebraic self-check for the PROB10-09 central-surface-amalgam theorem.
# The finite assertions below certify the radical/rational inequalities used in
# the written proof. The small floating-point sweep at the end is diagnostic
# only and is not used as theorem evidence.

sqrt2_upper = Fraction(99,70)
assert sqrt2_upper*sqrt2_upper > 2

# Smallest new family member: r=2, g1=g2=2.
z = Fraction(250,21)  # reciprocal of the rational floor p_u > 21/250
Q = 17
R_upper = 2 + 8*sqrt2_upper
lhs = z + Fraction(Q,1)/z
margin = lhs - R_upper
assert z*z > Q
assert margin == Fraction(97,5250)
assert margin > 0

pu_floor = Fraction(21,250)
pc_ceiling = Fraction(1,12)
gap = pu_floor - pc_ceiling
assert gap == Fraction(1,1500)

# Full-Z-fibre Galton-Watson strictness at p0=1/(b+1).
# The exact supercriticality numerator is b^3-b^2-b-1.
def fibre_poly(b):
    return b**3 - b**2 - b - 1

# In the central-amalgam family r>=2, g_i>=2 gives k>=6 and b=2k-1>=11.
assert fibre_poly(11) == 1198
for b in range(11,1000,2):
    assert fibre_poly(b) > 0

# Uniform spectral-root proof:
# 9-6*sqrt(2)>1/2 is equivalent (after positive squaring) to 289>288.
assert 289 > 288

# For G>=4, (1/2)G^2-2G+1 is increasing and already equals 1 at G=4.
for G in range(4,1000):
    coarse = Fraction(G*G,2)-2*G+1
    assert coarse >= 1

# Diagnostics only: stress the exact theorem against representative tuples.
worst = None
for r in range(2,11):
    tests = [[2]*r, [3]*r, [2]*(r-1)+[10]]
    for gs in tests:
        G = sum(gs)
        S = sum(math.sqrt(g) for g in gs)
        k = sum(2*g-1 for g in gs)
        D = 4*G+2
        Qf = D-1
        R = 4*S+2
        if R <= 2*math.sqrt(Qf):
            beta = math.sqrt(Qf)
        else:
            beta = (R+math.sqrt(R*R-4*Qf))/2
        diff = 2*k-beta
        if worst is None or diff < worst[0]:
            worst = (diff,r,tuple(gs),beta,2*k)

print('PROB10-09 CENTRAL SURFACE AMALGAM EXACT CHECK')
print('sqrt2_upper=99/70 square_minus_2 =', sqrt2_upper*sqrt2_upper-2)
print('minimal_z=250/21')
print('minimal_z^2_minus_17 =', z*z-Q)
print('minimal_root_test_margin =', margin)
print('p_u_floor=21/250 =', float(pu_floor))
print('p_c_ceiling=1/12 =', float(pc_ceiling))
print('certified_gap=1/1500 =', float(gap))
print('minimal_fibre_poly_b11 =', fibre_poly(11))
print('general_radical_margin_certificate: 289-288 =', 289-288)
print('G4_coarse_polynomial_floor =', Fraction(4*4,2)-8+1)
print('diagnostic_worst_2k_minus_beta =', worst)
print('ALL_EXACT_CHECKS_PASS')
