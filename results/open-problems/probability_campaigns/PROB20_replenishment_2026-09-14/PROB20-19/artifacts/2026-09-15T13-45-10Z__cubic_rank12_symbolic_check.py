"""Exact symbolic checks for PROB20-19 cubic projection-moment completion.

This file checks the algebraic identities used in the 2026-09-15T13-40-18Z
report. It is not a numerical proof of the Mallat-Zeitouni conjecture; it only
certifies the polynomial simplifications in the rank-one/rank-two diagonal
lemmas and the resulting cubic-gap coefficients.

Requires: sympy.
"""

import sympy as sp


def main() -> None:
    a, b, N, D1, D2, Delta2 = sp.symbols(
        "a b N D1 D2 Delta2", positive=True
    )

    # Rank-two capped-simplex polynomial.
    g = lambda x: 3*x**3 - 5*x**2 + 2*x
    merge_g = sp.factor(g(a) + g(b) - g(a+b))
    assert merge_g == -a*b*(9*a + 9*b - 10)
    print("rank-2 boundary merge identity:", merge_g)

    # Interior two-value critical point: g'(a)=g'(b) -> a+b=10/9.
    x = sp.symbols("x")
    gp = sp.diff(g(x), x)
    critical_difference = sp.factor(gp.subs(x, a) - gp.subs(x, b))
    assert critical_difference == (a-b)*(9*a + 9*b - 10)
    print("rank-2 critical-value identity:", critical_difference)

    # One singleton a, N-1 repeated values b.
    bN = sp.Rational(8, 9)/(N-2)
    aN = sp.Rational(10, 9) - bN
    interior_value = sp.factor(g(aN) + (N-1)*g(bN))
    expected = 8*(59*N**2 - 356*N + 540)/(243*(N-2)**2)
    assert sp.simplify(interior_value - expected) == 0
    disc = sp.discriminant(59*N**2 - 356*N + 540, N)
    assert disc == -704
    print("rank-2 two-value interior objective:", interior_value)
    print("rank-2 numerator discriminant:", disc)

    # Equal interior point x_i=2/N.
    equal_value = sp.factor(N*g(sp.Rational(2, 1)/N))
    assert equal_value == 4*(N-3)*(N-2)/N**2
    print("rank-2 equal-point objective:", equal_value)

    # Rank-one merge identity.
    h = lambda x: 2*x**3 - 3*x**2 + x
    merge_h = sp.factor(h(a) + h(b) - h(a+b))
    assert merge_h == -6*a*b*(a+b-1)
    print("rank-1 merge identity:", merge_h)

    # Cubic-gap lower bounds after applying the diagonal-ratio lemmas.
    # rank 2: 18 D1 + (5/3)(D2 - 10 D1) = (4 D1 + 5 D2)/3.
    rank2_coeff = sp.factor(18*D1 + sp.Rational(5, 3)*(D2-10*D1))
    assert rank2_coeff == (4*D1 + 5*D2)/3
    print("rank-2 cubic-gap coefficient:", rank2_coeff)

    # rank 1: 15 D1 + (3/2)(D2 - 10 D1) = 3 D2 / 2.
    rank1_coeff = sp.factor(15*D1 + sp.Rational(3, 2)*(D2-10*D1))
    assert rank1_coeff == sp.Rational(3, 2)*D2
    print("rank-1 cubic-gap coefficient:", rank1_coeff)

    print("ALL EXACT SYMBOLIC CHECKS PASSED")


if __name__ == "__main__":
    main()
