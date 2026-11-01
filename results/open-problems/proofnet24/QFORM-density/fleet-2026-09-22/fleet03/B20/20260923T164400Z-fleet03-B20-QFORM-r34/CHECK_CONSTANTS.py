import math

F = 0.05671470919622164
Delta = 0.0014419528160955833
zeta = 1.8425438602123219e-9
rho_star = 0.003845207509588222

K3 = 3 * 2**(4/3) * math.exp(1/3)
assert K3 < 10.551
assert 6*math.sqrt(math.e) < K3
assert 3*2**(7/6) < K3
assert 6 < K3

qform_e3 = K3 * zeta**(-1/6)
assert qform_e3 < 301.317

Etri = F + 2*Delta
partner_d5 = 5*math.sqrt(2*math.e)*120**0.1*64**0.4*Etri**(-0.5)
assert partner_d5 < 406.822

s3_exit = K3 * (Delta**2/4096)**(-1/6)
assert s3_exit < 373.539

Z2 = Delta**2
half_riesz = 8*math.sqrt(math.e)*Delta**(-0.25)
assert half_riesz < 67.687

cofactor = math.sqrt(127/512)*Delta
assert cofactor > 0.000718154571748
assert cofactor/2 > 0.000359077285874
assert 16*cofactor > 0.011490473147970

heavy_e2 = rho_star**2/320
assert heavy_e2 > 4.620506497435e-8

print('K3', K3)
print('e3_r37_bound', qform_e3)
print('Etri', Etri)
print('partner_D5', partner_d5)
print('s3_exit', s3_exit)
print('Z2', Z2)
print('half_riesz', half_riesz)
print('cofactor', cofactor)
print('double_star', cofactor/2)
print('residual_core', 16*cofactor)
print('heavy_e2_anchor', heavy_e2)
print('QFORM_B20_R34_CONSTANTS_PASS')
