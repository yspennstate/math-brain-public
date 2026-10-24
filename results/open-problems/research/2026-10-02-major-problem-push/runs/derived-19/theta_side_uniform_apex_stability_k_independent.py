#!/usr/bin/env python3
"""Independent exact checks for side-uniform K_{2,3} apex stability.

The apex polynomial is constructed from only the 64 backbone subsets via
their component partitions, not by the author's 2^11 edge-subset routine.
All four Rayleigh-orbit certificates are then derived from that polynomial.
"""

from collections import defaultdict
from fractions import Fraction
from itertools import permutations
from pathlib import Path
from random import Random
import json

import sympy as sp


OUT = Path(__file__).with_name(
    "theta_side_uniform_apex_stability_k_independent_results.json"
)
SEED = 1003202602


def backbone_component_polynomial(p, q, z):
    edges = ([(0, j, p) for j in (2, 3, 4)]
             + [(1, j, q) for j in (2, 3, 4)])
    answer = 0
    accepted = 0
    for mask in range(1 << 6):
        parent = list(range(5))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        weight = 1
        cyclic = False
        for edge, (u, v, activity) in enumerate(edges):
            if not (mask >> edge) & 1:
                continue
            u, v = find(u), find(v)
            if u == v:
                cyclic = True
                break
            parent[u] = v
            weight *= activity
        if cyclic:
            continue
        accepted += 1
        components = defaultdict(list)
        for vertex in range(5):
            components[find(vertex)].append(vertex)
        term = weight
        for component in components.values():
            term *= 1 + sum(z[vertex] for vertex in component)
        answer += term
    return sp.expand(answer), accepted


def rayleigh(polynomial, z, i, j):
    return sp.expand(
        sp.diff(polynomial, z[i]) * sp.diff(polynomial, z[j])
        - polynomial * sp.diff(polynomial, z[i], z[j])
    )


def quadratic_data(polynomial, variable):
    coefficients = sp.Poly(polynomial, variable).all_coeffs()
    assert len(coefficients) == 3
    leading, linear, constant = coefficients
    return tuple(map(sp.expand, (
        leading,
        linear,
        constant,
        linear * linear - 4 * leading * constant,
    )))


def canonical(labels):
    names = {}
    return tuple(names.setdefault(value, len(names)) for value in labels)


def join(partition, u, v):
    if partition[u] == partition[v]:
        return None
    a, b = partition[u], partition[v]
    return canonical(a if value == b else value for value in partition)


def direct_marked(p, q, beta, rows):
    """Return A,E,F,C for two unit-activity marked edges."""
    n = 5
    edges = ([(0, j, Fraction(p)) for j in (2, 3, 4)]
             + [(1, j, Fraction(q)) for j in (2, 3, 4)])
    edges += [
        (n + row, vertex, Fraction(rows[row]) * Fraction(beta[vertex]))
        for row in range(4)
        for vertex in range(n)
        if rows[row] * beta[vertex]
    ]
    states = {tuple(range(n + 4)): Fraction(1)}
    for u, v, weight in edges:
        following = defaultdict(Fraction)
        for partition, mass in states.items():
            following[partition] += mass
            target = join(partition, u, v)
            if target is not None:
                following[target] += weight * mass
        states = dict(following)
    coefficients = [Fraction(0)] * 4
    for partition, mass in states.items():
        for mask in range(4):
            target = partition
            if mask & 1:
                target = join(target, n, n + 1)
            if target is not None and mask & 2:
                target = join(target, n + 2, n + 3)
            if target is not None:
                coefficients[mask] += mass
    return coefficients


def univariate_root_cases(polynomial, p, q, z):
    rng = Random(SEED)
    s = sp.symbols("s", real=True)
    records = []
    for trial in range(24):
        pv = sp.Rational(rng.randrange(1, 8), rng.randrange(1, 6))
        qv = sp.Rational(rng.randrange(1, 8), rng.randrange(1, 6))
        beta = [
            sp.Rational(rng.randrange(0, 7), rng.randrange(1, 6))
            for _ in range(5)
        ]
        if not any(beta):
            beta[trial % 5] = sp.Rational(1)
        value = sp.Poly(
            polynomial.subs({p: pv, q: qv, **{z[i]: s * beta[i] for i in range(5)}}),
            s,
            domain=sp.QQ,
        )
        degree = sum(1 for entry in beta if entry > 0)
        roots = 0
        _, factors = sp.sqf_list(value)
        for factor, multiplicity in factors:
            roots += multiplicity * factor.count_roots(-sp.oo, 0)
        assert value.degree() == degree == roots
        assert all(coefficient > 0 for coefficient in reversed(value.all_coeffs()))
        records.append({
            "trial": trial,
            "p": str(pv),
            "q": str(qv),
            "profile": list(map(str, beta)),
            "degree": degree,
            "negative_roots_counting_multiplicity": int(roots),
            "coefficients_descending": list(map(str, value.all_coeffs())),
        })
    return records


