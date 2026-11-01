#!/usr/bin/env python3
"""Exact finite checks for the record-tilt/reservoir condensation argument.

Uses integers/Fraction only for all PASS assertions; decimals are display only.
No finite test is represented as an asymptotic proof or independent audit.
"""
from __future__ import annotations
from fractions import Fraction as F
from math import factorial, ceil
import json


def power_coefficients(weights: list[int], n: int, degree: int) -> list[int]:
    """Coefficients of (sum weights[j] z**j)**n, assuming weights[0] == 1.

    From F(z) C'(z) = n F'(z) C(z). Exact division is checked.
    """
    if n < 0 or degree < 0 or not weights or weights[0] != 1:
        raise ValueError('Require n, degree >= 0 and w[0] = 1')
    c = [0] * (degree + 1)
    c[0] = 1
    for m in range(1, degree + 1):
        s = sum(((n + 1) * j - m) * weights[j] * c[m - j]
                for j in range(1, min(m, len(weights) - 1) + 1))
        value, remainder = divmod(s, m)
        assert remainder == 0 and value >= 0
        c[m] = value
    return c


def direct_convolution(weights: list, n: int, degree: int) -> list:
    c = [1] + [0] * degree
    for _ in range(n):
        out = [0] * (degree + 1)
        for a, ca in enumerate(c):
            if ca:
                for j in range(min(len(weights) - 1, degree - a) + 1):
                    if weights[j]:
                        out[a+j] += ca * weights[j]
        c = out
    return c


def coefficient_crosschecks() -> int:
    families = [[1, 1], [1, 0, 2], [1, 3, 1, 7],
                [factorial(j) for j in range(9)]]
    count = 0
    for w in families:
        for n in range(1, 7):
            a = power_coefficients(w, n, 12)
            b = direct_convolution(w, n, 12)
            assert a == b
            count += 1
    return count


def allocation_row(n: int, sparse: bool) -> dict:
    m = n - 1
    support = {0, 1}
    j = 2
    while factorial(j) <= m:
        support.add(factorial(j))
        j += 1
    weights = [factorial(j) if (not sparse or j in support) else 0
               for j in range(m + 1)]
    z = power_coefficients(weights, n, m)[m]
    assert z > 0
    threshold = (9*m + 9)//10  # ceil(0.9 m), exactly
    z_small = power_coefficients(weights[:threshold], n, m)[m]
    p_large = F(z-z_small, z)
    p_all = F(n * weights[m], z)
    assert 0 <= p_all <= p_large <= 1
    if sparse and n in (24, 120):
        assert p_large == 0  # m=n-1: the next factorial is NOT available.
    return {'family': 'factorial_sparse' if sparse else 'factorial_full',
            'n': n, 'm': m, 'threshold': threshold,
            'P_max_at_least_threshold': float(p_large),
            'P_max_equals_m': float(p_all),
            'P_max_at_least_threshold_is_exactly_one': p_large == 1,
            'P_max_equals_m_is_exactly_one': p_all == 1,
            'decimal_values_are_rounded': True,
            'all_checks_exact': True}


def finite_reservoir_certificate() -> dict:
    """Verify the finite shifted-record bounds, crossing union, and denominator.

    Synthetic rational tilted weights, not an infinite zero-radius example.
    m_n=floor(3n/2)+(-1)^n has upward increments at most 4.
    Four reservoir boxes fill r in {0,1,2,3} using ones and zeros.
    """
    k, R, b, L = 16, 3, 6, 4
    tau = F(1, 4)
    q = [F(0)] * (k+1)
    q[0], q[1] = F(1), tau
    for j in range(R+1, k):
        q[j] = tau**R / (2**(4*j))
    q[k] = tau**R / k**b
    for j in range(R+1, k+1):
        assert q[j] <= tau**R / j**b
    assert q[k] == tau**R / k**b
    A = sum(q)
    p = [x/A for x in q]
    mean = sum(j*p[j] for j in range(k+1))
    assert sum(p) == 1

    def mass(n: int) -> int:
        return (3*n)//2 + (1 if n % 2 == 0 else -1)

    first, last = L+1, 20
    assert mass(first) < k
    assert all(mass(n+1)-mass(n) <= L for n in range(first, last))
    assert max(mass(n) for n in range(first, last+1)) < 2*k
    max_degree = max(mass(n) for n in range(first, last+1))
    distributions = [direct_convolution(p, s, max_degree)
                     for s in range(last-L)]
    union_bound = F(0)
    best = (F(-1), 0, 0)
    for n in range(first, last+1):
        bulk = distributions[n-L-1]
        for r in range(L):
            target = mass(n)-k-r
            prob = bulk[target] if 0 <= target <= max_degree else F(0)
            union_bound += prob
            if prob > best[0]:
                best = prob, n, r
    terminal = sum(distributions[last-L-1][:mass(last)-k+1])
    assert union_bound >= terminal > 0  # deterministic first-crossing inclusion
    prob, n, r = best
    reservoir = p[1]**r * p[0]**(L-r)
    lower = n * p[k] * reservoir * prob
    denominator = direct_convolution(p, n, mass(n))[mass(n)]
    assert 0 < lower <= denominator  # disjoint choices of the unique size-k box
    return {'k': k, 'R': R, 'b': b, 'L': L, 'tau': str(tau),
            'mean': float(mean), 'chosen_n': n, 'chosen_residual': r,
            'terminal_crossing_probability': float(terminal),
            'sum_of_crossing_atom_probabilities': float(union_bound),
            'denominator_lower_bound_over_exact_denominator': float(lower/denominator),
            'record_envelope': 'PASS', 'crossing_union': 'PASS',
            'disjoint_giant_denominator': 'PASS'}


def parameter_checks() -> list[dict]:
    out = []
    for epsilon in (F(1,2), F(1,4), F(1,10), F(1,100)):
        c = 1-epsilon/2
        padding_mass = 7
        b = ceil(F(4,1)/(1-c)) + 4
        R = ceil(F(2*padding_mass,1)/(1-c)) + 1
        a = (F(b) + (b-2)/c)/2
        v = (F(R+padding_mass) + R/c)/2
        assert b > 3 and a > b and a*c < b-2
        assert v > R+padding_mass and v*c < R
        out.append({'epsilon': str(epsilon), 'a_minus_b': str(a-b),
                    'b_minus_2_minus_ac': str(b-2-a*c),
                    'v_minus_R_minus_padding': str(v-R-padding_mass),
                    'R_minus_vc': str(R-v*c), 'PASS': True})
    return out


def main() -> None:
    result = {'coefficient_recurrence_vs_direct_convolution_cases': coefficient_crosschecks(),
              'parameter_checks': parameter_checks(),
              'finite_reservoir_certificate': finite_reservoir_certificate(),
              'allocation_examples': [allocation_row(n, False) for n in (20,40,80,120)]
                  + [allocation_row(n, True) for n in (24,25,120,121)],
              'status': 'ALL_EXACT_CHECKS_PASS',
              'scope': 'Finite identities and examples only; not an asymptotic proof or independent audit.'}
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
