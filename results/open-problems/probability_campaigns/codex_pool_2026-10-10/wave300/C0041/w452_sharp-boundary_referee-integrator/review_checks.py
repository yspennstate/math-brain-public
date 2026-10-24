"""Exact independent arithmetic for the finite-domain bridge counterexample."""

from fractions import Fraction as F


def main() -> None:
    weight_plus = F(51, 100)
    weight_minus = 1 - weight_plus
    plus = (F(9, 20), F(1, 20))
    minus = (F(1, 20), F(9, 20))
    rows = ((weight_plus, plus), (weight_minus, minus))
    numerator = F(0)
    denominator = F(0)
    terms = []
    for weight_s, row_s in rows:
        for weight_t, row_t in rows:
            green = 1 / (1 - row_s[1] * row_t[0])
            drift = row_s[0] - row_s[1]
            term = weight_s * weight_t * green * drift
            numerator += term
            denominator += weight_s * weight_t * green
            terms.append((green, term))
    mean_drift = weight_plus * (plus[0] - plus[1]) + weight_minus * (minus[0] - minus[1])
    print(f"mean_local_drift={mean_drift}")
    print(f"green_terms={terms}")
    print(f"weighted_numerator={numerator}")
    print(f"occupation_denominator={denominator}")
    print(f"kalikow_drift={numerator / denominator}")
    assert mean_drift == F(1, 125)
    assert numerator < 0 < denominator
    assert [x[0] for x in terms] == [F(400, 391), F(400, 399), F(400, 319), F(400, 391)]
    green = [x[0] for x in terms]

    def signed_numerator(theta: F) -> F:
        return F(2, 5) * ((2 * theta - 1) * green[0] + theta * (1 - theta) * (green[1] - green[2]))

    def claimed_polynomial(theta: F) -> F:
        return F(160, 49766871) * (31280 * theta * theta + 223282 * theta - 127281)

    for theta in (F(0), F(1, 2), F(51, 100), F(53, 100), F(531, 1000), F(1)):
        assert signed_numerator(theta) == claimed_polynomial(theta)
    assert signed_numerator(F(53, 100)) < 0 < signed_numerator(F(531, 1000))
    assert signed_numerator(F(51, 100)) == numerator
    kappa, b, theta = F(1, 20), F(1, 5), F(1, 10)
    generic = kappa * (2 * b * theta) / (1 - 3 * kappa)
    binary = (2 * b * theta) / (1 + (1 - theta) * b / F(1, 4))
    assert (generic, binary, binary / generic) == (F(1, 425), F(1, 43), F(425, 43))
    print(f"threshold_bracket=(53/100,531/1000); generic={generic}; binary={binary}; factor={binary/generic}")
    print("PASS: positive raw mean and negative finite-domain Kalikow drift")


if __name__ == "__main__":
    main()
