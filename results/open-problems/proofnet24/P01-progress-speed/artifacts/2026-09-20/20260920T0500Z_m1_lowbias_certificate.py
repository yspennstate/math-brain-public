from fractions import Fraction


def certificate(D, L):
    L = Fraction(L)
    Q = Fraction(D - 1, 1) / ((1 - L) * (Fraction(D, 1) - L))
    A = L * Q
    H = D - 1
    if A <= 1:
        delta = Fraction(1, 1)
    else:
        delta = Fraction(1, 1) - Fraction(H, 1) * (A - 1) ** 2 / (4 * A)
    margin = 2 * delta / (Fraction(D, 1) + L) ** 2
    return Q, A, delta, margin


def show(D, L):
    Q, A, delta, margin = certificate(D, L)
    print(f"D={D} L={L} Q={Q} A={A} delta={delta} margin={margin}")
    return Q, A, delta, margin


# Breadth endpoint: all supercritical no-leaf laws with 1 <= nu <= 26.
q, a, delta, margin = show(26, Fraction(3, 5))
assert q == Fraction(625, 254)
assert a == Fraction(375, 254)
assert delta == Fraction(599, 15240)
assert margin == Fraction(2995, 26958036)
assert delta > 0

# Immediate method boundary at the same rational bias endpoint.
q, a, delta, margin = show(27, Fraction(3, 5))
assert delta == Fraction(-1, 440)
assert margin == Fraction(-5, 837936)
assert delta < 0

# Deeper rectangles.
q, a, delta, margin = show(9, Fraction(2, 3))
assert delta == Fraction(71, 600)
assert margin == Fraction(213, 84100)
assert delta > 0
q, a, delta, margin = show(10, Fraction(2, 3))
assert delta == Fraction(-1, 168)
assert margin == Fraction(-3, 28672)
assert delta < 0

q, a, delta, margin = show(3, Fraction(4, 5))
assert delta == Fraction(39, 880)
assert margin == Fraction(195, 31768)
assert delta > 0
q, a, delta, margin = show(4, Fraction(4, 5))
assert delta == Fraction(-41, 80)
assert margin == Fraction(-205, 4608)
assert delta < 0

q, a, delta, margin = show(2, Fraction(13, 15))
assert delta == Fraction(599, 26520)
assert margin == Fraction(8985, 1634516)
assert delta > 0

# Source-wide old low-bias endpoint lambda=1/2 lies strictly inside every finite-D certificate.
for D in range(2, 201):
    q, a, delta, margin = certificate(D, Fraction(1, 2))
    assert a < 1
    assert delta == 1
    assert margin > 0

print("ALL_EXACT_CHECKS_PASS")
