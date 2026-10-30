from fractions import Fraction

# Exact check for the rational split r0=4849/5000 in
# QFORM-GROUPED-2PLUS1-OPTIMIZED-FEJER-v1.
r0 = Fraction(4849, 5000)
assert 0 < r0 < 1

# N0^3 = 103680 * 2^2 * 12 = 4,976,640.
# Need N0*(1-r0)^(-1/6) < 306.
near_lhs = 4_976_640**2 * 5000
near_rhs = 306**6 * 151
assert near_lhs < near_rhs

# F0 = 96*sqrt(10), so F0^4=96^4*100.
# Need F0*r0^(-1/4) < 306.
far_lhs = 96**4 * 100 * 5000
far_rhs = 306**4 * 4849
assert far_lhs < far_rhs

print(f"r0={r0}={float(r0):.10f}")
print(f"near_lhs={near_lhs}")
print(f"near_rhs={near_rhs}")
print(f"near_margin={near_rhs-near_lhs}")
print(f"far_lhs={far_lhs}")
print(f"far_rhs={far_rhs}")
print(f"far_margin={far_rhs-far_lhs}")
print("QFORM_B01_R22_EXACT_SPLIT_CHECK_PASS")
