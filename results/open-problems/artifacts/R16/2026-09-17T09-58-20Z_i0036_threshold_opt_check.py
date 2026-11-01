from fractions import Fraction
from math import e, log

A = 1000
M = 672_071
N = 18_817_988
eps = Fraction(1, N)
theta = M * eps
lam = Fraction(12_471, 10_000)

assert theta == Fraction(1, 28)

# Elementary exact algebraic envelopes used in the written proof.
# sqrt(2) < 71/50 => c_G=(1+sqrt(2))/2 < 121/100.
assert 2 * 50**2 < 71**2
# sqrt(2) < 3/2.
assert 2 * 2**2 < 3**2
# sec(pi/8)<11/10. Since cos^2(pi/8)=(2+sqrt(2))/4,
# it is enough that sqrt(2)>158/121.
assert 2 * 121**2 > 158**2

# K_1=((1+C_0/A)/(1-eps)); use C_0<11/10.
K1_upper = (1 + Fraction(11, 10*A)) / (1 - eps)
assert K1_upper < Fraction(501, 500)

# Large-ratio branch. Analytically 2^eps < exp(eps) < 1/(1-eps).
# The checker certifies the rational remainder of the comparison.
assert Fraction(N, N-1) < Fraction(100001, 100000)
large_rat = Fraction(100001, 100000) / lam
assert large_rat == Fraction(100001, 124710)
# 100001/124710 < 22^(-1/14).
assert 22 * large_rat.numerator**14 < large_rat.denominator**14

# Small-ratio case (a): use sqrt(2)<3/2, c_G<121/100,
# K_1<501/500, and threshold lambda=12471/10000.
Ca = 256 * Fraction(3, 2) * lam * Fraction(121, 100) * Fraction(501, 500)
Ca_over_M = Ca / M
assert Ca_over_M < Fraction(1, 1000)
# 1/1000 < 22^(-3/28).
assert 22**3 < 1000**28

# Small-ratio case (b): (5/2)^(2(1-eps)) < (5/2)^2.
Cb = (2**15 * lam**2 * Fraction(121, 100)
      * Fraction(501, 500)**2 * Fraction(25, 4))
Cb_over_M = Cb / M
bridge = Fraction(57577, 100000)
assert Cb_over_M < bridge
# 57577/100000 < 22^(-5/28).
assert 22**5 * bridge.numerator**28 < bridge.denominator**28

# q=22^(-1/28)>1/2, enough for the base endpoint bound with A=1000.
assert 22 < 2**28

# New exponent improves the previous R16 value 1/42,000,000.
assert eps > Fraction(1, 42_000_000)

# Route-saturation ingredient for eps<=1/100:
# (5/2)^(2(1-eps)) >= (5/2)^(99/50) > 6.
assert 5**99 > 2**149 * 3**50

print('R16 I0036 exact threshold-optimization checker')
print(f'epsilon = 1/{N} = {float(eps):.15g}')
print(f'M = {M}, M*epsilon = {theta}')
print(f'lambda = {lam} = {float(lam):.6f}')
print(f'K1_upper = {K1_upper} = {float(K1_upper):.12f} < 501/500')
print(f'large rational envelope = {large_rat} = {float(large_rat):.12f}')
print('large comparison: 22 * 100001^14 < 124710^14 =',
      22 * 100001**14 < 124710**14)
print(f'Ca/M = {Ca_over_M} = {float(Ca_over_M):.15g} < 1/1000')
print(f'Cb/M = {Cb_over_M} = {float(Cb_over_M):.15g} < 57577/100000')
print('case-b comparison: 22^5 * 57577^28 < 100000^28 =',
      22**5 * 57577**28 < 100000**28)
print(f'improvement factor over 1/42,000,000 = '
      f'{float(eps/Fraction(1,42_000_000)):.9f}')
Cnec = Fraction(36, 5) * 2**15
ceiling = 1 / (float(Cnec) * e * 9 * log(22))
print(f'one-threshold-method small-epsilon ceiling formula: '
      f'1/(9 e ({Cnec}) log 22) ~= {ceiling:.15g}')
print(f'candidate / ceiling ~= {float(eps)/ceiling:.9f}')
print('ALL_EXACT_CHECKS_PASS')
