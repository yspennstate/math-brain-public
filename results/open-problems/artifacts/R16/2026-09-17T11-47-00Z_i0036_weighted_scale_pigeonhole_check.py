from fractions import Fraction
from math import gcd

# Exact finite certificate for R16 I0036 weighted-scale pigeonhole theorem.
# All asserted comparisons below are integer/rational; floating point is used only for display.

A = 1000
QDEN = 21                  # theta = M*epsilon = 1/21
K = 128                    # number of logarithmic-scale bins
M = 689_024                # divisible by K
N = QDEN * M               # epsilon = 1/N
assert N == 14_469_504
assert M % K == 0
L = M // K
assert L == 5_383

# Scale-dependent threshold lambda_j = lambda0 * 22^(-j*epsilon).
lambda0 = Fraction(839, 625)  # 1.3424

# Geometric bin weights c_r = c0 * R^r, with average 1.
R = Fraction(218, 217)
S = sum(R**r for r in range(K))
c0 = Fraction(K, 1) / S
weights = [c0 * R**r for r in range(K)]
assert sum(weights, Fraction(0, 1)) == K
assert c0 > 0

# The geometric ratio is below the ideal compensation factor:
# R <= 22^(4/(21*K)) = 22^(1/672).
assert 4 * QDEN * K == 10_752
assert (218**672) < 22 * (217**672)

# Hence c_r * 22^(-4 j epsilon) <= c0 whenever j is in bin r.
# (The real-exponent implication is proved on the page; this is its exact integer core.)

# Exact envelopes used in the proof:
# C0=sec(pi/8)<11/10, cG=(1+sqrt(2))/2<121/100, sqrt(2)<3/2.
epsilon = Fraction(1, N)
K1_upper = Fraction(501, 500)
assert (Fraction(1, 1) + Fraction(11, 10*A)) / (Fraction(1, 1) - epsilon) < K1_upper

# Direct-drop branch.
# Analytically 2^epsilon < exp(epsilon) < 1/(1-epsilon).
# Check: (1/(1-epsilon))/lambda0 < 14899/20000 < 22^(-2/21).
direct_mid = Fraction(14_899, 20_000)
assert (Fraction(N, N-1) / lambda0) < direct_mid
assert (22**2) * (direct_mid.numerator**QDEN) < direct_mid.denominator**QDEN

# lambda_j remains >1 through the whole block: lambda0*q>1.
# It suffices that lambda0>6/5 and q=22^(-1/21)>5/6.
assert lambda0 > Fraction(6, 5)
assert 22 * (5**QDEN) < 6**QDEN

# Quadratic branch: c_r is uniformly <4/3.
cmax = weights[-1]
assert cmax < Fraction(4, 3)
# Expanded integer witness for cmax<4/3:
# 32 R^127 / sum_{0..127} R^r < 4/3.
# Fraction arithmetic above is the exact certificate.

case_a_upper = (
    Fraction(256, 1)
    * Fraction(3, 2)          # sqrt(2) upper bound
    * lambda0
    * Fraction(121, 100)      # cG upper bound
    * K1_upper
    * cmax
    / Fraction(M, 1)
)
assert case_a_upper < Fraction(1, 2)
# 1/2 < q^3 = 22^(-1/7) because 22<2^7.
assert 22 < 2**7

# Cubic branch. The geometric weights cancel the j-dependent factor exactly enough
# to replace the old uniform 1/M loss by c0/M.
case_b_upper = (
    Fraction(2**15, 1)
    * lambda0**2
    * Fraction(121, 100)
    * K1_upper**2
    * Fraction(25, 4)         # (5/2)^(2(1-epsilon)) < (5/2)^2
    * c0
    / Fraction(M, 1)
)

cubic_mid = Fraction(47_901, 100_000)
assert case_b_upper < cubic_mid
# cubic_mid < q^5 = 22^(-5/21)
assert (22**5) * (cubic_mid.numerator**QDEN) < cubic_mid.denominator**QDEN

# Historical metric movement.
old_N = 18_817_988
assert N < old_N

print('N =', N)
print('epsilon = 1/%d' % N)
print('M =', M, 'K =', K, 'L =', L)
print('lambda0 =', lambda0)
print('c0 ~= %.15f' % float(c0))
print('cmax ~= %.15f' % float(cmax))
print('case_a_upper ~= %.15f' % float(case_a_upper))
print('case_b_upper ~= %.15f' % float(case_b_upper))
print('direct_mid =', direct_mid)
print('cubic_mid =', cubic_mid)
print('improvement factor ~= %.12f' % (old_N / N))
print('ALL_EXACT_CHECKS_PASS')
