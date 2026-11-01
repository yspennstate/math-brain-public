from fractions import Fraction
from decimal import Decimal, getcontext

getcontext().prec = 80

# Endpoint n=8, k=8 rational radical certificates.
assert Fraction(39, 7) ** 2 > 31          # sqrt(31) < 39/7
assert Fraction(9, 4) ** 2 > 5            # sqrt(5) < 9/4
endpoint_margin = (
    Fraction(30, 1) + Fraction(53, 30)
    - Fraction(78, 7) - Fraction(9, 2) - 16
)
assert endpoint_margin == Fraction(13, 105)
assert endpoint_margin > 0

# At n=8,k=8: z=30, Q=53.
assert 30**2 - 53 == 847 > 0

# General monotonicity certificate for
# M(x)=2x-2 +(6x+5)/(4x-2) -2 sqrt(4x-1)-2 sqrt(5), x>=8.
# M'(x)=2 - 32/(4x-2)^2 - 4/sqrt(4x-1).
# For x>=8, 32/(4x-2)^2 <= 8/225 and sqrt(4x-1)>11/2.
derivative_lb = Fraction(2, 1) - Fraction(8, 225) - Fraction(8, 11)
assert derivative_lb == Fraction(3062, 2475)
assert derivative_lb > 0

# z^2-Q_max=(4n-2)^2-(6n+5)=16n^2-22n-1,
# positive and increasing from n=8 onward.
assert 16 * 8**2 - 22 * 8 - 1 == 847
assert 32 * 8 - 22 > 0

# Endpoint quantitative gap.
gap = Fraction(1, 30) - Fraction(1, 31)
assert gap == Fraction(1, 930)

# High-precision sanity grid (not load-bearing for the proof):
# n=8..500 and every 0<=k<=n.
def dsqrt(x: int) -> Decimal:
    return Decimal(x).sqrt()

min_margin = None
min_pair = None
for n in range(8, 501):
    z = Decimal(4 * n - 2)
    for k in range(n + 1):
        Q = Decimal(4 * n + 5 + 2 * k)
        a = 2 * dsqrt(4 * n - 1) + 2 * dsqrt(5) + Decimal(2 * k)
        margin = z + Q / z - a
        assert z * z > Q
        assert margin > 0
        if min_margin is None or margin < min_margin:
            min_margin = margin
            min_pair = (n, k)

print("endpoint_margin =", endpoint_margin)
print("derivative_lb =", derivative_lb)
print("endpoint_gap =", gap)
print("grid_min_margin =", min_margin)
print("grid_min_pair =", min_pair)
print("ALL_EXACT_CHECKS_PASS")
