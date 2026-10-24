from fractions import Fraction as F
from math import comb


def u(lam):
    return (F(4) - lam) / 4


def d(lam, p):
    return F(1) - lam * (F(4) - p) / 12


def r(lam, p):
    return d(lam, p) / u(lam)


def fU(lam, m):
    return lam / (lam + m * u(lam)) ** 2


def fC(lam, m):
    a = lam - 1
    return a / (a + m * u(lam)) ** 2


def A_n(lam, n):
    return n * u(lam) / (lam + n * u(lam)) ** 2


def kstar(j, r0, vals):
    return sum(
        F(comb(j, m)) * r0 ** m * (1 - r0) ** (j - m) * vals[m]
        for m in range(j + 1)
    )


def theta0(p):
    return 4 * p / (5 - p)


def g(th):
    return th * (1 - th) / (3 + th)


def cell_bound(pL, pU, lL, lU):
    # On the target strip d increases in p and decreases in lambda;
    # r=d/u increases in p and decreases in lambda.
    dmin = d(lU, pL)
    r0 = r(lU, pL)
    assert dmin > 0 and 0 < r0 <= 1

    # f_m(lambda)=lambda/(lambda+m u(lambda))^2.
    # For 2<lambda<4: m=0,1 decrease; m=2,3 increase.
    fs = [fU(lL, 0), fU(lL, 1), fU(lU, 2), fU(lU, 3)]
    assert all(fs[i] >= fs[i + 1] for i in range(3))
    K2 = kstar(2, r0, fs)
    K3 = kstar(3, r0, fs)

    def rho_at(p):
        return (1 - p) * 3 * K2 + p * 4 * K3

    rho = max(rho_at(pL), rho_at(pU))
    assert rho < 1

    # A_3 and A_4 decrease in lambda on this strip.  The p-mixture is affine.
    A3 = A_n(lL, 3)
    A4 = A_n(lL, 4)

    def A_at(p):
        return (1 - p) * A3 + p * A4

    A = max(A_at(pL), A_at(pU))
    eta = A / (1 - rho)

    # h_m(lambda)=(lambda-1)/(lambda-1+m u(lambda))^2.
    # For 2<lambda<4: m=0,1 decrease; m=2,3 increase.
    hs = [fC(lL, 0), fC(lL, 1), fC(lU, 2), fC(lU, 3)]
    assert all(hs[i] >= hs[i + 1] for i in range(3))
    Kc = kstar(3, r0, hs)

    Delta = 1 / (lL - 1) + 3 * eta * Kc / dmin - 4 / (16 - lL)

    th = theta0(pL)
    # theta0(p)>=theta0(3/4)=12/17, to the decreasing side of g.
    assert th >= F(12, 17)
    product = lU * g(th) * Delta
    return product, rho, dmin, r0, eta, Kc, Delta


def run_case(name, p0, l0, l1, npieces, lpieces, target):
    assert F(2) < l0 < l1 < F(4)
    max_product = F(0)
    max_rho = F(0)
    worst = None

    for i in range(npieces):
        pL = p0 + (1 - p0) * i / npieces
        pU = p0 + (1 - p0) * (i + 1) / npieces
        for j in range(lpieces):
            lL = l0 + (l1 - l0) * j / lpieces
            lU = l0 + (l1 - l0) * (j + 1) / lpieces
            product, rho, dmin, r0, eta, Kc, Delta = cell_bound(
                pL, pU, lL, lU
            )
            if product > max_product:
                max_product = product
                worst = (i, j, pL, pU, lL, lU, rho, dmin, r0, eta, Kc, Delta)
            max_rho = max(max_rho, rho)

    assert max_product < target

    # M=3+theta >= 3+12/17 > l1 in all three cases. Therefore
    # 2M/(M+lambda)^2 is minimized at M=4, lambda=l1.
    derivative_margin = 8 / (4 + l1) ** 2 * (1 - target)

    print(name)
    print("  cells =", npieces * lpieces)
    print("  max_product =", max_product)
    print("  max_product_decimal =", float(max_product))
    print("  target =", target)
    print("  max_rho_decimal =", float(max_rho))
    print("  worst_cell =", worst[:6])
    print("  certified_derivative_margin =", derivative_margin)
    print("  certified_derivative_margin_decimal =", float(derivative_margin))


if __name__ == "__main__":
    inherited = F(2861, 1000)  # prior p>=3/4 certified endpoint

    run_case(
        "A_p_ge_3_4_to_157_50",
        F(3, 4), inherited, F(157, 50), 80, 160, F(49, 50),
    )
    run_case(
        "B_p_ge_4_5_to_163_50",
        F(4, 5), inherited, F(163, 50), 40, 100, F(99, 100),
    )
    run_case(
        "C_p_ge_41_50_to_33_10",
        F(41, 50), inherited, F(33, 10), 40, 100, F(19, 20),
    )

    print("ALL_EXACT_CHECKS_PASS")
