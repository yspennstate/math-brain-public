from fractions import Fraction as Q

# Exact-arithmetic certificate for the P0279 post-Recovery-1 tree run.
# Tree: T_{2,1}, a root with two leaves.  Work in edge variables
# eta_1=sigma_r sigma_1, eta_2=sigma_r sigma_2, start from all-plus.
# Set theta=tanh(beta)=1/4, so 2 theta=1/2<1 (strict tree uniqueness).
# The two edge variables are independent under equilibrium, but this checker
# certifies that their covariance becomes positive to first order under the
# actual heat-bath dynamics, hence product structure is not dynamically
# preserved.

theta = Q(1, 4)
assert 2 * theta < 1

tanh_2beta = 2 * theta / (1 + theta * theta)
# At all-plus, a leaf sees one agreeing neighbor; the root sees two.
c_leaf = (1 - theta) / 2
c_root = (1 - tanh_2beta) / 2

# eta_1 and eta_2 each flip if its leaf updates or the root flips.
d_eta1 = -2 * (c_leaf + c_root)
d_eta2 = -2 * (c_leaf + c_root)
# eta_1 eta_2 is unchanged by a root flip and toggled by either leaf flip.
d_product = -4 * c_leaf
# Since eta_1=eta_2=1 at t=0,
# d/dt Cov(eta_1,eta_2)|_0 = d_product - d_eta1 - d_eta2.
cov_derivative = d_product - d_eta1 - d_eta2

assert tanh_2beta == Q(8, 17)
assert c_leaf == Q(3, 8)
assert c_root == Q(9, 34)
assert cov_derivative == Q(18, 17)
assert cov_derivative > 0

print('EXACT_CHECK_PASS')
print(f'theta={theta}')
print(f'2theta={2*theta}')
print(f'tanh(2beta)={tanh_2beta}')
print(f'c_leaf={c_leaf}')
print(f'c_root={c_root}')
print(f'd_covariance_at_0={cov_derivative}')
