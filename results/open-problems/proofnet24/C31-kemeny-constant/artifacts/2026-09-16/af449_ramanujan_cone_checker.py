from fractions import Fraction


def ball_bound(d: int, r: int) -> int:
    """Maximum possible number of vertices at graph distance < r in max degree d."""
    if r <= 1:
        return 1
    return 1 + d * ((d - 1) ** (r - 1) - 1) // (d - 2)


def main() -> None:
    print("C31 AF4.49(ii) Ramanujan-cone exact arithmetic checker")

    # Exact lower ratio from the archived PG(2,49) cone certificate.
    baseline = Fraction(10786653, 2251652) / (Fraction(51, 44) * 2)
    print(f"prior_projective_plane_ratio_lower={baseline} ~= {float(baseline):.12f}")

    for s in [4, 7, 8, 16, 32, 64, 128]:
        d = s * s
        r = s

        # Cone dual lengths: 2x = r y and x + (d/2)y = d+2.
        x = Fraction(r * (d + 2), d + r)
        y = Fraction(2 * (d + 2), d + r)
        assert x + Fraction(d, 2) * y == d + 2

        # If a d-regular base has n >= 2B(d,r), then for independent
        # uniform U,V, P(dist(U,V) >= r) >= 1/2, hence
        # E[min(dist(U,V),r)] >= r/2.
        B = ball_bound(d, r)
        n_min = 2 * B

        # Resulting exact metric-dual lower bound for F.
        F_lower = Fraction(r * (d + 1) * (d + 3), (d + 2) * (d + r))

        # For a d-regular Ramanujan base, theta_2 <= 2 sqrt(d-1).
        # Since d=s^2, sqrt(d-1)<s, so this rational value is a strict
        # upper bound on lambda_2 of the cone.
        rho_upper = Fraction(2 * s, d + 1)

        # D(cone)=2 and tau_rel <= 1/(1-rho_upper), so this is a strict
        # lower bound on F/(tau_rel D).
        ratio_lower = F_lower * (1 - rho_upper) / 2
        ratio_formula = Fraction(
            r * (d + 3) * (d + 1 - 2 * s),
            2 * (d + 2) * (d + r),
        )
        assert ratio_lower == ratio_formula

        # With d=s^2 and r=s,
        # ratio_lower - s/8 = P(s) / [8(s+1)(s^2+2)],
        # P(s)=3s^4-9s^3+14s^2-26s+12.
        poly = 3 * s**4 - 9 * s**3 + 14 * s**2 - 26 * s + 12
        assert poly > 0
        assert ratio_lower > Fraction(s, 8)

        print(f"s={s} d={d} r={r}")
        print(f"  x={x} y={y} normalization={x + Fraction(d, 2) * y}")
        print(f"  ball_bound_B={B}")
        print(f"  sufficient_order_n_min={n_min}")
        print(f"  F_lower={F_lower}")
        print(f"  rho_upper={rho_upper}")
        print(
            f"  ratio_lower={ratio_lower} ~= {float(ratio_lower):.12f} "
            f"> s/8={Fraction(s, 8)}"
        )
        print(f"  positivity_poly={poly}")

    print("ALL_EXACT_CHECKS_PASS")


if __name__ == "__main__":
    main()
