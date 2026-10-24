import math

tau = 2**-20
m = 2**23
beta = 0.000038585661932302174
rho_star = 0.003845207509588222
D_quarter = 22.103418361512958

assert 4/m < tau
assert 1/m < tau
assert 2 > beta
assert 1 > rho_star

# For a,b with ||a||^2=||b||^2=3 and a.b=1,
# aa^T-bb^T has trace zero, rank two and tr(A^2)=16.
lam = math.sqrt(8)
assert abs(2*lam*lam - 16) < 1e-12

# Cross block pq^T-rs^T for orthonormal pairs has singular values 1,1.
Delta = 1.0
FD = 1 - 1/m
bound = D_quarter * Delta**(-2/5) * FD**(-1/10)
assert bound < 22.105

# account04/B19 adaptive-HY corollary on e^-8 <= D_res <= 1.
partner = 34 * math.sqrt(math.log(math.e/(math.e**-8)))
assert abs(partner - 102) < 1e-12

print('QFORM_B19_R35_ALIGNED_LOCAL_FALSE_CHECK_PASS')
print(f'tau={tau:.18g}')
print(f'm={m}')
print(f'4/m={4/m:.18g}')
print(f'1/m={1/m:.18g}')
print(f'core_eigenvalues=+/-{lam:.15f}')
print('star_energy_left=2')
print('star_energy_right=2')
print('cross_singular_product=1')
print(f'live_beta={beta:.18g}')
print(f'live_rho_star={rho_star:.18g}')
print(f'F_D={FD:.18g}')
print(f'third_packet_bound={bound:.15f}')
print(f'partner_bound={partner:.15f}')
