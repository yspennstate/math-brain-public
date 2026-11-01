#!/usr/bin/env python3
from fractions import Fraction
from itertools import product
import json
import math

ODD_Q = (3, 5, 7, 9)

def hardy_coeff(q, a):
    return Fraction(q - 1, q) * Fraction(a)

def conditional_low_variance(a_by_q):
    # V_- = Var_{t uniform [0,1/2]} m(t), m(t)=sum_q a_q t^(q-1).
    qs = tuple(sorted(a_by_q))
    mean = sum(Fraction(a_by_q[q], q * 2 ** (q - 1)) for q in qs)
    e2 = sum(
        Fraction(a_by_q[q] * a_by_q[r], (q + r - 1) * 2 ** (q + r - 2))
        for q in qs for r in qs
    )
    return e2 - mean * mean

def gamma_by_collision_order(a_by_q):
    qs = tuple(sorted(a_by_q))
    u = {q: hardy_coeff(q, a_by_q[q]) for q in qs}
    gamma = {}
    for q in qs:
        for r in qs:
            gamma[q + r] = gamma.get(q + r, Fraction(0)) + u[q] * u[r]
    return gamma

def low_contribution_from_gamma(a_by_q):
    # This is (1/2) V_- in the law-of-total-variance split.
    gamma = gamma_by_collision_order(a_by_q)
    return sum(
        g * Fraction(1, (j - 1) * 2 ** (j - 1))
        for j, g in gamma.items()
    )

def radial_kernel(r, s, h):
    return Fraction(h) * (
        Fraction(1, r + s - 1) - Fraction(1, r * s)
    )

def main():
    exact_cases = 0
    cases_with_negative_gamma = 0
    q1_annihilation_cases = 0

    for vals in product(range(-2, 3), repeat=len(ODD_Q)):
        a = dict(zip(ODD_Q, vals))
        lhs = Fraction(1, 2) * conditional_low_variance(a)
        rhs = low_contribution_from_gamma(a)
        assert lhs == rhs
        gamma = gamma_by_collision_order(a)
        assert all(j % 2 == 0 for j in gamma)
        assert all(j >= 6 for j, g in gamma.items() if g != 0)
        if any(g < 0 for g in gamma.values()):
            cases_with_negative_gamma += 1
        exact_cases += 1

    # q=1 is a constant term of m and is killed by D(I+D)^(-1).
    for a1 in range(-3, 4):
        for a3 in range(-3, 4):
            a = {1: a1, 3: a3}
            gamma = gamma_by_collision_order(a)
            # all gamma involving q=1 are zero
            assert gamma.get(2, 0) == 0
            assert gamma.get(4, 0) == 0
            lhs = Fraction(1, 2) * conditional_low_variance(a)
            rhs = low_contribution_from_gamma(a)
            assert lhs == rhs
            q1_annihilation_cases += 1

    # Exact opposite-sign q=3 diagnostic from the B16 handoff:
    # two relations, each coefficient magnitude 1/8, overlap h=2.
    c = Fraction(1, 8)
    q = 3
    h = 2
    full_cross_refund = -2 * c * c * radial_kernel(q, q, h)
    # Low contribution = full radial pair contribution times 2^{-(q+q-1)}.
    low_cross_refund = full_cross_refund * Fraction(1, 2 ** (2 * q - 1))
    assert full_cross_refund == Fraction(-1, 180)
    assert low_cross_refund == Fraction(-1, 5760)

    # R16 positive-even envelope and the tail that can be touched by the
    # Hardy low-half demand.  q=1 is annihilated and the next odd q is 3,
    # hence collision order j starts at 6.
    def w(j):
        return Fraction(1, (j - 1) * 2 ** (j - 1))

    partial_80 = sum(Fraction(j) * w(j) for j in range(2, 82, 2))
    tail_partial_80 = sum(Fraction(j) * w(j) for j in range(6, 82, 2))
    kappa2 = Fraction(2, 3) + Fraction.from_float(math.atanh(0.5))
    kappa2_float = Fraction(2, 3).__float__() + math.atanh(0.5)
    tail_limit_float = math.atanh(0.5) - 0.5
    assert abs(float(partial_80) - kappa2_float) < 1e-14
    assert abs(float(tail_partial_80) - tail_limit_float) < 1e-14

    out = {
        "status": "PASS",
        "exact_signed_low_half_cases": exact_cases,
        "cases_with_negative_collision_coefficients": cases_with_negative_gamma,
        "q1_hardy_annihilation_cases": q1_annihilation_cases,
        "identity": "0.5*V_minus = sum_even_j Gamma_j/((j-1)*2^(j-1))",
        "first_nonzero_collision_order": 6,
        "r16_even_envelope_closed_form": "2/3 + atanh(1/2)",
        "r16_even_envelope_decimal": kappa2_float,
        "hardy_reachable_tail_closed_form": "atanh(1/2)-1/2 = (ln(3)-1)/2",
        "hardy_reachable_tail_decimal": tail_limit_float,
        "negative_credit_diagnostic": {
            "full_radial_cross_term": str(full_cross_refund),
            "low_half_contribution_cross_term": str(low_cross_refund),
        },
    }
    print(json.dumps(out, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()
