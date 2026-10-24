import math

Cstar = 2 + math.log(2) + math.sqrt(2*math.pi*math.e)*math.erfc(1/math.sqrt(2))
square_at_1_over_26 = 4 + 2*math.log(4*math.sqrt(2)) + math.log(26)
leak_at_1_over_26 = Cstar + 2**(11/4) * (676/675)**(1/4)

print('Cstar =', repr(Cstar))
print('square branch threshold bound =', repr(square_at_1_over_26))
print('leakage branch threshold bound =', repr(leak_at_1_over_26))
print('hybrid bound =', repr(max(square_at_1_over_26, leak_at_1_over_26)))
assert square_at_1_over_26 < 10.735
assert leak_at_1_over_26 < 10.735
