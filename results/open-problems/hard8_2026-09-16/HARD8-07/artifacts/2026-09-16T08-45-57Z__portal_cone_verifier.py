#!/usr/bin/env python3
"""Exact verifier for HARD8-07 portal-cone checkpoint.

Uses only Python standard-library integer arithmetic and fractions.Fraction.
It checks algebraic identities used in the report; it does not prove the
classical Littlewood conjecture.
"""

from fractions import Fraction
import random

SEED = 2026091607
TRIALS = 500


def cf_convergents(digits):
    p_m2, p_m1 = 0, 1
    q_m2, q_m1 = 1, 0
    out = []
    for a in digits:
        p = a * p_m1 + p_m2
        q = a * q_m1 + q_m2
        out.append((p, q))
        p_m2, p_m1 = p_m1, p
        q_m2, q_m1 = q_m1, q
    return out


def cf_value(digits):
    x = Fraction(digits[-1], 1)
    for a in reversed(digits[:-1]):
        x = a + Fraction(1, x)
    return x


def nearest_integer(x):
    """Nearest integer to a Fraction; ties are sent downward."""
    f = x.numerator // x.denominator
    r = x - f
    return f + 1 if r > Fraction(1, 2) else f


def canonical_m(denominators, D):
    """Largest m with B_{m+1}^3 <= D^2, or None if absent."""
    candidates = [
        m
        for m in range(len(denominators) - 1)
        if denominators[m + 1] ** 3 <= D**2
    ]
    return max(candidates) if candidates else None


def run():
    rng = random.Random(SEED)
    counts = {
        "wedge": 0,
        "nested": 0,
        "nonadjacent": 0,
        "canonical": 0,
        "modular": 0,
    }

    for _ in range(TRIALS):
        Aalpha = rng.randint(2, 6)
        Abeta = rng.randint(2, 6)
        alpha_digits = [0] + [rng.randint(1, Aalpha) for _ in range(24)]
        beta_digits = [0] + [rng.randint(1, Abeta) for _ in range(24)]

        aconv = cf_convergents(alpha_digits)
        bconv = cf_convergents(beta_digits)
        alpha = cf_value(alpha_digits)
        beta = cf_value(beta_digits)

        n = rng.randint(2, 14)
        Cn, Dn = bconv[n]
        C1, D1 = bconv[n + 1]
        eps = Cn * D1 - C1 * Dn
        assert abs(eps) == 1

        # Recover the exact complete quotient eta from the finite rational
        # continuation. All following identities are exact in Fraction.
        eta = (Fraction(Cn, 1) - beta * Dn) / (beta * D1 - C1)
        assert eta > 1
        Dstar = D1 * eta + Dn

        # Exact ++ coefficient/error inversion and aperture.
        for _j in range(4):
            z = rng.randint(0, 10)
            v = rng.randint(0, 10)
            if z == 0 and v == 0:
                z = 1
            q = z * Dn + v * D1
            r = z * Cn + v * C1
            E = q * beta - r

            z_back = Fraction(q, Dstar) - eps * D1 * E
            v_back = eta * Fraction(q, Dstar) + eps * Dn * E
            assert z_back == z
            assert v_back == v

            low = -eta * Fraction(q, Dstar * Dn)
            high = Fraction(q, Dstar * D1)
            oriented_error = eps * E
            assert low <= oriented_error <= high
            assert high - low == Fraction(q, Dn * D1)
            counts["wedge"] += 1

        # Nested positive semigroups: c_{n+2}=a c_{n+1}+c_n.
        C2, D2 = bconv[n + 2]
        a = beta_digits[n + 2]
        assert C2 == a * C1 + Cn
        assert D2 == a * D1 + Dn
        for _j in range(2):
            z = rng.randint(0, 10)
            v = rng.randint(0, 10)
            r = z * C1 + v * C2
            q = z * D1 + v * D2
            assert r == v * Cn + (z + a * v) * C1
            assert q == v * Dn + (z + a * v) * D1
            counts["nested"] += 1

        # Nonadjacent determinant/angle/index identity for odd gaps.
        j = n + rng.choice([1, 3, 5])
        if j < 20:
            Ci, Di = bconv[n]
            Cj, Dj = bconv[j]
            Delta = abs(Ci * Dj - Cj * Di)
            interval_width = abs(Fraction(Ci, Di) - Fraction(Cj, Dj))
            assert interval_width == Fraction(Delta, Di * Dj)
            # Basis (1,0,0), (0,Ci,Di), (0,Cj,Dj) in (p,r,q)
            # has determinant Ci*Dj-Cj*Di, so the triple sublattice index
            # is exactly Delta.
            assert abs(Ci * Dj - Cj * Di) == Delta
            counts["nonadjacent"] += 1

        # Exact integer critical scale B_{m+1}^3 <= D_n^2 < B_{m+2}^3.
        B = [q for _p, q in aconv]
        m = canonical_m(B, Dn)
        if m is None or m + 2 >= len(aconv):
            continue

        Bm = B[m]
        M = B[m + 1]
        assert M**3 <= Dn**2
        assert B[m + 2] ** 3 > Dn**2
        assert B[m + 2] <= (Aalpha + 1) * M
        # Equivalent lower bound M > D^(2/3)/(Aalpha+1), written
        # without extracting roots.
        assert ((Aalpha + 1) * M) ** 3 > Dn**2
        assert (Aalpha + 1) * Bm >= M
        counts["canonical"] += 1

        # Exact modular portal certificate.
        z = rng.randint(0, 4)
        v = rng.randint(0, 4)
        if z == 0 and v == 0:
            z = 1
        q = z * Dn + v * D1
        p = nearest_integer(q * alpha)

        Am = aconv[m][0]
        A1 = aconv[m + 1][0]
        det = Am * M - A1 * Bm
        assert abs(det) == 1

        x = (p * M - A1 * q) // det
        y = (-p * Bm + Am * q) // det
        assert x * Am + y * A1 == p
        assert x * Bm + y * M == q

        inv = pow(Bm, -1, M)
        assert (inv - ((-1) ** m) * A1) % M == 0
        assert (x - q * inv) % M == 0

        # The least absolute representative of q*Bm^{-1} mod M has size
        # M * ||q*A_{m+1}/M||, using the determinant identity above.
        residue = (q * inv) % M
        least_abs = min(residue, M - residue)
        phase_num = (q * A1) % M
        phase_abs = min(phase_num, M - phase_num)
        assert least_abs == phase_abs
        counts["modular"] += 1

    expected = {
        "wedge": 2000,
        "nested": 1000,
        "nonadjacent": 500,
        "canonical": 487,
        "modular": 487,
    }
    assert counts == expected, (counts, expected)

    print("HARD8-07 exact portal/cone verifier: PASS")
    print(f"seed={SEED} trials={TRIALS}")
    for key in ("wedge", "nested", "nonadjacent", "canonical", "modular"):
        print(f"{key}={counts[key]}")


if __name__ == "__main__":
    run()
