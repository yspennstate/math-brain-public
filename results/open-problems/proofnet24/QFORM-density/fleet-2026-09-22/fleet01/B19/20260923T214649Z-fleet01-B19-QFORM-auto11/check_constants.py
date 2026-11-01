from math import sqrt, pi, gamma

# Constants in QFORM-TWOHUB-COMMONPLANE-UNIFORM-MISMATCH-v1.
C_balanced = 16 * 2**(5/8)  # rank-two half-Riesz branch, |theta2| >= |theta1|/8
C_quarter = 3 * sqrt(2) * 400**(1/3)  # quarter-small-ball branch
C_rank1_gaussian = (2**0.75) * (2.718281828459045**0.5) * gamma(0.25)
C_rank1_pair = 4*sqrt(2*C_rank1_gaussian)

print('C_balanced =', C_balanced)
print('C_quarter =', C_quarter)
print('rank1 Gaussian small-ball H coefficient =', C_rank1_gaussian)
print('rank1 pair-log coefficient =', C_rank1_pair)

# Example universal payment thresholds used only as a bookkeeping corollary.
# If D_B >= 2^-12 and kappa >= 2^-6 (hence a strong physical pair)
# and mu >= 2^-20, evaluate both branches.
D = 2**-12
kappa = 2**-6
mu = 2**-20
balanced = C_balanced * (D*kappa*mu)**(-0.25)
quarter = C_quarter * (D*D*kappa*mu)**(-1/6)
print('strong-pair, mu>=2^-20 balanced bound =', balanced)
print('strong-pair, mu>=2^-20 quarter bound =', quarter)

# The already-established full-matrix physical-pair theorem is sharper here.
full_pair = 3 * 400**(1/3) * (D*D*kappa)**(-1/6)
print('full-matrix physical-pair bound at kappa=1/64 =', full_pair)