def main():
    p, q = sp.symbols("p q", positive=True)
    z = sp.symbols("z0:5", real=True)
    polynomial, backbone_forests = backbone_component_polynomial(p, q, z)
    assert backbone_forests == 54
    assert len(sp.Poly(polynomial, *z).terms()) == 32
    assert polynomial.subs({p: 1, q: 1, **{value: 1 for value in z}}) == 712
    for coefficient in sp.Poly(polynomial, *z).coeffs():
        assert all(value > 0 for value in sp.Poly(coefficient, p, q).coeffs())

    # Verify the actual fixed-parameter automorphism group used for the
    # four-orbit reduction: every permutation of internal vertices.
    for perm in permutations((2, 3, 4)):
        substitution = {z[source]: z[target] for source, target in zip((2, 3, 4), perm)}
        assert sp.expand(polynomial.xreplace(substitution) - polynomial) == 0
    # Endpoint exchange is available only together with p<->q.
    temporary_p, temporary_z = sp.symbols("temporary_p temporary_z")
    swapped = polynomial.subs({p: temporary_p, q: p, z[0]: temporary_z, z[1]: z[0]})
    swapped = swapped.subs({temporary_p: q, temporary_z: z[1]})
    assert sp.expand(swapped - polynomial) == 0

    h = p + q + 1
    x, y = sp.symbols("x y", real=True)
    phi_a = (p + 1) * (q + 1) * (x*x + y*y) + 2*p*q*x*y
    phi_q = (2*p*q + p + q + 1) * (x*x + y*y) + 2*p*q*x*y
    phi_b = q**2*(q + 1)**2*x*x + 2*p**2*q**2*x*y + p**2*(p + 1)**2*y*y
    phi_r = (3*q**2*(q + 1)**2*x*x
             + 2*p*q*(3*p*q - p - q - 1)*x*y
             + 3*p**2*(p + 1)**2*y*y)

    checks = []
    d01 = rayleigh(polynomial, z, 0, 1)
    a01, _, _, disc01 = quadratic_data(d01, z[2])
    checks += [
        sp.expand(a01 - p*q*phi_a.subs({x: z[3] + h, y: z[4] + h})) == 0,
        sp.expand(disc01 + 4*p**2*q**2*h*(z[3] + h)**2*(z[4] + h)**2
                  * phi_q.subs({x: z[3] + h, y: z[4] + h})) == 0,
        sp.expand(d01.subs({z[3]: -h, z[4]: -h})) == 0,
    ]

    d02 = rayleigh(polynomial, z, 0, 2)
    a02, _, _, disc02 = quadratic_data(d02, z[1])
    checks += [
        sp.expand(a02 - p*(p + 1)*(z[3] + h)**2*(z[4] + h)**2) == 0,
        sp.expand(disc02 + 4*p**2*q**2*h*(z[3] + h)**2*(z[4] + h)**2
                  * phi_q.subs({x: z[3] + h, y: z[4] + h})) == 0,
        sp.expand(d02.subs(z[3], -h) - 2*p*q**2*(q + 1)*h*(z[4] + h)**2) == 0,
        sp.expand(d02.subs(z[4], -h) - 2*p*q**2*(q + 1)*h*(z[3] + h)**2) == 0,
    ]

    d12 = rayleigh(polynomial, z, 1, 2)
    a12, _, _, disc12 = quadratic_data(d12, z[0])
    checks += [
        sp.expand(a12 - q*(q + 1)*(z[3] + h)**2*(z[4] + h)**2) == 0,
        sp.expand(disc12 + 4*p**2*q**2*h*(z[3] + h)**2*(z[4] + h)**2
                  * phi_q.subs({x: z[3] + h, y: z[4] + h})) == 0,
        sp.expand(d12.subs(z[3], -h) - 2*p**2*q*(p + 1)*h*(z[4] + h)**2) == 0,
        sp.expand(d12.subs(z[4], -h) - 2*p**2*q*(p + 1)*h*(z[3] + h)**2) == 0,
    ]

    u0, u1 = z[0] + 3*p + 1, z[1] + 3*q + 1
    d23 = rayleigh(polynomial, z, 2, 3)
    a23, _, _, disc23 = quadratic_data(d23, z[4])
    checks += [
        sp.expand(a23 - phi_b.subs({x: u0, y: u1})) == 0,
        sp.expand(disc23 + 4*p**2*q**2*h**2*phi_r.subs({x: u0, y: u1})) == 0,
        sp.expand(d23.subs({z[0]: -3*p - 1, z[1]: -3*q - 1})
                  - 4*p**2*q**2*h**2) == 0,
    ]

    determinants = {
        "Phi_A": sp.expand((p + 1)**2*(q + 1)**2 - p**2*q**2),
        "Phi_Q": sp.expand((2*p*q + p + q + 1)**2 - p**2*q**2),
        "Phi_B": sp.expand(p**2*q**2*(p + 1)**2*(q + 1)**2 - p**4*q**4),
        "Phi_R": sp.expand(9*p**2*q**2*(p + 1)**2*(q + 1)**2
                           - p**2*q**2*(3*p*q - p - q - 1)**2),
    }
    expected_determinants = {
        "Phi_A": h*(2*p*q + p + q + 1),
        "Phi_Q": (p + 1)*(q + 1)*(3*p*q + p + q + 1),
        "Phi_B": p**2*q**2*h*(2*p*q + p + q + 1),
        "Phi_R": 8*p**2*q**2*h*(3*p*q + p + q + 1),
    }
    checks += [sp.expand(determinants[name] - expected_determinants[name]) == 0
               for name in determinants]
    assert len(checks) == 18 and all(checks)

    root_records = univariate_root_cases(polynomial, p, q, z)
    marked_records = []
    rows = [Fraction(1, 2), Fraction(2, 3), Fraction(3, 4), Fraction(4, 5)]
    cases = [
        (Fraction(1), Fraction(2), [Fraction(1), Fraction(2), 0, 0, 0]),
        (Fraction(2, 3), Fraction(5, 2), [0, Fraction(1), Fraction(3), 0, 0]),
        (Fraction(7, 4), Fraction(1, 5), [0, 0, Fraction(1), Fraction(2), 0]),
        (Fraction(3), Fraction(4), [Fraction(1), 0, 0, 0, Fraction(5)]),
        (Fraction(1), Fraction(3), [Fraction(2), 0, 0, 0, 0]),
        (Fraction(5, 4), Fraction(2), [0, 0, 0, 0, 0]),
    ]
    for pv, qv, beta in cases:
        coefficients = direct_marked(pv, qv, beta, rows)
        difference = coefficients[1]*coefficients[2] - coefficients[0]*coefficients[3]
        strict = sum(value > 0 for value in beta) >= 2
        assert difference >= 0 and (difference > 0) == strict
        marked_records.append({
            "p": str(pv), "q": str(qv), "profile": list(map(str, beta)),
            "A_E_F_C": list(map(str, coefficients)),
            "EF_minus_AC": str(difference), "strict": strict,
        })

    report = {
        "status": "PASS; independent exact component enumeration and symbolic certificates",
        "implementation": "64 backbone subsets and component factors; no author import",
        "sympy_version": sp.__version__,
        "backbone_forests": backbone_forests,
        "apex_polynomial_terms": len(sp.Poly(polynomial, *z).terms()),
        "unit_activity_full_forests": 712,
        "pair_orbits": [[0, 1], [0, 2], [1, 2], [2, 3]],
        "exact_certificate_checks": len(checks),
        "positive_form_determinants": {
            name: str(sp.factor(value)) for name, value in expected_determinants.items()
        },
        "univariate_profile_cases": root_records,
        "direct_marked_cases": marked_records,
        "summary": {
            "exact_certificate_checks": len(checks),
            "exact_univariate_root_cases": len(root_records),
            "direct_marked_cases": len(marked_records),
            "strict_marked_cases": sum(row["strict"] for row in marked_records),
            "equality_marked_cases": sum(not row["strict"] for row in marked_records),
            "counterexamples": 0,
        },
    }
    OUT.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report["summary"], indent=2))


if __name__ == "__main__":
    main()
