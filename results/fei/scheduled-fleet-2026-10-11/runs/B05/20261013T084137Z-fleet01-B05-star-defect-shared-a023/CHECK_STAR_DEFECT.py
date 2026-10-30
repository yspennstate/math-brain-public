#!/usr/bin/env python3
"""Exact/interval certificate for the shared star--point-defect theorem."""

from fractions import Fraction as F
from math import comb


def ln_interval(x, terms=120):
    assert x > 0
    if x == 1:
        return F(0), F(0)
    n, d = x.numerator, x.denominator
    e = n.bit_length() - d.bit_length()
    if e >= 0:
        y = x / (1 << e)
    else:
        y = x * (1 << (-e))
    while y < 1:
        e -= 1
        y *= 2
    while y >= 2:
        e += 1
        y /= 2
    z = (y - 1) / (y + 1)

    def atanh_bounds(w):
        s = F(0)
        power = w
        for k in range(terms):
            s += power / (2 * k + 1)
            power *= w * w
        lo = 2 * s
        rem = 2 * power / ((2 * terms + 1) * (1 - w * w))
        return lo, lo + rem

    ly0, ly1 = atanh_bounds(z)
    l20, l21 = atanh_bounds(F(1, 3))
    # All calls below have x >= 1, hence e >= 0.
    assert e >= 0
    return e * l20 + ly0, e * l21 + ly1


def log2_interval(x):
    if x == 1:
        return F(0), F(0)
    lx0, lx1 = ln_interval(x)
    l20, l21 = ln_interval(F(2))
    return lx0 / l21, lx1 / l20


def phi_interval(p, q):
    if not p:
        return F(0), F(0)
    assert q >= p > 0
    lo, hi = log2_interval(q / p)
    return p * lo, p * hi


def add_iv(a, b):
    return a[0] + b[0], a[1] + b[1]


def scale_iv(c, a):
    assert c >= 0
    return c * a[0], c * a[1]


def fwht_int(values):
    a = list(values)
    h = 1
    while h < len(a):
        for i in range(0, len(a), 2 * h):
            for j in range(i, i + h):
                x, y = a[j], a[j + h]
                a[j], a[j + h] = x + y, x - y
        h *= 2
    return a


def spectral_law(values):
    n = len(values)
    return [F(z * z, n * n) for z in fwht_int(values)]


def upper_masses(p):
    q = list(p)
    n = len(p).bit_length() - 1
    for i in range(n):
        bit = 1 << i
        for s in range(len(q)):
            if not (s & bit):
                q[s] += q[s | bit]
    return q


def U_from_law(p):
    pi = upper_masses(p)
    out = (F(0), F(0))
    for x, y in zip(p, pi):
        out = add_iv(out, phi_interval(x, y))
    return out


def star_values(m, r, eps):
    n = 1 << m
    R = (1 << r) - 1
    g = [-1] + [1] * (n - 1)
    out = []
    for x in (0, 1):
        for y in range(n):
            exponent = x * (eps ^ ((y & R).bit_count() & 1))
            out.append((-1 if exponent else 1) * g[y])
    child = [(-1 if (eps ^ ((y & R).bit_count() & 1)) else 1) * g[y]
             for y in range(n)]
    return g, child, out


def formula_intervals(m, r, eps):
    delta = F(1, 1 << m)
    t = 4 * delta * delta
    A = (1 - 4 * delta) ** 2 / 4
    a = (1 - 2 * delta) ** 2

    def B(s):
        return A + F(1, 4) + t * ((1 << (m - s)) - 1)

    def C(s):
        return A + t * ((1 << (m - s)) - 1)

    def D(s):
        return a + t * ((1 << (m - s)) - 1)

    # Unshifted point defect.
    Ug = phi_interval(a, F(1))
    Ug = add_iv(Ug, (t * (m * (1 << (m - 1)) - m),) * 2)

    # Character-shifted point defect.
    Uh = phi_interval(a, D(r))
    for s in range(r):
        Uh = add_iv(Uh, scale_iv(comb(r, s), phi_interval(t, D(s))))
    for s in range(1, m + 1):
        outside = comb(m, s) - (comb(r, s) if s <= r else 0)
        Uh = add_iv(Uh, (F(outside) * t * (m - s),) * 2)

    tail = (F(0), F(0))
    for s in range(1, m + 1):
        outside = comb(m, s) - (comb(r, s) if s <= r else 0)
        tail = add_iv(tail, (F(outside) * t * (m - s),) * 2)

    if eps == 0:
        U = phi_interval(A, F(1))
        U = add_iv(U, phi_interval(A, B(r)))
        U = add_iv(U, (F(1, 4), F(1, 4)))
        for s in range(1, r):
            U = add_iv(U, scale_iv(comb(r, s), phi_interval(t, B(s))))
        U = add_iv(U, tail)
    else:
        U = (F(1, 2), F(1, 2))
        U = add_iv(U, phi_interval(F(1, 4), B(r)))
        U = add_iv(U, phi_interval(A, F(1, 2)))
        U = add_iv(U, phi_interval(A, C(r)))
        for s in range(1, r):
            U = add_iv(U, scale_iv(comb(r, s), phi_interval(t, C(s))))
        U = add_iv(U, tail)

    delta_u = U[0] - (Ug[1] + Uh[1]) / 2, U[1] - (Ug[0] + Uh[0]) / 2
    return Ug, Uh, U, delta_u


