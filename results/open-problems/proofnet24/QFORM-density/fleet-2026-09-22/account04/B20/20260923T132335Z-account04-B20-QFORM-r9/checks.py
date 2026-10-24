#!/usr/bin/env python3
from fractions import Fraction
from math import sqrt, e

tau = Fraction(1, 192)
eta = Fraction(1, 12)
eps = Fraction(1, 80)
S = eta * eta * eps - tau * tau
T = Fraction(1, 23040)
arm = (S - T) / 2
det_gap = T - tau * tau
cross = Fraction(1, 4) * Fraction(191, 192) ** 2
packet4 = Fraction(63, 64) * cross
ridge = sqrt(e) / sqrt(2) * (48000 / 7911) * (2400 / 71)
d5 = 5 * sqrt(2 * e) * (120 * 64**4 / float(cross)**5) ** 0.1

assert S == Fraction(11, 184320)
assert arm == Fraction(1, 122880)
assert det_gap == Fraction(1, 61440)
assert cross == Fraction(36481, 147456)
assert packet4 == Fraction(2298303, 9437184)
assert 27911000 < 27965385
assert 707**2 < 500000
assert ridge < 239.109
assert d5 < 199.674

print(f"S={S}")
print(f"arm={arm}")
print(f"det_gap={det_gap}")
print(f"cross={cross}")
print(f"packet4={packet4}")
print(f"ridge={ridge:.12f}")
print(f"d5={d5:.12f}")
print("STATUS=PASS")
