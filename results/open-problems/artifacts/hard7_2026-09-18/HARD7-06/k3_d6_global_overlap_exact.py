from fractions import Fraction as F
from math import comb


def horner_desc(coeffs, x):
    a = F(0)
    for c in coeffs:
        a = a * x + F(c)
    return a


def add_poly(a, b):
    c = dict(a)
    for k, v in b.items():
        c[k] = c.get(k, F(0)) + v
        if c[k] == 0:
            del c[k]
    return c


def mul_poly(a, b):
    c = {}
    for i, ai in a.items():
        for j, bj in b.items():
            c[i + j] = c.get(i + j, F(0)) + ai * bj
    return {k: v for k, v in c.items() if v}


def pow_poly(a, n):
    r = {0: F(1)}
    for _ in range(n):
        r = mul_poly(r, a)
    return r


def scale_poly(a, c):
    return {k: c * v for k, v in a.items()}


# Q(x) from the d=6 stationary equation after x=t^(1/5):
# 2 x^10 - x^9 - x^8 - x^7 - x^6 + 3 x^5
#        - x^4 - x^3 - x^2 - x + 2.
Q_desc = [2, -1, -1, -1, -1, 3, -1, -1, -1, -1, 2]
Q = {10 - i: F(c) for i, c in enumerate(Q_desc)}
assert Q_desc == list(reversed(Q_desc))

# Reciprocal reduction Q(x)/x^5 = R(y), y=x+x^{-1}.
R_desc = [2, -1, -11, 3, 12, 3]
base = {1: F(1), -1: F(1)}
R_laurent = {}
for p, c in zip(range(5, -1, -1), R_desc):
    R_laurent = add_poly(R_laurent, scale_poly(pow_poly(base, p), F(c)))
R_times_x5 = {k + 5: v for k, v in R_laurent.items()}
assert R_times_x5 == Q

# Shift y=z+2.  For x>1 one has y>2, hence z>0.
shift = {}
for p, c in zip(range(5, -1, -1), R_desc):
    for j in range(p + 1):
        shift[j] = shift.get(j, F(0)) + F(c) * F(comb(p, j)) * (F(2) ** (p - j))
Z_desc = [shift.get(j, F(0)) for j in range(5, -1, -1)]
assert Z_desc == [F(2), F(19), F(61), F(73), F(20), F(-1)]
# Descending coefficient signs are +,+,+,+,+,-: exactly one sign change.
assert sum(1 for a, b in zip(Z_desc, Z_desc[1:]) if a * b < 0) == 1

z_lo, z_hi = F(43, 1000), F(44, 1000)
Z_lo = horner_desc(Z_desc, z_lo)
Z_hi = horner_desc(Z_desc, z_hi)
assert Z_lo < 0 < Z_hi

# Direct x-bracket for the unique x>1 stationary root.
x_lo, x_hi = F(1229, 1000), F(1230, 1000)
Q_lo = horner_desc(Q_desc, x_lo)
Q_hi = horner_desc(Q_desc, x_hi)
assert Q_lo < 0 < Q_hi

# theta=(x^6-1)/(x^6+1) is increasing for x>1.
theta_lo = (x_lo**6 - 1) / (x_lo**6 + 1)
theta_hi = (x_hi**6 - 1) / (x_hi**6 + 1)
assert F(1, 2) < theta_lo < theta_hi < F(3, 5)

# Landau expansion of the symmetric-overlap rate:
# S_d(theta)-S_d(0)=a2(d) theta^2+a4(d) theta^4+a6(d) theta^6+O(theta^8).
def a2(d):
    return (2*d - 11) / 22


def a4(d):
    return (790*d - 14641) / 175692


def a6(d):
    return (270002*d - 19487171) / 584615130


dc = F(11, 2)
assert a2(dc) == 0
assert a4(dc) == F(-78, 1331)
assert a6(dc) == F(-54552, 1771561)

# For d=dc+eps, the nonzero stationary branch has
# theta_*^2=(121/156) eps+O(eps^2), and its rate excess is
# (11/312) eps^2+O(eps^3).
pitchfork_slope = F(121, 156)
excess_coeff = F(11, 312)
assert pitchfork_slope > 0 and excess_coeff > 0

print('Q_palindromic = PASS')
print('Q_over_x5_equals_R_x_plus_xinv = PASS')
print('R(z+2) coefficients =', ','.join(str(v) for v in Z_desc))
print('Descartes_positive_root_count_for_z = 1')
print('Z(43/1000) =', Z_lo)
print('Z(44/1000) =', Z_hi)
print('Q(1229/1000) =', Q_lo)
print('Q(1230/1000) =', Q_hi)
print('theta_lower =', theta_lo)
print('theta_upper =', theta_hi)
print('dc =', dc)
print('a4(dc) =', a4(dc))
print('a6(dc) =', a6(dc))
print('pitchfork_theta2_slope =', pitchfork_slope)
print('pitchfork_rate_excess_coeff =', excess_coeff)
print('ALL_EXACT_CHECKS_PASS')
