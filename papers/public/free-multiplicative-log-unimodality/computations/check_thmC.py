"""Exact check of the rational inequalities in the proof of Lemma 5.2 and Theorem C.

Only Fraction arithmetic enters an assertion. pi is enclosed by Machin's formula with alternating-series bounds;
the transcendental facts used in the paper are reduced to rational ones as follows.
  cot(1/20) > 799/40       from cos x > 1 - x^2/2 and sin x < x at x = 1/20
  tanh 5 > 9/10            equivalent to e^10 > 19 (partial sum of the exponential series)
  tanh(5/2) > 29/30        equivalent to e^5 > 59
  arctan x > pi/2 - 1/x    for x > 0;  arctan(1/3) > 1/3 - 1/81
Usage: python check_thmC.py   (prints PASS)
"""
from fractions import Fraction as F
from math import factorial


def atan_bounds(z, n):
    """Lower and upper bounds for arctan z, 0 <= z <= 1, from the first n terms of the alternating series."""
    s = sum((-1) ** k * z ** (2 * k + 1) / F(2 * k + 1) for k in range(n))
    nxt = z ** (2 * n + 1) / F(2 * n + 1)
    return (s, s + nxt) if n % 2 == 0 else (s - nxt, s)


def exp_lower(x, n):
    return sum(F(x) ** k / F(factorial(k)) for k in range(n))


a5 = atan_bounds(F(1, 5), 24)
a239 = atan_bounds(F(1, 239), 8)
PI_LO, PI_HI = 16 * a5[0] - 4 * a239[1], 16 * a5[1] - 4 * a239[0]
assert F(333, 106) < PI_LO and PI_HI < F(22, 7) < F(63, 20)
print("pi enclosure: 333/106 < pi < 22/7 < 63/20")

x = F(1, 20)
X = (1 - x ** 2 / 2) / x
assert X == F(799, 40)
print("cot(1/20) > (1 - x^2/2)/x =", X)

assert exp_lower(10, 3) > 19 and exp_lower(5, 5) > 59
T5, T52 = F(9, 10), F(29, 30)
assert X * T5 == F(7191, 400) and X * T52 == F(23171, 1200)
print("tanh 5 > 9/10 and tanh(5/2) > 29/30; X tanh 5 > 7191/400, X tanh(5/2) > 23171/1200")

# W(0) > 19/20:  2X/(25 pi) + (123/125)(1/2 - 400/(7191 pi)) > 19/20, i.e.
# 799/500 - (123/125)(400/7191) > (229/500) pi, checked with pi < 63/20.
assert 1 - F(8, 5 * 100) == F(123, 125)
assert F(8, 5) * X / 20 == 2 * X / 25 and 2 * X / 25 == F(799, 500)
lhs0 = F(799, 500) - F(123, 125) * F(400, 7191)
rhs0 = F(229, 500) * F(63, 20)
assert F(19, 20) - F(123, 250) == F(229, 500) and lhs0 > rhs0
print("W(0):    799/500 - (123/125)(400/7191) =", float(lhs0), "> (229/500)(63/20) =", float(rhs0))

# W(3) < 19/20:  arctan(1/3) > pi/20 + 4/25, via arctan(1/3) > 26/81 > 11/70 + 4/25 and pi/20 < 11/70.
assert F(1, 3) - F(1, 3) ** 3 / 3 == F(26, 81) and atan_bounds(F(1, 3), 2)[0] == F(26, 81)
assert F(26, 81) > F(11, 70) + F(4, 25) and F(22, 7) / 20 == F(11, 70)
assert F(8, 5) * F(1, 10) == F(4, 25)       # (8/5) K_0(3) = 4/(25 pi)
print("W(3):    26/81 - (11/70 + 4/25) =", F(26, 81) - F(11, 70) - F(4, 25))

# W(l/2) > 19/20:  (246/(125 pi))(pi/2 - 1200/23171) > 19/20, i.e. (17/500) pi > (246/125)(1200/23171), with pi > 3.
assert F(123, 125) - F(19, 20) == F(17, 500)
lhs2, rhs2 = F(17, 500) * 3, F(246, 125) * F(1200, 23171)
assert lhs2 > rhs2
print("W(l/2):  (17/500)*3 =", float(lhs2), "> (246/125)(1200/23171) =", float(rhs2))

# Parameters: l >= 95 pi t gives b^2 = 19 pi t/(20 l) <= 1/100; p = 8/(5l) <= 2/125; l b >= (19/2) pi t.
d = F(19, 20)
assert d / 95 == F(1, 100) and F(8, 5) / 100 == F(2, 125) and d * 95 == F(19, 2) ** 2
print("parameters: b^2 <= 1/100, p <= 2/125, (l b)^2 >= (19 pi t / 2)^2")
print("PASS")
