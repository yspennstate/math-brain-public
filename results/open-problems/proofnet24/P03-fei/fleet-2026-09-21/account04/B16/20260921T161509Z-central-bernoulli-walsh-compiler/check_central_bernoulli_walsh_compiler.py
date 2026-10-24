#!/usr/bin/env python3
"""Exact checks for the B16 central Bernoulli/Walsh compiler identities.

The checks use only fractions and finite F_2 arithmetic. They are falsification
evidence for the algebraic statements in REPORT.md; they do not claim full FEI.
"""
from fractions import Fraction
from itertools import product
import json
import random


def bern_expect(phi, m, p):
    out = Fraction(0)
    for S in range(1 << m):
        k = S.bit_count()
        out += (p ** k) * ((1 - p) ** (m - k)) * phi[S]
    return out


def phi_from_coeff(coeff, m):
    return {
        S: sum(
            c * (-1 if ((S & R).bit_count() & 1) else 1)
            for R, c in coeff.items()
        )
        for S in range(1 << m)
    }


def delta1_expect(phi, m, p, v):
    bits = [j for j in range(m) if j != v]
    out = Fraction(0)
    for raw in range(1 << len(bits)):
        S = 0
        prob = Fraction(1)
        for h, j in enumerate(bits):
            if (raw >> h) & 1:
                S |= 1 << j
                prob *= p
            else:
                prob *= 1 - p
        out += prob * (phi[S] - phi[S | (1 << v)])
    return out


def delta2_expect(phi, m, p, u, v):
    bits = [j for j in range(m) if j not in (u, v)]
    out = Fraction(0)
    for raw in range(1 << len(bits)):
        S = 0
        prob = Fraction(1)
        for h, j in enumerate(bits):
            if (raw >> h) & 1:
                S |= 1 << j
                prob *= p
            else:
                prob *= 1 - p
        val = (
            phi[S]
            - phi[S | (1 << u)]
            - phi[S | (1 << v)]
            + phi[S | (1 << u) | (1 << v)]
        )
        out += prob * val
    return out


def direct_P(coeff, t):
    return sum(c * (t ** R.bit_count()) for R, c in coeff.items())


def direct_odd(coeff, t):
    return sum(
        c * (t ** R.bit_count())
        for R, c in coeff.items()
        if R.bit_count() & 1
    )


def direct_m(coeff, v, t):
    return sum(
        c * (t ** (R.bit_count() - 1))
        for R, c in coeff.items()
        if ((R >> v) & 1) and (R.bit_count() & 1)
    )


def direct_mprime(coeff, v, t):
    return sum(
        c * (R.bit_count() - 1) * (t ** (R.bit_count() - 2))
        for R, c in coeff.items()
        if ((R >> v) & 1) and (R.bit_count() >= 3) and (R.bit_count() & 1)
    )


def xor_zero(mask, n):
    x = 0
    for a in range(1 << n):
        if (mask >> a) & 1:
            x ^= a
    return x == 0


def in_c0(mask, n):
    return (mask.bit_count() % 2 == 0) and xor_zero(mask, n)


def affine_words(n):
    N = 1 << n
    out = []
    for a in range(1 << n):
        for b in (0, 1):
            w = 0
            for x in range(N):
                bit = ((a & x).bit_count() & 1) ^ b
                if bit:
                    w |= 1 << x
            out.append(w)
    return out


def affine_span_dim(delta, n):
    pts = [x for x in range(1 << n) if (delta >> x) & 1]
    if not pts:
        return -1
    x0 = pts[0]
    basis = [0] * n
    rank = 0
    for x in pts[1:]:
        w = x ^ x0
        while w:
            j = w.bit_length() - 1
            if basis[j]:
                w ^= basis[j]
            else:
                basis[j] = w
                rank += 1
                break
    return rank


def dot_parity(a, b):
    return (a & b).bit_count() & 1


