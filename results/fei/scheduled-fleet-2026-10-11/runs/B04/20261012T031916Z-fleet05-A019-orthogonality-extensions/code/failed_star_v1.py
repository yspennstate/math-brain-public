"""Reconstructed minimal certificate of failed v1 formula; not a byte archive."""
from fractions import Fraction as Q
# A two-bit point sign has four squared Fourier coefficients1/4.
# Each residual pair contributes (1/2)h2(1/2)=1/2 to erasure.
actual_B=Q(1)
# alpha0,beta1: the omitted formula keeps only the empty residual pair.
omitted_formula_B=Q(1,2)
nonempty_mass=Q(1,2)
assert actual_B==omitted_formula_B+nonempty_mass
assert actual_B!=omitted_formula_B
print('Exact failure witness: actual B=1; omitted-term prediction=1/2.')
