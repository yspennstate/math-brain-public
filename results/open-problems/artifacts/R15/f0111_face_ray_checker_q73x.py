from fractions import Fraction
import math


def log_bounds(x: Fraction, N: int = 3):
    # For x>1, z=(x-1)/(x+1) in (0,1) and
    # log x = 2 sum_{k>=0} z^(2k+1)/(2k+1).
    z = (x - 1) / (x + 1)
    assert 0 < z < 1
    s = Fraction(0)
    for k in range(N + 1):
        s += z ** (2*k + 1) / (2*k + 1)
    lo = 2*s
    # Bound every later denominator by the first omitted denominator.
    tail = 2 * z ** (2*N + 3) / ((2*N + 3) * (1 - z*z))
    hi = lo + tail
    return lo, hi


aL, aU = log_bounds(Fraction(2), 3)
xL, xU = log_bounds(Fraction(4, 3), 3)
cL, cU = log_bounds(Fraction(17, 3), 3)

# H0 = -(14/3)x -(56/9)(log 2)x +(91/9)x^2 + log(17/3).
# Use lower bounds in negative terms and upper bounds in positive terms.
H_upper = (
    -Fraction(14, 3)*xL
    -Fraction(56, 9)*aL*xL
    +Fraction(91, 9)*xU*xU
    +cU
)
assert H_upper < 0

# Repair-ray coarse lower bound, using alpha >= 7/20 and beta >= 19/100:
# after y=14x, positivity reduces to a quadratic with this discriminant.
c = Fraction(13, 20)
d = Fraction(247, 2800)
disc = (2*d-c)**2 - 4*d*2*(1-c)
assert disc == Fraction(-44551, 1960000)
assert disc < 0

# theta=4/5 small-small limiting pair gate:
# 2 alpha_* + beta_* = (73 - 40 log 2)/45 > 1 follows from log 2 < 7/10.
# Certify e^(7/10)>2 by a rational Taylor lower bound.
e07_lower = sum(Fraction(7,10)**k / math.factorial(k) for k in range(4))
assert e07_lower == Fraction(12013, 6000)
assert e07_lower > 2

# Large-m asymptotic no-go for theta=0 at x=4/m:
# log 5 -4/9 -(16/9)log2 <0 iff 5^9 < e^4 * 2^16.
# It suffices that e^4 >30 and 5^9 <30*2^16.
e4_lower = sum(Fraction(4)**k / math.factorial(k) for k in range(5))
assert e4_lower == Fraction(103, 3)
assert e4_lower > 30
assert 5**9 < 30 * 2**16

print("R15 F0111 face-ray exact checker")
print("log2 bounds:", aL, aU)
print("log(4/3) bounds:", xL, xU)
print("log(17/3) bounds:", cL, cU)
print("H0 rigorous upper bound:", H_upper)
print("H0 upper decimal:", float(H_upper))
print("repair-ray discriminant:", disc)
print("exp(0.7) rational lower bound:", e07_lower)
print("exp(4) rational lower bound:", e4_lower)
print("5^9, 30*2^16:", 5**9, 30*2**16)
print("ALL_EXACT_CHECKS_PASS")
