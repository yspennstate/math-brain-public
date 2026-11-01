#!/usr/bin/env python3
"""Exact verifier for HARD8-07 frame-collapse identities.

Uses only Python standard-library integer/Fraction arithmetic.
No floating point is used in any asserted identity.
"""
from fractions import Fraction
from random import Random


def convergents(partials):
    """Return [(p_j,q_j)] for a finite simple continued-fraction prefix."""
    pm2, pm1 = 0, 1
    qm2, qm1 = 1, 0
    out = []
    for a in partials:
        p = a * pm1 + pm2
        q = a * qm1 + qm2
        out.append((p, q))
        pm2, pm1 = pm1, p
        qm2, qm1 = qm1, q
    return out


def det2(u, v):
    return u[0] * v[1] - v[0] * u[1]


def coords_in_basis(w, u, v):
    """Integer coordinates X,Y with w=Xu+Yv when det(u,v)=+-1."""
    d = det2(u, v)
    assert abs(d) == 1
    X = (w[0] * v[1] - v[0] * w[1]) // d
    Y = (u[0] * w[1] - w[0] * u[1]) // d
    assert (X * u[0] + Y * v[0], X * u[1] + Y * v[1]) == w
    return X, Y


def alpha_from_frame(c_m, c_m1, theta):
    pm, qm = c_m
    p1, q1 = c_m1
    return Fraction(p1 * theta + pm, q1 * theta + qm)


def inverse_coords(P, Q, c_m, c_m1):
    pm, qm = c_m
    p1, q1 = c_m1
    eps = pm * q1 - p1 * qm
    assert abs(eps) == 1
    x = (q1 * P - p1 * Q) // eps
    y = (-qm * P + pm * Q) // eps
    assert x * pm + y * p1 == P
    assert x * qm + y * q1 == Q
    return x, y, eps


def det3(M):
    (a, b, c), (d, e, f), (g, h, i) = M
    return a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)


def verify_frame_identities(rng, trials=500):
    for _ in range(trials):
        pa = [rng.randint(1, 7) for _ in range(rng.randint(5, 10))]
        pb = [rng.randint(1, 7) for _ in range(rng.randint(5, 10))]
        ca = convergents(pa)
        cb = convergents(pb)
        m = rng.randint(1, len(ca) - 2)
        n = rng.randint(1, len(cb) - 2)
        cm, cm1 = ca[m], ca[m + 1]
        dn, dn1 = cb[n], cb[n + 1]

        # Rational complete quotients > 1, sufficient for exact algebraic checks.
        theta = Fraction(rng.randint(3, 20), rng.randint(1, 2))
        eta = Fraction(rng.randint(3, 20), rng.randint(1, 2))
        if theta <= 1:
            theta += 2
        if eta <= 1:
            eta += 2

        alpha = alpha_from_frame(cm, cm1, theta)
        beta = alpha_from_frame(dn, dn1, eta)
        Dalpha = cm1[1] * theta + cm[1]
        Dbeta = dn1[1] * eta + dn[1]

        P = rng.randint(-100, 100)
        R = rng.randint(-100, 100)
        Q = rng.randint(-100, 100)

        x, y, epsm = inverse_coords(P, Q, cm, cm1)
        z, v, epsn = inverse_coords(R, Q, dn, dn1)

        assert x * cm[1] + y * cm1[1] == Q
        assert z * dn[1] + v * dn1[1] == Q

        Ea = Q * alpha - P
        Eb = Q * beta - R

        # Exact forward tail formulas.
        assert Ea == epsm * (y - x * theta) / Dalpha
        assert Eb == epsn * (v - z * eta) / Dbeta

        # Exact inverse formulas.
        assert x == Q / Dalpha - epsm * cm1[1] * Ea
        assert y == theta * Q / Dalpha + epsm * cm[1] * Ea
        assert z == Q / Dbeta - epsn * dn1[1] * Eb
        assert v == eta * Q / Dbeta + epsn * dn[1] * Eb

        # Fixed Littlewood lattice map determinant = +1.
        T = [
            [Fraction(0), Fraction(0), Fraction(1)],
            [Fraction(-1), Fraction(0), alpha],
            [Fraction(0), Fraction(-1), beta],
        ]
        assert det3(T) == 1

        # Scaling E_alpha,E_beta to unnormalized tail coordinates A,B
        # multiplies covolume by Dalpha*Dbeta.
        S = [
            [Fraction(0), Fraction(0), Fraction(1)],
            [-epsm * Dalpha, Fraction(0), epsm * Dalpha * alpha],
            [Fraction(0), -epsn * Dbeta, epsn * Dbeta * beta],
        ]
        assert abs(det3(S)) == Dalpha * Dbeta


def verify_block_collapse(rng, trials=500):
    for _ in range(trials):
        partials = [rng.randint(1, 6) for _ in range(rng.randint(8, 16))]
        cs = convergents(partials)
        m = rng.randint(1, len(cs) - 3)
        u, v = cs[m], cs[m + 1]
        lo = rng.randint(0, m)
        hi = rng.randint(m + 1, len(cs) - 1)
        xis = {j: rng.randint(-5, 5) for j in range(lo, hi + 1)}

        P = sum(xis[j] * cs[j][0] for j in xis)
        Q = sum(xis[j] * cs[j][1] for j in xis)

        X = 0
        Y = 0
        for j, coeff in xis.items():
            A, B = coords_in_basis(cs[j], u, v)
            X += coeff * A
            Y += coeff * B

        assert X * u[0] + Y * v[0] == P
        assert X * u[1] + Y * v[1] == Q


def fibs(n):
    F = [0, 1]
    for _ in range(2, n + 1):
        F.append(F[-1] + F[-2])
    return F


def verify_fibonacci_amplification(max_k=30):
    # Recurrence-only vector sequence c_{j+1}=c_j+c_{j-1} with unimodular seed.
    c0 = (1, 0)
    c1 = (0, 1)
    cs = [c0, c1]
    for _ in range(2, max_k + 8):
        a, b = cs[-2], cs[-1]
        cs.append((a[0] + b[0], a[1] + b[1]))
    F = fibs(max_k + 2)
    m = 4
    u, v = cs[m], cs[m + 1]
    for k in range(1, max_k + 1):
        w = cs[m + k]
        rhs = (
            F[k - 1] * u[0] + F[k] * v[0],
            F[k - 1] * u[1] + F[k] * v[1],
        )
        assert w == rhs
        X, Y = coords_in_basis(w, u, v)
        assert (X, Y) == (F[k - 1], F[k])


def main():
    rng = Random(20260916074341)
    verify_frame_identities(rng, 500)
    verify_block_collapse(rng, 500)
    verify_fibonacci_amplification(30)
    print("VERIFIED: 500 exact frame/covolume trials")
    print("VERIFIED: 500 exact finite-block collapse trials")
    print("VERIFIED: Fibonacci effective-coordinate identity through k=30")
    print("All asserted checks use integer/Fraction arithmetic only.")


if __name__ == "__main__":
    main()
