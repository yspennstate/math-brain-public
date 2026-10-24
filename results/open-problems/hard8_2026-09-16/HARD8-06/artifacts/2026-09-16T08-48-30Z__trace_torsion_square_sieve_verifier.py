#!/usr/bin/env python3
"""
Exact verifier for HARD8-06 checkpoint 2026-09-16T08-48-30Z.

Requires Python 3 + sympy.  All mathematical checks use exact ZZ or F_3
polynomial arithmetic; no floating point and no solver timeout is involved.

Verified claims:
  1. Chebyshev square identities for A_k.
  2. Trace-torsion resultant factorization
         Res(Q, x^k-1) = Q(1) Res(R,A_k)^2                  (k odd)
         Res(Q, x^k-1) = Q(1)Q(-1) Res(R,A_k)^2            (k even)
     for deterministic random trace polynomials.
  3. Exact p=3 criterion: 3 is in the signed-collision exceptional set E_m
     iff R mod 3 has an irreducible factor of degree <= m.
  4. Lehmer-polynomial torsion resultant benchmark through k=12.

Resultant convention: sympy.resultant(f,g,var) with monic f agrees with the
norm/product resultant prod_{f(rho)=0} g(rho), which is the convention used
in the report.
"""

import itertools
import random
import sympy as sp

x, y = sp.symbols("x y")


def C(n: int):
    if n == 0:
        return sp.Integer(2)
    if n == 1:
        return y
    a, b = sp.Integer(2), y
    for _ in range(1, n):
        a, b = b, sp.expand(y * b - a)
    return sp.Poly(b, y, domain=sp.ZZ).as_expr()


def A(k: int):
    """Integral trace polynomial whose square gives C_k-2."""
    assert k >= 1
    ck = C(k)
    denom = y - 2 if (k % 2) else y * y - 4
    q = sp.Poly(sp.cancel((ck - 2) / denom), y, domain=sp.ZZ)
    coeff, factors = sp.factor_list(q.as_expr())
    assert coeff == 1
    out = sp.Integer(1)
    for fac, exponent in factors:
        assert exponent % 2 == 0
        out *= sp.expand(fac) ** (exponent // 2)
    return sp.Poly(sp.expand(out), y, domain=sp.ZZ).as_expr()


def trace_lift(R):
    D = sp.degree(R, y)
    return sp.Poly(sp.expand(x**D * R.subs(y, x + 1 / x)), x, domain=sp.ZZ).as_expr()


def check_chebyshev_squares():
    for k in range(1, 31):
        ak = A(k)
        rhs = (y - 2) * ak**2 if (k % 2) else (y * y - 4) * ak**2
        assert sp.expand(C(k) - 2 - rhs) == 0
    return 30


def check_resultant_factorization():
    rng = random.Random(20260916)
    checks = 0
    for D in range(1, 6):
        for _ in range(12):
            R = y**D + sum(rng.randint(-4, 4) * y**j for j in range(D))
            Q = trace_lift(R)
            assert sp.degree(Q, x) == 2 * D
            assert sp.expand(x ** (2 * D) * Q.subs(x, 1 / x) - Q) == 0
            for k in range(1, 13):
                lhs = sp.resultant(Q, x**k - 1, x)
                rak = sp.resultant(R, A(k), y)
                if k % 2:
                    rhs = Q.subs(x, 1) * rak**2
                else:
                    rhs = Q.subs(x, 1) * Q.subs(x, -1) * rak**2
                assert sp.expand(lhs - rhs) == 0, (D, R, k, lhs, rhs)
                checks += 1
    return checks


def in_E3_by_enumeration(R, m: int) -> bool:
    R3 = sp.Poly(R, y, modulus=3)
    basis = [sp.Poly(C(j), y, modulus=3) for j in range(m + 1)]
    for coeffs in itertools.product((-1, 0, 1), repeat=m + 1):
        if all(c == 0 for c in coeffs):
            continue
        expr = sum((c * basis[j].as_expr() for j, c in enumerate(coeffs)), sp.Integer(0))
        B = sp.Poly(expr, y, modulus=3)
        # C_0,...,C_m are a basis mod 3, so this must never be zero.
        assert not B.is_zero
        if sp.degree(sp.gcd(R3, B)) >= 1:
            return True
    return False


def least_factor_degree_mod3(R) -> int:
    _, factors = sp.factor_list(sp.Poly(R, y, modulus=3))
    assert factors
    return min(sp.degree(fac) for fac, _ in factors)


def check_characteristic_three_criterion():
    rng = random.Random(6032026)
    checks = 0
    for D in range(1, 7):
        for _ in range(30):
            R = y**D + sum(rng.randint(-6, 6) * y**j for j in range(D))
            fmin = least_factor_degree_mod3(R)
            for m in range(0, min(D, 5)):
                actual = in_E3_by_enumeration(R, m)
                expected = fmin <= m
                assert actual == expected, (R, D, m, fmin, actual)
                checks += 1
    return checks


def check_lehmer_benchmark():
    Q = x**10 + x**9 - x**7 - x**6 - x**5 - x**4 - x**3 + x + 1
    R = y**5 + y**4 - 5*y**3 - 5*y**2 + 4*y + 3
    assert trace_lift(R) == Q
    assert Q.subs(x, 1) == -1
    assert Q.subs(x, -1) == 1

    expected = {
        1: (1, -1),
        2: (1, -1),
        3: (1, -1),
        4: (-3, -9),
        5: (1, -1),
        6: (1, -1),
        7: (1, -1),
        8: (-3, -9),
        9: (1, -1),
        10: (1, -1),
        11: (1, -1),
        12: (9, -81),
    }
    rows = []
    for k in range(1, 13):
        rak = int(sp.resultant(R, A(k), y))
        rq = int(sp.resultant(Q, x**k - 1, x))
        assert (rak, rq) == expected[k], (k, rak, rq)
        if k % 2:
            assert rq == int(Q.subs(x, 1)) * rak * rak
        else:
            assert rq == int(Q.subs(x, 1) * Q.subs(x, -1)) * rak * rak
        rows.append((k, rak, rq))

    R3 = sp.Poly(R, y, modulus=3)
    # R_L == y*(y^4+y^3+y^2+y+1) mod 3.
    target = sp.Poly(y * (y**4 + y**3 + y**2 + y + 1), y, modulus=3)
    assert R3 == target
    assert least_factor_degree_mod3(R) == 1
    assert not in_E3_by_enumeration(R, 0)
    assert in_E3_by_enumeration(R, 1)
    return rows


def main():
    n_square = check_chebyshev_squares()
    n_res = check_resultant_factorization()
    n_char3 = check_characteristic_three_criterion()
    rows = check_lehmer_benchmark()

    print(f"Chebyshev-square identities checked: {n_square}")
    print(f"Random exact resultant factorizations checked: {n_res}")
    print(f"Characteristic-3 criterion checks: {n_char3}")
    print("Lehmer rows (k, Res(R,A_k), Res(Q,x^k-1)):")
    for row in rows:
        print(row)
    print("ALL EXACT CHECKS PASSED")


if __name__ == "__main__":
    main()
