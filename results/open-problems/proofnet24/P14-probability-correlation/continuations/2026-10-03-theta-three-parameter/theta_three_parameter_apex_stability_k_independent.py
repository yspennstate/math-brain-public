#!/usr/bin/env python3
"""Independent exact checks for the three-parameter K_{2,3} theorem.

Uses backbone-component factors over 64 subsets, not the author's direct
enumeration of all 2^11 augmented-edge subsets.
"""

from collections import defaultdict
from fractions import Fraction
from pathlib import Path
from random import Random
import json

import sympy as sp


OUT = Path(__file__).with_name(
    "theta_three_parameter_apex_stability_k_independent_results.json"
)
SEED = 1003202604


def component_polynomial(p, q, r, z):
    edges = [
        (0, 2, p*r), (0, 3, p), (0, 4, p),
        (1, 2, q*r), (1, 3, q), (1, 4, q),
    ]
    answer, accepted = 0, 0
    for mask in range(64):
        parent = list(range(5))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        weight, cyclic = 1, False
        for index, (u, v, activity) in enumerate(edges):
            if not (mask >> index) & 1:
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
    a, b, c = coefficients
    return tuple(map(sp.expand, (a, b, c, b*b - 4*a*c)))


def swap(polynomial, left, right):
    temporary = sp.Dummy()
    return polynomial.xreplace({left: temporary, right: left}).xreplace({temporary: right})


def canonical(labels):
    names = {}
    return tuple(names.setdefault(value, len(names)) for value in labels)


def join(partition, u, v):
    if partition[u] == partition[v]:
        return None
    a, b = partition[u], partition[v]
    return canonical(a if value == b else value for value in partition)


def direct_marked(p, q, r, beta, rows):
    n = 5
    edges = [
        (0, 2, Fraction(p*r)), (0, 3, Fraction(p)), (0, 4, Fraction(p)),
        (1, 2, Fraction(q*r)), (1, 3, Fraction(q)), (1, 4, Fraction(q)),
    ]
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


def root_cases(polynomial, p, q, r, z):
    rng = Random(SEED)
    s = sp.symbols("s", real=True)
    records = []
    for trial in range(24):
        pv = sp.Rational(rng.randrange(1, 8), rng.randrange(1, 6))
        qv = sp.Rational(rng.randrange(1, 8), rng.randrange(1, 6))
        rv = sp.Rational(rng.randrange(1, 8), rng.randrange(1, 6))
        beta = [
            sp.Rational(rng.randrange(0, 7), rng.randrange(1, 6))
            for _ in range(5)
        ]
        if not any(beta):
            beta[trial % 5] = 1
        value = sp.Poly(
            polynomial.subs({
                p: pv, q: qv, r: rv,
                **{z[i]: s*beta[i] for i in range(5)},
            }),
            s,
            domain=sp.QQ,
        )
        degree = sum(1 for entry in beta if entry > 0)
        negative = 0
        _, factors = sp.sqf_list(value)
        for factor, multiplicity in factors:
            negative += multiplicity * factor.count_roots(-sp.oo, 0)
        assert value.degree() == degree == negative
        assert all(coefficient > 0 for coefficient in value.all_coeffs())
        records.append({
            "trial": trial, "p": str(pv), "q": str(qv), "r": str(rv),
            "profile": list(map(str, beta)), "degree": degree,
            "negative_roots_counting_multiplicity": int(negative),
            "coefficients_descending": list(map(str, value.all_coeffs())),
        })
    return records


