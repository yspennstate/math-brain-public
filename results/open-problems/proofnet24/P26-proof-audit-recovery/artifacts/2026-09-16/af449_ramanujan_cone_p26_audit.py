from fractions import Fraction


def ball_bound(d: int, r: int) -> int:
    if r <= 1:
        return 1
    return 1 + d * ((d - 1) ** (r - 1) - 1) // (d - 2)


def main() -> None:
    print("P26 independent exact audit: Aldous-Fill Open Problem 4.49(ii), C31 Ramanujan-cone theorem")

    baseline = Fraction(10786653, 2251652) / (Fraction(51, 44) * 2)
    assert baseline == Fraction(2326533, 1125826)
    print(f"baseline={baseline} decimal={float(baseline):.15f}")

    for s in [4, 7, 8, 16, 32, 64, 128]:
        d = s * s
        r = s
        x = Fraction(r * (d + 2), d + r)
        y = Fraction(2 * (d + 2), d + r)
        assert 2 * x == r * y
        assert x + Fraction(d, 2) * y == d + 2

        B = ball_bound(d, r)
        F_lower = Fraction(r * (d + 1) * (d + 3), (d + 2) * (d + r))
        rho_upper = Fraction(2 * s, d + 1)
        ratio_lower = F_lower * (1 - rho_upper) / 2
        ratio_formula = Fraction(
            r * (d + 3) * (d + 1 - 2 * s),
            2 * (d + 2) * (d + r),
        )
        assert ratio_lower == ratio_formula

        poly = 3 * s**4 - 9 * s**3 + 14 * s**2 - 26 * s + 12
        assert poly == 3 * s**3 * (s - 3) + 2 * (s - 1) * (7 * s - 6)
        assert poly > 0
        assert ratio_lower > Fraction(s, 8)

        print(f"s={s} d={d} r={r}")
        print(f"x={x} y={y} 2x=ry PASS normalization={x + Fraction(d, 2) * y}")
        print(f"ball_bound={B} sufficient_n={2 * B}")
        print(f"F_lower={F_lower}")
        print(f"rho_upper={rho_upper}")
        print(
            f"ratio_lower={ratio_lower} decimal={float(ratio_lower):.15f} "
            f"s_over_8={Fraction(s, 8)}"
        )
        print(f"positivity_poly={poly} PASS")

    assert Fraction(5422977, 177580) == Fraction(
        64 * (64**2 + 3) * (64**2 + 1 - 2 * 64),
        2 * (64**2 + 2) * (64**2 + 64),
    )
    print("P26_INDEPENDENT_EXACT_AUDIT_PASS")


if __name__ == "__main__":
    main()
