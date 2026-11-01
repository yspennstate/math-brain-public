from fractions import Fraction

# Exact rational certificate for the constants in the R16 I0036 dichotomy proof.
# No floating-point comparison is used in any assertion.

eps = Fraction(1, 42_000_000)
M = 2_625_000
A = 1000
L = 2

assert M * eps == Fraction(1, 16)

# Elementary algebraic bounds used for the trigonometric constants.
# sqrt(2) < 3/2
assert Fraction(2, 1) < Fraction(3, 2) ** 2
# sqrt(2) < 71/50, hence c_G=(1+sqrt2)/2 < 121/100
assert Fraction(2, 1) < Fraction(71, 50) ** 2
# sec(pi/8)^2 = 4/(2+sqrt2) < (11/10)^2.
# It suffices that sqrt2 > 158/121.
assert Fraction(2, 1) > Fraction(158, 121) ** 2

# K1 = (1+C0/A)/(1-eps), using C0<11/10.
K1_upper = (Fraction(1, 1) + Fraction(11, 10*A)) / (Fraction(1, 1) - eps)
assert K1_upper < Fraction(501, 500)

cG_upper = Fraction(121, 100)
K1_simple = Fraction(501, 500)

# Case (a): 256 sqrt2 L c_G K1.
Ca = 256 * Fraction(3, 2) * L * cG_upper * K1_simple
assert Ca == Fraction(2_909_808, 3_125)
assert Ca / M == Fraction(121_242, 341_796_875)
assert Ca / M < Fraction(1, 2)
# 1/2 < 22^{-3/16} iff 22^3 < 2^16.
assert 22**3 < 2**16

# Case (b): 2^15 L^2 c_G K1^2 (5/2)^2.
Cb = (2**15) * (L**2) * cG_upper * (K1_simple**2) * (Fraction(5, 2)**2)
assert Cb == Fraction(15_550_013_952, 15_625)
assert Cb / M == Fraction(647_917_248, 1_708_984_375)
assert Cb / M < Fraction(19, 50)
# 19/50 < 22^{-5/16} iff 22^5 * 19^16 < 50^16.
assert 22**5 * 19**16 < 50**16

# Direct-drop branch: 2^eps * 22^{2 M eps} < 2.
# eps<1/8 and 2 M eps=1/8, so lhs < 2^{1/8}22^{1/8}=44^{1/8}<2.
assert eps < Fraction(1, 8)
assert 2 * M * eps == Fraction(1, 8)
assert 44 < 2**8

# Base endpoint: q A > 500 is more than enough for D_1<11/10.
# q=22^{-1/16}>1/2 because 22<2^16.
assert 22 < 2**16
assert Fraction(A, 2) > Fraction(11, 10)

print('R16 I0036 exact dichotomy checker')
print('epsilon = 1/42000000')
print('M = 2625000, M*epsilon = 1/16')
print(f'K1_upper = {K1_upper.numerator}/{K1_upper.denominator} < 501/500')
print(f'Ca = {Ca.numerator}/{Ca.denominator}')
print(f'Ca/M = {(Ca/M).numerator}/{(Ca/M).denominator} < 1/2 < 22^(-3/16)')
print(f'Cb = {Cb.numerator}/{Cb.denominator}')
print(f'Cb/M = {(Cb/M).numerator}/{(Cb/M).denominator} < 19/50 < 22^(-5/16)')
print('22^5*19^16 =', 22**5 * 19**16)
print('50^16        =', 50**16)
print('ALL_EXACT_CHECKS_PASS')
