#!/usr/bin/env python3
"""Independent, standard-library-only rational audit of A14's smooth certificate.

Run from the workspace root: python research/code/a20_certificate_audit.py
No quadrature or imports from a14_checks.py are used. The one-dimensional
polynomial identity and the Gaussian Wick moments are checked separately.
"""

from fractions import Fraction as F


def polynomial_product(a: tuple[int, ...], b: tuple[int, ...]) -> tuple[int, ...]:
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return tuple(out)


def check_sqrt_envelope() -> None:
    """For t=sqrt(S)>=0, prove envelope minus t=(t-1)^4/[4(t^2+1)]."""
    # 4(t^2+1){(1+t^2)/2-t}-(t^2-1)^2 = (t-1)^4.
    one_plus_t2 = (1, 0, 1)
    t2_minus_one = (-1, 0, 1)
    left_a = polynomial_product((2, -4, 2), one_plus_t2)
    left_b = polynomial_product(t2_minus_one, t2_minus_one)
    assert tuple(x - y for x, y in zip(left_a, left_b)) == polynomial_product(
        polynomial_product((-1, 1), (-1, 1)),
        polynomial_product((-1, 1), (-1, 1)),
    ) == (1, -4, 6, -4, 1)


def double_factorial_odd(n: int) -> int:
    """E G^(2n) for G standard normal, including n=0."""
    out = 1
    for j in range(1, n + 1):
        out *= 2 * j - 1
    return out


def multiply_bivariate(a: dict[tuple[int, int], F],
                       b: dict[tuple[int, int], F]) -> dict[tuple[int, int], F]:
    result: dict[tuple[int, int], F] = {}
    for (i, j), x in a.items():
        for (k, ell), y in b.items():
            key = (i + k, j + ell)
            result[key] = result.get(key, F(0)) + x * y
    return result


def gaussian_expectation(poly: dict[tuple[int, int], F]) -> F:
    """Z,V0 iid N(0,1): a key (i,j) represents Z^(2i) V0^(2j)."""
    return sum((value * double_factorial_odd(i) * double_factorial_odd(j)
                for (i, j), value in poly.items()), F(0))


def even_norm_moments(beta: F) -> tuple[F, F, F]:
    # S=||(I-beta X X^T)e||^2 = (1-beta Z^2)^2+beta^2 Z^2 V0^2,
    # where Z=e.X and V0 is its independent orthogonal Gaussian coordinate.
    s_poly = {(0, 0): F(1), (1, 0): -2 * beta,
              (2, 0): beta**2, (1, 1): beta**2}
    power = {(0, 0): F(1)}
    moments = []
    for _ in range(3):
        power = multiply_bivariate(power, s_poly)
        moments.append(gaussian_expectation(power))
    return tuple(moments)


def main() -> None:
    check_sqrt_envelope()
    eta, eps = F(13, 25), F(1, 1000)
    m2, m4, m6 = even_norm_moments(eta)
    assert (m2, m4, m6) == (
        F(651, 625), F(1848809, 390625), F(1088264059, 9765625)
    )
    q = m4 - 2 * m2 + 1          # E(S-1)^2
    t = m6 - m4 - m2 + 1         # E[(S-1)^2(S+1)]
    assert q > 0 and t > 0
    # Weighted Cauchy gives E[(S-1)^2/(S+1)] >= q^2/t.
    tangent = (1 + m2) / 2
    deficit = q**2 / (4 * t)
    h1_bound = tangent - deficit
    assert h1_bound == F(7941802637, 8025437500) < 1 < m2

    # |g'-1| <= eps(7+2|Y|) follows from sech^2<=1,
    # |z|sech^2(z)<=1, |tanh(z)|<=1, and eps<=1.
    # Wick: E[Z^2||X||^2]=E Z^4+E Z^2 E V0^2=3+1=4.
    z2_r2 = double_factorial_odd(2) + double_factorial_odd(1)**2
    assert z2_r2 == 4
    # E|Z| ||X|| <= sqrt(4)=2; E|Y| <= sqrt(E Y^2)=1.
    k_bound = eta * 2 * (7 + 2)
    kappa = h1_bound + eps * k_bound
    assert k_bound == F(234, 25)
    assert kappa == F(2004230183, 2006359375) < 1
    assert 1 - kappa == F(2129192, 2006359375)

    for label, value in (
        ("m2 = h(2)", m2), ("m4", m4), ("m6", m6),
        ("Q", q), ("T", t), ("tangent", tangent),
        ("deficit", deficit), ("h(1) upper", h1_bound),
        ("E K upper", k_bound), ("kappa upper", kappa),
        ("1-kappa lower", 1 - kappa),
    ):
        print(f"{label}: {value}")
    print("sqrt envelope identity: exact; all certified inequalities: pass")
    print("unique positive root: 1 < alpha < 2 (log-convexity)")
    print("alpha ~ 1.84032259: numerical diagnostic only; not certified here")


if __name__ == "__main__":
    main()
