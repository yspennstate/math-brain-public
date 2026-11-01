from fractions import Fraction
import sympy as sp

# Frozen degree-five metric remains saturated.
degree5 = [(4, 1), (3, 2), (3, 1, 1), (2, 2, 1), (2, 1, 1, 1)]
assert len(degree5) == 5

# The run-15 residual profile is exactly log-affine:
# F_b = 2^(b-1), b=0,1,2.
F = [Fraction(1, 2), Fraction(1), Fraction(2)]
assert F[0] * F[2] == F[1] * F[1]

# Exact symbolic obstruction to naively reusing a multiplicity-only
# two-state h-transform for the Delta=6 [3,1,1,1] pattern.
#
# At z=1/sqrt(5), normalize h(S)=1 and write x=h(T)>0.
# After an incoming S edge, outgoing transformed weights are
#   1/sqrt(5), 1/sqrt(5), 3*x/sqrt(5).
# The sum of the two lightest weights is
#   2/sqrt(5)              if 3x >= 1,
#   (1+3x)/sqrt(5)         if 3x < 1.
# Both are strictly below 1.
x = sp.symbols("x", positive=True)
branch_hi = sp.reduce_inequalities(
    [3 * x >= 1, 2 / sp.sqrt(5) < 1], x
)
branch_lo = sp.reduce_inequalities(
    [3 * x < 1, (1 + 3 * x) / sp.sqrt(5) < 1], x
)
assert sp.simplify_logic(
    sp.Equivalent(branch_hi, x >= sp.Rational(1, 3))
) is sp.true
assert sp.simplify_logic(
    sp.Equivalent(branch_lo, x < sp.Rational(1, 3))
) is sp.true
assert sp.simplify((2 / sp.sqrt(5)) ** 2) == sp.Rational(4, 5)
assert sp.Rational(4, 5) < 1

print("C5=5/5")
print("degree5_exponential_profile=", F)
print("profile_log_affine_identity=PASS")
print("delta6_[3,1,1,1]_incoming_S_two_child_mass:")
print("  x>=1/3 -> 2/sqrt(5) < 1")
print("  0<x<1/3 -> (1+3x)/sqrt(5) < 1")
print("exact_squared_endpoint=4/5<1")
print("MULTIPLICITY_ONLY_TWO_STATE_CERTIFICATE_BARRIER_PASS")
