#!/usr/bin/env python3
"""
Exact verifier for HARD8-06, 2026-09-16T07-29-49Z checkpoint.

Requires Python 3 + sympy. All checks use exact ZZ/QQ arithmetic.

Important convention:
    norm_resultant(f,g) = product_{f(alpha)=0} g(alpha)
for monic f. This avoids the harmless (-1)^(deg f deg g) sign convention
used by some resultant implementations.
"""

import itertools
import sympy as sp

x, y = sp.symbols("x y")

Q = x**10 + x**9 - x**7 - x**6 - x**5 - x**4 - x**3 + x + 1
R = y**5 + y**4 - 5*y**3 - 5*y**2 + 4*y + 3
D = sp.degree(R, y)


def C(n):
    if n == 0:
        return sp.Integer(2)
    if n == 1:
        return y
    a, b = sp.Integer(2), y
    for _ in range(1, n):
        a, b = b, sp.expand(y*b - a)
    return b


CS = [C(i) for i in range(40)]


def trace_transform(poly_R):
    d = sp.degree(poly_R, y)
    return sp.cancel(x**d * poly_R.subs(y, x + x**-1)).expand()


assert trace_transform(R) == Q


def norm_resultant_monic(f, g, var):
    """For monic f, return product g(alpha) over the roots alpha of f."""
    fP = sp.Poly(f, var, domain=sp.QQ)
    assert fP.LC() == 1
    n = fP.degree()
    cols = []
    for j in range(n):
        rem = sp.rem(
            sp.Poly(sp.expand(g * var**j), var, domain=sp.QQ),
            fP,
        ).as_expr()
        P = sp.Poly(rem, var, domain=sp.QQ)
        cols.append(sp.Matrix([P.nth(i) for i in range(n)]))
    M = sp.Matrix.hstack(*cols)
    val = sp.factor(M.det())
    assert val.q == 1
    return int(val)


def remainder_key(poly):
    rem = sp.rem(
        sp.Poly(poly, y, domain=sp.ZZ),
        sp.Poly(R, y, domain=sp.ZZ),
    ).as_expr()
    P = sp.Poly(rem, y, domain=sp.ZZ)
    return tuple(int(P.nth(i)) for i in range(D))


def first_binary_collision(max_m=12):
    for m in range(max_m + 1):
        seen = {}
        for eps in itertools.product((0, 1), repeat=m+1):
            poly = sum(eps[j]*CS[j] for j in range(m+1))
            key = remainder_key(poly)
            if key in seen:
                return m, seen[key], eps
            seen[key] = eps
    return None


m_first, eps1, eps2 = first_binary_collision()
assert m_first == 6
assert sp.expand(CS[6] - CS[5] - CS[4] + CS[2] - (y-2)*R) == 0


def exceptional_data(m):
    primes = set()
    max_abs = 0
    count = 0
    for c in itertools.product((-1, 0, 1), repeat=m+1):
        if all(v == 0 for v in c):
            continue
        B = sp.expand(sum(c[j]*CS[j] for j in range(m+1)))
        res = norm_resultant_monic(R, B, y)
        assert res != 0
        count += 1
        max_abs = max(max_abs, abs(res))
        primes.update(sp.factorint(abs(res)).keys())
    return count, sorted(primes), max_abs


expected = {
    0: ([2], 32),
    1: ([2, 3], 32),
    2: ([2, 3, 13, 157], 157),
    3: ([2, 3, 5, 13, 23, 29, 31, 79, 109, 157, 163, 349], 471),
    4: ([2, 3, 5, 7, 13, 23, 29, 31, 37, 47, 53, 59, 67, 79, 103, 109,
         157, 163, 173, 193, 241, 311, 349, 463, 769, 821], 821),
}

for m in range(5):
    count, primes, max_abs = exceptional_data(m)
    assert count == 3**(m+1)-1
    assert primes == expected[m][0]
    assert max_abs == expected[m][1]


def frobenius_check(p):
    cp = CS[p]

    delta = sp.Poly(sp.expand(cp - y**p), y, domain=sp.ZZ)
    assert all(int(c) % p == 0 for c in delta.all_coeffs())

    numer = sp.expand(R.subs(y, cp) - R**p)
    Pnumer = sp.Poly(numer, y, domain=sp.ZZ)
    assert all(int(c) % p == 0 for c in Pnumer.all_coeffs())
    A = Pnumer.exquo_ground(p).as_expr()

    res_trace = norm_resultant_monic(R, sp.expand(R.subs(y, cp)), y)
    res_aux = norm_resultant_monic(R, A, y)
    assert res_trace == (p**D) * res_aux
    assert res_trace != 0

    res_original = norm_resultant_monic(Q, sp.expand(Q.subs(x, x**p)), x)
    assert res_original == res_trace**2

    vp = sp.factorint(abs(res_trace)).get(p, 0)
    return res_trace, res_aux, vp


expected_aux = {2: 1, 3: 1, 5: -3, 7: -3, 11: 9, 13: 9}
rows = []
for p in (2, 3, 5, 7, 11, 13):
    rt, ra, vp = frobenius_check(p)
    assert ra == expected_aux[p]
    assert vp == D
    rows.append((p, vp, ra, abs(ra)))

print("R_L(y) =", R)
print("First binary trace collision depth:", m_first)
print("Collision witnesses:", eps1, eps2)
print("Verified C6-C5-C4+C2=(y-2)R_L")
for m in range(5):
    count, primes, max_abs = exceptional_data(m)
    print(f"m={m}: vectors={count}; exceptional={primes}; maxabs={max_abs}")
print("Frobenius rows (p, v_p, signed norm quotient, absolute quotient):")
for row in rows:
    print(row)
print("ALL EXACT CHECKS PASSED")
