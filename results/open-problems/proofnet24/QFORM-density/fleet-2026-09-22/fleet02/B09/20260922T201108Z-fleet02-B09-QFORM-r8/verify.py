import math

C_pivot = 128 * 2 ** 0.25
C_pair = 8 * math.sqrt(5) * (32 / (math.sqrt(6) - 2)) ** 0.25
C_partner = 2 ** (4 / 3) * (3 + math.log(8))
C_bank = 256 * 2 ** 0.25

print(f"pivot_constant={C_pivot:.15f}")
print(f"low_diag_pair_constant={C_pair:.15f}")
print(f"partner_zero_self_constant={C_partner:.15f}")
print(f"bank_constant={C_bank:.15f}")
print("all_ones_spectrum=3,0,0")
print("centered_three_uniform_sum_density_at_zero=3/4")

assert C_pivot < 153
assert C_pair < 52
assert C_partner < 12.8
assert C_bank < 305
# For H=ones(3,3), H*(1,1,1)^T=3*(1,1,1)^T and H annihilates
# every vector orthogonal to (1,1,1), hence spectrum {3,0,0}.
# For T=sum of three Uniform[0,1], on 1<=x<=2,
# p_T(x)=0.5*(x*x-3*(x-1)**2), so p_T(1.5)=3/4.
assert abs(0.5 * (1.5**2 - 3 * 0.5**2) - 0.75) < 1e-15
