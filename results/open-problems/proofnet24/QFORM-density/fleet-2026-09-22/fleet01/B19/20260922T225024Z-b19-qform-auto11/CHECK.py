import math

# Regression check for Theorem 2.1 optimization.
# For H=|s|=|f|=1 the split bound is 8 sqrt(r)+1/(2r).
# The exact optimizer is r=(1/8)^(2/3), with minimum 6.

r = (1.0 / 8.0) ** (2.0 / 3.0)
F = 8.0 * math.sqrt(r) + 0.5 / r
assert abs(F - 6.0) < 1e-12, (r, F)

# Null-coloop application H=e and |det M|>=1.
C = 6.0 * math.e ** (2.0 / 3.0)
assert 11.686 < C < 11.687, C

# General coefficient identity: minimize
# 8H sqrt(r)/sqrt(|fs|) + 1/(2|s|r)
# and compare with 6 H^(2/3) |s^2 f|^(-1/3).
for H in (1.0, math.e, 7.25):
    for s in (0.2, 1.0, 5.0):
        for f in (0.3, 1.0, 11.0):
            rstar = (math.sqrt(f / s) / (8.0 * H)) ** (2.0 / 3.0)
            lhs = 8.0 * H * math.sqrt(rstar) / math.sqrt(f * s) + 1.0 / (2.0 * s * rstar)
            rhs = 6.0 * H ** (2.0 / 3.0) * (s * s * f) ** (-1.0 / 3.0)
            assert abs(lhs - rhs) <= 1e-11 * max(1.0, rhs), (H, s, f, lhs, rhs)

print(f"r_unit={r:.15f}")
print(f"null_coloop_constant={C:.15f}")
print("QFORM_B19_NULL_COLOOP_DIRECT_CHECK_PASS")
