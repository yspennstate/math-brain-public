#!/usr/bin/env python3
"""
R17 exact checker for run 20260916_2015Z_slackopt_51ac.

No Monte Carlo.

C010 sharpens R17-C009 using only the certified minimum multiplicative slack
extracted from Lueker's published h=8 error analysis and the deliberately coarse
safe inequality z > 0.32.

It also proves an information ceiling for every amplification certificate that
uses only those two pieces of information.
"""
from fractions import Fraction
from math import comb, factorial
from decimal import Decimal, getcontext

getcontext().prec = 80

a = Fraction(16777215, 562949953421312)
b = Fraction(256, 625)

k = 7
N = 209_648_759
partial = sum(Fraction(comb(N,j)) * a**j for j in range(27))
amp_lower = b**k * partial
amp_margin = amp_lower - 1
assert amp_margin > 0

p0 = 826_280
q0 = 1_000_000
p = N*p0
q = N*q0+k
U_new = Fraction(p,q)

U_prev = Fraction(24_788_400_000_000, 30_000_000_000_001)
assert U_new < U_prev

L = Fraction(792_665_992, 1_000_000_000)
W_prev = U_prev - L
W_new = U_new - L
assert W_new < W_prev

U_lueker = Fraction(826_280, 1_000_000)
assert U_new < U_lueker

# Information ceiling for the certified-minimum-slack amplification route.
N0 = 29_949_822
x = Fraction(N0) * a
assert 0 < x < 1

# Since log(1+a)<=a, (1+a)^N0 <= exp(x).  For the exponential
# series, from term 9 onward the ratio is at most x/10.
exp_upper = sum(x**j / Fraction(factorial(j)) for j in range(9))
exp_upper += (x**9 / Fraction(factorial(9))) / (1 - x/Fraction(10))

exp_margin = Fraction(625,256) - exp_upper
assert exp_margin > 0

U_floor = Fraction(N0*p0, N0*q0 + 1)
assert U_floor < U_new

floor_gap = U_new - U_floor
assert floor_gap == Fraction(
    4_131_400,
    6_278_943_014_571_317_297_513_000_007
)

assert U_new == Fraction(173_228_576_586_520, 209_648_759_000_007)
assert W_new == Fraction(
    880_891_882_776_315_417_257,
    26_206_094_875_000_875_000_000
)

c009_gain = U_prev - U_new
lueker_gain = U_lueker - U_new

print("R17-C010 EXACT CHECK: PASS")
print("a =", a)
print("b =", b)
print("k =", k, "N =", N)
print("finite binomial terms used = 0..26")
print("amplification margin =", amp_margin)
print("amplification margin decimal =", Decimal(amp_margin.numerator)/Decimal(amp_margin.denominator))
print()
print("C010 upper endpoint =", U_new)
print("C010 upper endpoint decimal =", Decimal(U_new.numerator)/Decimal(U_new.denominator))
print("C009 upper endpoint =", U_prev)
print("C009 -> C010 decrease =", c009_gain)
print("C009 -> C010 decrease decimal =", Decimal(c009_gain.numerator)/Decimal(c009_gain.denominator))
print("Lueker 0.826280 -> C010 decrease =", lueker_gain)
print("Lueker -> C010 decrease decimal =", Decimal(lueker_gain.numerator)/Decimal(lueker_gain.denominator))
print()
print("lower endpoint L =", L)
print("new interval width =", W_new)
print("new interval width decimal =", Decimal(W_new.numerator)/Decimal(W_new.denominator))
print()
print("N0 =", N0)
print("x=N0*a =", x)
print("625/256 - rigorous exp upper =", exp_margin)
print("exp-upper margin decimal =", Decimal(exp_margin.numerator)/Decimal(exp_margin.denominator))
print("certified slope bracket: 7/209648759 < c < 1/29949822")
print("information-floor endpoint =", U_floor)
print("C010 - information floor =", floor_gap)
print("C010 - information floor decimal =", Decimal(floor_gap.numerator)/Decimal(floor_gap.denominator))
print()
print("ALL_EXACT_CHECKS_PASS")
