#!/usr/bin/env python3
"""Exact integral-basis checks for the HARD8-06 relative index-square formula.

Requires Python 3 + sympy.  SymPy's round_two computes exact maximal orders
and field discriminants for the small irreducible examples below.
"""

import math
import sympy as sp
from sympy.polys.numberfields import round_two

x, y = sp.symbols('x y')


def reciprocal_from_trace(R):
    R = sp.Poly(R, y, domain=sp.ZZ)
    D = R.degree()
    return sp.Poly(sp.expand(sp.cancel(x**D * R.as_expr().subs(y, x + 1/x))), x, domain=sp.ZZ)


def square_index(poly, field_disc, var):
    pd = abs(int(sp.discriminant(poly.as_expr(), var)))
    fd = abs(int(field_disc))
    q, r = divmod(pd, fd)
    assert r == 0
    i = math.isqrt(q)
    assert i * i == q
    return i


def check_one(Rexpr):
    R = sp.Poly(Rexpr, y, domain=sp.ZZ)
    Q = reciprocal_from_trace(R)
    assert R.is_irreducible and Q.is_irreducible

    _, dF = round_two(R)
    _, dL = round_two(Q)
    dF, dL = int(dF), int(dL)
    IF = square_index(R, dF, y)
    IL = square_index(Q, dL, x)

    endpoint = abs(int(Q.eval(1) * Q.eval(-1)))
    # Tower formula determines the norm of the relative field discriminant.
    den = abs(dF) ** 2
    assert abs(dL) % den == 0
    Nrel = abs(dL) // den

    assert Nrel * IL * IL == endpoint * (IF ** 4)
    assert endpoint % Nrel == 0
    quotient = endpoint // Nrel
    root = math.isqrt(quotient)
    assert root * root == quotient
    assert IL % (IF * IF) == 0
    assert root == IL // (IF * IF)
    return (R.as_expr(), Q.as_expr(), dF, dL, IF, IL, endpoint, Nrel, quotient)


def main():
    samples = [
        y**2 - y - 1,
        y**2 - 4*y - 4,
        y**2 - 2*y - 4,
        y**2 - 3*y - 2,
        y**2 - 4*y - 1,
        y**2 - 3*y - 1,
        y**3 - y - 1,
        y**3 - 3*y + 1,
        y**4 - y**3 - y**2 - y + 1,
        y**5 + y**4 - 5*y**3 - 5*y**2 + 4*y + 3,
    ]
    rows = [check_one(r) for r in samples]
    print('PASS')
    print('exact integral-basis samples:', len(rows))
    for row in rows:
        Rexpr, Qexpr, dF, dL, IF, IL, endpoint, Nrel, quotient = row
        print('R=', Rexpr, 'IF=', IF, 'IL=', IL,
              'endpoint=', endpoint, 'Nrel=', Nrel, 'square quotient=', quotient)


if __name__ == '__main__':
    main()
