from fractions import Fraction
from decimal import Decimal, getcontext

getcontext().prec = 70

K = 142
delta = Fraction(258204856, 10**9)
coarse = Fraction(4683, 18176)
gap = delta - coarse
assert gap == Fraction(19788013, 35500000000)
assert gap > 0

# Symmetric p=x=1/2 radius and improvement over K=176.
Q = Fraction(1, 16)
L = 8
radius_142 = Q / (K * L)
radius_176 = Q / (176 * L)
assert radius_142 == Fraction(1, 18176)
assert radius_176 == Fraction(1, 22528)
assert radius_142 / radius_176 == Fraction(88, 71)

# Exact algebra in (4.1): constant and the surviving negative 1/L credit.
constant = Fraction(31, K) + Fraction(11 * 65, 2 * K * 64)
assert constant == coarse
one_over_L_coefficient = -Fraction(68, K) + Fraction(11 * 12, 2 * K)
assert one_over_L_coefficient == -Fraction(1, 71)

# K=141 cannot close the inherited asymptotic envelope.
asym_141 = Fraction(73, 2 * 141)
asym_142 = Fraction(73, 2 * 142)
assert asym_141 > delta
assert asym_142 < delta

# Numerically evaluate the exact minimum slack of Lemma 3.1 as a cross-check.
# phi(L)=12+L/64-log2((1065/44)L) has unique minimum at L*=64/ln2.
D = Decimal
ln2 = D(2).ln()
Lstar = D(64) / ln2
B = D(1065) / D(44)
phi_min = D(12) + Lstar / D(64) - (B * Lstar).ln() / ln2
assert phi_min > D(2)

print('PASS')
print('delta =', float(delta))
print('coarse coefficient =', float(coarse))
print('exact delta gap =', gap)
print('symmetric radius K=142 =', radius_142, float(radius_142))
print('improvement factor =', radius_142 / radius_176, float(radius_142 / radius_176))
print('asymptotic K=141 =', float(asym_141))
print('asymptotic K=142 =', float(asym_142))
print('lemma critical L =', Lstar)
print('lemma minimum slack =', phi_min)
