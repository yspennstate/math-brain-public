from fractions import Fraction as F

# Gaussian-baseline moments used in REPORT.md.
EH4_x = F(57, 32)
EH4_r = F(3, 4)
first = -F(1, 20) * (2 * EH4_x + EH4_r)
assert first == -F(69, 320)

EH6_x = -F(945, 128)
EH8_x = F(91035, 2048)
EH6_r = -F(15, 8)
EH8_r = F(105, 16)
EH4_xy = F(7803, 2048)
EH4_xr = F(603, 128)

E2x = EH6_x / 105 + EH8_x / 800
E2r = EH6_r / 105 + EH8_r / 800
cross = (EH4_xy + 2 * EH4_xr) / 400
second = 2 * E2x + E2r + cross

assert E2x == -F(4833, 327680)
assert E2r == -F(173, 17920)
assert cross == F(27099, 819200)
assert second == -F(17411, 2867200)

print('first =', first)
print('E2x =', E2x)
print('E2r =', E2r)
print('cross =', cross)
print('second =', second)
print('PASS')
