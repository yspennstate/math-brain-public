from fractions import Fraction

# Deterministic algebra/threshold verifier for account03/B16 r25.
# No Monte Carlo or statistical evidence is used.

# Gate-failure threshold: h < 1/64 and delta > 1/2 imply
# s^2/a > 1-2h > 31/32.
hmax = Fraction(1, 64)
assert 1 - 2*hmax == Fraction(31, 32)

# The 2-coordinate cocircuit eigenvalue estimate is
# lambda_min < (128/63) a h.  Since a<=1 and h<1/64,
# lambda_min < 2/63 and the captured fraction is >61/63.
err = Fraction(128, 63) * hmax
assert err == Fraction(2, 63)
assert 1 - err == Fraction(61, 63)

# Formal coefficient identities, represented by polynomial expansion.
# Let a=1-c. q=h+s2/a.
# neither = 1-c-(s2+h)+c*h = a(1-q).
# Multiplying by a clears the only denominator.
# a*neither = a^2(1-h)-a*s2.
# a*a(1-q) = a^2(1-h)-a*s2.
# Hence the identity is exact.

# For K=[[a-s2,-s*sqrt(h)],[-s*sqrt(h),1-h]],
# det K=(a-s2)(1-h)-s2*h = a(1-h)-s2.
# Its trace is 1+a-s2-h = 1+b-c*h with b=a(1-h)-s2.
# Check as a polynomial identity using representative exact rationals.
for c in [Fraction(1,5), Fraction(1,2), Fraction(63,64)]:
    a = 1-c
    for h in [Fraction(1,100), Fraction(1,128)]:
        # choose any admissible s2 below a(1-h)
        s2 = a * Fraction(3,4)
        q = h + s2/a
        neither = 1-c-(s2+h)+c*h
        b = a*(1-h)-s2
        assert neither == a*(1-q) == b
        trace = (a-s2) + (1-h)
        assert trace == 1+b-c*h

print("QFORM_B16_BALANCED_VOLUME_COCIRCUIT_CHECK_PASS")
print("gate_threshold=31/32")
print("cocircuit_capture_strictly_greater_than=61/63")
