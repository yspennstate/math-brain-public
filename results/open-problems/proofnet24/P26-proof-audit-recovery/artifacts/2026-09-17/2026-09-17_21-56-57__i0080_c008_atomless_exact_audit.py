from fractions import Fraction as F
import sympy as sp

# Independent P26 exact-arithmetic audit of the finite core in R18-I0080-C008.
# This checks only the rational/symbolic inequalities used by the written proof;
# it does not replace the analytic proof or the already-audited C007 dependencies.

eps = F(1, 100)
kappa = F(8, 5)
d = F(19, 20)

# y=0 conservative lower bound using the retained C007 kernel bounds.
short0 = kappa * F(4193, 13200) * F(10000, 10003)
long0 = F(123, 125) * F(12, 25)
bound0 = short0 + long0
margin0 = bound0 - d
assert bound0 == F(144478732, 147365625)
assert margin0 == F(17925553, 589462500) and margin0 > 0

# y=3 strict separation.  The analytic proof uses
# arctan(1/3) > 26/81 and pi/20 < 11/70.
low_margin = F(26, 81) - F(11, 70) - F(16000, 99401)
assert low_margin == F(1623529, 563603670) and low_margin > 0

# y=ell/2 conservative lower bound.
high_mid = F(123, 125) * F(967, 1000)
margin_mid = high_mid - d
assert high_mid == F(118941, 125000)
assert margin_mid == F(191, 125000) and margin_mid > 0

# Robustness in epsilon: for 0 < epsilon <= 1/100, the y=0 lower
# bound and y=3 upper correction are both worst at epsilon=1/100.
e = sp.symbols('e', positive=True)
y0_factor = 1 / (1 + 3 * e**2)
y3_corr = sp.Rational(8, 5) / (1 + (3 - e)**2)
assert sp.simplify(sp.diff(y0_factor, e)) < 0
y3_num = sp.factor(sp.together(sp.diff(y3_corr, e))).as_numer_denom()[0]
assert sp.simplify(y3_num - (-16 * (e - 3))) == 0

# Exact all-time parameterization.
t, pi = sp.symbols('t pi', positive=True)
ell = 100 + 95 * pi * t
D = sp.Rational(19, 20) / ell
b2 = pi * D * t
assert sp.simplify(b2 - (sp.Rational(1, 100) - 1 / ell)) == 0
p = sp.Rational(8, 5) / ell
assert sp.simplify((sp.Rational(2, 125) - p) - 38 * pi * t / (25 * ell)) == 0

print('P26-I0080-C008-INDEPENDENT-EXACT-AUDIT: PASS')
print('y=0 lower bound =', bound0)
print('y=0 margin over 19/20 =', margin0)
print('y=3 rational separation margin =', low_margin)
print('y=ell/2 lower bound =', high_mid)
print('y=ell/2 margin over 19/20 =', margin_mid)
print('parameter identity: b(t)^2 = 1/100 - 1/ell(t): PASS')
print('robustness: both critical epsilon bounds are worst at epsilon=1/100 on 0<epsilon<=1/100: PASS')