def main():
    p, q, r = sp.symbols("p q r", positive=True)
    z = sp.symbols("z0:5", real=True)
    x, y = sp.symbols("x y", real=True)
    polynomial, backbone_forests = component_polynomial(p, q, r, z)
    assert backbone_forests == 54
    assert len(sp.Poly(polynomial, *z).terms()) == 32
    assert polynomial.subs({p: 1, q: 1, r: 1, **{entry: 1 for entry in z}}) == 712
    for coefficient in sp.Poly(polynomial, *z).coeffs():
        assert all(value > 0 for value in sp.Poly(coefficient, p, q, r).coeffs())
    assert sp.expand(swap(polynomial, z[3], z[4]) - polynomial) == 0

    h, hs = p + q + 1, r*(p + q) + 1
    h0, h1 = p*(r + 2) + 1, q*(r + 2) + 1
    parameter_t = (p + q)*(r + 1) + 2
    parameter_n = 2*p*q + p + q + 1
    parameter_l = (
        p**2*q*r**2 + p**2*q*r + p**2*r + p*q**2*r**2 + p*q**2*r
        + p*q*r**2 + 2*p*q*r + p*q + p*r + p + q**2*r + q*r + q + 1
    )
    parameter_m = (
        p**2*q*r**2 + 2*p**2*q*r + p**2*r + p*q**2*r**2 + 2*p*q**2*r
        + p*q*r**2 + 2*p*q*r + 2*p*q + p*r + p + q**2*r + q*r + q + 1
    )

    phi_a = (p + 1)*(q + 1)*(x*x + y*y) + 2*p*q*x*y
    phi_01 = parameter_l*(x*x + y*y) + 2*p*q*hs*x*y
    phi_03 = h*parameter_n*x*x + 2*p*q*r**2*h*x*y + r**2*parameter_l*y*y
    phi_23 = (q**2*r*(q + 1)*(q*r + 1)*x*x
              + 2*p**2*q**2*r**2*x*y
              + p**2*r*(p + 1)*(p*r + 1)*y*y)
    phi_34 = q**2*(q + 1)**2*x*x + 2*p**2*q**2*x*y + p**2*(p + 1)**2*y*y
    eq = p*q*r + 2*p*q + 2*p*r + p + q**2*r + 2*q**2 + q*r + 5*q + 3
    ep = p**2*r + 2*p**2 + p*q*r + 2*p*q + p*r + 5*p + 2*q*r + q + 3
    parameter_k = (p**2*q*r**2 + 2*p**2*q*r - p**2*r
                   + p*q**2*r**2 + 2*p*q**2*r - p*q*r**2 + 2*p*q*r
                   - p*r - p - q**2*r - q*r - q - 1)
    phi_e = (q**2*(q*r + 1)*eq*x*x + 2*p*q*parameter_k*x*y
             + p**2*(p*r + 1)*ep*y*y)

    checks = []
    d01 = rayleigh(polynomial, z, 0, 1)
    a01, _, _, disc01 = quadratic_data(d01, z[2])
    checks += [
        sp.expand(a01 - p*q*phi_a.subs({x: z[3] + h, y: z[4] + h})) == 0,
        sp.expand(disc01 + 4*p**2*q**2*r**2*(z[3] + h)**2*(z[4] + h)**2
                  * phi_01.subs({x: z[3] + h, y: z[4] + h})) == 0,
        sp.expand(d01.subs({z[3]: -h, z[4]: -h})) == 0,
    ]

    for endpoint, other, leading, boundary in [
        (0, 1, p*r*(p*r + 1), p*q**2*r*(q + 1)*parameter_t),
        (1, 0, q*r*(q*r + 1), p**2*q*r*(p + 1)*parameter_t),
    ]:
        difference = rayleigh(polynomial, z, endpoint, 2)
        lead, _, _, discriminant = quadratic_data(difference, z[other])
        checks += [
            sp.expand(lead - leading*(z[3] + h)**2*(z[4] + h)**2) == 0,
            sp.expand(discriminant - disc01) == 0,
            sp.expand(difference.subs(z[3], -h) - boundary*(z[4] + h)**2) == 0,
            sp.expand(difference.subs(z[4], -h) - boundary*(z[3] + h)**2) == 0,
        ]

    for endpoint, other, leading, boundary_special, boundary_ordinary in [
        (0, 1, p*(p + 1), p*q**2*r**2*(q*r + 1)*parameter_t,
         2*p*q**2*(q + 1)*h),
        (1, 0, q*(q + 1), p**2*q*r**2*(p*r + 1)*parameter_t,
         2*p**2*q*(p + 1)*h),
    ]:
        difference = rayleigh(polynomial, z, endpoint, 3)
        lead, _, _, discriminant = quadratic_data(difference, z[other])
        checks += [
            sp.expand(lead - leading*(z[2] + hs)**2*(z[4] + h)**2) == 0,
            sp.expand(discriminant + 4*p**2*q**2*(z[2] + hs)**2*(z[4] + h)**2
                      * phi_03.subs({x: z[2] + hs, y: z[4] + h})) == 0,
            sp.expand(difference.subs(z[2], -hs)
                      - boundary_special*(z[4] + h)**2) == 0,
            sp.expand(difference.subs(z[4], -h)
                      - boundary_ordinary*(z[2] + hs)**2) == 0,
        ]

    u0, u1 = z[0] + h0, z[1] + h1
    d23 = rayleigh(polynomial, z, 2, 3)
    a23, _, _, disc23 = quadratic_data(d23, z[4])
    checks += [
        sp.expand(a23 - phi_23.subs({x: u0, y: u1})) == 0,
        sp.expand(disc23 + 4*p**2*q**2*r**2*h*phi_e.subs({x: u0, y: u1})) == 0,
        sp.expand(d23.subs({z[0]: -h0, z[1]: -h1})
                  - 2*p**2*q**2*r*h*parameter_t) == 0,
    ]

    d34 = rayleigh(polynomial, z, 3, 4)
    a34, _, _, disc34 = quadratic_data(d34, z[2])
    checks += [
        sp.expand(a34 - phi_34.subs({x: u0, y: u1})) == 0,
        sp.expand(disc34 - disc23) == 0,
        sp.expand(d34.subs({z[0]: -h0, z[1]: -h1})
                  - p**2*q**2*r**2*parameter_t**2) == 0,
    ]

    determinants = {
        "Phi_A": sp.expand((p + 1)**2*(q + 1)**2 - p**2*q**2),
        "Phi_01": sp.expand(parameter_l**2 - p**2*q**2*hs**2),
        "Phi_03": sp.expand(h*parameter_n*r**2*parameter_l - p**2*q**2*r**4*h**2),
        "Phi_23": sp.expand(
            q**2*r*(q + 1)*(q*r + 1)*p**2*r*(p + 1)*(p*r + 1)
            - p**4*q**4*r**4
        ),
        "Phi_34": sp.expand(q**2*(q + 1)**2*p**2*(p + 1)**2 - p**4*q**4),
        "Phi_E": sp.expand(
            q**2*(q*r + 1)*eq*p**2*(p*r + 1)*ep - p**2*q**2*parameter_k**2
        ),
    }
    expected = {
        "Phi_A": h*parameter_n,
        "Phi_01": (p*r + 1)*(q*r + 1)*h*parameter_m,
        "Phi_03": r**2*(p + 1)*(q + 1)*h*parameter_m,
        "Phi_23": p**2*q**2*r**2*parameter_l,
        "Phi_34": p**2*q**2*h*parameter_n,
        "Phi_E": 2*p**2*q**2*parameter_t**2*parameter_m,
    }
    checks += [sp.expand(determinants[name] - expected[name]) == 0 for name in determinants]
    assert len(checks) == 31 and all(checks)

    profiles = root_cases(polynomial, p, q, r, z)
    rows = [Fraction(1, 2), Fraction(2, 3), Fraction(3, 4), Fraction(4, 5)]
    marked_input = [
        (Fraction(1), Fraction(2), Fraction(3), [Fraction(1), Fraction(2), 0, 0, 0]),
        (Fraction(2, 3), Fraction(5, 2), Fraction(4, 3), [0, Fraction(1), Fraction(3), 0, 0]),
        (Fraction(7, 4), Fraction(1, 5), Fraction(2), [0, 0, Fraction(1), Fraction(2), 0]),
        (Fraction(3), Fraction(4), Fraction(5, 3), [Fraction(1), 0, 0, 0, Fraction(5)]),
        (Fraction(1), Fraction(3), Fraction(7, 2), [Fraction(2), 0, 0, 0, 0]),
        (Fraction(5, 4), Fraction(2), Fraction(1, 7), [0, 0, 0, 0, 0]),
    ]
    marked = []
    for pv, qv, rv, beta in marked_input:
        coefficients = direct_marked(pv, qv, rv, beta, rows)
        difference = coefficients[1]*coefficients[2] - coefficients[0]*coefficients[3]
        strict = sum(value > 0 for value in beta) >= 2
        assert difference >= 0 and (difference > 0) == strict
        marked.append({
            "p": str(pv), "q": str(qv), "r": str(rv),
            "profile": list(map(str, beta)), "A_E_F_C": list(map(str, coefficients)),
            "EF_minus_AC": str(difference), "strict": strict,
        })

    report = {
        "status": "PASS; independent component reconstruction and exact certificates",
        "implementation": "64 backbone subsets with component factors; no author import",
        "sympy_version": sp.__version__, "backbone_forests": backbone_forests,
        "apex_polynomial_terms": len(sp.Poly(polynomial, *z).terms()),
        "unit_activity_augmented_forests": 712,
        "pair_orbits": [[0, 1], [0, 2], [1, 2], [0, 3], [1, 3], [2, 3], [3, 4]],
        "exact_certificate_checks": len(checks),
        "positive_form_determinants": {
            name: str(sp.factor(value)) for name, value in expected.items()
        },
        "univariate_profile_cases": profiles, "direct_marked_cases": marked,
        "summary": {
            "exact_certificate_checks": len(checks),
            "exact_univariate_root_cases": len(profiles),
            "direct_marked_cases": len(marked),
            "strict_marked_cases": sum(row["strict"] for row in marked),
            "equality_marked_cases": sum(not row["strict"] for row in marked),
            "counterexamples": 0,
        },
    }
    OUT.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report["summary"], indent=2))


if __name__ == "__main__":
    main()
