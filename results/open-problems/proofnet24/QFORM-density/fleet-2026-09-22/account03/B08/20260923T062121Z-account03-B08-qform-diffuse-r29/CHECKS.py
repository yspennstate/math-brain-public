from fractions import Fraction
import math

eta = Fraction(16,25)
q = 2*eta
kbar = Fraction(2,1)+eta
gap = kbar-2*q
ratio = kbar/gap

assert q == Fraction(32,25)
assert kbar == Fraction(66,25)
assert gap == Fraction(2,25)
assert ratio == 33

C = (math.e * float(q)**(-0.5) * float(ratio)
     * 6912**(1/(2*float(kbar)))
     * (float(eta)**float(eta)*float(1-eta)**float(1-eta))**(1/(2*float(kbar))))
assert C < 374

nested = eta/Fraction(6912,1)
assert nested == Fraction(1,10800)

intersection = 2*eta-1
assert intersection == Fraction(7,25)
double_nested = intersection/Fraction(6912,1)
assert double_nested == Fraction(7,172800)

edge_const = 1/(360*math.sqrt(6))
three_bank_const = 1/(360*math.sqrt(3))
joint_cap_const = 720*math.sqrt(6)

# Account03/B07 r26 applied after |edge|,||star||<=L.
G_floor = edge_const
vol_const = 4860*math.e*math.sqrt(6)
assert vol_const < 32360
bicore_const = math.sqrt(2/27)*G_floor
assert abs(bicore_const - 1/3240) < 1e-15

e2_denom = 192*360**4
match_denom = 3072*360**4

print('eta =', eta)
print('q =', q)
print('kbar =', kbar)
print('gap =', gap)
print('kbar/gap =', ratio)
print('C_16/25 = %.15f' % C)
print('nested coefficient =', nested)
print('double-nested coefficient =', double_nested)
print('edge-star-core coefficient = %.15g' % edge_const)
print('three-bank coefficient = %.15g' % three_bank_const)
print('partner joint-cap coefficient = %.15f' % joint_cap_const)
print('G floor coefficient = %.15g' % G_floor)
print('VOL coefficient = %.15f' % vol_const)
print('BICORE coefficient = 1/3240 = %.15g' % bicore_const)
print('E2 denominator =', e2_denom)
print('matching denominator =', match_denom)
print('QFORM_B08_R29_CHECK_PASS')
