from math import exp, sqrt

# Arithmetic regression for QFORM-TWO-STAR-JOINT-COLOR-OR-R1-v1.
# These checks are not proof evidence; the proof is in REPORT.md.

h = (2*sqrt(2)-1)/1572864
# Safe external-star norm after deleting one possible mutual-anchor edge of size <=h/8.
H = h*sqrt(63)/8
bank = H/(2*sqrt(2))
union_bound = 4*exp(-63/32)
cross_e2 = H**4/64
local_e2 = H**4/4096
zero_block_density = 16*sqrt(2)/H

assert union_bound < 1
assert bank > 0
assert cross_e2 > local_e2 > 0

print(f"h={h:.18g}")
print(f"H={H:.18g}")
print(f"bank={bank:.18g}")
print(f"four_event_union_bound={union_bound:.18g}")
print(f"cross_E2_threshold={cross_e2:.18g}")
print(f"local_E2_threshold={local_e2:.18g}")
print(f"exact_zero_anchor_density_cap={zero_block_density:.18g}")
print("STATUS=PASS")