def borel_coeff(A, N, s, c):
    q = A.bit_count()
    assert q % 2 == 0
    return (
        2
        * N
        * ((-1) ** (q // 2))
        * (s ** q)
        * (c ** (N - q))
    )


def all_corr_brute(delta, code, N, s, c):
    return sum(
        borel_coeff(A, N, s, c) * borel_coeff(A ^ delta, N, s, c)
        for A in code
    )


def all_corr_formula(delta, n, s, c):
    N = 1 << n
    m = delta.bit_count()
    C = c * c - s * s
    S = 2 * s * c
    if delta == 0:
        return 2 * N * (C ** N + 1 + (2 * N - 2) * (C ** (N // 2)))
    k = affine_span_dim(delta, n)
    multiplicity = (1 << (n - k)) - 1
    bracket = C ** (N - m)
    if multiplicity:
        bracket += multiplicity * (C ** (N // 2 - m))
    return 2 * N * ((-1) ** (m // 2)) * (S ** m) * bracket


def twist_corr_brute(delta, g, code, N, s, c):
    return sum(
        (-1 if dot_parity(g, A) else 1)
        * borel_coeff(A, N, s, c)
        * borel_coeff(A ^ delta, N, s, c)
        for A in code
    )


def twist_corr_formula(delta, g, n, s, c):
    N = 1 << n
    m = delta.bit_count()
    C = c * c - s * s
    S = 2 * s * c
    enumerator = Fraction(0)
    for r in affine_words(n):
        h = g ^ r
        if h & delta:
            continue
        zeros_off = sum(
            1
            for x in range(N)
            if not ((delta >> x) & 1) and not ((h >> x) & 1)
        )
        enumerator += C ** zeros_off
    return 2 * N * ((-1) ** (m // 2)) * (S ** m) * enumerator


def phase(A, g):
    return -1 if dot_parity(A, g) else 1


def frustrated_corr_brute(delta, g, code, N, s, c):
    return sum(
        borel_coeff(A, N, s, c) * borel_coeff(A ^ delta, N, s, c)
        for A in code
        if phase(A, g) == -1 and phase(A ^ delta, g) == -1
    )


def frustrated_corr_formula(delta, g, n, s, c):
    fdelta = phase(delta, g)
    return Fraction(1 + fdelta, 4) * (
        all_corr_formula(delta, n, s, c)
        - twist_corr_formula(delta, g, n, s, c)
    )


def main():
    rng = random.Random(20260921)

    bernoulli_checks = 0
    derivative_checks = 0
    for m in range(1, 7):
        for _ in range(20):
            coeff = {
                R: Fraction(rng.randint(-3, 3), rng.randint(1, 4))
                for R in range(1 << m)
            }
            phi = phi_from_coeff(coeff, m)
            for t in (
                Fraction(0),
                Fraction(1, 8),
                Fraction(1, 4),
                Fraction(1, 2),
            ):
                p_minus = (1 - t) / 2
                p_plus = (1 + t) / 2
                assert direct_P(coeff, t) == bern_expect(phi, m, p_minus)
                assert direct_odd(coeff, t) == (
                    bern_expect(phi, m, p_minus)
                    - bern_expect(phi, m, p_plus)
                ) / 2
                bernoulli_checks += 2

                for v in range(m):
                    assert direct_m(coeff, v, t) == (
                        delta1_expect(phi, m, p_minus, v)
                        + delta1_expect(phi, m, p_plus, v)
                    ) / 4
                    assert direct_mprime(coeff, v, t) == sum(
                        (
                            delta2_expect(phi, m, p_minus, u, v)
                            - delta2_expect(phi, m, p_plus, u, v)
                        )
                        for u in range(m)
                        if u != v
                    ) / 8
                    derivative_checks += 2

    multiplier_checks = 0
    max_scalar_weight = Fraction(0)
    max_relation_weight = Fraction(0)
    max_scalar_q = None
    max_relation_q = None
    for q in range(3, 32, 2):
        scalar_weight = Fraction(q - 1, (2 * q - 1) * (2 ** (2 * q)))
        relation_weight = q * scalar_weight
        if scalar_weight > max_scalar_weight:
            max_scalar_weight, max_scalar_q = scalar_weight, q
        if relation_weight > max_relation_weight:
            max_relation_weight, max_relation_q = relation_weight, q
        for j in range(17):
            t = Fraction(j, 32)
            assert (q - 1) * (t ** (q - 2)) <= 2 * t
            multiplier_checks += 1
    assert max_scalar_weight == Fraction(1, 160)
    assert max_scalar_q == 3
    assert max_relation_weight == Fraction(3, 160)
    assert max_relation_q == 3

    autocorr_checks = 0
    twisted_checks = 0
    frustrated_checks = 0
    trig_pairs = (
        (Fraction(3, 5), Fraction(4, 5)),
        (Fraction(5, 13), Fraction(12, 13)),
    )
    for n in (2, 3):
        N = 1 << n
        code = [A for A in range(1 << N) if in_c0(A, n)]
        gs = list(range(1 << N))
        for s, c in trig_pairs:
            for delta in code:
                assert all_corr_brute(delta, code, N, s, c) == all_corr_formula(
                    delta, n, s, c
                )
                autocorr_checks += 1
                for g in gs:
                    assert twist_corr_brute(
                        delta, g, code, N, s, c
                    ) == twist_corr_formula(delta, g, n, s, c)
                    assert frustrated_corr_brute(
                        delta, g, code, N, s, c
                    ) == frustrated_corr_formula(delta, g, n, s, c)
                    twisted_checks += 1
                    frustrated_checks += 1

    n = 4
    N = 1 << n
    code = [A for A in range(1 << N) if in_c0(A, n)]
    rng.shuffle(code)
    deltas = code[:24]
    gs = [rng.randrange(1 << N) for _ in range(24)]
    s, c = trig_pairs[0]
    for delta in deltas:
        assert all_corr_brute(delta, code, N, s, c) == all_corr_formula(
            delta, n, s, c
        )
        autocorr_checks += 1
        for g in gs:
            assert twist_corr_brute(
                delta, g, code, N, s, c
            ) == twist_corr_formula(delta, g, n, s, c)
            assert frustrated_corr_brute(
                delta, g, code, N, s, c
            ) == frustrated_corr_formula(delta, g, n, s, c)
            twisted_checks += 1
            frustrated_checks += 1

    out = {
        "status": "PASS",
        "bernoulli_transform_checks": bernoulli_checks,
        "first_second_difference_checks": derivative_checks,
        "radial_multiplier_grid_checks": multiplier_checks,
        "max_integrated_scalar_weight": str(max_scalar_weight),
        "max_integrated_scalar_weight_q": max_scalar_q,
        "max_integrated_relation_weight": str(max_relation_weight),
        "max_integrated_relation_weight_q": max_relation_q,
        "borel_autocorrelation_checks": autocorr_checks,
        "borel_twisted_autocorrelation_checks": twisted_checks,
        "borel_frustrated_pair_checks": frustrated_checks,
        "full_FEI_claimed": False,
        "execution_context": "WITHOUT_VERIFIED_BRAIN",
    }
    print(json.dumps(out, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
