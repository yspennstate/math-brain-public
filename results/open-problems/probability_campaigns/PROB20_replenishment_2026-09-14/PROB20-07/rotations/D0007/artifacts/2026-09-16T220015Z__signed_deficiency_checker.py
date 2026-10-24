# Exact finite-core checker for D0007 signed-deficiency obstruction.
# Uses only Python arbitrary-precision integer arithmetic.

E = 20001
n_bad = 28855
n_next_odd = 28857

def cmp_integer_boundary(n: int) -> int:
    """Sign of (n+1)^(E+1) - 2*n^(E+1)."""
    d = pow(n + 1, E + 1) - 2 * pow(n, E + 1)
    return (d > 0) - (d < 0)

assert E == 20001
assert E - 1 == 20000
assert n_bad % 2 == 1 and n_next_odd == n_bad + 2

bad_cmp = cmp_integer_boundary(n_bad)
next_cmp = cmp_integer_boundary(n_next_odd)

# The analytic theorem proves non-CM for odd n whenever
# (n+1)^(E+1) > 2*n^(E+1).
assert bad_cmp == 1

# The same necessary-condition witness no longer obstructs at the next odd n.
assert next_cmp == -1

# Since (1+1/n)^(E+1) is strictly decreasing in n>0, these two checks
# certify that 28855 is the largest odd n detected by this exact witness.
assert cmp_integer_boundary(20001) == 1

db = pow(n_bad + 1, E + 1) - 2 * pow(n_bad, E + 1)
dn = pow(n_next_odd + 1, E + 1) - 2 * pow(n_next_odd, E + 1)

print("ALL EXACT D0007 SIGNED-DEFICIENCY CHECKS PASSED")
print(f"E = {E}; frozen density = (E/2)|x|^(E-1) on [-1,1]")
print(f"n_bad = {n_bad}; integer-boundary sign = {bad_cmp} (>0)")
print(f"n_next_odd = {n_next_odd}; integer-boundary sign = {next_cmp} (<0)")
print(f"|difference at n_bad| bit_length = {abs(db).bit_length()}")
print(f"|difference at n_next_odd| bit_length = {abs(dn).bit_length()}")
print("largest odd dimension certified non-CM by this witness = 28855")
