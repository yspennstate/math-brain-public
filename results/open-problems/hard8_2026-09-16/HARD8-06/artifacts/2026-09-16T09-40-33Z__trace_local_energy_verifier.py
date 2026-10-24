#!/usr/bin/env python3
"""Exact sanity checks for HARD8-06 trace-local p-adic energy checkpoint.

Checks use exact integer / symbolic arithmetic only.
They do not prove the global Lehmer conjecture; they independently test the
finite algebraic identities and the K=Q_p specialization of the local collision
inequality used in the report.
"""

from math import prod
import itertools
import sympy as sp

x, y = sp.symbols('x y')


def vp(n: int, p: int) -> int:
    n = abs(int(n))
    assert n != 0
    c = 0
    while n % p == 0:
        n //= p
        c += 1
    return c


def poly_from_roots(roots):
    f = sp.Poly(1, y, domain=sp.ZZ)
    for r in roots:
        f *= sp.Poly(y - int(r), y, domain=sp.ZZ)
    return f


def residue_collision_energy(roots, p):
    counts = [0] * p
    for r in roots:
        counts[r % p] += 1
    return sum(n * (n - 1) for n in counts), counts


def check_local_collision_integer_roots():
    checks = 0
    primes = [2, 3, 5, 7, 11, 13]
    # Deterministic, distinct integer root sets with many different collision patterns.
    for D in range(2, 13):
        families = []
        families.append(list(range(D)))
        families.append([j * j + 3 * j + 1 for j in range(D)])
        families.append([2 ** j + j for j in range(D)])
        families.append([17 * j + (j % 3) for j in range(D)])
        for roots in families:
            assert len(set(roots)) == D
            R = poly_from_roots(roots)
            disc = int(sp.discriminant(R.as_expr(), y))
            assert disc != 0
            for p in primes:
                coll, counts = residue_collision_energy(roots, p)
                val = vp(disc, p)
                # K=Q_p means e=1, q=p and s=D. The sharper occupancy count
                # is sum_a N_a(N_a-1).
                assert val >= coll
                # Cauchy lower bound, written without fractions.
                assert p * coll >= D * D - p * D
                checks += 1
    return checks


def reciprocal_from_trace(R):
    R = sp.Poly(R, y, domain=sp.ZZ)
    D = R.degree()
    Qexpr = sp.cancel(x**D * R.as_expr().subs(y, x + 1/x))
    Q = sp.Poly(sp.expand(Qexpr), x, domain=sp.ZZ)
    assert Q.degree() == 2 * D
    assert Q.LC() == 1
    assert Q.nth(0) == 1
    return Q


def check_endpoint_norm_and_discriminant():
    checks = 0
    samples = [
        y**2 - 3*y + 1,
        y**3 + y + 1,
        y**4 - 2*y**3 - y + 1,
        y**5 + y**4 - 5*y**3 - 5*y**2 + 4*y + 3,
        y**6 + 2*y**5 - y**3 + 3*y + 1,
    ]
    for expr in samples:
        R = sp.Poly(expr, y, domain=sp.ZZ)
        Q = reciprocal_from_trace(R)
        D = R.degree()
        # Norm(beta^2-4) = Res(R, y^2-4), and its absolute value equals
        # |R(2)R(-2)| = |Q(1)Q(-1)|.
        norm = int(sp.resultant(R.as_expr(), y*y - 4, y))
        endpoint = int(R.eval(2) * R.eval(-2))
        assert abs(norm) == abs(endpoint)
        assert abs(endpoint) == abs(int(Q.eval(1) * Q.eval(-1)))

        discR = int(sp.discriminant(R.as_expr(), y))
        discQ = int(sp.discriminant(Q.as_expr(), x))
        rhs = ((-1) ** D) * int(Q.eval(1) * Q.eval(-1)) * discR * discR
        assert discQ == rhs
        checks += 1
    return checks


def check_lehmer_benchmark():
    Q = sp.Poly(
        x**10 + x**9 - x**7 - x**6 - x**5 - x**4 - x**3 + x + 1,
        x, domain=sp.ZZ,
    )
    R = sp.Poly(y**5 + y**4 - 5*y**3 - 5*y**2 + 4*y + 3, y, domain=sp.ZZ)
    assert reciprocal_from_trace(R) == Q
    assert int(Q.eval(1)) == -1
    assert int(Q.eval(-1)) == 1
    assert int(sp.discriminant(R.as_expr(), y)) == 36497
    assert int(sp.discriminant(Q.as_expr(), x)) == 36497**2
    return 1


def main():
    a = check_local_collision_integer_roots()
    b = check_endpoint_norm_and_discriminant()
    c = check_lehmer_benchmark()
    print('PASS')
    print('local collision checks:', a)
    print('endpoint/norm/discriminant checks:', b)
    print('Lehmer benchmark checks:', c)


if __name__ == '__main__':
    main()
