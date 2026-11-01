from fractions import Fraction
from decimal import Decimal, getcontext

getcontext().prec = 60

# q=7 (free rank four), r=3 complementary directed generators.
q = 7
r = 3

# The free-core/complement polynomial at z=q is
# P(7)=7^2-(2*sqrt(7)+3)*7+(7+3)=38-14*sqrt(7).
# It is positive because 38^2 > 14^2*7.
assert 38**2 > (14**2) * 7
assert q*q > q+r

# Rational upper certificate for the larger nonbacktracking root
# beta=(3+2 sqrt(7)+sqrt(12 sqrt(7)-3))/2.
# sqrt(7)<127/48 since 127^2>7*48^2.
assert 127**2 > 7 * 48**2
# Therefore 12 sqrt(7)-3 < 115/4.  Also sqrt(115/4)<43/8.
assert Fraction(43, 8)**2 > Fraction(115, 4)

beta_upper = Fraction(41, 6)
assert beta_upper < q
p2_lower = 1 / beta_upper
assert p2_lower == Fraction(6, 41)

gap = p2_lower - Fraction(1, 7)
assert gap == Fraction(1, 287)

# Numerical context only; all theorem inequalities above are exact rational checks.
sqrt7 = Decimal(7).sqrt()
beta = (Decimal(3) + Decimal(2)*sqrt7 +
        (Decimal(12)*sqrt7 - Decimal(3)).sqrt()) / Decimal(2)
formula_gap = Decimal(1)/beta - Decimal(1)/Decimal(7)

print('T09 rank4+3 exact checker')
print(f'q={q}, r={r}, D={q+1+r}')
print(f'P(7)>0 certificate: 38^2={38**2} > 14^2*7={(14**2)*7}')
print(f'q^2>q+r certificate: {q*q}>{q+r}')
print(f'sqrt(7)<127/48 certificate: {127**2}>{7*48**2}')
print(f'sqrt(115/4)<43/8 certificate: {Fraction(43,8)**2}>{Fraction(115,4)}')
print(f'beta rational upper = {beta_upper}')
print(f'p_2to2 rational lower > {p2_lower}')
print(f'certified p_u-p_c gap > {gap}')
print(f'certified gap decimal = {Decimal(gap.numerator)/Decimal(gap.denominator)}')
print(f'beta numeric = {beta}')
print(f'exact-formula gap numeric = {formula_gap}')
print('ALL_EXACT_CHECKS_PASS')
