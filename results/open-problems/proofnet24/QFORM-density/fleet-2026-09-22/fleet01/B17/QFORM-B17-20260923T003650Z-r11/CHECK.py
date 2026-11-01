from fractions import Fraction
import math

# Exact heavy-row certificate inherited by the rigidity theorem.
heavy = Fraction(6*52933, 76545)
assert heavy == Fraction(105866, 25515)
endpoint = 3*math.sqrt(2)
assert float(heavy) < endpoint

# Gaussian endpoint used in the iff sharp-sequence statement.
# If G~N(0,1/12), E exp(-6G^2)=1/sqrt(2), hence C=6/sqrt(2)=3sqrt(2).
gaussian_branch = 6/math.sqrt(2)
assert abs(gaussian_branch-endpoint) < 1e-14

print('PASS QFORM-COLLINEAR-NEAR-EXTREMIZER-RIGIDITY-v1 constants')
print('heavy_exact =', heavy)
print('heavy_decimal =', float(heavy))
print('3sqrt2 =', endpoint)
print('heavy_gap =', endpoint-float(heavy))
print('gaussian_branch =', gaussian_branch)
