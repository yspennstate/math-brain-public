from fractions import Fraction


def F_lower(s: int) -> Fraction:
    d = s * s
    r = s
    return Fraction(r * (d + 1) * (d + 3), (d + 2) * (d + r))


def inverse_tau_lower(s: int) -> Fraction:
    return Fraction((s - 1) ** 2, s * s + 1)


def L(s: int) -> Fraction:
    return Fraction((s - 1) ** 2 * (s * s + 3), 2 * (s + 1) * (s * s + 2))


def check_s(s: int) -> None:
    assert s >= 4
    d = s * s
    r = s
    x = Fraction(r * (d + 2), d + r)
    y = Fraction(2 * (d + 2), d + r)
    assert 2 * x == r * y
    assert x + Fraction(d, 2) * y == d + 2
    direct = F_lower(s) * inverse_tau_lower(s) / 2
    assert direct == L(s)
    rhs = Fraction(5 * s * s - 2 * s + 9, 2 * (s + 1) * (s * s + 2))
    assert L(s) - Fraction(s - 3, 2) == rhs
    assert rhs > 0
    print(f"s={s} d={d} x={x} y={y} F_lb={F_lower(s)} L_s={L(s)} decimal={float(L(s)):.15f}")


for s in (4, 7, 8, 16, 32, 64, 128):
    check_s(s)

assert L(64) == Fraction(5422977, 177580)
print(f"L_64={L(64)} decimal={float(L(64)):.15f}")
print("ALL_EXACT_CHECKS_PASS")
