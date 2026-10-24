from fractions import Fraction as Q


def qpoly(lam):
    return 29 * lam * lam - 328 * lam + 720


def Asharp(lam):
    return (
        6 * lam / ((Q(3) - lam) * (Q(9) - lam))
        - 12 * lam / ((Q(4) - lam) * (Q(16) - lam))
    )


def Uratio(lam):
    return (Q(9) - lam) / (2 * (Q(6) - lam))


def theta(p, t):
    return p * t / (1 - p + p * t)


def vertex(A):
    return (A - 1) / (2 * A)


def G(A, th):
    return Q(3) + th - A * th * (1 - th)


def speed_margin(L, g):
    # M=3+theta<=4, hence (M+lambda)^2 <= (4+L)^2.
    return 2 * g / (Q(4) + L) ** 2


cases = [
    ("moderate_low", Q(71, 25), Q(1, 3), "low"),
    ("moderate_high", Q(71, 25), Q(2, 3), "high"),
    ("tail_low", Q(1429, 500), Q(1, 4), "low"),
    ("tail_high", Q(2861, 1000), Q(3, 4), "high"),
]

# Monotonicity of A_sharp on [1,3): if g1 and g2 are the two positive
# terms of A_sharp, then
# g1'/g2' >= (9/55)*(3/2)^2*(15/8)^2 = 3645/2816 > 1.
ratio_lower = Q(9, 55) * Q(9, 4) * Q(225, 64)
assert ratio_lower > 1
print("A_derivative_ratio_lower =", ratio_lower)

for name, L, p, side in cases:
    A = Asharp(L)
    assert qpoly(L) > 0
    if side == "low":
        t = Uratio(L)
        th = theta(p, t)
        assert th <= vertex(A)
    else:
        t = Q(4, 5)
        th = theta(p, t)
        assert th >= vertex(A)
    g = G(A, th)
    m = speed_margin(L, g)
    assert g > 0 and m > 0
    print(name)
    print("  L =", L)
    print("  qpoly(L) =", qpoly(L))
    print("  A_sharp(L) =", A)
    print("  t_bound =", t)
    print("  theta_bound =", th)
    print("  theta_vertex =", vertex(A))
    print("  G_margin =", g)
    print("  speed_derivative_margin =", m)

# Strict improvements over the immediate NM13-05 predecessor endpoints.
assert Q(71, 25) > Q(1131, 400)   # p<=1/3
assert Q(71, 25) > Q(283, 100)    # p>=2/3
assert Q(1429, 500) > Q(356, 125) # p<=1/4
assert Q(2861, 1000) > Q(713, 250) # p>=3/4
print("endpoint_improvements = PASS")
print("ALL_EXACT_CHECKS_PASS")
