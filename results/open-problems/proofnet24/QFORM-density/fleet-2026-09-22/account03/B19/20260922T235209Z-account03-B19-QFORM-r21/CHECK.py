from fractions import Fraction
import math

# Exact constants for account03/B19 QFORM r21.
tau = Fraction(1, 2**20)
w0 = Fraction(3, 4) * (1 - tau)**2
assert w0 > Fraction(2, 3)

# No-pivot off-diagonal bound tau+tau^2 < 10^-6.
assert tau + tau*tau < Fraction(1, 10**6)

# R1: E2 <= 2^-20 and W>w0.
delta2 = Fraction(1, 2**20)
tail1 = 2*delta2/w0
assert tail1 < Fraction(1, 590**2)
assert float(w0-tail1) > (4/5)**2
entry_cap = math.sqrt(float(tau + tau*tau))
product_bound = (entry_cap + 1/590)/(4/5)
assert product_bound < 1/296

# R2: E2>2^-20, E3<2^-36.
delta3 = Fraction(1, 2**36)
tail2 = 3*delta3/delta2
assert tail2 < Fraction(1, 147**2)

# P0 D' constant.
C_diffuse = 576*math.sqrt(3*math.e)
assert C_diffuse < 1645

# R3 anchored packet and Hadamard cardinality.
anchor_mass = delta3/12
minor_sq_upper = Fraction(27, 10**18)
ratio = anchor_mass/minor_sq_upper
assert ratio > 44913
assert ratio < 44914

print("QFORM_B19_R21_CHECK_PASS")
print(f"w0={float(w0):.15f}")
print(f"r1_tail_sq_upper={float(tail1):.15e}")
print(f"r1_dist_upper={math.sqrt(float(tail1)):.15e}")
print(f"entry_cap={entry_cap:.15e}")
print(f"rank1_uv_product_bound={product_bound:.15e}")
print(f"r2_tail_sq_upper={float(tail2):.15e}")
print(f"r2_dist_upper={math.sqrt(float(tail2)):.15e}")
print(f"diffuse_density_constant={C_diffuse:.15f}")
print(f"anchor_mass={float(anchor_mass):.15e}")
print(f"anchor_minor_count_ratio={float(ratio):.15f}")
print("anchor_min_distinct_minors=44914")
