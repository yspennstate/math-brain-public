from fractions import Fraction


def check_baseline():
    dual = Fraction(10786653, 2251652)
    tau = Fraction(51, 44)
    ratio = dual / (2 * tau)
    assert ratio == Fraction(2326533, 1125826)
    gap_c2 = dual - 4 * tau
    assert gap_c2 == Fraction(3818931, 24768172)
    return dual, tau, ratio, gap_c2


def grassmann_values(k: int):
    assert k >= 2
    A = 2**k - 1                      # [k]_2
    d = 2 * A * A                     # valency of J_2(2k,k)
    theta1 = A * A - 2 * A

    # Standard Grassmann eigenvalues specialized to q=2,n=2k.
    # Verify the exact ordering identity theta_1 - theta_j >= 0.
    for j in range(2, k + 1):
        Akj = 2 ** (k - j) - 1
        theta_j = 2 ** (j + 1) * Akj * Akj - (2**j - 1)
        closed = (2 ** (j - 1) - 1) * (2 ** (2 * k - j + 1) - 2)
        assert theta1 - theta_j == closed
        assert closed >= 0

    tau = Fraction(d + 1, (A + 1) ** 2)
    assert tau < 2

    # E dim(U cap V) <= expected number of lines in U cap V = A/(A+2).
    mu_lower = Fraction(k, 1) - Fraction(A, A + 2)
    assert mu_lower > k - 1

    # Dual lengths on the cone.
    x = Fraction(k * (d + 2), d + k)
    y = Fraction(2 * (d + 2), d + k)
    assert 2 * x == k * y
    assert x + Fraction(d, 2) * y == d + 2

    # Base/base contribution alone gives a rigorous F lower bound.
    F_base = Fraction(2 * (d + 1) ** 2, (d + 2) * (d + k)) * mu_lower
    R_base = F_base / (2 * tau)        # D(cone)=2

    Q = Fraction((d + 1) * (A + 1) ** 2, (d + 2) * (d + k))
    assert R_base == Q * mu_lower

    # Exact positivity proving Q > 1/2.
    numerator = 2 * (d + 1) * (A + 1) ** 2 - (d + 2) * (d + k)
    closed_num = 2 * (A * A * (4 * A - k + 1) + 2 * A - k + 1)
    assert numerator == closed_num
    assert numerator > 0
    assert Q > Fraction(1, 2)
    assert R_base > Fraction(k - 1, 2)

    return A, d, theta1, tau, mu_lower, x, y, F_base, R_base, Q


def main():
    dual, tau, ratio, gap = check_baseline()
    print("BASELINE_EXACT")
    print("dual =", dual)
    print("tau =", tau)
    print("ratio =", ratio)
    print("constant2_gap =", gap)
    print()

    for k in [2, 4, 8, 16, 32, 64, 128]:
        A, d, theta1, tau, mu, x, y, F, R, Q = grassmann_values(k)
        print(f"k={k}")
        print("A =", A)
        print("d =", d)
        print("theta1 =", theta1)
        print("tau =", tau)
        print("mu_lower =", mu)
        print("dual_x =", x)
        print("dual_y =", y)
        print("base_F_lower =", F)
        print("ratio_lower =", R)
        print("simple_ratio_certificate >", Fraction(k - 1, 2))
        print("Q =", Q)
        print()

    print("ALL_EXACT_CHECKS_PASS")


if __name__ == "__main__":
    main()
