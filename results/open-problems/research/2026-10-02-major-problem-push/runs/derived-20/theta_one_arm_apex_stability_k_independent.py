#!/usr/bin/env python3
"""Independent exact checks for one-distinguished-arm K_{2,3} stability.

The polynomial is built from the 64 backbone subsets and their component
factors, independently of the author's 2^11 augmented-subset enumerator.
"""

from collections import defaultdict
from fractions import Fraction
from itertools import product
from pathlib import Path
from random import Random
import json

import sympy as sp


OUT = Path(__file__).with_name(
    "theta_one_arm_apex_stability_k_independent_results.json"
)
SEED = 1003202603


def component_polynomial(t, r, z):
    edges = ([(0, 2, r*t), (0, 3, t), (0, 4, t)]
             + [(1, 2, r*t), (1, 3, t), (1, 4, t)])
    answer, accepted = 0, 0
    for mask in range(64):
        parent = list(range(5))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        weight, cyclic = 1, False
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
    a, b, c = coefficients
    return tuple(map(sp.expand, (a, b, c, b*b - 4*a*c)))


def simultaneous_swap(polynomial, left, right):
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


def direct_marked(t, r, beta, rows):
    n = 5
    edges = [
        (0, 2, Fraction(r*t)), (0, 3, Fraction(t)), (0, 4, Fraction(t)),
        (1, 2, Fraction(r*t)), (1, 3, Fraction(t)), (1, 4, Fraction(t)),
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


def root_cases(polynomial, t, r, z):
    rng = Random(SEED)
    s = sp.symbols("s", real=True)
    records = []
    for trial in range(24):
        tv = sp.Rational(rng.randrange(1, 8), rng.randrange(1, 6))
        rv = sp.Rational(rng.randrange(1, 8), rng.randrange(1, 6))
        beta = [
            sp.Rational(rng.randrange(0, 7), rng.randrange(1, 6))
            for _ in range(5)
        ]
        if not any(beta):
            beta[trial % 5] = 1
        value = sp.Poly(
            polynomial.subs({t: tv, r: rv, **{z[i]: s*beta[i] for i in range(5)}}),
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
            "trial": trial, "t": str(tv), "r": str(rv),
            "profile": list(map(str, beta)), "degree": degree,
            "negative_roots_counting_multiplicity": int(negative),
            "coefficients_descending": list(map(str, value.all_coeffs())),
        })
    return records


