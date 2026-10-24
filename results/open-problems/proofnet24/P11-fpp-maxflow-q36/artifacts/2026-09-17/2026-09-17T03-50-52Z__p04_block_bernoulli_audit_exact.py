from math import comb

# Exact finite arithmetic self-check for P11's claim-scoped audit of
# P04-I0101-REGULAR-S3-BLOCK-BERNOULLI-13.

s = sum(comb(8, r) * (r - 1) for r in range(2, 9))
assert s == 769

# The main term conversion in P04 eq. (6.2): after summing over the
# C(6,k) patterns and dividing the vertex count by six, p/1536 differs
# from q/64, q=(p-5)/24, by exactly 5/1536 per pattern.
for k in range(7):
    c = comb(6, k)
    # Compare numerators over common denominator 1536.
    # c*p/1536 - c*(p-5)/1536 = 5c/1536.
    for p in (29, 53, 101, 149):
        assert p % 24 == 5
        q = (p - 5) // 24
        assert c * p - 24 * c * q == 5 * c

print('P11-AUDIT-P04-I0101-BLOCK-BERNOULLI-12 finite arithmetic check: PASS')
print('binomial_error_sum=', s)
print('k_values_checked=7')
print('sample_primes_checked=4')
print('floating_point_used=false')
print('scope=finite arithmetic only; Weil/orbit proof audited in run report')
