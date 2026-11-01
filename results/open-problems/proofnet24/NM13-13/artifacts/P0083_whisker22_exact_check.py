from fractions import Fraction as F


def main() -> None:
    # Rational envelope used in the proof of the alpha > 22 whisker bound.
    d0 = F(51, 500)

    # At alpha = 22, delta_22=(1-sqrt(7/11))/2 < 51/500.
    assert (1 - 2 * d0) ** 2 < F(7, 11)
    assert d0 < F(1, 3)

    # With alpha*delta*(1-delta)=2 and
    # log(1+delta) < delta-delta^2/2+delta^3/3,
    # alpha log(1+delta) is bounded by g(delta), and g is increasing.
    g_d0 = 2 * (1 - d0 / 2 + d0 * d0 / 3) / (1 - d0)
    assert g_d0 == F(238117, 112250)

    # e^x < (1-x/50)^(-50), since -log(1-u)>u for 0<u<1.
    m = 50
    one_minus = 1 - g_d0 / m
    exp_upper = one_minus ** (-m)
    target = (1 - d0) / d0
    assert one_minus == F(5374383, 5612500)
    assert target == F(449, 51)
    assert exp_upper < target

    # Same final comparison as a single exact integer inequality.
    assert 51 * 5612500**50 < 449 * 5374383**50

    print("PASS")
    print("d0 = 51/500")
    print("(1-2d0)^2 = 39601/62500 < 7/11")
    print("g(d0) = 238117/112250")
    print("exp rational upper = (5612500/5374383)^50")
    print("target = 449/51")
    print("exact comparison: True")


if __name__ == "__main__":
    main()
