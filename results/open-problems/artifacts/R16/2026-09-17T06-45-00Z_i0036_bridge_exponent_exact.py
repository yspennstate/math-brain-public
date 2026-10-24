from fractions import Fraction

# Exact arithmetic certificate for the constants in the R16/I0036
# re-optimization of the Krachun--Panagiotis bridge-decay recurrence.
# No floating-point comparison is used for any asserted inequality.

M = 36_000_000
A = 1000
eps = Fraction(9, 10_000_000_000)   # 9e-10

# Exponent bookkeeping.
assert M * eps == Fraction(81, 2500)
assert 10 * M * eps == Fraction(81, 250)

# Elementary algebraic upper bounds used in the proof.
# sqrt(2) < 71/50, so c_G=(1+sqrt(2))/2 < 121/100.
assert 2 * 50**2 < 71**2

# 279/200 < sqrt(2).  Since C0^2=4-2sqrt(2), this implies
# C0^2 < 121/100 and hence C0=sec(pi/8) < 11/10.
assert 279**2 < 2 * 200**2

# The recurrence coefficient is bounded by the following rational number:
#   2^17/M * (121/100) * ((A+11/10)/A)^4
#   * 3^4 * (1-eps)^(-4).
R_upper = (
    Fraction(2**17, M)
    * Fraction(121, 100)
    * Fraction(10011, 10000) ** 4
    * 81
    * Fraction(10_000_000_000, 9_999_999_991) ** 4
)
assert R_upper < Fraction(9, 25)

# 9/25 < 22^(-81/250), proved after raising to the 250th power.
assert 22**81 * 9**250 < 25**250

# Endpoint buffer q=22^(-M eps)=22^(-81/2500) is > 1/2,
# so A q > 500 > C0; this certifies the base endpoint.
assert 22**81 < 2**2500

print(f"epsilon = {eps}")
print(f"M = {M}; A = {A}")
print(f"M*epsilon = {M*eps}; 10*M*epsilon = {10*M*eps}")
print(f"R_upper numerator digits = {len(str(R_upper.numerator))}")
print(f"R_upper denominator digits = {len(str(R_upper.denominator))}")
print("R_upper < 9/25 = PASS")
print("9/25 < 22^(-81/250) = PASS")
print("q = 22^(-81/2500) > 1/2 = PASS")
print("ALGEBRAIC_BOUNDS_PASS")
print("ALL_EXACT_CHECKS_PASS")