def main():
    t, r = sp.symbols("t r", positive=True)
    z = sp.symbols("z0:5", real=True)
    x, y = sp.symbols("x y", real=True)
    polynomial, backbone_forests = component_polynomial(t, r, z)
    assert backbone_forests == 54
    assert len(sp.Poly(polynomial, *z).terms()) == 32
    assert polynomial.subs({t: 1, r: 1, **{entry: 1 for entry in z}}) == 712
    for coefficient in sp.Poly(polynomial, *z).coeffs():
        assert all(value > 0 for value in sp.Poly(coefficient, t, r).coeffs())

    # These generate the fixed-parameter automorphism group.
    assert sp.expand(simultaneous_swap(polynomial, z[0], z[1]) - polynomial) == 0
    assert sp.expand(simultaneous_swap(polynomial, z[3], z[4]) - polynomial) == 0

    h, hs, he = 2*t + 1, 2*r*t + 1, t*(r + 2) + 1
    positive_s = (2*r**2*t**3 + r**2*t**2 + 4*r*t**3 + 4*r*t**2
                  + 2*r*t + 2*t**2 + 2*t + 1)
    phi_a = (t + 1)**2*(x*x + y*y) + 2*t**2*x*y
    alpha_01 = (r*t + t + 1)*(2*r*t**2 + r*t + t + 1)
    beta_01 = t**2*(2*r*t + 1)
    phi_01 = alpha_01*(x*x + y*y) + 2*beta_01*x*y
    phi_03 = ((2*t + 1)*(2*t**2 + 2*t + 1)*x*x
              + 2*r**2*t**2*(2*t + 1)*x*y
              + r**2*(r*t + t + 1)*(2*r*t**2 + r*t + t + 1)*y*y)
    phi_23 = (t + 1)*(r*t + 1)*(x*x + y*y) + 2*r*t**2*x*y
    alpha_e = (r*t + 1)*(2*r*t**2 + 3*r*t + 4*t**2 + 6*t + 3)
    beta_e = (r*t + 2*t + 1)*(2*r*t**2 - r*t - 1)
    phi_e = alpha_e*(x*x + y*y) + 2*beta_e*x*y

    checks = []
    d01 = rayleigh(polynomial, z, 0, 1)
    a01, _, _, disc01 = quadratic_data(d01, z[2])
    checks += [
        sp.expand(a01 - t**2*phi_a.subs({x: z[3] + h, y: z[4] + h})) == 0,
        sp.expand(disc01 + 4*r**2*t**4*(z[3] + h)**2*(z[4] + h)**2
                  * phi_01.subs({x: z[3] + h, y: z[4] + h})) == 0,
        sp.expand(d01.subs({z[3]: -h, z[4]: -h})) == 0,
    ]

    d02 = rayleigh(polynomial, z, 0, 2)
    a02, _, _, disc02 = quadratic_data(d02, z[1])
    checks += [
        sp.expand(a02 - r*t*(r*t + 1)*(z[3] + h)**2*(z[4] + h)**2) == 0,
        sp.expand(disc02 - disc01) == 0,
        sp.expand(d02.subs(z[3], -h)
                  - 2*r*t**3*(t + 1)*(r*t + t + 1)*(z[4] + h)**2) == 0,
        sp.expand(d02.subs(z[4], -h)
                  - 2*r*t**3*(t + 1)*(r*t + t + 1)*(z[3] + h)**2) == 0,
    ]

    d03 = rayleigh(polynomial, z, 0, 3)
    a03, _, _, disc03 = quadratic_data(d03, z[1])
    checks += [
        sp.expand(a03 - t*(t + 1)*(z[2] + hs)**2*(z[4] + h)**2) == 0,
        sp.expand(disc03 + 4*t**4*(z[2] + hs)**2*(z[4] + h)**2
                  * phi_03.subs({x: z[2] + hs, y: z[4] + h})) == 0,
        sp.expand(d03.subs(z[2], -hs)
                  - 2*r**2*t**3*(r*t + 1)*(r*t + t + 1)*(z[4] + h)**2) == 0,
        sp.expand(d03.subs(z[4], -h)
                  - 2*t**3*(t + 1)*(2*t + 1)*(z[2] + hs)**2) == 0,
    ]

    u0, u1 = z[0] + he, z[1] + he
    d23 = rayleigh(polynomial, z, 2, 3)
    a23, _, _, disc23 = quadratic_data(d23, z[4])
    checks += [
        sp.expand(a23 - r*t**2*phi_23.subs({x: u0, y: u1})) == 0,
        sp.expand(disc23 + 4*r**2*t**6*(2*t + 1)*phi_e.subs({x: u0, y: u1})) == 0,
        sp.expand(d23.subs({z[0]: -he, z[1]: -he})
                  - 4*r*t**4*(2*t + 1)*(r*t + t + 1)) == 0,
    ]

    d34 = rayleigh(polynomial, z, 3, 4)
    a34, _, _, disc34 = quadratic_data(d34, z[2])
    checks += [
        sp.expand(a34 - t**2*phi_a.subs({x: u0, y: u1})) == 0,
        sp.expand(disc34 - disc23) == 0,
        sp.expand(d34.subs({z[0]: -he, z[1]: -he})
                  - 4*r**2*t**4*(r*t + t + 1)**2) == 0,
    ]

    determinants = {
        "Phi_A": sp.expand((t + 1)**4 - t**4),
        "Phi_01": sp.expand(alpha_01**2 - beta_01**2),
        "Phi_03": sp.expand(
            (2*t + 1)*(2*t**2 + 2*t + 1)
            * r**2*(r*t + t + 1)*(2*r*t**2 + r*t + t + 1)
            - r**4*t**4*(2*t + 1)**2
        ),
        "Phi_23": sp.expand((t + 1)**2*(r*t + 1)**2 - r**2*t**4),
        "Phi_E": sp.expand(alpha_e**2 - beta_e**2),
    }
    expected = {
        "Phi_A": (2*t + 1)*(2*t**2 + 2*t + 1),
        "Phi_01": (2*t + 1)*(r*t + 1)**2*positive_s,
        "Phi_03": r**2*(t + 1)**2*(2*t + 1)*positive_s,
        "Phi_23": (r*t + t + 1)*(2*r*t**2 + r*t + t + 1),
        "Phi_E": 8*(r*t + t + 1)**2*positive_s,
    }
    checks += [sp.expand(determinants[name] - expected[name]) == 0 for name in determinants]
    assert len(checks) == 22 and all(checks)

    profiles = root_cases(polynomial, t, r, z)
    rows = [Fraction(1, 2), Fraction(2, 3), Fraction(3, 4), Fraction(4, 5)]
    marked_input = [
        (Fraction(1), Fraction(2), [Fraction(1), Fraction(2), 0, 0, 0]),
        (Fraction(2, 3), Fraction(5, 2), [0, Fraction(1), Fraction(3), 0, 0]),
        (Fraction(7, 4), Fraction(1, 5), [0, 0, Fraction(1), Fraction(2), 0]),
        (Fraction(3), Fraction(4), [Fraction(1), 0, 0, 0, Fraction(5)]),
        (Fraction(1), Fraction(3), [Fraction(2), 0, 0, 0, 0]),
        (Fraction(5, 4), Fraction(2), [0, 0, 0, 0, 0]),
    ]
    marked = []
    for tv, rv, beta in marked_input:
        coefficients = direct_marked(tv, rv, beta, rows)
        difference = coefficients[1]*coefficients[2] - coefficients[0]*coefficients[3]
        strict = sum(value > 0 for value in beta) >= 2
        assert difference >= 0 and (difference > 0) == strict
        marked.append({
            "t": str(tv), "r": str(rv), "profile": list(map(str, beta)),
            "A_E_F_C": list(map(str, coefficients)),
            "EF_minus_AC": str(difference), "strict": strict,
        })

    report = {
        "status": "PASS; independent component enumeration and exact certificates",
        "implementation": "64 backbone subsets with component factors; no author import",
        "sympy_version": sp.__version__, "backbone_forests": backbone_forests,
        "apex_polynomial_terms": len(sp.Poly(polynomial, *z).terms()),
        "unit_activity_augmented_forests": 712,
        "pair_orbits": [[0, 1], [0, 2], [0, 3], [2, 3], [3, 4]],
        "exact_certificate_checks": len(checks),
        "positive_form_determinants": {
            name: str(sp.factor(value)) for name, value in expected.items()
        },
        "univariate_profile_cases": profiles,
        "direct_marked_cases": marked,
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
