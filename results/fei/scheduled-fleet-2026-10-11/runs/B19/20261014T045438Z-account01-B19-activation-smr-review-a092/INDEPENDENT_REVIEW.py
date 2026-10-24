#!/usr/bin/env python3
"""Independent A092 reconstruction of the B05 fair-activation falsifier.

This implementation does not import or call the author checker.  Walsh
coefficients are computed as raw integer character sums.  Every logarithmic
base is prime-factorized; after clearing rational coefficient denominators,
the sign certificate is a comparison of two products of primes.
"""

from fractions import Fraction
from math import gcd, log2

QMASK = 56242


def lcm(a, b):
    return a // gcd(a, b) * b


def raw_walsh(f):
    n = len(f).bit_length() - 1
    return [sum(v * (-1 if (s & x).bit_count() & 1 else 1)
                for x, v in enumerate(f))
            for s in range(1 << n)]


def spectral_law(f):
    n = len(f).bit_length() - 1
    den = 1 << (2*n)
    return [Fraction(w*w, den) for w in raw_walsh(f)]


def upper_caps(p):
    n = len(p).bit_length() - 1
    return [sum(p[t] for t in range(1 << n) if t & s == s)
            for s in range(1 << n)]


def factor_integer(v):
    assert v >= 1
    out = {}
    d = 2
    while d*d <= v:
        while v % d == 0:
            out[d] = out.get(d, 0) + 1
            v //= d
        d += 1 if d == 2 else 2
    if v > 1:
        out[v] = out.get(v, 0) + 1
    return out


def add_log(out, coeff, base):
    if coeff == 0 or base == 1:
        return
    for prime, exponent in factor_integer(base.numerator).items():
        out[prime] = out.get(prime, Fraction(0)) + coeff*exponent
    for prime, exponent in factor_integer(base.denominator).items():
        out[prime] = out.get(prime, Fraction(0)) - coeff*exponent


def add_expr(out, src, scale=Fraction(1)):
    for prime, coeff in src.items():
        out[prime] = out.get(prime, Fraction(0)) + scale*coeff
        if out[prime] == 0:
            del out[prime]


def entropy_pair(expr, a, b):
    if a:
        add_log(expr, a, (a+b)/a)
    if b:
        add_log(expr, b, (a+b)/b)


def UB_I(f):
    p = spectral_law(f)
    cap = upper_caps(p)
    n = len(f).bit_length() - 1
    u = {}
    for a, c in zip(p, cap):
        if a:
            add_log(u, a, c/a)
    b = {}
    for i in range(n):
        bit = 1 << i
        for s in range(1 << n):
            if not s & bit:
                entropy_pair(b, p[s], p[s | bit])
    influence = sum(a*s.bit_count() for s, a in enumerate(p))
    return u, b, influence, p


def restrict_truth(f, i, bit):
    n = len(f).bit_length() - 1
    answer = []
    for y in range(1 << (n-1)):
        lower = y & ((1 << i)-1)
        upper = y >> i
        x = lower | (bit << i) | (upper << (i+1))
        answer.append(f[x])
    return tuple(answer)


def residual(f):
    n = len(f).bit_length() - 1
    u, b, influence, p = UB_I(f)
    expr = {}
    # L = G-B+5U/4-2I, G=nU-(1/2)sum U(restriction).
    add_expr(expr, u, Fraction(4*n+5, 4))
    for i in range(n):
        for bit in (0, 1):
            ur, _, _, _ = UB_I(restrict_truth(f, i, bit))
            add_expr(expr, ur, Fraction(-1, 2))
    add_expr(expr, b, Fraction(-1))
    add_log(expr, -2*influence, Fraction(2))
    return expr, influence, u, b, p


def exact_sign(expr):
    den = 1
    for c in expr.values():
        den = lcm(den, c.denominator)
    exponents = {p: c.numerator*(den//c.denominator)
                 for p, c in expr.items() if c}
    left = right = 1
    for p, e in exponents.items():
        if e > 0:
            left *= p**e
        elif e < 0:
            right *= p**(-e)
    return den, exponents, (left > right)-(left < right), left, right


def eval_expr(expr):
    return sum(float(c)*log2(p) for p, c in expr.items())


def eval_UBGI(f):
    n = len(f).bit_length()-1
    u, b, influence, _ = UB_I(f)
    U = eval_expr(u)
    B = eval_expr(b)
    G = n*U
    for i in range(n):
        for bit in (0, 1):
            ur, _, _, _ = UB_I(restrict_truth(f, i, bit))
            G -= eval_expr(ur)/2
    M = G-B
    L = M+1.25*U-2*float(influence)
    return U, influence, B, G, M, L


q = tuple(1 if QMASK >> j & 1 else -1 for j in range(16))
F = tuple(1 if x & 1 else q[x >> 1] for x in range(32))

q_walsh = raw_walsh(q)
assert all(abs(w) == 4 for w in q_walsh)
q_expr, qI, _, _, qp = residual(q)
F_expr, FI, _, _, Fp = residual(F)
q_cert = exact_sign(q_expr)
F_cert = exact_sign(F_expr)

# Independent spectral-shape check from the activation formula.
assert Fp[0] == Fraction(25, 64)
assert Fp[1] == Fraction(9, 64)
assert sum(a == Fraction(1, 64) for a in Fp) == 30
assert sum(Fp) == 1

q_stats = eval_UBGI(q)
F_stats = eval_UBGI(F)
GU_slack = 4*float(FI) + 0.75*F_stats[0] - F_stats[3]
c_lower = (F_stats[4] + 1.25*F_stats[0])/float(FI)

print(f"q_mask={QMASK}")
print(f"q_truth={''.join('+' if v == 1 else '-' for v in q)}")
print(f"F_truth={''.join('+' if v == 1 else '-' for v in F)}")
print(f"q_raw_walsh={q_walsh}")
print(f"q_stats_U_I_B_G_M_L={q_stats}")
print(f"F_stats_U_I_B_G_M_L={F_stats}")
print(f"F_spectrum_shape=25/64,9/64,30x1/64")
print(f"q_exact_sign={q_cert[2]} q_prime_exponents={q_cert[1]}")
print(f"F_coefficient_denominator={F_cert[0]}")
print(f"F_prime_exponents={dict(sorted(F_cert[1].items()))}")
print(f"F_exact_sign={F_cert[2]}")
print(f"F_product_bits={F_cert[3].bit_length()},{F_cert[4].bit_length()}")
print(f"GU_4_3over4_slack={GU_slack:.15f}")
print(f"forced_c_at_eta_quarter={c_lower:.15f}")

assert q_cert[2] == 0
assert F_cert[2] == 1
assert FI == Fraction(11, 8)
assert F_stats[-1] > 0.09
assert GU_slack > 2.99
print("PASS")