def expected_parent_law(m, r, eps):
    n = 1 << m
    delta = F(1, n)
    t = 4 * delta * delta
    A = (1 - 4 * delta) ** 2 / 4
    R = (1 << r) - 1
    p = [F(0)] * (2 * n)
    for s in range(n):
        broad = A if s in (0, R) else t
        special = F(1, 4) if s in (0, R) else F(0)
        if eps == 0:
            p[s], p[n | s] = broad, special
        else:
            p[s], p[n | s] = special, broad
    return p


def main():
    assertions = 0
    max_u = (F(-1), None)
    max_delta = (F(-1), None)
    direct_cases = 0
    for m in range(1, 10):
        for r in range(1, m + 1):
            for eps in (0, 1):
                Ug, Uh, U, dU = formula_intervals(m, r, eps)
                assert U[1] < 2
                assert dU[1] < F(5, 4)
                assertions += 2
                if U[1] > max_u[0]:
                    max_u = (U[1], (m, r, eps, U))
                if dU[1] > max_delta[0]:
                    max_delta = (dU[1], (m, r, eps, dU))
                g, child, parent = star_values(m, r, eps)
                p = spectral_law(parent)
                assert p == expected_parent_law(m, r, eps)
                assertions += len(p) + 1
                direct_U = U_from_law(p)
                direct_g = U_from_law(spectral_law(g))
                direct_h = U_from_law(spectral_law(child))
                for left, right in ((direct_U, U), (direct_g, Ug), (direct_h, Uh)):
                    assert max(left[0], right[0]) <= min(left[1], right[1])
                    assertions += 1
                direct_cases += 1

    # Analytic tail m >= 10. The report proves these rational envelopes.
    tail_mass = F(8 * (10 - 1), 1 << 10)
    A_min = F(255 * 255, 4 * 256 * 256)
    # Exact interval checks for the four numerical logarithmic envelopes used
    # in the analytic m >= 10 proof.
    assert log2_interval(F(81, 40))[1] < F(102, 100)
    assert log2_interval(F(257, 128))[1] < F(101, 100)
    assert log2_interval(F(1, 2) / A_min)[1] < F(102, 100)
    assert log2_interval(1 + F(1, 512) / A_min)[1] < F(12, 1000)
    assertions += 4
    eps0_envelope = F(1, 2) + F(255, 1000) + F(1, 4) + tail_mass
    eps1_envelope = F(1, 2) + F(253, 1000) + F(255, 1000) + F(3, 1000) + tail_mass
    assert eps0_envelope < F(5, 4)
    assert eps1_envelope < F(5, 4)
    assertions += 2

    print(f"finite_parameter_rows={2 * sum(range(1, 10))}")
    print(f"direct_walsh_rows={direct_cases}")
    print(f"assertions={assertions}")
    print(f"max_finite_U_upper={float(max_u[0]):.15f} at={max_u[1][:3]}")
    print(f"max_finite_DeltaU_upper={float(max_delta[0]):.15f} at={max_delta[1][:3]}")
    print(f"eps0_tail_envelope={float(eps0_envelope):.15f}")
    print(f"eps1_tail_envelope={float(eps1_envelope):.15f}")
    print("arithmetic=exact rational Walsh plus positive-series rational log intervals")
    print("RESULT=PASS")


if __name__ == "__main__":
    main()
