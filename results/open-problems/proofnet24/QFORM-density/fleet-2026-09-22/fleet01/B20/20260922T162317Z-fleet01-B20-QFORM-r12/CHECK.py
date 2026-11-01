import math

Cstar = 32768*math.sqrt(2)
tau = 1/4
sigma = tau/128
minimality_barrier = 16/(tau*sigma)
row_norm_factor = 1/math.sqrt(32)-1/64
coordinate_factor = row_norm_factor/math.sqrt(2)
c = 2/(math.pi**2*math.e**2)
beta_18 = math.gamma(1/8)**2/math.gamma(1/4)
C_FR = (2*math.pi)**(-0.5)*0.5*beta_18*c**(-0.25)
paid_bound = 4*C_FR*(1536**(1/8))
same_sign_bound = 12*math.pi

print(f"Cstar={Cstar:.12f}")
print(f"minimality_barrier={minimality_barrier:.12f}")
print(f"minimality_closes={minimality_barrier < Cstar}")
print(f"row_norm_factor={row_norm_factor:.12f}")
print(f"coordinate_factor={coordinate_factor:.12f}")
print(f"coordinate_factor_gt_1_over_9={coordinate_factor > 1/9}")
print(f"C_FR={C_FR:.12f}")
print(f"disjoint_q1_paid_bound={paid_bound:.12f}")
print(f"disjoint_q1_closes={paid_bound < Cstar}")
print(f"same_sign_pair_bound={same_sign_bound:.12f}")
print(f"same_sign_closes={same_sign_bound < Cstar}")
