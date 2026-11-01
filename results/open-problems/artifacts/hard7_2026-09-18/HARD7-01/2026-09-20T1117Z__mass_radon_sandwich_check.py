from fractions import Fraction as F


def shoelace(poly):
    s = F(0)
    for (x1, y1), (x2, y2) in zip(poly, poly[1:] + poly[:1]):
        s += x1 * y2 - y1 * x2
    return abs(s) / 2

# Langi mass inequality + Chakerian: c_m >= 6 iff 6A-4h>=3P.
A, h, P = F(5, 2), F(9, 4), F(2)
K = 2 * A - F(4, 3) * h
cm = 2 * (K + 2 * P) / P
assert cm == 6
assert 6 * A - 4 * h == 3 * P

# Exact factorization of the two lower envelopes.
for a in [F(2), F(9, 4), F(5, 2), F(11, 4), F(3)]:
    lhs = F(3, 2) * (a + 1) * (6 - a) - 18
    rhs = F(3, 2) * (a - 2) * (3 - a)
    assert lhs == rhs and lhs >= 0
for a in [F(3), F(13, 4), F(7, 2), F(4)]:
    lhs = F(3, 2) * a * (a + 1) - 18
    rhs = F(3, 2) * (a - 3) * (a + 4)
    assert lhs == rhs and lhs >= 0

# Equality sanity checks for DF2: parallelogram and triangle.
Ksq = [(F(-1), F(-1)), (F(1), F(-1)), (F(1), F(1)), (F(-1), F(1))]
Dsq = [(F(-2), F(-2)), (F(2), F(-2)), (F(2), F(2)), (F(-2), F(2))]
Dsq_pol = [(F(1, 2), F(0)), (F(0), F(1, 2)), (F(-1, 2), F(0)), (F(0), F(-1, 2))]
Ktri = [(F(0), F(0)), (F(1), F(0)), (F(0), F(1))]
Dtri = [(F(1), F(0)), (F(1), F(-1)), (F(0), F(-1)), (F(-1), F(0)), (F(-1), F(1)), (F(0), F(1))]
Dtri_pol = [(F(1), F(1)), (F(0), F(1)), (F(-1), F(0)), (F(-1), F(-1)), (F(0), F(-1)), (F(1), F(0))]

def area(poly):
    s = F(0)
    for (x1, y1), (x2, y2) in zip(poly, poly[1:] + poly[:1]):
        s += x1 * y2 - y1 * x2
    return abs(s) / 2

sq_lhs = (area(Dsq) + 2 * area(Ksq)) * area(Dsq_pol)
tri_lhs = (area(Dtri) + 2 * area(Ktri)) * area(Dtri_pol)
assert (area(Ksq), area(Dsq), area(Dsq_pol), sq_lhs) == (4, 16, F(1, 2), 12)
assert (area(Ktri), area(Dtri), area(Dtri_pol), tri_lhs) == (F(1, 2), 3, 3, 12)

print("mass_rearrangement_boundary =", 6 * A - 4 * h - 3 * P)
print("low_interval_samples = exact_nonnegative")
print("high_interval_samples = exact_nonnegative")
print("DF2_square_endpoint =", sq_lhs)
print("DF2_triangle_endpoint =", tri_lhs)
print("ALL_EXACT_CHECKS_PASS = True")
