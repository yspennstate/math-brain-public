from fractions import Fraction
import math

# Exact algebraic switch constants in the pair/triple dichotomy.
c2 = Fraction(17, 1000)
c3 = Fraction(949, 2000)
assert 3*c2 + 2*c3 == 1

C3 = 2*math.pi + 3*math.sqrt(3)
pair = math.pi / math.sqrt(float(c2))
triple = C3 / float(c3)
C = max(pair, triple)

print('3*c2+2*c3 =', 3*c2 + 2*c3)
print('pair constant  = %.15f' % pair)
print('triple constant= %.15f' % triple)
print('max constant   = %.15f' % C)
print('max < 24.193   =', C < 24.193)

# The structural numerical identity behind the contradiction is
# 1 - 2*c3 = 3*c2.
assert 1 - 2*c3 == 3*c2
assert C < 24.193
print('PASS')
