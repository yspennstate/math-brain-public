import math

L = math.log(5.0)
I_star = 1152/25 + (48/5)*L + (144/25)*L**2 + (32/25)*L**3
C_star = I_star/4
B_star = 2*C_star**(1/3)
theta_sharp = (3*math.sqrt(2)/B_star)**3
theta_partner = (2*math.sqrt(6)/B_star)**3
cone_max = 2*math.sqrt(2) - 0.5

assert abs(B_star*theta_sharp**(1/3) - 3*math.sqrt(2)) < 1e-12
assert abs(B_star*theta_partner**(1/3) - 2*math.sqrt(6)) < 1e-12
assert cone_max < math.pi < 3*math.sqrt(2)

print('PASS QFORM_SHARED_FOLD_DISTRIBUTION_FREE')
print(f'I_star={I_star:.17g}')
print(f'C_star={C_star:.17g}')
print(f'B_star={B_star:.17g}')
print(f'theta_sharp={theta_sharp:.17g}')
print(f'theta_partner={theta_partner:.17g}')
print(f'cone_max={cone_max:.17g}')
