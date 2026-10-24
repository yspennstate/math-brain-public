from fractions import Fraction
from math import comb

EPS = Fraction(56721646463783, 2500000000000000)
THRESH = Fraction(1, 20)

# R(m)=1-5m+7m^2-EPS*(31m^4-59m^3+25m^2+m+1).
# We certify R(m)-1/20 >= 0 on [0,1] by exact degree-4 Bernstein
# coefficients on the eleven rational subintervals [j/11,(j+1)/11].
COEFF = [
    Fraction(1) - EPS - THRESH,
    Fraction(-5) - EPS,
    Fraction(7) - 25 * EPS,
    59 * EPS,
    -31 * EPS,
]

def affine_power(c, a, b):
    h = b - a
    n = len(c) - 1
    out = [Fraction(0) for _ in range(n + 1)]
    for k, ck in enumerate(c):
        for j in range(k + 1):
            out[j] += ck * comb(k, j) * a ** (k - j) * h ** j
    return out

def power_to_bernstein(d):
    n = len(d) - 1
    return [
        sum(d[j] * Fraction(comb(k, j), comb(n, j)) for j in range(k + 1))
        for k in range(n + 1)
    ]

global_min = None
global_box = None
global_index = None
for box in range(11):
    a = Fraction(box, 11)
    b = Fraction(box + 1, 11)
    bern = power_to_bernstein(affine_power(COEFF, a, b))
    m = min(bern)
    assert m >= 0
    if global_min is None or m < global_min:
        global_min = m
        global_box = box
        global_index = bern.index(m)

# The derivative of the minimal-disagreement local gap as a function of x=c^2
# is m*(30 EPS x + 15 EPS m^2 - 18 EPS - 6).  Since 0<=x,m<=1
# and EPS<1/5, it is at most m*(27/5-6)<0 for m>0.
assert EPS < Fraction(1, 5)
assert Fraction(27, 1) * EPS - 6 < 0

# r=eta(1/2)=1-EPS dominates the 1/20 coefficient used to combine the
# disagreement excess with the boundary gap.
r = 1 - EPS
assert r >= THRESH

print('PASS')
print('epsilon', EPS, float(EPS))
print('subintervals', 11)
print('bernstein_global_min', global_min, float(global_min))
print('bernstein_min_box', global_box)
print('bernstein_min_index', global_index)
print('R_lower_bound', THRESH, float(THRESH))
print('r', r, float(r))
print('derivative_upper_coefficient', 27 * EPS - 6, float(27 * EPS - 6))
print('local_currency_consequence', 'ell >= (delta-m^2)/20 = Q/5')
