from fractions import Fraction
import math


def h(u: Fraction) -> Fraction:
    return (Fraction(57) + 6*u - 39*u*u) / 32

u = [Fraction(9,49), Fraction(36,49), Fraction(4,49)]
hv = [h(x) for x in u]
cv = [x/Fraction(20) for x in hv]

assert h(Fraction(0)) == Fraction(57,32)
assert h(Fraction(1)) == Fraction(3,4)
assert all(x >= Fraction(3,4) for x in hv)
assert sum(hv) == Fraction(26475,5488)
assert sum(cv) == Fraction(5295,21952)

print('PASS QFORM_UNEQUAL_BANK_EDGEWORTH')
print('u =', ', '.join(map(str,u)))
print('h =', ', '.join(map(str,hv)))
print('h/20 =', ', '.join(map(str,cv)))
print('sum h =', sum(hv))
print('sum h/20 =', sum(cv))
print('partner coefficient =', Fraction(5295,21952))
print('min endpoint h =', min(h(Fraction(0)), h(Fraction(1))))
print('relative deficit lower coefficient =', Fraction(3,80))
print('3sqrt2 =', repr(3*math.sqrt(2)))
