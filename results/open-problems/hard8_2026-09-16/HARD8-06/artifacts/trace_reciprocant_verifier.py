#!/usr/bin/env python3
"""
Exact symbolic checks for the reciprocal hard core of Lehmer's conjecture.

Requires: sympy

This script verifies three identities used in the HARD8-06 checkpoint:
  (1) every monic reciprocal even-degree Q has a unique trace polynomial R with
      Q(x)=x^d R(x+x^{-1});
  (2) for two such polynomials Q=x^d R(y), B=x^e S(y),
      Res_x(Q,B)=Res_y(R,S)^2;
  (3) Disc_x(Q)=R(2)R(-2) Disc_y(R)^2.

It then applies them to Lehmer's polynomial and cyclotomic polynomials Phi_n,
n=3,...,30, and asserts exact integer square resultants.
"""

import math
import sympy as sp

x, y = sp.symbols("x y")


def trace_from_reciprocal(Q):
    Q = sp.Poly(sp.expand(Q), x, domain=sp.ZZ)
    n = Q.degree()
    assert n % 2 == 0
    d = n // 2
    coeff = [Q.nth(i) for i in range(n + 1)]
    assert coeff == coeff[::-1], "Q must be reciprocal"
    assert Q.LC() == 1 and Q.nth(0) == 1, "Q must be monic with constant 1"

    C = [sp.Integer(2), y]
    for k in range(2, d + 1):
        C.append(sp.expand(y * C[-1] - C[-2]))
    R = sp.Integer(coeff[d])
    for k in range(1, d + 1):
        R += coeff[d + k] * C[k]
    R = sp.Poly(sp.expand(R), y, domain=sp.ZZ)
    assert R.degree() == d and R.LC() == 1

    lifted = sp.expand(x**d * R.as_expr().subs(y, x + 1/x))
    assert sp.expand(lifted - Q.as_expr()) == 0
    return R


def reciprocal_from_trace(R):
    R = sp.Poly(R, y, domain=sp.ZZ)
    d = R.degree()
    assert R.LC() == 1
    Q = sp.Poly(sp.expand(x**d * R.as_expr().subs(y, x + 1/x)), x, domain=sp.ZZ)
    assert Q.degree() == 2 * d
    assert Q.LC() == 1 and Q.nth(0) == 1
    assert [Q.nth(i) for i in range(2*d+1)] == [Q.nth(i) for i in range(2*d, -1, -1)]
    return Q


def assert_trace_identities(R, S):
    R = sp.Poly(R, y, domain=sp.ZZ)
    S = sp.Poly(S, y, domain=sp.ZZ)
    Q = reciprocal_from_trace(R)
    B = reciprocal_from_trace(S)

    rx = sp.resultant(Q.as_expr(), B.as_expr(), x)
    ry = sp.resultant(R.as_expr(), S.as_expr(), y)
    assert sp.Integer(rx) == sp.Integer(ry) ** 2

    disc_q = sp.discriminant(Q.as_expr(), x)
    disc_r = sp.discriminant(R.as_expr(), y)
    rhs = R.eval(2) * R.eval(-2) * sp.Integer(disc_r) ** 2
    assert sp.Integer(disc_q) == sp.Integer(rhs)


def main():
    L = sp.Poly(
        x**10 + x**9 - x**7 - x**6 - x**5 - x**4 - x**3 + x + 1,
        x, domain=sp.ZZ
    )
    R = trace_from_reciprocal(L.as_expr())
    expected_R = sp.Poly(y**5 + y**4 - 5*y**3 - 5*y**2 + 4*y + 3, y, domain=sp.ZZ)
    assert R == expected_R

    disc_L = sp.Integer(sp.discriminant(L.as_expr(), x))
    disc_R = sp.Integer(sp.discriminant(R.as_expr(), y))
    assert disc_L == R.eval(2) * R.eval(-2) * disc_R**2

    print("Lehmer trace polynomial:", R.as_expr())
    print("Disc(trace) =", disc_R)
    print("R(2), R(-2) =", R.eval(2), R.eval(-2))
    print("Disc(Lehmer) =", disc_L)
    print()

    samples = [
        (y**2 + 1, y**2 - y + 2),
        (y**3 + 2*y - 3, y**2 + y + 1),
        (y**3 - 2*y**2 + y + 1, y**3 + y**2 - 2),
    ]
    for A, B in samples:
        assert_trace_identities(A, B)
    print("Sample resultant/discriminant identities: VERIFIED")
    print()

    print("n  Res(L,Phi_n)  sqrt")
    for n in range(3, 31):
        phi = sp.Poly(sp.cyclotomic_poly(n, x), x, domain=sp.ZZ)
        psi = trace_from_reciprocal(phi.as_expr())
        r_x = sp.Integer(sp.resultant(L.as_expr(), phi.as_expr(), x))
        r_y = sp.Integer(sp.resultant(R.as_expr(), psi.as_expr(), y))
        assert r_x == r_y**2
        assert r_x >= 0
        s = math.isqrt(int(r_x))
        assert s*s == int(r_x)
        print(f"{n:2d} {int(r_x):12d} {s:6d}")

    print()
    print("All exact assertions passed.")


if __name__ == "__main__":
    main()
