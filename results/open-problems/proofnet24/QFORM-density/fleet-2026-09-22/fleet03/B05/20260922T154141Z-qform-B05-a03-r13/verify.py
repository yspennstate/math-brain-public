from fractions import Fraction
import math

# Exact star stress: one singleton transverse row and m parallel bank rows.
for m in (2, 3, 7, 31):
    weights = [Fraction(1, m) for _ in range(m)]
    d_center = sum(weights)
    d_leaf_sq_sum = sum(w*w for w in weights)
    sum_d_sq = d_center*d_center + d_leaf_sq_sum
    sum_w_sq = d_leaf_sq_sum
    R = Fraction(1,1) - sum_d_sq + sum_w_sq
    assert R == 0

# Exact equal triangle: three pair weights 1/3, every vertex marginal 2/3.
w = Fraction(1,3)
sum_d_sq = 3 * Fraction(4,9)
sum_w_sq = 3 * Fraction(1,9)
R = Fraction(1,1) - sum_d_sq + sum_w_sq
assert R == 0

# Reported endpoint constants.
triangle = 3 * 2**(2/3) * 6**(1/3)
assert 8.65 < triangle < 8.66
assert abs(3*2 - 6) < 1e-15
base = 3 * math.sqrt(math.e)
assert 4.94 < base < 4.95

# Fourier inversion algebra in the star-diffuse branch:
# int min(1,K t^{-3/2}) over R = 6 K^{2/3}; after /(2pi),
# K=(pi^(3/2)e^(3/4) D)^1 gives coefficient 3 sqrt(e) D^(2/3)/pi-power cancellation.
K0 = math.pi**1.5 * math.e**0.75
lhs = (6 * K0**(2/3)) / (2*math.pi)
rhs = 3 * math.sqrt(math.e)
assert abs(lhs-rhs) < 1e-12

print('QFORM_B05_R13_CHECK_PASS')
print(f'triangle_constant={triangle:.12f}')
print(f'star_density_prefactor={base:.12f}')
