from fractions import Fraction as F

# PROB10-05 exact self-check for the Mills-ratio improvement.
# Analytic theorem proved in the accompanying report:
#   for m(x)=(1-Phi(x))/phi(x), x>0,
#   m(x) < 4/(3x+sqrt(x^2+8)).
# This script checks every theorem-deciding finite/rational comparison
# after that analytic lemma, plus the final spectral contradiction.

r = F(7, 8)
rho = F(168557580, 170952323)
b = F(167065920, 170952323)
mu_lo = F(9116948312, 10_000_000_000)
mu_hi = F(9116948313, 10_000_000_000)
eps2 = F(47004495, 100_000_000_000)

# q after the Gaussian change of measure in the equicorrelated endpoint.
q = F(6,25) * rho / (1 + rho)
S_old = 1 - q + 3*q*q - 15*q**3 + 105*q**4

# 4/(3+sqrt(1+8q)) < 91/100 is equivalent to
# sqrt(1+8q) > 127/91.  Check the squared rational inequality.
mills_sq_margin = (1 + 8*q) - F(127,91)**2
assert mills_sq_margin > 0

# Lower bound needed to turn the expectation improvement into a normalized
# four-cycle-trace improvement.
Ainv = (1-rho)/(1+rho)
sqrtAinv_lb = F(8398,100000)
sqrt_margin = Ainv - sqrtAinv_lb**2
assert sqrt_margin > 0

# Old proof used S_old as an upper bound for E[(1+qY^2)^(-1)].
# New analytic lemma gives the strict upper bound 91/100.
delta_norm_lb = sqrtAinv_lb * (S_old - F(91,100)) / F(16) / (1-r**4)
assert delta_norm_lb > F(117, 1_000_000)

# Consume the already certified normalized equicorrelated cap 1.091019.
eq_old_cap = F(1_091_019,1_000_000)
eq_new_cap = F(1_090_902,1_000_000)
assert eq_old_cap - F(117,1_000_000) == eq_new_cap

# Consume the already certified 64-block Plackett decrement
# P(rho)-P(b) > 147/40000.
plackett_dec = F(147,40000)
trace_bound = eq_new_cap - plackett_dec/(1-r**4)
trace_cap = F(1_082_022,1_000_000)
assert trace_bound < trace_cap

# New source-level lower-bound target theta*=0.16548.
theta_before = F(41369,250000)
theta_target = F(4137,25000)
assert theta_target > theta_before
exp = 4*theta_target
x = F(572129,625000)     # 0.9154064
beta = F(981313,1250000) # 0.7850504

# Exact x < r^(4 theta*) using integer powers.
assert exp == F(4137,6250)
power_lhs = x.numerator**exp.denominator * r.denominator**exp.numerator
power_rhs = x.denominator**exp.denominator * r.numerator**exp.numerator
assert power_lhs < power_rhs

assert beta < mu_lo < mu_hi < x

# If lambda_1 >= x, the fourth-trace cap forces every non-Perron spectral
# point below beta in modulus.
tail_margin = beta**4 - (trace_cap - x**4)
assert tail_margin > 0

# Inherited degree-18 quasimode/Temple contradiction.
temple_margin = (x-mu_hi)*(mu_lo-beta) - eps2
assert temple_margin > 0

width_before = F(1,4) - theta_before
width_after = F(1,4) - theta_target
gain = theta_target - theta_before

print("q =", q, float(q))
print("S_old =", S_old, float(S_old))
print("mills_sq_margin =", mills_sq_margin, float(mills_sq_margin))
print("sqrt_margin =", sqrt_margin, float(sqrt_margin))
print("delta_norm_lb =", delta_norm_lb, float(delta_norm_lb))
print("trace_bound =", trace_bound, float(trace_bound))
print("trace_cap =", trace_cap, float(trace_cap))
print("theta_before =", theta_before, float(theta_before))
print("theta_target =", theta_target, float(theta_target))
print("gain =", gain, float(gain))
print("width_before =", width_before, float(width_before))
print("width_after =", width_after, float(width_after))
print("x =", x, float(x), "power_check =", power_lhs < power_rhs)
print("beta =", beta, float(beta))
print("tail_margin =", tail_margin, float(tail_margin))
print("temple_margin =", temple_margin, float(temple_margin))
print("ALL_EXACT_CHECKS_PASS = True")