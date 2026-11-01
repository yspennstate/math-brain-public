from fractions import Fraction

# HARD7-01 exact self-check for the finite rational core of run 15.
# This checks the n=3, q=4 Dirichlet spectral calibration and the
# curvature-margin consequence delta=1/16.  The general theorem is proved
# on the page in the run report; this script is not a substitute for it.

n = 3
q = 4
alpha = Fraction(1, q)
alpha0 = n * alpha

# W=(|Z_1|^q,...,|Z_n|^q) ~ Dirichlet(1/q,...,1/q).
EW1 = alpha / alpha0
EW1_sq = alpha * (alpha + 1) / (alpha0 * (alpha0 + 1))
var_W1 = EW1_sq - EW1 * EW1
EW1_one_minus = EW1 - EW1_sq

# Hessian-metric carré-du-champ multiplier on the l_q cone.
C = Fraction(q * q, 2 * (q - 1))
energy_W1 = C * EW1_one_minus
rayleigh_W1 = energy_W1 / var_W1
lambda_unc = Fraction(n * q, 2 * (q - 1))

assert EW1 == Fraction(1, 3)
assert EW1_sq == Fraction(5, 21)
assert var_W1 == Fraction(8, 63)
assert EW1_one_minus == Fraction(2, 21)
assert C == Fraction(8, 3)
assert energy_W1 == Fraction(16, 63)
assert rayleigh_W1 == Fraction(2, 1)
assert lambda_unc == Fraction(2, 1)

# Curvature margin delta=1/16:
# Var(U)/(m(1-m)) <= [2/(lambda+2)] (1-2 delta)^2.
delta = Fraction(1, 16)
ratio_bound = Fraction(2, 1) / (lambda_unc + 2) * (1 - 2 * delta) ** 2
target_ratio = Fraction(2, n + 2)

assert ratio_bound == Fraction(49, 128)
assert ratio_bound < target_ratio

# For p=2, n=3, k=n/p=3/2 and k+1=5/2.
# Cov(phi,psi) >= k [1-(k+1) ratio_bound] m(1-m).
k = Fraction(3, 2)
covariance_coefficient = k * (1 - Fraction(5, 2) * ratio_bound)
assert covariance_coefficient == Fraction(33, 512)
assert covariance_coefficient > 0

# The exact critical margin is delta_c = 1/2 - 1/sqrt(5).
# To verify delta=1/16 exceeds it without floating point, note
# 1/16 >= 1/2 - 1/sqrt(5) iff 1/sqrt(5) >= 7/16,
# and squaring positive quantities gives 256 >= 245.
assert 256 > 245

print("n =", n)
print("q =", q)
print("Dirichlet alpha =", alpha, "alpha0 =", alpha0)
print("E[W1] =", EW1)
print("E[W1^2] =", EW1_sq)
print("Var(W1) =", var_W1)
print("E[W1(1-W1)] =", EW1_one_minus)
print("metric factor C =", C)
print("energy =", energy_W1)
print("Rayleigh quotient =", rayleigh_W1)
print("lambda_unc =", lambda_unc)
print("delta =", delta)
print("variance-ratio bound =", ratio_bound)
print("target ratio =", target_ratio)
print("covariance coefficient =", covariance_coefficient)
print("delta=1/16 clears delta_c because 256 > 245")
print("ALL_EXACT_CHECKS_PASS = True")
