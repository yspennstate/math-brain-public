import math
import numpy as np

# Main strict-target carrier: 2 S^2 + 2 L^2 - 2 V^2.
B_main = np.diag([2.0, 2.0, -2.0])
e_main = np.linalg.eigvalsh(B_main)
assert np.allclose(e_main, [-2.0, 2.0, 2.0])

# A perturbation with operator norm <=1/2 leaves two eigenvalues >=3/2
# and one <=-3/2 by Weyl. The analytic constant uses |a|*|det Lambda|=2*4=8.
C_projection = (144.0 * math.e**2) ** (1.0/3.0)
C_main = C_projection / (8.0 ** (1.0/3.0))
C_literal = (2.0 * (3.0 * math.e) ** (2.0/3.0)) / (8.0 ** (1.0/3.0))

# Designated account02/B16 application: 2 H^2 + 8 H L + 2 V^2.
B_partner = np.array([[2.0, 4.0, 0.0], [4.0, 0.0, 0.0], [0.0, 0.0, 2.0]])
e_partner = np.linalg.eigvalsh(B_partner)
expected_partner = np.array([1.0-math.sqrt(17.0), 2.0, 1.0+math.sqrt(17.0)])
assert np.allclose(e_partner, expected_partner)
assert np.min(np.abs(e_partner)) > 1.0
C_partner = 3.0 * 2.0 ** (-1.0/3.0)

# Algebraic constant check:
# 2 * (3 B M)^(2/3), with B=e, M=sqrt(2), equals
# (144 e^2)^(1/3).
lhs = 2.0 * (3.0 * math.e * math.sqrt(2.0)) ** (2.0/3.0)
assert abs(lhs - C_projection) < 1e-12

print('main_eigenvalues=', e_main.tolist())
print('projection_constant_unscaled=', repr(C_projection))
print('main_bound_projected_square=', repr(C_main))
print('main_bound_literal_square=', repr(C_literal))
print('partner_eigenvalues=', e_partner.tolist())
print('partner_bound=', repr(C_partner))
print('STATUS=PASS')
