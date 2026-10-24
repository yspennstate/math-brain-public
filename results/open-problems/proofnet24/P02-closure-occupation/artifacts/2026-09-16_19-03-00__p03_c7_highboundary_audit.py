#!/usr/bin/env python3
# Exact-arithmetic independent audit of P03-C7-HIGH-BOUNDARY-198.
# No floating point is used.
import sys
sys.set_int_max_str_digits(100000)

# The analytic derivation reduces the strict comparison to
# 110336 - 39690 log_2(3) + 1120 log_2(5)
#        - 26117 log_2(7) + 5152 log_2(23) > 0.
# Exponentiating base 2 gives the exactly equivalent integer inequality:
# 2^110336 * 5^1120 * 23^5152 > 3^39690 * 7^26117.
lhs = (2 ** 110336) * (5 ** 1120) * (23 ** 5152)
rhs = (3 ** 39690) * (7 ** 26117)
diff = lhs - rhs

assert lhs > rhs
assert diff > 0

s_lhs = str(lhs)
s_rhs = str(rhs)
s_diff = str(diff)

print("P02_AUDIT_P03_C7_HIGHBOUNDARY_27=PASS")
print("exact_integer_inequality=True")
print("lhs_digits=", len(s_lhs))
print("rhs_digits=", len(s_rhs))
print("difference_digits=", len(s_diff))
print("difference_prefix=", s_diff[:100])
print("difference_suffix=", s_diff[-100:])
print("ALL_EXACT_CHECKS_PASS")
