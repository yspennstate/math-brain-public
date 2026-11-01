from fractions import Fraction

# Exact arithmetic for the n=15 corollary of the shifted-Grunbaum bound
# derived in the accompanying I0122 report:
#
#   delta_xy >= L_n(d) := n^n (1-d) / (n+1-d)^n,
#
# for an incomparable pair whose expected-rank gap is d<1.
# Here we certify L_15(399/1000) > 1/3.

n = 15
d = Fraction(399, 1000)
L = Fraction(n**n, 1) * (1 - d) / (Fraction(n + 1, 1) - d) ** n

assert L > Fraction(1, 3)

# Equivalent integer comparison after clearing denominators:
# 3 * 15^15 * 601 * 1000^14 > 15601^15.
lhs = 3 * (15**15) * 601 * (1000**14)
rhs = 15601**15
assert lhs > rhs

print("n=", n)
print("d=", d)
print("L_n(d)=", L)
print("L_n(d)_decimal=", f"{float(L):.15f}")
print("one_third=", Fraction(1, 3))
print("integer_margin=", lhs - rhs)
print("CONCLUSION: any n=15 incomparable pair with expected-rank gap <= 399/1000 is 1/3-balanced under the proved shifted-Grunbaum corollary")
print("ALL_EXACT_CHECKS_PASS")
