from fractions import Fraction


def ball_bound(d: int, r: int) -> int:
    if r <= 1:
        return 1
    return 1 + d * ((d - 1) ** (r - 1) - 1) // (d - 2)


def main() -> None:
    print("C31 AF4.49(ii) direct-duality / Ramanujan-cone audit")

    baseline = Fraction(10786653, 2251652) / (Fraction(51, 44) * 2)
    assert baseline == Fraction(2326533, 1125826)
    print(f"PG49_ratio_lower={baseline} ~= {float(baseline):.12f}")

    for s in [4, 7, 8, 16, 32, 64, 128]:
        d = s * s
        r = s

        x = Fraction(r * (d + 2), d + r)
        y = Fraction(2 * (d + 2), d + r)
        assert 2 * x == r * y
        assert x + Fraction(d, 2) * y == d + 2

        B = ball_bound(d, r)
        n_min = 2 * B

        F_lower = Fraction(r * (d + 1) * (d + 3), (d + 2) * (d + r))
        rho_upper = Fraction(2 * s, d + 1)
        ratio_lower = F_lower * (1 - rho_upper) / 2

        ratio_closed = Fraction(
            (s - 1) ** 2 * (s * s + 3),
            2 * (s + 1) * (s * s + 2),
        )
        assert ratio_lower == ratio_closed

        # Sharper exact asymptotic certificate than the first-run s/8 bound:
        # ratio_lower - (s-3)/2 = (5s^2 - 2s + 9)/(2(s+1)(s^2+2)) > 0.
        diff = ratio_lower - Fraction(s - 3, 2)
        expected_diff = Fraction(
            5 * s * s - 2 * s + 9,
            2 * (s + 1) * (s * s + 2),
        )
        assert diff == expected_diff
        assert diff > 0

        print(
            f"s={s} d={d} r={r} n_min={n_min} "
            f"ratio_lower={ratio_lower} ~= {float(ratio_lower):.12f} > (s-3)/2"
        )

    print("ALL_EXACT_CHECKS_PASS")


if __name__ == "__main__":
    main()
