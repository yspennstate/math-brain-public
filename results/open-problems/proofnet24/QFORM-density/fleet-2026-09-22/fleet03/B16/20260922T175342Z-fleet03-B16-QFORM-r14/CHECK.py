from fractions import Fraction
import math

c = Fraction(3, 4)
inner = Fraction(-1, 4)
h = c - inner * inner / c
G = c * h
assert h == Fraction(2, 3)
assert G == Fraction(1, 2)

prefactor = (2.0 / 3.0) ** (2.0 / 3.0)
assert abs(prefactor - 0.7631428283688879) < 1e-15

# Packet supports: T_m support length=(3+1/m)/2 <=2 for m>=1;
# translations are separated by 5, so they are disjoint.
for m in range(1, 1001):
    width = (3.0 + 1.0 / m) / 2.0
    assert width <= 2.0
    assert width < 5.0

print('PASS')
print('residual_leverage=', h)
print('pair_gram_area=', G)
print('conditional_2_3_prefactor=', repr(prefactor))
