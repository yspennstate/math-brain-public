from fractions import Fraction


def A_crude(d, delta):
    L = Fraction(d, 1) - delta
    return Fraction(d * (d - 1), 1) * L / (
        (Fraction(d, 1) - L) * (Fraction(d * d, 1) - L)
    )


def theta_lower(d, p):
    alpha = Fraction(d + 1, d + 2)
    return p * alpha / (1 - p + p * alpha)


def gap_small(d, delta):
    A = A_crude(d, delta)
    return Fraction(d, 1) - A * delta


def gap_large(d, delta):
    A = A_crude(d, delta)
    p = 1 - delta
    th = theta_lower(d, p)
    return Fraction(d, 1) + th - A * th * (1 - th)


def polyN(d):
    return (
        10000 * d**5
        + 39900 * d**4
        + 1019800 * d**3
        - 9900 * d**2
        - 989600 * d
        + 9999
    )


delta = Fraction(1, 100)
d = 3
L = Fraction(d, 1) - delta
A = A_crude(d, delta)
gs = gap_small(d, delta)
gl = gap_large(d, delta)
theta0 = theta_lower(d, 1 - delta)
denmax = Fraction(2 * d + 1, 1) - delta
ms = 2 * gs / (denmax**2)
ml = 2 * gl / (denmax**2)

print("delta =", delta)
print("d=3 L =", L)
print("A =", A)
print("small_tail_gap =", gs, float(gs))
print("large_tail_theta_lower =", theta0, float(theta0))
print("large_tail_gap =", gl, float(gl))
print("uniform_derivative_margin_small =", ms, float(ms))
print("uniform_derivative_margin_large =", ml, float(ml))

for D in [2, 3, 4, 5, 10, 100, 1000]:
    gsD = gap_small(D, delta)
    glD = gap_large(D, delta)
    assert gsD > 0
    assert glD > 0
    assert polyN(D) > 0
    print("d", D, "gap_small", gsD, "gap_large", glD, "N", polyN(D))

# Analytic proof for all integer d>=2 groups
# N(d) = [10000 d^5 - 9900 d^2] + 39900 d^4
#      + [1019800 d^3 - 989600 d] + 9999,
# whose four displayed terms are positive for d>=2.
assert all(polyN(D) > 0 for D in range(2, 1001))
print("CHECKED d=2..1000 exact; analytic grouping proves all d>=2")
print("ALL_EXACT_CHECKS_PASS")
