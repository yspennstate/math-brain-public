import math

tau = 3/10
prod_lower = 7*tau*tau/256
corrected_holder_const = math.sqrt(2*math.e) * math.pi**0.25 * prod_lower**(-0.25)
assert abs(prod_lower - 63/25600) < 1e-15
assert corrected_holder_const < 13.938

# Exact product-minimum check for the two-channel cut branch.
f_lo = (1/16)*(1/2-1/16)
f_hi = (1/4)*(1/2-1/4)
assert abs(f_lo - 7/256) < 1e-15
assert f_hi == 1/16
assert min(f_lo, f_hi, 1/16) == 7/256

print(f"two_channel_product_lower={prod_lower:.12f}")
print(f"corrected_half_holder_constant={corrected_holder_const:.12f}")
print("product_minimum_fraction=7/256")
print("QFORM_CROSSCUT_HALF_HOLDER_CORRECTION_PASS")
