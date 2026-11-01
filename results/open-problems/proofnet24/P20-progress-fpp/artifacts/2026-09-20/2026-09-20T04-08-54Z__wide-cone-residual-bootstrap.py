from fractions import Fraction

# Exact arithmetic sanity checker for the P20/P04 wide-cone residual bootstrap.
# This is not a sampled-curvature computation.  It only verifies the rational
# constants and one explicit finite-n corollary of the proved inequalities.

A0 = Fraction(
    127596793342690034600361684870097,
    197703921604834678505472000000000,
)
C0 = Fraction(27865448, 206955)
BETA = Fraction(
    713425217726611388616507115106921327,
    740604339057582092285156250000000000,
)

G0 = Fraction(2, 3) - A0
DELTA0 = 2 * G0
ETA0 = G0 / A0

# Explicit asymmetric directions from the theorem:
# u=(16,33), v=(15,-32).  Both lie in the opposing P04 wide cones,
# while their transverse coordinates differ by one.
a, b, c, d = 16, 33, 15, 32
X = a + c
H = abs(b - d)
KAPPA = Fraction(2, 3) * X - A0 * (X + H)

# For n divisible by six, the P04 axis concatenation has zero expectation
# interface error.  At n=24 the explicit lower-tail error is already smaller
# than KAPPA.
n = 24
EPS = Fraction(2, 3) * C0 * (
    a * BETA ** (a * n) + c * BETA ** (c * n)
)
FINITE_PER_N = KAPPA - EPS
FINITE_LB = n * FINITE_PER_N

assert G0 > 0
assert DELTA0 > Fraction(1, 24)
assert BETA < 1
assert b >= 2 * a and d >= 2 * c
assert H * A0 < G0 * X
assert KAPPA > 0
assert EPS < KAPPA
assert FINITE_LB > 0

print("P20-WIDE-CONE-RESIDUAL-BOOTSTRAP EXACT CHECK")
print("A0 =", A0)
print("A0_FLOAT =", float(A0))
print("G0 =", G0)
print("G0_FLOAT =", float(G0))
print("DELTA0 =", DELTA0)
print("DELTA0_FLOAT =", float(DELTA0))
print("ETA0 =", ETA0)
print("ETA0_FLOAT =", float(ETA0))
print("EXAMPLE_U =", (a, b))
print("EXAMPLE_V =", (c, -d))
print("EXAMPLE_SUM =", (X, b - d))
print("KAPPA =", KAPPA)
print("KAPPA_FLOAT =", float(KAPPA))
print("BETA_UPPER_FLOAT =", float(BETA))
print("N =", n)
print("FINITE_ERROR_PER_N_FLOAT =", float(EPS))
print("FINITE_ERROR_NUM_BITS =", EPS.numerator.bit_length())
print("FINITE_ERROR_DEN_BITS =", EPS.denominator.bit_length())
print("FINITE_ERROR_LT_KAPPA =", EPS < KAPPA)
print("FINITE_RESIDUAL_PER_N_LB_FLOAT =", float(FINITE_PER_N))
print("FINITE_EXPECTED_RESIDUAL_LB_FLOAT =", float(FINITE_LB))
print("FINITE_EXPECTED_RESIDUAL_LB_POSITIVE =", FINITE_LB > 0)
print("ALL_EXACT_CHECKS_PASS")
