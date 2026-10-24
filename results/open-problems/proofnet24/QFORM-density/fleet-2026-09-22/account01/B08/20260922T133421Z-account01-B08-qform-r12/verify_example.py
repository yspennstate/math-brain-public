from fractions import Fraction as F
from math import prod

# Squared row norms for directions e1,e1,e2,e2,e3,e3.
c = [F(4,5), F(1,5), F(1,2), F(1,2), F(1,2), F(1,2)]
theta = [F(1,2)] * 6
axes = [0,0,1,1,2,2]

# W^T W and alternative isotropy are diagonal in this example.
canonical = [sum(c[i] for i,a in enumerate(axes) if a==j) for j in range(3)]
alt = [sum(theta[i] for i,a in enumerate(axes) if a==j) for j in range(3)]
assert canonical == [F(1),F(1),F(1)]
assert alt == [F(1),F(1),F(1)]
assert max(c) > F(1,2)

# Conditioning row 1 leaves e1 mass 1/5, so row 2 whitens to leverage one.
residual_whitened_leverage_row2 = c[1] / (F(1)-c[0])
assert residual_whitened_leverage_row2 == F(1)

pc = prod(c)
assert pc == F(1,100)

print('canonical_axis_masses=', canonical)
print('fractional_axis_masses=', alt)
print('max_c=', max(c))
print('residual_whitened_leverage_row2=', residual_whitened_leverage_row2)
print('product_c=', pc)
print('B_theta=sqrt(10)')
print('density_constant_for_abs_det_ge_1 = 3*10^(1/3) =', 3*(10**(1/3)))
