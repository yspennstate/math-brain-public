from fractions import Fraction
import math

th = Fraction(499, 1000)
assert th < Fraction(1, 2)
assert th / 2 == Fraction(499, 2000)
assert th / 8 == Fraction(499, 8000)
assert 3 * th / 8 == Fraction(1497, 8000)
beta = 1 - th / 8
assert beta == Fraction(7501, 8000)
assert beta / 2 == Fraction(7501, 16000)
assert beta / 4 == Fraction(7501, 32000)

# Fresh B19 paid-branch constants at theta=499/1000.
c1 = 50 * (1 - float(th)) ** (-3 / 4)
c2 = math.pi / math.sqrt(1 - 2 * float(th))
assert max(c1, c2) < 84

# Assigned fleet04/B20 terminal constant.
B = (2 + math.sqrt(math.pi)) * (4 * math.e) ** 0.25
partner = 768 * B
assert partner < 5262
assert 48 * 2 ** 0.75 < 81

print('theta=', th, float(th))
print('outer_sum_floor=', th/2, float(th/2))
print('two_cross_floor=', th/8, float(th/8))
print('outer_one_floor=', 3*th/8, float(3*th/8))
print('side_beta=', beta, float(beta))
print('pivot_floor=', beta/2, float(beta/2))
print('nested_floor=', beta/4, float(beta/4))
print('B19_branch_constants=', c1, c2, 'max=', max(c1,c2))
print('partner_768B=', partner)
print('STATUS=PASS')
